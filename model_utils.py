def convert_target(value):
    """Convert bank marketing target into binary format."""
    if value == "yes":
        return 1
    elif value == "no":
        return 0
    else:
        raise ValueError("Target must be 'yes' or 'no'")