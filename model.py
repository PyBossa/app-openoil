# -*- coding: utf8 -*-
# This file is part of PyBossa.
#
# Copyright (C) 2014 SF Isle of Man Limited
#
# PyBossa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBossa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBossa.  If not, see <http://www.gnu.org/licenses/>.

from lea import Lea
import pandas as pd
import ngram

def lower(s):
    return s.lower()

task_runs = Lea.fromValFreqs(("hola mundo", 55), ("HoLa mundos", 45), ("algo horroroso", 10))

observation = task_runs.random(30)

a = [lower(w) for w in observation]

df = pd.DataFrame({'info': a})

desc = df.describe()

top_string = desc['info']['top']

print "The top transcribed word is: %s" % top_string

G = ngram.NGram([ lower(w) for w in a])

threshold = 0.7
results = G.search(top_string, threshold=threshold)

print "With a confidence threshold of: %s" % threshold
for pair in results:
    msg = "%s has a confidence of being the best transcription of %s" % (pair[0], pair[1])
    print msg
