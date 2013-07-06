from .exceptions import CheckError

def check_required(required, attributes):
    """Check attributes satisfy required."""

    if   isinstance(required, list):
        return any([check_required(x, attributes) for x in required])
    elif isinstance(required, tuple):
        return all([check_required(x, attributes) for x in required])
    elif isinstance(required, dict):
        return all([key not in attributes
                    or (key in attributes
                        and check_required(required[key], attributes))
                    for key in required])
    else:
        return required in attributes
