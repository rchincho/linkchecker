# -*- coding: iso-8859-1 -*-
# Copyright (C) 2005-2009 Bastian Kleineidam
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""
Locking utility class.
"""
import threading
from . import log, LOG_THREAD

def get_lock (name):
    return threading.Lock()
    # for thread debugging, use the DebugLock wrapper
    #return DebugLock(threading.Lock(), name)


class DebugLock (object):
    """Debugging lock class."""
    def __init__ (self, lock, name):
        self.lock = lock
        self.name = name

    def acquire (self, blocking=1):
        """Acquire lock."""
        threadname = threading.currentThread().getName()
        log.debug(LOG_THREAD, "Acquire %s for %s", self.name, threadname)
        self.lock.acquire(blocking)
        log.debug(LOG_THREAD, "...acquired %s for %s", self.name, threadname)

    def release (self):
        """Release lock."""
        threadname = threading.currentThread().getName()
        log.debug(LOG_THREAD, "Release %s for %s", self.name, threadname)
        self.lock.release()
