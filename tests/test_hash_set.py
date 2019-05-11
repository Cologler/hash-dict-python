# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from pytest import raises

from hash_dict import HashSet, StringComparers

def test_hashdict_empty():
    test_set = HashSet()
    assert len(test_set) == 0
    assert list(test_set) == []

def test_hashdict_default():
    test_set = HashSet()
    test_set.add('a')
    assert len(test_set) == 1
    assert list(test_set) == ['a']
    assert 'a' in test_set

def test_hashdict_str_ignorecase():
    test_set = HashSet(StringComparers.IgnoreCaseComparer)
    test_set.add('a')
    assert len(test_set) == 1
    assert list(test_set) == ['a']

    assert 'a' in test_set
    assert 'A' in test_set
