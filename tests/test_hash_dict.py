# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from pytest import raises

from hash_dict import HashDict, StringComparers, IEqualityComparer

def test_hashdict_empty():
    test_dict = HashDict()
    assert len(test_dict) == 0
    assert list(test_dict) == []

def test_hashdict_default():
    test_dict = HashDict()
    test_dict['a'] = 1
    assert len(test_dict) == 1
    assert list(test_dict) == ['a']

    assert test_dict['a'] == 1
    with raises(KeyError):
        test_dict['A']

def test_hashdict_str_ignorecase():
    test_dict = HashDict(StringComparers.IgnoreCaseComparer)
    test_dict['a'] = 1
    assert len(test_dict) == 1
    assert list(test_dict) == ['a']

    assert test_dict['a'] == 1
    assert test_dict['A'] == 1
