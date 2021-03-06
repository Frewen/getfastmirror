#!/usr/bin/env python
# -*- encoding=utf8 -*-
#
# Copyright © 2010 Canonical Ltd.
#
# Author Hsin-Yi Chen
#
# This is a free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# This software is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this software; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA 02111-1307 USA

import os
import unittest
import shutil
import tempfile

from getfastmirror import sourceslist

class SourcesListTestCase(unittest.TestCase):

    #{{{def setUp(self):
    def setUp(self):
        self.tmpdir = os.path.join(tempfile.gettempdir(), 'getfastboot')
        self.rulesdir = os.path.join(self.tmpdir, 'filters')
        self.datadir = os.path.join(os.path.dirname(__file__), 'data')
        os.system('cp -r %s  %s' % (self.datadir, self.tmpdir))
        self.sourceslist = sourceslist.SourcesList()
    #}}}

    #{{{def tearDown(self):
    def tearDown(self):
        shutil.rmtree(self.tmpdir)
    #}}}

    #{{{def test_refresh(self):
    def test_refresh(self):
        self.sourceslist.refresh(self.tmpdir)
        self.assertEquals(self.sourceslist.list[0].file,
                    os.path.join(self.tmpdir, 'sources.list'))
    #}}}

    #{{{def test_filters(self):
    def test_filters(self):
        rulepath = os.path.join(self.rulesdir, 'test_rules.ini')
        self.sourceslist.refresh(self.tmpdir)
        self.sourceslist.apply_filters(sourceslist.RulesList(rulepath))
        self.sourceslist.save()
        ret = open(os.path.join(self.tmpdir, 'sources.list'), 'r').read().split('\n')
        self.assertEquals(testreulst__applyfilters, ret)
    #}}}
pass

def suite():
    return unittest.makeSuite(SourcesListTestCase, 'test')

#{{{TEST RESULTS
testreulst__applyfilters = [
"# deb cdrom:[Ubuntu 10.04 LTS _Lucid Lynx_ - Release i386 (20100429)]/ lucid main restricted",
"# See http://help.ubuntu.com/community/UpgradeNotes for how to upgrade to",
"# newer versions of the distribution.",
"",
"deb http://archive.ubuntu.com/ubuntu/ lucid main restricted",
"deb-src http://archive.ubuntu.com/ubuntu/ lucid main restricted",
"",
"## Major bug fix updates produced after the final release of the",
"## distribution.",
"# deb http://archive.ubuntu.com/ubuntu/ lucid-updates main restricted",
"# deb-src http://archive.ubuntu.com/ubuntu/ lucid-updates main restricted",
"",
"## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu",
"## team. Also, please note that software in universe WILL NOT receive any",
"## review or updates from the Ubuntu security team.",
"deb http://archive.ubuntu.com/ubuntu/ lucid universe",
"deb-src http://archive.ubuntu.com/ubuntu/ lucid universe",
"# deb http://archive.ubuntu.com/ubuntu/ lucid-updates universe",
"# deb-src http://archive.ubuntu.com/ubuntu/ lucid-updates universe",
"",
"## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu",
"## team, and may not be under a free licence. Please satisfy yourself as to",
"## your rights to use the software. Also, please note that software in",
"## multiverse WILL NOT receive any review or updates from the Ubuntu",
"## security team.",
"deb http://archive.ubuntu.com/ubuntu/ lucid multiverse",
"deb-src http://archive.ubuntu.com/ubuntu/ lucid multiverse",
"# deb http://archive.ubuntu.com/ubuntu/ lucid-updates multiverse",
"# deb-src http://archive.ubuntu.com/ubuntu/ lucid-updates multiverse",
"",
"## Uncomment the following two lines to add software from the 'backports'",
"## repository.",
"## N.B. software from this repository may not have been tested as",
"## extensively as that contained in the main release, although it includes",
"## newer versions of some applications which may provide useful features.",
"## Also, please note that software in backports WILL NOT receive any review",
"## or updates from the Ubuntu security team.",
"# deb http://archive.ubuntu.com/ubuntu/ lucid-backports main restricted universe multiverse",
"# deb-src http://archive.ubuntu.com/ubuntu/ lucid-backports main restricted universe multiverse",
"",
"## Uncomment the following two lines to add software from Canonical's",
"## 'partner' repository.",
"## This software is not part of Ubuntu, but is offered by Canonical and the",
"## respective vendors as a service to Ubuntu users.",
"# deb http://archive.canonical.com/ubuntu lucid partner",
"# deb-src http://archive.canonical.com/ubuntu lucid partner",
"",
"# deb http://security.ubuntu.com/ubuntu lucid-security main restricted",
"# deb-src http://security.ubuntu.com/ubuntu lucid-security main restricted",
"# deb http://security.ubuntu.com/ubuntu lucid-security universe",
"# deb-src http://security.ubuntu.com/ubuntu lucid-security universe",
"# deb http://security.ubuntu.com/ubuntu lucid-security multiverse",
"# deb-src http://security.ubuntu.com/ubuntu lucid-security multiverse",
'']
#}}}

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
