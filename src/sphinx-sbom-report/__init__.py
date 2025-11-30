r"""Sphinx extension: sphinx-sbom-report
========================================
"""
import typing

from sphinx.application import Sphinx
from sphinx.util import logging

from .helloworld import *
from .sbom import SbomDirective

logger = logging.getLogger("sphinx-sbom-report")

# Try to get the version number from package metadata
try:
    from importlib import metadata
except ImportError:
    import importlib_metadata as metadata

try:
    __version__ = metadata.version("sphinx-sbom-report")
except metadata.PackageNotFoundError:
    logger.warning("sphinx-sbom-report package metadata not found. Could not get version")



def setup(app: Sphinx) -> dict[str, typing.Any]:
    app.add_config_value(name="sbom_report_title", default="{title}", rebuild="env")
    app.add_directive(name="hello", cls=HelloDirective)
    app.add_directive(name="sbom", cls=SbomDirective)
    app.add_role(name="hello", role=HelloRole())

    metadata = {
        "version": ".".join(__version__.split(".")[:3]),
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
    return metadata
