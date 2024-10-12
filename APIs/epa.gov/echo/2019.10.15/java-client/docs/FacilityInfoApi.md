# FacilityInfoApi

All URIs are relative to *https://echodata.epa.gov/echo*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**echoRestServicesGetDownloadGet**](FacilityInfoApi.md#echoRestServicesGetDownloadGet) | **GET** /echo_rest_services.get_download | Combined ECHO Download Data Service |
| [**echoRestServicesGetDownloadPost**](FacilityInfoApi.md#echoRestServicesGetDownloadPost) | **POST** /echo_rest_services.get_download | Combined ECHO Download Data Service |
| [**echoRestServicesGetFacilitiesGet**](FacilityInfoApi.md#echoRestServicesGetFacilitiesGet) | **GET** /echo_rest_services.get_facilities | Combined ECHO Facility Search Service |
| [**echoRestServicesGetFacilitiesPost**](FacilityInfoApi.md#echoRestServicesGetFacilitiesPost) | **POST** /echo_rest_services.get_facilities | Combined ECHO Facility Search Service |
| [**echoRestServicesGetFacilityInfoGet**](FacilityInfoApi.md#echoRestServicesGetFacilityInfoGet) | **GET** /echo_rest_services.get_facility_info | Combined ECHO Facility Enhanced Search Service |
| [**echoRestServicesGetFacilityInfoPost**](FacilityInfoApi.md#echoRestServicesGetFacilityInfoPost) | **POST** /echo_rest_services.get_facility_info | Combined ECHO Facility Enhanced Search Service |
| [**echoRestServicesGetGeojsonGet**](FacilityInfoApi.md#echoRestServicesGetGeojsonGet) | **GET** /echo_rest_services.get_geojson | Combined ECHO GeoJSON Service |
| [**echoRestServicesGetGeojsonPost**](FacilityInfoApi.md#echoRestServicesGetGeojsonPost) | **POST** /echo_rest_services.get_geojson | Combined ECHO GeoJSON Service |
| [**echoRestServicesGetInfoClustersGet**](FacilityInfoApi.md#echoRestServicesGetInfoClustersGet) | **GET** /echo_rest_services.get_info_clusters | Combined ECHO Info Clusters Service |
| [**echoRestServicesGetInfoClustersPost**](FacilityInfoApi.md#echoRestServicesGetInfoClustersPost) | **POST** /echo_rest_services.get_info_clusters | Combined ECHO Info Clusters Service |
| [**echoRestServicesGetMapGet**](FacilityInfoApi.md#echoRestServicesGetMapGet) | **GET** /echo_rest_services.get_map | Combined ECHO Map Service |
| [**echoRestServicesGetMapPost**](FacilityInfoApi.md#echoRestServicesGetMapPost) | **POST** /echo_rest_services.get_map | Combined ECHO Map Service |
| [**echoRestServicesGetQidGet**](FacilityInfoApi.md#echoRestServicesGetQidGet) | **GET** /echo_rest_services.get_qid | Combined ECHO Paginated Results Service |
| [**echoRestServicesGetQidPost**](FacilityInfoApi.md#echoRestServicesGetQidPost) | **POST** /echo_rest_services.get_qid | Combined ECHO Paginated Results Service |


<a id="echoRestServicesGetDownloadGet"></a>
# **echoRestServicesGetDownloadGet**
> File echoRestServicesGetDownloadGet(qid, output, qcolumns, pPrettyPrint)

Combined ECHO Download Data Service

Based on the QID obtained from a get_facilities or get_facility_info query, return a comma separated value (CSV) file of the facilities found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInfoApi apiInstance = new FacilityInfoApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default). - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      File result = apiInstance.echoRestServicesGetDownloadGet(qid, output, qcolumns, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInfoApi#echoRestServicesGetDownloadGet");
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
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default). - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download. | [optional] |
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

<a id="echoRestServicesGetDownloadPost"></a>
# **echoRestServicesGetDownloadPost**
> File echoRestServicesGetDownloadPost(qid, output, qcolumns, pPrettyPrint)

Combined ECHO Download Data Service

Based on the QID obtained from a get_facilities or get_facility_info query, return a comma separated value (CSV) file of the facilities found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInfoApi apiInstance = new FacilityInfoApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default). - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      File result = apiInstance.echoRestServicesGetDownloadPost(qid, output, qcolumns, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInfoApi#echoRestServicesGetDownloadPost");
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
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default). - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download. | [optional] |
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

<a id="echoRestServicesGetFacilitiesGet"></a>
# **echoRestServicesGetFacilitiesGet**
> EchoRestServicesGetFacilitiesGet200Response echoRestServicesGetFacilitiesGet(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pFrs, pReg, pSic, pNcs, pPen, pC1lat, pC1lon, pC2lat, pC2lon, pUsmex, pSic2, pSic4, pFa, pFf, pAct, pMaj, pMact, pFea, pFeay, pFeaa, pFeac, pFea5yr, pIea, pIeay, pIeaa, pIea5yr, pCs, pQiv, pNaa, pImpw, pTrep, pOcr, pOct, pPm, pPd, pIco, pHuc, pPid, pMed, pIstatute, pYsl, pYsly, pYsla, pQs, pSfs, pTribeid, pTribename, pTribedist, pWbd, pFntype, pIcoo, pFacIcos, pEjscreen, pLimitAddr, pLat, pLong, pRadius, pEjscreenOver80cnt, pAgoo, pNeiu, queryset, responseset, tablelist, maplist, summarylist, paramCallback, qcolumns)

Combined ECHO Facility Search Service

Validates query search parameters and returns query identifier.  Use the responseset parameter to set the page size

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInfoApi apiInstance = new FacilityInfoApi(defaultClient);
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
    String pAct = "Y"; // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
    String pMaj = "Y"; // String | Major Facility Flag.  Enter Y to restrict results to Major facilities only.
    String pMact = "pMact_example"; // String | CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility.
    String pFea = "W"; // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
    BigDecimal pFeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
    String pFeaa = "A"; // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
    String pFeac = "pFeac_example"; // String | Formal Enforcment Action Last Case Date Limiter Flag.  Enter a value of \"Y\" to additionally apply the p_feay year filter to the last formal enforcement action case date.  Use the p_fea parameter to control if the filter is within or outside the date span provided.
    String pFea5yr = "pFea5yr_example"; // String | A Y value identifies facilities that have had a formal enforcement action within the last 5 years.
    String pIea = "W"; // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
    BigDecimal pIeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
    String pIeaa = "E"; // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
    String pIea5yr = "pIea5yr_example"; // String | A Y value identifies facilities that have had an informal enforcement action within the last 5 years.
    BigDecimal pCs = new BigDecimal("2"); // BigDecimal | Facility Compliance Limiter.  Enter 2, 3 or 4 to limit facilities returned. - 2 = Facilities in noncompliance. - 3 = Facilities having one or more programs reporting significant noncompliance. - 4 = Facilities having more than one program reporting significant noncompliance.
    String pQiv = "0"; // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    String pNaa = "pNaa_example"; // String | Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas.
    String pImpw = "Y"; // String | Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
    String pTrep = "CURR"; // String | Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR = Current TRI reporter. - NONCURR = Has reported to TRI in the past but not for the current reporting year.
    String pOcr = "pOcr_example"; // String | Toxics Release Inventory Pounds of On-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of chemical releases. - GT0 = More than zero pounds of chemical releases. - GT1000 = More than one thousand pounds of chemical releases. - GT5000 = More than five thousand pounds of chemical releases. - GT10000 = More than ten thousand pounds of chemical releases. - GT20000 = More than twenty thousand pounds of chemical releases. - GT50000 = More than fifty thousand pounds of chemical releases.
    String pOct = "Z"; // String | Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of chemical releases. - GT0 = More than zero pounds of chemical releases. - GT1000 = More than one thousand pounds of chemical releases. - GT5000 = More than five thousand pounds of chemical releases. - GT10000 = More than ten thousand pounds of chemical releases. - GT20000 = More than twenty thousand pounds of chemical releases. - GT50000 = More than fifty thousand pounds of chemical releases.
    String pPm = "NONE"; // String | Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE = 0% - GT5 = greater than 5% - GT10 = greater than 10% - GT25 = greater than 25% - GT50 = greater than 50% - GT75 = greater than 75%
    String pPd = "NONE"; // String | Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE = 0 population density per square mile - GT100 = More than 100 population density per square mile - GT500 = More than 500 population density per square mile - GT1000 = More than 1000 population density per square mile - GT5000 = More than 5000 population density per square mile - GT10000 = More than 10000 population density per square mile - GT20000 = More than 20000 population density per square mile
    String pIco = "Y"; // String | Indian Country Flag.  Enter a \"Y\" or \"N\" to restrict searches to facilities inside or outside Indian Country.
    String pHuc = "pHuc_example"; // String | 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
    String pPid = "pPid_example"; // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    String pMed = "A"; // String | Filter Results by Media.- A = Air- C = CAMD (Clean Air Markets Division)- E = EIS (Emissions Inventory Systems)- G = GHG (Greenhouse Gases)- M = RMP (Risk Management Plan)- R = RCRA (Hazardous Waste)- S = SDWA (Public Drinking Water Systems)- T = TRI (Toxic Release Inventory)- TSCA = TSCA (Toxic Substances Control Act)- W = Water- ALL = Air and Water and RCRA
    String pIstatute = "pIstatute_example"; // String | For use in identifying Facilities that have an inspection performed under the entered Statute.
    String pYsl = "W"; // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
    BigDecimal pYsly = new BigDecimal("1"); // BigDecimal | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
    String pYsla = "E"; // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
    String pQs = "pQs_example"; // String | Quick Search. Allows entry for city, state, and/or zip code.
    String pSfs = "pSfs_example"; // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
    BigDecimal pTribeid = new BigDecimal(78); // BigDecimal | Numeric code for tribe (or list of tribes).
    String pTribename = "pTribename_example"; // String | Tribe Name Filter.  Enter a single tribe name to filter results.
    BigDecimal pTribedist = new BigDecimal(78); // BigDecimal | Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
    String pWbd = "pWbd_example"; // String | 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    String pFntype = "ALL"; // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
    String pIcoo = "pIcoo_example"; // String | Indian country search and/or flag.  Enter \"Y\" to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
    String pFacIcos = "pFacIcos_example"; // String | FRS tribal land spatial flag.  Enter \"Y\" or \"N\" to include or exclude facilities based on FRS tribal land spatial flag.
    String pEjscreen = "pEjscreen_example"; // String | Enter \"Y\" to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
    String pLimitAddr = "Y"; // String | Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
    BigDecimal pLat = new BigDecimal(78); // BigDecimal | Latitude location in decimal degrees.
    BigDecimal pLong = new BigDecimal(78); // BigDecimal | Longitude location in decimal degrees.
    BigDecimal pRadius = new BigDecimal(78); // BigDecimal | Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
    String pEjscreenOver80cnt = "1"; // String | The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
    String pAgoo = "AND"; // String | Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
    String pNeiu = "pNeiu_example"; // String | 
    BigDecimal queryset = new BigDecimal(78); // BigDecimal | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    BigDecimal responseset = new BigDecimal(78); // BigDecimal | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    String tablelist = "Y"; // String | Table List Flag. Enter a Y to display the first page of facility results.
    String maplist = "Y"; // String | Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria).
    String summarylist = "Y"; // String | Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    try {
      EchoRestServicesGetFacilitiesGet200Response result = apiInstance.echoRestServicesGetFacilitiesGet(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pFrs, pReg, pSic, pNcs, pPen, pC1lat, pC1lon, pC2lat, pC2lon, pUsmex, pSic2, pSic4, pFa, pFf, pAct, pMaj, pMact, pFea, pFeay, pFeaa, pFeac, pFea5yr, pIea, pIeay, pIeaa, pIea5yr, pCs, pQiv, pNaa, pImpw, pTrep, pOcr, pOct, pPm, pPd, pIco, pHuc, pPid, pMed, pIstatute, pYsl, pYsly, pYsla, pQs, pSfs, pTribeid, pTribename, pTribedist, pWbd, pFntype, pIcoo, pFacIcos, pEjscreen, pLimitAddr, pLat, pLong, pRadius, pEjscreenOver80cnt, pAgoo, pNeiu, queryset, responseset, tablelist, maplist, summarylist, paramCallback, qcolumns);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInfoApi#echoRestServicesGetFacilitiesGet");
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
| **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits. | [optional] [enum: Y, N, A] |
| **pMaj** | **String**| Major Facility Flag.  Enter Y to restrict results to Major facilities only. | [optional] [enum: Y, N] |
| **pMact** | **String**| CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility. | [optional] |
| **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pFeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] [enum: A, E, S] |
| **pFeac** | **String**| Formal Enforcment Action Last Case Date Limiter Flag.  Enter a value of \&quot;Y\&quot; to additionally apply the p_feay year filter to the last formal enforcement action case date.  Use the p_fea parameter to control if the filter is within or outside the date span provided. | [optional] |
| **pFea5yr** | **String**| A Y value identifies facilities that have had a formal enforcement action within the last 5 years. | [optional] |
| **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pIeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S] |
| **pIea5yr** | **String**| A Y value identifies facilities that have had an informal enforcement action within the last 5 years. | [optional] |
| **pCs** | **BigDecimal**| Facility Compliance Limiter.  Enter 2, 3 or 4 to limit facilities returned. - 2 &#x3D; Facilities in noncompliance. - 3 &#x3D; Facilities having one or more programs reporting significant noncompliance. - 4 &#x3D; Facilities having more than one program reporting significant noncompliance. | [optional] [enum: 2, 3, 4] |
| **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] [enum: 0, GT1, GT2, GT4, GT8, 12] |
| **pNaa** | **String**| Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas. | [optional] |
| **pImpw** | **String**| Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database. | [optional] [enum: Y, N] |
| **pTrep** | **String**| Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year. | [optional] [enum: CURR, NOTCURR] |
| **pOcr** | **String**| Toxics Release Inventory Pounds of On-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases. | [optional] |
| **pOct** | **String**| Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases. | [optional] [enum: Z, GT0, GT1000, GT5000, GT10000, GT20000, GT50000] |
| **pPm** | **String**| Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75% | [optional] [enum: NONE, GT5, GT10, GT25, GT50, GT75] |
| **pPd** | **String**| Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile | [optional] [enum: NONE, GT100, GT500, GT1000, GT5000, GT10000, GT20000] |
| **pIco** | **String**| Indian Country Flag.  Enter a \&quot;Y\&quot; or \&quot;N\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] [enum: Y, N] |
| **pHuc** | **String**| 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values. | [optional] |
| **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] |
| **pMed** | **String**| Filter Results by Media.- A &#x3D; Air- C &#x3D; CAMD (Clean Air Markets Division)- E &#x3D; EIS (Emissions Inventory Systems)- G &#x3D; GHG (Greenhouse Gases)- M &#x3D; RMP (Risk Management Plan)- R &#x3D; RCRA (Hazardous Waste)- S &#x3D; SDWA (Public Drinking Water Systems)- T &#x3D; TRI (Toxic Release Inventory)- TSCA &#x3D; TSCA (Toxic Substances Control Act)- W &#x3D; Water- ALL &#x3D; Air and Water and RCRA | [optional] [enum: A, C, E, G, M, R, S, T, TSCA, W, ALL] |
| **pIstatute** | **String**| For use in identifying Facilities that have an inspection performed under the entered Statute. | [optional] |
| **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N, NV] |
| **pYsly** | **BigDecimal**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S, A] |
| **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] |
| **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] |
| **pTribeid** | **BigDecimal**| Numeric code for tribe (or list of tribes). | [optional] |
| **pTribename** | **String**| Tribe Name Filter.  Enter a single tribe name to filter results. | [optional] |
| **pTribedist** | **BigDecimal**| Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated. | [optional] |
| **pWbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] |
| **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] [enum: ALL, CONTAINS, EXACT, BEGINS] |
| **pIcoo** | **String**| Indian country search and/or flag.  Enter \&quot;Y\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned. | [optional] |
| **pFacIcos** | **String**| FRS tribal land spatial flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land spatial flag. | [optional] |
| **pEjscreen** | **String**| Enter \&quot;Y\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile. | [optional] |
| **pLimitAddr** | **String**| Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.   | [optional] [enum: Y, N] |
| **pLat** | **BigDecimal**| Latitude location in decimal degrees. | [optional] |
| **pLong** | **BigDecimal**| Longitude location in decimal degrees. | [optional] |
| **pRadius** | **BigDecimal**| Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities. | [optional] |
| **pEjscreenOver80cnt** | **String**| The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11. | [optional] [enum: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] |
| **pAgoo** | **String**| Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters. | [optional] [enum: AND, OR] |
| **pNeiu** | **String**|  | [optional] |
| **queryset** | **BigDecimal**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] |
| **responseset** | **BigDecimal**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] |
| **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] [enum: Y, N] |
| **maplist** | **String**| Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria). | [optional] [enum: Y, N] |
| **summarylist** | **String**| Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service. | [optional] [enum: Y, N] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |

### Return type

[**EchoRestServicesGetFacilitiesGet200Response**](EchoRestServicesGetFacilitiesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are summary statistics for the query and a query identifier (QID). |  -  |

<a id="echoRestServicesGetFacilitiesPost"></a>
# **echoRestServicesGetFacilitiesPost**
> EchoRestServicesGetFacilitiesGet200Response echoRestServicesGetFacilitiesPost(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pFrs, pReg, pSic, pNcs, pPen, pC1lat, pC1lon, pC2lat, pC2lon, pUsmex, pSic2, pSic4, pFa, pFf, pAct, pMaj, pMact, pFea, pFeay, pFeaa, pFeac, pFea5yr, pIea, pIeay, pIeaa, pIea5yr, pCs, pQiv, pNaa, pImpw, pTrep, pOcr, pOct, pPm, pPd, pIco, pHuc, pPid, pMed, pIstatute, pYsl, pYsly, pYsla, pQs, pSfs, pTribeid, pTribename, pTribedist, pWbd, pFntype, pIcoo, pFacIcos, pEjscreen, pLimitAddr, pLat, pLong, pRadius, pEjscreenOver80cnt, pAgoo, pNeiu, queryset, responseset, tablelist, maplist, summarylist, paramCallback, qcolumns)

Combined ECHO Facility Search Service

Validates query search parameters and returns query identifier.  Use the responseset parameter to set the page size

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInfoApi apiInstance = new FacilityInfoApi(defaultClient);
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
    String pAct = "Y"; // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
    String pMaj = "Y"; // String | Major Facility Flag.  Enter Y to restrict results to Major facilities only.
    String pMact = "pMact_example"; // String | CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility.
    String pFea = "W"; // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
    BigDecimal pFeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
    String pFeaa = "A"; // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
    String pFeac = "pFeac_example"; // String | Formal Enforcment Action Last Case Date Limiter Flag.  Enter a value of \\\"Y\\\" to additionally apply the p_feay year filter to the last formal enforcement action case date.  Use the p_fea parameter to control if the filter is within or outside the date span provided.
    String pFea5yr = "pFea5yr_example"; // String | A Y value identifies facilities that have had a formal enforcement action within the last 5 years.
    String pIea = "W"; // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
    BigDecimal pIeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
    String pIeaa = "E"; // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
    String pIea5yr = "pIea5yr_example"; // String | A Y value identifies facilities that have had an informal enforcement action within the last 5 years.
    BigDecimal pCs = new BigDecimal("2"); // BigDecimal | Facility Compliance Limiter.  Enter 2, 3 or 4 to limit facilities returned. - 2 = Facilities in noncompliance. - 3 = Facilities having one or more programs reporting significant noncompliance. - 4 = Facilities having more than one program reporting significant noncompliance.
    String pQiv = "0"; // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    String pNaa = "pNaa_example"; // String | Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas.
    String pImpw = "Y"; // String | Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
    String pTrep = "CURR"; // String | Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR = Current TRI reporter. - NONCURR = Has reported to TRI in the past but not for the current reporting year.
    String pOcr = "pOcr_example"; // String | Toxics Release Inventory Pounds of On-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of chemical releases. - GT0 = More than zero pounds of chemical releases. - GT1000 = More than one thousand pounds of chemical releases. - GT5000 = More than five thousand pounds of chemical releases. - GT10000 = More than ten thousand pounds of chemical releases. - GT20000 = More than twenty thousand pounds of chemical releases. - GT50000 = More than fifty thousand pounds of chemical releases.
    String pOct = "Z"; // String | Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of chemical releases. - GT0 = More than zero pounds of chemical releases. - GT1000 = More than one thousand pounds of chemical releases. - GT5000 = More than five thousand pounds of chemical releases. - GT10000 = More than ten thousand pounds of chemical releases. - GT20000 = More than twenty thousand pounds of chemical releases. - GT50000 = More than fifty thousand pounds of chemical releases.
    String pPm = "NONE"; // String | Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE = 0% - GT5 = greater than 5% - GT10 = greater than 10% - GT25 = greater than 25% - GT50 = greater than 50% - GT75 = greater than 75%
    String pPd = "NONE"; // String | Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE = 0 population density per square mile - GT100 = More than 100 population density per square mile - GT500 = More than 500 population density per square mile - GT1000 = More than 1000 population density per square mile - GT5000 = More than 5000 population density per square mile - GT10000 = More than 10000 population density per square mile - GT20000 = More than 20000 population density per square mile
    String pIco = "Y"; // String | Indian Country Flag.  Enter a \\\"Y\\\" or \\\"N\\\" to restrict searches to facilities inside or outside Indian Country.
    String pHuc = "pHuc_example"; // String | 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
    String pPid = "pPid_example"; // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    String pMed = "A"; // String | Filter Results by Media.- A = Air- C = CAMD (Clean Air Markets Division)- E = EIS (Emissions Inventory Systems)- G = GHG (Greenhouse Gases)- M = RMP (Risk Management Plan)- R = RCRA (Hazardous Waste)- S = SDWA (Public Drinking Water Systems)- T = TRI (Toxic Release Inventory)- TSCA = TSCA (Toxic Substances Control Act)- W = Water- ALL = Air and Water and RCRA
    String pIstatute = "pIstatute_example"; // String | For use in identifying Facilities that have an inspection performed under the entered Statute.
    String pYsl = "W"; // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
    BigDecimal pYsly = new BigDecimal("1"); // BigDecimal | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
    String pYsla = "E"; // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
    String pQs = "pQs_example"; // String | Quick Search. Allows entry for city, state, and/or zip code.
    String pSfs = "pSfs_example"; // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
    BigDecimal pTribeid = new BigDecimal(78); // BigDecimal | Numeric code for tribe (or list of tribes).
    String pTribename = "pTribename_example"; // String | Tribe Name Filter.  Enter a single tribe name to filter results.
    BigDecimal pTribedist = new BigDecimal(78); // BigDecimal | Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
    String pWbd = "pWbd_example"; // String | 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    String pFntype = "ALL"; // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
    String pIcoo = "pIcoo_example"; // String | Indian country search and/or flag.  Enter \\\"Y\\\" to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
    String pFacIcos = "pFacIcos_example"; // String | FRS tribal land spatial flag.  Enter \\\"Y\\\" or \\\"N\\\" to include or exclude facilities based on FRS tribal land spatial flag.
    String pEjscreen = "pEjscreen_example"; // String | Enter \\\"Y\\\" to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
    String pLimitAddr = "Y"; // String | Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
    BigDecimal pLat = new BigDecimal(78); // BigDecimal | Latitude location in decimal degrees.
    BigDecimal pLong = new BigDecimal(78); // BigDecimal | Longitude location in decimal degrees.
    BigDecimal pRadius = new BigDecimal(78); // BigDecimal | Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
    String pEjscreenOver80cnt = "1"; // String | The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
    String pAgoo = "AND"; // String | Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
    String pNeiu = "pNeiu_example"; // String | 
    BigDecimal queryset = new BigDecimal(78); // BigDecimal | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    BigDecimal responseset = new BigDecimal(78); // BigDecimal | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    String tablelist = "Y"; // String | Table List Flag. Enter a Y to display the first page of facility results.
    String maplist = "Y"; // String | Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria).
    String summarylist = "Y"; // String | Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    try {
      EchoRestServicesGetFacilitiesGet200Response result = apiInstance.echoRestServicesGetFacilitiesPost(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pFrs, pReg, pSic, pNcs, pPen, pC1lat, pC1lon, pC2lat, pC2lon, pUsmex, pSic2, pSic4, pFa, pFf, pAct, pMaj, pMact, pFea, pFeay, pFeaa, pFeac, pFea5yr, pIea, pIeay, pIeaa, pIea5yr, pCs, pQiv, pNaa, pImpw, pTrep, pOcr, pOct, pPm, pPd, pIco, pHuc, pPid, pMed, pIstatute, pYsl, pYsly, pYsla, pQs, pSfs, pTribeid, pTribename, pTribedist, pWbd, pFntype, pIcoo, pFacIcos, pEjscreen, pLimitAddr, pLat, pLong, pRadius, pEjscreenOver80cnt, pAgoo, pNeiu, queryset, responseset, tablelist, maplist, summarylist, paramCallback, qcolumns);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInfoApi#echoRestServicesGetFacilitiesPost");
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
| **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits. | [optional] [enum: Y, N, A] |
| **pMaj** | **String**| Major Facility Flag.  Enter Y to restrict results to Major facilities only. | [optional] [enum: Y, N] |
| **pMact** | **String**| CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility. | [optional] |
| **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pFeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] [enum: A, E, S] |
| **pFeac** | **String**| Formal Enforcment Action Last Case Date Limiter Flag.  Enter a value of \\\&quot;Y\\\&quot; to additionally apply the p_feay year filter to the last formal enforcement action case date.  Use the p_fea parameter to control if the filter is within or outside the date span provided. | [optional] |
| **pFea5yr** | **String**| A Y value identifies facilities that have had a formal enforcement action within the last 5 years. | [optional] |
| **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pIeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S] |
| **pIea5yr** | **String**| A Y value identifies facilities that have had an informal enforcement action within the last 5 years. | [optional] |
| **pCs** | **BigDecimal**| Facility Compliance Limiter.  Enter 2, 3 or 4 to limit facilities returned. - 2 &#x3D; Facilities in noncompliance. - 3 &#x3D; Facilities having one or more programs reporting significant noncompliance. - 4 &#x3D; Facilities having more than one program reporting significant noncompliance. | [optional] [enum: 2, 3, 4] |
| **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] [enum: 0, GT1, GT2, GT4, GT8, 12] |
| **pNaa** | **String**| Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas. | [optional] |
| **pImpw** | **String**| Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database. | [optional] [enum: Y, N] |
| **pTrep** | **String**| Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year. | [optional] [enum: CURR, NOTCURR] |
| **pOcr** | **String**| Toxics Release Inventory Pounds of On-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases. | [optional] |
| **pOct** | **String**| Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases. | [optional] [enum: Z, GT0, GT1000, GT5000, GT10000, GT20000, GT50000] |
| **pPm** | **String**| Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75% | [optional] [enum: NONE, GT5, GT10, GT25, GT50, GT75] |
| **pPd** | **String**| Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile | [optional] [enum: NONE, GT100, GT500, GT1000, GT5000, GT10000, GT20000] |
| **pIco** | **String**| Indian Country Flag.  Enter a \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] [enum: Y, N] |
| **pHuc** | **String**| 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values. | [optional] |
| **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] |
| **pMed** | **String**| Filter Results by Media.- A &#x3D; Air- C &#x3D; CAMD (Clean Air Markets Division)- E &#x3D; EIS (Emissions Inventory Systems)- G &#x3D; GHG (Greenhouse Gases)- M &#x3D; RMP (Risk Management Plan)- R &#x3D; RCRA (Hazardous Waste)- S &#x3D; SDWA (Public Drinking Water Systems)- T &#x3D; TRI (Toxic Release Inventory)- TSCA &#x3D; TSCA (Toxic Substances Control Act)- W &#x3D; Water- ALL &#x3D; Air and Water and RCRA | [optional] [enum: A, C, E, G, M, R, S, T, TSCA, W, ALL] |
| **pIstatute** | **String**| For use in identifying Facilities that have an inspection performed under the entered Statute. | [optional] |
| **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N, NV] |
| **pYsly** | **BigDecimal**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S, A] |
| **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] |
| **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] |
| **pTribeid** | **BigDecimal**| Numeric code for tribe (or list of tribes). | [optional] |
| **pTribename** | **String**| Tribe Name Filter.  Enter a single tribe name to filter results. | [optional] |
| **pTribedist** | **BigDecimal**| Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated. | [optional] |
| **pWbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] |
| **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] [enum: ALL, CONTAINS, EXACT, BEGINS] |
| **pIcoo** | **String**| Indian country search and/or flag.  Enter \\\&quot;Y\\\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned. | [optional] |
| **pFacIcos** | **String**| FRS tribal land spatial flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land spatial flag. | [optional] |
| **pEjscreen** | **String**| Enter \\\&quot;Y\\\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile. | [optional] |
| **pLimitAddr** | **String**| Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.   | [optional] [enum: Y, N] |
| **pLat** | **BigDecimal**| Latitude location in decimal degrees. | [optional] |
| **pLong** | **BigDecimal**| Longitude location in decimal degrees. | [optional] |
| **pRadius** | **BigDecimal**| Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities. | [optional] |
| **pEjscreenOver80cnt** | **String**| The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11. | [optional] [enum: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] |
| **pAgoo** | **String**| Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters. | [optional] [enum: AND, OR] |
| **pNeiu** | **String**|  | [optional] |
| **queryset** | **BigDecimal**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] |
| **responseset** | **BigDecimal**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] |
| **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] [enum: Y, N] |
| **maplist** | **String**| Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria). | [optional] [enum: Y, N] |
| **summarylist** | **String**| Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service. | [optional] [enum: Y, N] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |

### Return type

[**EchoRestServicesGetFacilitiesGet200Response**](EchoRestServicesGetFacilitiesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are summary statistics for the query and a query identifier (QID). |  -  |

<a id="echoRestServicesGetFacilityInfoGet"></a>
# **echoRestServicesGetFacilityInfoGet**
> EchoRestServicesGetFacilityInfoGet200Response echoRestServicesGetFacilityInfoGet(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pFrs, pReg, pSic, pNcs, pPen, xmin, ymin, xmax, ymax, pUsmex, pSic2, pSic4, pFa, pFf, pAct, pMaj, pMact, pFea, pFeay, pFeaa, pFeac, pFeac5yr, pIea, pIeay, pIeaa, pIea5yr, pCs, pQiv, pNaa, pImpw, pTrep, pOcr, pOct, pPm, pPd, pIco, pHuc, pPid, pMed, pIstatute, pYsl, pYsly, pYsla, pQs, pSfs, pTribeid, pTribename, pTribedist, pWbd, pFntype, pIcoo, pFacIcos, pEjscreen, pLimitAddr, pLat, pLong, pRadius, pEjscreenOver80cnt, pAgoo, pNeiu, responseset, paramCallback, qcolumns, pPrettyPrint)

Combined ECHO Facility Enhanced Search Service

Returns either an array of Facilities or an array of Clusters that meet the specified search criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInfoApi apiInstance = new FacilityInfoApi(defaultClient);
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
    String pAct = "Y"; // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
    String pMaj = "Y"; // String | Major Facility Flag.  Enter Y to restrict results to Major facilities only.
    String pMact = "pMact_example"; // String | CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility.
    String pFea = "W"; // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
    BigDecimal pFeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
    String pFeaa = "A"; // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
    String pFeac = "pFeac_example"; // String | Formal Enforcment Action Last Case Date Limiter Flag.  Enter a value of \"Y\" to additionally apply the p_feay year filter to the last formal enforcement action case date.  Use the p_fea parameter to control if the filter is within or outside the date span provided.
    String pFeac5yr = "pFeac5yr_example"; // String | 
    String pIea = "W"; // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
    BigDecimal pIeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
    String pIeaa = "E"; // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
    String pIea5yr = "pIea5yr_example"; // String | A Y value identifies facilities that have had an informal enforcement action within the last 5 years.
    BigDecimal pCs = new BigDecimal("2"); // BigDecimal | Facility Compliance Limiter.  Enter 2, 3 or 4 to limit facilities returned. - 2 = Facilities in noncompliance. - 3 = Facilities having one or more programs reporting significant noncompliance. - 4 = Facilities having more than one program reporting significant noncompliance.
    String pQiv = "0"; // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    String pNaa = "pNaa_example"; // String | Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas.
    String pImpw = "Y"; // String | Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
    String pTrep = "CURR"; // String | Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR = Current TRI reporter. - NONCURR = Has reported to TRI in the past but not for the current reporting year.
    String pOcr = "pOcr_example"; // String | Toxics Release Inventory Pounds of On-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of chemical releases. - GT0 = More than zero pounds of chemical releases. - GT1000 = More than one thousand pounds of chemical releases. - GT5000 = More than five thousand pounds of chemical releases. - GT10000 = More than ten thousand pounds of chemical releases. - GT20000 = More than twenty thousand pounds of chemical releases. - GT50000 = More than fifty thousand pounds of chemical releases.
    String pOct = "Z"; // String | Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of chemical releases. - GT0 = More than zero pounds of chemical releases. - GT1000 = More than one thousand pounds of chemical releases. - GT5000 = More than five thousand pounds of chemical releases. - GT10000 = More than ten thousand pounds of chemical releases. - GT20000 = More than twenty thousand pounds of chemical releases. - GT50000 = More than fifty thousand pounds of chemical releases.
    String pPm = "NONE"; // String | Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE = 0% - GT5 = greater than 5% - GT10 = greater than 10% - GT25 = greater than 25% - GT50 = greater than 50% - GT75 = greater than 75%
    String pPd = "NONE"; // String | Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE = 0 population density per square mile - GT100 = More than 100 population density per square mile - GT500 = More than 500 population density per square mile - GT1000 = More than 1000 population density per square mile - GT5000 = More than 5000 population density per square mile - GT10000 = More than 10000 population density per square mile - GT20000 = More than 20000 population density per square mile
    String pIco = "Y"; // String | Indian Country Flag.  Enter a \"Y\" or \"N\" to restrict searches to facilities inside or outside Indian Country.
    String pHuc = "pHuc_example"; // String | 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
    String pPid = "pPid_example"; // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    String pMed = "A"; // String | Filter Results by Media.- A = Air- C = CAMD (Clean Air Markets Division)- E = EIS (Emissions Inventory Systems)- G = GHG (Greenhouse Gases)- M = RMP (Risk Management Plan)- R = RCRA (Hazardous Waste)- S = SDWA (Public Drinking Water Systems)- T = TRI (Toxic Release Inventory)- TSCA = TSCA (Toxic Substances Control Act)- W = Water- ALL = Air and Water and RCRA
    String pIstatute = "pIstatute_example"; // String | For use in identifying Facilities that have an inspection performed under the entered Statute.
    String pYsl = "W"; // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
    BigDecimal pYsly = new BigDecimal("1"); // BigDecimal | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
    String pYsla = "E"; // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
    String pQs = "pQs_example"; // String | Quick Search. Allows entry for city, state, and/or zip code.
    String pSfs = "pSfs_example"; // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
    BigDecimal pTribeid = new BigDecimal(78); // BigDecimal | Numeric code for tribe (or list of tribes).
    String pTribename = "pTribename_example"; // String | Tribe Name Filter.  Enter a single tribe name to filter results.
    BigDecimal pTribedist = new BigDecimal(78); // BigDecimal | Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
    String pWbd = "pWbd_example"; // String | 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    String pFntype = "ALL"; // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
    String pIcoo = "pIcoo_example"; // String | Indian country search and/or flag.  Enter \"Y\" to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
    String pFacIcos = "pFacIcos_example"; // String | FRS tribal land spatial flag.  Enter \"Y\" or \"N\" to include or exclude facilities based on FRS tribal land spatial flag.
    String pEjscreen = "pEjscreen_example"; // String | Enter \"Y\" to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
    String pLimitAddr = "Y"; // String | Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
    BigDecimal pLat = new BigDecimal(78); // BigDecimal | Latitude location in decimal degrees.
    BigDecimal pLong = new BigDecimal(78); // BigDecimal | Longitude location in decimal degrees.
    BigDecimal pRadius = new BigDecimal(78); // BigDecimal | Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
    String pEjscreenOver80cnt = "1"; // String | The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
    String pAgoo = "AND"; // String | Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
    String pNeiu = "pNeiu_example"; // String | 
    BigDecimal responseset = new BigDecimal(78); // BigDecimal | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      EchoRestServicesGetFacilityInfoGet200Response result = apiInstance.echoRestServicesGetFacilityInfoGet(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pFrs, pReg, pSic, pNcs, pPen, xmin, ymin, xmax, ymax, pUsmex, pSic2, pSic4, pFa, pFf, pAct, pMaj, pMact, pFea, pFeay, pFeaa, pFeac, pFeac5yr, pIea, pIeay, pIeaa, pIea5yr, pCs, pQiv, pNaa, pImpw, pTrep, pOcr, pOct, pPm, pPd, pIco, pHuc, pPid, pMed, pIstatute, pYsl, pYsly, pYsla, pQs, pSfs, pTribeid, pTribename, pTribedist, pWbd, pFntype, pIcoo, pFacIcos, pEjscreen, pLimitAddr, pLat, pLong, pRadius, pEjscreenOver80cnt, pAgoo, pNeiu, responseset, paramCallback, qcolumns, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInfoApi#echoRestServicesGetFacilityInfoGet");
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
| **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits. | [optional] [enum: Y, N, A] |
| **pMaj** | **String**| Major Facility Flag.  Enter Y to restrict results to Major facilities only. | [optional] [enum: Y, N] |
| **pMact** | **String**| CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility. | [optional] |
| **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pFeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] [enum: A, E, S] |
| **pFeac** | **String**| Formal Enforcment Action Last Case Date Limiter Flag.  Enter a value of \&quot;Y\&quot; to additionally apply the p_feay year filter to the last formal enforcement action case date.  Use the p_fea parameter to control if the filter is within or outside the date span provided. | [optional] |
| **pFeac5yr** | **String**|  | [optional] |
| **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pIeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S] |
| **pIea5yr** | **String**| A Y value identifies facilities that have had an informal enforcement action within the last 5 years. | [optional] |
| **pCs** | **BigDecimal**| Facility Compliance Limiter.  Enter 2, 3 or 4 to limit facilities returned. - 2 &#x3D; Facilities in noncompliance. - 3 &#x3D; Facilities having one or more programs reporting significant noncompliance. - 4 &#x3D; Facilities having more than one program reporting significant noncompliance. | [optional] [enum: 2, 3, 4] |
| **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] [enum: 0, GT1, GT2, GT4, GT8, 12] |
| **pNaa** | **String**| Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas. | [optional] |
| **pImpw** | **String**| Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database. | [optional] [enum: Y, N] |
| **pTrep** | **String**| Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year. | [optional] [enum: CURR, NOTCURR] |
| **pOcr** | **String**| Toxics Release Inventory Pounds of On-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases. | [optional] |
| **pOct** | **String**| Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases. | [optional] [enum: Z, GT0, GT1000, GT5000, GT10000, GT20000, GT50000] |
| **pPm** | **String**| Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75% | [optional] [enum: NONE, GT5, GT10, GT25, GT50, GT75] |
| **pPd** | **String**| Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile | [optional] [enum: NONE, GT100, GT500, GT1000, GT5000, GT10000, GT20000] |
| **pIco** | **String**| Indian Country Flag.  Enter a \&quot;Y\&quot; or \&quot;N\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] [enum: Y, N] |
| **pHuc** | **String**| 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values. | [optional] |
| **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] |
| **pMed** | **String**| Filter Results by Media.- A &#x3D; Air- C &#x3D; CAMD (Clean Air Markets Division)- E &#x3D; EIS (Emissions Inventory Systems)- G &#x3D; GHG (Greenhouse Gases)- M &#x3D; RMP (Risk Management Plan)- R &#x3D; RCRA (Hazardous Waste)- S &#x3D; SDWA (Public Drinking Water Systems)- T &#x3D; TRI (Toxic Release Inventory)- TSCA &#x3D; TSCA (Toxic Substances Control Act)- W &#x3D; Water- ALL &#x3D; Air and Water and RCRA | [optional] [enum: A, C, E, G, M, R, S, T, TSCA, W, ALL] |
| **pIstatute** | **String**| For use in identifying Facilities that have an inspection performed under the entered Statute. | [optional] |
| **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N, NV] |
| **pYsly** | **BigDecimal**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S, A] |
| **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] |
| **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] |
| **pTribeid** | **BigDecimal**| Numeric code for tribe (or list of tribes). | [optional] |
| **pTribename** | **String**| Tribe Name Filter.  Enter a single tribe name to filter results. | [optional] |
| **pTribedist** | **BigDecimal**| Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated. | [optional] |
| **pWbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] |
| **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] [enum: ALL, CONTAINS, EXACT, BEGINS] |
| **pIcoo** | **String**| Indian country search and/or flag.  Enter \&quot;Y\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned. | [optional] |
| **pFacIcos** | **String**| FRS tribal land spatial flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land spatial flag. | [optional] |
| **pEjscreen** | **String**| Enter \&quot;Y\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile. | [optional] |
| **pLimitAddr** | **String**| Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.   | [optional] [enum: Y, N] |
| **pLat** | **BigDecimal**| Latitude location in decimal degrees. | [optional] |
| **pLong** | **BigDecimal**| Longitude location in decimal degrees. | [optional] |
| **pRadius** | **BigDecimal**| Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities. | [optional] |
| **pEjscreenOver80cnt** | **String**| The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11. | [optional] [enum: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] |
| **pAgoo** | **String**| Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters. | [optional] [enum: AND, OR] |
| **pNeiu** | **String**|  | [optional] |
| **responseset** | **BigDecimal**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |
| **pPrettyPrint** | **BigDecimal**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] |

### Return type

[**EchoRestServicesGetFacilityInfoGet200Response**](EchoRestServicesGetFacilityInfoGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results will either be an array of Facilities or an array of Clusters. The determination as to whether Facilities or Clusters are returned is based on the number of facilities that meet the specified criteria. Generally, if there are more than ~2000 facilities, the search will return clusters; otherwise individual facility records will be returned. |  -  |

<a id="echoRestServicesGetFacilityInfoPost"></a>
# **echoRestServicesGetFacilityInfoPost**
> EchoRestServicesGetFacilityInfoGet200Response echoRestServicesGetFacilityInfoPost(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pFrs, pReg, pSic, pNcs, pPen, xmin, ymin, xmax, ymax, pUsmex, pSic2, pSic4, pFa, pFf, pAct, pMaj, pMact, pFea, pFeay, pFeaa, pFeac, pFeac5yr, pIea, pIeay, pIeaa, pIea5yr, pCs, pQiv, pNaa, pImpw, pTrep, pOcr, pOct, pPm, pPd, pIco, pHuc, pPid, pMed, pIstatute, pYsl, pYsly, pYsla, pQs, pSfs, pTribeid, pTribename, pTribedist, pWbd, pFntype, pIcoo, pFacIcos, pEjscreen, pLimitAddr, pLat, pLong, pRadius, pEjscreenOver80cnt, pAgoo, pNeiu, responseset, paramCallback, qcolumns, pPrettyPrint)

Combined ECHO Facility Enhanced Search Service

Returns either an array of Facilities or an array of Clusters that meet the specified search criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInfoApi apiInstance = new FacilityInfoApi(defaultClient);
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
    String pAct = "Y"; // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
    String pMaj = "Y"; // String | Major Facility Flag.  Enter Y to restrict results to Major facilities only.
    String pMact = "pMact_example"; // String | CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility.
    String pFea = "W"; // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
    BigDecimal pFeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
    String pFeaa = "A"; // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
    String pFeac = "pFeac_example"; // String | Formal Enforcment Action Last Case Date Limiter Flag.  Enter a value of \\\"Y\\\" to additionally apply the p_feay year filter to the last formal enforcement action case date.  Use the p_fea parameter to control if the filter is within or outside the date span provided.
    String pFeac5yr = "pFeac5yr_example"; // String | 
    String pIea = "W"; // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
    BigDecimal pIeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
    String pIeaa = "E"; // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
    String pIea5yr = "pIea5yr_example"; // String | A Y value identifies facilities that have had an informal enforcement action within the last 5 years.
    BigDecimal pCs = new BigDecimal("2"); // BigDecimal | Facility Compliance Limiter.  Enter 2, 3 or 4 to limit facilities returned. - 2 = Facilities in noncompliance. - 3 = Facilities having one or more programs reporting significant noncompliance. - 4 = Facilities having more than one program reporting significant noncompliance.
    String pQiv = "0"; // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    String pNaa = "pNaa_example"; // String | Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas.
    String pImpw = "Y"; // String | Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
    String pTrep = "CURR"; // String | Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR = Current TRI reporter. - NONCURR = Has reported to TRI in the past but not for the current reporting year.
    String pOcr = "pOcr_example"; // String | Toxics Release Inventory Pounds of On-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of chemical releases. - GT0 = More than zero pounds of chemical releases. - GT1000 = More than one thousand pounds of chemical releases. - GT5000 = More than five thousand pounds of chemical releases. - GT10000 = More than ten thousand pounds of chemical releases. - GT20000 = More than twenty thousand pounds of chemical releases. - GT50000 = More than fifty thousand pounds of chemical releases.
    String pOct = "Z"; // String | Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of chemical releases. - GT0 = More than zero pounds of chemical releases. - GT1000 = More than one thousand pounds of chemical releases. - GT5000 = More than five thousand pounds of chemical releases. - GT10000 = More than ten thousand pounds of chemical releases. - GT20000 = More than twenty thousand pounds of chemical releases. - GT50000 = More than fifty thousand pounds of chemical releases.
    String pPm = "NONE"; // String | Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE = 0% - GT5 = greater than 5% - GT10 = greater than 10% - GT25 = greater than 25% - GT50 = greater than 50% - GT75 = greater than 75%
    String pPd = "NONE"; // String | Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE = 0 population density per square mile - GT100 = More than 100 population density per square mile - GT500 = More than 500 population density per square mile - GT1000 = More than 1000 population density per square mile - GT5000 = More than 5000 population density per square mile - GT10000 = More than 10000 population density per square mile - GT20000 = More than 20000 population density per square mile
    String pIco = "Y"; // String | Indian Country Flag.  Enter a \\\"Y\\\" or \\\"N\\\" to restrict searches to facilities inside or outside Indian Country.
    String pHuc = "pHuc_example"; // String | 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
    String pPid = "pPid_example"; // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    String pMed = "A"; // String | Filter Results by Media.- A = Air- C = CAMD (Clean Air Markets Division)- E = EIS (Emissions Inventory Systems)- G = GHG (Greenhouse Gases)- M = RMP (Risk Management Plan)- R = RCRA (Hazardous Waste)- S = SDWA (Public Drinking Water Systems)- T = TRI (Toxic Release Inventory)- TSCA = TSCA (Toxic Substances Control Act)- W = Water- ALL = Air and Water and RCRA
    String pIstatute = "pIstatute_example"; // String | For use in identifying Facilities that have an inspection performed under the entered Statute.
    String pYsl = "W"; // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
    BigDecimal pYsly = new BigDecimal("1"); // BigDecimal | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
    String pYsla = "E"; // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
    String pQs = "pQs_example"; // String | Quick Search. Allows entry for city, state, and/or zip code.
    String pSfs = "pSfs_example"; // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
    BigDecimal pTribeid = new BigDecimal(78); // BigDecimal | Numeric code for tribe (or list of tribes).
    String pTribename = "pTribename_example"; // String | Tribe Name Filter.  Enter a single tribe name to filter results.
    BigDecimal pTribedist = new BigDecimal(78); // BigDecimal | Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
    String pWbd = "pWbd_example"; // String | 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    String pFntype = "ALL"; // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
    String pIcoo = "pIcoo_example"; // String | Indian country search and/or flag.  Enter \\\"Y\\\" to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
    String pFacIcos = "pFacIcos_example"; // String | FRS tribal land spatial flag.  Enter \\\"Y\\\" or \\\"N\\\" to include or exclude facilities based on FRS tribal land spatial flag.
    String pEjscreen = "pEjscreen_example"; // String | Enter \\\"Y\\\" to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
    String pLimitAddr = "Y"; // String | Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
    BigDecimal pLat = new BigDecimal(78); // BigDecimal | Latitude location in decimal degrees.
    BigDecimal pLong = new BigDecimal(78); // BigDecimal | Longitude location in decimal degrees.
    BigDecimal pRadius = new BigDecimal(78); // BigDecimal | Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
    String pEjscreenOver80cnt = "1"; // String | The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
    String pAgoo = "AND"; // String | Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
    String pNeiu = "pNeiu_example"; // String | 
    BigDecimal responseset = new BigDecimal(78); // BigDecimal | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      EchoRestServicesGetFacilityInfoGet200Response result = apiInstance.echoRestServicesGetFacilityInfoPost(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pFrs, pReg, pSic, pNcs, pPen, xmin, ymin, xmax, ymax, pUsmex, pSic2, pSic4, pFa, pFf, pAct, pMaj, pMact, pFea, pFeay, pFeaa, pFeac, pFeac5yr, pIea, pIeay, pIeaa, pIea5yr, pCs, pQiv, pNaa, pImpw, pTrep, pOcr, pOct, pPm, pPd, pIco, pHuc, pPid, pMed, pIstatute, pYsl, pYsly, pYsla, pQs, pSfs, pTribeid, pTribename, pTribedist, pWbd, pFntype, pIcoo, pFacIcos, pEjscreen, pLimitAddr, pLat, pLong, pRadius, pEjscreenOver80cnt, pAgoo, pNeiu, responseset, paramCallback, qcolumns, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInfoApi#echoRestServicesGetFacilityInfoPost");
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
| **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits. | [optional] [enum: Y, N, A] |
| **pMaj** | **String**| Major Facility Flag.  Enter Y to restrict results to Major facilities only. | [optional] [enum: Y, N] |
| **pMact** | **String**| CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility. | [optional] |
| **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pFeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] [enum: A, E, S] |
| **pFeac** | **String**| Formal Enforcment Action Last Case Date Limiter Flag.  Enter a value of \\\&quot;Y\\\&quot; to additionally apply the p_feay year filter to the last formal enforcement action case date.  Use the p_fea parameter to control if the filter is within or outside the date span provided. | [optional] |
| **pFeac5yr** | **String**|  | [optional] |
| **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pIeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S] |
| **pIea5yr** | **String**| A Y value identifies facilities that have had an informal enforcement action within the last 5 years. | [optional] |
| **pCs** | **BigDecimal**| Facility Compliance Limiter.  Enter 2, 3 or 4 to limit facilities returned. - 2 &#x3D; Facilities in noncompliance. - 3 &#x3D; Facilities having one or more programs reporting significant noncompliance. - 4 &#x3D; Facilities having more than one program reporting significant noncompliance. | [optional] [enum: 2, 3, 4] |
| **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] [enum: 0, GT1, GT2, GT4, GT8, 12] |
| **pNaa** | **String**| Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas. | [optional] |
| **pImpw** | **String**| Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database. | [optional] [enum: Y, N] |
| **pTrep** | **String**| Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year. | [optional] [enum: CURR, NOTCURR] |
| **pOcr** | **String**| Toxics Release Inventory Pounds of On-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases. | [optional] |
| **pOct** | **String**| Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases. | [optional] [enum: Z, GT0, GT1000, GT5000, GT10000, GT20000, GT50000] |
| **pPm** | **String**| Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75% | [optional] [enum: NONE, GT5, GT10, GT25, GT50, GT75] |
| **pPd** | **String**| Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile | [optional] [enum: NONE, GT100, GT500, GT1000, GT5000, GT10000, GT20000] |
| **pIco** | **String**| Indian Country Flag.  Enter a \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] [enum: Y, N] |
| **pHuc** | **String**| 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values. | [optional] |
| **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] |
| **pMed** | **String**| Filter Results by Media.- A &#x3D; Air- C &#x3D; CAMD (Clean Air Markets Division)- E &#x3D; EIS (Emissions Inventory Systems)- G &#x3D; GHG (Greenhouse Gases)- M &#x3D; RMP (Risk Management Plan)- R &#x3D; RCRA (Hazardous Waste)- S &#x3D; SDWA (Public Drinking Water Systems)- T &#x3D; TRI (Toxic Release Inventory)- TSCA &#x3D; TSCA (Toxic Substances Control Act)- W &#x3D; Water- ALL &#x3D; Air and Water and RCRA | [optional] [enum: A, C, E, G, M, R, S, T, TSCA, W, ALL] |
| **pIstatute** | **String**| For use in identifying Facilities that have an inspection performed under the entered Statute. | [optional] |
| **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N, NV] |
| **pYsly** | **BigDecimal**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S, A] |
| **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] |
| **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] |
| **pTribeid** | **BigDecimal**| Numeric code for tribe (or list of tribes). | [optional] |
| **pTribename** | **String**| Tribe Name Filter.  Enter a single tribe name to filter results. | [optional] |
| **pTribedist** | **BigDecimal**| Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated. | [optional] |
| **pWbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] |
| **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] [enum: ALL, CONTAINS, EXACT, BEGINS] |
| **pIcoo** | **String**| Indian country search and/or flag.  Enter \\\&quot;Y\\\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned. | [optional] |
| **pFacIcos** | **String**| FRS tribal land spatial flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land spatial flag. | [optional] |
| **pEjscreen** | **String**| Enter \\\&quot;Y\\\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile. | [optional] |
| **pLimitAddr** | **String**| Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.   | [optional] [enum: Y, N] |
| **pLat** | **BigDecimal**| Latitude location in decimal degrees. | [optional] |
| **pLong** | **BigDecimal**| Longitude location in decimal degrees. | [optional] |
| **pRadius** | **BigDecimal**| Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities. | [optional] |
| **pEjscreenOver80cnt** | **String**| The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11. | [optional] [enum: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] |
| **pAgoo** | **String**| Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters. | [optional] [enum: AND, OR] |
| **pNeiu** | **String**|  | [optional] |
| **responseset** | **BigDecimal**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |
| **pPrettyPrint** | **BigDecimal**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] |

### Return type

[**EchoRestServicesGetFacilityInfoGet200Response**](EchoRestServicesGetFacilityInfoGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results will either be an array of Facilities or an array of Clusters. The determination as to whether Facilities or Clusters are returned is based on the number of facilities that meet the specified criteria. Generally, if there are more than ~2000 facilities, the search will return clusters; otherwise individual facility records will be returned. |  -  |

<a id="echoRestServicesGetGeojsonGet"></a>
# **echoRestServicesGetGeojsonGet**
> EchoRestServicesGetGeojsonGet200Response echoRestServicesGetGeojsonGet(qid, output, paramCallback, newsort, descending, qcolumns, pPrettyPrint)

Combined ECHO GeoJSON Service

Based on the QID obtained from a get_facilities or get_facility_info query, return GeoJSON of the facilities found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInfoApi apiInstance = new FacilityInfoApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - GEOJSON = Facility results formatted as GeoJSON feature collection (default). - GEOJSONP = Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    BigDecimal newsort = new BigDecimal(78); // BigDecimal | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
    String descending = "Y"; // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      EchoRestServicesGetGeojsonGet200Response result = apiInstance.echoRestServicesGetGeojsonGet(qid, output, paramCallback, newsort, descending, qcolumns, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInfoApi#echoRestServicesGetGeojsonGet");
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

[**EchoRestServicesGetGeojsonGet200Response**](EchoRestServicesGetGeojsonGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are formatted as a GeoJSON feature collection. |  -  |

<a id="echoRestServicesGetGeojsonPost"></a>
# **echoRestServicesGetGeojsonPost**
> EchoRestServicesGetGeojsonGet200Response echoRestServicesGetGeojsonPost(qid, output, paramCallback, newsort, descending, qcolumns, pPrettyPrint)

Combined ECHO GeoJSON Service

Based on the QID obtained from a get_facilities or get_facility_info query, return GeoJSON of the facilities found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInfoApi apiInstance = new FacilityInfoApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - GEOJSON = Facility results formatted as GeoJSON feature collection (default). - GEOJSONP = Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    BigDecimal newsort = new BigDecimal(78); // BigDecimal | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
    String descending = "Y"; // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      EchoRestServicesGetGeojsonGet200Response result = apiInstance.echoRestServicesGetGeojsonPost(qid, output, paramCallback, newsort, descending, qcolumns, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInfoApi#echoRestServicesGetGeojsonPost");
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

[**EchoRestServicesGetGeojsonGet200Response**](EchoRestServicesGetGeojsonGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are formatted as a GeoJSON feature collection. |  -  |

<a id="echoRestServicesGetInfoClustersGet"></a>
# **echoRestServicesGetInfoClustersGet**
> File echoRestServicesGetInfoClustersGet(pQid, output, pPrettyPrint)

Combined ECHO Info Clusters Service

Based on the QID obtained from a clustered get_facility_info query, download cluster facility information as either a CSV or GEOJSON file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInfoApi apiInstance = new FacilityInfoApi(defaultClient);
    String pQid = "pQid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default). - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      File result = apiInstance.echoRestServicesGetInfoClustersGet(pQid, output, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInfoApi#echoRestServicesGetInfoClustersGet");
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

<a id="echoRestServicesGetInfoClustersPost"></a>
# **echoRestServicesGetInfoClustersPost**
> File echoRestServicesGetInfoClustersPost(pQid, output, pPrettyPrint)

Combined ECHO Info Clusters Service

Based on the QID obtained from a clustered get_facility_info query, download cluster facility information as either a CSV or GEOJSON file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInfoApi apiInstance = new FacilityInfoApi(defaultClient);
    String pQid = "pQid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default). - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      File result = apiInstance.echoRestServicesGetInfoClustersPost(pQid, output, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInfoApi#echoRestServicesGetInfoClustersPost");
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

<a id="echoRestServicesGetMapGet"></a>
# **echoRestServicesGetMapGet**
> EchoRestServicesGetMapGet200Response echoRestServicesGetMapGet(qid, pId, output, paramCallback, tablelist, c1Lat, c1Long, c2Lat, c2Long)

Combined ECHO Map Service

The purpose of the GET_MAP service is to display facility coordinates and facility clusters related to a get_facilities facility query. Currently, the maximum number of coordinates returned is 500. GET_MAP performs automatic clustering at the state, county, and zip code levels to maximize the number of coordinates returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInfoApi apiInstance = new FacilityInfoApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String pId = "pId_example"; // String | Identifier for the service.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String tablelist = "Y"; // String | Table List Flag. Enter a Y to display the first page of facility results.
    BigDecimal c1Lat = new BigDecimal(78); // BigDecimal | Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal c1Long = new BigDecimal(78); // BigDecimal | Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal c2Lat = new BigDecimal(78); // BigDecimal | Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal c2Long = new BigDecimal(78); // BigDecimal | Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    try {
      EchoRestServicesGetMapGet200Response result = apiInstance.echoRestServicesGetMapGet(qid, pId, output, paramCallback, tablelist, c1Lat, c1Long, c2Lat, c2Long);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInfoApi#echoRestServicesGetMapGet");
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
| **pId** | **String**| Identifier for the service. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] [enum: Y, N] |
| **c1Lat** | **BigDecimal**| Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **c1Long** | **BigDecimal**| Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **c2Lat** | **BigDecimal**| Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **c2Long** | **BigDecimal**| Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |

### Return type

[**EchoRestServicesGetMapGet200Response**](EchoRestServicesGetMapGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are either an array of State, County, Zip Code facility cluster map coordinates or individual facility coordinates.  Coordinates provided are in WGS84. |  -  |

<a id="echoRestServicesGetMapPost"></a>
# **echoRestServicesGetMapPost**
> EchoRestServicesGetMapGet200Response echoRestServicesGetMapPost(qid, pId, output, paramCallback, tablelist, c1Lat, c1Long, c2Lat, c2Long)

Combined ECHO Map Service

The purpose of the GET_MAP service is to display facility coordinates and facility clusters related to a get_facilities facility query. Currently, the maximum number of coordinates returned is 500. GET_MAP performs automatic clustering at the state, county, and zip code levels to maximize the number of coordinates returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInfoApi apiInstance = new FacilityInfoApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String pId = "pId_example"; // String | Identifier for the service.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String tablelist = "Y"; // String | Table List Flag. Enter a Y to display the first page of facility results.
    BigDecimal c1Lat = new BigDecimal(78); // BigDecimal | Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal c1Long = new BigDecimal(78); // BigDecimal | Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal c2Lat = new BigDecimal(78); // BigDecimal | Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal c2Long = new BigDecimal(78); // BigDecimal | Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    try {
      EchoRestServicesGetMapGet200Response result = apiInstance.echoRestServicesGetMapPost(qid, pId, output, paramCallback, tablelist, c1Lat, c1Long, c2Lat, c2Long);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInfoApi#echoRestServicesGetMapPost");
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
| **pId** | **String**| Identifier for the service. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] [enum: Y, N] |
| **c1Lat** | **BigDecimal**| Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **c1Long** | **BigDecimal**| Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **c2Lat** | **BigDecimal**| Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **c2Long** | **BigDecimal**| Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |

### Return type

[**EchoRestServicesGetMapGet200Response**](EchoRestServicesGetMapGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are either an array of State, County, Zip Code facility cluster map coordinates or individual facility coordinates.  Coordinates provided are in WGS84. |  -  |

<a id="echoRestServicesGetQidGet"></a>
# **echoRestServicesGetQidGet**
> EchoRestServicesGetQidGet200Response echoRestServicesGetQidGet(qid, output, pageno, paramCallback, newsort, descending, qcolumns)

Combined ECHO Paginated Results Service

GET_QID is passed with a query ID corresponding to a previously run get_facilities query. It then returns a Facility object containing all matching facilities. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInfoApi apiInstance = new FacilityInfoApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    BigDecimal pageno = new BigDecimal("1.0"); // BigDecimal | Indicates the number of the page to display. It is used only when the results are paginated.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    BigDecimal newsort = new BigDecimal(78); // BigDecimal | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
    String descending = "Y"; // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    try {
      EchoRestServicesGetQidGet200Response result = apiInstance.echoRestServicesGetQidGet(qid, output, pageno, paramCallback, newsort, descending, qcolumns);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInfoApi#echoRestServicesGetQidGet");
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

[**EchoRestServicesGetQidGet200Response**](EchoRestServicesGetQidGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are an array (page) Facility Registry System (FRS)  Facilities with the number of facilities equal to the responseset (page size). |  -  |

<a id="echoRestServicesGetQidPost"></a>
# **echoRestServicesGetQidPost**
> EchoRestServicesGetQidGet200Response echoRestServicesGetQidPost(qid, output, pageno, paramCallback, newsort, descending, qcolumns)

Combined ECHO Paginated Results Service

GET_QID is passed with a query ID corresponding to a previously run get_facilities query. It then returns a Facility object containing all matching facilities. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilityInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilityInfoApi apiInstance = new FacilityInfoApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    BigDecimal pageno = new BigDecimal("1.0"); // BigDecimal | Indicates the number of the page to display. It is used only when the results are paginated.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    BigDecimal newsort = new BigDecimal(78); // BigDecimal | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
    String descending = "Y"; // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    try {
      EchoRestServicesGetQidGet200Response result = apiInstance.echoRestServicesGetQidPost(qid, output, pageno, paramCallback, newsort, descending, qcolumns);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilityInfoApi#echoRestServicesGetQidPost");
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

[**EchoRestServicesGetQidGet200Response**](EchoRestServicesGetQidGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are an array (page) Facility Registry System (FRS)  Facilities with the number of facilities equal to the responseset (page size). |  -  |

