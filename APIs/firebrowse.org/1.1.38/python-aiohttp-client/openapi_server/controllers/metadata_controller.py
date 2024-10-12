from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def barcode(request: web.Request, tcga_barcode, format=None) -> web.Response:
    """Given a TCGA barcode, return its short letter sample type code.

    

    :param tcga_barcode: Enter a single TCGA barcode, of any form: e.g. TCGA-GF-A4EO-06 or TCGA-EL-A3D5-01A-22D-A202-08
    :type tcga_barcode: str
    :param format: Format of result.
    :type format: str

    """
    return web.Response(status=200)


async def centers(request: web.Request, format=None, center=None) -> web.Response:
    """Obtain identities of TCGA consortium member centers.

    By default this function returns a table of all consortium members in TCGA, aka centers; it provides both the HTTP domain and full organizational name of each center.  A subset of this table may be obtained by explicitly specifying one or more domain names.

    :param format: Format of result.
    :type format: str
    :param center: Narrow search to one or more TCGA centers from the scrollable list.
    :type center: List[str]

    """
    return web.Response(status=200)


async def clinical_names(request: web.Request, format=None) -> web.Response:
    """Retrieve names of all TCGA clinical data elements (CDEs).

    Retrieve names of all patient-level clinical data elements (CDES) available in TCGA, unioned across all disease cohorts. A CDE will be listed here only when it has a value other than NA for at least 1 patient case in any disease cohort. For more information on how these CDEs are processed see our &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Documentation\&quot;&gt;pipeline documentation&lt;/a&gt;.

    :param format: Format of result.
    :type format: str

    """
    return web.Response(status=200)


async def clinical_names_fh(request: web.Request, format=None) -> web.Response:
    """Retrieve names of CDEs normalized by Firehose and selected for analyses.

    This service returns the names of patient-level clinical data elements (CDEs) that have been normalized by Firehose for use in analyses, unioned across all disease cohorts. For more information on how these CDEs are processed, see our &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Documentation\&quot;&gt;pipeline documentation&lt;/a&gt;.

    :param format: Format of result.
    :type format: str

    """
    return web.Response(status=200)


async def code(request: web.Request, code, format=None) -> web.Response:
    """Translate from numeric to symbolic TCGA sample codes.

    Convert a TCGA numeric sample type code (e.g. 01, 02) to its corresponding symbolic (short letter) code (e.g. TP, TR).

    :param code: Narrow search to one or more TCGA sample type codes.
    :type code: List[str]
    :param format: Format of result.
    :type format: str

    """
    return web.Response(status=200)


async def cohorts(request: web.Request, format=None, cohort=None) -> web.Response:
    """Translate TCGA cohort abbreviations to full disease names.

    By default this function returns a table containing all TCGA cohort abbreviations and their corresponding disease names.  A subset of that table may be obtained by explicitly specifying one or more cohort abbreviations.

    :param format: Format of result.
    :type format: str
    :param cohort: Narrow search to one or more TCGA disease cohorts from the scrollable list.
    :type cohort: List[str]

    """
    return web.Response(status=200)


async def counts(request: web.Request, format=None, _date=None, cohort=None, sample_type=None, data_type=None, totals=None, sort_by=None) -> web.Response:
    """Retrieve sample counts.

    Returns the aliquot counts for each disease cohort, per sample type and data type.  The sample type designation of \&quot;Tumor\&quot; may be used to aggregate the count of all tumor aliquots into a single number per disease and data type. See the SampleTypes function for a complete description of sample types.

    :param format: Format of result.
    :type format: str
    :param _date: Select one or more date stamps.
    :type _date: List[str]
    :param cohort: Narrow search to one or more TCGA disease cohorts from the scrollable list.
    :type cohort: List[str]
    :param sample_type: Narrow search to one or more TCGA sample types from the scrollable list.
    :type sample_type: List[str]
    :param data_type: Narrow search to one or more TCGA data types from the scrollable list.
    :type data_type: List[str]
    :param totals: Output an entry providing the totals for each data type.
    :type totals: bool
    :param sort_by: Which column in the results should be used for sorting paginated results?
    :type sort_by: str

    """
    _date = [util.deserialize_date(s) for s in _date]
    return web.Response(status=200)


async def dates(request: web.Request, format=None) -> web.Response:
    """Retrieve dates of all GDAC Firehose stddata &amp; analyses runs that have been ingested into FireBrowse.

    

    :param format: Format of result.
    :type format: str

    """
    return web.Response(status=200)


async def heart_beat(request: web.Request, format=None) -> web.Response:
    """Simple way to discern whether API server is up and running

    Returns a message to indicate that API (server) is up and running, or times out if not.

    :param format: Format of result.
    :type format: str

    """
    return web.Response(status=200)


async def m_af_col_names(request: web.Request, format=None) -> web.Response:
    """Retrieve names of all columns in the mutation annotation files (MAFs) served by FireBrowse.

    Retrieve the names of all columns in the mutation annotation files (MAFs) hosted by FireBrowse.  For more information on the mutation data, and how it is processed by Firehose, please consult the &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Documentation#Documentation-MutationPipelines\&quot;&gt;pipeline documentation&lt;/a&gt;.

    :param format: Format of result.
    :type format: str

    """
    return web.Response(status=200)


async def patients(request: web.Request, format=None, cohort=None, page=None, page_size=None, sort_by=None) -> web.Response:
    """Retrieve list of all TCGA patients.

    This service returns a list of all TCGA patient barcodes in FireBrowse, optionally filtered by disease cohort.  The barcodes are obtained directy from the clinical data.

    :param format: Format of result.
    :type format: str
    :param cohort: Narrow search to one or more TCGA disease cohorts from the scrollable list.
    :type cohort: List[str]
    :param page: Which page (slice) of entire results set should be returned. 
    :type page: List[int]
    :param page_size: Number of records per page of results.  Max is 2000.
    :type page_size: List[int]
    :param sort_by: Which column in the results should be used for sorting paginated results?
    :type sort_by: str

    """
    return web.Response(status=200)


async def platforms(request: web.Request, format=None, platform=None) -> web.Response:
    """Translate TCGA platform codes to full platform names.

    By default this function returns a table of all of the technology platforms used to sequence or characterize samples in TCGA--both their short platform codes and full names.  A subset of this table may be obtained by explicitly specifying one or more platform codes.

    :param format: Format of result.
    :type format: str
    :param platform: Narrow search to one or more TCGA data generation platforms from the scrollable list.
    :type platform: List[str]

    """
    return web.Response(status=200)


async def sample_types(request: web.Request, format=None) -> web.Response:
    """Return all TCGA sample type codes, both numeric and symbolic.

    

    :param format: Format of result.
    :type format: str

    """
    return web.Response(status=200)


async def short_letter_code(request: web.Request, short_letter_code, format=None) -> web.Response:
    """Translate from symbolic to numeric TCGA sample codes.

    Convert a TCGA sample type code in symbolic form (or &#39;short letter code&#39; like TP, TR) to its corresponding numeric form (e.g. 01, 02).

    :param short_letter_code: TCGA sample type short letter code(s) (e.g. TP, NB, etc.). 
    :type short_letter_code: List[str]
    :param format: Format of result.
    :type format: str

    """
    return web.Response(status=200)


async def t_s_sites(request: web.Request, format=None, tss_code=None) -> web.Response:
    """Obtain identities of tissue source sites in TCGA.

    By default this function returns a table of all sites which contributed source tissue to TCGA, aka TSS&#39;s. A subset of this table may be obtained by explicitly specifying one or more sites.

    :param format: Format of result.
    :type format: str
    :param tss_code: Narrow search to one or more TSS codes
    :type tss_code: List[str]

    """
    return web.Response(status=200)
