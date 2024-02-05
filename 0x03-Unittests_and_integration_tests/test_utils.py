#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from typing import (
    Dict,
    Mapping,
    Sequence,
    Union
)
from utils import (
    access_nested_map,
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
