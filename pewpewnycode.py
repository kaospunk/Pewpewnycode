#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pewpewnycode.py
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the project nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#  author: Brandon Knight (kaospunk)

import sys
import itertools
import argparse

a_glyphs = [
         0x61, 0xc0, 0xc1, 0xc2, 0xc3, 0xc4, 0xc5, 0xe0, 0xe1, 0xe2,
         0xe3, 0xe4, 0xe5, 0x251
         ]
b_glyphs = [
         0x62, 0x299
         ]
c_glyphs = [
         0x63
         ]
d_glyphs = [
         0x64, 0x10e, 0x10f, 0x110, 0x111, 0x56a, 0x13a0
         ]
e_glyphs = [
         0x65, 0xc8, 0xc9, 0xca, 0xcb, 0xe9, 0xea, 0xeb, 0x112, 0x113,
         0x114, 0x115, 0x116, 0x117, 0x118, 0x11a, 0x11b
         ]
f_glyphs = [
         0x66
         ]
g_glyphs = [
         0x67, 0x261, 0x262
         ]
h_glyphs = [
         0x68, 0x29c
         ]
i_glyphs = [
         0x69, 0x6c, 0x269
         ]
j_glyphs = [
         0x6a
         ]
k_glyphs = [
         0x6b
         ]
l_glyphs = [
         0x6c, 0x29f
         ]
m_glyphs = [
         0x6d
         ]
n_glyphs = [
         0x6e, 0x274
         ]
o_glyphs = [
         0x6f, 0x30
         ]
p_glyphs = [
         0x70
         ]
q_glyphs = [
         0x71
         ]
r_glyphs = [
         0x72, 0x280
         ]
s_glyphs = [
         0x73
         ]
t_glyphs = [
         0x74
         ]
u_glyphs = [
         0x75
         ]
v_glyphs = [
         0x76
         ]
w_glyphs = [
         0x77
         ]
x_glyphs = [
         0x78
         ]
y_glyphs = [
         0x79, 0x28f
         ]
z_glyphs = [
         0x7a
         ]

lookup = {
        'a': a_glyphs, 'b': b_glyphs, 'c': c_glyphs, 'd': d_glyphs,
        'e': e_glyphs, 'f': f_glyphs, 'g': g_glyphs, 'h': h_glyphs,
        'i': i_glyphs, 'j': j_glyphs, 'k': k_glyphs, 'l': l_glyphs,
        'm': m_glyphs, 'n': n_glyphs, 'o': o_glyphs, 'p': p_glyphs,
        'q': q_glyphs, 'r': r_glyphs, 's': s_glyphs, 't': t_glyphs,
        'u': u_glyphs, 'v': v_glyphs, 'w': w_glyphs, 'x': x_glyphs,
        'y': y_glyphs, 'z': z_glyphs
        }


def add_uppers():
    a_glyphs.append(0x41)
    b_glyphs.append(0x42)
    c_glyphs.append(0x43)
    d_glyphs.append(0x44)
    e_glyphs.append(0x45)
    f_glyphs.append(0x46)
    g_glyphs.append(0x47)
    h_glyphs.append(0x48)
    i_glyphs.append(0x49)
    j_glyphs.append(0x4a)
    k_glyphs.append(0x4b)
    l_glyphs.append(0x4c)
    m_glyphs.append(0x4d)
    n_glyphs.append(0x4e)
    o_glyphs.append(0x4f)
    p_glyphs.append(0x50)
    q_glyphs.append(0x51)
    r_glyphs.append(0x52)
    s_glyphs.append(0x53)
    t_glyphs.append(0x54)
    u_glyphs.append(0x55)
    v_glyphs.append(0x56)
    w_glyphs.append(0x57)
    x_glyphs.append(0x58)
    y_glyphs.append(0x59)
    z_glyphs.append(0x5a)


if __name__ == '__main__':
    if sys.version_info[0] != 3:
        print('This script requires Python version 3')
        sys.exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='domain',
                        help='Domain to enumerate homoglpyhs for without the TLD',
                        required=True)
    parser.add_argument('-u', dest='uppers', action="store_true",
                        help='Use upper case ascii characters as well',
                        default=False)
    parser.add_argument('-t', dest='tld', required=False, default='com')
    args = parser.parse_args()
    domain = args.domain

    if args.uppers:
        add_uppers()

    multi_arr = []

    for i in range(0, len(domain)):
        if domain[i] in lookup:
            multi_arr.append(lookup[domain[i]])
        else:
            multi_arr.append([ord(domain[i])])

    for arr in list(itertools.product(*multi_arr)):
        result = []
        for c in arr:
            result.append(chr(c))
        print("{0}.{1}".format(''.join(result),args.tld))
