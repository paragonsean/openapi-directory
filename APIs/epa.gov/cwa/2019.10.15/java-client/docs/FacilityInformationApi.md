# FacilityInformationApi

All URIs are relative to *https://echodata.epa.gov/echo*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cwaRestServicesGetDownloadGet**](FacilityInformationApi.md#cwaRestServicesGetDownloadGet) | **GET** /cwa_rest_services.get_download | Clean Water Act (CWA) Download Data Service |
| [**cwaRestServicesGetDownloadPost**](FacilityInformationApi.md#cwaRestServicesGetDownloadPost) | **POST** /cwa_rest_services.get_download | Clean Water Act (CWA) Download Data Service |
| [**cwaRestServicesGetFacilitiesGet**](FacilityInformationApi.md#cwaRestServicesGetFacilitiesGet) | **GET** /cwa_rest_services.get_facilities | Clean Water Act (CWA) Facility Search Service |
| [**cwaRestServicesGetFacilitiesPost**](FacilityInformationApi.md#cwaRestServicesGetFacilitiesPost) | **POST** /cwa_rest_services.get_facilities | Clean Water Act (CWA) Facility Search Service |
| [**cwaRestServicesGetFacilityInfoGet**](FacilityInformationApi.md#cwaRestServicesGetFacilityInfoGet) | **GET** /cwa_rest_services.get_facility_info | Clean Water Act (CWA) Facility Enhanced Search Service |
| [**cwaRestServicesGetFacilityInfoPost**](FacilityInformationApi.md#cwaRestServicesGetFacilityInfoPost) | **POST** /cwa_rest_services.get_facility_info | Clean Water Act (CWA) Facility Enhanced Search Service |
| [**cwaRestServicesGetGeojsonGet**](FacilityInformationApi.md#cwaRestServicesGetGeojsonGet) | **GET** /cwa_rest_services.get_geojson | Clean Water Act (CWA) GeoJSON Service |
| [**cwaRestServicesGetGeojsonPost**](FacilityInformationApi.md#cwaRestServicesGetGeojsonPost) | **POST** /cwa_rest_services.get_geojson | Clean Water Act (CWA) GeoJSON Service |
| [**cwaRestServicesGetInfoClustersGet**](FacilityInformationApi.md#cwaRestServicesGetInfoClustersGet) | **GET** /cwa_rest_services.get_info_clusters | Clean Water Act (CWA) Info Clusters Service |
| [**cwaRestServicesGetInfoClustersPost**](FacilityInformationApi.md#cwaRestServicesGetInfoClustersPost) | **POST** /cwa_rest_services.get_info_clusters | Clean Water Act (CWA) Info Clusters Service |
| [**cwaRestServicesGetMapGet**](FacilityInformationApi.md#cwaRestServicesGetMapGet) | **GET** /cwa_rest_services.get_map | Clean Water Act (CWA) Map Service |
| [**cwaRestServicesGetMapPost**](FacilityInformationApi.md#cwaRestServicesGetMapPost) | **POST** /cwa_rest_services.get_map | Clean Water Act (CWA) Map Service |
| [**cwaRestServicesGetQidGet**](FacilityInformationApi.md#cwaRestServicesGetQidGet) | **GET** /cwa_rest_services.get_qid | Clean Water Act (CWA) Paginated Results Service |
| [**cwaRestServicesGetQidPost**](FacilityInformationApi.md#cwaRestServicesGetQidPost) | **POST** /cwa_rest_services.get_qid | Clean Water Act (CWA) Paginated Results Service |


<a id="cwaRestServicesGetDownloadGet"></a>
# **cwaRestServicesGetDownloadGet**
> File cwaRestServicesGetDownloadGet(qid, output, qcolumns, pPrettyPrint)

Clean Water Act (CWA) Download Data Service

Based on the QID obtained from a get_facilities or get_facility_info query, return a comma separated value (CSV) file of the facilities found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInformationApi apiInstance = new FacilityInformationApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default).
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      File result = apiInstance.cwaRestServicesGetDownloadGet(qid, output, qcolumns, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInformationApi#cwaRestServicesGetDownloadGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **qid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default). | [optional] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |
| **pPrettyPrint** | **BigDecimal**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are a comma separated value (CSV) file or a file containing a GeoJSON feature collection. |  -  |

<a id="cwaRestServicesGetDownloadPost"></a>
# **cwaRestServicesGetDownloadPost**
> File cwaRestServicesGetDownloadPost(qid, output, qcolumns, pPrettyPrint)

Clean Water Act (CWA) Download Data Service

Based on the QID obtained from a get_facilities or get_facility_info query, return a comma separated value (CSV) file of the facilities found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInformationApi apiInstance = new FacilityInformationApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default).
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      File result = apiInstance.cwaRestServicesGetDownloadPost(qid, output, qcolumns, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInformationApi#cwaRestServicesGetDownloadPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **qid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default). | [optional] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |
| **pPrettyPrint** | **BigDecimal**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are a comma separated value (CSV) file or a file containing a GeoJSON feature collection. |  -  |

<a id="cwaRestServicesGetFacilitiesGet"></a>
# **cwaRestServicesGetFacilitiesGet**
> CwaRestServicesGetFacilitiesGet200Response cwaRestServicesGetFacilitiesGet(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pFrs, pReg, pSic, pNcs, pPen, pC1lat, pC1lon, pC2lat, pC2lon, pUsmex, pSic2, pSic4, pFa, pFf, pAct, pMaj, pMact, pFea, pFeay, pFeaa, pIea, pIeay, pIeaa, pQiv, pIv, pImpw, pImpCauGrp, pImpPol, pTrep, pPm, pPd, pIco, pHuc, pPid, pMed, pYsl, pYsly, pYsla, pQs, pSfs, pTribeid, pTribename, pTribedist, pPstat, pPtype, pPcomp, pPlimits, pPcss, pPexp, pOwop, pIpfti, pAgoo, pIdt1, pIdt2, pPityp, pPfead1, pPfead2, pPfeat, pPccs, pPexcd, pPsncq, pPctrack, pDwd, pPt, pPdwdist, pPswdpc, pPswdmp, pPswpol, pPswcas, pPswparam, pPswvio, pWbd, pRadwbd, pFrswbd, pFntype, pPidall, pMonthsLastDmr, pLastDmrWithin, pIndsw, pMsgpPtype, pMonType, pIagency, pPermittingAgency, pIsws, pIswss, pIswssID, pDs1, pDs2, pDa1, pDa2, pMS4, pOoFN, pOoFNtype, pOoSA, pOoSA1, pOoCt, pOoSt, pOoZip, pFacIco, pIcoo, pFacIcos, pEjscreen, pAlrexceed, pLimitAddr, pLat, pLong, pRadius, pEjscreenOver80cnt, pBioFlag, pBioFacType, pBioTrtmntProcs, pBioAnalyMethodCatgry, pBioTotalVolumeAmt, pBioMgmtPrctceType, pBioMgmtPrctceStype, pBioMgmtPrctceHandler, pBioMgmtContainer, pBioMgmtPathogen, pBioMgmtPathred, pBioMgmtVector, pBioMgmtDefCategory, pBioMgmtDeficiencies, pBioVioCode, pBioCurrentVio, pBioQtrsInVio, pBioRptYear, pBioVioLastYear, pMsgpRptYear, pVioLastYear, queryset, responseset, tablelist, maplist, summarylist, paramCallback, qcolumns, pE90Count, pE90Years, pPsc)

Clean Water Act (CWA) Facility Search Service

Validates query search parameters and returns query identifier.  Use the responseset parameter to set the page size

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInformationApi apiInstance = new FacilityInformationApi(defaultClient);
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String pFn = "pFn_example"; // String | Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
    String pSa = "pSa_example"; // String | Facility street address. Enter a complete or partial street address.
    String pSa1 = "pSa1_example"; // String | Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa.
    String pCt = "pCt_example"; // String | Facility City Filter. Enter a single case-insensitive city name to filter results.
    String pCo = "pCo_example"; // String | Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
    String pFips = "pFips_example"; // String | FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
    String pSt = "pSt_example"; // String | Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
    String pZip = "pZip_example"; // String | 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values.
    String pFrs = "pFrs_example"; // String | Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results.
    String pReg = "01"; // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    String pSic = "pSic_example"; // String | Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4.
    String pNcs = "pNcs_example"; // String | North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
    String pPen = "pPen_example"; // String | Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER = No Penalties - ANY = Any Penalty - LEXX = Less than or equal to XX months.  Provide a number in place of XX, e.g. \"LE5\" for a facility with a penalty within previous 5 months. - GTXX = Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago.
    BigDecimal pC1lat = new BigDecimal(78); // BigDecimal | In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC1lon = new BigDecimal(78); // BigDecimal | In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC2lat = new BigDecimal(78); // BigDecimal | In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC2lon = new BigDecimal(78); // BigDecimal | In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    String pUsmex = "Y"; // String | US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
    String pSic2 = "pSic2_example"; // String | Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \"22\" to match all SIC codes beginning with 22.  Use the \"%\" character within strings to match any SIC values with the pattern.  For example, \"2%21\" matches 2021, 2121, 2221, etc.
    String pSic4 = "pSic4_example"; // String | Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker.
    String pFa = "pFa_example"; // String | Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values.
    String pFf = "Y"; // String | Federal Facility Indicator Flag. Enter Y to restrict searches to federal facilities.
    String pAct = "pAct_example"; // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.  A Y will select ICIS NPDES permits with a status of effective, continued, or expired.
    String pMaj = "Y"; // String | Major Facility Flag.  Enter Y to restrict results to Major facilities only.
    String pMact = "pMact_example"; // String | CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility.
    String pFea = "W"; // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
    BigDecimal pFeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
    String pFeaa = "A"; // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
    String pIea = "W"; // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
    BigDecimal pIeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
    String pIeaa = "E"; // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
    String pQiv = "0"; // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    String pIv = "pIv_example"; // String | Facility has a violation status of 'In Viol' during any of the selected quarters.   Range: Fiscal Year 2020 Quarter 2 to Fiscal Year 2017 Quarter 2  Multiple values are comma delimited.   ||||||  Fiscal Years |||||| - FY2020 or FY20 or 2020 or 20 - FY2019 or FY19 or 2019 or 19 - FY2018 or FY18 or 2018 or 18 - FY2017 or FY17 or 2017 or 17  ||||| Fiscal Quarters ||||| - FY2020Q2 or FY20Q2 or 20202 or 202 or 13 - FY2020Q1 or FY20Q1 or 20201 or 201 or 12 - FY2019Q4 or FY19Q4 or 20194 or 194 or 11 - FY2019Q3 or FY19Q3 or 20193 or 193 or 10 - FY2019Q2 or FY19Q2 or 20192 or 192 or 9 - FY2019Q1 or FY19Q1 or 20191 or 191 or 8 - FY2018Q4 or FY18Q4 or 20184 or 184 or 7 - FY2018Q3 or FY18Q3 or 20183 or 183 or 6 - FY2018Q2 or FY18Q2 or 20182 or 182 or 5 - FY2018Q1 or FY18Q1 or 20181 or 181 or 4 - FY2017Q4 or FY17Q4 or 20174 or 174 or 3 - FY2017Q3 or FY17Q3 or 20173 or 173 or 2 - FY2017Q2 or FY17Q2 or 20172 or 172 or 1
    String pImpw = "Y"; // String | Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
    String pImpCauGrp = "ALGAL GROWTH"; // String | Facility is discharging a pollutant group causing a waterbody to be impaired.  Enter 1 through 34 (the internal number of the pollutant group); or enter a partial name such as Dioxin,Temp,tUrBidity.
    String pImpPol = "Y"; // String | Facility is discharging pollutants that are potentially contributing to the impairment of local waterbodies according to the ATTAINS database.
    String pTrep = "CURR"; // String | Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR = Current TRI reporter. - NONCURR = Has reported to TRI in the past but not for the current reporting year.
    String pPm = "NONE"; // String | Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE = 0% - GT5 = greater than 5% - GT10 = greater than 10% - GT25 = greater than 25% - GT50 = greater than 50% - GT75 = greater than 75%
    String pPd = "NONE"; // String | Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE = 0 population density per square mile - GT100 = More than 100 population density per square mile - GT500 = More than 500 population density per square mile - GT1000 = More than 1000 population density per square mile - GT5000 = More than 5000 population density per square mile - GT10000 = More than 10000 population density per square mile - GT20000 = More than 20000 population density per square mile
    String pIco = "Y"; // String | Indian Country Flag.  Enter a \"Y\" or \"N\" to restrict searches to facilities inside or outside Indian Country.
    String pHuc = "pHuc_example"; // String | 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
    String pPid = "pPid_example"; // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    String pMed = "A"; // String | Filter Results by Media. - A = Air - M = RMP (Risk Management Plan) - R = RCRA (Hazardous Waste) - S = SDWA (Public Drinking Water Systems) - ALL = Air and RCRA and Water
    String pYsl = "W"; // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
    BigDecimal pYsly = new BigDecimal("1"); // BigDecimal | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
    String pYsla = "E"; // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
    String pQs = "pQs_example"; // String | Quick Search. Allows entry for city, state, and/or zip code.
    String pSfs = "pSfs_example"; // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
    BigDecimal pTribeid = new BigDecimal(78); // BigDecimal | Numeric code for tribe (or list of tribes).
    String pTribename = "pTribename_example"; // String | Tribe Name Filter.  Enter a single tribe name to filter results.
    BigDecimal pTribedist = new BigDecimal(78); // BigDecimal | Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
    String pPstat = "pPstat_example"; // String | Permit Status Filter.  Enter one or more of the following codes.  Provide multiple values as a comma-delimited list. - EFF = Effective - EXP = Expired - PND = Pending - TRM = Terminated - RET = Retired - NON = Not Needed - ADC = Admin Continued
    String pPtype = "pPtype_example"; // String | Permit Type Filter. Enter one or more code values to filter results.  Provide multiple values as a comma-delimited list. - NPD = NPDES Individual Permit - NGP = NPDES Master General Permit - GPC = General Permit Covered Facility - SNN = State Issued Master General Permit (Non-NPDES) - IIU = Individual IU Permit (Non-NPDES) - SIN = Individual State Issued Permit (Non-NPDES) - APR = Associated Permit Record - UFT = Unpermitted Facility
    String pPcomp = "pPcomp_example"; // String | Permit Component Code Filter.  Enter one or more codes to filter results.  Provide multiple values as a comma-delimited list. - PRE = Pretreatment - CAF = CAFO - CSO = CSO - POT = POTW - BIO = Biosolids - SWS = Storm Water Small MS4s - SWM = Storm Water Medium/Large MS4s - SWI = Storm Water Industrial - SWC = Storm Water Construction
    String pPlimits = "Y"; // String | Permit Limits Present Flag.  Enter Y to limit results to facilities have present permit limits.
    String pPcss = "ALL"; // String | Combined Sewer Systems Outflows Limiter.  Enter one of the following to limit results to facilities having the given count of CSS outflows. - ALL = returns all facilities, regardless of the number of outflows. - GE1 = returns facilities with one or more outflows. - GE10 = returns facilities with ten or more outflows. - GE50 = returns facilities with fifty or more outflows.
    String pPexp = "EXP"; // String | Permit Expired or Administratively Continued Limiter.  Enter one of the following values to filter results. - EXP = limit results to facilities with permits expired or administratively continued. - EXPLE1YR = limit resuls to facilities with permits expired administratively continued within the past year. - EXPGT1YR = limit resuls to facilities with permits expired administratively continued more than a year ago.
    String pOwop = "FEDERAL"; // String | Owner/Operator code filter.  Enter one of the following values to restrict results. - Federal = Federal facilities regulated under the NPDES program. - POTW = Publicly owned treatment works. Treatment works that are owned by a State, Tribe, or municipality. - Non-POTW = Non-publicly owned treatment works. Often referred to as \"non-municipals\" or \"industrials\".
    String pIpfti = "pIpfti_example"; // String | 
    String pAgoo = "AND"; // String | Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
    String pIdt1 = "pIdt1_example"; // String | Beginning of date range of most recent facility inspection.
    String pIdt2 = "pIdt2_example"; // String | End of date range of most recent facility inspection.
    String pPityp = "pPityp_example"; // String | Inspection Type Code.  See ICIS Compliance Monitor Types lookup serivce for a list of available codes and descriptions.
    String pPfead1 = "pPfead1_example"; // String | Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    String pPfead2 = "pPfead2_example"; // String | Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    String pPfeat = "pPfeat_example"; // String | Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
    String pPccs = "pPccs_example"; // String | Current Compliance Status: |||||||||||||||||||||||||||  Significant Noncompliance (SNC)  ||||||||||||||||||||||||||| - SNC = E, S, X, T, D - E�= E(EffViol) - S�= S(CSchVio) - X = X(EffNMth) - T = T(CSchRpt) - D�= D(DMR NR)  ||||||||||||||||||||||||||| Noncompliance (NC) ||||||||||||||||||||||||||| - NC = N, V - N�= N(RptViol) - V�= V(NonRNCV)  ||||||||||||||||||||||||||| New Violations (PQV) ||||||||||||||||||||||||||| - PQV = New Violations (13th Quarter)  ||||||||||||||||||||||||||| No Violations (NV) ||||||||||||||||||||||||||| - NV = R, P, M, U, W , Blank, and No New Violations (no PQV) - R�= R(Resolvd) - P�= P(ResPend) - M�= C(Manual) - U = U(N/A) - W = W(N/A) - Blank = (null)  May contain multiple comma-separated values.
    String pPexcd = "0"; // String | 3-Year Effluent Exceedances Limiter.  Enter a value to restrict results to facilities with the given amount of exceedances in the past 3 years. - 0 = facilities with no exceedances - GE0 = facilities with one or more exceedances - GE10 = facilities with ten or more exceedances - GE50 = facilities with fifty or more exceedances - GE100 = facilities with one hundred or more exceedances
    String pPsncq = "GT1"; // String | Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z = Zero quarters in significant noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in significant noncompliance.
    String pPctrack = "false"; // String | Compliance Tracking Limiter. Provide a keyword to indicate the extent to which data is being entered and effluent exceedances are being identified. - Off - Partial - On
    String pDwd = "0"; // String | Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory.
    String pPt = "0"; // String | POTW Transfers. Pounds of toxic chemicals transferred to a Publicly Operated Treatment Works (POTW) as reported to the Toxics Release Inventory.
    String pPdwdist = "N"; // String | Distance (in miles) to downstream drinking water intake.
    String pPswdpc = "pPswdpc_example"; // String | Pollutant Category Code:  Values: WTR for Water, AIR for Air
    String pPswdmp = "1"; // String | Used to determine limit begin and end dates for surface water discharges. Number represents years from current date.
    String pPswpol = "pPswpol_example"; // String | For CWA, pollutant names for surface water discharges. for Drinking Water, SDWIS Violation contaminant codes for unaddressed violations that have occurred in the last 3 years. May contain multiple comma-separated values.
    String pPswcas = "pPswcas_example"; // String | CAS numbers for surface water discharges. May contain multiple comma-separated values.
    String pPswparam = "pPswparam_example"; // String | Parameter codes for surface water discharges. May contain multiple comma-separated values.
    String pPswvio = "Y"; // String | Used in conjuction with parameters p_pswpol and p_pswparam, indicates whether search should only include pollutants with violations.
    String pWbd = "pWbd_example"; // String | 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    String pRadwbd = "pRadwbd_example"; // String | 2-, 4-, 6-, 8-, 10-, or 12 character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Will search against WBD values otained by \"reach indexing\" NPDES permits against the medium resolution National Hydrography Dataset. 
    String pFrswbd = "pFrswbd_example"; // String | Works exactly the same as the p_wbd parameter.  2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    String pFntype = "ALL"; // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
    String pPidall = "Y"; // String | Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc).
    BigDecimal pMonthsLastDmr = new BigDecimal(78); // BigDecimal | The number of months since the last Discharge Monitoring Report has been submitted.
    String pLastDmrWithin = "W"; // String | W value returns facilities that have submitted DMRs within the number of months specified by p_months_last_dmr. An N value returns facilities that have not submitted a DMR within the specified number of months.
    String pIndsw = "Y"; // String | Industrial Stormwater Permit Flag.  Enter a Y or N to filter results by this type of permit.
    String pMsgpPtype = "NOI"; // String | Multi-Sector General Purpose Permit Type.  Enter a value to filter results by MSGP Permit Type. - NOI = Notice of Intent - NOE = No Exposure Certification
    String pMonType = "BENCHG2"; // String | For use with the Industrial Stormwater search only. Valid values are BENCHGS fro Benchmark (Alert Limit) G2 Ore, BENCH for Benchmark (Alert Limit), and ELG fro Effluent Limitation Guidelines(ELG)(Effluent Limit).  
    String pIagency = "pIagency_example"; // String | Issuing Agency Limiter.  Enter a single value to filter results by the issuing agency, e.g. \"State\" or \"EPA\".
    String pPermittingAgency = "pPermittingAgency_example"; // String | 
    String pIsws = "pIsws_example"; // String | Multi-Sector General Purpose Permit Subsector Individual Identifier.  Enter a value to filter results.
    String pIswss = "pIswss_example"; // String | Multi-Sector General Purpose Permit Subsector Group Code.  Enter a value to filter results.
    String pIswssID = "pIswssID_example"; // String | Multi-Sector General Purpose Permit Sector Code.  Enter a value to filter results.
    String pDs1 = "pDs1_example"; // String | Submitted Date Filter Start.  To filter by the date of submission, enter a start date here and an end date in the p_ds2 parameter.  Both dates are required for filtering.
    String pDs2 = "pDs2_example"; // String | Submitted Date Filter End.  To filter by the date of submission, enter an end date here and a start date in the p_ds1 parameter.  Both dates are required for filtering.
    String pDa1 = "pDa1_example"; // String | Active Date Filter Start.  To filter by the active date, enter a start date here and an end date in the p_da2 parameter.  Both dates are required for filtering.
    String pDa2 = "pDa2_example"; // String | Active Date Filter End.  To filter by the active date, enter an end date here and a start date in the p_da1 parameter.  Both dates are required for filtering.
    String pMS4 = "Y"; // String | Municipal Separate Storm Water Sewer (MS4) Permit Flag.  Enter a Y or N to filter results by this type of permit.
    String pOoFN = "pOoFN_example"; // String | Owner/Operator Name. Enter the owner/operator name of the facility.
    String pOoFNtype = "ALL"; // String | Owner/Operator Name Multiple Selection Evaluator.  
    String pOoSA = "pOoSA_example"; // String | Owner/Operator Address.  Enter the address of the owner/operator of the facility.
    String pOoSA1 = "pOoSA1_example"; // String | Owner/Operator Address Line 2.  Enter the line 2 address of the owner/operator of the facility.
    String pOoCt = "pOoCt_example"; // String | Owner/Operator City. Enter the city where the owner/operator of the facility is located.
    String pOoSt = "pOoSt_example"; // String | Owner/Operator State.  Enter the standardized postal state code where the owner/operator of the facility is located.
    String pOoZip = "pOoZip_example"; // String | Owner/Operator Zip Code.  Enter the postal zip code where the owner/operator of the facility is located.
    String pFacIco = "Y"; // String | FRS tribal land code flag.  Enter \"Y\" or \"N\" to include or exclude facilities based on FRS tribal land code.
    String pIcoo = "pIcoo_example"; // String | Indian country search and/or flag.  Enter \"Y\" to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
    String pFacIcos = "pFacIcos_example"; // String | FRS tribal land spatial flag.  Enter \"Y\" or \"N\" to include or exclude facilities based on FRS tribal land spatial flag.
    String pEjscreen = "pEjscreen_example"; // String | Enter \"Y\" to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
    BigDecimal pAlrexceed = new BigDecimal(78); // BigDecimal | Alert Limits Exceedences Limiter.  Enter a numeric value to restrict results to facilities having the given amount or more of alert limits exceedances.
    String pLimitAddr = "Y"; // String | Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
    BigDecimal pLat = new BigDecimal(78); // BigDecimal | Latitude location in decimal degrees.
    BigDecimal pLong = new BigDecimal(78); // BigDecimal | Longitude location in decimal degrees.
    BigDecimal pRadius = new BigDecimal(78); // BigDecimal | Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
    String pEjscreenOver80cnt = "1"; // String | The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
    String pBioFlag = "pBioFlag_example"; // String | A Y value will select all biosolid-related permits.
    String pBioFacType = "pBioFacType_example"; // String | The code indicating the reporting obligation reason:  - POT = A POTW with a design flow rate equal to or greater than one million gallons per day - CLI = A Class I Sludge Management Facility as defined in 40 CFR 503.9 - PPL = A POTW that serves 10,000 people or more - OTH = Otherwise required to report (e.g., permit condition, enforcement action) - NOA = None of the above
    String pBioTrtmntProcs = "pBioTrtmntProcs_example"; // String | The biosolids or sewage sludge treatment process or processes at the facility:  - AER = Aerobic Digestion - AIR = Air Drying (or Sludge Drying Beds) - ANA = Anaerobic Digestion - COD = Beta Ray Irradiation - COM = Lower Temperature Composting - DEW = Pasteurization - DIS = Gamma Ray Irradiation - HEA = Heat Drying (e.g., Flash Dryer, Spray Dryer, Rotary Dryer) - HET = Heat Treatment (Liquid Sewage Sludge Heated to 356 Deg. F/180 Deg. C or Higher for 30 min.) - HTC = Higher Temperature Composting - MET = Methane or Biogas Capture and Recovery - OTH = Other Treatment Process - PRE = Preliminary Operations (e.g., Sludge Grinding, Degritting, Blending) - SLU = Sludge Lagoon - STA = Lime Stabilization - THE = Temporary Sludge Storage (Sewage Sludge Stored on Land 2 Years or Less, Not in Sewage Sludge Unit) - THI = Thickening (Gravity and/or Flotation Thickening, Centrifugation, Belt Filter Press, Vacuum Filter) - THM = Thermophilic Aerobic Digestion - UND = Long-Term Sludge Storage (Sewage Sludge Stored on Land 2 Years or More, not in Sewage Sludge Unit)\"
    String pBioAnalyMethodCatgry = "pBioAnalyMethodCatgry_example"; // String | The unique code for the category of the analytic methods used by the facility to analyze regulated parameters (including enteric viruses, fecal coliforms, helminth ova, and Salmonella sp.) at the facility:  - PAT = Pathogens - MET = Metals - NIT = Nitrogen Compounds - OTH = Other Analytes
    String pBioTotalVolumeAmt = "pBioTotalVolumeAmt_example"; // String | Total annual amount (in dry metric tons) of biosolids or sewage sludge generated at the facility.  - EQ0 = 0 - IN0_1 = GT 0 but LT 1 - IN0_289  =  GT 0 but LT 290 MT/year - IN290_1499  =  GE 290 but LT 1500 MT/year - IN1500_14999  =  GE 1500 but LT 15,000 - GE15000  =  GE 15,000
    String pBioMgmtPrctceType = "pBioMgmtPrctceType_example"; // String | The unique code that identifies the type of biosolids or sewage sludge management practice (e.g., land application, surface disposal, incineration) used by the facility. The facility will separately report the management practice for each biosolids or sewage sludge form and pathogen class. This data element will also identify the management practices used by surface disposal site owners/operators (see 40 CFR 503.24):  - BIN = Incineration - BLN = Land Application - BOT = Other Management Practice - BSD = Surface Disposal
    String pBioMgmtPrctceStype = "pBioMgmtPrctceStype_example"; // String | This is the code indicating additional detail about the type of Management Practice used for a volume of Biosolids or Sewage Sludge:  - ADV = Advanced Alkaline Stabilized Biosolids Distribution & Marketing - AGR = Agricultural Land Application - COM = Distribution and Marketing - Compost - DEE = Deep-well Injection Disposal - DIS = Disposal in a Municipal Landfill (under 40 CFR 258) - DMO = Distribution and Marketing - Other - HEA = Heat Dried Biosolids Distribution & Marketing - OTL = Other Land Application Management Practice Detail - OTO = Other Management Practice Detail - RSA = Reclamation Site Application - SEN = Sent to Cement Kiln for Use as Alternative Energy - STO = Storage - UIC = Use in Construction - UPS = Used in Production of Syngas - USE = Use as Daily Cover for Municipal Landfill (under 40 CFR 258)
    String pBioMgmtPrctceHandler = "pBioMgmtPrctceHandler_example"; // String | This is the code indicating the type of Biosolids or Sewage Sludge handlers/preparers.  - OWN = Owner or Operator - OFF = Off-Site Third-Party Handler or Preparer
    String pBioMgmtContainer = "pBioMgmtContainer_example"; // String | The code that identifies the nature of each biosolids and sewage sludge material generated by the facility in terms of whether the material is a biosolid or sewage sludge and whether the material is ultimately conveyed off-site in bulk or in bags. The facility separately reports the form for each biosolids or sewage sludge management practice or practices used by the facility and pathogen class:  - BUL = Bulk - BAG = Bag or Container
    String pBioMgmtPathogen = "pBioMgmtPathogen_example"; // String | This code identifies the pathogen class [e.g., Class A, Class B, Not Applicable (Incineration)] for biosolids or sewage sludge generated by the facility. The facility will separately report the pathogen class for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form. It also is used to filter applicable Pathogen Reduction and Vector Attraction Reduction Options as well as Land Application Management Practice Deficiencies. Only reqired for some of the mgmt. practice types:  - AAA = Class A - AEQ = Class A EQ (sale/give away) - BBB = Class B - NAP = Not Applicable (Incineration)
    String pBioMgmtPathred = "pBioMgmtPathred_example"; // String | This is the description of the option used by the facility to control pathogen for a Biosolids Management Practice:  - A1 = Class A - Alternative 1: Time/Temperature - A2 = Class A - Alternative 2: pH/Temperature/Percent Solids - A3 = Class A - Alternative 3: Test Enteric Viruses and Helminth ova; Operating Parameters - A4 = Class A - Alternative 4: Test Enteric Viruses and Helminth ova; No New Solids - A51 = Class A - Alternative 5: PFRP 1: Composting - A52 = Class A - Alternative 5: PFRP 2: Heat Drying - A53 = Class A - Alternative 5: PFRP 3: Liquid heat treatment - A54 = Class A - Alternative 5: PFRP 4: Thermophilic Aerobic Digestion (ATAD) - A55 = Class A - Alternative 5 PFPR 5: Beta Ray Irradiation - A56 = Class A - Alternative 5 PFPR 6: Gamma Ray Irradiation - A57 = Class A - Alternative 5: PFRP 7: Pasteurization - A6 = Class A - Alternative 6: PFRP Equivalency - B1 = Class B - Alternative 1: Fecal Coliform Geometric Mean - B21 = Class B - Alternative 2 PSRP 1: Aerobic Digestion - B22 = Class B - Alternative 2 PSRP 2: Air Drying - B23 = Class B - Alternative 2 PSRP 3: Anaerobic Digestion - B24 = Class B - Alternative 2 PSRP 4: Composting - B25 = Class B - Alternative 2 PSRP 5: Lime Stabilization - B3 = Class B - Alternative 3: PSRP Equivalency - PH = pH Adjustment (Domestic Septage)
    String pBioMgmtVector = "pBioMgmtVector_example"; // String | The unique code that identifies the option used by the facility for vector attraction reduction. See a listing of these vector attraction reduction options at 40 CFR 503.33(b)(1) through (11). The facility will separately report the vector attraction reduction options for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form as well as by each biosolids or sewage sludge pathogen class:  - VR1 = Option 1 - Volatile Solids Reduction - VR2 = Option 2 - Bench-Scale Volatile Solids Reduction (Anaerobic Bench Test) - VR3 = Option 3 - Bench-Scale Volatile Solids Reduction (Aerobic Bench Test w/ Percent Solids - 2% or Less) - VR4 = Option 4 - Specific Oxygen Uptake Rate - VR5 = Option 5 - Aerobic Processing (Thermophilic Aerobic Digestion/Composting) - VR6 = Option 6 - Alkaline Treatment - VR7 = Option 7 - Drying (Equal to or Greater than 75 Percent) - VR8 = Option 8 - Drying (Equal to or Greater than 90 Percent) - VR9 = Option 9 - Sewage Sludge Injection - V10 = Option 10 - Sewage Sludge Timely Incorporation into Land - V11 = Option 11 - Sewage Sludge Covered at the End of Each Operating Day
    String pBioMgmtDefCategory = "pBioMgmtDefCategory_example"; // String | This is the code indicating the type of NPDES special regulatory program deficiency:  - INC = Biosolids Incineration - LNA = Biosolids Land Application - LNB = Biosolids Land Application - Pathogen Class B - OTB = Biosolids Other Management Practice - SFD = Biosolids Surface Disposal
    BigDecimal pBioMgmtDeficiencies = new BigDecimal(78); // BigDecimal | The number of times noncompliance was reported by the facility in the last 3 years. The results returned will include facilities whose number of reported noncompliance events is greater than or equal to the number entered.
    String pBioVioCode = "pBioVioCode_example"; // String | The Biosolids Single Event Violation Code.  Enter one or mode codes.
    String pBioCurrentVio = "Y"; // String | Indicator of whether the facility is currently in violation for biosolids under the Clean Water Act, in the 12th or 13th quarter:  - Y = Yes - N = No
    BigDecimal pBioQtrsInVio = new BigDecimal(78); // BigDecimal | The number of quarters, in the last three years, where the facility was in violation for a biosolids violation type.  The results returned will include facilities whose number of quarters with violations is greater than or equal to the number entered.
    String pBioRptYear = "pBioRptYear_example"; // String | The last year that the permittee submitted an annual Biosolids report.  Valid values are NONE and any year greater or equal to 2016.
    String pBioVioLastYear = "Y"; // String | Identifies if a biosolids violation has occured in the last year.  Valid values are Y and N.
    String pMsgpRptYear = "pMsgpRptYear_example"; // String | The last year that a MSGP report was submitted for the permit.  Valid values are \"NONE\" and any year Greater or Eqal to 2015.
    String pVioLastYear = "Y"; // String | Identifies if a permit violation has occured in the last year.  Valid values are Y and N.
    BigDecimal queryset = new BigDecimal(78); // BigDecimal | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    BigDecimal responseset = new BigDecimal(78); // BigDecimal | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    String tablelist = "Y"; // String | Table List Flag. Enter a Y to display the first page of facility results.
    String maplist = "Y"; // String | Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria).
    String summarylist = "Y"; // String | Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pE90Count = new BigDecimal(78); // BigDecimal | Number of E90 Exceedances.  Identifies water permits with a number of E90 (Effluient Exceedances) >= the value provided for the last number of years provided by the p_e90_years value.
    BigDecimal pE90Years = new BigDecimal(78); // BigDecimal | Number of years for the p_e90_count search.  Identified the past number of years to be used for the p_e90_count search.
    String pPsc = "pPsc_example"; // String | Point Source Category.
    try {
      CwaRestServicesGetFacilitiesGet200Response result = apiInstance.cwaRestServicesGetFacilitiesGet(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pFrs, pReg, pSic, pNcs, pPen, pC1lat, pC1lon, pC2lat, pC2lon, pUsmex, pSic2, pSic4, pFa, pFf, pAct, pMaj, pMact, pFea, pFeay, pFeaa, pIea, pIeay, pIeaa, pQiv, pIv, pImpw, pImpCauGrp, pImpPol, pTrep, pPm, pPd, pIco, pHuc, pPid, pMed, pYsl, pYsly, pYsla, pQs, pSfs, pTribeid, pTribename, pTribedist, pPstat, pPtype, pPcomp, pPlimits, pPcss, pPexp, pOwop, pIpfti, pAgoo, pIdt1, pIdt2, pPityp, pPfead1, pPfead2, pPfeat, pPccs, pPexcd, pPsncq, pPctrack, pDwd, pPt, pPdwdist, pPswdpc, pPswdmp, pPswpol, pPswcas, pPswparam, pPswvio, pWbd, pRadwbd, pFrswbd, pFntype, pPidall, pMonthsLastDmr, pLastDmrWithin, pIndsw, pMsgpPtype, pMonType, pIagency, pPermittingAgency, pIsws, pIswss, pIswssID, pDs1, pDs2, pDa1, pDa2, pMS4, pOoFN, pOoFNtype, pOoSA, pOoSA1, pOoCt, pOoSt, pOoZip, pFacIco, pIcoo, pFacIcos, pEjscreen, pAlrexceed, pLimitAddr, pLat, pLong, pRadius, pEjscreenOver80cnt, pBioFlag, pBioFacType, pBioTrtmntProcs, pBioAnalyMethodCatgry, pBioTotalVolumeAmt, pBioMgmtPrctceType, pBioMgmtPrctceStype, pBioMgmtPrctceHandler, pBioMgmtContainer, pBioMgmtPathogen, pBioMgmtPathred, pBioMgmtVector, pBioMgmtDefCategory, pBioMgmtDeficiencies, pBioVioCode, pBioCurrentVio, pBioQtrsInVio, pBioRptYear, pBioVioLastYear, pMsgpRptYear, pVioLastYear, queryset, responseset, tablelist, maplist, summarylist, paramCallback, qcolumns, pE90Count, pE90Years, pPsc);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInformationApi#cwaRestServicesGetFacilitiesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **pFn** | **String**| Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers. | [optional] |
| **pSa** | **String**| Facility street address. Enter a complete or partial street address. | [optional] |
| **pSa1** | **String**| Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa. | [optional] |
| **pCt** | **String**| Facility City Filter. Enter a single case-insensitive city name to filter results. | [optional] |
| **pCo** | **String**| Facility County Filter. Provide a single county name in combination with a state value provided via p_st. | [optional] |
| **pFips** | **String**| FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059. | [optional] |
| **pSt** | **String**| Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pZip** | **String**| 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values. | [optional] |
| **pFrs** | **String**| Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results. | [optional] |
| **pReg** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] [enum: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10] |
| **pSic** | **String**| Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4. | [optional] |
| **pNcs** | **String**| North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values. | [optional] |
| **pPen** | **String**| Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER &#x3D; No Penalties - ANY &#x3D; Any Penalty - LEXX &#x3D; Less than or equal to XX months.  Provide a number in place of XX, e.g. \&quot;LE5\&quot; for a facility with a penalty within previous 5 months. - GTXX &#x3D; Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago. | [optional] |
| **pC1lat** | **BigDecimal**| In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC1lon** | **BigDecimal**| In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC2lat** | **BigDecimal**| In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC2lon** | **BigDecimal**| In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pUsmex** | **String**| US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border. | [optional] [enum: Y, N] |
| **pSic2** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \&quot;22\&quot; to match all SIC codes beginning with 22.  Use the \&quot;%\&quot; character within strings to match any SIC values with the pattern.  For example, \&quot;2%21\&quot; matches 2021, 2121, 2221, etc. | [optional] |
| **pSic4** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker. | [optional] |
| **pFa** | **String**| Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values. | [optional] |
| **pFf** | **String**| Federal Facility Indicator Flag. Enter Y to restrict searches to federal facilities. | [optional] [enum: Y] |
| **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.  A Y will select ICIS NPDES permits with a status of effective, continued, or expired. | [optional] |
| **pMaj** | **String**| Major Facility Flag.  Enter Y to restrict results to Major facilities only. | [optional] [enum: Y, N] |
| **pMact** | **String**| CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility. | [optional] |
| **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pFeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] [enum: A, E, S] |
| **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pIeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S] |
| **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] [enum: 0, GT1, GT2, GT4, GT8, 12] |
| **pIv** | **String**| Facility has a violation status of &#39;In Viol&#39; during any of the selected quarters.   Range: Fiscal Year 2020 Quarter 2 to Fiscal Year 2017 Quarter 2  Multiple values are comma delimited.   ||||||  Fiscal Years |||||| - FY2020 or FY20 or 2020 or 20 - FY2019 or FY19 or 2019 or 19 - FY2018 or FY18 or 2018 or 18 - FY2017 or FY17 or 2017 or 17  ||||| Fiscal Quarters ||||| - FY2020Q2 or FY20Q2 or 20202 or 202 or 13 - FY2020Q1 or FY20Q1 or 20201 or 201 or 12 - FY2019Q4 or FY19Q4 or 20194 or 194 or 11 - FY2019Q3 or FY19Q3 or 20193 or 193 or 10 - FY2019Q2 or FY19Q2 or 20192 or 192 or 9 - FY2019Q1 or FY19Q1 or 20191 or 191 or 8 - FY2018Q4 or FY18Q4 or 20184 or 184 or 7 - FY2018Q3 or FY18Q3 or 20183 or 183 or 6 - FY2018Q2 or FY18Q2 or 20182 or 182 or 5 - FY2018Q1 or FY18Q1 or 20181 or 181 or 4 - FY2017Q4 or FY17Q4 or 20174 or 174 or 3 - FY2017Q3 or FY17Q3 or 20173 or 173 or 2 - FY2017Q2 or FY17Q2 or 20172 or 172 or 1 | [optional] |
| **pImpw** | **String**| Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database. | [optional] [enum: Y, N] |
| **pImpCauGrp** | **String**| Facility is discharging a pollutant group causing a waterbody to be impaired.  Enter 1 through 34 (the internal number of the pollutant group); or enter a partial name such as Dioxin,Temp,tUrBidity. | [optional] [enum: ALGAL GROWTH, AMMONIA, BIOTOXINS, CAUSE UNKNOWN, CAUSE UNKNOWN - FISH KILLS, CAUSE UNKNOWN - IMPAIRED BIOTA, CHLORINE, DIOXINS, FISH CONSUMPTION ADVISORY, FLOW ALTERATION(S), HABITAT ALTERATIONS, MERCURY, METALS (OTHER THAN MERCURY), NOXIOUS AQUATIC PLANTS, NUISANCE EXOTIC SPECIES, NUISANCE NATIVE SPECIES, NUTRIENTS, OIL AND GREASE, ORGANIC ENRICHMENT/OXYGEN DEPLETION, OTHER CAUSE, PATHOGENS, PESTICIDES, PH/ACIDITY/CAUSTIC CONDITIONS, POLYCHLORINATED BIPHENYLS (PCBS), RADIATION, SALINITY/TOTAL DISSOLVED SOLIDS/CHLORIDES/SULFATES, SEDIMENT, TASTE, COLOR AND ODOR, TEMPERATURE, TOTAL TOXICS, TOXIC INORGANICS, TOXIC ORGANICS, TRASH, TURBIDITY] |
| **pImpPol** | **String**| Facility is discharging pollutants that are potentially contributing to the impairment of local waterbodies according to the ATTAINS database. | [optional] [enum: Y, N] |
| **pTrep** | **String**| Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year. | [optional] [enum: CURR, NOTCURR] |
| **pPm** | **String**| Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75% | [optional] [enum: NONE, GT5, GT10, GT25, GT50, GT75] |
| **pPd** | **String**| Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile | [optional] [enum: NONE, GT100, GT500, GT1000, GT5000, GT10000, GT20000] |
| **pIco** | **String**| Indian Country Flag.  Enter a \&quot;Y\&quot; or \&quot;N\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] [enum: Y, N] |
| **pHuc** | **String**| 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values. | [optional] |
| **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] |
| **pMed** | **String**| Filter Results by Media. - A &#x3D; Air - M &#x3D; RMP (Risk Management Plan) - R &#x3D; RCRA (Hazardous Waste) - S &#x3D; SDWA (Public Drinking Water Systems) - ALL &#x3D; Air and RCRA and Water | [optional] [enum: A, M, R, S, ALL] |
| **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N, NV] |
| **pYsly** | **BigDecimal**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S, A] |
| **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] |
| **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] |
| **pTribeid** | **BigDecimal**| Numeric code for tribe (or list of tribes). | [optional] |
| **pTribename** | **String**| Tribe Name Filter.  Enter a single tribe name to filter results. | [optional] |
| **pTribedist** | **BigDecimal**| Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated. | [optional] |
| **pPstat** | **String**| Permit Status Filter.  Enter one or more of the following codes.  Provide multiple values as a comma-delimited list. - EFF &#x3D; Effective - EXP &#x3D; Expired - PND &#x3D; Pending - TRM &#x3D; Terminated - RET &#x3D; Retired - NON &#x3D; Not Needed - ADC &#x3D; Admin Continued | [optional] |
| **pPtype** | **String**| Permit Type Filter. Enter one or more code values to filter results.  Provide multiple values as a comma-delimited list. - NPD &#x3D; NPDES Individual Permit - NGP &#x3D; NPDES Master General Permit - GPC &#x3D; General Permit Covered Facility - SNN &#x3D; State Issued Master General Permit (Non-NPDES) - IIU &#x3D; Individual IU Permit (Non-NPDES) - SIN &#x3D; Individual State Issued Permit (Non-NPDES) - APR &#x3D; Associated Permit Record - UFT &#x3D; Unpermitted Facility | [optional] |
| **pPcomp** | **String**| Permit Component Code Filter.  Enter one or more codes to filter results.  Provide multiple values as a comma-delimited list. - PRE &#x3D; Pretreatment - CAF &#x3D; CAFO - CSO &#x3D; CSO - POT &#x3D; POTW - BIO &#x3D; Biosolids - SWS &#x3D; Storm Water Small MS4s - SWM &#x3D; Storm Water Medium/Large MS4s - SWI &#x3D; Storm Water Industrial - SWC &#x3D; Storm Water Construction | [optional] |
| **pPlimits** | **String**| Permit Limits Present Flag.  Enter Y to limit results to facilities have present permit limits. | [optional] [enum: Y, N] |
| **pPcss** | **String**| Combined Sewer Systems Outflows Limiter.  Enter one of the following to limit results to facilities having the given count of CSS outflows. - ALL &#x3D; returns all facilities, regardless of the number of outflows. - GE1 &#x3D; returns facilities with one or more outflows. - GE10 &#x3D; returns facilities with ten or more outflows. - GE50 &#x3D; returns facilities with fifty or more outflows. | [optional] [enum: ALL, GE1, GE10, GE50] |
| **pPexp** | **String**| Permit Expired or Administratively Continued Limiter.  Enter one of the following values to filter results. - EXP &#x3D; limit results to facilities with permits expired or administratively continued. - EXPLE1YR &#x3D; limit resuls to facilities with permits expired administratively continued within the past year. - EXPGT1YR &#x3D; limit resuls to facilities with permits expired administratively continued more than a year ago. | [optional] [enum: EXP, EXPLE1YR, EXPGT1YR] |
| **pOwop** | **String**| Owner/Operator code filter.  Enter one of the following values to restrict results. - Federal &#x3D; Federal facilities regulated under the NPDES program. - POTW &#x3D; Publicly owned treatment works. Treatment works that are owned by a State, Tribe, or municipality. - Non-POTW &#x3D; Non-publicly owned treatment works. Often referred to as \&quot;non-municipals\&quot; or \&quot;industrials\&quot;. | [optional] [enum: FEDERAL, POTW, NON-POTW] |
| **pIpfti** | **String**|  | [optional] |
| **pAgoo** | **String**| Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters. | [optional] [enum: AND, OR] |
| **pIdt1** | **String**| Beginning of date range of most recent facility inspection. | [optional] |
| **pIdt2** | **String**| End of date range of most recent facility inspection. | [optional] |
| **pPityp** | **String**| Inspection Type Code.  See ICIS Compliance Monitor Types lookup serivce for a list of available codes and descriptions. | [optional] |
| **pPfead1** | **String**| Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] |
| **pPfead2** | **String**| Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] |
| **pPfeat** | **String**| Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list. | [optional] |
| **pPccs** | **String**| Current Compliance Status: |||||||||||||||||||||||||||  Significant Noncompliance (SNC)  ||||||||||||||||||||||||||| - SNC &#x3D; E, S, X, T, D - E�&#x3D; E(EffViol) - S�&#x3D; S(CSchVio) - X &#x3D; X(EffNMth) - T &#x3D; T(CSchRpt) - D�&#x3D; D(DMR NR)  ||||||||||||||||||||||||||| Noncompliance (NC) ||||||||||||||||||||||||||| - NC &#x3D; N, V - N�&#x3D; N(RptViol) - V�&#x3D; V(NonRNCV)  ||||||||||||||||||||||||||| New Violations (PQV) ||||||||||||||||||||||||||| - PQV &#x3D; New Violations (13th Quarter)  ||||||||||||||||||||||||||| No Violations (NV) ||||||||||||||||||||||||||| - NV &#x3D; R, P, M, U, W , Blank, and No New Violations (no PQV) - R�&#x3D; R(Resolvd) - P�&#x3D; P(ResPend) - M�&#x3D; C(Manual) - U &#x3D; U(N/A) - W &#x3D; W(N/A) - Blank &#x3D; (null)  May contain multiple comma-separated values. | [optional] |
| **pPexcd** | **String**| 3-Year Effluent Exceedances Limiter.  Enter a value to restrict results to facilities with the given amount of exceedances in the past 3 years. - 0 &#x3D; facilities with no exceedances - GE0 &#x3D; facilities with one or more exceedances - GE10 &#x3D; facilities with ten or more exceedances - GE50 &#x3D; facilities with fifty or more exceedances - GE100 &#x3D; facilities with one hundred or more exceedances | [optional] [enum: 0, GE0, GE10, GE50, GE100] |
| **pPsncq** | **String**| Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z &#x3D; Zero quarters in significant noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in significant noncompliance. | [optional] [enum: GT1, GE1, GT2, GE2, GT4, GE4, GT8, GE8, GT12, GE12] |
| **pPctrack** | **String**| Compliance Tracking Limiter. Provide a keyword to indicate the extent to which data is being entered and effluent exceedances are being identified. - Off - Partial - On | [optional] [enum: false, Partial, true] |
| **pDwd** | **String**| Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory. | [optional] [enum: 0, GT0, GT1000, GT5000, GT10000, GT20000, GT50000] |
| **pPt** | **String**| POTW Transfers. Pounds of toxic chemicals transferred to a Publicly Operated Treatment Works (POTW) as reported to the Toxics Release Inventory. | [optional] [enum: 0, GT0, GT1000, GT5000, GT10000, GT20000, GT50000] |
| **pPdwdist** | **String**| Distance (in miles) to downstream drinking water intake. | [optional] [enum: N, LT1, LT2, LT5, LT10, LT15] |
| **pPswdpc** | **String**| Pollutant Category Code:  Values: WTR for Water, AIR for Air | [optional] |
| **pPswdmp** | **String**| Used to determine limit begin and end dates for surface water discharges. Number represents years from current date. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pPswpol** | **String**| For CWA, pollutant names for surface water discharges. for Drinking Water, SDWIS Violation contaminant codes for unaddressed violations that have occurred in the last 3 years. May contain multiple comma-separated values. | [optional] |
| **pPswcas** | **String**| CAS numbers for surface water discharges. May contain multiple comma-separated values. | [optional] |
| **pPswparam** | **String**| Parameter codes for surface water discharges. May contain multiple comma-separated values. | [optional] |
| **pPswvio** | **String**| Used in conjuction with parameters p_pswpol and p_pswparam, indicates whether search should only include pollutants with violations. | [optional] [enum: Y, N] |
| **pWbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] |
| **pRadwbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12 character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Will search against WBD values otained by \&quot;reach indexing\&quot; NPDES permits against the medium resolution National Hydrography Dataset.  | [optional] |
| **pFrswbd** | **String**| Works exactly the same as the p_wbd parameter.  2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] |
| **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] [enum: ALL, CONTAINS, EXACT, BEGINS] |
| **pPidall** | **String**| Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc). | [optional] [enum: Y, N] |
| **pMonthsLastDmr** | **BigDecimal**| The number of months since the last Discharge Monitoring Report has been submitted. | [optional] |
| **pLastDmrWithin** | **String**| W value returns facilities that have submitted DMRs within the number of months specified by p_months_last_dmr. An N value returns facilities that have not submitted a DMR within the specified number of months. | [optional] [enum: W, N] |
| **pIndsw** | **String**| Industrial Stormwater Permit Flag.  Enter a Y or N to filter results by this type of permit. | [optional] [enum: Y, N] |
| **pMsgpPtype** | **String**| Multi-Sector General Purpose Permit Type.  Enter a value to filter results by MSGP Permit Type. - NOI &#x3D; Notice of Intent - NOE &#x3D; No Exposure Certification | [optional] [enum: NOI, NOE] |
| **pMonType** | **String**| For use with the Industrial Stormwater search only. Valid values are BENCHGS fro Benchmark (Alert Limit) G2 Ore, BENCH for Benchmark (Alert Limit), and ELG fro Effluent Limitation Guidelines(ELG)(Effluent Limit).   | [optional] [enum: BENCHG2, BENCH, ELG] |
| **pIagency** | **String**| Issuing Agency Limiter.  Enter a single value to filter results by the issuing agency, e.g. \&quot;State\&quot; or \&quot;EPA\&quot;. | [optional] |
| **pPermittingAgency** | **String**|  | [optional] |
| **pIsws** | **String**| Multi-Sector General Purpose Permit Subsector Individual Identifier.  Enter a value to filter results. | [optional] |
| **pIswss** | **String**| Multi-Sector General Purpose Permit Subsector Group Code.  Enter a value to filter results. | [optional] |
| **pIswssID** | **String**| Multi-Sector General Purpose Permit Sector Code.  Enter a value to filter results. | [optional] |
| **pDs1** | **String**| Submitted Date Filter Start.  To filter by the date of submission, enter a start date here and an end date in the p_ds2 parameter.  Both dates are required for filtering. | [optional] |
| **pDs2** | **String**| Submitted Date Filter End.  To filter by the date of submission, enter an end date here and a start date in the p_ds1 parameter.  Both dates are required for filtering. | [optional] |
| **pDa1** | **String**| Active Date Filter Start.  To filter by the active date, enter a start date here and an end date in the p_da2 parameter.  Both dates are required for filtering. | [optional] |
| **pDa2** | **String**| Active Date Filter End.  To filter by the active date, enter an end date here and a start date in the p_da1 parameter.  Both dates are required for filtering. | [optional] |
| **pMS4** | **String**| Municipal Separate Storm Water Sewer (MS4) Permit Flag.  Enter a Y or N to filter results by this type of permit. | [optional] [enum: Y, N] |
| **pOoFN** | **String**| Owner/Operator Name. Enter the owner/operator name of the facility. | [optional] |
| **pOoFNtype** | **String**| Owner/Operator Name Multiple Selection Evaluator.   | [optional] [enum: ALL, EXACT, BEGINS, CONTAINS] |
| **pOoSA** | **String**| Owner/Operator Address.  Enter the address of the owner/operator of the facility. | [optional] |
| **pOoSA1** | **String**| Owner/Operator Address Line 2.  Enter the line 2 address of the owner/operator of the facility. | [optional] |
| **pOoCt** | **String**| Owner/Operator City. Enter the city where the owner/operator of the facility is located. | [optional] |
| **pOoSt** | **String**| Owner/Operator State.  Enter the standardized postal state code where the owner/operator of the facility is located. | [optional] |
| **pOoZip** | **String**| Owner/Operator Zip Code.  Enter the postal zip code where the owner/operator of the facility is located. | [optional] |
| **pFacIco** | **String**| FRS tribal land code flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land code. | [optional] [enum: Y, N] |
| **pIcoo** | **String**| Indian country search and/or flag.  Enter \&quot;Y\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned. | [optional] |
| **pFacIcos** | **String**| FRS tribal land spatial flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land spatial flag. | [optional] |
| **pEjscreen** | **String**| Enter \&quot;Y\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile. | [optional] |
| **pAlrexceed** | **BigDecimal**| Alert Limits Exceedences Limiter.  Enter a numeric value to restrict results to facilities having the given amount or more of alert limits exceedances. | [optional] |
| **pLimitAddr** | **String**| Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.   | [optional] [enum: Y, N] |
| **pLat** | **BigDecimal**| Latitude location in decimal degrees. | [optional] |
| **pLong** | **BigDecimal**| Longitude location in decimal degrees. | [optional] |
| **pRadius** | **BigDecimal**| Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities. | [optional] |
| **pEjscreenOver80cnt** | **String**| The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11. | [optional] [enum: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] |
| **pBioFlag** | **String**| A Y value will select all biosolid-related permits. | [optional] |
| **pBioFacType** | **String**| The code indicating the reporting obligation reason:  - POT &#x3D; A POTW with a design flow rate equal to or greater than one million gallons per day - CLI &#x3D; A Class I Sludge Management Facility as defined in 40 CFR 503.9 - PPL &#x3D; A POTW that serves 10,000 people or more - OTH &#x3D; Otherwise required to report (e.g., permit condition, enforcement action) - NOA &#x3D; None of the above | [optional] |
| **pBioTrtmntProcs** | **String**| The biosolids or sewage sludge treatment process or processes at the facility:  - AER &#x3D; Aerobic Digestion - AIR &#x3D; Air Drying (or Sludge Drying Beds) - ANA &#x3D; Anaerobic Digestion - COD &#x3D; Beta Ray Irradiation - COM &#x3D; Lower Temperature Composting - DEW &#x3D; Pasteurization - DIS &#x3D; Gamma Ray Irradiation - HEA &#x3D; Heat Drying (e.g., Flash Dryer, Spray Dryer, Rotary Dryer) - HET &#x3D; Heat Treatment (Liquid Sewage Sludge Heated to 356 Deg. F/180 Deg. C or Higher for 30 min.) - HTC &#x3D; Higher Temperature Composting - MET &#x3D; Methane or Biogas Capture and Recovery - OTH &#x3D; Other Treatment Process - PRE &#x3D; Preliminary Operations (e.g., Sludge Grinding, Degritting, Blending) - SLU &#x3D; Sludge Lagoon - STA &#x3D; Lime Stabilization - THE &#x3D; Temporary Sludge Storage (Sewage Sludge Stored on Land 2 Years or Less, Not in Sewage Sludge Unit) - THI &#x3D; Thickening (Gravity and/or Flotation Thickening, Centrifugation, Belt Filter Press, Vacuum Filter) - THM &#x3D; Thermophilic Aerobic Digestion - UND &#x3D; Long-Term Sludge Storage (Sewage Sludge Stored on Land 2 Years or More, not in Sewage Sludge Unit)\&quot; | [optional] |
| **pBioAnalyMethodCatgry** | **String**| The unique code for the category of the analytic methods used by the facility to analyze regulated parameters (including enteric viruses, fecal coliforms, helminth ova, and Salmonella sp.) at the facility:  - PAT &#x3D; Pathogens - MET &#x3D; Metals - NIT &#x3D; Nitrogen Compounds - OTH &#x3D; Other Analytes | [optional] |
| **pBioTotalVolumeAmt** | **String**| Total annual amount (in dry metric tons) of biosolids or sewage sludge generated at the facility.  - EQ0 &#x3D; 0 - IN0_1 &#x3D; GT 0 but LT 1 - IN0_289  &#x3D;  GT 0 but LT 290 MT/year - IN290_1499  &#x3D;  GE 290 but LT 1500 MT/year - IN1500_14999  &#x3D;  GE 1500 but LT 15,000 - GE15000  &#x3D;  GE 15,000 | [optional] |
| **pBioMgmtPrctceType** | **String**| The unique code that identifies the type of biosolids or sewage sludge management practice (e.g., land application, surface disposal, incineration) used by the facility. The facility will separately report the management practice for each biosolids or sewage sludge form and pathogen class. This data element will also identify the management practices used by surface disposal site owners/operators (see 40 CFR 503.24):  - BIN &#x3D; Incineration - BLN &#x3D; Land Application - BOT &#x3D; Other Management Practice - BSD &#x3D; Surface Disposal | [optional] |
| **pBioMgmtPrctceStype** | **String**| This is the code indicating additional detail about the type of Management Practice used for a volume of Biosolids or Sewage Sludge:  - ADV &#x3D; Advanced Alkaline Stabilized Biosolids Distribution &amp; Marketing - AGR &#x3D; Agricultural Land Application - COM &#x3D; Distribution and Marketing - Compost - DEE &#x3D; Deep-well Injection Disposal - DIS &#x3D; Disposal in a Municipal Landfill (under 40 CFR 258) - DMO &#x3D; Distribution and Marketing - Other - HEA &#x3D; Heat Dried Biosolids Distribution &amp; Marketing - OTL &#x3D; Other Land Application Management Practice Detail - OTO &#x3D; Other Management Practice Detail - RSA &#x3D; Reclamation Site Application - SEN &#x3D; Sent to Cement Kiln for Use as Alternative Energy - STO &#x3D; Storage - UIC &#x3D; Use in Construction - UPS &#x3D; Used in Production of Syngas - USE &#x3D; Use as Daily Cover for Municipal Landfill (under 40 CFR 258) | [optional] |
| **pBioMgmtPrctceHandler** | **String**| This is the code indicating the type of Biosolids or Sewage Sludge handlers/preparers.  - OWN &#x3D; Owner or Operator - OFF &#x3D; Off-Site Third-Party Handler or Preparer | [optional] |
| **pBioMgmtContainer** | **String**| The code that identifies the nature of each biosolids and sewage sludge material generated by the facility in terms of whether the material is a biosolid or sewage sludge and whether the material is ultimately conveyed off-site in bulk or in bags. The facility separately reports the form for each biosolids or sewage sludge management practice or practices used by the facility and pathogen class:  - BUL &#x3D; Bulk - BAG &#x3D; Bag or Container | [optional] |
| **pBioMgmtPathogen** | **String**| This code identifies the pathogen class [e.g., Class A, Class B, Not Applicable (Incineration)] for biosolids or sewage sludge generated by the facility. The facility will separately report the pathogen class for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form. It also is used to filter applicable Pathogen Reduction and Vector Attraction Reduction Options as well as Land Application Management Practice Deficiencies. Only reqired for some of the mgmt. practice types:  - AAA &#x3D; Class A - AEQ &#x3D; Class A EQ (sale/give away) - BBB &#x3D; Class B - NAP &#x3D; Not Applicable (Incineration) | [optional] |
| **pBioMgmtPathred** | **String**| This is the description of the option used by the facility to control pathogen for a Biosolids Management Practice:  - A1 &#x3D; Class A - Alternative 1: Time/Temperature - A2 &#x3D; Class A - Alternative 2: pH/Temperature/Percent Solids - A3 &#x3D; Class A - Alternative 3: Test Enteric Viruses and Helminth ova; Operating Parameters - A4 &#x3D; Class A - Alternative 4: Test Enteric Viruses and Helminth ova; No New Solids - A51 &#x3D; Class A - Alternative 5: PFRP 1: Composting - A52 &#x3D; Class A - Alternative 5: PFRP 2: Heat Drying - A53 &#x3D; Class A - Alternative 5: PFRP 3: Liquid heat treatment - A54 &#x3D; Class A - Alternative 5: PFRP 4: Thermophilic Aerobic Digestion (ATAD) - A55 &#x3D; Class A - Alternative 5 PFPR 5: Beta Ray Irradiation - A56 &#x3D; Class A - Alternative 5 PFPR 6: Gamma Ray Irradiation - A57 &#x3D; Class A - Alternative 5: PFRP 7: Pasteurization - A6 &#x3D; Class A - Alternative 6: PFRP Equivalency - B1 &#x3D; Class B - Alternative 1: Fecal Coliform Geometric Mean - B21 &#x3D; Class B - Alternative 2 PSRP 1: Aerobic Digestion - B22 &#x3D; Class B - Alternative 2 PSRP 2: Air Drying - B23 &#x3D; Class B - Alternative 2 PSRP 3: Anaerobic Digestion - B24 &#x3D; Class B - Alternative 2 PSRP 4: Composting - B25 &#x3D; Class B - Alternative 2 PSRP 5: Lime Stabilization - B3 &#x3D; Class B - Alternative 3: PSRP Equivalency - PH &#x3D; pH Adjustment (Domestic Septage) | [optional] |
| **pBioMgmtVector** | **String**| The unique code that identifies the option used by the facility for vector attraction reduction. See a listing of these vector attraction reduction options at 40 CFR 503.33(b)(1) through (11). The facility will separately report the vector attraction reduction options for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form as well as by each biosolids or sewage sludge pathogen class:  - VR1 &#x3D; Option 1 - Volatile Solids Reduction - VR2 &#x3D; Option 2 - Bench-Scale Volatile Solids Reduction (Anaerobic Bench Test) - VR3 &#x3D; Option 3 - Bench-Scale Volatile Solids Reduction (Aerobic Bench Test w/ Percent Solids - 2% or Less) - VR4 &#x3D; Option 4 - Specific Oxygen Uptake Rate - VR5 &#x3D; Option 5 - Aerobic Processing (Thermophilic Aerobic Digestion/Composting) - VR6 &#x3D; Option 6 - Alkaline Treatment - VR7 &#x3D; Option 7 - Drying (Equal to or Greater than 75 Percent) - VR8 &#x3D; Option 8 - Drying (Equal to or Greater than 90 Percent) - VR9 &#x3D; Option 9 - Sewage Sludge Injection - V10 &#x3D; Option 10 - Sewage Sludge Timely Incorporation into Land - V11 &#x3D; Option 11 - Sewage Sludge Covered at the End of Each Operating Day | [optional] |
| **pBioMgmtDefCategory** | **String**| This is the code indicating the type of NPDES special regulatory program deficiency:  - INC &#x3D; Biosolids Incineration - LNA &#x3D; Biosolids Land Application - LNB &#x3D; Biosolids Land Application - Pathogen Class B - OTB &#x3D; Biosolids Other Management Practice - SFD &#x3D; Biosolids Surface Disposal | [optional] |
| **pBioMgmtDeficiencies** | **BigDecimal**| The number of times noncompliance was reported by the facility in the last 3 years. The results returned will include facilities whose number of reported noncompliance events is greater than or equal to the number entered. | [optional] |
| **pBioVioCode** | **String**| The Biosolids Single Event Violation Code.  Enter one or mode codes. | [optional] |
| **pBioCurrentVio** | **String**| Indicator of whether the facility is currently in violation for biosolids under the Clean Water Act, in the 12th or 13th quarter:  - Y &#x3D; Yes - N &#x3D; No | [optional] [enum: Y, N] |
| **pBioQtrsInVio** | **BigDecimal**| The number of quarters, in the last three years, where the facility was in violation for a biosolids violation type.  The results returned will include facilities whose number of quarters with violations is greater than or equal to the number entered. | [optional] |
| **pBioRptYear** | **String**| The last year that the permittee submitted an annual Biosolids report.  Valid values are NONE and any year greater or equal to 2016. | [optional] |
| **pBioVioLastYear** | **String**| Identifies if a biosolids violation has occured in the last year.  Valid values are Y and N. | [optional] [enum: Y, N] |
| **pMsgpRptYear** | **String**| The last year that a MSGP report was submitted for the permit.  Valid values are \&quot;NONE\&quot; and any year Greater or Eqal to 2015. | [optional] |
| **pVioLastYear** | **String**| Identifies if a permit violation has occured in the last year.  Valid values are Y and N. | [optional] [enum: Y, N] |
| **queryset** | **BigDecimal**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] |
| **responseset** | **BigDecimal**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] |
| **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] [enum: Y, N] |
| **maplist** | **String**| Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria). | [optional] [enum: Y, N] |
| **summarylist** | **String**| Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service. | [optional] [enum: Y, N] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |
| **pE90Count** | **BigDecimal**| Number of E90 Exceedances.  Identifies water permits with a number of E90 (Effluient Exceedances) &gt;&#x3D; the value provided for the last number of years provided by the p_e90_years value. | [optional] |
| **pE90Years** | **BigDecimal**| Number of years for the p_e90_count search.  Identified the past number of years to be used for the p_e90_count search. | [optional] |
| **pPsc** | **String**| Point Source Category. | [optional] |

### Return type

[**CwaRestServicesGetFacilitiesGet200Response**](CwaRestServicesGetFacilitiesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are summary statistics for the query and a query identifier (QID). |  -  |

<a id="cwaRestServicesGetFacilitiesPost"></a>
# **cwaRestServicesGetFacilitiesPost**
> CwaRestServicesGetFacilitiesGet200Response cwaRestServicesGetFacilitiesPost(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pFrs, pReg, pSic, pNcs, pPen, pC1lat, pC1lon, pC2lat, pC2lon, pUsmex, pSic2, pSic4, pFa, pFf, pAct, pMaj, pMact, pFea, pFeay, pFeaa, pIea, pIeay, pIeaa, pQiv, pIv, pImpw, pImpCauGrp, pImpPol, pTrep, pPm, pPd, pIco, pHuc, pPid, pMed, pYsl, pYsly, pYsla, pQs, pSfs, pTribeid, pTribename, pTribedist, pPstat, pPtype, pPcomp, pPlimits, pPcss, pPexp, pOwop, pIpfti, pAgoo, pIdt1, pIdt2, pPityp, pPfead1, pPfead2, pPfeat, pPccs, pPexcd, pPsncq, pPctrack, pDwd, pPt, pPdwdist, pPswdpc, pPswdmp, pPswpol, pPswcas, pPswparam, pPswvio, pWbd, pRadwbd, pFrswbd, pFntype, pPidall, pMonthsLastDmr, pLastDmrWithin, pIndsw, pMsgpPtype, pMonType, pIagency, pPermittingAgency, pIsws, pIswss, pIswssID, pDs1, pDs2, pDa1, pDa2, pMS4, pOoFN, pOoFNtype, pOoSA, pOoSA1, pOoCt, pOoSt, pOoZip, pFacIco, pIcoo, pFacIcos, pEjscreen, pAlrexceed, pLimitAddr, pLat, pLong, pRadius, pEjscreenOver80cnt, pBioFlag, pBioFacType, pBioTrtmntProcs, pBioAnalyMethodCatgry, pBioTotalVolumeAmt, pBioMgmtPrctceType, pBioMgmtPrctceStype, pBioMgmtPrctceHandler, pBioMgmtContainer, pBioMgmtPathogen, pBioMgmtPathred, pBioMgmtVector, pBioMgmtDefCategory, pBioMgmtDeficiencies, pBioVioCode, pBioCurrentVio, pBioQtrsInVio, pBioRptYear, pBioVioLastYear, pMsgpRptYear, pVioLastYear, queryset, responseset, tablelist, maplist, summarylist, paramCallback, qcolumns, pE90Count, pE90Years, pPsc)

Clean Water Act (CWA) Facility Search Service

Validates query search parameters and returns query identifier.  Use the responseset parameter to set the page size

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInformationApi apiInstance = new FacilityInformationApi(defaultClient);
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String pFn = "pFn_example"; // String | Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
    String pSa = "pSa_example"; // String | Facility street address. Enter a complete or partial street address.
    String pSa1 = "pSa1_example"; // String | Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa.
    String pCt = "pCt_example"; // String | Facility City Filter. Enter a single case-insensitive city name to filter results.
    String pCo = "pCo_example"; // String | Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
    String pFips = "pFips_example"; // String | FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
    String pSt = "pSt_example"; // String | Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
    String pZip = "pZip_example"; // String | 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values.
    String pFrs = "pFrs_example"; // String | Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results.
    String pReg = "01"; // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    String pSic = "pSic_example"; // String | Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4.
    String pNcs = "pNcs_example"; // String | North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
    String pPen = "pPen_example"; // String | Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER = No Penalties - ANY = Any Penalty - LEXX = Less than or equal to XX months.  Provide a number in place of XX, e.g. \\\"LE5\\\" for a facility with a penalty within previous 5 months. - GTXX = Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago.
    BigDecimal pC1lat = new BigDecimal(78); // BigDecimal | In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC1lon = new BigDecimal(78); // BigDecimal | In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC2lat = new BigDecimal(78); // BigDecimal | In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC2lon = new BigDecimal(78); // BigDecimal | In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    String pUsmex = "Y"; // String | US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
    String pSic2 = "pSic2_example"; // String | Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \\\"22\\\" to match all SIC codes beginning with 22.  Use the \\\"%\\\" character within strings to match any SIC values with the pattern.  For example, \\\"2%21\\\" matches 2021, 2121, 2221, etc.
    String pSic4 = "pSic4_example"; // String | Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker.
    String pFa = "pFa_example"; // String | Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values.
    String pFf = "Y"; // String | Federal Facility Indicator Flag. Enter Y to restrict searches to federal facilities.
    String pAct = "pAct_example"; // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.  A Y will select ICIS NPDES permits with a status of effective, continued, or expired.
    String pMaj = "Y"; // String | Major Facility Flag.  Enter Y to restrict results to Major facilities only.
    String pMact = "pMact_example"; // String | CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility.
    String pFea = "W"; // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
    BigDecimal pFeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
    String pFeaa = "A"; // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
    String pIea = "W"; // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
    BigDecimal pIeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
    String pIeaa = "E"; // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
    String pQiv = "0"; // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    String pIv = "pIv_example"; // String | Facility has a violation status of 'In Viol' during any of the selected quarters.   Range: Fiscal Year 2020 Quarter 2 to Fiscal Year 2017 Quarter 2  Multiple values are comma delimited.   ||||||  Fiscal Years |||||| - FY2020 or FY20 or 2020 or 20 - FY2019 or FY19 or 2019 or 19 - FY2018 or FY18 or 2018 or 18 - FY2017 or FY17 or 2017 or 17  ||||| Fiscal Quarters ||||| - FY2020Q2 or FY20Q2 or 20202 or 202 or 13 - FY2020Q1 or FY20Q1 or 20201 or 201 or 12 - FY2019Q4 or FY19Q4 or 20194 or 194 or 11 - FY2019Q3 or FY19Q3 or 20193 or 193 or 10 - FY2019Q2 or FY19Q2 or 20192 or 192 or 9 - FY2019Q1 or FY19Q1 or 20191 or 191 or 8 - FY2018Q4 or FY18Q4 or 20184 or 184 or 7 - FY2018Q3 or FY18Q3 or 20183 or 183 or 6 - FY2018Q2 or FY18Q2 or 20182 or 182 or 5 - FY2018Q1 or FY18Q1 or 20181 or 181 or 4 - FY2017Q4 or FY17Q4 or 20174 or 174 or 3 - FY2017Q3 or FY17Q3 or 20173 or 173 or 2 - FY2017Q2 or FY17Q2 or 20172 or 172 or 1
    String pImpw = "Y"; // String | Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
    String pImpCauGrp = "ALGAL GROWTH"; // String | Facility is discharging a pollutant group causing a waterbody to be impaired.  Enter 1 through 34 (the internal number of the pollutant group); or enter a partial name such as Dioxin,Temp,tUrBidity.
    String pImpPol = "Y"; // String | Facility is discharging pollutants that are potentially contributing to the impairment of local waterbodies according to the ATTAINS database.
    String pTrep = "CURR"; // String | Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR = Current TRI reporter. - NONCURR = Has reported to TRI in the past but not for the current reporting year.
    String pPm = "NONE"; // String | Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE = 0% - GT5 = greater than 5% - GT10 = greater than 10% - GT25 = greater than 25% - GT50 = greater than 50% - GT75 = greater than 75%
    String pPd = "NONE"; // String | Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE = 0 population density per square mile - GT100 = More than 100 population density per square mile - GT500 = More than 500 population density per square mile - GT1000 = More than 1000 population density per square mile - GT5000 = More than 5000 population density per square mile - GT10000 = More than 10000 population density per square mile - GT20000 = More than 20000 population density per square mile
    String pIco = "Y"; // String | Indian Country Flag.  Enter a \\\"Y\\\" or \\\"N\\\" to restrict searches to facilities inside or outside Indian Country.
    String pHuc = "pHuc_example"; // String | 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
    String pPid = "pPid_example"; // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    String pMed = "A"; // String | Filter Results by Media. - A = Air - M = RMP (Risk Management Plan) - R = RCRA (Hazardous Waste) - S = SDWA (Public Drinking Water Systems) - ALL = Air and RCRA and Water
    String pYsl = "W"; // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
    BigDecimal pYsly = new BigDecimal("1"); // BigDecimal | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
    String pYsla = "E"; // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
    String pQs = "pQs_example"; // String | Quick Search. Allows entry for city, state, and/or zip code.
    String pSfs = "pSfs_example"; // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
    BigDecimal pTribeid = new BigDecimal(78); // BigDecimal | Numeric code for tribe (or list of tribes).
    String pTribename = "pTribename_example"; // String | Tribe Name Filter.  Enter a single tribe name to filter results.
    BigDecimal pTribedist = new BigDecimal(78); // BigDecimal | Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
    String pPstat = "pPstat_example"; // String | Permit Status Filter.  Enter one or more of the following codes.  Provide multiple values as a comma-delimited list. - EFF = Effective - EXP = Expired - PND = Pending - TRM = Terminated - RET = Retired - NON = Not Needed - ADC = Admin Continued
    String pPtype = "pPtype_example"; // String | Permit Type Filter. Enter one or more code values to filter results.  Provide multiple values as a comma-delimited list. - NPD = NPDES Individual Permit - NGP = NPDES Master General Permit - GPC = General Permit Covered Facility - SNN = State Issued Master General Permit (Non-NPDES) - IIU = Individual IU Permit (Non-NPDES) - SIN = Individual State Issued Permit (Non-NPDES) - APR = Associated Permit Record - UFT = Unpermitted Facility
    String pPcomp = "pPcomp_example"; // String | Permit Component Code Filter.  Enter one or more codes to filter results.  Provide multiple values as a comma-delimited list. - PRE = Pretreatment - CAF = CAFO - CSO = CSO - POT = POTW - BIO = Biosolids - SWS = Storm Water Small MS4s - SWM = Storm Water Medium/Large MS4s - SWI = Storm Water Industrial - SWC = Storm Water Construction
    String pPlimits = "Y"; // String | Permit Limits Present Flag.  Enter Y to limit results to facilities have present permit limits.
    String pPcss = "ALL"; // String | Combined Sewer Systems Outflows Limiter.  Enter one of the following to limit results to facilities having the given count of CSS outflows. - ALL = returns all facilities, regardless of the number of outflows. - GE1 = returns facilities with one or more outflows. - GE10 = returns facilities with ten or more outflows. - GE50 = returns facilities with fifty or more outflows.
    String pPexp = "EXP"; // String | Permit Expired or Administratively Continued Limiter.  Enter one of the following values to filter results. - EXP = limit results to facilities with permits expired or administratively continued. - EXPLE1YR = limit resuls to facilities with permits expired administratively continued within the past year. - EXPGT1YR = limit resuls to facilities with permits expired administratively continued more than a year ago.
    String pOwop = "FEDERAL"; // String | Owner/Operator code filter.  Enter one of the following values to restrict results. - Federal = Federal facilities regulated under the NPDES program. - POTW = Publicly owned treatment works. Treatment works that are owned by a State, Tribe, or municipality. - Non-POTW = Non-publicly owned treatment works. Often referred to as \\\"non-municipals\\\" or \\\"industrials\\\".
    String pIpfti = "pIpfti_example"; // String | 
    String pAgoo = "AND"; // String | Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
    String pIdt1 = "pIdt1_example"; // String | Beginning of date range of most recent facility inspection.
    String pIdt2 = "pIdt2_example"; // String | End of date range of most recent facility inspection.
    String pPityp = "pPityp_example"; // String | Inspection Type Code.  See ICIS Compliance Monitor Types lookup serivce for a list of available codes and descriptions.
    String pPfead1 = "pPfead1_example"; // String | Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    String pPfead2 = "pPfead2_example"; // String | Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    String pPfeat = "pPfeat_example"; // String | Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
    String pPccs = "pPccs_example"; // String | Current Compliance Status: |||||||||||||||||||||||||||  Significant Noncompliance (SNC)  ||||||||||||||||||||||||||| - SNC = E, S, X, T, D - E�= E(EffViol) - S�= S(CSchVio) - X = X(EffNMth) - T = T(CSchRpt) - D�= D(DMR NR)  ||||||||||||||||||||||||||| Noncompliance (NC) ||||||||||||||||||||||||||| - NC = N, V - N�= N(RptViol) - V�= V(NonRNCV)  ||||||||||||||||||||||||||| New Violations (PQV) ||||||||||||||||||||||||||| - PQV = New Violations (13th Quarter)  ||||||||||||||||||||||||||| No Violations (NV) ||||||||||||||||||||||||||| - NV = R, P, M, U, W , Blank, and No New Violations (no PQV) - R�= R(Resolvd) - P�= P(ResPend) - M�= C(Manual) - U = U(N/A) - W = W(N/A) - Blank = (null)  May contain multiple comma-separated values.
    String pPexcd = "0"; // String | 3-Year Effluent Exceedances Limiter.  Enter a value to restrict results to facilities with the given amount of exceedances in the past 3 years. - 0 = facilities with no exceedances - GE0 = facilities with one or more exceedances - GE10 = facilities with ten or more exceedances - GE50 = facilities with fifty or more exceedances - GE100 = facilities with one hundred or more exceedances
    String pPsncq = "GT1"; // String | Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z = Zero quarters in significant noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in significant noncompliance.
    String pPctrack = "false"; // String | Compliance Tracking Limiter. Provide a keyword to indicate the extent to which data is being entered and effluent exceedances are being identified. - Off - Partial - On
    String pDwd = "0"; // String | Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory.
    String pPt = "0"; // String | POTW Transfers. Pounds of toxic chemicals transferred to a Publicly Operated Treatment Works (POTW) as reported to the Toxics Release Inventory.
    String pPdwdist = "N"; // String | Distance (in miles) to downstream drinking water intake.
    String pPswdpc = "pPswdpc_example"; // String | Pollutant Category Code:  Values: WTR for Water, AIR for Air
    String pPswdmp = "1"; // String | Used to determine limit begin and end dates for surface water discharges. Number represents years from current date.
    String pPswpol = "pPswpol_example"; // String | For CWA, pollutant names for surface water discharges. for Drinking Water, SDWIS Violation contaminant codes for unaddressed violations that have occurred in the last 3 years. May contain multiple comma-separated values.
    String pPswcas = "pPswcas_example"; // String | CAS numbers for surface water discharges. May contain multiple comma-separated values.
    String pPswparam = "pPswparam_example"; // String | Parameter codes for surface water discharges. May contain multiple comma-separated values.
    String pPswvio = "Y"; // String | Used in conjuction with parameters p_pswpol and p_pswparam, indicates whether search should only include pollutants with violations.
    String pWbd = "pWbd_example"; // String | 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    String pRadwbd = "pRadwbd_example"; // String | 2-, 4-, 6-, 8-, 10-, or 12 character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Will search against WBD values otained by \\\"reach indexing\\\" NPDES permits against the medium resolution National Hydrography Dataset. 
    String pFrswbd = "pFrswbd_example"; // String | Works exactly the same as the p_wbd parameter.  2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    String pFntype = "ALL"; // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
    String pPidall = "Y"; // String | Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc).
    BigDecimal pMonthsLastDmr = new BigDecimal(78); // BigDecimal | The number of months since the last Discharge Monitoring Report has been submitted.
    String pLastDmrWithin = "W"; // String | W value returns facilities that have submitted DMRs within the number of months specified by p_months_last_dmr. An N value returns facilities that have not submitted a DMR within the specified number of months.
    String pIndsw = "Y"; // String | Industrial Stormwater Permit Flag.  Enter a Y or N to filter results by this type of permit.
    String pMsgpPtype = "NOI"; // String | Multi-Sector General Purpose Permit Type.  Enter a value to filter results by MSGP Permit Type. - NOI = Notice of Intent - NOE = No Exposure Certification
    String pMonType = "BENCHG2"; // String | For use with the Industrial Stormwater search only. Valid values are BENCHGS fro Benchmark (Alert Limit) G2 Ore, BENCH for Benchmark (Alert Limit), and ELG fro Effluent Limitation Guidelines(ELG)(Effluent Limit).  
    String pIagency = "pIagency_example"; // String | Issuing Agency Limiter.  Enter a single value to filter results by the issuing agency, e.g. \\\"State\\\" or \\\"EPA\\\".
    String pPermittingAgency = "pPermittingAgency_example"; // String | 
    String pIsws = "pIsws_example"; // String | Multi-Sector General Purpose Permit Subsector Individual Identifier.  Enter a value to filter results.
    String pIswss = "pIswss_example"; // String | Multi-Sector General Purpose Permit Subsector Group Code.  Enter a value to filter results.
    String pIswssID = "pIswssID_example"; // String | Multi-Sector General Purpose Permit Sector Code.  Enter a value to filter results.
    String pDs1 = "pDs1_example"; // String | Submitted Date Filter Start.  To filter by the date of submission, enter a start date here and an end date in the p_ds2 parameter.  Both dates are required for filtering.
    String pDs2 = "pDs2_example"; // String | Submitted Date Filter End.  To filter by the date of submission, enter an end date here and a start date in the p_ds1 parameter.  Both dates are required for filtering.
    String pDa1 = "pDa1_example"; // String | Active Date Filter Start.  To filter by the active date, enter a start date here and an end date in the p_da2 parameter.  Both dates are required for filtering.
    String pDa2 = "pDa2_example"; // String | Active Date Filter End.  To filter by the active date, enter an end date here and a start date in the p_da1 parameter.  Both dates are required for filtering.
    String pMS4 = "Y"; // String | Municipal Separate Storm Water Sewer (MS4) Permit Flag.  Enter a Y or N to filter results by this type of permit.
    String pOoFN = "pOoFN_example"; // String | Owner/Operator Name. Enter the owner/operator name of the facility.
    String pOoFNtype = "ALL"; // String | Owner/Operator Name Multiple Selection Evaluator.  
    String pOoSA = "pOoSA_example"; // String | Owner/Operator Address.  Enter the address of the owner/operator of the facility.
    String pOoSA1 = "pOoSA1_example"; // String | Owner/Operator Address Line 2.  Enter the line 2 address of the owner/operator of the facility.
    String pOoCt = "pOoCt_example"; // String | Owner/Operator City. Enter the city where the owner/operator of the facility is located.
    String pOoSt = "pOoSt_example"; // String | Owner/Operator State.  Enter the standardized postal state code where the owner/operator of the facility is located.
    String pOoZip = "pOoZip_example"; // String | Owner/Operator Zip Code.  Enter the postal zip code where the owner/operator of the facility is located.
    String pFacIco = "Y"; // String | FRS tribal land code flag.  Enter \\\"Y\\\" or \\\"N\\\" to include or exclude facilities based on FRS tribal land code.
    String pIcoo = "pIcoo_example"; // String | Indian country search and/or flag.  Enter \\\"Y\\\" to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
    String pFacIcos = "pFacIcos_example"; // String | FRS tribal land spatial flag.  Enter \\\"Y\\\" or \\\"N\\\" to include or exclude facilities based on FRS tribal land spatial flag.
    String pEjscreen = "pEjscreen_example"; // String | Enter \\\"Y\\\" to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
    BigDecimal pAlrexceed = new BigDecimal(78); // BigDecimal | Alert Limits Exceedences Limiter.  Enter a numeric value to restrict results to facilities having the given amount or more of alert limits exceedances.
    String pLimitAddr = "Y"; // String | Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
    BigDecimal pLat = new BigDecimal(78); // BigDecimal | Latitude location in decimal degrees.
    BigDecimal pLong = new BigDecimal(78); // BigDecimal | Longitude location in decimal degrees.
    BigDecimal pRadius = new BigDecimal(78); // BigDecimal | Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
    String pEjscreenOver80cnt = "1"; // String | The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
    String pBioFlag = "pBioFlag_example"; // String | A Y value will select all biosolid-related permits.
    String pBioFacType = "pBioFacType_example"; // String | The code indicating the reporting obligation reason:  - POT = A POTW with a design flow rate equal to or greater than one million gallons per day - CLI = A Class I Sludge Management Facility as defined in 40 CFR 503.9 - PPL = A POTW that serves 10,000 people or more - OTH = Otherwise required to report (e.g., permit condition, enforcement action) - NOA = None of the above
    String pBioTrtmntProcs = "pBioTrtmntProcs_example"; // String | The biosolids or sewage sludge treatment process or processes at the facility:  - AER = Aerobic Digestion - AIR = Air Drying (or Sludge Drying Beds) - ANA = Anaerobic Digestion - COD = Beta Ray Irradiation - COM = Lower Temperature Composting - DEW = Pasteurization - DIS = Gamma Ray Irradiation - HEA = Heat Drying (e.g., Flash Dryer, Spray Dryer, Rotary Dryer) - HET = Heat Treatment (Liquid Sewage Sludge Heated to 356 Deg. F/180 Deg. C or Higher for 30 min.) - HTC = Higher Temperature Composting - MET = Methane or Biogas Capture and Recovery - OTH = Other Treatment Process - PRE = Preliminary Operations (e.g., Sludge Grinding, Degritting, Blending) - SLU = Sludge Lagoon - STA = Lime Stabilization - THE = Temporary Sludge Storage (Sewage Sludge Stored on Land 2 Years or Less, Not in Sewage Sludge Unit) - THI = Thickening (Gravity and/or Flotation Thickening, Centrifugation, Belt Filter Press, Vacuum Filter) - THM = Thermophilic Aerobic Digestion - UND = Long-Term Sludge Storage (Sewage Sludge Stored on Land 2 Years or More, not in Sewage Sludge Unit)\\\"
    String pBioAnalyMethodCatgry = "pBioAnalyMethodCatgry_example"; // String | The unique code for the category of the analytic methods used by the facility to analyze regulated parameters (including enteric viruses, fecal coliforms, helminth ova, and Salmonella sp.) at the facility:  - PAT = Pathogens - MET = Metals - NIT = Nitrogen Compounds - OTH = Other Analytes
    String pBioTotalVolumeAmt = "pBioTotalVolumeAmt_example"; // String | Total annual amount (in dry metric tons) of biosolids or sewage sludge generated at the facility.  - EQ0 = 0 - IN0_1 = GT 0 but LT 1 - IN0_289  =  GT 0 but LT 290 MT/year - IN290_1499  =  GE 290 but LT 1500 MT/year - IN1500_14999  =  GE 1500 but LT 15,000 - GE15000  =  GE 15,000
    String pBioMgmtPrctceType = "pBioMgmtPrctceType_example"; // String | The unique code that identifies the type of biosolids or sewage sludge management practice (e.g., land application, surface disposal, incineration) used by the facility. The facility will separately report the management practice for each biosolids or sewage sludge form and pathogen class. This data element will also identify the management practices used by surface disposal site owners/operators (see 40 CFR 503.24):  - BIN = Incineration - BLN = Land Application - BOT = Other Management Practice - BSD = Surface Disposal
    String pBioMgmtPrctceStype = "pBioMgmtPrctceStype_example"; // String | This is the code indicating additional detail about the type of Management Practice used for a volume of Biosolids or Sewage Sludge:  - ADV = Advanced Alkaline Stabilized Biosolids Distribution & Marketing - AGR = Agricultural Land Application - COM = Distribution and Marketing - Compost - DEE = Deep-well Injection Disposal - DIS = Disposal in a Municipal Landfill (under 40 CFR 258) - DMO = Distribution and Marketing - Other - HEA = Heat Dried Biosolids Distribution & Marketing - OTL = Other Land Application Management Practice Detail - OTO = Other Management Practice Detail - RSA = Reclamation Site Application - SEN = Sent to Cement Kiln for Use as Alternative Energy - STO = Storage - UIC = Use in Construction - UPS = Used in Production of Syngas - USE = Use as Daily Cover for Municipal Landfill (under 40 CFR 258)
    String pBioMgmtPrctceHandler = "pBioMgmtPrctceHandler_example"; // String | This is the code indicating the type of Biosolids or Sewage Sludge handlers/preparers.  - OWN = Owner or Operator - OFF = Off-Site Third-Party Handler or Preparer
    String pBioMgmtContainer = "pBioMgmtContainer_example"; // String | The code that identifies the nature of each biosolids and sewage sludge material generated by the facility in terms of whether the material is a biosolid or sewage sludge and whether the material is ultimately conveyed off-site in bulk or in bags. The facility separately reports the form for each biosolids or sewage sludge management practice or practices used by the facility and pathogen class:  - BUL = Bulk - BAG = Bag or Container
    String pBioMgmtPathogen = "pBioMgmtPathogen_example"; // String | This code identifies the pathogen class [e.g., Class A, Class B, Not Applicable (Incineration)] for biosolids or sewage sludge generated by the facility. The facility will separately report the pathogen class for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form. It also is used to filter applicable Pathogen Reduction and Vector Attraction Reduction Options as well as Land Application Management Practice Deficiencies. Only reqired for some of the mgmt. practice types:  - AAA = Class A - AEQ = Class A EQ (sale/give away) - BBB = Class B - NAP = Not Applicable (Incineration)
    String pBioMgmtPathred = "pBioMgmtPathred_example"; // String | This is the description of the option used by the facility to control pathogen for a Biosolids Management Practice:  - A1 = Class A - Alternative 1: Time/Temperature - A2 = Class A - Alternative 2: pH/Temperature/Percent Solids - A3 = Class A - Alternative 3: Test Enteric Viruses and Helminth ova; Operating Parameters - A4 = Class A - Alternative 4: Test Enteric Viruses and Helminth ova; No New Solids - A51 = Class A - Alternative 5: PFRP 1: Composting - A52 = Class A - Alternative 5: PFRP 2: Heat Drying - A53 = Class A - Alternative 5: PFRP 3: Liquid heat treatment - A54 = Class A - Alternative 5: PFRP 4: Thermophilic Aerobic Digestion (ATAD) - A55 = Class A - Alternative 5 PFPR 5: Beta Ray Irradiation - A56 = Class A - Alternative 5 PFPR 6: Gamma Ray Irradiation - A57 = Class A - Alternative 5: PFRP 7: Pasteurization - A6 = Class A - Alternative 6: PFRP Equivalency - B1 = Class B - Alternative 1: Fecal Coliform Geometric Mean - B21 = Class B - Alternative 2 PSRP 1: Aerobic Digestion - B22 = Class B - Alternative 2 PSRP 2: Air Drying - B23 = Class B - Alternative 2 PSRP 3: Anaerobic Digestion - B24 = Class B - Alternative 2 PSRP 4: Composting - B25 = Class B - Alternative 2 PSRP 5: Lime Stabilization - B3 = Class B - Alternative 3: PSRP Equivalency - PH = pH Adjustment (Domestic Septage)
    String pBioMgmtVector = "pBioMgmtVector_example"; // String | The unique code that identifies the option used by the facility for vector attraction reduction. See a listing of these vector attraction reduction options at 40 CFR 503.33(b)(1) through (11). The facility will separately report the vector attraction reduction options for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form as well as by each biosolids or sewage sludge pathogen class:  - VR1 = Option 1 - Volatile Solids Reduction - VR2 = Option 2 - Bench-Scale Volatile Solids Reduction (Anaerobic Bench Test) - VR3 = Option 3 - Bench-Scale Volatile Solids Reduction (Aerobic Bench Test w/ Percent Solids - 2% or Less) - VR4 = Option 4 - Specific Oxygen Uptake Rate - VR5 = Option 5 - Aerobic Processing (Thermophilic Aerobic Digestion/Composting) - VR6 = Option 6 - Alkaline Treatment - VR7 = Option 7 - Drying (Equal to or Greater than 75 Percent) - VR8 = Option 8 - Drying (Equal to or Greater than 90 Percent) - VR9 = Option 9 - Sewage Sludge Injection - V10 = Option 10 - Sewage Sludge Timely Incorporation into Land - V11 = Option 11 - Sewage Sludge Covered at the End of Each Operating Day
    String pBioMgmtDefCategory = "pBioMgmtDefCategory_example"; // String | This is the code indicating the type of NPDES special regulatory program deficiency:  - INC = Biosolids Incineration - LNA = Biosolids Land Application - LNB = Biosolids Land Application - Pathogen Class B - OTB = Biosolids Other Management Practice - SFD = Biosolids Surface Disposal
    BigDecimal pBioMgmtDeficiencies = new BigDecimal(78); // BigDecimal | The number of times noncompliance was reported by the facility in the last 3 years. The results returned will include facilities whose number of reported noncompliance events is greater than or equal to the number entered.
    String pBioVioCode = "pBioVioCode_example"; // String | The Biosolids Single Event Violation Code.  Enter one or mode codes.
    String pBioCurrentVio = "Y"; // String | Indicator of whether the facility is currently in violation for biosolids under the Clean Water Act, in the 12th or 13th quarter:  - Y = Yes - N = No
    BigDecimal pBioQtrsInVio = new BigDecimal(78); // BigDecimal | The number of quarters, in the last three years, where the facility was in violation for a biosolids violation type.  The results returned will include facilities whose number of quarters with violations is greater than or equal to the number entered.
    String pBioRptYear = "pBioRptYear_example"; // String | The last year that the permittee submitted an annual Biosolids report.  Valid values are NONE and any year greater or equal to 2016.
    String pBioVioLastYear = "Y"; // String | Identifies if a biosolids violation has occured in the last year.  Valid values are Y and N.
    String pMsgpRptYear = "pMsgpRptYear_example"; // String | The last year that a MSGP report was submitted for the permit.  Valid values are \\\"NONE\\\" and any year Greater or Eqal to 2015.
    String pVioLastYear = "Y"; // String | Identifies if a permit violation has occured in the last year.  Valid values are Y and N.
    BigDecimal queryset = new BigDecimal(78); // BigDecimal | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    BigDecimal responseset = new BigDecimal(78); // BigDecimal | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    String tablelist = "Y"; // String | Table List Flag. Enter a Y to display the first page of facility results.
    String maplist = "Y"; // String | Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria).
    String summarylist = "Y"; // String | Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pE90Count = new BigDecimal(78); // BigDecimal | Number of E90 Exceedances.  Identifies water permits with a number of E90 (Effluient Exceedances) >= the value provided for the last number of years provided by the p_e90_years value.
    BigDecimal pE90Years = new BigDecimal(78); // BigDecimal | Number of years for the p_e90_count search.  Identified the past number of years to be used for the p_e90_count search.
    String pPsc = "pPsc_example"; // String | Point Source Category.
    try {
      CwaRestServicesGetFacilitiesGet200Response result = apiInstance.cwaRestServicesGetFacilitiesPost(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pFrs, pReg, pSic, pNcs, pPen, pC1lat, pC1lon, pC2lat, pC2lon, pUsmex, pSic2, pSic4, pFa, pFf, pAct, pMaj, pMact, pFea, pFeay, pFeaa, pIea, pIeay, pIeaa, pQiv, pIv, pImpw, pImpCauGrp, pImpPol, pTrep, pPm, pPd, pIco, pHuc, pPid, pMed, pYsl, pYsly, pYsla, pQs, pSfs, pTribeid, pTribename, pTribedist, pPstat, pPtype, pPcomp, pPlimits, pPcss, pPexp, pOwop, pIpfti, pAgoo, pIdt1, pIdt2, pPityp, pPfead1, pPfead2, pPfeat, pPccs, pPexcd, pPsncq, pPctrack, pDwd, pPt, pPdwdist, pPswdpc, pPswdmp, pPswpol, pPswcas, pPswparam, pPswvio, pWbd, pRadwbd, pFrswbd, pFntype, pPidall, pMonthsLastDmr, pLastDmrWithin, pIndsw, pMsgpPtype, pMonType, pIagency, pPermittingAgency, pIsws, pIswss, pIswssID, pDs1, pDs2, pDa1, pDa2, pMS4, pOoFN, pOoFNtype, pOoSA, pOoSA1, pOoCt, pOoSt, pOoZip, pFacIco, pIcoo, pFacIcos, pEjscreen, pAlrexceed, pLimitAddr, pLat, pLong, pRadius, pEjscreenOver80cnt, pBioFlag, pBioFacType, pBioTrtmntProcs, pBioAnalyMethodCatgry, pBioTotalVolumeAmt, pBioMgmtPrctceType, pBioMgmtPrctceStype, pBioMgmtPrctceHandler, pBioMgmtContainer, pBioMgmtPathogen, pBioMgmtPathred, pBioMgmtVector, pBioMgmtDefCategory, pBioMgmtDeficiencies, pBioVioCode, pBioCurrentVio, pBioQtrsInVio, pBioRptYear, pBioVioLastYear, pMsgpRptYear, pVioLastYear, queryset, responseset, tablelist, maplist, summarylist, paramCallback, qcolumns, pE90Count, pE90Years, pPsc);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInformationApi#cwaRestServicesGetFacilitiesPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **pFn** | **String**| Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers. | [optional] |
| **pSa** | **String**| Facility street address. Enter a complete or partial street address. | [optional] |
| **pSa1** | **String**| Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa. | [optional] |
| **pCt** | **String**| Facility City Filter. Enter a single case-insensitive city name to filter results. | [optional] |
| **pCo** | **String**| Facility County Filter. Provide a single county name in combination with a state value provided via p_st. | [optional] |
| **pFips** | **String**| FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059. | [optional] |
| **pSt** | **String**| Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pZip** | **String**| 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values. | [optional] |
| **pFrs** | **String**| Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results. | [optional] |
| **pReg** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] [enum: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10] |
| **pSic** | **String**| Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4. | [optional] |
| **pNcs** | **String**| North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values. | [optional] |
| **pPen** | **String**| Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER &#x3D; No Penalties - ANY &#x3D; Any Penalty - LEXX &#x3D; Less than or equal to XX months.  Provide a number in place of XX, e.g. \\\&quot;LE5\\\&quot; for a facility with a penalty within previous 5 months. - GTXX &#x3D; Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago. | [optional] |
| **pC1lat** | **BigDecimal**| In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC1lon** | **BigDecimal**| In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC2lat** | **BigDecimal**| In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC2lon** | **BigDecimal**| In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pUsmex** | **String**| US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border. | [optional] [enum: Y, N] |
| **pSic2** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \\\&quot;22\\\&quot; to match all SIC codes beginning with 22.  Use the \\\&quot;%\\\&quot; character within strings to match any SIC values with the pattern.  For example, \\\&quot;2%21\\\&quot; matches 2021, 2121, 2221, etc. | [optional] |
| **pSic4** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker. | [optional] |
| **pFa** | **String**| Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values. | [optional] |
| **pFf** | **String**| Federal Facility Indicator Flag. Enter Y to restrict searches to federal facilities. | [optional] [enum: Y] |
| **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.  A Y will select ICIS NPDES permits with a status of effective, continued, or expired. | [optional] |
| **pMaj** | **String**| Major Facility Flag.  Enter Y to restrict results to Major facilities only. | [optional] [enum: Y, N] |
| **pMact** | **String**| CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility. | [optional] |
| **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pFeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] [enum: A, E, S] |
| **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pIeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S] |
| **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] [enum: 0, GT1, GT2, GT4, GT8, 12] |
| **pIv** | **String**| Facility has a violation status of &#39;In Viol&#39; during any of the selected quarters.   Range: Fiscal Year 2020 Quarter 2 to Fiscal Year 2017 Quarter 2  Multiple values are comma delimited.   ||||||  Fiscal Years |||||| - FY2020 or FY20 or 2020 or 20 - FY2019 or FY19 or 2019 or 19 - FY2018 or FY18 or 2018 or 18 - FY2017 or FY17 or 2017 or 17  ||||| Fiscal Quarters ||||| - FY2020Q2 or FY20Q2 or 20202 or 202 or 13 - FY2020Q1 or FY20Q1 or 20201 or 201 or 12 - FY2019Q4 or FY19Q4 or 20194 or 194 or 11 - FY2019Q3 or FY19Q3 or 20193 or 193 or 10 - FY2019Q2 or FY19Q2 or 20192 or 192 or 9 - FY2019Q1 or FY19Q1 or 20191 or 191 or 8 - FY2018Q4 or FY18Q4 or 20184 or 184 or 7 - FY2018Q3 or FY18Q3 or 20183 or 183 or 6 - FY2018Q2 or FY18Q2 or 20182 or 182 or 5 - FY2018Q1 or FY18Q1 or 20181 or 181 or 4 - FY2017Q4 or FY17Q4 or 20174 or 174 or 3 - FY2017Q3 or FY17Q3 or 20173 or 173 or 2 - FY2017Q2 or FY17Q2 or 20172 or 172 or 1 | [optional] |
| **pImpw** | **String**| Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database. | [optional] [enum: Y, N] |
| **pImpCauGrp** | **String**| Facility is discharging a pollutant group causing a waterbody to be impaired.  Enter 1 through 34 (the internal number of the pollutant group); or enter a partial name such as Dioxin,Temp,tUrBidity. | [optional] [enum: ALGAL GROWTH, AMMONIA, BIOTOXINS, CAUSE UNKNOWN, CAUSE UNKNOWN - FISH KILLS, CAUSE UNKNOWN - IMPAIRED BIOTA, CHLORINE, DIOXINS, FISH CONSUMPTION ADVISORY, FLOW ALTERATION(S), HABITAT ALTERATIONS, MERCURY, METALS (OTHER THAN MERCURY), NOXIOUS AQUATIC PLANTS, NUISANCE EXOTIC SPECIES, NUISANCE NATIVE SPECIES, NUTRIENTS, OIL AND GREASE, ORGANIC ENRICHMENT/OXYGEN DEPLETION, OTHER CAUSE, PATHOGENS, PESTICIDES, PH/ACIDITY/CAUSTIC CONDITIONS, POLYCHLORINATED BIPHENYLS (PCBS), RADIATION, SALINITY/TOTAL DISSOLVED SOLIDS/CHLORIDES/SULFATES, SEDIMENT, TASTE, COLOR AND ODOR, TEMPERATURE, TOTAL TOXICS, TOXIC INORGANICS, TOXIC ORGANICS, TRASH, TURBIDITY] |
| **pImpPol** | **String**| Facility is discharging pollutants that are potentially contributing to the impairment of local waterbodies according to the ATTAINS database. | [optional] [enum: Y, N] |
| **pTrep** | **String**| Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year. | [optional] [enum: CURR, NOTCURR] |
| **pPm** | **String**| Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75% | [optional] [enum: NONE, GT5, GT10, GT25, GT50, GT75] |
| **pPd** | **String**| Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile | [optional] [enum: NONE, GT100, GT500, GT1000, GT5000, GT10000, GT20000] |
| **pIco** | **String**| Indian Country Flag.  Enter a \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] [enum: Y, N] |
| **pHuc** | **String**| 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values. | [optional] |
| **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] |
| **pMed** | **String**| Filter Results by Media. - A &#x3D; Air - M &#x3D; RMP (Risk Management Plan) - R &#x3D; RCRA (Hazardous Waste) - S &#x3D; SDWA (Public Drinking Water Systems) - ALL &#x3D; Air and RCRA and Water | [optional] [enum: A, M, R, S, ALL] |
| **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N, NV] |
| **pYsly** | **BigDecimal**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S, A] |
| **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] |
| **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] |
| **pTribeid** | **BigDecimal**| Numeric code for tribe (or list of tribes). | [optional] |
| **pTribename** | **String**| Tribe Name Filter.  Enter a single tribe name to filter results. | [optional] |
| **pTribedist** | **BigDecimal**| Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated. | [optional] |
| **pPstat** | **String**| Permit Status Filter.  Enter one or more of the following codes.  Provide multiple values as a comma-delimited list. - EFF &#x3D; Effective - EXP &#x3D; Expired - PND &#x3D; Pending - TRM &#x3D; Terminated - RET &#x3D; Retired - NON &#x3D; Not Needed - ADC &#x3D; Admin Continued | [optional] |
| **pPtype** | **String**| Permit Type Filter. Enter one or more code values to filter results.  Provide multiple values as a comma-delimited list. - NPD &#x3D; NPDES Individual Permit - NGP &#x3D; NPDES Master General Permit - GPC &#x3D; General Permit Covered Facility - SNN &#x3D; State Issued Master General Permit (Non-NPDES) - IIU &#x3D; Individual IU Permit (Non-NPDES) - SIN &#x3D; Individual State Issued Permit (Non-NPDES) - APR &#x3D; Associated Permit Record - UFT &#x3D; Unpermitted Facility | [optional] |
| **pPcomp** | **String**| Permit Component Code Filter.  Enter one or more codes to filter results.  Provide multiple values as a comma-delimited list. - PRE &#x3D; Pretreatment - CAF &#x3D; CAFO - CSO &#x3D; CSO - POT &#x3D; POTW - BIO &#x3D; Biosolids - SWS &#x3D; Storm Water Small MS4s - SWM &#x3D; Storm Water Medium/Large MS4s - SWI &#x3D; Storm Water Industrial - SWC &#x3D; Storm Water Construction | [optional] |
| **pPlimits** | **String**| Permit Limits Present Flag.  Enter Y to limit results to facilities have present permit limits. | [optional] [enum: Y, N] |
| **pPcss** | **String**| Combined Sewer Systems Outflows Limiter.  Enter one of the following to limit results to facilities having the given count of CSS outflows. - ALL &#x3D; returns all facilities, regardless of the number of outflows. - GE1 &#x3D; returns facilities with one or more outflows. - GE10 &#x3D; returns facilities with ten or more outflows. - GE50 &#x3D; returns facilities with fifty or more outflows. | [optional] [enum: ALL, GE1, GE10, GE50] |
| **pPexp** | **String**| Permit Expired or Administratively Continued Limiter.  Enter one of the following values to filter results. - EXP &#x3D; limit results to facilities with permits expired or administratively continued. - EXPLE1YR &#x3D; limit resuls to facilities with permits expired administratively continued within the past year. - EXPGT1YR &#x3D; limit resuls to facilities with permits expired administratively continued more than a year ago. | [optional] [enum: EXP, EXPLE1YR, EXPGT1YR] |
| **pOwop** | **String**| Owner/Operator code filter.  Enter one of the following values to restrict results. - Federal &#x3D; Federal facilities regulated under the NPDES program. - POTW &#x3D; Publicly owned treatment works. Treatment works that are owned by a State, Tribe, or municipality. - Non-POTW &#x3D; Non-publicly owned treatment works. Often referred to as \\\&quot;non-municipals\\\&quot; or \\\&quot;industrials\\\&quot;. | [optional] [enum: FEDERAL, POTW, NON-POTW] |
| **pIpfti** | **String**|  | [optional] |
| **pAgoo** | **String**| Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters. | [optional] [enum: AND, OR] |
| **pIdt1** | **String**| Beginning of date range of most recent facility inspection. | [optional] |
| **pIdt2** | **String**| End of date range of most recent facility inspection. | [optional] |
| **pPityp** | **String**| Inspection Type Code.  See ICIS Compliance Monitor Types lookup serivce for a list of available codes and descriptions. | [optional] |
| **pPfead1** | **String**| Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] |
| **pPfead2** | **String**| Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] |
| **pPfeat** | **String**| Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list. | [optional] |
| **pPccs** | **String**| Current Compliance Status: |||||||||||||||||||||||||||  Significant Noncompliance (SNC)  ||||||||||||||||||||||||||| - SNC &#x3D; E, S, X, T, D - E�&#x3D; E(EffViol) - S�&#x3D; S(CSchVio) - X &#x3D; X(EffNMth) - T &#x3D; T(CSchRpt) - D�&#x3D; D(DMR NR)  ||||||||||||||||||||||||||| Noncompliance (NC) ||||||||||||||||||||||||||| - NC &#x3D; N, V - N�&#x3D; N(RptViol) - V�&#x3D; V(NonRNCV)  ||||||||||||||||||||||||||| New Violations (PQV) ||||||||||||||||||||||||||| - PQV &#x3D; New Violations (13th Quarter)  ||||||||||||||||||||||||||| No Violations (NV) ||||||||||||||||||||||||||| - NV &#x3D; R, P, M, U, W , Blank, and No New Violations (no PQV) - R�&#x3D; R(Resolvd) - P�&#x3D; P(ResPend) - M�&#x3D; C(Manual) - U &#x3D; U(N/A) - W &#x3D; W(N/A) - Blank &#x3D; (null)  May contain multiple comma-separated values. | [optional] |
| **pPexcd** | **String**| 3-Year Effluent Exceedances Limiter.  Enter a value to restrict results to facilities with the given amount of exceedances in the past 3 years. - 0 &#x3D; facilities with no exceedances - GE0 &#x3D; facilities with one or more exceedances - GE10 &#x3D; facilities with ten or more exceedances - GE50 &#x3D; facilities with fifty or more exceedances - GE100 &#x3D; facilities with one hundred or more exceedances | [optional] [enum: 0, GE0, GE10, GE50, GE100] |
| **pPsncq** | **String**| Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z &#x3D; Zero quarters in significant noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in significant noncompliance. | [optional] [enum: GT1, GE1, GT2, GE2, GT4, GE4, GT8, GE8, GT12, GE12] |
| **pPctrack** | **String**| Compliance Tracking Limiter. Provide a keyword to indicate the extent to which data is being entered and effluent exceedances are being identified. - Off - Partial - On | [optional] [enum: false, Partial, true] |
| **pDwd** | **String**| Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory. | [optional] [enum: 0, GT0, GT1000, GT5000, GT10000, GT20000, GT50000] |
| **pPt** | **String**| POTW Transfers. Pounds of toxic chemicals transferred to a Publicly Operated Treatment Works (POTW) as reported to the Toxics Release Inventory. | [optional] [enum: 0, GT0, GT1000, GT5000, GT10000, GT20000, GT50000] |
| **pPdwdist** | **String**| Distance (in miles) to downstream drinking water intake. | [optional] [enum: N, LT1, LT2, LT5, LT10, LT15] |
| **pPswdpc** | **String**| Pollutant Category Code:  Values: WTR for Water, AIR for Air | [optional] |
| **pPswdmp** | **String**| Used to determine limit begin and end dates for surface water discharges. Number represents years from current date. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pPswpol** | **String**| For CWA, pollutant names for surface water discharges. for Drinking Water, SDWIS Violation contaminant codes for unaddressed violations that have occurred in the last 3 years. May contain multiple comma-separated values. | [optional] |
| **pPswcas** | **String**| CAS numbers for surface water discharges. May contain multiple comma-separated values. | [optional] |
| **pPswparam** | **String**| Parameter codes for surface water discharges. May contain multiple comma-separated values. | [optional] |
| **pPswvio** | **String**| Used in conjuction with parameters p_pswpol and p_pswparam, indicates whether search should only include pollutants with violations. | [optional] [enum: Y, N] |
| **pWbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] |
| **pRadwbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12 character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Will search against WBD values otained by \\\&quot;reach indexing\\\&quot; NPDES permits against the medium resolution National Hydrography Dataset.  | [optional] |
| **pFrswbd** | **String**| Works exactly the same as the p_wbd parameter.  2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] |
| **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] [enum: ALL, CONTAINS, EXACT, BEGINS] |
| **pPidall** | **String**| Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc). | [optional] [enum: Y, N] |
| **pMonthsLastDmr** | **BigDecimal**| The number of months since the last Discharge Monitoring Report has been submitted. | [optional] |
| **pLastDmrWithin** | **String**| W value returns facilities that have submitted DMRs within the number of months specified by p_months_last_dmr. An N value returns facilities that have not submitted a DMR within the specified number of months. | [optional] [enum: W, N] |
| **pIndsw** | **String**| Industrial Stormwater Permit Flag.  Enter a Y or N to filter results by this type of permit. | [optional] [enum: Y, N] |
| **pMsgpPtype** | **String**| Multi-Sector General Purpose Permit Type.  Enter a value to filter results by MSGP Permit Type. - NOI &#x3D; Notice of Intent - NOE &#x3D; No Exposure Certification | [optional] [enum: NOI, NOE] |
| **pMonType** | **String**| For use with the Industrial Stormwater search only. Valid values are BENCHGS fro Benchmark (Alert Limit) G2 Ore, BENCH for Benchmark (Alert Limit), and ELG fro Effluent Limitation Guidelines(ELG)(Effluent Limit).   | [optional] [enum: BENCHG2, BENCH, ELG] |
| **pIagency** | **String**| Issuing Agency Limiter.  Enter a single value to filter results by the issuing agency, e.g. \\\&quot;State\\\&quot; or \\\&quot;EPA\\\&quot;. | [optional] |
| **pPermittingAgency** | **String**|  | [optional] |
| **pIsws** | **String**| Multi-Sector General Purpose Permit Subsector Individual Identifier.  Enter a value to filter results. | [optional] |
| **pIswss** | **String**| Multi-Sector General Purpose Permit Subsector Group Code.  Enter a value to filter results. | [optional] |
| **pIswssID** | **String**| Multi-Sector General Purpose Permit Sector Code.  Enter a value to filter results. | [optional] |
| **pDs1** | **String**| Submitted Date Filter Start.  To filter by the date of submission, enter a start date here and an end date in the p_ds2 parameter.  Both dates are required for filtering. | [optional] |
| **pDs2** | **String**| Submitted Date Filter End.  To filter by the date of submission, enter an end date here and a start date in the p_ds1 parameter.  Both dates are required for filtering. | [optional] |
| **pDa1** | **String**| Active Date Filter Start.  To filter by the active date, enter a start date here and an end date in the p_da2 parameter.  Both dates are required for filtering. | [optional] |
| **pDa2** | **String**| Active Date Filter End.  To filter by the active date, enter an end date here and a start date in the p_da1 parameter.  Both dates are required for filtering. | [optional] |
| **pMS4** | **String**| Municipal Separate Storm Water Sewer (MS4) Permit Flag.  Enter a Y or N to filter results by this type of permit. | [optional] [enum: Y, N] |
| **pOoFN** | **String**| Owner/Operator Name. Enter the owner/operator name of the facility. | [optional] |
| **pOoFNtype** | **String**| Owner/Operator Name Multiple Selection Evaluator.   | [optional] [enum: ALL, EXACT, BEGINS, CONTAINS] |
| **pOoSA** | **String**| Owner/Operator Address.  Enter the address of the owner/operator of the facility. | [optional] |
| **pOoSA1** | **String**| Owner/Operator Address Line 2.  Enter the line 2 address of the owner/operator of the facility. | [optional] |
| **pOoCt** | **String**| Owner/Operator City. Enter the city where the owner/operator of the facility is located. | [optional] |
| **pOoSt** | **String**| Owner/Operator State.  Enter the standardized postal state code where the owner/operator of the facility is located. | [optional] |
| **pOoZip** | **String**| Owner/Operator Zip Code.  Enter the postal zip code where the owner/operator of the facility is located. | [optional] |
| **pFacIco** | **String**| FRS tribal land code flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land code. | [optional] [enum: Y, N] |
| **pIcoo** | **String**| Indian country search and/or flag.  Enter \\\&quot;Y\\\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned. | [optional] |
| **pFacIcos** | **String**| FRS tribal land spatial flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land spatial flag. | [optional] |
| **pEjscreen** | **String**| Enter \\\&quot;Y\\\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile. | [optional] |
| **pAlrexceed** | **BigDecimal**| Alert Limits Exceedences Limiter.  Enter a numeric value to restrict results to facilities having the given amount or more of alert limits exceedances. | [optional] |
| **pLimitAddr** | **String**| Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.   | [optional] [enum: Y, N] |
| **pLat** | **BigDecimal**| Latitude location in decimal degrees. | [optional] |
| **pLong** | **BigDecimal**| Longitude location in decimal degrees. | [optional] |
| **pRadius** | **BigDecimal**| Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities. | [optional] |
| **pEjscreenOver80cnt** | **String**| The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11. | [optional] [enum: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] |
| **pBioFlag** | **String**| A Y value will select all biosolid-related permits. | [optional] |
| **pBioFacType** | **String**| The code indicating the reporting obligation reason:  - POT &#x3D; A POTW with a design flow rate equal to or greater than one million gallons per day - CLI &#x3D; A Class I Sludge Management Facility as defined in 40 CFR 503.9 - PPL &#x3D; A POTW that serves 10,000 people or more - OTH &#x3D; Otherwise required to report (e.g., permit condition, enforcement action) - NOA &#x3D; None of the above | [optional] |
| **pBioTrtmntProcs** | **String**| The biosolids or sewage sludge treatment process or processes at the facility:  - AER &#x3D; Aerobic Digestion - AIR &#x3D; Air Drying (or Sludge Drying Beds) - ANA &#x3D; Anaerobic Digestion - COD &#x3D; Beta Ray Irradiation - COM &#x3D; Lower Temperature Composting - DEW &#x3D; Pasteurization - DIS &#x3D; Gamma Ray Irradiation - HEA &#x3D; Heat Drying (e.g., Flash Dryer, Spray Dryer, Rotary Dryer) - HET &#x3D; Heat Treatment (Liquid Sewage Sludge Heated to 356 Deg. F/180 Deg. C or Higher for 30 min.) - HTC &#x3D; Higher Temperature Composting - MET &#x3D; Methane or Biogas Capture and Recovery - OTH &#x3D; Other Treatment Process - PRE &#x3D; Preliminary Operations (e.g., Sludge Grinding, Degritting, Blending) - SLU &#x3D; Sludge Lagoon - STA &#x3D; Lime Stabilization - THE &#x3D; Temporary Sludge Storage (Sewage Sludge Stored on Land 2 Years or Less, Not in Sewage Sludge Unit) - THI &#x3D; Thickening (Gravity and/or Flotation Thickening, Centrifugation, Belt Filter Press, Vacuum Filter) - THM &#x3D; Thermophilic Aerobic Digestion - UND &#x3D; Long-Term Sludge Storage (Sewage Sludge Stored on Land 2 Years or More, not in Sewage Sludge Unit)\\\&quot; | [optional] |
| **pBioAnalyMethodCatgry** | **String**| The unique code for the category of the analytic methods used by the facility to analyze regulated parameters (including enteric viruses, fecal coliforms, helminth ova, and Salmonella sp.) at the facility:  - PAT &#x3D; Pathogens - MET &#x3D; Metals - NIT &#x3D; Nitrogen Compounds - OTH &#x3D; Other Analytes | [optional] |
| **pBioTotalVolumeAmt** | **String**| Total annual amount (in dry metric tons) of biosolids or sewage sludge generated at the facility.  - EQ0 &#x3D; 0 - IN0_1 &#x3D; GT 0 but LT 1 - IN0_289  &#x3D;  GT 0 but LT 290 MT/year - IN290_1499  &#x3D;  GE 290 but LT 1500 MT/year - IN1500_14999  &#x3D;  GE 1500 but LT 15,000 - GE15000  &#x3D;  GE 15,000 | [optional] |
| **pBioMgmtPrctceType** | **String**| The unique code that identifies the type of biosolids or sewage sludge management practice (e.g., land application, surface disposal, incineration) used by the facility. The facility will separately report the management practice for each biosolids or sewage sludge form and pathogen class. This data element will also identify the management practices used by surface disposal site owners/operators (see 40 CFR 503.24):  - BIN &#x3D; Incineration - BLN &#x3D; Land Application - BOT &#x3D; Other Management Practice - BSD &#x3D; Surface Disposal | [optional] |
| **pBioMgmtPrctceStype** | **String**| This is the code indicating additional detail about the type of Management Practice used for a volume of Biosolids or Sewage Sludge:  - ADV &#x3D; Advanced Alkaline Stabilized Biosolids Distribution &amp; Marketing - AGR &#x3D; Agricultural Land Application - COM &#x3D; Distribution and Marketing - Compost - DEE &#x3D; Deep-well Injection Disposal - DIS &#x3D; Disposal in a Municipal Landfill (under 40 CFR 258) - DMO &#x3D; Distribution and Marketing - Other - HEA &#x3D; Heat Dried Biosolids Distribution &amp; Marketing - OTL &#x3D; Other Land Application Management Practice Detail - OTO &#x3D; Other Management Practice Detail - RSA &#x3D; Reclamation Site Application - SEN &#x3D; Sent to Cement Kiln for Use as Alternative Energy - STO &#x3D; Storage - UIC &#x3D; Use in Construction - UPS &#x3D; Used in Production of Syngas - USE &#x3D; Use as Daily Cover for Municipal Landfill (under 40 CFR 258) | [optional] |
| **pBioMgmtPrctceHandler** | **String**| This is the code indicating the type of Biosolids or Sewage Sludge handlers/preparers.  - OWN &#x3D; Owner or Operator - OFF &#x3D; Off-Site Third-Party Handler or Preparer | [optional] |
| **pBioMgmtContainer** | **String**| The code that identifies the nature of each biosolids and sewage sludge material generated by the facility in terms of whether the material is a biosolid or sewage sludge and whether the material is ultimately conveyed off-site in bulk or in bags. The facility separately reports the form for each biosolids or sewage sludge management practice or practices used by the facility and pathogen class:  - BUL &#x3D; Bulk - BAG &#x3D; Bag or Container | [optional] |
| **pBioMgmtPathogen** | **String**| This code identifies the pathogen class [e.g., Class A, Class B, Not Applicable (Incineration)] for biosolids or sewage sludge generated by the facility. The facility will separately report the pathogen class for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form. It also is used to filter applicable Pathogen Reduction and Vector Attraction Reduction Options as well as Land Application Management Practice Deficiencies. Only reqired for some of the mgmt. practice types:  - AAA &#x3D; Class A - AEQ &#x3D; Class A EQ (sale/give away) - BBB &#x3D; Class B - NAP &#x3D; Not Applicable (Incineration) | [optional] |
| **pBioMgmtPathred** | **String**| This is the description of the option used by the facility to control pathogen for a Biosolids Management Practice:  - A1 &#x3D; Class A - Alternative 1: Time/Temperature - A2 &#x3D; Class A - Alternative 2: pH/Temperature/Percent Solids - A3 &#x3D; Class A - Alternative 3: Test Enteric Viruses and Helminth ova; Operating Parameters - A4 &#x3D; Class A - Alternative 4: Test Enteric Viruses and Helminth ova; No New Solids - A51 &#x3D; Class A - Alternative 5: PFRP 1: Composting - A52 &#x3D; Class A - Alternative 5: PFRP 2: Heat Drying - A53 &#x3D; Class A - Alternative 5: PFRP 3: Liquid heat treatment - A54 &#x3D; Class A - Alternative 5: PFRP 4: Thermophilic Aerobic Digestion (ATAD) - A55 &#x3D; Class A - Alternative 5 PFPR 5: Beta Ray Irradiation - A56 &#x3D; Class A - Alternative 5 PFPR 6: Gamma Ray Irradiation - A57 &#x3D; Class A - Alternative 5: PFRP 7: Pasteurization - A6 &#x3D; Class A - Alternative 6: PFRP Equivalency - B1 &#x3D; Class B - Alternative 1: Fecal Coliform Geometric Mean - B21 &#x3D; Class B - Alternative 2 PSRP 1: Aerobic Digestion - B22 &#x3D; Class B - Alternative 2 PSRP 2: Air Drying - B23 &#x3D; Class B - Alternative 2 PSRP 3: Anaerobic Digestion - B24 &#x3D; Class B - Alternative 2 PSRP 4: Composting - B25 &#x3D; Class B - Alternative 2 PSRP 5: Lime Stabilization - B3 &#x3D; Class B - Alternative 3: PSRP Equivalency - PH &#x3D; pH Adjustment (Domestic Septage) | [optional] |
| **pBioMgmtVector** | **String**| The unique code that identifies the option used by the facility for vector attraction reduction. See a listing of these vector attraction reduction options at 40 CFR 503.33(b)(1) through (11). The facility will separately report the vector attraction reduction options for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form as well as by each biosolids or sewage sludge pathogen class:  - VR1 &#x3D; Option 1 - Volatile Solids Reduction - VR2 &#x3D; Option 2 - Bench-Scale Volatile Solids Reduction (Anaerobic Bench Test) - VR3 &#x3D; Option 3 - Bench-Scale Volatile Solids Reduction (Aerobic Bench Test w/ Percent Solids - 2% or Less) - VR4 &#x3D; Option 4 - Specific Oxygen Uptake Rate - VR5 &#x3D; Option 5 - Aerobic Processing (Thermophilic Aerobic Digestion/Composting) - VR6 &#x3D; Option 6 - Alkaline Treatment - VR7 &#x3D; Option 7 - Drying (Equal to or Greater than 75 Percent) - VR8 &#x3D; Option 8 - Drying (Equal to or Greater than 90 Percent) - VR9 &#x3D; Option 9 - Sewage Sludge Injection - V10 &#x3D; Option 10 - Sewage Sludge Timely Incorporation into Land - V11 &#x3D; Option 11 - Sewage Sludge Covered at the End of Each Operating Day | [optional] |
| **pBioMgmtDefCategory** | **String**| This is the code indicating the type of NPDES special regulatory program deficiency:  - INC &#x3D; Biosolids Incineration - LNA &#x3D; Biosolids Land Application - LNB &#x3D; Biosolids Land Application - Pathogen Class B - OTB &#x3D; Biosolids Other Management Practice - SFD &#x3D; Biosolids Surface Disposal | [optional] |
| **pBioMgmtDeficiencies** | **BigDecimal**| The number of times noncompliance was reported by the facility in the last 3 years. The results returned will include facilities whose number of reported noncompliance events is greater than or equal to the number entered. | [optional] |
| **pBioVioCode** | **String**| The Biosolids Single Event Violation Code.  Enter one or mode codes. | [optional] |
| **pBioCurrentVio** | **String**| Indicator of whether the facility is currently in violation for biosolids under the Clean Water Act, in the 12th or 13th quarter:  - Y &#x3D; Yes - N &#x3D; No | [optional] [enum: Y, N] |
| **pBioQtrsInVio** | **BigDecimal**| The number of quarters, in the last three years, where the facility was in violation for a biosolids violation type.  The results returned will include facilities whose number of quarters with violations is greater than or equal to the number entered. | [optional] |
| **pBioRptYear** | **String**| The last year that the permittee submitted an annual Biosolids report.  Valid values are NONE and any year greater or equal to 2016. | [optional] |
| **pBioVioLastYear** | **String**| Identifies if a biosolids violation has occured in the last year.  Valid values are Y and N. | [optional] [enum: Y, N] |
| **pMsgpRptYear** | **String**| The last year that a MSGP report was submitted for the permit.  Valid values are \\\&quot;NONE\\\&quot; and any year Greater or Eqal to 2015. | [optional] |
| **pVioLastYear** | **String**| Identifies if a permit violation has occured in the last year.  Valid values are Y and N. | [optional] [enum: Y, N] |
| **queryset** | **BigDecimal**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] |
| **responseset** | **BigDecimal**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] |
| **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] [enum: Y, N] |
| **maplist** | **String**| Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria). | [optional] [enum: Y, N] |
| **summarylist** | **String**| Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service. | [optional] [enum: Y, N] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |
| **pE90Count** | **BigDecimal**| Number of E90 Exceedances.  Identifies water permits with a number of E90 (Effluient Exceedances) &gt;&#x3D; the value provided for the last number of years provided by the p_e90_years value. | [optional] |
| **pE90Years** | **BigDecimal**| Number of years for the p_e90_count search.  Identified the past number of years to be used for the p_e90_count search. | [optional] |
| **pPsc** | **String**| Point Source Category. | [optional] |

### Return type

[**CwaRestServicesGetFacilitiesGet200Response**](CwaRestServicesGetFacilitiesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are summary statistics for the query and a query identifier (QID). |  -  |

<a id="cwaRestServicesGetFacilityInfoGet"></a>
# **cwaRestServicesGetFacilityInfoGet**
> CwaRestServicesGetFacilityInfoGet200Response cwaRestServicesGetFacilityInfoGet(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pFrs, pReg, pSic, pNcs, pPen, xmin, ymin, xmax, ymax, pUsmex, pSic2, pSic4, pFa, pFf, pAct, pMaj, pMact, pFea, pFeay, pFeaa, pIea, pIeay, pIeaa, pQiv, pIv, pImpw, pImpPol, pImpCauGrp, pTrep, pPm, pPd, pIco, pHuc, pPid, pMed, pYsl, pYsly, pYsla, pQs, pSfs, pTribeid, pTribename, pTribedist, pPstat, pPtype, pPcomp, pPlimits, pPcss, pPexp, pOwop, pIpfti, pAgoo, pIdt1, pIdt2, pPityp, pPfead1, pPfead2, pPfeat, pPccs, pPexcd, pPsncq, pPctrack, pDwd, pPt, pPdwdist, pPswdpc, pPswdmp, pPswpol, pPswcas, pPswparam, pPswvio, pWbd, pRadwbd, pFrswbd, pFntype, pPidall, pMonthsLastDmr, pLastDmrWithin, pIndsw, pMsgpPtype, pMonType, pIagency, pPermittingAgency, pIsws, pIswss, pIswssID, pDs1, pDs2, pDa1, pDa2, pMS4, pOoFN, pOoFNtype, pOoSA, pOoSA1, pOoCt, pOoSt, pOoZip, pFacIco, pIcoo, pFacIcos, pEjscreen, pAlrexceed, pLimitAddr, pLat, pLong, pRadius, pEjscreenOver80cnt, pBioFlag, pBioFacType, pBioTrtmntProcs, pBioAnalyMethodCatgry, pBioTotalVolumeAmt, pBioMgmtPrctceType, pBioMgmtPrctceStype, pBioMgmtPrctceHandler, pBioMgmtContainer, pBioMgmtPathogen, pBioMgmtPathred, pBioMgmtVector, pBioMgmtDefCategory, pBioMgmtDeficiencies, pBioVioCode, pBioCurrentVio, pBioQtrsInVio, pBioRptYear, pBioVioLastYear, pMsgpRptYear, pVioLastYear, responseset, paramCallback, qcolumns, pPrettyPrint, pE90Count, pE90Years, pPsc)

Clean Water Act (CWA) Facility Enhanced Search Service

Returns either an array of Facilities or an array of Clusters that meet the specified search criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInformationApi apiInstance = new FacilityInformationApi(defaultClient);
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language. - CSV = Facility results formatted as comma delimited file download. - GEOJSON = Facility results formatted as GeoJSON feature collection. - GEOJSONP = Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
    String pFn = "pFn_example"; // String | Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
    String pSa = "pSa_example"; // String | Facility street address. Enter a complete or partial street address.
    String pSa1 = "pSa1_example"; // String | Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa.
    String pCt = "pCt_example"; // String | Facility City Filter. Enter a single case-insensitive city name to filter results.
    String pCo = "pCo_example"; // String | Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
    String pFips = "pFips_example"; // String | FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
    String pSt = "pSt_example"; // String | Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
    String pZip = "pZip_example"; // String | 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values.
    String pFrs = "pFrs_example"; // String | Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results.
    String pReg = "01"; // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    String pSic = "pSic_example"; // String | Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4.
    String pNcs = "pNcs_example"; // String | North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
    String pPen = "pPen_example"; // String | Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER = No Penalties - ANY = Any Penalty - LEXX = Less than or equal to XX months.  Provide a number in place of XX, e.g. \"LE5\" for a facility with a penalty within previous 5 months. - GTXX = Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago.
    BigDecimal xmin = new BigDecimal(78); // BigDecimal | Minimum longitude value in decimal degrees.
    BigDecimal ymin = new BigDecimal(78); // BigDecimal | Minimum latitude value in decimal degrees.
    BigDecimal xmax = new BigDecimal(78); // BigDecimal | Maximum longitude value in decimal degrees.
    BigDecimal ymax = new BigDecimal(78); // BigDecimal | Maximum latitude value in decimal degrees.
    String pUsmex = "Y"; // String | US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
    String pSic2 = "pSic2_example"; // String | Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \"22\" to match all SIC codes beginning with 22.  Use the \"%\" character within strings to match any SIC values with the pattern.  For example, \"2%21\" matches 2021, 2121, 2221, etc.
    String pSic4 = "pSic4_example"; // String | Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker.
    String pFa = "pFa_example"; // String | Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values.
    String pFf = "Y"; // String | Federal Facility Indicator Flag. Enter Y to restrict searches to federal facilities.
    String pAct = "pAct_example"; // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.  A Y will select ICIS NPDES permits with a status of effective, continued, or expired.
    String pMaj = "Y"; // String | Major Facility Flag.  Enter Y to restrict results to Major facilities only.
    String pMact = "pMact_example"; // String | CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility.
    String pFea = "W"; // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
    BigDecimal pFeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
    String pFeaa = "A"; // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
    String pIea = "W"; // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
    BigDecimal pIeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
    String pIeaa = "E"; // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
    String pQiv = "0"; // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    String pIv = "pIv_example"; // String | Facility has a violation status of 'In Viol' during any of the selected quarters.   Range: Fiscal Year 2020 Quarter 2 to Fiscal Year 2017 Quarter 2  Multiple values are comma delimited.   ||||||  Fiscal Years |||||| - FY2020 or FY20 or 2020 or 20 - FY2019 or FY19 or 2019 or 19 - FY2018 or FY18 or 2018 or 18 - FY2017 or FY17 or 2017 or 17  ||||| Fiscal Quarters ||||| - FY2020Q2 or FY20Q2 or 20202 or 202 or 13 - FY2020Q1 or FY20Q1 or 20201 or 201 or 12 - FY2019Q4 or FY19Q4 or 20194 or 194 or 11 - FY2019Q3 or FY19Q3 or 20193 or 193 or 10 - FY2019Q2 or FY19Q2 or 20192 or 192 or 9 - FY2019Q1 or FY19Q1 or 20191 or 191 or 8 - FY2018Q4 or FY18Q4 or 20184 or 184 or 7 - FY2018Q3 or FY18Q3 or 20183 or 183 or 6 - FY2018Q2 or FY18Q2 or 20182 or 182 or 5 - FY2018Q1 or FY18Q1 or 20181 or 181 or 4 - FY2017Q4 or FY17Q4 or 20174 or 174 or 3 - FY2017Q3 or FY17Q3 or 20173 or 173 or 2 - FY2017Q2 or FY17Q2 or 20172 or 172 or 1
    String pImpw = "Y"; // String | Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
    String pImpPol = "Y"; // String | Facility is discharging pollutants that are potentially contributing to the impairment of local waterbodies according to the ATTAINS database.
    String pImpCauGrp = "ALGAL GROWTH"; // String | Facility is discharging a pollutant group causing a waterbody to be impaired.  Enter 1 through 34 (the internal number of the pollutant group); or enter a partial name such as Dioxin,Temp,tUrBidity.
    String pTrep = "CURR"; // String | Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR = Current TRI reporter. - NONCURR = Has reported to TRI in the past but not for the current reporting year.
    String pPm = "NONE"; // String | Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE = 0% - GT5 = greater than 5% - GT10 = greater than 10% - GT25 = greater than 25% - GT50 = greater than 50% - GT75 = greater than 75%
    String pPd = "NONE"; // String | Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE = 0 population density per square mile - GT100 = More than 100 population density per square mile - GT500 = More than 500 population density per square mile - GT1000 = More than 1000 population density per square mile - GT5000 = More than 5000 population density per square mile - GT10000 = More than 10000 population density per square mile - GT20000 = More than 20000 population density per square mile
    String pIco = "Y"; // String | Indian Country Flag.  Enter a \"Y\" or \"N\" to restrict searches to facilities inside or outside Indian Country.
    String pHuc = "pHuc_example"; // String | 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
    String pPid = "pPid_example"; // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    String pMed = "A"; // String | Filter Results by Media. - A = Air - M = RMP (Risk Management Plan) - R = RCRA (Hazardous Waste) - S = SDWA (Public Drinking Water Systems) - ALL = Air and RCRA and Water
    String pYsl = "W"; // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
    BigDecimal pYsly = new BigDecimal("1"); // BigDecimal | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
    String pYsla = "E"; // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
    String pQs = "pQs_example"; // String | Quick Search. Allows entry for city, state, and/or zip code.
    String pSfs = "pSfs_example"; // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
    BigDecimal pTribeid = new BigDecimal(78); // BigDecimal | Numeric code for tribe (or list of tribes).
    String pTribename = "pTribename_example"; // String | Tribe Name Filter.  Enter a single tribe name to filter results.
    BigDecimal pTribedist = new BigDecimal(78); // BigDecimal | Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
    String pPstat = "pPstat_example"; // String | Permit Status Filter.  Enter one or more of the following codes.  Provide multiple values as a comma-delimited list. - EFF = Effective - EXP = Expired - PND = Pending - TRM = Terminated - RET = Retired - NON = Not Needed - ADC = Admin Continued
    String pPtype = "pPtype_example"; // String | Permit Type Filter. Enter one or more code values to filter results.  Provide multiple values as a comma-delimited list. - NPD = NPDES Individual Permit - NGP = NPDES Master General Permit - GPC = General Permit Covered Facility - SNN = State Issued Master General Permit (Non-NPDES) - IIU = Individual IU Permit (Non-NPDES) - SIN = Individual State Issued Permit (Non-NPDES) - APR = Associated Permit Record - UFT = Unpermitted Facility
    String pPcomp = "pPcomp_example"; // String | Permit Component Code Filter.  Enter one or more codes to filter results.  Provide multiple values as a comma-delimited list. - PRE = Pretreatment - CAF = CAFO - CSO = CSO - POT = POTW - BIO = Biosolids - SWS = Storm Water Small MS4s - SWM = Storm Water Medium/Large MS4s - SWI = Storm Water Industrial - SWC = Storm Water Construction
    String pPlimits = "Y"; // String | Permit Limits Present Flag.  Enter Y to limit results to facilities have present permit limits.
    String pPcss = "ALL"; // String | Combined Sewer Systems Outflows Limiter.  Enter one of the following to limit results to facilities having the given count of CSS outflows. - ALL = returns all facilities, regardless of the number of outflows. - GE1 = returns facilities with one or more outflows. - GE10 = returns facilities with ten or more outflows. - GE50 = returns facilities with fifty or more outflows.
    String pPexp = "EXP"; // String | Permit Expired or Administratively Continued Limiter.  Enter one of the following values to filter results. - EXP = limit results to facilities with permits expired or administratively continued. - EXPLE1YR = limit resuls to facilities with permits expired administratively continued within the past year. - EXPGT1YR = limit resuls to facilities with permits expired administratively continued more than a year ago.
    String pOwop = "FEDERAL"; // String | Owner/Operator code filter.  Enter one of the following values to restrict results. - Federal = Federal facilities regulated under the NPDES program. - POTW = Publicly owned treatment works. Treatment works that are owned by a State, Tribe, or municipality. - Non-POTW = Non-publicly owned treatment works. Often referred to as \"non-municipals\" or \"industrials\".
    String pIpfti = "pIpfti_example"; // String | 
    String pAgoo = "AND"; // String | Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
    String pIdt1 = "pIdt1_example"; // String | Beginning of date range of most recent facility inspection.
    String pIdt2 = "pIdt2_example"; // String | End of date range of most recent facility inspection.
    String pPityp = "pPityp_example"; // String | Inspection Type Code.  See ICIS Compliance Monitor Types lookup serivce for a list of available codes and descriptions.
    String pPfead1 = "pPfead1_example"; // String | Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    String pPfead2 = "pPfead2_example"; // String | Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    String pPfeat = "pPfeat_example"; // String | Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
    String pPccs = "pPccs_example"; // String | Current Compliance Status: |||||||||||||||||||||||||||  Significant Noncompliance (SNC)  ||||||||||||||||||||||||||| - SNC = E, S, X, T, D - E�= E(EffViol) - S�= S(CSchVio) - X = X(EffNMth) - T = T(CSchRpt) - D�= D(DMR NR)  ||||||||||||||||||||||||||| Noncompliance (NC) ||||||||||||||||||||||||||| - NC = N, V - N�= N(RptViol) - V�= V(NonRNCV)  ||||||||||||||||||||||||||| New Violations (PQV) ||||||||||||||||||||||||||| - PQV = New Violations (13th Quarter)  ||||||||||||||||||||||||||| No Violations (NV) ||||||||||||||||||||||||||| - NV = R, P, M, U, W , Blank, and No New Violations (no PQV) - R�= R(Resolvd) - P�= P(ResPend) - M�= C(Manual) - U = U(N/A) - W = W(N/A) - Blank = (null)  May contain multiple comma-separated values.
    String pPexcd = "0"; // String | 3-Year Effluent Exceedances Limiter.  Enter a value to restrict results to facilities with the given amount of exceedances in the past 3 years. - 0 = facilities with no exceedances - GE0 = facilities with one or more exceedances - GE10 = facilities with ten or more exceedances - GE50 = facilities with fifty or more exceedances - GE100 = facilities with one hundred or more exceedances
    String pPsncq = "GT1"; // String | Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z = Zero quarters in significant noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in significant noncompliance.
    String pPctrack = "false"; // String | Compliance Tracking Limiter. Provide a keyword to indicate the extent to which data is being entered and effluent exceedances are being identified. - Off - Partial - On
    String pDwd = "0"; // String | Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory.
    String pPt = "0"; // String | POTW Transfers. Pounds of toxic chemicals transferred to a Publicly Operated Treatment Works (POTW) as reported to the Toxics Release Inventory.
    String pPdwdist = "N"; // String | Distance (in miles) to downstream drinking water intake.
    String pPswdpc = "pPswdpc_example"; // String | Pollutant Category Code:  Values: WTR for Water, AIR for Air
    String pPswdmp = "1"; // String | Used to determine limit begin and end dates for surface water discharges. Number represents years from current date.
    String pPswpol = "pPswpol_example"; // String | For CWA, pollutant names for surface water discharges. for Drinking Water, SDWIS Violation contaminant codes for unaddressed violations that have occurred in the last 3 years. May contain multiple comma-separated values.
    String pPswcas = "pPswcas_example"; // String | CAS numbers for surface water discharges. May contain multiple comma-separated values.
    String pPswparam = "pPswparam_example"; // String | Parameter codes for surface water discharges. May contain multiple comma-separated values.
    String pPswvio = "Y"; // String | Used in conjuction with parameters p_pswpol and p_pswparam, indicates whether search should only include pollutants with violations.
    String pWbd = "pWbd_example"; // String | 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    String pRadwbd = "pRadwbd_example"; // String | 2-, 4-, 6-, 8-, 10-, or 12 character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Will search against WBD values otained by \"reach indexing\" NPDES permits against the medium resolution National Hydrography Dataset. 
    String pFrswbd = "pFrswbd_example"; // String | Works exactly the same as the p_wbd parameter.  2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    String pFntype = "ALL"; // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
    String pPidall = "Y"; // String | Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc).
    BigDecimal pMonthsLastDmr = new BigDecimal(78); // BigDecimal | The number of months since the last Discharge Monitoring Report has been submitted.
    String pLastDmrWithin = "W"; // String | W value returns facilities that have submitted DMRs within the number of months specified by p_months_last_dmr. An N value returns facilities that have not submitted a DMR within the specified number of months.
    String pIndsw = "Y"; // String | Industrial Stormwater Permit Flag.  Enter a Y or N to filter results by this type of permit.
    String pMsgpPtype = "NOI"; // String | Multi-Sector General Purpose Permit Type.  Enter a value to filter results by MSGP Permit Type. - NOI = Notice of Intent - NOE = No Exposure Certification
    String pMonType = "BENCHG2"; // String | For use with the Industrial Stormwater search only. Valid values are BENCHGS fro Benchmark (Alert Limit) G2 Ore, BENCH for Benchmark (Alert Limit), and ELG fro Effluent Limitation Guidelines(ELG)(Effluent Limit).  
    String pIagency = "pIagency_example"; // String | Issuing Agency Limiter.  Enter a single value to filter results by the issuing agency, e.g. \"State\" or \"EPA\".
    String pPermittingAgency = "pPermittingAgency_example"; // String | 
    String pIsws = "pIsws_example"; // String | Multi-Sector General Purpose Permit Subsector Individual Identifier.  Enter a value to filter results.
    String pIswss = "pIswss_example"; // String | Multi-Sector General Purpose Permit Subsector Group Code.  Enter a value to filter results.
    String pIswssID = "pIswssID_example"; // String | Multi-Sector General Purpose Permit Sector Code.  Enter a value to filter results.
    String pDs1 = "pDs1_example"; // String | Submitted Date Filter Start.  To filter by the date of submission, enter a start date here and an end date in the p_ds2 parameter.  Both dates are required for filtering.
    String pDs2 = "pDs2_example"; // String | Submitted Date Filter End.  To filter by the date of submission, enter an end date here and a start date in the p_ds1 parameter.  Both dates are required for filtering.
    String pDa1 = "pDa1_example"; // String | Active Date Filter Start.  To filter by the active date, enter a start date here and an end date in the p_da2 parameter.  Both dates are required for filtering.
    String pDa2 = "pDa2_example"; // String | Active Date Filter End.  To filter by the active date, enter an end date here and a start date in the p_da1 parameter.  Both dates are required for filtering.
    String pMS4 = "Y"; // String | Municipal Separate Storm Water Sewer (MS4) Permit Flag.  Enter a Y or N to filter results by this type of permit.
    String pOoFN = "pOoFN_example"; // String | Owner/Operator Name. Enter the owner/operator name of the facility.
    String pOoFNtype = "ALL"; // String | Owner/Operator Name Multiple Selection Evaluator.  
    String pOoSA = "pOoSA_example"; // String | Owner/Operator Address.  Enter the address of the owner/operator of the facility.
    String pOoSA1 = "pOoSA1_example"; // String | Owner/Operator Address Line 2.  Enter the line 2 address of the owner/operator of the facility.
    String pOoCt = "pOoCt_example"; // String | Owner/Operator City. Enter the city where the owner/operator of the facility is located.
    String pOoSt = "pOoSt_example"; // String | Owner/Operator State.  Enter the standardized postal state code where the owner/operator of the facility is located.
    String pOoZip = "pOoZip_example"; // String | Owner/Operator Zip Code.  Enter the postal zip code where the owner/operator of the facility is located.
    String pFacIco = "Y"; // String | FRS tribal land code flag.  Enter \"Y\" or \"N\" to include or exclude facilities based on FRS tribal land code.
    String pIcoo = "pIcoo_example"; // String | Indian country search and/or flag.  Enter \"Y\" to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
    String pFacIcos = "pFacIcos_example"; // String | FRS tribal land spatial flag.  Enter \"Y\" or \"N\" to include or exclude facilities based on FRS tribal land spatial flag.
    String pEjscreen = "pEjscreen_example"; // String | Enter \"Y\" to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
    BigDecimal pAlrexceed = new BigDecimal(78); // BigDecimal | Alert Limits Exceedences Limiter.  Enter a numeric value to restrict results to facilities having the given amount or more of alert limits exceedances.
    String pLimitAddr = "Y"; // String | Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
    BigDecimal pLat = new BigDecimal(78); // BigDecimal | Latitude location in decimal degrees.
    BigDecimal pLong = new BigDecimal(78); // BigDecimal | Longitude location in decimal degrees.
    BigDecimal pRadius = new BigDecimal(78); // BigDecimal | Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
    String pEjscreenOver80cnt = "1"; // String | The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
    String pBioFlag = "pBioFlag_example"; // String | A Y value will select all biosolid-related permits.
    String pBioFacType = "pBioFacType_example"; // String | The code indicating the reporting obligation reason:  - POT = A POTW with a design flow rate equal to or greater than one million gallons per day - CLI = A Class I Sludge Management Facility as defined in 40 CFR 503.9 - PPL = A POTW that serves 10,000 people or more - OTH = Otherwise required to report (e.g., permit condition, enforcement action) - NOA = None of the above
    String pBioTrtmntProcs = "pBioTrtmntProcs_example"; // String | The biosolids or sewage sludge treatment process or processes at the facility:  - AER = Aerobic Digestion - AIR = Air Drying (or Sludge Drying Beds) - ANA = Anaerobic Digestion - COD = Beta Ray Irradiation - COM = Lower Temperature Composting - DEW = Pasteurization - DIS = Gamma Ray Irradiation - HEA = Heat Drying (e.g., Flash Dryer, Spray Dryer, Rotary Dryer) - HET = Heat Treatment (Liquid Sewage Sludge Heated to 356 Deg. F/180 Deg. C or Higher for 30 min.) - HTC = Higher Temperature Composting - MET = Methane or Biogas Capture and Recovery - OTH = Other Treatment Process - PRE = Preliminary Operations (e.g., Sludge Grinding, Degritting, Blending) - SLU = Sludge Lagoon - STA = Lime Stabilization - THE = Temporary Sludge Storage (Sewage Sludge Stored on Land 2 Years or Less, Not in Sewage Sludge Unit) - THI = Thickening (Gravity and/or Flotation Thickening, Centrifugation, Belt Filter Press, Vacuum Filter) - THM = Thermophilic Aerobic Digestion - UND = Long-Term Sludge Storage (Sewage Sludge Stored on Land 2 Years or More, not in Sewage Sludge Unit)\"
    String pBioAnalyMethodCatgry = "pBioAnalyMethodCatgry_example"; // String | The unique code for the category of the analytic methods used by the facility to analyze regulated parameters (including enteric viruses, fecal coliforms, helminth ova, and Salmonella sp.) at the facility:  - PAT = Pathogens - MET = Metals - NIT = Nitrogen Compounds - OTH = Other Analytes
    String pBioTotalVolumeAmt = "pBioTotalVolumeAmt_example"; // String | Total annual amount (in dry metric tons) of biosolids or sewage sludge generated at the facility.  - EQ0 = 0 - IN0_1 = GT 0 but LT 1 - IN0_289  =  GT 0 but LT 290 MT/year - IN290_1499  =  GE 290 but LT 1500 MT/year - IN1500_14999  =  GE 1500 but LT 15,000 - GE15000  =  GE 15,000
    String pBioMgmtPrctceType = "pBioMgmtPrctceType_example"; // String | The unique code that identifies the type of biosolids or sewage sludge management practice (e.g., land application, surface disposal, incineration) used by the facility. The facility will separately report the management practice for each biosolids or sewage sludge form and pathogen class. This data element will also identify the management practices used by surface disposal site owners/operators (see 40 CFR 503.24):  - BIN = Incineration - BLN = Land Application - BOT = Other Management Practice - BSD = Surface Disposal
    String pBioMgmtPrctceStype = "pBioMgmtPrctceStype_example"; // String | This is the code indicating additional detail about the type of Management Practice used for a volume of Biosolids or Sewage Sludge:  - ADV = Advanced Alkaline Stabilized Biosolids Distribution & Marketing - AGR = Agricultural Land Application - COM = Distribution and Marketing - Compost - DEE = Deep-well Injection Disposal - DIS = Disposal in a Municipal Landfill (under 40 CFR 258) - DMO = Distribution and Marketing - Other - HEA = Heat Dried Biosolids Distribution & Marketing - OTL = Other Land Application Management Practice Detail - OTO = Other Management Practice Detail - RSA = Reclamation Site Application - SEN = Sent to Cement Kiln for Use as Alternative Energy - STO = Storage - UIC = Use in Construction - UPS = Used in Production of Syngas - USE = Use as Daily Cover for Municipal Landfill (under 40 CFR 258)
    String pBioMgmtPrctceHandler = "pBioMgmtPrctceHandler_example"; // String | This is the code indicating the type of Biosolids or Sewage Sludge handlers/preparers.  - OWN = Owner or Operator - OFF = Off-Site Third-Party Handler or Preparer
    String pBioMgmtContainer = "pBioMgmtContainer_example"; // String | The code that identifies the nature of each biosolids and sewage sludge material generated by the facility in terms of whether the material is a biosolid or sewage sludge and whether the material is ultimately conveyed off-site in bulk or in bags. The facility separately reports the form for each biosolids or sewage sludge management practice or practices used by the facility and pathogen class:  - BUL = Bulk - BAG = Bag or Container
    String pBioMgmtPathogen = "pBioMgmtPathogen_example"; // String | This code identifies the pathogen class [e.g., Class A, Class B, Not Applicable (Incineration)] for biosolids or sewage sludge generated by the facility. The facility will separately report the pathogen class for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form. It also is used to filter applicable Pathogen Reduction and Vector Attraction Reduction Options as well as Land Application Management Practice Deficiencies. Only reqired for some of the mgmt. practice types:  - AAA = Class A - AEQ = Class A EQ (sale/give away) - BBB = Class B - NAP = Not Applicable (Incineration)
    String pBioMgmtPathred = "pBioMgmtPathred_example"; // String | This is the description of the option used by the facility to control pathogen for a Biosolids Management Practice:  - A1 = Class A - Alternative 1: Time/Temperature - A2 = Class A - Alternative 2: pH/Temperature/Percent Solids - A3 = Class A - Alternative 3: Test Enteric Viruses and Helminth ova; Operating Parameters - A4 = Class A - Alternative 4: Test Enteric Viruses and Helminth ova; No New Solids - A51 = Class A - Alternative 5: PFRP 1: Composting - A52 = Class A - Alternative 5: PFRP 2: Heat Drying - A53 = Class A - Alternative 5: PFRP 3: Liquid heat treatment - A54 = Class A - Alternative 5: PFRP 4: Thermophilic Aerobic Digestion (ATAD) - A55 = Class A - Alternative 5 PFPR 5: Beta Ray Irradiation - A56 = Class A - Alternative 5 PFPR 6: Gamma Ray Irradiation - A57 = Class A - Alternative 5: PFRP 7: Pasteurization - A6 = Class A - Alternative 6: PFRP Equivalency - B1 = Class B - Alternative 1: Fecal Coliform Geometric Mean - B21 = Class B - Alternative 2 PSRP 1: Aerobic Digestion - B22 = Class B - Alternative 2 PSRP 2: Air Drying - B23 = Class B - Alternative 2 PSRP 3: Anaerobic Digestion - B24 = Class B - Alternative 2 PSRP 4: Composting - B25 = Class B - Alternative 2 PSRP 5: Lime Stabilization - B3 = Class B - Alternative 3: PSRP Equivalency - PH = pH Adjustment (Domestic Septage)
    String pBioMgmtVector = "pBioMgmtVector_example"; // String | The unique code that identifies the option used by the facility for vector attraction reduction. See a listing of these vector attraction reduction options at 40 CFR 503.33(b)(1) through (11). The facility will separately report the vector attraction reduction options for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form as well as by each biosolids or sewage sludge pathogen class:  - VR1 = Option 1 - Volatile Solids Reduction - VR2 = Option 2 - Bench-Scale Volatile Solids Reduction (Anaerobic Bench Test) - VR3 = Option 3 - Bench-Scale Volatile Solids Reduction (Aerobic Bench Test w/ Percent Solids - 2% or Less) - VR4 = Option 4 - Specific Oxygen Uptake Rate - VR5 = Option 5 - Aerobic Processing (Thermophilic Aerobic Digestion/Composting) - VR6 = Option 6 - Alkaline Treatment - VR7 = Option 7 - Drying (Equal to or Greater than 75 Percent) - VR8 = Option 8 - Drying (Equal to or Greater than 90 Percent) - VR9 = Option 9 - Sewage Sludge Injection - V10 = Option 10 - Sewage Sludge Timely Incorporation into Land - V11 = Option 11 - Sewage Sludge Covered at the End of Each Operating Day
    String pBioMgmtDefCategory = "pBioMgmtDefCategory_example"; // String | This is the code indicating the type of NPDES special regulatory program deficiency:  - INC = Biosolids Incineration - LNA = Biosolids Land Application - LNB = Biosolids Land Application - Pathogen Class B - OTB = Biosolids Other Management Practice - SFD = Biosolids Surface Disposal
    BigDecimal pBioMgmtDeficiencies = new BigDecimal(78); // BigDecimal | The number of times noncompliance was reported by the facility in the last 3 years. The results returned will include facilities whose number of reported noncompliance events is greater than or equal to the number entered.
    String pBioVioCode = "pBioVioCode_example"; // String | The Biosolids Single Event Violation Code.  Enter one or mode codes.
    String pBioCurrentVio = "Y"; // String | Indicator of whether the facility is currently in violation for biosolids under the Clean Water Act, in the 12th or 13th quarter:  - Y = Yes - N = No
    BigDecimal pBioQtrsInVio = new BigDecimal(78); // BigDecimal | The number of quarters, in the last three years, where the facility was in violation for a biosolids violation type.  The results returned will include facilities whose number of quarters with violations is greater than or equal to the number entered.
    String pBioRptYear = "pBioRptYear_example"; // String | The last year that the permittee submitted an annual Biosolids report.  Valid values are NONE and any year greater or equal to 2016.
    String pBioVioLastYear = "Y"; // String | Identifies if a biosolids violation has occured in the last year.  Valid values are Y and N.
    String pMsgpRptYear = "pMsgpRptYear_example"; // String | The last year that a MSGP report was submitted for the permit.  Valid values are \"NONE\" and any year Greater or Eqal to 2015.
    String pVioLastYear = "Y"; // String | Identifies if a permit violation has occured in the last year.  Valid values are Y and N.
    BigDecimal responseset = new BigDecimal(78); // BigDecimal | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    BigDecimal pE90Count = new BigDecimal(78); // BigDecimal | Number of E90 Exceedances.  Identifies water permits with a number of E90 (Effluient Exceedances) >= the value provided for the last number of years provided by the p_e90_years value.
    BigDecimal pE90Years = new BigDecimal(78); // BigDecimal | Number of years for the p_e90_count search.  Identified the past number of years to be used for the p_e90_count search.
    String pPsc = "pPsc_example"; // String | Point Source Category.
    try {
      CwaRestServicesGetFacilityInfoGet200Response result = apiInstance.cwaRestServicesGetFacilityInfoGet(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pFrs, pReg, pSic, pNcs, pPen, xmin, ymin, xmax, ymax, pUsmex, pSic2, pSic4, pFa, pFf, pAct, pMaj, pMact, pFea, pFeay, pFeaa, pIea, pIeay, pIeaa, pQiv, pIv, pImpw, pImpPol, pImpCauGrp, pTrep, pPm, pPd, pIco, pHuc, pPid, pMed, pYsl, pYsly, pYsla, pQs, pSfs, pTribeid, pTribename, pTribedist, pPstat, pPtype, pPcomp, pPlimits, pPcss, pPexp, pOwop, pIpfti, pAgoo, pIdt1, pIdt2, pPityp, pPfead1, pPfead2, pPfeat, pPccs, pPexcd, pPsncq, pPctrack, pDwd, pPt, pPdwdist, pPswdpc, pPswdmp, pPswpol, pPswcas, pPswparam, pPswvio, pWbd, pRadwbd, pFrswbd, pFntype, pPidall, pMonthsLastDmr, pLastDmrWithin, pIndsw, pMsgpPtype, pMonType, pIagency, pPermittingAgency, pIsws, pIswss, pIswssID, pDs1, pDs2, pDa1, pDa2, pMS4, pOoFN, pOoFNtype, pOoSA, pOoSA1, pOoCt, pOoSt, pOoZip, pFacIco, pIcoo, pFacIcos, pEjscreen, pAlrexceed, pLimitAddr, pLat, pLong, pRadius, pEjscreenOver80cnt, pBioFlag, pBioFacType, pBioTrtmntProcs, pBioAnalyMethodCatgry, pBioTotalVolumeAmt, pBioMgmtPrctceType, pBioMgmtPrctceStype, pBioMgmtPrctceHandler, pBioMgmtContainer, pBioMgmtPathogen, pBioMgmtPathred, pBioMgmtVector, pBioMgmtDefCategory, pBioMgmtDeficiencies, pBioVioCode, pBioCurrentVio, pBioQtrsInVio, pBioRptYear, pBioVioLastYear, pMsgpRptYear, pVioLastYear, responseset, paramCallback, qcolumns, pPrettyPrint, pE90Count, pE90Years, pPsc);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInformationApi#cwaRestServicesGetFacilityInfoGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. - CSV &#x3D; Facility results formatted as comma delimited file download. - GEOJSON &#x3D; Facility results formatted as GeoJSON feature collection. - GEOJSONP &#x3D; Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download. | [optional] |
| **pFn** | **String**| Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers. | [optional] |
| **pSa** | **String**| Facility street address. Enter a complete or partial street address. | [optional] |
| **pSa1** | **String**| Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa. | [optional] |
| **pCt** | **String**| Facility City Filter. Enter a single case-insensitive city name to filter results. | [optional] |
| **pCo** | **String**| Facility County Filter. Provide a single county name in combination with a state value provided via p_st. | [optional] |
| **pFips** | **String**| FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059. | [optional] |
| **pSt** | **String**| Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pZip** | **String**| 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values. | [optional] |
| **pFrs** | **String**| Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results. | [optional] |
| **pReg** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] [enum: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10] |
| **pSic** | **String**| Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4. | [optional] |
| **pNcs** | **String**| North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values. | [optional] |
| **pPen** | **String**| Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER &#x3D; No Penalties - ANY &#x3D; Any Penalty - LEXX &#x3D; Less than or equal to XX months.  Provide a number in place of XX, e.g. \&quot;LE5\&quot; for a facility with a penalty within previous 5 months. - GTXX &#x3D; Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago. | [optional] |
| **xmin** | **BigDecimal**| Minimum longitude value in decimal degrees. | [optional] |
| **ymin** | **BigDecimal**| Minimum latitude value in decimal degrees. | [optional] |
| **xmax** | **BigDecimal**| Maximum longitude value in decimal degrees. | [optional] |
| **ymax** | **BigDecimal**| Maximum latitude value in decimal degrees. | [optional] |
| **pUsmex** | **String**| US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border. | [optional] [enum: Y, N] |
| **pSic2** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \&quot;22\&quot; to match all SIC codes beginning with 22.  Use the \&quot;%\&quot; character within strings to match any SIC values with the pattern.  For example, \&quot;2%21\&quot; matches 2021, 2121, 2221, etc. | [optional] |
| **pSic4** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker. | [optional] |
| **pFa** | **String**| Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values. | [optional] |
| **pFf** | **String**| Federal Facility Indicator Flag. Enter Y to restrict searches to federal facilities. | [optional] [enum: Y] |
| **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.  A Y will select ICIS NPDES permits with a status of effective, continued, or expired. | [optional] |
| **pMaj** | **String**| Major Facility Flag.  Enter Y to restrict results to Major facilities only. | [optional] [enum: Y, N] |
| **pMact** | **String**| CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility. | [optional] |
| **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pFeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] [enum: A, E, S] |
| **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pIeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S] |
| **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] [enum: 0, GT1, GT2, GT4, GT8, 12] |
| **pIv** | **String**| Facility has a violation status of &#39;In Viol&#39; during any of the selected quarters.   Range: Fiscal Year 2020 Quarter 2 to Fiscal Year 2017 Quarter 2  Multiple values are comma delimited.   ||||||  Fiscal Years |||||| - FY2020 or FY20 or 2020 or 20 - FY2019 or FY19 or 2019 or 19 - FY2018 or FY18 or 2018 or 18 - FY2017 or FY17 or 2017 or 17  ||||| Fiscal Quarters ||||| - FY2020Q2 or FY20Q2 or 20202 or 202 or 13 - FY2020Q1 or FY20Q1 or 20201 or 201 or 12 - FY2019Q4 or FY19Q4 or 20194 or 194 or 11 - FY2019Q3 or FY19Q3 or 20193 or 193 or 10 - FY2019Q2 or FY19Q2 or 20192 or 192 or 9 - FY2019Q1 or FY19Q1 or 20191 or 191 or 8 - FY2018Q4 or FY18Q4 or 20184 or 184 or 7 - FY2018Q3 or FY18Q3 or 20183 or 183 or 6 - FY2018Q2 or FY18Q2 or 20182 or 182 or 5 - FY2018Q1 or FY18Q1 or 20181 or 181 or 4 - FY2017Q4 or FY17Q4 or 20174 or 174 or 3 - FY2017Q3 or FY17Q3 or 20173 or 173 or 2 - FY2017Q2 or FY17Q2 or 20172 or 172 or 1 | [optional] |
| **pImpw** | **String**| Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database. | [optional] [enum: Y, N] |
| **pImpPol** | **String**| Facility is discharging pollutants that are potentially contributing to the impairment of local waterbodies according to the ATTAINS database. | [optional] [enum: Y, N] |
| **pImpCauGrp** | **String**| Facility is discharging a pollutant group causing a waterbody to be impaired.  Enter 1 through 34 (the internal number of the pollutant group); or enter a partial name such as Dioxin,Temp,tUrBidity. | [optional] [enum: ALGAL GROWTH, AMMONIA, BIOTOXINS, CAUSE UNKNOWN, CAUSE UNKNOWN - FISH KILLS, CAUSE UNKNOWN - IMPAIRED BIOTA, CHLORINE, DIOXINS, FISH CONSUMPTION ADVISORY, FLOW ALTERATION(S), HABITAT ALTERATIONS, MERCURY, METALS (OTHER THAN MERCURY), NOXIOUS AQUATIC PLANTS, NUISANCE EXOTIC SPECIES, NUISANCE NATIVE SPECIES, NUTRIENTS, OIL AND GREASE, ORGANIC ENRICHMENT/OXYGEN DEPLETION, OTHER CAUSE, PATHOGENS, PESTICIDES, PH/ACIDITY/CAUSTIC CONDITIONS, POLYCHLORINATED BIPHENYLS (PCBS), RADIATION, SALINITY/TOTAL DISSOLVED SOLIDS/CHLORIDES/SULFATES, SEDIMENT, TASTE, COLOR AND ODOR, TEMPERATURE, TOTAL TOXICS, TOXIC INORGANICS, TOXIC ORGANICS, TRASH, TURBIDITY] |
| **pTrep** | **String**| Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year. | [optional] [enum: CURR, NOTCURR] |
| **pPm** | **String**| Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75% | [optional] [enum: NONE, GT5, GT10, GT25, GT50, GT75] |
| **pPd** | **String**| Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile | [optional] [enum: NONE, GT100, GT500, GT1000, GT5000, GT10000, GT20000] |
| **pIco** | **String**| Indian Country Flag.  Enter a \&quot;Y\&quot; or \&quot;N\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] [enum: Y, N] |
| **pHuc** | **String**| 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values. | [optional] |
| **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] |
| **pMed** | **String**| Filter Results by Media. - A &#x3D; Air - M &#x3D; RMP (Risk Management Plan) - R &#x3D; RCRA (Hazardous Waste) - S &#x3D; SDWA (Public Drinking Water Systems) - ALL &#x3D; Air and RCRA and Water | [optional] [enum: A, M, R, S, ALL] |
| **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N, NV] |
| **pYsly** | **BigDecimal**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S, A] |
| **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] |
| **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] |
| **pTribeid** | **BigDecimal**| Numeric code for tribe (or list of tribes). | [optional] |
| **pTribename** | **String**| Tribe Name Filter.  Enter a single tribe name to filter results. | [optional] |
| **pTribedist** | **BigDecimal**| Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated. | [optional] |
| **pPstat** | **String**| Permit Status Filter.  Enter one or more of the following codes.  Provide multiple values as a comma-delimited list. - EFF &#x3D; Effective - EXP &#x3D; Expired - PND &#x3D; Pending - TRM &#x3D; Terminated - RET &#x3D; Retired - NON &#x3D; Not Needed - ADC &#x3D; Admin Continued | [optional] |
| **pPtype** | **String**| Permit Type Filter. Enter one or more code values to filter results.  Provide multiple values as a comma-delimited list. - NPD &#x3D; NPDES Individual Permit - NGP &#x3D; NPDES Master General Permit - GPC &#x3D; General Permit Covered Facility - SNN &#x3D; State Issued Master General Permit (Non-NPDES) - IIU &#x3D; Individual IU Permit (Non-NPDES) - SIN &#x3D; Individual State Issued Permit (Non-NPDES) - APR &#x3D; Associated Permit Record - UFT &#x3D; Unpermitted Facility | [optional] |
| **pPcomp** | **String**| Permit Component Code Filter.  Enter one or more codes to filter results.  Provide multiple values as a comma-delimited list. - PRE &#x3D; Pretreatment - CAF &#x3D; CAFO - CSO &#x3D; CSO - POT &#x3D; POTW - BIO &#x3D; Biosolids - SWS &#x3D; Storm Water Small MS4s - SWM &#x3D; Storm Water Medium/Large MS4s - SWI &#x3D; Storm Water Industrial - SWC &#x3D; Storm Water Construction | [optional] |
| **pPlimits** | **String**| Permit Limits Present Flag.  Enter Y to limit results to facilities have present permit limits. | [optional] [enum: Y, N] |
| **pPcss** | **String**| Combined Sewer Systems Outflows Limiter.  Enter one of the following to limit results to facilities having the given count of CSS outflows. - ALL &#x3D; returns all facilities, regardless of the number of outflows. - GE1 &#x3D; returns facilities with one or more outflows. - GE10 &#x3D; returns facilities with ten or more outflows. - GE50 &#x3D; returns facilities with fifty or more outflows. | [optional] [enum: ALL, GE1, GE10, GE50] |
| **pPexp** | **String**| Permit Expired or Administratively Continued Limiter.  Enter one of the following values to filter results. - EXP &#x3D; limit results to facilities with permits expired or administratively continued. - EXPLE1YR &#x3D; limit resuls to facilities with permits expired administratively continued within the past year. - EXPGT1YR &#x3D; limit resuls to facilities with permits expired administratively continued more than a year ago. | [optional] [enum: EXP, EXPLE1YR, EXPGT1YR] |
| **pOwop** | **String**| Owner/Operator code filter.  Enter one of the following values to restrict results. - Federal &#x3D; Federal facilities regulated under the NPDES program. - POTW &#x3D; Publicly owned treatment works. Treatment works that are owned by a State, Tribe, or municipality. - Non-POTW &#x3D; Non-publicly owned treatment works. Often referred to as \&quot;non-municipals\&quot; or \&quot;industrials\&quot;. | [optional] [enum: FEDERAL, POTW, NON-POTW] |
| **pIpfti** | **String**|  | [optional] |
| **pAgoo** | **String**| Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters. | [optional] [enum: AND, OR] |
| **pIdt1** | **String**| Beginning of date range of most recent facility inspection. | [optional] |
| **pIdt2** | **String**| End of date range of most recent facility inspection. | [optional] |
| **pPityp** | **String**| Inspection Type Code.  See ICIS Compliance Monitor Types lookup serivce for a list of available codes and descriptions. | [optional] |
| **pPfead1** | **String**| Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] |
| **pPfead2** | **String**| Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] |
| **pPfeat** | **String**| Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list. | [optional] |
| **pPccs** | **String**| Current Compliance Status: |||||||||||||||||||||||||||  Significant Noncompliance (SNC)  ||||||||||||||||||||||||||| - SNC &#x3D; E, S, X, T, D - E�&#x3D; E(EffViol) - S�&#x3D; S(CSchVio) - X &#x3D; X(EffNMth) - T &#x3D; T(CSchRpt) - D�&#x3D; D(DMR NR)  ||||||||||||||||||||||||||| Noncompliance (NC) ||||||||||||||||||||||||||| - NC &#x3D; N, V - N�&#x3D; N(RptViol) - V�&#x3D; V(NonRNCV)  ||||||||||||||||||||||||||| New Violations (PQV) ||||||||||||||||||||||||||| - PQV &#x3D; New Violations (13th Quarter)  ||||||||||||||||||||||||||| No Violations (NV) ||||||||||||||||||||||||||| - NV &#x3D; R, P, M, U, W , Blank, and No New Violations (no PQV) - R�&#x3D; R(Resolvd) - P�&#x3D; P(ResPend) - M�&#x3D; C(Manual) - U &#x3D; U(N/A) - W &#x3D; W(N/A) - Blank &#x3D; (null)  May contain multiple comma-separated values. | [optional] |
| **pPexcd** | **String**| 3-Year Effluent Exceedances Limiter.  Enter a value to restrict results to facilities with the given amount of exceedances in the past 3 years. - 0 &#x3D; facilities with no exceedances - GE0 &#x3D; facilities with one or more exceedances - GE10 &#x3D; facilities with ten or more exceedances - GE50 &#x3D; facilities with fifty or more exceedances - GE100 &#x3D; facilities with one hundred or more exceedances | [optional] [enum: 0, GE0, GE10, GE50, GE100] |
| **pPsncq** | **String**| Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z &#x3D; Zero quarters in significant noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in significant noncompliance. | [optional] [enum: GT1, GE1, GT2, GE2, GT4, GE4, GT8, GE8, GT12, GE12] |
| **pPctrack** | **String**| Compliance Tracking Limiter. Provide a keyword to indicate the extent to which data is being entered and effluent exceedances are being identified. - Off - Partial - On | [optional] [enum: false, Partial, true] |
| **pDwd** | **String**| Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory. | [optional] [enum: 0, GT0, GT1000, GT5000, GT10000, GT20000, GT50000] |
| **pPt** | **String**| POTW Transfers. Pounds of toxic chemicals transferred to a Publicly Operated Treatment Works (POTW) as reported to the Toxics Release Inventory. | [optional] [enum: 0, GT0, GT1000, GT5000, GT10000, GT20000, GT50000] |
| **pPdwdist** | **String**| Distance (in miles) to downstream drinking water intake. | [optional] [enum: N, LT1, LT2, LT5, LT10, LT15] |
| **pPswdpc** | **String**| Pollutant Category Code:  Values: WTR for Water, AIR for Air | [optional] |
| **pPswdmp** | **String**| Used to determine limit begin and end dates for surface water discharges. Number represents years from current date. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pPswpol** | **String**| For CWA, pollutant names for surface water discharges. for Drinking Water, SDWIS Violation contaminant codes for unaddressed violations that have occurred in the last 3 years. May contain multiple comma-separated values. | [optional] |
| **pPswcas** | **String**| CAS numbers for surface water discharges. May contain multiple comma-separated values. | [optional] |
| **pPswparam** | **String**| Parameter codes for surface water discharges. May contain multiple comma-separated values. | [optional] |
| **pPswvio** | **String**| Used in conjuction with parameters p_pswpol and p_pswparam, indicates whether search should only include pollutants with violations. | [optional] [enum: Y, N] |
| **pWbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] |
| **pRadwbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12 character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Will search against WBD values otained by \&quot;reach indexing\&quot; NPDES permits against the medium resolution National Hydrography Dataset.  | [optional] |
| **pFrswbd** | **String**| Works exactly the same as the p_wbd parameter.  2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] |
| **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] [enum: ALL, CONTAINS, EXACT, BEGINS] |
| **pPidall** | **String**| Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc). | [optional] [enum: Y, N] |
| **pMonthsLastDmr** | **BigDecimal**| The number of months since the last Discharge Monitoring Report has been submitted. | [optional] |
| **pLastDmrWithin** | **String**| W value returns facilities that have submitted DMRs within the number of months specified by p_months_last_dmr. An N value returns facilities that have not submitted a DMR within the specified number of months. | [optional] [enum: W, N] |
| **pIndsw** | **String**| Industrial Stormwater Permit Flag.  Enter a Y or N to filter results by this type of permit. | [optional] [enum: Y, N] |
| **pMsgpPtype** | **String**| Multi-Sector General Purpose Permit Type.  Enter a value to filter results by MSGP Permit Type. - NOI &#x3D; Notice of Intent - NOE &#x3D; No Exposure Certification | [optional] [enum: NOI, NOE] |
| **pMonType** | **String**| For use with the Industrial Stormwater search only. Valid values are BENCHGS fro Benchmark (Alert Limit) G2 Ore, BENCH for Benchmark (Alert Limit), and ELG fro Effluent Limitation Guidelines(ELG)(Effluent Limit).   | [optional] [enum: BENCHG2, BENCH, ELG] |
| **pIagency** | **String**| Issuing Agency Limiter.  Enter a single value to filter results by the issuing agency, e.g. \&quot;State\&quot; or \&quot;EPA\&quot;. | [optional] |
| **pPermittingAgency** | **String**|  | [optional] |
| **pIsws** | **String**| Multi-Sector General Purpose Permit Subsector Individual Identifier.  Enter a value to filter results. | [optional] |
| **pIswss** | **String**| Multi-Sector General Purpose Permit Subsector Group Code.  Enter a value to filter results. | [optional] |
| **pIswssID** | **String**| Multi-Sector General Purpose Permit Sector Code.  Enter a value to filter results. | [optional] |
| **pDs1** | **String**| Submitted Date Filter Start.  To filter by the date of submission, enter a start date here and an end date in the p_ds2 parameter.  Both dates are required for filtering. | [optional] |
| **pDs2** | **String**| Submitted Date Filter End.  To filter by the date of submission, enter an end date here and a start date in the p_ds1 parameter.  Both dates are required for filtering. | [optional] |
| **pDa1** | **String**| Active Date Filter Start.  To filter by the active date, enter a start date here and an end date in the p_da2 parameter.  Both dates are required for filtering. | [optional] |
| **pDa2** | **String**| Active Date Filter End.  To filter by the active date, enter an end date here and a start date in the p_da1 parameter.  Both dates are required for filtering. | [optional] |
| **pMS4** | **String**| Municipal Separate Storm Water Sewer (MS4) Permit Flag.  Enter a Y or N to filter results by this type of permit. | [optional] [enum: Y, N] |
| **pOoFN** | **String**| Owner/Operator Name. Enter the owner/operator name of the facility. | [optional] |
| **pOoFNtype** | **String**| Owner/Operator Name Multiple Selection Evaluator.   | [optional] [enum: ALL, EXACT, BEGINS, CONTAINS] |
| **pOoSA** | **String**| Owner/Operator Address.  Enter the address of the owner/operator of the facility. | [optional] |
| **pOoSA1** | **String**| Owner/Operator Address Line 2.  Enter the line 2 address of the owner/operator of the facility. | [optional] |
| **pOoCt** | **String**| Owner/Operator City. Enter the city where the owner/operator of the facility is located. | [optional] |
| **pOoSt** | **String**| Owner/Operator State.  Enter the standardized postal state code where the owner/operator of the facility is located. | [optional] |
| **pOoZip** | **String**| Owner/Operator Zip Code.  Enter the postal zip code where the owner/operator of the facility is located. | [optional] |
| **pFacIco** | **String**| FRS tribal land code flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land code. | [optional] [enum: Y, N] |
| **pIcoo** | **String**| Indian country search and/or flag.  Enter \&quot;Y\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned. | [optional] |
| **pFacIcos** | **String**| FRS tribal land spatial flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land spatial flag. | [optional] |
| **pEjscreen** | **String**| Enter \&quot;Y\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile. | [optional] |
| **pAlrexceed** | **BigDecimal**| Alert Limits Exceedences Limiter.  Enter a numeric value to restrict results to facilities having the given amount or more of alert limits exceedances. | [optional] |
| **pLimitAddr** | **String**| Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.   | [optional] [enum: Y, N] |
| **pLat** | **BigDecimal**| Latitude location in decimal degrees. | [optional] |
| **pLong** | **BigDecimal**| Longitude location in decimal degrees. | [optional] |
| **pRadius** | **BigDecimal**| Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities. | [optional] |
| **pEjscreenOver80cnt** | **String**| The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11. | [optional] [enum: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] |
| **pBioFlag** | **String**| A Y value will select all biosolid-related permits. | [optional] |
| **pBioFacType** | **String**| The code indicating the reporting obligation reason:  - POT &#x3D; A POTW with a design flow rate equal to or greater than one million gallons per day - CLI &#x3D; A Class I Sludge Management Facility as defined in 40 CFR 503.9 - PPL &#x3D; A POTW that serves 10,000 people or more - OTH &#x3D; Otherwise required to report (e.g., permit condition, enforcement action) - NOA &#x3D; None of the above | [optional] |
| **pBioTrtmntProcs** | **String**| The biosolids or sewage sludge treatment process or processes at the facility:  - AER &#x3D; Aerobic Digestion - AIR &#x3D; Air Drying (or Sludge Drying Beds) - ANA &#x3D; Anaerobic Digestion - COD &#x3D; Beta Ray Irradiation - COM &#x3D; Lower Temperature Composting - DEW &#x3D; Pasteurization - DIS &#x3D; Gamma Ray Irradiation - HEA &#x3D; Heat Drying (e.g., Flash Dryer, Spray Dryer, Rotary Dryer) - HET &#x3D; Heat Treatment (Liquid Sewage Sludge Heated to 356 Deg. F/180 Deg. C or Higher for 30 min.) - HTC &#x3D; Higher Temperature Composting - MET &#x3D; Methane or Biogas Capture and Recovery - OTH &#x3D; Other Treatment Process - PRE &#x3D; Preliminary Operations (e.g., Sludge Grinding, Degritting, Blending) - SLU &#x3D; Sludge Lagoon - STA &#x3D; Lime Stabilization - THE &#x3D; Temporary Sludge Storage (Sewage Sludge Stored on Land 2 Years or Less, Not in Sewage Sludge Unit) - THI &#x3D; Thickening (Gravity and/or Flotation Thickening, Centrifugation, Belt Filter Press, Vacuum Filter) - THM &#x3D; Thermophilic Aerobic Digestion - UND &#x3D; Long-Term Sludge Storage (Sewage Sludge Stored on Land 2 Years or More, not in Sewage Sludge Unit)\&quot; | [optional] |
| **pBioAnalyMethodCatgry** | **String**| The unique code for the category of the analytic methods used by the facility to analyze regulated parameters (including enteric viruses, fecal coliforms, helminth ova, and Salmonella sp.) at the facility:  - PAT &#x3D; Pathogens - MET &#x3D; Metals - NIT &#x3D; Nitrogen Compounds - OTH &#x3D; Other Analytes | [optional] |
| **pBioTotalVolumeAmt** | **String**| Total annual amount (in dry metric tons) of biosolids or sewage sludge generated at the facility.  - EQ0 &#x3D; 0 - IN0_1 &#x3D; GT 0 but LT 1 - IN0_289  &#x3D;  GT 0 but LT 290 MT/year - IN290_1499  &#x3D;  GE 290 but LT 1500 MT/year - IN1500_14999  &#x3D;  GE 1500 but LT 15,000 - GE15000  &#x3D;  GE 15,000 | [optional] |
| **pBioMgmtPrctceType** | **String**| The unique code that identifies the type of biosolids or sewage sludge management practice (e.g., land application, surface disposal, incineration) used by the facility. The facility will separately report the management practice for each biosolids or sewage sludge form and pathogen class. This data element will also identify the management practices used by surface disposal site owners/operators (see 40 CFR 503.24):  - BIN &#x3D; Incineration - BLN &#x3D; Land Application - BOT &#x3D; Other Management Practice - BSD &#x3D; Surface Disposal | [optional] |
| **pBioMgmtPrctceStype** | **String**| This is the code indicating additional detail about the type of Management Practice used for a volume of Biosolids or Sewage Sludge:  - ADV &#x3D; Advanced Alkaline Stabilized Biosolids Distribution &amp; Marketing - AGR &#x3D; Agricultural Land Application - COM &#x3D; Distribution and Marketing - Compost - DEE &#x3D; Deep-well Injection Disposal - DIS &#x3D; Disposal in a Municipal Landfill (under 40 CFR 258) - DMO &#x3D; Distribution and Marketing - Other - HEA &#x3D; Heat Dried Biosolids Distribution &amp; Marketing - OTL &#x3D; Other Land Application Management Practice Detail - OTO &#x3D; Other Management Practice Detail - RSA &#x3D; Reclamation Site Application - SEN &#x3D; Sent to Cement Kiln for Use as Alternative Energy - STO &#x3D; Storage - UIC &#x3D; Use in Construction - UPS &#x3D; Used in Production of Syngas - USE &#x3D; Use as Daily Cover for Municipal Landfill (under 40 CFR 258) | [optional] |
| **pBioMgmtPrctceHandler** | **String**| This is the code indicating the type of Biosolids or Sewage Sludge handlers/preparers.  - OWN &#x3D; Owner or Operator - OFF &#x3D; Off-Site Third-Party Handler or Preparer | [optional] |
| **pBioMgmtContainer** | **String**| The code that identifies the nature of each biosolids and sewage sludge material generated by the facility in terms of whether the material is a biosolid or sewage sludge and whether the material is ultimately conveyed off-site in bulk or in bags. The facility separately reports the form for each biosolids or sewage sludge management practice or practices used by the facility and pathogen class:  - BUL &#x3D; Bulk - BAG &#x3D; Bag or Container | [optional] |
| **pBioMgmtPathogen** | **String**| This code identifies the pathogen class [e.g., Class A, Class B, Not Applicable (Incineration)] for biosolids or sewage sludge generated by the facility. The facility will separately report the pathogen class for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form. It also is used to filter applicable Pathogen Reduction and Vector Attraction Reduction Options as well as Land Application Management Practice Deficiencies. Only reqired for some of the mgmt. practice types:  - AAA &#x3D; Class A - AEQ &#x3D; Class A EQ (sale/give away) - BBB &#x3D; Class B - NAP &#x3D; Not Applicable (Incineration) | [optional] |
| **pBioMgmtPathred** | **String**| This is the description of the option used by the facility to control pathogen for a Biosolids Management Practice:  - A1 &#x3D; Class A - Alternative 1: Time/Temperature - A2 &#x3D; Class A - Alternative 2: pH/Temperature/Percent Solids - A3 &#x3D; Class A - Alternative 3: Test Enteric Viruses and Helminth ova; Operating Parameters - A4 &#x3D; Class A - Alternative 4: Test Enteric Viruses and Helminth ova; No New Solids - A51 &#x3D; Class A - Alternative 5: PFRP 1: Composting - A52 &#x3D; Class A - Alternative 5: PFRP 2: Heat Drying - A53 &#x3D; Class A - Alternative 5: PFRP 3: Liquid heat treatment - A54 &#x3D; Class A - Alternative 5: PFRP 4: Thermophilic Aerobic Digestion (ATAD) - A55 &#x3D; Class A - Alternative 5 PFPR 5: Beta Ray Irradiation - A56 &#x3D; Class A - Alternative 5 PFPR 6: Gamma Ray Irradiation - A57 &#x3D; Class A - Alternative 5: PFRP 7: Pasteurization - A6 &#x3D; Class A - Alternative 6: PFRP Equivalency - B1 &#x3D; Class B - Alternative 1: Fecal Coliform Geometric Mean - B21 &#x3D; Class B - Alternative 2 PSRP 1: Aerobic Digestion - B22 &#x3D; Class B - Alternative 2 PSRP 2: Air Drying - B23 &#x3D; Class B - Alternative 2 PSRP 3: Anaerobic Digestion - B24 &#x3D; Class B - Alternative 2 PSRP 4: Composting - B25 &#x3D; Class B - Alternative 2 PSRP 5: Lime Stabilization - B3 &#x3D; Class B - Alternative 3: PSRP Equivalency - PH &#x3D; pH Adjustment (Domestic Septage) | [optional] |
| **pBioMgmtVector** | **String**| The unique code that identifies the option used by the facility for vector attraction reduction. See a listing of these vector attraction reduction options at 40 CFR 503.33(b)(1) through (11). The facility will separately report the vector attraction reduction options for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form as well as by each biosolids or sewage sludge pathogen class:  - VR1 &#x3D; Option 1 - Volatile Solids Reduction - VR2 &#x3D; Option 2 - Bench-Scale Volatile Solids Reduction (Anaerobic Bench Test) - VR3 &#x3D; Option 3 - Bench-Scale Volatile Solids Reduction (Aerobic Bench Test w/ Percent Solids - 2% or Less) - VR4 &#x3D; Option 4 - Specific Oxygen Uptake Rate - VR5 &#x3D; Option 5 - Aerobic Processing (Thermophilic Aerobic Digestion/Composting) - VR6 &#x3D; Option 6 - Alkaline Treatment - VR7 &#x3D; Option 7 - Drying (Equal to or Greater than 75 Percent) - VR8 &#x3D; Option 8 - Drying (Equal to or Greater than 90 Percent) - VR9 &#x3D; Option 9 - Sewage Sludge Injection - V10 &#x3D; Option 10 - Sewage Sludge Timely Incorporation into Land - V11 &#x3D; Option 11 - Sewage Sludge Covered at the End of Each Operating Day | [optional] |
| **pBioMgmtDefCategory** | **String**| This is the code indicating the type of NPDES special regulatory program deficiency:  - INC &#x3D; Biosolids Incineration - LNA &#x3D; Biosolids Land Application - LNB &#x3D; Biosolids Land Application - Pathogen Class B - OTB &#x3D; Biosolids Other Management Practice - SFD &#x3D; Biosolids Surface Disposal | [optional] |
| **pBioMgmtDeficiencies** | **BigDecimal**| The number of times noncompliance was reported by the facility in the last 3 years. The results returned will include facilities whose number of reported noncompliance events is greater than or equal to the number entered. | [optional] |
| **pBioVioCode** | **String**| The Biosolids Single Event Violation Code.  Enter one or mode codes. | [optional] |
| **pBioCurrentVio** | **String**| Indicator of whether the facility is currently in violation for biosolids under the Clean Water Act, in the 12th or 13th quarter:  - Y &#x3D; Yes - N &#x3D; No | [optional] [enum: Y, N] |
| **pBioQtrsInVio** | **BigDecimal**| The number of quarters, in the last three years, where the facility was in violation for a biosolids violation type.  The results returned will include facilities whose number of quarters with violations is greater than or equal to the number entered. | [optional] |
| **pBioRptYear** | **String**| The last year that the permittee submitted an annual Biosolids report.  Valid values are NONE and any year greater or equal to 2016. | [optional] |
| **pBioVioLastYear** | **String**| Identifies if a biosolids violation has occured in the last year.  Valid values are Y and N. | [optional] [enum: Y, N] |
| **pMsgpRptYear** | **String**| The last year that a MSGP report was submitted for the permit.  Valid values are \&quot;NONE\&quot; and any year Greater or Eqal to 2015. | [optional] |
| **pVioLastYear** | **String**| Identifies if a permit violation has occured in the last year.  Valid values are Y and N. | [optional] [enum: Y, N] |
| **responseset** | **BigDecimal**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |
| **pPrettyPrint** | **BigDecimal**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] |
| **pE90Count** | **BigDecimal**| Number of E90 Exceedances.  Identifies water permits with a number of E90 (Effluient Exceedances) &gt;&#x3D; the value provided for the last number of years provided by the p_e90_years value. | [optional] |
| **pE90Years** | **BigDecimal**| Number of years for the p_e90_count search.  Identified the past number of years to be used for the p_e90_count search. | [optional] |
| **pPsc** | **String**| Point Source Category. | [optional] |

### Return type

[**CwaRestServicesGetFacilityInfoGet200Response**](CwaRestServicesGetFacilityInfoGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results will either be an array of Facilities or an array of Clusters. The search will return clusters if the number of facilities returned is greater than the resposeset size, otherwise individual facility records will be returned. |  -  |

<a id="cwaRestServicesGetFacilityInfoPost"></a>
# **cwaRestServicesGetFacilityInfoPost**
> CwaRestServicesGetFacilityInfoGet200Response cwaRestServicesGetFacilityInfoPost(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pFrs, pReg, pSic, pNcs, pPen, xmin, ymin, xmax, ymax, pUsmex, pSic2, pSic4, pFa, pFf, pAct, pMaj, pMact, pFea, pFeay, pFeaa, pIea, pIeay, pIeaa, pQiv, pIv, pImpw, pImpPol, pImpCauGrp, pTrep, pPm, pPd, pIco, pHuc, pPid, pMed, pYsl, pYsly, pYsla, pQs, pSfs, pTribeid, pTribename, pTribedist, pPstat, pPtype, pPcomp, pPlimits, pPcss, pPexp, pOwop, pIpfti, pAgoo, pIdt1, pIdt2, pPityp, pPfead1, pPfead2, pPfeat, pPccs, pPexcd, pPsncq, pPctrack, pDwd, pPt, pPdwdist, pPswdpc, pPswdmp, pPswpol, pPswcas, pPswparam, pPswvio, pWbd, pRadwbd, pFrswbd, pFntype, pPidall, pMonthsLastDmr, pLastDmrWithin, pIndsw, pMsgpPtype, pMonType, pIagency, pPermittingAgency, pIsws, pIswss, pIswssID, pDs1, pDs2, pDa1, pDa2, pMS4, pOoFN, pOoFNtype, pOoSA, pOoSA1, pOoCt, pOoSt, pOoZip, pFacIco, pIcoo, pFacIcos, pEjscreen, pAlrexceed, pLimitAddr, pLat, pLong, pRadius, pEjscreenOver80cnt, pBioFlag, pBioFacType, pBioTrtmntProcs, pBioAnalyMethodCatgry, pBioTotalVolumeAmt, pBioMgmtPrctceType, pBioMgmtPrctceStype, pBioMgmtPrctceHandler, pBioMgmtContainer, pBioMgmtPathogen, pBioMgmtPathred, pBioMgmtVector, pBioMgmtDefCategory, pBioMgmtDeficiencies, pBioVioCode, pBioCurrentVio, pBioQtrsInVio, pBioRptYear, pBioVioLastYear, pMsgpRptYear, pVioLastYear, responseset, paramCallback, qcolumns, pPrettyPrint, pE90Count, pE90Years, pPsc)

Clean Water Act (CWA) Facility Enhanced Search Service

Returns either an array of Facilities or an array of Clusters that meet the specified search criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInformationApi apiInstance = new FacilityInformationApi(defaultClient);
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language. - CSV = Facility results formatted as comma delimited file download. - GEOJSON = Facility results formatted as GeoJSON feature collection. - GEOJSONP = Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
    String pFn = "pFn_example"; // String | Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
    String pSa = "pSa_example"; // String | Facility street address. Enter a complete or partial street address.
    String pSa1 = "pSa1_example"; // String | Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa.
    String pCt = "pCt_example"; // String | Facility City Filter. Enter a single case-insensitive city name to filter results.
    String pCo = "pCo_example"; // String | Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
    String pFips = "pFips_example"; // String | FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
    String pSt = "pSt_example"; // String | Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
    String pZip = "pZip_example"; // String | 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values.
    String pFrs = "pFrs_example"; // String | Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results.
    String pReg = "01"; // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    String pSic = "pSic_example"; // String | Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4.
    String pNcs = "pNcs_example"; // String | North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
    String pPen = "pPen_example"; // String | Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER = No Penalties - ANY = Any Penalty - LEXX = Less than or equal to XX months.  Provide a number in place of XX, e.g. \\\"LE5\\\" for a facility with a penalty within previous 5 months. - GTXX = Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago.
    BigDecimal xmin = new BigDecimal(78); // BigDecimal | Minimum longitude value in decimal degrees.
    BigDecimal ymin = new BigDecimal(78); // BigDecimal | Minimum latitude value in decimal degrees.
    BigDecimal xmax = new BigDecimal(78); // BigDecimal | Maximum longitude value in decimal degrees.
    BigDecimal ymax = new BigDecimal(78); // BigDecimal | Maximum latitude value in decimal degrees.
    String pUsmex = "Y"; // String | US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
    String pSic2 = "pSic2_example"; // String | Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \\\"22\\\" to match all SIC codes beginning with 22.  Use the \\\"%\\\" character within strings to match any SIC values with the pattern.  For example, \\\"2%21\\\" matches 2021, 2121, 2221, etc.
    String pSic4 = "pSic4_example"; // String | Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker.
    String pFa = "pFa_example"; // String | Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values.
    String pFf = "Y"; // String | Federal Facility Indicator Flag. Enter Y to restrict searches to federal facilities.
    String pAct = "pAct_example"; // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.  A Y will select ICIS NPDES permits with a status of effective, continued, or expired.
    String pMaj = "Y"; // String | Major Facility Flag.  Enter Y to restrict results to Major facilities only.
    String pMact = "pMact_example"; // String | CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility.
    String pFea = "W"; // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
    BigDecimal pFeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
    String pFeaa = "A"; // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
    String pIea = "W"; // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
    BigDecimal pIeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
    String pIeaa = "E"; // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
    String pQiv = "0"; // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    String pIv = "pIv_example"; // String | Facility has a violation status of 'In Viol' during any of the selected quarters.   Range: Fiscal Year 2020 Quarter 2 to Fiscal Year 2017 Quarter 2  Multiple values are comma delimited.   ||||||  Fiscal Years |||||| - FY2020 or FY20 or 2020 or 20 - FY2019 or FY19 or 2019 or 19 - FY2018 or FY18 or 2018 or 18 - FY2017 or FY17 or 2017 or 17  ||||| Fiscal Quarters ||||| - FY2020Q2 or FY20Q2 or 20202 or 202 or 13 - FY2020Q1 or FY20Q1 or 20201 or 201 or 12 - FY2019Q4 or FY19Q4 or 20194 or 194 or 11 - FY2019Q3 or FY19Q3 or 20193 or 193 or 10 - FY2019Q2 or FY19Q2 or 20192 or 192 or 9 - FY2019Q1 or FY19Q1 or 20191 or 191 or 8 - FY2018Q4 or FY18Q4 or 20184 or 184 or 7 - FY2018Q3 or FY18Q3 or 20183 or 183 or 6 - FY2018Q2 or FY18Q2 or 20182 or 182 or 5 - FY2018Q1 or FY18Q1 or 20181 or 181 or 4 - FY2017Q4 or FY17Q4 or 20174 or 174 or 3 - FY2017Q3 or FY17Q3 or 20173 or 173 or 2 - FY2017Q2 or FY17Q2 or 20172 or 172 or 1
    String pImpw = "Y"; // String | Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
    String pImpPol = "Y"; // String | Facility is discharging pollutants that are potentially contributing to the impairment of local waterbodies according to the ATTAINS database.
    String pImpCauGrp = "ALGAL GROWTH"; // String | Facility is discharging a pollutant group causing a waterbody to be impaired.  Enter 1 through 34 (the internal number of the pollutant group); or enter a partial name such as Dioxin,Temp,tUrBidity.
    String pTrep = "CURR"; // String | Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR = Current TRI reporter. - NONCURR = Has reported to TRI in the past but not for the current reporting year.
    String pPm = "NONE"; // String | Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE = 0% - GT5 = greater than 5% - GT10 = greater than 10% - GT25 = greater than 25% - GT50 = greater than 50% - GT75 = greater than 75%
    String pPd = "NONE"; // String | Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE = 0 population density per square mile - GT100 = More than 100 population density per square mile - GT500 = More than 500 population density per square mile - GT1000 = More than 1000 population density per square mile - GT5000 = More than 5000 population density per square mile - GT10000 = More than 10000 population density per square mile - GT20000 = More than 20000 population density per square mile
    String pIco = "Y"; // String | Indian Country Flag.  Enter a \\\"Y\\\" or \\\"N\\\" to restrict searches to facilities inside or outside Indian Country.
    String pHuc = "pHuc_example"; // String | 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
    String pPid = "pPid_example"; // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    String pMed = "A"; // String | Filter Results by Media. - A = Air - M = RMP (Risk Management Plan) - R = RCRA (Hazardous Waste) - S = SDWA (Public Drinking Water Systems) - ALL = Air and RCRA and Water
    String pYsl = "W"; // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
    BigDecimal pYsly = new BigDecimal("1"); // BigDecimal | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
    String pYsla = "E"; // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
    String pQs = "pQs_example"; // String | Quick Search. Allows entry for city, state, and/or zip code.
    String pSfs = "pSfs_example"; // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
    BigDecimal pTribeid = new BigDecimal(78); // BigDecimal | Numeric code for tribe (or list of tribes).
    String pTribename = "pTribename_example"; // String | Tribe Name Filter.  Enter a single tribe name to filter results.
    BigDecimal pTribedist = new BigDecimal(78); // BigDecimal | Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
    String pPstat = "pPstat_example"; // String | Permit Status Filter.  Enter one or more of the following codes.  Provide multiple values as a comma-delimited list. - EFF = Effective - EXP = Expired - PND = Pending - TRM = Terminated - RET = Retired - NON = Not Needed - ADC = Admin Continued
    String pPtype = "pPtype_example"; // String | Permit Type Filter. Enter one or more code values to filter results.  Provide multiple values as a comma-delimited list. - NPD = NPDES Individual Permit - NGP = NPDES Master General Permit - GPC = General Permit Covered Facility - SNN = State Issued Master General Permit (Non-NPDES) - IIU = Individual IU Permit (Non-NPDES) - SIN = Individual State Issued Permit (Non-NPDES) - APR = Associated Permit Record - UFT = Unpermitted Facility
    String pPcomp = "pPcomp_example"; // String | Permit Component Code Filter.  Enter one or more codes to filter results.  Provide multiple values as a comma-delimited list. - PRE = Pretreatment - CAF = CAFO - CSO = CSO - POT = POTW - BIO = Biosolids - SWS = Storm Water Small MS4s - SWM = Storm Water Medium/Large MS4s - SWI = Storm Water Industrial - SWC = Storm Water Construction
    String pPlimits = "Y"; // String | Permit Limits Present Flag.  Enter Y to limit results to facilities have present permit limits.
    String pPcss = "ALL"; // String | Combined Sewer Systems Outflows Limiter.  Enter one of the following to limit results to facilities having the given count of CSS outflows. - ALL = returns all facilities, regardless of the number of outflows. - GE1 = returns facilities with one or more outflows. - GE10 = returns facilities with ten or more outflows. - GE50 = returns facilities with fifty or more outflows.
    String pPexp = "EXP"; // String | Permit Expired or Administratively Continued Limiter.  Enter one of the following values to filter results. - EXP = limit results to facilities with permits expired or administratively continued. - EXPLE1YR = limit resuls to facilities with permits expired administratively continued within the past year. - EXPGT1YR = limit resuls to facilities with permits expired administratively continued more than a year ago.
    String pOwop = "FEDERAL"; // String | Owner/Operator code filter.  Enter one of the following values to restrict results. - Federal = Federal facilities regulated under the NPDES program. - POTW = Publicly owned treatment works. Treatment works that are owned by a State, Tribe, or municipality. - Non-POTW = Non-publicly owned treatment works. Often referred to as \\\"non-municipals\\\" or \\\"industrials\\\".
    String pIpfti = "pIpfti_example"; // String | 
    String pAgoo = "AND"; // String | Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
    String pIdt1 = "pIdt1_example"; // String | Beginning of date range of most recent facility inspection.
    String pIdt2 = "pIdt2_example"; // String | End of date range of most recent facility inspection.
    String pPityp = "pPityp_example"; // String | Inspection Type Code.  See ICIS Compliance Monitor Types lookup serivce for a list of available codes and descriptions.
    String pPfead1 = "pPfead1_example"; // String | Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    String pPfead2 = "pPfead2_example"; // String | Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    String pPfeat = "pPfeat_example"; // String | Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
    String pPccs = "pPccs_example"; // String | Current Compliance Status: |||||||||||||||||||||||||||  Significant Noncompliance (SNC)  ||||||||||||||||||||||||||| - SNC = E, S, X, T, D - E�= E(EffViol) - S�= S(CSchVio) - X = X(EffNMth) - T = T(CSchRpt) - D�= D(DMR NR)  ||||||||||||||||||||||||||| Noncompliance (NC) ||||||||||||||||||||||||||| - NC = N, V - N�= N(RptViol) - V�= V(NonRNCV)  ||||||||||||||||||||||||||| New Violations (PQV) ||||||||||||||||||||||||||| - PQV = New Violations (13th Quarter)  ||||||||||||||||||||||||||| No Violations (NV) ||||||||||||||||||||||||||| - NV = R, P, M, U, W , Blank, and No New Violations (no PQV) - R�= R(Resolvd) - P�= P(ResPend) - M�= C(Manual) - U = U(N/A) - W = W(N/A) - Blank = (null)  May contain multiple comma-separated values.
    String pPexcd = "0"; // String | 3-Year Effluent Exceedances Limiter.  Enter a value to restrict results to facilities with the given amount of exceedances in the past 3 years. - 0 = facilities with no exceedances - GE0 = facilities with one or more exceedances - GE10 = facilities with ten or more exceedances - GE50 = facilities with fifty or more exceedances - GE100 = facilities with one hundred or more exceedances
    String pPsncq = "GT1"; // String | Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z = Zero quarters in significant noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in significant noncompliance.
    String pPctrack = "false"; // String | Compliance Tracking Limiter. Provide a keyword to indicate the extent to which data is being entered and effluent exceedances are being identified. - Off - Partial - On
    String pDwd = "0"; // String | Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory.
    String pPt = "0"; // String | POTW Transfers. Pounds of toxic chemicals transferred to a Publicly Operated Treatment Works (POTW) as reported to the Toxics Release Inventory.
    String pPdwdist = "N"; // String | Distance (in miles) to downstream drinking water intake.
    String pPswdpc = "pPswdpc_example"; // String | Pollutant Category Code:  Values: WTR for Water, AIR for Air
    String pPswdmp = "1"; // String | Used to determine limit begin and end dates for surface water discharges. Number represents years from current date.
    String pPswpol = "pPswpol_example"; // String | For CWA, pollutant names for surface water discharges. for Drinking Water, SDWIS Violation contaminant codes for unaddressed violations that have occurred in the last 3 years. May contain multiple comma-separated values.
    String pPswcas = "pPswcas_example"; // String | CAS numbers for surface water discharges. May contain multiple comma-separated values.
    String pPswparam = "pPswparam_example"; // String | Parameter codes for surface water discharges. May contain multiple comma-separated values.
    String pPswvio = "Y"; // String | Used in conjuction with parameters p_pswpol and p_pswparam, indicates whether search should only include pollutants with violations.
    String pWbd = "pWbd_example"; // String | 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    String pRadwbd = "pRadwbd_example"; // String | 2-, 4-, 6-, 8-, 10-, or 12 character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Will search against WBD values otained by \\\"reach indexing\\\" NPDES permits against the medium resolution National Hydrography Dataset. 
    String pFrswbd = "pFrswbd_example"; // String | Works exactly the same as the p_wbd parameter.  2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    String pFntype = "ALL"; // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
    String pPidall = "Y"; // String | Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc).
    BigDecimal pMonthsLastDmr = new BigDecimal(78); // BigDecimal | The number of months since the last Discharge Monitoring Report has been submitted.
    String pLastDmrWithin = "W"; // String | W value returns facilities that have submitted DMRs within the number of months specified by p_months_last_dmr. An N value returns facilities that have not submitted a DMR within the specified number of months.
    String pIndsw = "Y"; // String | Industrial Stormwater Permit Flag.  Enter a Y or N to filter results by this type of permit.
    String pMsgpPtype = "NOI"; // String | Multi-Sector General Purpose Permit Type.  Enter a value to filter results by MSGP Permit Type. - NOI = Notice of Intent - NOE = No Exposure Certification
    String pMonType = "BENCHG2"; // String | For use with the Industrial Stormwater search only. Valid values are BENCHGS fro Benchmark (Alert Limit) G2 Ore, BENCH for Benchmark (Alert Limit), and ELG fro Effluent Limitation Guidelines(ELG)(Effluent Limit).  
    String pIagency = "pIagency_example"; // String | Issuing Agency Limiter.  Enter a single value to filter results by the issuing agency, e.g. \\\"State\\\" or \\\"EPA\\\".
    String pPermittingAgency = "pPermittingAgency_example"; // String | 
    String pIsws = "pIsws_example"; // String | Multi-Sector General Purpose Permit Subsector Individual Identifier.  Enter a value to filter results.
    String pIswss = "pIswss_example"; // String | Multi-Sector General Purpose Permit Subsector Group Code.  Enter a value to filter results.
    String pIswssID = "pIswssID_example"; // String | Multi-Sector General Purpose Permit Sector Code.  Enter a value to filter results.
    String pDs1 = "pDs1_example"; // String | Submitted Date Filter Start.  To filter by the date of submission, enter a start date here and an end date in the p_ds2 parameter.  Both dates are required for filtering.
    String pDs2 = "pDs2_example"; // String | Submitted Date Filter End.  To filter by the date of submission, enter an end date here and a start date in the p_ds1 parameter.  Both dates are required for filtering.
    String pDa1 = "pDa1_example"; // String | Active Date Filter Start.  To filter by the active date, enter a start date here and an end date in the p_da2 parameter.  Both dates are required for filtering.
    String pDa2 = "pDa2_example"; // String | Active Date Filter End.  To filter by the active date, enter an end date here and a start date in the p_da1 parameter.  Both dates are required for filtering.
    String pMS4 = "Y"; // String | Municipal Separate Storm Water Sewer (MS4) Permit Flag.  Enter a Y or N to filter results by this type of permit.
    String pOoFN = "pOoFN_example"; // String | Owner/Operator Name. Enter the owner/operator name of the facility.
    String pOoFNtype = "ALL"; // String | Owner/Operator Name Multiple Selection Evaluator.  
    String pOoSA = "pOoSA_example"; // String | Owner/Operator Address.  Enter the address of the owner/operator of the facility.
    String pOoSA1 = "pOoSA1_example"; // String | Owner/Operator Address Line 2.  Enter the line 2 address of the owner/operator of the facility.
    String pOoCt = "pOoCt_example"; // String | Owner/Operator City. Enter the city where the owner/operator of the facility is located.
    String pOoSt = "pOoSt_example"; // String | Owner/Operator State.  Enter the standardized postal state code where the owner/operator of the facility is located.
    String pOoZip = "pOoZip_example"; // String | Owner/Operator Zip Code.  Enter the postal zip code where the owner/operator of the facility is located.
    String pFacIco = "Y"; // String | FRS tribal land code flag.  Enter \\\"Y\\\" or \\\"N\\\" to include or exclude facilities based on FRS tribal land code.
    String pIcoo = "pIcoo_example"; // String | Indian country search and/or flag.  Enter \\\"Y\\\" to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
    String pFacIcos = "pFacIcos_example"; // String | FRS tribal land spatial flag.  Enter \\\"Y\\\" or \\\"N\\\" to include or exclude facilities based on FRS tribal land spatial flag.
    String pEjscreen = "pEjscreen_example"; // String | Enter \\\"Y\\\" to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
    BigDecimal pAlrexceed = new BigDecimal(78); // BigDecimal | Alert Limits Exceedences Limiter.  Enter a numeric value to restrict results to facilities having the given amount or more of alert limits exceedances.
    String pLimitAddr = "Y"; // String | Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
    BigDecimal pLat = new BigDecimal(78); // BigDecimal | Latitude location in decimal degrees.
    BigDecimal pLong = new BigDecimal(78); // BigDecimal | Longitude location in decimal degrees.
    BigDecimal pRadius = new BigDecimal(78); // BigDecimal | Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
    String pEjscreenOver80cnt = "1"; // String | The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
    String pBioFlag = "pBioFlag_example"; // String | A Y value will select all biosolid-related permits.
    String pBioFacType = "pBioFacType_example"; // String | The code indicating the reporting obligation reason:  - POT = A POTW with a design flow rate equal to or greater than one million gallons per day - CLI = A Class I Sludge Management Facility as defined in 40 CFR 503.9 - PPL = A POTW that serves 10,000 people or more - OTH = Otherwise required to report (e.g., permit condition, enforcement action) - NOA = None of the above
    String pBioTrtmntProcs = "pBioTrtmntProcs_example"; // String | The biosolids or sewage sludge treatment process or processes at the facility:  - AER = Aerobic Digestion - AIR = Air Drying (or Sludge Drying Beds) - ANA = Anaerobic Digestion - COD = Beta Ray Irradiation - COM = Lower Temperature Composting - DEW = Pasteurization - DIS = Gamma Ray Irradiation - HEA = Heat Drying (e.g., Flash Dryer, Spray Dryer, Rotary Dryer) - HET = Heat Treatment (Liquid Sewage Sludge Heated to 356 Deg. F/180 Deg. C or Higher for 30 min.) - HTC = Higher Temperature Composting - MET = Methane or Biogas Capture and Recovery - OTH = Other Treatment Process - PRE = Preliminary Operations (e.g., Sludge Grinding, Degritting, Blending) - SLU = Sludge Lagoon - STA = Lime Stabilization - THE = Temporary Sludge Storage (Sewage Sludge Stored on Land 2 Years or Less, Not in Sewage Sludge Unit) - THI = Thickening (Gravity and/or Flotation Thickening, Centrifugation, Belt Filter Press, Vacuum Filter) - THM = Thermophilic Aerobic Digestion - UND = Long-Term Sludge Storage (Sewage Sludge Stored on Land 2 Years or More, not in Sewage Sludge Unit)\\\"
    String pBioAnalyMethodCatgry = "pBioAnalyMethodCatgry_example"; // String | The unique code for the category of the analytic methods used by the facility to analyze regulated parameters (including enteric viruses, fecal coliforms, helminth ova, and Salmonella sp.) at the facility:  - PAT = Pathogens - MET = Metals - NIT = Nitrogen Compounds - OTH = Other Analytes
    String pBioTotalVolumeAmt = "pBioTotalVolumeAmt_example"; // String | Total annual amount (in dry metric tons) of biosolids or sewage sludge generated at the facility.  - EQ0 = 0 - IN0_1 = GT 0 but LT 1 - IN0_289  =  GT 0 but LT 290 MT/year - IN290_1499  =  GE 290 but LT 1500 MT/year - IN1500_14999  =  GE 1500 but LT 15,000 - GE15000  =  GE 15,000
    String pBioMgmtPrctceType = "pBioMgmtPrctceType_example"; // String | The unique code that identifies the type of biosolids or sewage sludge management practice (e.g., land application, surface disposal, incineration) used by the facility. The facility will separately report the management practice for each biosolids or sewage sludge form and pathogen class. This data element will also identify the management practices used by surface disposal site owners/operators (see 40 CFR 503.24):  - BIN = Incineration - BLN = Land Application - BOT = Other Management Practice - BSD = Surface Disposal
    String pBioMgmtPrctceStype = "pBioMgmtPrctceStype_example"; // String | This is the code indicating additional detail about the type of Management Practice used for a volume of Biosolids or Sewage Sludge:  - ADV = Advanced Alkaline Stabilized Biosolids Distribution & Marketing - AGR = Agricultural Land Application - COM = Distribution and Marketing - Compost - DEE = Deep-well Injection Disposal - DIS = Disposal in a Municipal Landfill (under 40 CFR 258) - DMO = Distribution and Marketing - Other - HEA = Heat Dried Biosolids Distribution & Marketing - OTL = Other Land Application Management Practice Detail - OTO = Other Management Practice Detail - RSA = Reclamation Site Application - SEN = Sent to Cement Kiln for Use as Alternative Energy - STO = Storage - UIC = Use in Construction - UPS = Used in Production of Syngas - USE = Use as Daily Cover for Municipal Landfill (under 40 CFR 258)
    String pBioMgmtPrctceHandler = "pBioMgmtPrctceHandler_example"; // String | This is the code indicating the type of Biosolids or Sewage Sludge handlers/preparers.  - OWN = Owner or Operator - OFF = Off-Site Third-Party Handler or Preparer
    String pBioMgmtContainer = "pBioMgmtContainer_example"; // String | The code that identifies the nature of each biosolids and sewage sludge material generated by the facility in terms of whether the material is a biosolid or sewage sludge and whether the material is ultimately conveyed off-site in bulk or in bags. The facility separately reports the form for each biosolids or sewage sludge management practice or practices used by the facility and pathogen class:  - BUL = Bulk - BAG = Bag or Container
    String pBioMgmtPathogen = "pBioMgmtPathogen_example"; // String | This code identifies the pathogen class [e.g., Class A, Class B, Not Applicable (Incineration)] for biosolids or sewage sludge generated by the facility. The facility will separately report the pathogen class for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form. It also is used to filter applicable Pathogen Reduction and Vector Attraction Reduction Options as well as Land Application Management Practice Deficiencies. Only reqired for some of the mgmt. practice types:  - AAA = Class A - AEQ = Class A EQ (sale/give away) - BBB = Class B - NAP = Not Applicable (Incineration)
    String pBioMgmtPathred = "pBioMgmtPathred_example"; // String | This is the description of the option used by the facility to control pathogen for a Biosolids Management Practice:  - A1 = Class A - Alternative 1: Time/Temperature - A2 = Class A - Alternative 2: pH/Temperature/Percent Solids - A3 = Class A - Alternative 3: Test Enteric Viruses and Helminth ova; Operating Parameters - A4 = Class A - Alternative 4: Test Enteric Viruses and Helminth ova; No New Solids - A51 = Class A - Alternative 5: PFRP 1: Composting - A52 = Class A - Alternative 5: PFRP 2: Heat Drying - A53 = Class A - Alternative 5: PFRP 3: Liquid heat treatment - A54 = Class A - Alternative 5: PFRP 4: Thermophilic Aerobic Digestion (ATAD) - A55 = Class A - Alternative 5 PFPR 5: Beta Ray Irradiation - A56 = Class A - Alternative 5 PFPR 6: Gamma Ray Irradiation - A57 = Class A - Alternative 5: PFRP 7: Pasteurization - A6 = Class A - Alternative 6: PFRP Equivalency - B1 = Class B - Alternative 1: Fecal Coliform Geometric Mean - B21 = Class B - Alternative 2 PSRP 1: Aerobic Digestion - B22 = Class B - Alternative 2 PSRP 2: Air Drying - B23 = Class B - Alternative 2 PSRP 3: Anaerobic Digestion - B24 = Class B - Alternative 2 PSRP 4: Composting - B25 = Class B - Alternative 2 PSRP 5: Lime Stabilization - B3 = Class B - Alternative 3: PSRP Equivalency - PH = pH Adjustment (Domestic Septage)
    String pBioMgmtVector = "pBioMgmtVector_example"; // String | The unique code that identifies the option used by the facility for vector attraction reduction. See a listing of these vector attraction reduction options at 40 CFR 503.33(b)(1) through (11). The facility will separately report the vector attraction reduction options for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form as well as by each biosolids or sewage sludge pathogen class:  - VR1 = Option 1 - Volatile Solids Reduction - VR2 = Option 2 - Bench-Scale Volatile Solids Reduction (Anaerobic Bench Test) - VR3 = Option 3 - Bench-Scale Volatile Solids Reduction (Aerobic Bench Test w/ Percent Solids - 2% or Less) - VR4 = Option 4 - Specific Oxygen Uptake Rate - VR5 = Option 5 - Aerobic Processing (Thermophilic Aerobic Digestion/Composting) - VR6 = Option 6 - Alkaline Treatment - VR7 = Option 7 - Drying (Equal to or Greater than 75 Percent) - VR8 = Option 8 - Drying (Equal to or Greater than 90 Percent) - VR9 = Option 9 - Sewage Sludge Injection - V10 = Option 10 - Sewage Sludge Timely Incorporation into Land - V11 = Option 11 - Sewage Sludge Covered at the End of Each Operating Day
    String pBioMgmtDefCategory = "pBioMgmtDefCategory_example"; // String | This is the code indicating the type of NPDES special regulatory program deficiency:  - INC = Biosolids Incineration - LNA = Biosolids Land Application - LNB = Biosolids Land Application - Pathogen Class B - OTB = Biosolids Other Management Practice - SFD = Biosolids Surface Disposal
    BigDecimal pBioMgmtDeficiencies = new BigDecimal(78); // BigDecimal | The number of times noncompliance was reported by the facility in the last 3 years. The results returned will include facilities whose number of reported noncompliance events is greater than or equal to the number entered.
    String pBioVioCode = "pBioVioCode_example"; // String | The Biosolids Single Event Violation Code.  Enter one or mode codes.
    String pBioCurrentVio = "Y"; // String | Indicator of whether the facility is currently in violation for biosolids under the Clean Water Act, in the 12th or 13th quarter:  - Y = Yes - N = No
    BigDecimal pBioQtrsInVio = new BigDecimal(78); // BigDecimal | The number of quarters, in the last three years, where the facility was in violation for a biosolids violation type.  The results returned will include facilities whose number of quarters with violations is greater than or equal to the number entered.
    String pBioRptYear = "pBioRptYear_example"; // String | The last year that the permittee submitted an annual Biosolids report.  Valid values are NONE and any year greater or equal to 2016.
    String pBioVioLastYear = "Y"; // String | Identifies if a biosolids violation has occured in the last year.  Valid values are Y and N.
    String pMsgpRptYear = "pMsgpRptYear_example"; // String | The last year that a MSGP report was submitted for the permit.  Valid values are \\\"NONE\\\" and any year Greater or Eqal to 2015.
    String pVioLastYear = "Y"; // String | Identifies if a permit violation has occured in the last year.  Valid values are Y and N.
    BigDecimal responseset = new BigDecimal(78); // BigDecimal | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    BigDecimal pE90Count = new BigDecimal(78); // BigDecimal | Number of E90 Exceedances.  Identifies water permits with a number of E90 (Effluient Exceedances) >= the value provided for the last number of years provided by the p_e90_years value.
    BigDecimal pE90Years = new BigDecimal(78); // BigDecimal | Number of years for the p_e90_count search.  Identified the past number of years to be used for the p_e90_count search.
    String pPsc = "pPsc_example"; // String | Point Source Category.
    try {
      CwaRestServicesGetFacilityInfoGet200Response result = apiInstance.cwaRestServicesGetFacilityInfoPost(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pFrs, pReg, pSic, pNcs, pPen, xmin, ymin, xmax, ymax, pUsmex, pSic2, pSic4, pFa, pFf, pAct, pMaj, pMact, pFea, pFeay, pFeaa, pIea, pIeay, pIeaa, pQiv, pIv, pImpw, pImpPol, pImpCauGrp, pTrep, pPm, pPd, pIco, pHuc, pPid, pMed, pYsl, pYsly, pYsla, pQs, pSfs, pTribeid, pTribename, pTribedist, pPstat, pPtype, pPcomp, pPlimits, pPcss, pPexp, pOwop, pIpfti, pAgoo, pIdt1, pIdt2, pPityp, pPfead1, pPfead2, pPfeat, pPccs, pPexcd, pPsncq, pPctrack, pDwd, pPt, pPdwdist, pPswdpc, pPswdmp, pPswpol, pPswcas, pPswparam, pPswvio, pWbd, pRadwbd, pFrswbd, pFntype, pPidall, pMonthsLastDmr, pLastDmrWithin, pIndsw, pMsgpPtype, pMonType, pIagency, pPermittingAgency, pIsws, pIswss, pIswssID, pDs1, pDs2, pDa1, pDa2, pMS4, pOoFN, pOoFNtype, pOoSA, pOoSA1, pOoCt, pOoSt, pOoZip, pFacIco, pIcoo, pFacIcos, pEjscreen, pAlrexceed, pLimitAddr, pLat, pLong, pRadius, pEjscreenOver80cnt, pBioFlag, pBioFacType, pBioTrtmntProcs, pBioAnalyMethodCatgry, pBioTotalVolumeAmt, pBioMgmtPrctceType, pBioMgmtPrctceStype, pBioMgmtPrctceHandler, pBioMgmtContainer, pBioMgmtPathogen, pBioMgmtPathred, pBioMgmtVector, pBioMgmtDefCategory, pBioMgmtDeficiencies, pBioVioCode, pBioCurrentVio, pBioQtrsInVio, pBioRptYear, pBioVioLastYear, pMsgpRptYear, pVioLastYear, responseset, paramCallback, qcolumns, pPrettyPrint, pE90Count, pE90Years, pPsc);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInformationApi#cwaRestServicesGetFacilityInfoPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. - CSV &#x3D; Facility results formatted as comma delimited file download. - GEOJSON &#x3D; Facility results formatted as GeoJSON feature collection. - GEOJSONP &#x3D; Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download. | [optional] |
| **pFn** | **String**| Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers. | [optional] |
| **pSa** | **String**| Facility street address. Enter a complete or partial street address. | [optional] |
| **pSa1** | **String**| Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa. | [optional] |
| **pCt** | **String**| Facility City Filter. Enter a single case-insensitive city name to filter results. | [optional] |
| **pCo** | **String**| Facility County Filter. Provide a single county name in combination with a state value provided via p_st. | [optional] |
| **pFips** | **String**| FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059. | [optional] |
| **pSt** | **String**| Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pZip** | **String**| 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values. | [optional] |
| **pFrs** | **String**| Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results. | [optional] |
| **pReg** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] [enum: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10] |
| **pSic** | **String**| Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4. | [optional] |
| **pNcs** | **String**| North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values. | [optional] |
| **pPen** | **String**| Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER &#x3D; No Penalties - ANY &#x3D; Any Penalty - LEXX &#x3D; Less than or equal to XX months.  Provide a number in place of XX, e.g. \\\&quot;LE5\\\&quot; for a facility with a penalty within previous 5 months. - GTXX &#x3D; Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago. | [optional] |
| **xmin** | **BigDecimal**| Minimum longitude value in decimal degrees. | [optional] |
| **ymin** | **BigDecimal**| Minimum latitude value in decimal degrees. | [optional] |
| **xmax** | **BigDecimal**| Maximum longitude value in decimal degrees. | [optional] |
| **ymax** | **BigDecimal**| Maximum latitude value in decimal degrees. | [optional] |
| **pUsmex** | **String**| US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border. | [optional] [enum: Y, N] |
| **pSic2** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \\\&quot;22\\\&quot; to match all SIC codes beginning with 22.  Use the \\\&quot;%\\\&quot; character within strings to match any SIC values with the pattern.  For example, \\\&quot;2%21\\\&quot; matches 2021, 2121, 2221, etc. | [optional] |
| **pSic4** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker. | [optional] |
| **pFa** | **String**| Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values. | [optional] |
| **pFf** | **String**| Federal Facility Indicator Flag. Enter Y to restrict searches to federal facilities. | [optional] [enum: Y] |
| **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.  A Y will select ICIS NPDES permits with a status of effective, continued, or expired. | [optional] |
| **pMaj** | **String**| Major Facility Flag.  Enter Y to restrict results to Major facilities only. | [optional] [enum: Y, N] |
| **pMact** | **String**| CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility. | [optional] |
| **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pFeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] [enum: A, E, S] |
| **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pIeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S] |
| **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] [enum: 0, GT1, GT2, GT4, GT8, 12] |
| **pIv** | **String**| Facility has a violation status of &#39;In Viol&#39; during any of the selected quarters.   Range: Fiscal Year 2020 Quarter 2 to Fiscal Year 2017 Quarter 2  Multiple values are comma delimited.   ||||||  Fiscal Years |||||| - FY2020 or FY20 or 2020 or 20 - FY2019 or FY19 or 2019 or 19 - FY2018 or FY18 or 2018 or 18 - FY2017 or FY17 or 2017 or 17  ||||| Fiscal Quarters ||||| - FY2020Q2 or FY20Q2 or 20202 or 202 or 13 - FY2020Q1 or FY20Q1 or 20201 or 201 or 12 - FY2019Q4 or FY19Q4 or 20194 or 194 or 11 - FY2019Q3 or FY19Q3 or 20193 or 193 or 10 - FY2019Q2 or FY19Q2 or 20192 or 192 or 9 - FY2019Q1 or FY19Q1 or 20191 or 191 or 8 - FY2018Q4 or FY18Q4 or 20184 or 184 or 7 - FY2018Q3 or FY18Q3 or 20183 or 183 or 6 - FY2018Q2 or FY18Q2 or 20182 or 182 or 5 - FY2018Q1 or FY18Q1 or 20181 or 181 or 4 - FY2017Q4 or FY17Q4 or 20174 or 174 or 3 - FY2017Q3 or FY17Q3 or 20173 or 173 or 2 - FY2017Q2 or FY17Q2 or 20172 or 172 or 1 | [optional] |
| **pImpw** | **String**| Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database. | [optional] [enum: Y, N] |
| **pImpPol** | **String**| Facility is discharging pollutants that are potentially contributing to the impairment of local waterbodies according to the ATTAINS database. | [optional] [enum: Y, N] |
| **pImpCauGrp** | **String**| Facility is discharging a pollutant group causing a waterbody to be impaired.  Enter 1 through 34 (the internal number of the pollutant group); or enter a partial name such as Dioxin,Temp,tUrBidity. | [optional] [enum: ALGAL GROWTH, AMMONIA, BIOTOXINS, CAUSE UNKNOWN, CAUSE UNKNOWN - FISH KILLS, CAUSE UNKNOWN - IMPAIRED BIOTA, CHLORINE, DIOXINS, FISH CONSUMPTION ADVISORY, FLOW ALTERATION(S), HABITAT ALTERATIONS, MERCURY, METALS (OTHER THAN MERCURY), NOXIOUS AQUATIC PLANTS, NUISANCE EXOTIC SPECIES, NUISANCE NATIVE SPECIES, NUTRIENTS, OIL AND GREASE, ORGANIC ENRICHMENT/OXYGEN DEPLETION, OTHER CAUSE, PATHOGENS, PESTICIDES, PH/ACIDITY/CAUSTIC CONDITIONS, POLYCHLORINATED BIPHENYLS (PCBS), RADIATION, SALINITY/TOTAL DISSOLVED SOLIDS/CHLORIDES/SULFATES, SEDIMENT, TASTE, COLOR AND ODOR, TEMPERATURE, TOTAL TOXICS, TOXIC INORGANICS, TOXIC ORGANICS, TRASH, TURBIDITY] |
| **pTrep** | **String**| Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year. | [optional] [enum: CURR, NOTCURR] |
| **pPm** | **String**| Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75% | [optional] [enum: NONE, GT5, GT10, GT25, GT50, GT75] |
| **pPd** | **String**| Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile | [optional] [enum: NONE, GT100, GT500, GT1000, GT5000, GT10000, GT20000] |
| **pIco** | **String**| Indian Country Flag.  Enter a \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] [enum: Y, N] |
| **pHuc** | **String**| 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values. | [optional] |
| **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] |
| **pMed** | **String**| Filter Results by Media. - A &#x3D; Air - M &#x3D; RMP (Risk Management Plan) - R &#x3D; RCRA (Hazardous Waste) - S &#x3D; SDWA (Public Drinking Water Systems) - ALL &#x3D; Air and RCRA and Water | [optional] [enum: A, M, R, S, ALL] |
| **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N, NV] |
| **pYsly** | **BigDecimal**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S, A] |
| **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] |
| **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] |
| **pTribeid** | **BigDecimal**| Numeric code for tribe (or list of tribes). | [optional] |
| **pTribename** | **String**| Tribe Name Filter.  Enter a single tribe name to filter results. | [optional] |
| **pTribedist** | **BigDecimal**| Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated. | [optional] |
| **pPstat** | **String**| Permit Status Filter.  Enter one or more of the following codes.  Provide multiple values as a comma-delimited list. - EFF &#x3D; Effective - EXP &#x3D; Expired - PND &#x3D; Pending - TRM &#x3D; Terminated - RET &#x3D; Retired - NON &#x3D; Not Needed - ADC &#x3D; Admin Continued | [optional] |
| **pPtype** | **String**| Permit Type Filter. Enter one or more code values to filter results.  Provide multiple values as a comma-delimited list. - NPD &#x3D; NPDES Individual Permit - NGP &#x3D; NPDES Master General Permit - GPC &#x3D; General Permit Covered Facility - SNN &#x3D; State Issued Master General Permit (Non-NPDES) - IIU &#x3D; Individual IU Permit (Non-NPDES) - SIN &#x3D; Individual State Issued Permit (Non-NPDES) - APR &#x3D; Associated Permit Record - UFT &#x3D; Unpermitted Facility | [optional] |
| **pPcomp** | **String**| Permit Component Code Filter.  Enter one or more codes to filter results.  Provide multiple values as a comma-delimited list. - PRE &#x3D; Pretreatment - CAF &#x3D; CAFO - CSO &#x3D; CSO - POT &#x3D; POTW - BIO &#x3D; Biosolids - SWS &#x3D; Storm Water Small MS4s - SWM &#x3D; Storm Water Medium/Large MS4s - SWI &#x3D; Storm Water Industrial - SWC &#x3D; Storm Water Construction | [optional] |
| **pPlimits** | **String**| Permit Limits Present Flag.  Enter Y to limit results to facilities have present permit limits. | [optional] [enum: Y, N] |
| **pPcss** | **String**| Combined Sewer Systems Outflows Limiter.  Enter one of the following to limit results to facilities having the given count of CSS outflows. - ALL &#x3D; returns all facilities, regardless of the number of outflows. - GE1 &#x3D; returns facilities with one or more outflows. - GE10 &#x3D; returns facilities with ten or more outflows. - GE50 &#x3D; returns facilities with fifty or more outflows. | [optional] [enum: ALL, GE1, GE10, GE50] |
| **pPexp** | **String**| Permit Expired or Administratively Continued Limiter.  Enter one of the following values to filter results. - EXP &#x3D; limit results to facilities with permits expired or administratively continued. - EXPLE1YR &#x3D; limit resuls to facilities with permits expired administratively continued within the past year. - EXPGT1YR &#x3D; limit resuls to facilities with permits expired administratively continued more than a year ago. | [optional] [enum: EXP, EXPLE1YR, EXPGT1YR] |
| **pOwop** | **String**| Owner/Operator code filter.  Enter one of the following values to restrict results. - Federal &#x3D; Federal facilities regulated under the NPDES program. - POTW &#x3D; Publicly owned treatment works. Treatment works that are owned by a State, Tribe, or municipality. - Non-POTW &#x3D; Non-publicly owned treatment works. Often referred to as \\\&quot;non-municipals\\\&quot; or \\\&quot;industrials\\\&quot;. | [optional] [enum: FEDERAL, POTW, NON-POTW] |
| **pIpfti** | **String**|  | [optional] |
| **pAgoo** | **String**| Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters. | [optional] [enum: AND, OR] |
| **pIdt1** | **String**| Beginning of date range of most recent facility inspection. | [optional] |
| **pIdt2** | **String**| End of date range of most recent facility inspection. | [optional] |
| **pPityp** | **String**| Inspection Type Code.  See ICIS Compliance Monitor Types lookup serivce for a list of available codes and descriptions. | [optional] |
| **pPfead1** | **String**| Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] |
| **pPfead2** | **String**| Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] |
| **pPfeat** | **String**| Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list. | [optional] |
| **pPccs** | **String**| Current Compliance Status: |||||||||||||||||||||||||||  Significant Noncompliance (SNC)  ||||||||||||||||||||||||||| - SNC &#x3D; E, S, X, T, D - E�&#x3D; E(EffViol) - S�&#x3D; S(CSchVio) - X &#x3D; X(EffNMth) - T &#x3D; T(CSchRpt) - D�&#x3D; D(DMR NR)  ||||||||||||||||||||||||||| Noncompliance (NC) ||||||||||||||||||||||||||| - NC &#x3D; N, V - N�&#x3D; N(RptViol) - V�&#x3D; V(NonRNCV)  ||||||||||||||||||||||||||| New Violations (PQV) ||||||||||||||||||||||||||| - PQV &#x3D; New Violations (13th Quarter)  ||||||||||||||||||||||||||| No Violations (NV) ||||||||||||||||||||||||||| - NV &#x3D; R, P, M, U, W , Blank, and No New Violations (no PQV) - R�&#x3D; R(Resolvd) - P�&#x3D; P(ResPend) - M�&#x3D; C(Manual) - U &#x3D; U(N/A) - W &#x3D; W(N/A) - Blank &#x3D; (null)  May contain multiple comma-separated values. | [optional] |
| **pPexcd** | **String**| 3-Year Effluent Exceedances Limiter.  Enter a value to restrict results to facilities with the given amount of exceedances in the past 3 years. - 0 &#x3D; facilities with no exceedances - GE0 &#x3D; facilities with one or more exceedances - GE10 &#x3D; facilities with ten or more exceedances - GE50 &#x3D; facilities with fifty or more exceedances - GE100 &#x3D; facilities with one hundred or more exceedances | [optional] [enum: 0, GE0, GE10, GE50, GE100] |
| **pPsncq** | **String**| Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z &#x3D; Zero quarters in significant noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in significant noncompliance. | [optional] [enum: GT1, GE1, GT2, GE2, GT4, GE4, GT8, GE8, GT12, GE12] |
| **pPctrack** | **String**| Compliance Tracking Limiter. Provide a keyword to indicate the extent to which data is being entered and effluent exceedances are being identified. - Off - Partial - On | [optional] [enum: false, Partial, true] |
| **pDwd** | **String**| Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory. | [optional] [enum: 0, GT0, GT1000, GT5000, GT10000, GT20000, GT50000] |
| **pPt** | **String**| POTW Transfers. Pounds of toxic chemicals transferred to a Publicly Operated Treatment Works (POTW) as reported to the Toxics Release Inventory. | [optional] [enum: 0, GT0, GT1000, GT5000, GT10000, GT20000, GT50000] |
| **pPdwdist** | **String**| Distance (in miles) to downstream drinking water intake. | [optional] [enum: N, LT1, LT2, LT5, LT10, LT15] |
| **pPswdpc** | **String**| Pollutant Category Code:  Values: WTR for Water, AIR for Air | [optional] |
| **pPswdmp** | **String**| Used to determine limit begin and end dates for surface water discharges. Number represents years from current date. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pPswpol** | **String**| For CWA, pollutant names for surface water discharges. for Drinking Water, SDWIS Violation contaminant codes for unaddressed violations that have occurred in the last 3 years. May contain multiple comma-separated values. | [optional] |
| **pPswcas** | **String**| CAS numbers for surface water discharges. May contain multiple comma-separated values. | [optional] |
| **pPswparam** | **String**| Parameter codes for surface water discharges. May contain multiple comma-separated values. | [optional] |
| **pPswvio** | **String**| Used in conjuction with parameters p_pswpol and p_pswparam, indicates whether search should only include pollutants with violations. | [optional] [enum: Y, N] |
| **pWbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] |
| **pRadwbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12 character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Will search against WBD values otained by \\\&quot;reach indexing\\\&quot; NPDES permits against the medium resolution National Hydrography Dataset.  | [optional] |
| **pFrswbd** | **String**| Works exactly the same as the p_wbd parameter.  2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] |
| **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] [enum: ALL, CONTAINS, EXACT, BEGINS] |
| **pPidall** | **String**| Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc). | [optional] [enum: Y, N] |
| **pMonthsLastDmr** | **BigDecimal**| The number of months since the last Discharge Monitoring Report has been submitted. | [optional] |
| **pLastDmrWithin** | **String**| W value returns facilities that have submitted DMRs within the number of months specified by p_months_last_dmr. An N value returns facilities that have not submitted a DMR within the specified number of months. | [optional] [enum: W, N] |
| **pIndsw** | **String**| Industrial Stormwater Permit Flag.  Enter a Y or N to filter results by this type of permit. | [optional] [enum: Y, N] |
| **pMsgpPtype** | **String**| Multi-Sector General Purpose Permit Type.  Enter a value to filter results by MSGP Permit Type. - NOI &#x3D; Notice of Intent - NOE &#x3D; No Exposure Certification | [optional] [enum: NOI, NOE] |
| **pMonType** | **String**| For use with the Industrial Stormwater search only. Valid values are BENCHGS fro Benchmark (Alert Limit) G2 Ore, BENCH for Benchmark (Alert Limit), and ELG fro Effluent Limitation Guidelines(ELG)(Effluent Limit).   | [optional] [enum: BENCHG2, BENCH, ELG] |
| **pIagency** | **String**| Issuing Agency Limiter.  Enter a single value to filter results by the issuing agency, e.g. \\\&quot;State\\\&quot; or \\\&quot;EPA\\\&quot;. | [optional] |
| **pPermittingAgency** | **String**|  | [optional] |
| **pIsws** | **String**| Multi-Sector General Purpose Permit Subsector Individual Identifier.  Enter a value to filter results. | [optional] |
| **pIswss** | **String**| Multi-Sector General Purpose Permit Subsector Group Code.  Enter a value to filter results. | [optional] |
| **pIswssID** | **String**| Multi-Sector General Purpose Permit Sector Code.  Enter a value to filter results. | [optional] |
| **pDs1** | **String**| Submitted Date Filter Start.  To filter by the date of submission, enter a start date here and an end date in the p_ds2 parameter.  Both dates are required for filtering. | [optional] |
| **pDs2** | **String**| Submitted Date Filter End.  To filter by the date of submission, enter an end date here and a start date in the p_ds1 parameter.  Both dates are required for filtering. | [optional] |
| **pDa1** | **String**| Active Date Filter Start.  To filter by the active date, enter a start date here and an end date in the p_da2 parameter.  Both dates are required for filtering. | [optional] |
| **pDa2** | **String**| Active Date Filter End.  To filter by the active date, enter an end date here and a start date in the p_da1 parameter.  Both dates are required for filtering. | [optional] |
| **pMS4** | **String**| Municipal Separate Storm Water Sewer (MS4) Permit Flag.  Enter a Y or N to filter results by this type of permit. | [optional] [enum: Y, N] |
| **pOoFN** | **String**| Owner/Operator Name. Enter the owner/operator name of the facility. | [optional] |
| **pOoFNtype** | **String**| Owner/Operator Name Multiple Selection Evaluator.   | [optional] [enum: ALL, EXACT, BEGINS, CONTAINS] |
| **pOoSA** | **String**| Owner/Operator Address.  Enter the address of the owner/operator of the facility. | [optional] |
| **pOoSA1** | **String**| Owner/Operator Address Line 2.  Enter the line 2 address of the owner/operator of the facility. | [optional] |
| **pOoCt** | **String**| Owner/Operator City. Enter the city where the owner/operator of the facility is located. | [optional] |
| **pOoSt** | **String**| Owner/Operator State.  Enter the standardized postal state code where the owner/operator of the facility is located. | [optional] |
| **pOoZip** | **String**| Owner/Operator Zip Code.  Enter the postal zip code where the owner/operator of the facility is located. | [optional] |
| **pFacIco** | **String**| FRS tribal land code flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land code. | [optional] [enum: Y, N] |
| **pIcoo** | **String**| Indian country search and/or flag.  Enter \\\&quot;Y\\\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned. | [optional] |
| **pFacIcos** | **String**| FRS tribal land spatial flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land spatial flag. | [optional] |
| **pEjscreen** | **String**| Enter \\\&quot;Y\\\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile. | [optional] |
| **pAlrexceed** | **BigDecimal**| Alert Limits Exceedences Limiter.  Enter a numeric value to restrict results to facilities having the given amount or more of alert limits exceedances. | [optional] |
| **pLimitAddr** | **String**| Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.   | [optional] [enum: Y, N] |
| **pLat** | **BigDecimal**| Latitude location in decimal degrees. | [optional] |
| **pLong** | **BigDecimal**| Longitude location in decimal degrees. | [optional] |
| **pRadius** | **BigDecimal**| Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities. | [optional] |
| **pEjscreenOver80cnt** | **String**| The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11. | [optional] [enum: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] |
| **pBioFlag** | **String**| A Y value will select all biosolid-related permits. | [optional] |
| **pBioFacType** | **String**| The code indicating the reporting obligation reason:  - POT &#x3D; A POTW with a design flow rate equal to or greater than one million gallons per day - CLI &#x3D; A Class I Sludge Management Facility as defined in 40 CFR 503.9 - PPL &#x3D; A POTW that serves 10,000 people or more - OTH &#x3D; Otherwise required to report (e.g., permit condition, enforcement action) - NOA &#x3D; None of the above | [optional] |
| **pBioTrtmntProcs** | **String**| The biosolids or sewage sludge treatment process or processes at the facility:  - AER &#x3D; Aerobic Digestion - AIR &#x3D; Air Drying (or Sludge Drying Beds) - ANA &#x3D; Anaerobic Digestion - COD &#x3D; Beta Ray Irradiation - COM &#x3D; Lower Temperature Composting - DEW &#x3D; Pasteurization - DIS &#x3D; Gamma Ray Irradiation - HEA &#x3D; Heat Drying (e.g., Flash Dryer, Spray Dryer, Rotary Dryer) - HET &#x3D; Heat Treatment (Liquid Sewage Sludge Heated to 356 Deg. F/180 Deg. C or Higher for 30 min.) - HTC &#x3D; Higher Temperature Composting - MET &#x3D; Methane or Biogas Capture and Recovery - OTH &#x3D; Other Treatment Process - PRE &#x3D; Preliminary Operations (e.g., Sludge Grinding, Degritting, Blending) - SLU &#x3D; Sludge Lagoon - STA &#x3D; Lime Stabilization - THE &#x3D; Temporary Sludge Storage (Sewage Sludge Stored on Land 2 Years or Less, Not in Sewage Sludge Unit) - THI &#x3D; Thickening (Gravity and/or Flotation Thickening, Centrifugation, Belt Filter Press, Vacuum Filter) - THM &#x3D; Thermophilic Aerobic Digestion - UND &#x3D; Long-Term Sludge Storage (Sewage Sludge Stored on Land 2 Years or More, not in Sewage Sludge Unit)\\\&quot; | [optional] |
| **pBioAnalyMethodCatgry** | **String**| The unique code for the category of the analytic methods used by the facility to analyze regulated parameters (including enteric viruses, fecal coliforms, helminth ova, and Salmonella sp.) at the facility:  - PAT &#x3D; Pathogens - MET &#x3D; Metals - NIT &#x3D; Nitrogen Compounds - OTH &#x3D; Other Analytes | [optional] |
| **pBioTotalVolumeAmt** | **String**| Total annual amount (in dry metric tons) of biosolids or sewage sludge generated at the facility.  - EQ0 &#x3D; 0 - IN0_1 &#x3D; GT 0 but LT 1 - IN0_289  &#x3D;  GT 0 but LT 290 MT/year - IN290_1499  &#x3D;  GE 290 but LT 1500 MT/year - IN1500_14999  &#x3D;  GE 1500 but LT 15,000 - GE15000  &#x3D;  GE 15,000 | [optional] |
| **pBioMgmtPrctceType** | **String**| The unique code that identifies the type of biosolids or sewage sludge management practice (e.g., land application, surface disposal, incineration) used by the facility. The facility will separately report the management practice for each biosolids or sewage sludge form and pathogen class. This data element will also identify the management practices used by surface disposal site owners/operators (see 40 CFR 503.24):  - BIN &#x3D; Incineration - BLN &#x3D; Land Application - BOT &#x3D; Other Management Practice - BSD &#x3D; Surface Disposal | [optional] |
| **pBioMgmtPrctceStype** | **String**| This is the code indicating additional detail about the type of Management Practice used for a volume of Biosolids or Sewage Sludge:  - ADV &#x3D; Advanced Alkaline Stabilized Biosolids Distribution &amp; Marketing - AGR &#x3D; Agricultural Land Application - COM &#x3D; Distribution and Marketing - Compost - DEE &#x3D; Deep-well Injection Disposal - DIS &#x3D; Disposal in a Municipal Landfill (under 40 CFR 258) - DMO &#x3D; Distribution and Marketing - Other - HEA &#x3D; Heat Dried Biosolids Distribution &amp; Marketing - OTL &#x3D; Other Land Application Management Practice Detail - OTO &#x3D; Other Management Practice Detail - RSA &#x3D; Reclamation Site Application - SEN &#x3D; Sent to Cement Kiln for Use as Alternative Energy - STO &#x3D; Storage - UIC &#x3D; Use in Construction - UPS &#x3D; Used in Production of Syngas - USE &#x3D; Use as Daily Cover for Municipal Landfill (under 40 CFR 258) | [optional] |
| **pBioMgmtPrctceHandler** | **String**| This is the code indicating the type of Biosolids or Sewage Sludge handlers/preparers.  - OWN &#x3D; Owner or Operator - OFF &#x3D; Off-Site Third-Party Handler or Preparer | [optional] |
| **pBioMgmtContainer** | **String**| The code that identifies the nature of each biosolids and sewage sludge material generated by the facility in terms of whether the material is a biosolid or sewage sludge and whether the material is ultimately conveyed off-site in bulk or in bags. The facility separately reports the form for each biosolids or sewage sludge management practice or practices used by the facility and pathogen class:  - BUL &#x3D; Bulk - BAG &#x3D; Bag or Container | [optional] |
| **pBioMgmtPathogen** | **String**| This code identifies the pathogen class [e.g., Class A, Class B, Not Applicable (Incineration)] for biosolids or sewage sludge generated by the facility. The facility will separately report the pathogen class for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form. It also is used to filter applicable Pathogen Reduction and Vector Attraction Reduction Options as well as Land Application Management Practice Deficiencies. Only reqired for some of the mgmt. practice types:  - AAA &#x3D; Class A - AEQ &#x3D; Class A EQ (sale/give away) - BBB &#x3D; Class B - NAP &#x3D; Not Applicable (Incineration) | [optional] |
| **pBioMgmtPathred** | **String**| This is the description of the option used by the facility to control pathogen for a Biosolids Management Practice:  - A1 &#x3D; Class A - Alternative 1: Time/Temperature - A2 &#x3D; Class A - Alternative 2: pH/Temperature/Percent Solids - A3 &#x3D; Class A - Alternative 3: Test Enteric Viruses and Helminth ova; Operating Parameters - A4 &#x3D; Class A - Alternative 4: Test Enteric Viruses and Helminth ova; No New Solids - A51 &#x3D; Class A - Alternative 5: PFRP 1: Composting - A52 &#x3D; Class A - Alternative 5: PFRP 2: Heat Drying - A53 &#x3D; Class A - Alternative 5: PFRP 3: Liquid heat treatment - A54 &#x3D; Class A - Alternative 5: PFRP 4: Thermophilic Aerobic Digestion (ATAD) - A55 &#x3D; Class A - Alternative 5 PFPR 5: Beta Ray Irradiation - A56 &#x3D; Class A - Alternative 5 PFPR 6: Gamma Ray Irradiation - A57 &#x3D; Class A - Alternative 5: PFRP 7: Pasteurization - A6 &#x3D; Class A - Alternative 6: PFRP Equivalency - B1 &#x3D; Class B - Alternative 1: Fecal Coliform Geometric Mean - B21 &#x3D; Class B - Alternative 2 PSRP 1: Aerobic Digestion - B22 &#x3D; Class B - Alternative 2 PSRP 2: Air Drying - B23 &#x3D; Class B - Alternative 2 PSRP 3: Anaerobic Digestion - B24 &#x3D; Class B - Alternative 2 PSRP 4: Composting - B25 &#x3D; Class B - Alternative 2 PSRP 5: Lime Stabilization - B3 &#x3D; Class B - Alternative 3: PSRP Equivalency - PH &#x3D; pH Adjustment (Domestic Septage) | [optional] |
| **pBioMgmtVector** | **String**| The unique code that identifies the option used by the facility for vector attraction reduction. See a listing of these vector attraction reduction options at 40 CFR 503.33(b)(1) through (11). The facility will separately report the vector attraction reduction options for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form as well as by each biosolids or sewage sludge pathogen class:  - VR1 &#x3D; Option 1 - Volatile Solids Reduction - VR2 &#x3D; Option 2 - Bench-Scale Volatile Solids Reduction (Anaerobic Bench Test) - VR3 &#x3D; Option 3 - Bench-Scale Volatile Solids Reduction (Aerobic Bench Test w/ Percent Solids - 2% or Less) - VR4 &#x3D; Option 4 - Specific Oxygen Uptake Rate - VR5 &#x3D; Option 5 - Aerobic Processing (Thermophilic Aerobic Digestion/Composting) - VR6 &#x3D; Option 6 - Alkaline Treatment - VR7 &#x3D; Option 7 - Drying (Equal to or Greater than 75 Percent) - VR8 &#x3D; Option 8 - Drying (Equal to or Greater than 90 Percent) - VR9 &#x3D; Option 9 - Sewage Sludge Injection - V10 &#x3D; Option 10 - Sewage Sludge Timely Incorporation into Land - V11 &#x3D; Option 11 - Sewage Sludge Covered at the End of Each Operating Day | [optional] |
| **pBioMgmtDefCategory** | **String**| This is the code indicating the type of NPDES special regulatory program deficiency:  - INC &#x3D; Biosolids Incineration - LNA &#x3D; Biosolids Land Application - LNB &#x3D; Biosolids Land Application - Pathogen Class B - OTB &#x3D; Biosolids Other Management Practice - SFD &#x3D; Biosolids Surface Disposal | [optional] |
| **pBioMgmtDeficiencies** | **BigDecimal**| The number of times noncompliance was reported by the facility in the last 3 years. The results returned will include facilities whose number of reported noncompliance events is greater than or equal to the number entered. | [optional] |
| **pBioVioCode** | **String**| The Biosolids Single Event Violation Code.  Enter one or mode codes. | [optional] |
| **pBioCurrentVio** | **String**| Indicator of whether the facility is currently in violation for biosolids under the Clean Water Act, in the 12th or 13th quarter:  - Y &#x3D; Yes - N &#x3D; No | [optional] [enum: Y, N] |
| **pBioQtrsInVio** | **BigDecimal**| The number of quarters, in the last three years, where the facility was in violation for a biosolids violation type.  The results returned will include facilities whose number of quarters with violations is greater than or equal to the number entered. | [optional] |
| **pBioRptYear** | **String**| The last year that the permittee submitted an annual Biosolids report.  Valid values are NONE and any year greater or equal to 2016. | [optional] |
| **pBioVioLastYear** | **String**| Identifies if a biosolids violation has occured in the last year.  Valid values are Y and N. | [optional] [enum: Y, N] |
| **pMsgpRptYear** | **String**| The last year that a MSGP report was submitted for the permit.  Valid values are \\\&quot;NONE\\\&quot; and any year Greater or Eqal to 2015. | [optional] |
| **pVioLastYear** | **String**| Identifies if a permit violation has occured in the last year.  Valid values are Y and N. | [optional] [enum: Y, N] |
| **responseset** | **BigDecimal**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |
| **pPrettyPrint** | **BigDecimal**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] |
| **pE90Count** | **BigDecimal**| Number of E90 Exceedances.  Identifies water permits with a number of E90 (Effluient Exceedances) &gt;&#x3D; the value provided for the last number of years provided by the p_e90_years value. | [optional] |
| **pE90Years** | **BigDecimal**| Number of years for the p_e90_count search.  Identified the past number of years to be used for the p_e90_count search. | [optional] |
| **pPsc** | **String**| Point Source Category. | [optional] |

### Return type

[**CwaRestServicesGetFacilityInfoGet200Response**](CwaRestServicesGetFacilityInfoGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results will either be an array of Facilities or an array of Clusters. The search will return clusters if the number of facilities returned is greater than the resposeset size, otherwise individual facility records will be returned. |  -  |

<a id="cwaRestServicesGetGeojsonGet"></a>
# **cwaRestServicesGetGeojsonGet**
> CwaRestServicesGetGeojsonGet200Response cwaRestServicesGetGeojsonGet(qid, output, paramCallback, newsort, descending, qcolumns, pPrettyPrint)

Clean Water Act (CWA) GeoJSON Service

Based on the QID obtained from a get_facilities or get_facility_info query, return GeoJSON of the facilities found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInformationApi apiInstance = new FacilityInformationApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - GEOJSON = Facility results formatted as GeoJSON feature collection (default). - GEOJSONP = Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    BigDecimal newsort = new BigDecimal(78); // BigDecimal | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
    String descending = "Y"; // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      CwaRestServicesGetGeojsonGet200Response result = apiInstance.cwaRestServicesGetGeojsonGet(qid, output, paramCallback, newsort, descending, qcolumns, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInformationApi#cwaRestServicesGetGeojsonGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **qid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - GEOJSON &#x3D; Facility results formatted as GeoJSON feature collection (default). - GEOJSONP &#x3D; Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download. | [optional] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **newsort** | **BigDecimal**| Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column. | [optional] |
| **descending** | **String**| Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated. | [optional] [enum: Y, N] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |
| **pPrettyPrint** | **BigDecimal**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] |

### Return type

[**CwaRestServicesGetGeojsonGet200Response**](CwaRestServicesGetGeojsonGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are formatted as a GeoJSON feature collection. |  -  |

<a id="cwaRestServicesGetGeojsonPost"></a>
# **cwaRestServicesGetGeojsonPost**
> CwaRestServicesGetGeojsonGet200Response cwaRestServicesGetGeojsonPost(qid, output, paramCallback, newsort, descending, qcolumns, pPrettyPrint)

Clean Water Act (CWA) GeoJSON Service

Based on the QID obtained from a get_facilities or get_facility_info query, return GeoJSON of the facilities found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInformationApi apiInstance = new FacilityInformationApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - GEOJSON = Facility results formatted as GeoJSON feature collection (default). - GEOJSONP = Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    BigDecimal newsort = new BigDecimal(78); // BigDecimal | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
    String descending = "Y"; // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      CwaRestServicesGetGeojsonGet200Response result = apiInstance.cwaRestServicesGetGeojsonPost(qid, output, paramCallback, newsort, descending, qcolumns, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInformationApi#cwaRestServicesGetGeojsonPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **qid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - GEOJSON &#x3D; Facility results formatted as GeoJSON feature collection (default). - GEOJSONP &#x3D; Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download. | [optional] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **newsort** | **BigDecimal**| Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column. | [optional] |
| **descending** | **String**| Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated. | [optional] [enum: Y, N] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |
| **pPrettyPrint** | **BigDecimal**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] |

### Return type

[**CwaRestServicesGetGeojsonGet200Response**](CwaRestServicesGetGeojsonGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are formatted as a GeoJSON feature collection. |  -  |

<a id="cwaRestServicesGetInfoClustersGet"></a>
# **cwaRestServicesGetInfoClustersGet**
> File cwaRestServicesGetInfoClustersGet(pQid, output, pPrettyPrint)

Clean Water Act (CWA) Info Clusters Service

Based on the QID obtained from a clustered get_facility_info query, download cluster facility information as either a CSV or GEOJSON file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInformationApi apiInstance = new FacilityInformationApi(defaultClient);
    String pQid = "pQid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default). - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      File result = apiInstance.cwaRestServicesGetInfoClustersGet(pQid, output, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInformationApi#cwaRestServicesGetInfoClustersGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pQid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default). - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download. | [optional] |
| **pPrettyPrint** | **BigDecimal**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are a comma separated value (CSV) file or a file containing a GeoJSON feature collection. |  -  |

<a id="cwaRestServicesGetInfoClustersPost"></a>
# **cwaRestServicesGetInfoClustersPost**
> File cwaRestServicesGetInfoClustersPost(pQid, output, pPrettyPrint)

Clean Water Act (CWA) Info Clusters Service

Based on the QID obtained from a clustered get_facility_info query, download cluster facility information as either a CSV or GEOJSON file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInformationApi apiInstance = new FacilityInformationApi(defaultClient);
    String pQid = "pQid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default). - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      File result = apiInstance.cwaRestServicesGetInfoClustersPost(pQid, output, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInformationApi#cwaRestServicesGetInfoClustersPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pQid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default). - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download. | [optional] |
| **pPrettyPrint** | **BigDecimal**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are a comma separated value (CSV) file or a file containing a GeoJSON feature collection. |  -  |

<a id="cwaRestServicesGetMapGet"></a>
# **cwaRestServicesGetMapGet**
> CwaRestServicesGetMapGet200Response cwaRestServicesGetMapGet(qid, pId, output, paramCallback, tablelist, c1Lat, c1Long, c2Lat, c2Long)

Clean Water Act (CWA) Map Service

The purpose of the GET_MAP service is to display facility coordinates and facility clusters related to a get_facilities facility query. Currently, the maximum number of coordinates returned is 500. GET_MAP performs automatic clustering at the state, county, and zip code levels to maximize the number of coordinates returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInformationApi apiInstance = new FacilityInformationApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String pId = "pId_example"; // String | Nine-character code used to uniquely identify a permitted NPDES facility. The NPDES permit program regulates the direct discharge of pollutants into US waters.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String tablelist = "Y"; // String | Table List Flag. Enter a Y to display the first page of facility results.
    BigDecimal c1Lat = new BigDecimal(78); // BigDecimal | Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal c1Long = new BigDecimal(78); // BigDecimal | Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal c2Lat = new BigDecimal(78); // BigDecimal | Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal c2Long = new BigDecimal(78); // BigDecimal | Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    try {
      CwaRestServicesGetMapGet200Response result = apiInstance.cwaRestServicesGetMapGet(qid, pId, output, paramCallback, tablelist, c1Lat, c1Long, c2Lat, c2Long);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInformationApi#cwaRestServicesGetMapGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **qid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | |
| **pId** | **String**| Nine-character code used to uniquely identify a permitted NPDES facility. The NPDES permit program regulates the direct discharge of pollutants into US waters. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] [enum: Y, N] |
| **c1Lat** | **BigDecimal**| Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **c1Long** | **BigDecimal**| Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **c2Lat** | **BigDecimal**| Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **c2Long** | **BigDecimal**| Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |

### Return type

[**CwaRestServicesGetMapGet200Response**](CwaRestServicesGetMapGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are either an array of State, County, Zip Code facility cluster map coordinates or individual facility coordinates.  Coordinates provided are in WGS84. |  -  |

<a id="cwaRestServicesGetMapPost"></a>
# **cwaRestServicesGetMapPost**
> CwaRestServicesGetMapGet200Response cwaRestServicesGetMapPost(qid, pId, output, paramCallback, tablelist, c1Lat, c1Long, c2Lat, c2Long)

Clean Water Act (CWA) Map Service

The purpose of the GET_MAP service is to display facility coordinates and facility clusters related to a get_facilities facility query. Currently, the maximum number of coordinates returned is 500. GET_MAP performs automatic clustering at the state, county, and zip code levels to maximize the number of coordinates returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInformationApi apiInstance = new FacilityInformationApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String pId = "pId_example"; // String | Nine-character code used to uniquely identify a permitted NPDES facility. The NPDES permit program regulates the direct discharge of pollutants into US waters.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String tablelist = "Y"; // String | Table List Flag. Enter a Y to display the first page of facility results.
    BigDecimal c1Lat = new BigDecimal(78); // BigDecimal | Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal c1Long = new BigDecimal(78); // BigDecimal | Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal c2Lat = new BigDecimal(78); // BigDecimal | Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal c2Long = new BigDecimal(78); // BigDecimal | Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    try {
      CwaRestServicesGetMapGet200Response result = apiInstance.cwaRestServicesGetMapPost(qid, pId, output, paramCallback, tablelist, c1Lat, c1Long, c2Lat, c2Long);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInformationApi#cwaRestServicesGetMapPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **qid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | |
| **pId** | **String**| Nine-character code used to uniquely identify a permitted NPDES facility. The NPDES permit program regulates the direct discharge of pollutants into US waters. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] [enum: Y, N] |
| **c1Lat** | **BigDecimal**| Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **c1Long** | **BigDecimal**| Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **c2Lat** | **BigDecimal**| Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **c2Long** | **BigDecimal**| Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |

### Return type

[**CwaRestServicesGetMapGet200Response**](CwaRestServicesGetMapGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are either an array of State, County, Zip Code facility cluster map coordinates or individual facility coordinates.  Coordinates provided are in WGS84. |  -  |

<a id="cwaRestServicesGetQidGet"></a>
# **cwaRestServicesGetQidGet**
> CwaRestServicesGetQidGet200Response cwaRestServicesGetQidGet(qid, output, pageno, paramCallback, newsort, descending, qcolumns)

Clean Water Act (CWA) Paginated Results Service

GET_QID is passed with a query ID corresponding to a previously run get_facilities query. It then returns a Facility object containing all matching facilities. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInformationApi apiInstance = new FacilityInformationApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    BigDecimal pageno = new BigDecimal("1.0"); // BigDecimal | Indicates the number of the page to display. It is used only when the results are paginated.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    BigDecimal newsort = new BigDecimal(78); // BigDecimal | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
    String descending = "Y"; // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    try {
      CwaRestServicesGetQidGet200Response result = apiInstance.cwaRestServicesGetQidGet(qid, output, pageno, paramCallback, newsort, descending, qcolumns);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInformationApi#cwaRestServicesGetQidGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **qid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **pageno** | **BigDecimal**| Indicates the number of the page to display. It is used only when the results are paginated. | [optional] [default to 1.0] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **newsort** | **BigDecimal**| Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column. | [optional] |
| **descending** | **String**| Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated. | [optional] [enum: Y, N] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |

### Return type

[**CwaRestServicesGetQidGet200Response**](CwaRestServicesGetQidGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are an array (page)  of CWA (ICIS NPDES) Facilities with the number of facilities equal to the responseset (page size). |  -  |

<a id="cwaRestServicesGetQidPost"></a>
# **cwaRestServicesGetQidPost**
> CwaRestServicesGetQidGet200Response cwaRestServicesGetQidPost(qid, output, pageno, paramCallback, newsort, descending, qcolumns)

Clean Water Act (CWA) Paginated Results Service

GET_QID is passed with a query ID corresponding to a previously run get_facilities query. It then returns a Facility object containing all matching facilities. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInformationApi apiInstance = new FacilityInformationApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    BigDecimal pageno = new BigDecimal("1.0"); // BigDecimal | Indicates the number of the page to display. It is used only when the results are paginated.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    BigDecimal newsort = new BigDecimal(78); // BigDecimal | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
    String descending = "Y"; // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    try {
      CwaRestServicesGetQidGet200Response result = apiInstance.cwaRestServicesGetQidPost(qid, output, pageno, paramCallback, newsort, descending, qcolumns);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInformationApi#cwaRestServicesGetQidPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **qid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **pageno** | **BigDecimal**| Indicates the number of the page to display. It is used only when the results are paginated. | [optional] [default to 1.0] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **newsort** | **BigDecimal**| Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column. | [optional] |
| **descending** | **String**| Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated. | [optional] [enum: Y, N] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |

### Return type

[**CwaRestServicesGetQidGet200Response**](CwaRestServicesGetQidGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are an array (page)  of CWA (ICIS NPDES) Facilities with the number of facilities equal to the responseset (page size). |  -  |

