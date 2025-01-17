import json
import numpy as np
from datetime import datetime
from decimal import Decimal

class json_serialize(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        self.type_handlers = {
            np.integer: lambda x: int(x),
            np.floating: lambda x: float(x),
            np.ndarray: lambda x: x.tolist(),
            datetime: lambda x: x.isoformat(),
            Decimal: lambda x: float(x),
            set: lambda x: list(x)
        }
        super().__init__(*args, **kwargs)
    
    def default(self, obj):
        for type_, handler in self.type_handlers.items():
            if isinstance(obj, type_):
                return handler(obj)
        
        if hasattr(obj, 'to_dict'):
            return obj.to_dict()
        
        return super().default(obj)