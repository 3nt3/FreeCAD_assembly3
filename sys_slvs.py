from .system import System, SystemBase, SystemExtension
from .utils import syslogger as logger, objName
from .py_slvs import slvs

class SystemSlvs(SystemBase):
    __metaclass__ = System
    _id = 1

    def __init__(self,obj):
        super(SystemSlvs,self).__init__(obj)

    @classmethod
    def getName(cls):
        return 'SolveSpace'

    def isDisabled(self,_obj):
        return False

    def getSystem(self,_obj):
        return _SystemSlvs(self.log)


class _SystemSlvs(slvs.System, SystemExtension):
    def __init__(self,log):
        super(_SystemSlvs,self).__init__()
        self.log = log

    def solve(self, group=0, reportFailed=False):
        ret = super(_SystemSlvs,self).solve(group,reportFailed)
        if ret:
            if ret==1:
                reason = 'inconsistent constraints'
            elif ret==2:
                reason = 'not converging'
            elif ret==3:
                reason = 'too many unknowns'
            elif ret==4:
                reason = 'init failed'
            elif ret==5:
                reason = 'redundent constraints'
            else:
                reason = 'unknown failure'
            raise RuntimeError(reason)
        self.log('dof remaining: {}'.format(self.Dof))
