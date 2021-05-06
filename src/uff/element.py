from dataclasses import dataclass 
from uff.transform import Transform
from uff.element_geometry import ElementGeometry
from uff.impulse_response import ImpulseResponse


@dataclass
class Element:
    """UFF class to define an ultrasonic element

    Notes:

        The class describe an ultrasonic element with a given geometry 
        and impulse response, located at a given location in space. 
        The element_geometry defines the geometry of the elements that
        have unique geometry (i.e. in a linear array element_geometry 
        will have size 1) and unique impulse response.
    """
    transform: Transform
    element_geometery: ElementGeometry
    impulse_response: ImpulseResponse
    