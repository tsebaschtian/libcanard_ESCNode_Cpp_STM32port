Import("env")


def skip_from_build(node):
    """
    `node.name` - a name of File System Node
    `node.get_path()` - a relative path
    `node.get_abspath()` - an absolute path
     to ignore file from a build process, just return None
    """
    if "libcanard/drivers" in node.get_path():
        # Return None for exclude
        return None
    if "libcanard/examples" in node.get_path():
        # Return None for exclude
        return None
    if "libcanard/tests" in node.get_path():
        # Return None for exclude
        return None
    if "libcanard/canard/tests" in node.get_path():
        # Return None for exclude
        return None
    
    return node

# Register callback
env.AddBuildMiddleware(skip_from_build, "*")