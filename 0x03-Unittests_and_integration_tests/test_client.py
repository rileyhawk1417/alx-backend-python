#!/usr/bin/env python3
"""This module tests clients.
Clients could be 3rd party services.
Github, Google provide OAuth services.
They could be considered clients.
"""

import unittest
from unittest.mock import (
    MagicMock,
    PropertyMock,
    patch
)
from typing import Dict
from parameterized import parameterized
from client import GithubOrgClient

repo_payload = {
    'repos_url': 'https://api.github.com/users/google/repos',
    'repos': [
        {
            "id": 7697149,
            "name": "episodes.dart",
            "full_name": "google/episodes.dart",
            "private": False,
            "owner": {
                "login": "google",
                "id": 1342004,
            },
            "fork": False,
            "url": "https://api.github.com/repos/google/episodes.dart",
            "created_at": "2013-01-19T00:31:37Z",
            "updated_at": "2019-09-23T11:53:58Z",
            "has_issues": True,
            "forks": 22,
            "default_branch": "master",
        },
        {
            "id": 7776515,
            "node_id": "MDEwOlJlcG9zaXRvcnk3Nzc2NTE1",
            "name": "cpp-netlib",
            "private": False,
            "owner": {
                "login": "google",
                "id": 1342004,
            },
            "fork": True,
            "url": "https://api.github.com/repos/google/cpp-netlib",
            "has_issues": False,
            "forks": 59,
            "default_branch": "master",
        },
    ]
}


class TestGithubOrgClient(unittest.TestCase):
    """Test case for `GithubOrgClient`"""
    @parameterized.expand([
        ('google', {'login': 'google'}),
        ('abc', {'login': 'abc'}),
    ])
    @patch(
        'client.get_json'
    )
    def test_org(self, org: str, res: Dict, mocked_func: MagicMock) -> None:
        """Test org method of the api"""
        mocked_func.return_value = MagicMock(return_value=res)
        gh_client = GithubOrgClient(org)
        self.assertEqual(gh_client.org(), res)
        mocked_func.assert_called_once_with(
            f'https://api.github.com/orgs{org}'
        )

    def test_public_repos_url(self) -> None:
        """Test public repos api method"""
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock
        ) as prop_mock:
            prop_mock.return_value = {
                'repos_url': 'https://api.github.com/users/google/repos'
            }
            self.assertEqual(
                GithubOrgClient('google')._public_repos_url,
                'https://api.github.com/users/google/repos'
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Test the public repo method"""
        test_payload = repo_payload
        mock_get_json.return_value = test_payload['repos']
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as res:
            res.return_value = test_payload['repos_url']
            self.assertEqual(
                GithubOrgClient('google').public_repos(),
                [
                    'episodes.dart'
                    'cpp-netlib'
                ],
            )
            res.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'bsd-3-clause'}}, 'bsd-3-clause', True),
        ({'license': {'key': 'bsl-1.0'}}, 'bsd-3-clause', False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """Test the license method"""
        gh_client = GithubOrgClient('google')
        has_license = gh_client.has_license(repo, key)
        self.assertEqual(has_license, expected)
