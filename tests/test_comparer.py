# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from pytest import raises

from hash_dict import HashDict
from hash_dict.comparer import (
    AnyComparer, ObjectComparer
)

def test_any_comparer():
    d = {}
    with raises(TypeError, match='unhashable type'):
        d[{}] = 1
    assert len(d) == 0

    hd = HashDict(AnyComparer.instance)
    hd[d] = 15
    assert hd[d] == 15
    assert hd[{}] == 15 # oh, wtf
    d['k'] = 'v'
    assert hd[d] == 15
    assert hd[{'k': 'v'}] == 15 # oh, no!
    with raises(KeyError):
        hd[{}]
        
    hd[None] = 10
    assert hd[None] == 10

def test_obj_comparer():
    s = HashDict(ObjectComparer())
    s[0] = 15
    assert s[0] == 15
    