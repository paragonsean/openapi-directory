from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def all(request: web.Request, format=None, cohort=None, gene=None, tcga_participant_barcode=None, page=None, page_size=None, sort_by=None) -> web.Response:
    """Retrieve all data by genes Gistic2 results.

    This service provides access to the Gistic2 all_data_by_genes.txt output data. This data is a gene-level table of copy number values for all samples. The returned copy number values are in units (copy number - 2) so that no amplification or deletion is 0, genes with amplifications have positive values, and genes with deletions are negative values. The data are converted from marker level to gene level using the extreme method: a gene is assigned the greatest amplification or the least deletion value among the markers it covers. Results may be filtered by cohort, gene, or barcode, but at least one gene or barcode must be supplied.

    :param format: Format of result.
    :type format: str
    :param cohort: Narrow search to one or more TCGA disease cohorts from the scrollable list.
    :type cohort: List[str]
    :param gene: Comma separated list of gene name(s).
    :type gene: List[str]
    :param tcga_participant_barcode: Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
    :type tcga_participant_barcode: List[str]
    :param page: Which page (slice) of entire results set should be returned. 
    :type page: List[int]
    :param page_size: Number of records per page of results.  Max is 2000.
    :type page_size: List[int]
    :param sort_by: Which column in the results should be used for sorting paginated results?
    :type sort_by: str

    """
    return web.Response(status=200)


async def amplified(request: web.Request, format=None, cohort=None, gene=None, q=None, page=None, page_size=None, sort_by=None) -> web.Response:
    """Retrieve Gistic2 significantly amplified genes results.

    This service provides access to the Gistic2 amp_genes.conf_99.txt output data.  At least 1 gene or cohort must be supplied.

    :param format: Format of result.
    :type format: str
    :param cohort: Narrow search to one or more TCGA disease cohorts from the scrollable list.
    :type cohort: List[str]
    :param gene: Comma separated list of gene name(s).
    :type gene: List[str]
    :param q: Only return results with Q-value &lt;&#x3D; given threshold.
    :type q: 
    :param page: Which page (slice) of entire results set should be returned. 
    :type page: List[int]
    :param page_size: Number of records per page of results.  Max is 2000.
    :type page_size: List[int]
    :param sort_by: Which column in the results should be used for sorting paginated results?
    :type sort_by: str

    """
    return web.Response(status=200)


async def deleted(request: web.Request, format=None, cohort=None, gene=None, q=None, page=None, page_size=None, sort_by=None) -> web.Response:
    """Retrieve Gistic2 significantly deleted genes results.

    This service provides access to the Gistic2 del_genes.conf_99.txt output data.  At least 1 gene or cohort must be supplied.

    :param format: Format of result.
    :type format: str
    :param cohort: Narrow search to one or more TCGA disease cohorts from the scrollable list.
    :type cohort: List[str]
    :param gene: Comma separated list of gene name(s).
    :type gene: List[str]
    :param q: Only return results with Q-value &lt;&#x3D; given threshold.
    :type q: 
    :param page: Which page (slice) of entire results set should be returned. 
    :type page: List[int]
    :param page_size: Number of records per page of results.  Max is 2000.
    :type page_size: List[int]
    :param sort_by: Which column in the results should be used for sorting paginated results?
    :type sort_by: str

    """
    return web.Response(status=200)


async def feature_table(request: web.Request, format=None, cohort=None, _date=None, column=None, page=None, page_size=None) -> web.Response:
    """Retrieve aggregated analysis features table.

    This service returns part or all of the so-called &lt;strong&gt;feature table&lt;/strong&gt;; which aggregates the most important findings across ALL pipelines in the GDAC Firehose analysis workflow into a single table for simple access.  One feature table is created per disease cohort.  Results may be filtered by date or cohort, but at least 1 cohort must be specified here. For more details please visit the &lt;a href&#x3D;https://confluence.broadinstitute.org/display/GDAC/Documentation\\#Documentation-FeatureTable&gt;online documentation&lt;/a&gt;.  Please note that the service is still undergoing experimental evaluation and does not return JSON format.

    :param format: Format of result.
    :type format: str
    :param cohort: Narrow search to one or more TCGA disease cohorts from the scrollable list.
    :type cohort: List[str]
    :param _date: Select one or more date stamps.
    :type _date: List[str]
    :param column: Comma separated list of which data columns/fields to return.
    :type column: List[str]
    :param page: Which page (slice) of entire results set should be returned. 
    :type page: List[int]
    :param page_size: Number of records per page of results.  Max is 2000.
    :type page_size: List[int]

    """
    _date = [util.deserialize_date(s) for s in _date]
    return web.Response(status=200)


async def focal(request: web.Request, format=None, cohort=None, gene=None, tcga_participant_barcode=None, page=None, page_size=None, sort_by=None) -> web.Response:
    """Retrieve focal data by genes Gistic2 results.

    This service provides access to the Gistic2 focal_data_by_genes.txt output data. This output is similar to the all_data_by_genes.txt output, but using only focal events with lengths greater than the  focal length cutoff. This data is a gene-level table of copy number values for all samples. The returned copy number values are in units (copy number - 2) so that no amplification or deletion is 0, genes with amplifications have positive values, and genes with deletions are negative values. The data are converted from marker level to gene level using the extreme method: a gene is assigned the greatest amplification or the least deletion value among the markers it covers. Results may be filtered by cohort, gene, and/or barcode, but at least one gene or barcode must be supplied.

    :param format: Format of result.
    :type format: str
    :param cohort: Narrow search to one or more TCGA disease cohorts from the scrollable list.
    :type cohort: List[str]
    :param gene: Comma separated list of gene name(s).
    :type gene: List[str]
    :param tcga_participant_barcode: Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
    :type tcga_participant_barcode: List[str]
    :param page: Which page (slice) of entire results set should be returned. 
    :type page: List[int]
    :param page_size: Number of records per page of results.  Max is 2000.
    :type page_size: List[int]
    :param sort_by: Which column in the results should be used for sorting paginated results?
    :type sort_by: str

    """
    return web.Response(status=200)


async def m_af(request: web.Request, format=None, cohort=None, tool=None, gene=None, tcga_participant_barcode=None, column=None, page=None, page_size=None, sort_by=None) -> web.Response:
    """Retrieve MutSig final analysis MAF.

    This service returns columns from the MAF generated by MutSig. Results may be filtered by gene, cohort, tool, or barcode, but at least one gene OR barcode OR cohort must be given.  By default a subset consisting of the most commonly used columns will be returned, but that can be modified with the column parameter. Specifying &#39;all&#39; in this parameter is a convenient way to return every column of the respective MAF, and has precedence over any any other column selection expression.  The complete list of column names that may be specified is &lt;a href&#x3D;&#39;http://firebrowse.org/api-docs/#!/Metadata/MAFColNames&#39;&gt;given here&lt;/a&gt;.  For more information on the mutation data, and how it is processed by Firehose, please consult the &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Documentation#Documentation-MutationPipelines\&quot;&gt;pipeline documentation&lt;/a&gt;.

    :param format: Format of result.
    :type format: str
    :param cohort: Narrow search to one or more TCGA disease cohorts from the scrollable list.
    :type cohort: List[str]
    :param tool: Narrow search to include only data/results produced by the selected Firehose tool.
    :type tool: List[str]
    :param gene: Comma separated list of gene name(s).
    :type gene: List[str]
    :param tcga_participant_barcode: Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
    :type tcga_participant_barcode: List[str]
    :param column: Comma separated list of which data columns/fields to return.
    :type column: List[str]
    :param page: Which page (slice) of entire results set should be returned. 
    :type page: List[int]
    :param page_size: Number of records per page of results.  Max is 2000.
    :type page_size: List[int]
    :param sort_by: Which column in the results should be used for sorting paginated results?
    :type sort_by: str

    """
    return web.Response(status=200)


async def m_rna_seq_quartiles(request: web.Request, gene, format=None, cohort=None, protocol=None, sample_type=None, exclude=None) -> web.Response:
    """Returns RNASeq expression quartiles, e.g. suitable for drawing a boxplot.

    For a given gene compute quartiles and extrema, suitable e.g. for drawing a boxplot (Tukey 1977).  Results may be filtered by cohort, sample type, patient barcode  or characterization protocol, and are returned sorted by cohort.  Note that samples for which no expression value was recorded (e.g. &lt;a href&#x3D;\&quot;http://firebrowse.org/api/v1/Samples/mRNASeq?&amp;gene&#x3D;egfr&amp;cohort&#x3D;SKCM&amp;tcga_participant_barcode&#x3D;TCGA-GN-A262\&quot;&gt;the melanoma sample TCGA-GN-262&lt;/a&gt;) are removed prior to calculation.

    :param gene: Enter a single gene name.
    :type gene: str
    :param format: Format of result.
    :type format: str
    :param cohort: Narrow search to one or more TCGA disease cohorts from the scrollable list.
    :type cohort: List[str]
    :param protocol: Narrow search to one or more sample characterization protocols from the scrollable list.
    :type protocol: List[str]
    :param sample_type: For which type of sample(s) should quartiles be computed?
    :type sample_type: List[str]
    :param exclude: Comma separated list of TCGA participants, identified by barcodes such as TCGA-GF-A4EO, denoting samples to exclude from computation.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def reports(request: web.Request, format=None, _date=None, cohort=None, name=None, type=None, page=None, page_size=None, sort_by=None) -> web.Response:
    """Retrieve links to summary reports from Firehose analysis runs.

    This service returns URLs to the analysis result reports for runs of the Broad Institute GDAC Firehose analysis pipeline. At least one year of run reports are maintained in the database, but the reports from the latest run will be returned by default. The set of &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Nozzle\&quot;&gt;Nozzle&lt;/a&gt; reports returned may be filtered by disease cohort, report type and report name.

    :param format: Format of result.
    :type format: str
    :param _date: Select one or more date stamps.
    :type _date: List[str]
    :param cohort: Narrow search to one or more TCGA disease cohorts from the scrollable list.
    :type cohort: List[str]
    :param name: Narrow search to one or more report names.
    :type name: List[str]
    :param type: Narrow search to one or more report types.
    :type type: List[str]
    :param page: Which page (slice) of entire results set should be returned. 
    :type page: List[int]
    :param page_size: Number of records per page of results.  Max is 2000.
    :type page_size: List[int]
    :param sort_by: Which column in the results should be used for sorting paginated results?
    :type sort_by: str

    """
    _date = [util.deserialize_date(s) for s in _date]
    return web.Response(status=200)


async def s_mg(request: web.Request, format=None, cohort=None, tool=None, rank=None, gene=None, q=None, page=None, page_size=None, sort_by=None) -> web.Response:
    """Retrieve Significantly Mutated Genes (SMG).

    This service provides a list of significantly mutated genes, as scored by MutSig.  It may be filtered by cohort, rank, gene, tool and/or Q-value threshold, but at least one cohort or gene must be supplied.

    :param format: Format of result.
    :type format: str
    :param cohort: Narrow search to one or more TCGA disease cohorts from the scrollable list.
    :type cohort: List[str]
    :param tool: Narrow search to include only data/results produced by the selected Firehose tool.
    :type tool: List[str]
    :param rank: Number of significant genes to return.
    :type rank: int
    :param gene: Comma separated list of gene name(s).
    :type gene: List[str]
    :param q: Only return results with Q-value &lt;&#x3D; given threshold.
    :type q: 
    :param page: Which page (slice) of entire results set should be returned. 
    :type page: List[int]
    :param page_size: Number of records per page of results.  Max is 2000.
    :type page_size: List[int]
    :param sort_by: Which column in the results should be used for sorting paginated results?
    :type sort_by: str

    """
    return web.Response(status=200)


async def thresholded(request: web.Request, format=None, cohort=None, gene=None, tcga_participant_barcode=None, page=None, page_size=None, sort_by=None) -> web.Response:
    """Retrieve all thresholded by genes Gistic2 results.

    This service provides access to the Gistic2 all_thresholded_by_genes.txt output data. A gene-level table of discrete amplification and deletion indicators for all samples. A table value of 0 means no amplification or deletion above the threshold. Amplifications are positive numbers: 1 means amplification above the amplification threshold; 2 means amplifications larger to the arm level amplifications observed for the sample. Deletions are represented by negative table values: -1 represents deletion beyond the threshold; -2 means deletions greater than the minimum arm-level deletion observed for the sample. Results maybe filtered by cohort, gene or barcode, but at least one gene or barcode must be supplied.

    :param format: Format of result.
    :type format: str
    :param cohort: Narrow search to one or more TCGA disease cohorts from the scrollable list.
    :type cohort: List[str]
    :param gene: Comma separated list of gene name(s).
    :type gene: List[str]
    :param tcga_participant_barcode: Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
    :type tcga_participant_barcode: List[str]
    :param page: Which page (slice) of entire results set should be returned. 
    :type page: List[int]
    :param page_size: Number of records per page of results.  Max is 2000.
    :type page_size: List[int]
    :param sort_by: Which column in the results should be used for sorting paginated results?
    :type sort_by: str

    """
    return web.Response(status=200)
