"""A collection of basic metrics coming from the database that are 
generated by Cyclus itself.
"""
from __future__ import print_function, unicode_literals

from cymetric.evaluator import register_metric

def _genrootclass(name):
    class Cls(object):
        dependencies = ()

        @property
        def schema(self):
            if self._schema is not None:
                return
            # fill in schema code

        @property
        def name(self):
            return self.__class__.__name__
            
        def __init__(self, db):
            self._schema = None
            self.db = db

        def __call__(self, *args, **kwargs):
            return self.db.query(self.name)

    Cls.__name__ = str(name)
    register_metric(Cls)
    return Cls


def root_metric(obj=None, name=None, schema=None, *args, **kwargs):
    if obj is not None:
        raise RuntimeError
    if name is None:
        raise RuntimeError
    return _genrootclass(name=name)


resources = root_metric(name='Resources')
compositions = root_metric(name='Compositions')
recipes = root_metric(name='Recipes')
products = root_metric(name='Products')
res_creators = root_metric(name='ResCreators')
agent_entry = root_metric(name='AgentEntry')
agent_exit = root_metric(name='AgentExit')
transactions = root_metric(name='Transactions')
info = root_metric(name='Info')
finish = root_metric(name='Finish')
input_files = root_metric(name='InputFiles')
decom_schedule = root_metric(name='DecomSchedule')
build_schedule = root_metric(name='BuildSchedule')
snapshots = root_metric(name='Snapshots')
debug_requests = root_metric(name='DebugRequests')
debug_bids = root_metric(name='DebugBids')
