from __future__ import annotations

from docutils import nodes
from docutils.parsers.rst import directives

from sphinx.util.docutils import SphinxDirective


class SbomDirective(SphinxDirective):
    """A directive to render a SBOM report."""

    required_arguments = 1
    option_spec = {
        "summary": directives.flag,
        "package_summary": directives.flag,
        "include_licenses": directives.flag,
        "component_type_summary": directives.flag,
        "license_summary": directives.flag,
        "supplier_summary": directives.flag,
        "vulnerability_summary": directives.flag,
        "vulnerability_detail": directives.flag,
    }

    def run(self) -> list[nodes.Node]:
        sbom_file = self.arguments[0]
        
        # For now, just return a simple paragraph.
        paragraph_node = nodes.paragraph(text=f"SBOM report for {sbom_file}")
        
        if "summary" in self.options:
            paragraph_node += nodes.paragraph(text="Summary option is set")

        return [paragraph_node]
