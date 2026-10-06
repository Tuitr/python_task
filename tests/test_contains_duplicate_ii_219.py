from problems.contains_duplicate_ii_219 import containsNearbyDuplicate


def test_duplicate_within_k():
    assert containsNearbyDuplicate([1, 2, 3, 1], 3) is True


def test_adjacent_duplicate():
    assert containsNearbyDuplicate([1, 0, 1, 1], 1) is True


def test_duplicates_too_far():
    assert containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) is False