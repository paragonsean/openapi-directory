from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def clinical(request: web.Request, format=None, cohort=None, tcga_participant_barcode=None, cde_name=None, page=None, page_size=None, sort_by=None) -> web.Response:
    """Retrieve TCGA CDEs verbatim, i.e. not normalized by Firehose.

    This service returns patient clinical data from TCGA, verbatim. It differs from the Samples/Clinical_FH method by providing access to all TCGA CDEs in their original form, not merely the subset of CDEs normalized by Firehose for analyses.  Results may be selected by disease cohort, patient barcode or CDE name, but at least one cohort, barcode, or CDE must be provided. When filtering by CDE note that only when a patient record contains one or more of the selected CDEs will it be returned. Visit the Metadata/ClinicalNames api function to see the entire list of TCGA CDEs that may be queried via this method. For more information on how clinical data are processed, see our &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Documentation#Documentation-ClinicalPipeline\&quot;&gt;pipeline documentation&lt;/a&gt;.

    :param format: Format of result.
    :type format: str
    :param cohort: Narrow search to one or more TCGA disease cohorts from the scrollable list.
    :type cohort: List[str]
    :param tcga_participant_barcode: Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
    :type tcga_participant_barcode: List[str]
    :param cde_name: Retrieve results only for specified CDEs, per the Metadata/ClinicalNames function
    :type cde_name: List[str]
    :param page: Which page (slice) of entire results set should be returned. 
    :type page: List[int]
    :param page_size: Number of records per page of results.  Max is 2000.
    :type page_size: List[int]
    :param sort_by: Which column in the results should be used for sorting paginated results?
    :type sort_by: str

    """
    return web.Response(status=200)


async def clinical_fh(request: web.Request, format=None, cohort=None, tcga_participant_barcode=None, fh_cde_name=None, page=None, page_size=None, sort_by=None) -> web.Response:
    """Retrieve CDEs normalized by Firehose and selected for analyses.

    This service returns patient-level clinical data elements (CDEs) that have been normalized by Firehose for use in analyses. Results may be selected by disease cohort, patient barcode or CDE name, but at least one cohort, barcode or CDE must be provided. When filtering by CDE note that only when a  patient record contains one or more of the selected CDEs will it be returned. Visit &lt;a href&#x3D;\&quot;http://gdac.broadinstitute.org/runs/info/clinical\&quot;&gt;this table of CDEs&lt;/a&gt; to see what&#39;s available for every disase cohort; for more information on how these CDEs are processed see our &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Documentation#Documentation-ClinicalPipeline\&quot;&gt;pipeline documentation&lt;/a&gt;.

    :param format: Format of result.
    :type format: str
    :param cohort: Narrow search to one or more TCGA disease cohorts from the scrollable list.
    :type cohort: List[str]
    :param tcga_participant_barcode: Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
    :type tcga_participant_barcode: List[str]
    :param fh_cde_name: Retrieve results only for the CDEs specified from the scrollable list.
    :type fh_cde_name: List[str]
    :param page: Which page (slice) of entire results set should be returned. 
    :type page: List[int]
    :param page_size: Number of records per page of results.  Max is 2000.
    :type page_size: List[int]
    :param sort_by: Which column in the results should be used for sorting paginated results?
    :type sort_by: str

    """
    return web.Response(status=200)


async def m_rna_seq(request: web.Request, format=None, gene=None, cohort=None, tcga_participant_barcode=None, sample_type=None, protocol=None, page=None, page_size=None, sort_by=None) -> web.Response:
    """Retrieve mRNASeq data.

    This service returns sample-level log2 mRNASeq expression values. Results may be filtered by gene, cohort, barcode, sample type or characterization protocol, but at least one gene must be supplied.

    :param format: Format of result.
    :type format: str
    :param gene: Comma separated list of gene name(s).
    :type gene: List[str]
    :param cohort: Narrow search to one or more TCGA disease cohorts from the scrollable list.
    :type cohort: List[str]
    :param tcga_participant_barcode: Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
    :type tcga_participant_barcode: List[str]
    :param sample_type: Narrow search to one or more TCGA sample types from the scrollable list.
    :type sample_type: List[str]
    :param protocol: Narrow search to one or more sample characterization protocols from the scrollable list.
    :type protocol: List[str]
    :param page: Which page (slice) of entire results set should be returned. 
    :type page: List[int]
    :param page_size: Number of records per page of results.  Max is 2000.
    :type page_size: List[int]
    :param sort_by: Which column in the results should be used for sorting paginated results?
    :type sort_by: str

    """
    return web.Response(status=200)


async def mi_r_seq(request: web.Request, format=None, mir=None, cohort=None, tcga_participant_barcode=None, tool=None, sample_type=None, page=None, page_size=None, sort_by=None) -> web.Response:
    """Retrieve miRSeq data.

    This service returns sample-level log2 miRSeq expression values. Results may be filtered by miR, cohort, barcode, sample type or Firehose preprocessing tool, but at least one miR must be supplied.

    :param format: Format of result.
    :type format: str
    :param mir: Comma separated list of miR names (e.g. hsa-let-7b-5p,hsa-let-7a-1).
    :type mir: List[str]
    :param cohort: Narrow search to one or more TCGA disease cohorts from the scrollable list.
    :type cohort: List[str]
    :param tcga_participant_barcode: Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
    :type tcga_participant_barcode: List[str]
    :param tool: Narrow search to include only data/results produced by the selected Firehose tool.
    :type tool: List[str]
    :param sample_type: Narrow search to one or more TCGA sample types from the scrollable list.
    :type sample_type: List[str]
    :param page: Which page (slice) of entire results set should be returned. 
    :type page: List[int]
    :param page_size: Number of records per page of results.  Max is 2000.
    :type page_size: List[int]
    :param sort_by: Which column in the results should be used for sorting paginated results?
    :type sort_by: str

    """
    return web.Response(status=200)
