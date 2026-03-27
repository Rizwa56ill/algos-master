"""
Tests for Bubble Sort Algorithm
"""

import pytest
from bubble_sort import bubble_sort


def test_bubble_sort_empty_list():
    """Test sorting an empty list"""
    assert bubble_sort([]) == []


def test_bubble_sort_single_element():
    """Test sorting a list with single element"""
    assert bubble_sort([5]) == [5]


def test_bubble_sort_already_sorted():
    """Test sorting an already sorted list"""
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_bubble_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_bubble_sort_random_order():
    """Test sorting a randomly ordered list"""
    assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]


def test_bubble_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    assert bubble_sort([3, 3, 1, 1, 2, 2]) == [1, 1, 2, 2, 3, 3]


def test_bubble_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    assert bubble_sort([-3, -1, -5, -2, -4]) == [-5, -4, -3, -2, -1]


def test_bubble_sort_mixed_numbers():
    """Test sorting a list with mixed positive and negative numbers"""
    assert bubble_sort([3, -1, 4, -5, 2, 0]) == [-5, -1, 0, 2, 3, 4]
