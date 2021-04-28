from dataclasses import dataclass 
from transform import Transform
from element import Element
from element_geometry import ElementGeometry
from impulse_response import ImpulseResponse


@dataclass
class Probe:
    """
    Describes an generic ultrsound probe formed by a collection of elements.

    Note:

    Where focal_length specifies the lens focusing distance. Note that the 
    elements in element_geometry and impulse_response are referred by the 
    fields inside each member in element, avoiding unnecessary replication 
    of information.

    More compact, although less general, descriptions are available for:

        uff.probe.linear_array,
        uff.probe.curvilinear_array, and
        uff.probe.matrix_array.
    """
    
    transform: Transform 
    element: Element
    focal_length: float = None
    element_impulse_response: list[ImulseResponse]
