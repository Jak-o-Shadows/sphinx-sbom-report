# sphinx-sbom-report
Sphinx Extension for displaying SBOM

This Sphinx extension puts a SBOM into the ReStructuredtext, in order to nicely display it with the various outputs. This enables putting a SBOM into your documentation automatically.

Currently only supports CycloneDS SBOM format

The key directive is:
```
.. sbom:: your-sbom.xml
```

With options used to configure what details are shown:
 * `summary`: Show an overall summary table
 * `package_summary`: Show a summary table of what packages are being used
 * `include_licenses`: Include the license details in the package summary
 * `component_type_summary`: Show a summary table of the component types (application, library, etc)
 * `license_summary`: Show a summary table of the licenses
 * `supplier_summary`: Show a summary table of the supplier's
 * `vulnerability_summary`: Show a summary table of vulnerabilities
 * `vulnerabilitiy_detail`: Show a detailed listing of the vulnerabilities
