"""
Argyle is a collection of Fabric utilities for Django deployment.
"""


__version_info__ = {
    'major': 0,
    'minor': 1,
    'micro': 0,
    'releaselevel': 'beta',
}

def get_version():
    """
    Return the formatted version information
    """
    vers = ["%(major)i.%(minor)i" % __version_info__, ]

    if __version_info__['micro']:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__['releaselevel'] != 'final':
        vers.append('%(releaselevel)s' % __version_info__)
    return ''.join(vers)

__version__ = get_version()
