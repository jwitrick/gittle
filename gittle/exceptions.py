class InvalidRemoteUrl(Exception):
    """The url provided for the remote service is invalid"""
    pass

class InvalidRSAKey(Exception):
    """Can't generate key ..."""
    pass

class InvalidTag(Exception):
    """The tag specified does not exist"""
    pass
