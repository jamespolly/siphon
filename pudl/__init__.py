# use __init__.py to setup the namespace

from . import tds

__all__ = ['tds']
# will be able to call things in tds using pudl
#    import pudl
#    pudl.tds