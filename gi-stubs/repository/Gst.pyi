# Stubs for gi.overrides.Gst (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

long = int

class Bin(Gst.Bin):
    def __init__(self, name: Optional[Any] = ...) -> None: ...
    def add(self, *args: Any) -> None: ...

class Caps(Gst.Caps):
    def __nonzero__(self): ...
    def __new__(cls, *args: Any): ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __getitem__(self, index: Any): ...
    def __len__(self): ...

class Pad(Gst.Pad):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def set_chain_function(self, func: Any) -> None: ...
    def set_event_function(self, func: Any) -> None: ...
    def set_query_function(self, func: Any) -> None: ...
    def set_query_function_full(self, func: Any, udata: Any) -> None: ...
    def query_caps(self, filter: Optional[Any] = ...): ...
    def link(self, pad: Any): ...

class GhostPad(Gst.GhostPad):
    def __init__(self, name: Any, target: Optional[Any] = ..., direction: Optional[Any] = ...) -> None: ...
    def query_caps(self, filter: Optional[Any] = ...): ...

class IteratorError(Exception): ...
class AddError(Exception): ...
class LinkError(Exception): ...

class Iterator(Gst.Iterator):
    def __iter__(self) -> None: ...

class ElementFactory(Gst.ElementFactory):
    def get_longname(self): ...
    def get_description(self): ...
    def get_klass(self): ...
    @classmethod
    def make(cls, factory_name: Any, instance_name: Optional[Any] = ...): ...

class Pipeline(Gst.Pipeline):
    def __init__(self, name: Optional[Any] = ...) -> None: ...

class Structure(Gst.Structure):
    def __new__(cls, *args: Any, **kwargs: Any): ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __getitem__(self, key: Any): ...
    def keys(self): ...
    def __setitem__(self, key: Any, value: Any): ...

class Fraction(Gst.Fraction):
    num: Any = ...
    denom: Any = ...
    type: str = ...
    def __init__(self, num: Any, denom: int = ...) -> None: ...
    def __value__(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def __mul__(self, other: Any): ...
    __rmul__: Any = ...
    def __truediv__(self, other: Any): ...
    __div__: Any = ...
    def __rtruediv__(self, other: Any): ...
    __rdiv__: Any = ...
    def __float__(self): ...

class IntRange(Gst.IntRange):
    range: Any = ...
    def __init__(self, r: Any) -> None: ...
    def __eq__(self, other: Any): ...

class Int64Range(Gst.Int64Range):
    range: Any = ...
    def __init__(self, r: Any) -> None: ...
    def __eq__(self, other: Any): ...

class Bitmask(Gst.Bitmask):
    v: Any = ...
    def __init__(self, v: Any) -> None: ...
    def __eq__(self, other: Any): ...

class DoubleRange(Gst.DoubleRange):
    start: Any = ...
    stop: Any = ...
    def __init__(self, start: Any, stop: Any) -> None: ...

class FractionRange(Gst.FractionRange):
    start: Any = ...
    stop: Any = ...
    def __init__(self, start: Any, stop: Any) -> None: ...

class ValueArray(Gst.ValueArray):
    array: Any = ...
    def __init__(self, array: Any) -> None: ...
    def __getitem__(self, index: Any): ...
    def __setitem__(self, index: Any, value: Any) -> None: ...
    def __len__(self): ...

class ValueList(Gst.ValueList):
    array: Any = ...
    def __init__(self, array: Any) -> None: ...
    def __getitem__(self, index: Any): ...
    def __setitem__(self, index: Any, value: Any) -> None: ...
    def __len__(self): ...

def TIME_ARGS(time: Any): ...

class NotInitialized(Exception): ...