from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action.include_vars import ActionModule as IncludeVars
from ansible.plugins.action import ActionBase

class ActionModule(IncludeVars):
    def run(self, tmp=None, task_vars=None):
        result = super(ActionModule, self).run(tmp, task_vars)
        return result
