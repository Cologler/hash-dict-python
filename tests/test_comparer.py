# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from pytest import raises

from hash_dict import HashDict

def test_any_comparer():
    d = {}
    with raises(TypeError, match='unhashable type'):
        d[{}] = 1
    assert len(d) == 0

    from hash_dict import AnyComparer

    hd = HashDict(AnyComparer.instance)
    hd[d] = 15
    assert hd[d] == 15
    assert hd[{}] == 15 # oh, wtf
    d['k'] = 'v'
    assert hd[d] == 15
    assert hd[{'k': 'v'}] == 15 # oh, no!
    with raises(KeyError):
        hd[{}]