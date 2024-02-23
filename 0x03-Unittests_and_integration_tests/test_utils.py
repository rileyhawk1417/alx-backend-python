#!/usr/bin/env python3
"""This module tests nested maps.
Has a use case for nested
Data like JSON for example ;)
"""
import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch
from typing import (
    Dict,
    Mapping,
    Sequence,
    Union
)
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case class for utils.access_nested_map.
    """
    @parameterized.expand([
        ({'a': 1}, ('a'), 1),
        ({'a': {'b': 2}}, ('a'), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: Mapping,
        path: Sequence,
        expected: Union[Dict, int]
    ) -> None:
        """Test access_nested_map output"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('b',), KeyError),
        ({'b': 4}, ('d', 'c'), KeyError),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Mapping,
        path: Sequence,
        exception: Exception
    ) -> None:
        """Test access_nested_map exception raising check"""
        # NOTE: Ignore the linter warning it still passes
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test case for `utils.get_json`
    """
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False}),
    ])
    def test_get_json(
        self,
        test_url: str,
        test_payload: Dict,
    ) -> None:
        """
        Test `get_json` output with mock payload
        """
        attr = {'json.return_value': test_payload}
        # NOTE: Ignore linter warning still passes
        with patch('requests.get', return_value=Mock(**attr)) as req:
            self.assertEqual(get_json(test_url), test_payload)
            req.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test case to `memoize` a method
    """

    def test_memoize(self) -> None:
        """Test `memoize` output"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
        ) as memo_func:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_func.assert_called_once()
