from typing import List, Dict
from aiohttp import web

from openapi_server.models.dfr_rest_services_get_air_compliance_get200_response import DfrRestServicesGetAirComplianceGet200Response
from openapi_server.models.dfr_rest_services_get_air_quality_get200_response import DfrRestServicesGetAirQualityGet200Response
from openapi_server.models.dfr_rest_services_get_aws_docs_get200_response import DfrRestServicesGetAwsDocsGet200Response
from openapi_server.models.dfr_rest_services_get_case_formal_actions_get200_response import DfrRestServicesGetCaseFormalActionsGet200Response
from openapi_server.models.dfr_rest_services_get_compliance_history_get200_response import DfrRestServicesGetComplianceHistoryGet200Response
from openapi_server.models.dfr_rest_services_get_compliance_summary_get200_response import DfrRestServicesGetComplianceSummaryGet200Response
from openapi_server.models.dfr_rest_services_get_cwa3yr_compliance_get200_response import DfrRestServicesGetCwa3yrComplianceGet200Response
from openapi_server.models.dfr_rest_services_get_cwa3yr_d80d90_counts_get200_response import DfrRestServicesGetCwa3yrD80d90CountsGet200Response
from openapi_server.models.dfr_rest_services_get_cwa_cs_compliance_get200_response import DfrRestServicesGetCwaCsComplianceGet200Response
from openapi_server.models.dfr_rest_services_get_cwa_eff_alr_exp_get200_response import DfrRestServicesGetCwaEffAlrExpGet200Response
from openapi_server.models.dfr_rest_services_get_cwa_eff_alr_get200_response import DfrRestServicesGetCwaEffAlrGet200Response
from openapi_server.models.dfr_rest_services_get_cwa_eff_compliance_exp_get200_response import DfrRestServicesGetCwaEffComplianceExpGet200Response
from openapi_server.models.dfr_rest_services_get_cwa_eff_compliance_get200_response import DfrRestServicesGetCwaEffComplianceGet200Response
from openapi_server.models.dfr_rest_services_get_cwa_ps_compliance_get200_response import DfrRestServicesGetCwaPsComplianceGet200Response
from openapi_server.models.dfr_rest_services_get_cwa_rnc_compliance_get200_response import DfrRestServicesGetCwaRncComplianceGet200Response
from openapi_server.models.dfr_rest_services_get_cwa_se_compliance_get200_response import DfrRestServicesGetCwaSeComplianceGet200Response
from openapi_server.models.dfr_rest_services_get_d80d90s_details_get200_response import DfrRestServicesGetD80d90sDetailsGet200Response
from openapi_server.models.dfr_rest_services_get_demographics_by_id_get200_response import DfrRestServicesGetDemographicsByIdGet200Response
from openapi_server.models.dfr_rest_services_get_dfr_get200_response import DfrRestServicesGetDfrGet200Response
from openapi_server.models.dfr_rest_services_get_ejscreen_indexes_get200_response import DfrRestServicesGetEjscreenIndexesGet200Response
from openapi_server.models.dfr_rest_services_get_enforcement_summary_get200_response import DfrRestServicesGetEnforcementSummaryGet200Response
from openapi_server.models.dfr_rest_services_get_extract_dates_get200_response import DfrRestServicesGetExtractDatesGet200Response
from openapi_server.models.dfr_rest_services_get_formal_actions_get200_response import DfrRestServicesGetFormalActionsGet200Response
from openapi_server.models.dfr_rest_services_get_icis_formal_actions_get200_response import DfrRestServicesGetIcisFormalActionsGet200Response
from openapi_server.models.dfr_rest_services_get_inspections_get200_response import DfrRestServicesGetInspectionsGet200Response
from openapi_server.models.dfr_rest_services_get_map_get200_response import DfrRestServicesGetMapGet200Response
from openapi_server.models.dfr_rest_services_get_naics_get200_response import DfrRestServicesGetNaicsGet200Response
from openapi_server.models.dfr_rest_services_get_notices_get200_response import DfrRestServicesGetNoticesGet200Response
from openapi_server.models.dfr_rest_services_get_permits_get200_response import DfrRestServicesGetPermitsGet200Response
from openapi_server.models.dfr_rest_services_get_rcra_compliance_get200_response import DfrRestServicesGetRcraComplianceGet200Response
from openapi_server.models.dfr_rest_services_get_sdwa_lead_and_copper_get200_response import DfrRestServicesGetSdwaLeadAndCopperGet200Response
from openapi_server.models.dfr_rest_services_get_sdwa_sanitary_surveys_get200_response import DfrRestServicesGetSdwaSanitarySurveysGet200Response
from openapi_server.models.dfr_rest_services_get_sdwa_site_visits_get200_response import DfrRestServicesGetSdwaSiteVisitsGet200Response
from openapi_server.models.dfr_rest_services_get_sdwa_violations_get200_response import DfrRestServicesGetSdwaViolationsGet200Response
from openapi_server.models.dfr_rest_services_get_sdwis_compliance_get200_response import DfrRestServicesGetSdwisComplianceGet200Response
from openapi_server.models.dfr_rest_services_get_sic_codes_get200_response import DfrRestServicesGetSicCodesGet200Response
from openapi_server.models.dfr_rest_services_get_spatial_metadata_get200_response import DfrRestServicesGetSpatialMetadataGet200Response
from openapi_server.models.dfr_rest_services_get_tri_history_get200_response import DfrRestServicesGetTriHistoryGet200Response
from openapi_server.models.dfr_rest_services_get_tri_releases_get200_response import DfrRestServicesGetTriReleasesGet200Response
from openapi_server.models.dfr_rest_services_get_tribes_get200_response import DfrRestServicesGetTribesGet200Response
from openapi_server.models.dfr_rest_services_get_water_quality_details_get200_response import DfrRestServicesGetWaterQualityDetailsGet200Response
from openapi_server.models.dfr_rest_services_get_water_quality_get200_response import DfrRestServicesGetWaterQualityGet200Response
from openapi_server import util


async def dfr_rest_services_air3_yr_download_get(request: web.Request, ) -> web.Response:
    """Downloads the complete Air Compliance History Section of the DFR

    For the provided system identifier, dowloads all displayed Air quaterly/monthly Facility Level Status, High Priority Violation (HPV) History, HPV Detailed Violations and Federal Reportable Violation  information in a Comma Seperated Value (CSV) format.


    """
    return web.Response(status=200)


async def dfr_rest_services_air3_yr_download_post(request: web.Request, ) -> web.Response:
    """Downloads the complete Air Compliance History Section of the DFR

    For the provided system identifier, dowloads all displayed Air quaterly/monthly Facility Level Status, High Priority Violation (HPV) History, HPV Detailed Violations and Federal Reportable Violation  information in a Comma Seperated Value (CSV) format.


    """
    return web.Response(status=200)


async def dfr_rest_services_cwa3_yr_effluent_download_get(request: web.Request, ) -> web.Response:
    """Downloads NPDES Effluent Violation Information by month and quarter.

    For the provided system identifier, dowloads all displayed NPDES quaterly/monthly effluent violation information in a Comma Seperated Value (CSV) format.


    """
    return web.Response(status=200)


async def dfr_rest_services_cwa3_yr_effluent_download_post(request: web.Request, ) -> web.Response:
    """Downloads NPDES Effluent Violation Information by month and quarter.

    For the provided system identifier, dowloads all displayed NPDES quaterly/monthly effluent violation information in a Comma Seperated Value (CSV) format.


    """
    return web.Response(status=200)


async def dfr_rest_services_cwa3_yr_sepscs_download_get(request: web.Request, ) -> web.Response:
    """Downloads NPDES Compliance Schedule, Permit Schedule and Single Event Violation Information by month and quarter.

    For the provided system identifier, dowloads all displayed NPDES quaterly/monthly Compliance Schedule, Permit Schedule, and Single Event Violation  information in a Comma Seperated Value (CSV) format.


    """
    return web.Response(status=200)


async def dfr_rest_services_cwa3_yr_sepscs_download_post(request: web.Request, ) -> web.Response:
    """Downloads NPDES Compliance Schedule, Permit Schedule and Single Event Violation Information by month and quarter.

    For the provided system identifier, dowloads all displayed NPDES quaterly/monthly Compliance Schedule, Permit Schedule, and Single Event Violation  information in a Comma Seperated Value (CSV) format.


    """
    return web.Response(status=200)


async def dfr_rest_services_get_air_compliance_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Air Compliance Report Service

    This procedure obtains data for Air Compliance in the Environmental Conditions Section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_air_compliance_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Air Compliance Report Service

    This procedure obtains data for Air Compliance in the Environmental Conditions Section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_air_quality_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Air Quality Report Service

    This procedure obtains data for Air Quality in the Environmental Conditions Section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_air_quality_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Air Quality Report Service

    This procedure obtains data for Air Quality in the Environmental Conditions Section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_aws_docs_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Placeholder

    

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_aws_docs_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Placeholder

    

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_case_formal_actions_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Displays Cases related to the Facility

    Displays closed case information from EPA&#39;s Federal Enforcement &amp; Compliance System that are related to the facility.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_case_formal_actions_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Displays Cases related to the Facility

    Displays closed case information from EPA&#39;s Federal Enforcement &amp; Compliance System that are related to the facility.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_compliance_history_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report 5 Year Compliance Monitoring History Service

    This procedure obtains data for the Compliance Monitoring History (5 years) in the Enforcement and Compliance Section of the Detailed Facility report.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_compliance_history_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report 5 Year Compliance Monitoring History Service

    This procedure obtains data for the Compliance Monitoring History (5 years) in the Enforcement and Compliance Section of the Detailed Facility report.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_compliance_summary_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Compliance Summary Service

    This procedure obtains data for Compliance Summary Data in the Enforcement and Compliance Section of the Detailed Facility report.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_compliance_summary_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Compliance Summary Service

    This procedure obtains data for Compliance Summary Data in the Enforcement and Compliance Section of the Detailed Facility report.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_csv_get(request: web.Request, ) -> web.Response:
    """Downloads a spectific section  of the DFR in CSV Format

    For a supplied system id and DFR section name, the procedure will download that section in a Comma Separated Value (CSV) format.


    """
    return web.Response(status=200)


async def dfr_rest_services_get_csv_post(request: web.Request, ) -> web.Response:
    """Downloads a spectific section  of the DFR in CSV Format

    For a supplied system id and DFR section name, the procedure will download that section in a Comma Separated Value (CSV) format.


    """
    return web.Response(status=200)


async def dfr_rest_services_get_cwa3yr_compliance_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report 3 Year CWA Facility-Level Status Service

    This procedure obtains data for the CWA Facility-Level Status section located in the Three Year Compliance Status by Quarter portion of the DFR. Valid Compliance Statuses are as follows: &gt; \&quot;In Viol\&quot; &#x3D; Facility is in violation &gt; \&quot;No Viol\&quot; &#x3D; No violation found &gt; \&quot;Unk\&quot; &#x3D; Unknown status &gt; \&quot;SNC/Cat 1\&quot; &#x3D; SNC/Category I violation found

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_cwa3yr_compliance_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report 3 Year CWA Facility-Level Status Service

    This procedure obtains data for the CWA Facility-Level Status section located in the Three Year Compliance Status by Quarter portion of the DFR. Valid Compliance Statuses are as follows: &gt; \&quot;In Viol\&quot; &#x3D; Facility is in violation &gt; \&quot;No Viol\&quot; &#x3D; No violation found &gt; \&quot;Unk\&quot; &#x3D; Unknown status &gt; \&quot;SNC/Cat 1\&quot; &#x3D; SNC/Category I violation found

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_cwa3yr_d80d90_counts_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Displays monlthly and quarterly counts of D80 and D90 Effluent Non Reporting Violations Related to the Facility

    Displays monlthly and quarterly counts of D80 and D90 Effluent Non Reporting Violations Related to the Facility from EPA&#39;s ICIS NPDES System.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_cwa3yr_d80d90_counts_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Displays monlthly and quarterly counts of D80 and D90 Effluent Non Reporting Violations Related to the Facility

    Displays monlthly and quarterly counts of D80 and D90 Effluent Non Reporting Violations Related to the Facility from EPA&#39;s ICIS NPDES System.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_cwa_cs_compliance_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report CWA CSV Compliance Service

    This procedure obtains data for the CWA Compliance Schedule Violations section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_cwa_cs_compliance_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report CWA CSV Compliance Service

    This procedure obtains data for the CWA Compliance Schedule Violations section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_cwa_eff_alr_exp_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Placeholder

    

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_cwa_eff_alr_exp_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Placeholder

    

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_cwa_eff_alr_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report CWA Effluent ALR Service

    This procedure obtains data for the CWA Pollutant Discharge section located in the Three Year Compliance Status by Quarter portion of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_cwa_eff_alr_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report CWA Effluent ALR Service

    This procedure obtains data for the CWA Pollutant Discharge section located in the Three Year Compliance Status by Quarter portion of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_cwa_eff_compliance_exp_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Placeholder

    

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_cwa_eff_compliance_exp_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Placeholder

    

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_cwa_eff_compliance_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report CWA Effluent Compliance Service

    This procedure obtains data for the CWA Effluent Compliance section on the DFR.  

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_cwa_eff_compliance_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report CWA Effluent Compliance Service

    This procedure obtains data for the CWA Effluent Compliance section on the DFR.  

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_cwa_ps_compliance_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report CWA PSV Compliance Service

    This procedure obtains data for the CWA Permit Schedule Violations section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_cwa_ps_compliance_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report CWA PSV Compliance Service

    This procedure obtains data for the CWA Permit Schedule Violations section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_cwa_rnc_compliance_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report CWA RNC Compliance Service

    This procedure obtains data for the CWA SNC/RNC History section located in the Three Year ompliance Status by Quarter portion of the DFR. Valid Compliance Statuses are as follows. &gt; S &#x3D; SNC/Category I - an enforcement action has been issued, and the facility is not meeting its compliance schedule &gt; E &#x3D; SNC/Category I - effluent violations of monthly average limits (Technical Review Criteria and chronic) &gt; X &#x3D; SNC/Category I - effluent violations of non-monthly average limits (Technical Review Criteria and chronic) &gt; T &#x3D; SNC/Category I - compliance schedule reporting violation &gt; D &#x3D; SNC/Category I - reporting violation - nonreceipt of DMR &gt; N &#x3D; RNC/Category II - reportable non-compliance &gt; P &#x3D; Resolved Pending - an enforcement action has been issued, and facility compliance with the action is pending final completion &gt; R &#x3D; Resolved - the facility has returned to compliance with its permit conditions, either with or without issuance of an enforcement action &gt; C &#x3D; Not considered in RNC/SNC based on manual review of data by state or EPA region. This manual override status is also indicated by a superscripted \&quot;m\&quot;. &gt; Blank &#x3D; Not considered in RNC/SNC &gt; N/A &#x3D; EPA&#39;s data system is not able to determine the facility-level compliance status based upon the information available. This information may be available from a state database.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_cwa_rnc_compliance_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report CWA RNC Compliance Service

    This procedure obtains data for the CWA SNC/RNC History section located in the Three Year ompliance Status by Quarter portion of the DFR. Valid Compliance Statuses are as follows. &gt; S &#x3D; SNC/Category I - an enforcement action has been issued, and the facility is not meeting its compliance schedule &gt; E &#x3D; SNC/Category I - effluent violations of monthly average limits (Technical Review Criteria and chronic) &gt; X &#x3D; SNC/Category I - effluent violations of non-monthly average limits (Technical Review Criteria and chronic) &gt; T &#x3D; SNC/Category I - compliance schedule reporting violation &gt; D &#x3D; SNC/Category I - reporting violation - nonreceipt of DMR &gt; N &#x3D; RNC/Category II - reportable non-compliance &gt; P &#x3D; Resolved Pending - an enforcement action has been issued, and facility compliance with the action is pending final completion &gt; R &#x3D; Resolved - the facility has returned to compliance with its permit conditions, either with or without issuance of an enforcement action &gt; C &#x3D; Not considered in RNC/SNC based on manual review of data by state or EPA region. This manual override status is also indicated by a superscripted \&quot;m\&quot;. &gt; Blank &#x3D; Not considered in RNC/SNC &gt; N/A &#x3D; EPA&#39;s data system is not able to determine the facility-level compliance status based upon the information available. This information may be available from a state database.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_cwa_se_compliance_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report CWA SEV Compliance Service

    This procedure obtains data for the CWA Single Event Violations section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_cwa_se_compliance_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report CWA SEV Compliance Service

    This procedure obtains data for the CWA Single Event Violations section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_d80d90s_details_get(request: web.Request, output=None, p_npdes_id=None, p_missinglate=None, p_qmtype=None, p_qmvalue=None, param_callback=None) -> web.Response:
    """Display detailed D80/D90 information for the facility for a given quarter or month

    Displays detailed D80/D90 Effluent Non Reporting  information from EPA&#39;s ICIS NPDES system for the facility for a given quarter or month.

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param p_npdes_id: The NPDES_ID for the NPDES Permit to download DMR D80 and D90 Non-Receipt violations.
    :type p_npdes_id: str
    :param p_missinglate: For the D80.D90 download, identifies whether or not MISSINGviolations are downloaded or LATE violations are downloaded.  Valid values are:  MiISSING and LATE.
    :type p_missinglate: str
    :param p_qmtype: Identifies the time frame type, month or quarter, for the D80/D90 download.
    :type p_qmtype: str
    :param p_qmvalue: A number between 1 and 39 that identifies the specific month or quarter for the D80/D90 violation download.
    :type p_qmvalue: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_d80d90s_details_post(request: web.Request, output=None, p_npdes_id=None, p_missinglate=None, p_qmtype=None, p_qmvalue=None, param_callback=None) -> web.Response:
    """Display detailed D80/D90 information for the facility for a given quarter or month

    Displays detailed D80/D90 Effluent Non Reporting  information from EPA&#39;s ICIS NPDES system for the facility for a given quarter or month.

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param p_npdes_id: The NPDES_ID for the NPDES Permit to download DMR D80 and D90 Non-Receipt violations.
    :type p_npdes_id: str
    :param p_missinglate: For the D80.D90 download, identifies whether or not MISSINGviolations are downloaded or LATE violations are downloaded.  Valid values are:  MiISSING and LATE.
    :type p_missinglate: str
    :param p_qmtype: Identifies the time frame type, month or quarter, for the D80/D90 download.
    :type p_qmtype: str
    :param p_qmvalue: A number between 1 and 39 that identifies the specific month or quarter for the D80/D90 violation download.
    :type p_qmvalue: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_demographics_by_id_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Displays 2010 Census and ACS demographics by Facility ID

    Displays precalculated 2010 Census and American Community Survey demographic information for a provided facility identifier.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_demographics_by_id_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Displays 2010 Census and ACS demographics by Facility ID

    Displays precalculated 2010 Census and American Community Survey demographic information for a provided facility identifier.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_dfr_get(request: web.Request, p_id, output=None, p_system=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Service

    This procedure is the overall service for the Detailed Facility Report. It returns all of the data displayed in the DFR web report by invoking individual procedures that each return a targeted portion of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param p_system: System Acronym Filter.  Enter a single system acronym to filter results.
    :type p_system: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_dfr_post(request: web.Request, p_id, output=None, p_system=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Service

    This procedure is the overall service for the Detailed Facility Report. It returns all of the data displayed in the DFR web report by invoking individual procedures that each return a targeted portion of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param p_system: System Acronym Filter.  Enter a single system acronym to filter results.
    :type p_system: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_ejscreen_indexes_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report EJScreen Indexes Service

    

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_ejscreen_indexes_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report EJScreen Indexes Service

    

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_enforcement_summary_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Enforcement Summary Service

    This procedure obtains data for the Enforcement and Compliance Summary in the Facility Summary section of the Detailed Facility Report.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_enforcement_summary_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Enforcement Summary Service

    This procedure obtains data for the Enforcement and Compliance Summary in the Facility Summary section of the Detailed Facility Report.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_extract_dates_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Displays the dates that data was extracted from native EPA systems for the DFR.

    By EPA System, displays the extract dates that data was extracted for the DFR from multiple EPA computer systems.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_extract_dates_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Displays the dates that data was extracted from native EPA systems for the DFR.

    By EPA System, displays the extract dates that data was extracted for the DFR from multiple EPA computer systems.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_formal_actions_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Formal Actions Service

    This procedure obtains data for the Formal Enforcement Actions section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_formal_actions_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Formal Actions Service

    This procedure obtains data for the Formal Enforcement Actions section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_icis_formal_actions_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report ICIS Formal Actions Service

    This procedure obtains data for the Integrated Compliance Information System, Formal Enforcement Actions section of the DFR. 

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_icis_formal_actions_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report ICIS Formal Actions Service

    This procedure obtains data for the Integrated Compliance Information System, Formal Enforcement Actions section of the DFR. 

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_inspections_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Inspections Summary Service

    This procedure obtains data for Enforcement and Compliance Summary Section of the Detailed Facility report.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_inspections_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Inspections Summary Service

    This procedure obtains data for Enforcement and Compliance Summary Section of the Detailed Facility report.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_map_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Map Service

    Returns an object with the facility&#39;s latitude and longitude coordinates.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_map_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Map Service

    Returns an object with the facility&#39;s latitude and longitude coordinates.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_naics_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report NAICS Code Service

    This procedure obtains data for the Facility NAICS Codes section in Facility/System Characteristics of the Detailed Facility Report.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_naics_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report NAICS Code Service

    This procedure obtains data for the Facility NAICS Codes section in Facility/System Characteristics of the Detailed Facility Report.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_notices_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Notices Service

    This procedure obtains data for the Notices/Informal Actions section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_notices_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Notices Service

    This procedure obtains data for the Notices/Informal Actions section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_permits_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Permits Service

    This procedure obtains data for the following sections of the Detailed Facility Report. &gt; Facility Information (FRS) in the Facility Summary. &gt; Regulatory Interests in the Facility Summary. &gt; Also Reports in the Facility Summary. &gt; Facility/System Characteristics in Facility/System Characteristics. &gt; Facility Contact Information in Facility/System Characteristics. &gt; Facility SIC Codes in Facility/System Characteristics section. &gt; Facility NAICS Codes in Facility/System Characteristics section.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_permits_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Permits Service

    This procedure obtains data for the following sections of the Detailed Facility Report. &gt; Facility Information (FRS) in the Facility Summary. &gt; Regulatory Interests in the Facility Summary. &gt; Also Reports in the Facility Summary. &gt; Facility/System Characteristics in Facility/System Characteristics. &gt; Facility Contact Information in Facility/System Characteristics. &gt; Facility SIC Codes in Facility/System Characteristics section. &gt; Facility NAICS Codes in Facility/System Characteristics section.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_rcra_compliance_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report RCRA Compliance Service

    This procedure obtains data for the RCRA Compliance section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_rcra_compliance_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report RCRA Compliance Service

    This procedure obtains data for the RCRA Compliance section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_sdwa_lead_and_copper_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report SDWA Lead and Copper Service

    This procedure obtains data for the SDWA, Lead and Copper Rule section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_sdwa_lead_and_copper_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report SDWA Lead and Copper Service

    This procedure obtains data for the SDWA, Lead and Copper Rule section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_sdwa_sanitary_surveys_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report SDWA Sanitary Surveys Service

    This procedure obtains data for the SDWA, Sanitary Surveys section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_sdwa_sanitary_surveys_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report SDWA Sanitary Surveys Service

    This procedure obtains data for the SDWA, Sanitary Surveys section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_sdwa_site_visits_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report SDWA Sanitary Site Visits Service

    This procedure obtains data for the SDWA, Sanitary Site Visits section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_sdwa_site_visits_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report SDWA Sanitary Site Visits Service

    This procedure obtains data for the SDWA, Sanitary Site Visits section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_sdwa_violations_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report SDWA Violations Service

    This procedure obtains data for the SDWA Violations section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_sdwa_violations_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report SDWA Violations Service

    This procedure obtains data for the SDWA Violations section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_sdwis_compliance_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report SDWIS Compliance Service

    This procedure obtains data for the SDWA Compliance section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_sdwis_compliance_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report SDWIS Compliance Service

    This procedure obtains data for the SDWA Compliance section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_sic_codes_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report SIC Code Service

    This procedure obtains data for the Facility SIC Codes section in Facility/System Characteristics of the Detailed Facility Report.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_sic_codes_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report SIC Code Service

    This procedure obtains data for the Facility SIC Codes section in Facility/System Characteristics of the Detailed Facility Report.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_spatial_metadata_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Spatial Metadata Service

    Returns an object with the facility coordinate spatial metadata.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_spatial_metadata_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Spatial Metadata Service

    Returns an object with the facility coordinate spatial metadata.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_tri_history_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report TRI History Service

    This procedure obtains data for the TRI History section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_tri_history_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report TRI History Service

    This procedure obtains data for the TRI History section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_tri_releases_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report TRI Releases Service

    This procedrue obtains data for the TRI Releases section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_tri_releases_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report TRI Releases Service

    This procedrue obtains data for the TRI Releases section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_tribes_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Tribes Service

    This procedure obtains data for the Tribes and Reservations section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_tribes_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Tribes Service

    This procedure obtains data for the Tribes and Reservations section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_water_quality_details_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Displays detailed Water Quality information from EPA&#39;s Office of Water Systems

    This information is only available for facilities with a NPDES permit. Based on spatial data, displays water quality information from EPA&#39;s Office of Water ATTAINS system.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_water_quality_details_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Displays detailed Water Quality information from EPA&#39;s Office of Water Systems

    This information is only available for facilities with a NPDES permit. Based on spatial data, displays water quality information from EPA&#39;s Office of Water ATTAINS system.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_water_quality_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Water Quality Service

    This procedure obtains data for the Water Quality section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_get_water_quality_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Detailed Facility Report Water Quality Service

    This procedure obtains data for the Water Quality section of the DFR.

    :param p_id: Either the EPA Facility Registry System&#39;s REGISTRY_ID for a facility or the facility identifier from the following EPA Systems: RCRAINFO (HANDLER_ID), AFS (SCSC), ICIS NPDES (NPDES_ID), or SDWIS (PWS_ID).
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def dfr_rest_services_rcra3_yr_download_get(request: web.Request, ) -> web.Response:
    """Downloads the complete RCRA Compliance History Section of the DFR

    For the provided system identifier, dowloads all displayed RCRA quaterly/monthly Facility Level Status and Violation information in a Comma Seperated Value (CSV) format.


    """
    return web.Response(status=200)


async def dfr_rest_services_rcra3_yr_download_post(request: web.Request, ) -> web.Response:
    """Downloads the complete RCRA Compliance History Section of the DFR

    For the provided system identifier, dowloads all displayed RCRA quaterly/monthly Facility Level Status and Violation information in a Comma Seperated Value (CSV) format.


    """
    return web.Response(status=200)
