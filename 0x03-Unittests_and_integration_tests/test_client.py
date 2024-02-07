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
