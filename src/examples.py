"""
Example of how to create units and scales
"""

from unit.scale import Scale
from unit.Unit import Unit


class Length(Unit):
    pass

class Time(Unit):
    pass

Length.add_scale(Scale("metre", "m", factor=1.0), is_base=True)
Length.add_scale(Scale("foot", "ft", factor=0.3048))

Time.add_scale(Scale("second", "s", factor=1.0), is_base=True)

ms = Annotated[float, "m,s^-1"]
fts = Annotated[float, "ft,s-1"]
m = Annotated[float, "m"]
ft = Annotated[float, "ft"]
s = Annotated[float, "s"]

def average_speed_auto_scale(distance: ft, time: s) -> ms:
    speed_fts: fts = distance / time
    return speed_fts # This will be automatically fixed by linter in --fix mode

def average_speed_wrong_units(distance: m, time: s) -> ms:
    return distance / (time**2) # This will raise an error

@scilint.scale_convert(fts, ms)
def your_conversion_function(fts: fts) -> ms:
    """no need to explicitly type from this point
    the decorator means to trust without investigation
    """
    # return answer
    pass

def average_speed_pre_converted(distance: ft, time: s) -> ms:
    return your_conversion_function(distance / time) # no errors raised
