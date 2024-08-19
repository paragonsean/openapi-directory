# FacilitiesApi

All URIs are relative to *https://echodata.epa.gov/echo*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**airRestServicesGetDownloadGet**](FacilitiesApi.md#airRestServicesGetDownloadGet) | **GET** /air_rest_services.get_download | Clean Air Act Download Data Service |
| [**airRestServicesGetDownloadPost**](FacilitiesApi.md#airRestServicesGetDownloadPost) | **POST** /air_rest_services.get_download | Clean Air Act Download Data Service |
| [**airRestServicesGetFacilitiesGet**](FacilitiesApi.md#airRestServicesGetFacilitiesGet) | **GET** /air_rest_services.get_facilities | Clean Air Act Facility Search |
| [**airRestServicesGetFacilitiesPost**](FacilitiesApi.md#airRestServicesGetFacilitiesPost) | **POST** /air_rest_services.get_facilities | Clean Air Act Facility Search |
| [**airRestServicesGetFacilityInfoGet**](FacilitiesApi.md#airRestServicesGetFacilityInfoGet) | **GET** /air_rest_services.get_facility_info | Clean Air Act Facility Enhanced Search |
| [**airRestServicesGetFacilityInfoPost**](FacilitiesApi.md#airRestServicesGetFacilityInfoPost) | **POST** /air_rest_services.get_facility_info | Clean Air Act Facility Enhanced Search |
| [**airRestServicesGetGeojsonGet**](FacilitiesApi.md#airRestServicesGetGeojsonGet) | **GET** /air_rest_services.get_geojson | Clean Air Act GeoJSON Service |
| [**airRestServicesGetGeojsonPost**](FacilitiesApi.md#airRestServicesGetGeojsonPost) | **POST** /air_rest_services.get_geojson | Clean Air Act GeoJSON Service |
| [**airRestServicesGetInfoClustersGet**](FacilitiesApi.md#airRestServicesGetInfoClustersGet) | **GET** /air_rest_services.get_info_clusters | Clean Air Act Info Clusters Service |
| [**airRestServicesGetInfoClustersPost**](FacilitiesApi.md#airRestServicesGetInfoClustersPost) | **POST** /air_rest_services.get_info_clusters | Clean Air Act Info Clusters Service |
| [**airRestServicesGetMapGet**](FacilitiesApi.md#airRestServicesGetMapGet) | **GET** /air_rest_services.get_map | Clean Air Act Map Service |
| [**airRestServicesGetMapPost**](FacilitiesApi.md#airRestServicesGetMapPost) | **POST** /air_rest_services.get_map | Clean Air Act Map Service |
| [**airRestServicesGetQidGet**](FacilitiesApi.md#airRestServicesGetQidGet) | **GET** /air_rest_services.get_qid | Clean Air Act Search by Query ID |
| [**airRestServicesGetQidPost**](FacilitiesApi.md#airRestServicesGetQidPost) | **POST** /air_rest_services.get_qid | Clean Air Act Search by Query ID |


<a id="airRestServicesGetDownloadGet"></a>
# **airRestServicesGetDownloadGet**
> File airRestServicesGetDownloadGet(qid, output, qcolumns, pPrettyPrint)

Clean Air Act Download Data Service

Based on the QID obtained from a get_facilities or get_facility_info query, return a comma sepated vaule (CSV) file of the facilities found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilitiesApi apiInstance = new FacilitiesApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default). - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      File result = apiInstance.airRestServicesGetDownloadGet(qid, output, qcolumns, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilitiesApi#airRestServicesGetDownloadGet");
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

<a id="airRestServicesGetDownloadPost"></a>
# **airRestServicesGetDownloadPost**
> File airRestServicesGetDownloadPost(qid, output, qcolumns, pPrettyPrint)

Clean Air Act Download Data Service

Based on the QID obtained from a get_facilities or get_facility_info query, return a comma sepated vaule (CSV) file of the facilities found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilitiesApi apiInstance = new FacilitiesApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default). - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      File result = apiInstance.airRestServicesGetDownloadPost(qid, output, qcolumns, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilitiesApi#airRestServicesGetDownloadPost");
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

<a id="airRestServicesGetFacilitiesGet"></a>
# **airRestServicesGetFacilitiesGet**
> AirRestServicesGetFacilitiesGet200Response airRestServicesGetFacilitiesGet(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pLcon, pFrs, pReg, pSic, pNcs, pQnc, pPen, pOpst, pC1lat, pC1lon, pC2lat, pC2lon, pUsmex, pSic2, pSic4, pFa, pAct, pMaj, pMact, pNsps, pNspsm, pProg, pFea, pFeay, pFeaa, pIea, pIeay, pIeaa, pQiv, pNaa, pImpw, pTrep, pTriCat, pTriAmt, pTriAnyAmt, pTriPol, pGhgCat, pGhgAmt, pGhgAnyAmt, pGhgYr, pNeiPol, pNeiAmt, pNeiAnyAmt, pNeiYr, pNeiCat, pPm, pPd, pIco, pHuc, pWbd, pPid, pMed, pYsl, pYsly, pYsla, pStsl, pStsly, pStsla, pStres, pSttyp, pQs, pSfs, pTribeid, pTribename, pTribedist, pOwop, pAgoo, pIdt1, pIdt2, pStdt1, pStdt2, pPityp, pCifdi, pPfead1, pPfead2, pPfeat, pPsncq, pPctrack, pSwpa, pDes, pFntype, pHpvmth, pRecvio, pPollvio, pAr, pTriYr, pPidall, pFacIco, pIcoo, pFacIcos, pEjscreen, pLimitAddr, pLat, pLong, pRadius, pDecouple, pEjscreenOver80cnt, queryset, responseset, tablelist, maplist, summarylist, paramCallback, qcolumns)

Clean Air Act Facility Search

Validates query search parameters and returns query identifier.  Use the responseset parameter to set the page size

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilitiesApi apiInstance = new FacilitiesApi(defaultClient);
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String pFn = "pFn_example"; // String | Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
    String pSa = "pSa_example"; // String | Facility street address. Enter a complete or partial street address.
    String pSa1 = "pSa1_example"; // String | Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa.
    String pCt = "pCt_example"; // String | Facility City Filter. Enter a single case-insensitive city name to filter results.
    String pCo = "pCo_example"; // String | Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
    String pFips = "pFips_example"; // String | FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
    String pSt = "pSt_example"; // String | Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
    String pZip = "pZip_example"; // String | 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values.
    String pLcon = "pLcon_example"; // String | Air Program Local Control Region Code Filter.  Enter one or more local control region codes to filter results.  Provide multiple codes as a comma-delimited list.  Codes where they exist are specific by state.
    String pFrs = "pFrs_example"; // String | Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results.
    String pReg = "01"; // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    String pSic = "pSic_example"; // String | Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4.
    String pNcs = "pNcs_example"; // String | North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
    BigDecimal pQnc = new BigDecimal(78); // BigDecimal | Number of quarters in non-compliance limiter.  Enter an integer value between 1 and 4 to limit results.
    String pPen = "pPen_example"; // String | Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER = No Penalties - ANY = Any Penalty - LEXX = Less than or equal to XX months.  Provide a number in place of XX, e.g. \"LE5\" for a facility with a penalty within previous 5 months. - GTXX = Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago.
    String pOpst = "pOpst_example"; // String | Operating status filter.  Enter one or more operating status codes to limit results.   Provide multiple codes as a comma-delimited list.
    BigDecimal pC1lat = new BigDecimal(78); // BigDecimal | In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC1lon = new BigDecimal(78); // BigDecimal | In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC2lat = new BigDecimal(78); // BigDecimal | In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC2lon = new BigDecimal(78); // BigDecimal | In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    String pUsmex = "Y"; // String | US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
    String pSic2 = "pSic2_example"; // String | Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \"22\" to match all SIC codes beginning with 22.  Use the \"%\" character within strings to match any SIC values with the pattern.  For example, \"2%21\" matches 2021, 2121, 2221, etc.
    String pSic4 = "pSic4_example"; // String | Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker.
    String pFa = "pFa_example"; // String | Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values.
    String pAct = "Y"; // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
    String pMaj = "Y"; // String | Major Facility Flag.  Enter Y to restrict results to Major facilities only.
    String pMact = "pMact_example"; // String | CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility.
    String pNsps = "pNsps_example"; // String | Air Programl New Source Performance Standards (NSPS)  Subpart Code Search.  One or more valid Air Program NSPS Program codes cand be passed.  
    String pNspsm = "pNspsm_example"; // String | Air Programl New Source Performance Standards Minors (NSPSM) Subpart Code Search.  One or more valid Air Program NSPSM Subpart codes can be passed.  
    String pProg = "pProg_example"; // String | Air Program Code Filter.  Enter one or more Air program codes to filter results.  Provide multiple values as a comma-delimited list.
    String pFea = "W"; // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
    BigDecimal pFeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
    String pFeaa = "A"; // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
    String pIea = "W"; // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
    BigDecimal pIeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
    String pIeaa = "E"; // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
    String pQiv = "0"; // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    String pNaa = "pNaa_example"; // String | Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas.
    String pImpw = "Y"; // String | Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
    String pTrep = "CURR"; // String | Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR = Current TRI reporter. - NONCURR = Has reported to TRI in the past but not for the current reporting year.
    String pTriCat = "TOTAL"; // String | Toxic Release Inventory Released To Air Chemical Identifier Category Filter.  Enter the chemical identifier category code to limit results. Note when filtering by TRI chemical identifier categories one may not also filter by specific chemical identifiers via p_tri_pol.  You must also specify a release amount using p_tri_amt or p_tri_any_amt. - TOTAL = Total Released to Air - CARC = Total Carcinogens Released to Air - HAP = Total Hazardous Air Pollutants Released to Air
    String pTriAmt = "0"; // String | Toxic Release Inventory Release Amount Filter.  Enter a value in pounds to limit results to facilities releasing this amount or greateer of TRI releases.  Valid values are 0, GT0, GT1000, GT5000, GT10000 and GT50000. Note when filtering by TRI release amounts one may only use either p_tri_amt or p_tri_any_amt.
    BigDecimal pTriAnyAmt = new BigDecimal(78); // BigDecimal | Toxic Release Inventory Release Of Any Kind Above Value Filter.  Enter a value to limit results to facilities releasing this amount or more of TRI releases.  Note when filtering by TRI releases one may only use p_tri_any_amt or p_tri_amt and not both.
    String pTriPol = "pTriPol_example"; // String | Toxic Release Inventory Chemical Identifier Filter.  Enter one or more chemical identifier codes to limit results. Note when filtering by specific TRI chemical identifiers one may not also filter by chemical identifier categories via p_tri_cat.
    String pGhgCat = "ALL"; // String | Green House Gas (GHG) Gas Code Category.  Must be used with either a formatted (p_ghg_amt) or custom (p_ghg_any_amt) release amount.
    String pGhgAmt = "None"; // String | Green House Gas (GHG) CO2 Equivalent Formatted Release Amount.  First 2 characters must contain GT (greater than) followed by a number.
    BigDecimal pGhgAnyAmt = new BigDecimal(78); // BigDecimal | Green House Gas (GHG) C02 Equivalent Custom Amount.  The C02E value reported for the provided category, will be greater or equal to the amount provided.
    String pGhgYr = "pGhgYr_example"; // String | Green House Gas (GHG) Reporting Year. (2010 through 2015)
    String pNeiPol = "pNeiPol_example"; // String | National Emissions Inventory (NEI) Pollutant Identifier.  When a pollutant identifer is entered a corresponding formatted amount or custom amount must be entered.
    String pNeiAmt = "None"; // String | National Emissions Inventory (NEI) Formatted Pollutant Amount.  A formatted value where the 1st two characters must start with GT or LT followed by a number.  Identifies facilities that have a NEI Pollutant Emission  where the supplied value is > or < the pollutant emission amount.  
    BigDecimal pNeiAnyAmt = new BigDecimal(78); // BigDecimal | National Emissions Inventory (NEI) Custom Pollutant Amount.  Only a number can be entered.  Identifies facilities with where the NEI Pollutant Emission Amount is greater than the number entered.
    String pNeiYr = "pNeiYr_example"; // String | National Emissions Inventory (NEI) year:  2014 or 2011
    String pNeiCat = "pNeiCat_example"; // String | National Emissions Inventory (NEI) Pollutant Category.  When a pollutant category is entered, a corresponding formatted pollutant amount or custom amount must be entered.
    String pPm = "NONE"; // String | Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE = 0% - GT5 = greater than 5% - GT10 = greater than 10% - GT25 = greater than 25% - GT50 = greater than 50% - GT75 = greater than 75%
    String pPd = "NONE"; // String | Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE = 0 population density per square mile - GT100 = More than 100 population density per square mile - GT500 = More than 500 population density per square mile - GT1000 = More than 1000 population density per square mile - GT5000 = More than 5000 population density per square mile - GT10000 = More than 10000 population density per square mile - GT20000 = More than 20000 population density per square mile
    String pIco = "Y"; // String | Indian Country Flag.  Enter a \"Y\" or \"N\" to restrict searches to facilities inside or outside Indian Country.
    String pHuc = "pHuc_example"; // String | 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
    String pWbd = "pWbd_example"; // String | 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    String pPid = "pPid_example"; // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    String pMed = "M"; // String | Filter Results by Media. - M = RMP (Risk Management Plan) - R = RCRA (Hazardous Waste) - S = SDWA (Public Drinking Water Systems) - W = Water - ALL = Water and RCRA and SDWA
    String pYsl = "W"; // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
    BigDecimal pYsly = new BigDecimal("1"); // BigDecimal | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
    String pYsla = "E"; // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
    String pStsl = "W"; // String | Last Stack Test [within / not within] Specified Date Range Indicator. - W = within date range - N = not within date range
    BigDecimal pStsly = new BigDecimal("1"); // BigDecimal | Number of years (1 to 5) since date of last stack test. A value of 1 means it has been inspected within the year.
    String pStsla = "A"; // String | Stack Last Test Code Filter.  Enter a value to limit results: - A = All - E = EPA - S = State
    String pStres = "pStres_example"; // String | Air Stack Test Status Description Filter.  Enter one or more test status descriptions to filter results.  Enter multiple values as a comma-delimited list.
    String pSttyp = "pSttyp_example"; // String | Air Conductor Type Code Filter.  Enter one or more conductor type codes to filter results.  Provide multiple values as a comma-delimited list.
    String pQs = "pQs_example"; // String | Quick Search. Allows entry for city, state, and/or zip code.
    String pSfs = "pSfs_example"; // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
    BigDecimal pTribeid = new BigDecimal(78); // BigDecimal | Numeric code for tribe (or list of tribes).
    String pTribename = "pTribename_example"; // String | Tribe Name Filter.  Enter a single tribe name to filter results.
    BigDecimal pTribedist = new BigDecimal(78); // BigDecimal | Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
    String pOwop = "pOwop_example"; // String | Owner/Operator code filter.  Enter one or more codes to limit results. - CNG - COR - CTG - DIS - FDF - MWD - MXO - NON - POF - SDT - STF - TRB
    String pAgoo = "AND"; // String | Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
    String pIdt1 = "pIdt1_example"; // String | Beginning of date range of most recent facility inspection.
    String pIdt2 = "pIdt2_example"; // String | End of date range of most recent facility inspection.
    String pStdt1 = "pStdt1_example"; // String | Beginning of date range of most recent stack test.
    String pStdt2 = "pStdt2_example"; // String | End of date range of most recent stack test.
    String pPityp = "pPityp_example"; // String | Inspection Type: - CAC = Corrective Action Inspection - CAV = Compliance Assistance Visit - CDI = Case Development Inspection - CEI = Inspection Inspection - CSE = Compliance Schedule Evaluation - FCI = Focused Compliance - FRR = Financial Record Review - FSD = Facility Self Disclosure - FUI = Follow-Up Inspection - GME = Groundwater Monitoring Evaluation - NRR = Non-Financial Record Review - OAM = Operation and Maintenance Inspection May contain multiple comma-separated values.
    String pCifdi = "Any"; // String | Compliance issuess found during inspection.
    String pPfead1 = "pPfead1_example"; // String | Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    String pPfead2 = "pPfead2_example"; // String | Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    String pPfeat = "pPfeat_example"; // String | Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
    String pPsncq = "GT1"; // String | Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z = Zero quarters in significant noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in significant noncompliance.
    String pPctrack = "false"; // String | Compliance Tracking Limiter. Provide a keyword to indicate the extent to which data is being entered and effluent exceedances are being identified. - Off - Partial - On
    String pSwpa = "source water"; // String | Source water protection area
    String pDes = "pDes_example"; // String | Universe Designation Limiter.  Enter one or more universe designation codes.  Provide multiple values as a comma-delimited list.  Use code \"TSDF\" to return the full enforcement TSDF universe and \"Operating TSDF\" to return the operating TSDF universe.
    String pFntype = "ALL"; // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
    String pHpvmth = "pHpvmth_example"; // String | Months in high priority violation status out of the previous three years limiter.  Provide a number of months in the past three years.  Results will limited to facilities in high priority violation status during that time. 
    String pRecvio = "pRecvio_example"; // String | Recent Violation Status Filter.  Enter one or more recent violation codes to limit results.  Provide multiple values as a comma-delimited list. - NO VIOL = Selects facilities with no recent violations. - ANY HPV = Selects facilities with either addressed or unaddressed high priority violations. - ADDRS-EPA - Select facilities with recent EPA addressed violations. - ADDRS-LOCAL - Select facilities with recent locally addressed violations. - ADDRS-STATE - Select facilities with recent state addressed violations. - UNADDR-EPA - Select facilities with recent EPA unaddressed violations. - UNADDR-LOCAL - Select facilities with recent locally unaddressed violations. - UNADDR-STATE - Select facilities with recent state unaddressed violations. - FRV VIOL = Selects facilities with a recent federally reportable violation without a high priority violation.
    String pPollvio = "pPollvio_example"; // String | Air Pollutant Code For A Recent Violation Filter.  Provide one or more pollutant codes to select facilities with one or more of the entered pollutant codes for a recent air violation.  Provide multiple values as a comma-delimited list.
    String pAr = "pAr_example"; // String | Associated EPA Air Reports Program Filter.  Enter multiple values as a comma-delimited list.  Valid values are: - TRI = Toxic Release Inventory. - GHG = Green House Gas Reporter. - EIS = Emission Inventory System. - CAMD = Clean Air Markets Program Reporter.
    String pTriYr = "pTriYr_example"; // String | Toxic Release Inventory Reporting Year Filter.  Enter one or more year values to filter results by the TRI reporting year.  Provide multiple years as a comma-delimited list.
    String pPidall = "Y"; // String | Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc).
    String pFacIco = "Y"; // String | FRS tribal land code flag.  Enter \"Y\" or \"N\" to include or exclude facilities based on FRS tribal land code.
    String pIcoo = "pIcoo_example"; // String | Indian country search and/or flag.  Enter \"Y\" to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
    String pFacIcos = "pFacIcos_example"; // String | FRS tribal land spatial flag.  Enter \"Y\" or \"N\" to include or exclude facilities based on FRS tribal land spatial flag.
    String pEjscreen = "pEjscreen_example"; // String | Enter \"Y\" to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
    String pLimitAddr = "Y"; // String | Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
    BigDecimal pLat = new BigDecimal(78); // BigDecimal | Latitude location in decimal degrees.
    BigDecimal pLong = new BigDecimal(78); // BigDecimal | Longitude location in decimal degrees.
    BigDecimal pRadius = new BigDecimal(78); // BigDecimal | Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
    String pDecouple = "Y"; // String | Decouple Inspection Code Search Flag.  Enter \"Y\" to search for inspection code types with p_pityp without respect to the date range search provided with p_ysl* parameters.
    String pEjscreenOver80cnt = "1"; // String | The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
    BigDecimal queryset = new BigDecimal(78); // BigDecimal | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    BigDecimal responseset = new BigDecimal(78); // BigDecimal | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    String tablelist = "Y"; // String | Table List Flag. Enter a Y to display the first page of facility results.
    String maplist = "Y"; // String | Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria).
    String summarylist = "Y"; // String | Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    try {
      AirRestServicesGetFacilitiesGet200Response result = apiInstance.airRestServicesGetFacilitiesGet(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pLcon, pFrs, pReg, pSic, pNcs, pQnc, pPen, pOpst, pC1lat, pC1lon, pC2lat, pC2lon, pUsmex, pSic2, pSic4, pFa, pAct, pMaj, pMact, pNsps, pNspsm, pProg, pFea, pFeay, pFeaa, pIea, pIeay, pIeaa, pQiv, pNaa, pImpw, pTrep, pTriCat, pTriAmt, pTriAnyAmt, pTriPol, pGhgCat, pGhgAmt, pGhgAnyAmt, pGhgYr, pNeiPol, pNeiAmt, pNeiAnyAmt, pNeiYr, pNeiCat, pPm, pPd, pIco, pHuc, pWbd, pPid, pMed, pYsl, pYsly, pYsla, pStsl, pStsly, pStsla, pStres, pSttyp, pQs, pSfs, pTribeid, pTribename, pTribedist, pOwop, pAgoo, pIdt1, pIdt2, pStdt1, pStdt2, pPityp, pCifdi, pPfead1, pPfead2, pPfeat, pPsncq, pPctrack, pSwpa, pDes, pFntype, pHpvmth, pRecvio, pPollvio, pAr, pTriYr, pPidall, pFacIco, pIcoo, pFacIcos, pEjscreen, pLimitAddr, pLat, pLong, pRadius, pDecouple, pEjscreenOver80cnt, queryset, responseset, tablelist, maplist, summarylist, paramCallback, qcolumns);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilitiesApi#airRestServicesGetFacilitiesGet");
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
| **pLcon** | **String**| Air Program Local Control Region Code Filter.  Enter one or more local control region codes to filter results.  Provide multiple codes as a comma-delimited list.  Codes where they exist are specific by state. | [optional] |
| **pFrs** | **String**| Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results. | [optional] |
| **pReg** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] [enum: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10] |
| **pSic** | **String**| Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4. | [optional] |
| **pNcs** | **String**| North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values. | [optional] |
| **pQnc** | **BigDecimal**| Number of quarters in non-compliance limiter.  Enter an integer value between 1 and 4 to limit results. | [optional] |
| **pPen** | **String**| Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER &#x3D; No Penalties - ANY &#x3D; Any Penalty - LEXX &#x3D; Less than or equal to XX months.  Provide a number in place of XX, e.g. \&quot;LE5\&quot; for a facility with a penalty within previous 5 months. - GTXX &#x3D; Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago. | [optional] |
| **pOpst** | **String**| Operating status filter.  Enter one or more operating status codes to limit results.   Provide multiple codes as a comma-delimited list. | [optional] |
| **pC1lat** | **BigDecimal**| In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC1lon** | **BigDecimal**| In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC2lat** | **BigDecimal**| In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC2lon** | **BigDecimal**| In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pUsmex** | **String**| US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border. | [optional] [enum: Y, N] |
| **pSic2** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \&quot;22\&quot; to match all SIC codes beginning with 22.  Use the \&quot;%\&quot; character within strings to match any SIC values with the pattern.  For example, \&quot;2%21\&quot; matches 2021, 2121, 2221, etc. | [optional] |
| **pSic4** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker. | [optional] |
| **pFa** | **String**| Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values. | [optional] |
| **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits. | [optional] [enum: Y, N, A] |
| **pMaj** | **String**| Major Facility Flag.  Enter Y to restrict results to Major facilities only. | [optional] [enum: Y, N] |
| **pMact** | **String**| CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility. | [optional] |
| **pNsps** | **String**| Air Programl New Source Performance Standards (NSPS)  Subpart Code Search.  One or more valid Air Program NSPS Program codes cand be passed.   | [optional] |
| **pNspsm** | **String**| Air Programl New Source Performance Standards Minors (NSPSM) Subpart Code Search.  One or more valid Air Program NSPSM Subpart codes can be passed.   | [optional] |
| **pProg** | **String**| Air Program Code Filter.  Enter one or more Air program codes to filter results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pFeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] [enum: A, E, S] |
| **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pIeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S] |
| **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] [enum: 0, GT1, GT2, GT4, GT8, 12] |
| **pNaa** | **String**| Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas. | [optional] |
| **pImpw** | **String**| Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database. | [optional] [enum: Y, N] |
| **pTrep** | **String**| Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year. | [optional] [enum: CURR, NOTCURR] |
| **pTriCat** | **String**| Toxic Release Inventory Released To Air Chemical Identifier Category Filter.  Enter the chemical identifier category code to limit results. Note when filtering by TRI chemical identifier categories one may not also filter by specific chemical identifiers via p_tri_pol.  You must also specify a release amount using p_tri_amt or p_tri_any_amt. - TOTAL &#x3D; Total Released to Air - CARC &#x3D; Total Carcinogens Released to Air - HAP &#x3D; Total Hazardous Air Pollutants Released to Air | [optional] [enum: TOTAL, CARC, HAP] |
| **pTriAmt** | **String**| Toxic Release Inventory Release Amount Filter.  Enter a value in pounds to limit results to facilities releasing this amount or greateer of TRI releases.  Valid values are 0, GT0, GT1000, GT5000, GT10000 and GT50000. Note when filtering by TRI release amounts one may only use either p_tri_amt or p_tri_any_amt. | [optional] [enum: 0, GT0, GT1000, GT5000, GT10000, GT50000] |
| **pTriAnyAmt** | **BigDecimal**| Toxic Release Inventory Release Of Any Kind Above Value Filter.  Enter a value to limit results to facilities releasing this amount or more of TRI releases.  Note when filtering by TRI releases one may only use p_tri_any_amt or p_tri_amt and not both. | [optional] |
| **pTriPol** | **String**| Toxic Release Inventory Chemical Identifier Filter.  Enter one or more chemical identifier codes to limit results. Note when filtering by specific TRI chemical identifiers one may not also filter by chemical identifier categories via p_tri_cat. | [optional] |
| **pGhgCat** | **String**| Green House Gas (GHG) Gas Code Category.  Must be used with either a formatted (p_ghg_amt) or custom (p_ghg_any_amt) release amount. | [optional] [enum: ALL, BIOCO2, CH4, CO2, HFC, N2O, NF3, OTHER_L, PFC, SF6] |
| **pGhgAmt** | **String**| Green House Gas (GHG) CO2 Equivalent Formatted Release Amount.  First 2 characters must contain GT (greater than) followed by a number. | [optional] [enum: None, 0, GT0, GT10000, GT25000, GT250000, GT1000000] |
| **pGhgAnyAmt** | **BigDecimal**| Green House Gas (GHG) C02 Equivalent Custom Amount.  The C02E value reported for the provided category, will be greater or equal to the amount provided. | [optional] |
| **pGhgYr** | **String**| Green House Gas (GHG) Reporting Year. (2010 through 2015) | [optional] |
| **pNeiPol** | **String**| National Emissions Inventory (NEI) Pollutant Identifier.  When a pollutant identifer is entered a corresponding formatted amount or custom amount must be entered. | [optional] |
| **pNeiAmt** | **String**| National Emissions Inventory (NEI) Formatted Pollutant Amount.  A formatted value where the 1st two characters must start with GT or LT followed by a number.  Identifies facilities that have a NEI Pollutant Emission  where the supplied value is &gt; or &lt; the pollutant emission amount.   | [optional] [enum: None, 0, GT0, GT10000, GT25000, GT250000, GT1000000] |
| **pNeiAnyAmt** | **BigDecimal**| National Emissions Inventory (NEI) Custom Pollutant Amount.  Only a number can be entered.  Identifies facilities with where the NEI Pollutant Emission Amount is greater than the number entered. | [optional] |
| **pNeiYr** | **String**| National Emissions Inventory (NEI) year:  2014 or 2011 | [optional] |
| **pNeiCat** | **String**| National Emissions Inventory (NEI) Pollutant Category.  When a pollutant category is entered, a corresponding formatted pollutant amount or custom amount must be entered. | [optional] |
| **pPm** | **String**| Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75% | [optional] [enum: NONE, GT5, GT10, GT25, GT50, GT75] |
| **pPd** | **String**| Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile | [optional] [enum: NONE, GT100, GT500, GT1000, GT5000, GT10000, GT20000] |
| **pIco** | **String**| Indian Country Flag.  Enter a \&quot;Y\&quot; or \&quot;N\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] [enum: Y, N] |
| **pHuc** | **String**| 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values. | [optional] |
| **pWbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] |
| **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] |
| **pMed** | **String**| Filter Results by Media. - M &#x3D; RMP (Risk Management Plan) - R &#x3D; RCRA (Hazardous Waste) - S &#x3D; SDWA (Public Drinking Water Systems) - W &#x3D; Water - ALL &#x3D; Water and RCRA and SDWA | [optional] [enum: M, R, S, W, ALL] |
| **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N, NV] |
| **pYsly** | **BigDecimal**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S, A] |
| **pStsl** | **String**| Last Stack Test [within / not within] Specified Date Range Indicator. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pStsly** | **BigDecimal**| Number of years (1 to 5) since date of last stack test. A value of 1 means it has been inspected within the year. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pStsla** | **String**| Stack Last Test Code Filter.  Enter a value to limit results: - A &#x3D; All - E &#x3D; EPA - S &#x3D; State | [optional] [enum: A, E, S] |
| **pStres** | **String**| Air Stack Test Status Description Filter.  Enter one or more test status descriptions to filter results.  Enter multiple values as a comma-delimited list. | [optional] |
| **pSttyp** | **String**| Air Conductor Type Code Filter.  Enter one or more conductor type codes to filter results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] |
| **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] |
| **pTribeid** | **BigDecimal**| Numeric code for tribe (or list of tribes). | [optional] |
| **pTribename** | **String**| Tribe Name Filter.  Enter a single tribe name to filter results. | [optional] |
| **pTribedist** | **BigDecimal**| Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated. | [optional] |
| **pOwop** | **String**| Owner/Operator code filter.  Enter one or more codes to limit results. - CNG - COR - CTG - DIS - FDF - MWD - MXO - NON - POF - SDT - STF - TRB | [optional] |
| **pAgoo** | **String**| Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters. | [optional] [enum: AND, OR] |
| **pIdt1** | **String**| Beginning of date range of most recent facility inspection. | [optional] |
| **pIdt2** | **String**| End of date range of most recent facility inspection. | [optional] |
| **pStdt1** | **String**| Beginning of date range of most recent stack test. | [optional] |
| **pStdt2** | **String**| End of date range of most recent stack test. | [optional] |
| **pPityp** | **String**| Inspection Type: - CAC &#x3D; Corrective Action Inspection - CAV &#x3D; Compliance Assistance Visit - CDI &#x3D; Case Development Inspection - CEI &#x3D; Inspection Inspection - CSE &#x3D; Compliance Schedule Evaluation - FCI &#x3D; Focused Compliance - FRR &#x3D; Financial Record Review - FSD &#x3D; Facility Self Disclosure - FUI &#x3D; Follow-Up Inspection - GME &#x3D; Groundwater Monitoring Evaluation - NRR &#x3D; Non-Financial Record Review - OAM &#x3D; Operation and Maintenance Inspection May contain multiple comma-separated values. | [optional] |
| **pCifdi** | **String**| Compliance issuess found during inspection. | [optional] [enum: Any, true, false, Undetermined] |
| **pPfead1** | **String**| Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] |
| **pPfead2** | **String**| Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] |
| **pPfeat** | **String**| Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list. | [optional] |
| **pPsncq** | **String**| Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z &#x3D; Zero quarters in significant noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in significant noncompliance. | [optional] [enum: GT1, GE1, GT2, GE2, GT4, GE4, GT8, GE8, GT12, GE12] |
| **pPctrack** | **String**| Compliance Tracking Limiter. Provide a keyword to indicate the extent to which data is being entered and effluent exceedances are being identified. - Off - Partial - On | [optional] [enum: false, Partial, true] |
| **pSwpa** | **String**| Source water protection area | [optional] [enum: source water, surface water, ground water, waiting for SSO] |
| **pDes** | **String**| Universe Designation Limiter.  Enter one or more universe designation codes.  Provide multiple values as a comma-delimited list.  Use code \&quot;TSDF\&quot; to return the full enforcement TSDF universe and \&quot;Operating TSDF\&quot; to return the operating TSDF universe. | [optional] |
| **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] [enum: ALL, CONTAINS, EXACT, BEGINS] |
| **pHpvmth** | **String**| Months in high priority violation status out of the previous three years limiter.  Provide a number of months in the past three years.  Results will limited to facilities in high priority violation status during that time.  | [optional] |
| **pRecvio** | **String**| Recent Violation Status Filter.  Enter one or more recent violation codes to limit results.  Provide multiple values as a comma-delimited list. - NO VIOL &#x3D; Selects facilities with no recent violations. - ANY HPV &#x3D; Selects facilities with either addressed or unaddressed high priority violations. - ADDRS-EPA - Select facilities with recent EPA addressed violations. - ADDRS-LOCAL - Select facilities with recent locally addressed violations. - ADDRS-STATE - Select facilities with recent state addressed violations. - UNADDR-EPA - Select facilities with recent EPA unaddressed violations. - UNADDR-LOCAL - Select facilities with recent locally unaddressed violations. - UNADDR-STATE - Select facilities with recent state unaddressed violations. - FRV VIOL &#x3D; Selects facilities with a recent federally reportable violation without a high priority violation. | [optional] |
| **pPollvio** | **String**| Air Pollutant Code For A Recent Violation Filter.  Provide one or more pollutant codes to select facilities with one or more of the entered pollutant codes for a recent air violation.  Provide multiple values as a comma-delimited list. | [optional] |
| **pAr** | **String**| Associated EPA Air Reports Program Filter.  Enter multiple values as a comma-delimited list.  Valid values are: - TRI &#x3D; Toxic Release Inventory. - GHG &#x3D; Green House Gas Reporter. - EIS &#x3D; Emission Inventory System. - CAMD &#x3D; Clean Air Markets Program Reporter. | [optional] |
| **pTriYr** | **String**| Toxic Release Inventory Reporting Year Filter.  Enter one or more year values to filter results by the TRI reporting year.  Provide multiple years as a comma-delimited list. | [optional] |
| **pPidall** | **String**| Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc). | [optional] [enum: Y, N] |
| **pFacIco** | **String**| FRS tribal land code flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land code. | [optional] [enum: Y, N] |
| **pIcoo** | **String**| Indian country search and/or flag.  Enter \&quot;Y\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned. | [optional] |
| **pFacIcos** | **String**| FRS tribal land spatial flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land spatial flag. | [optional] |
| **pEjscreen** | **String**| Enter \&quot;Y\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile. | [optional] |
| **pLimitAddr** | **String**| Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.   | [optional] [enum: Y, N] |
| **pLat** | **BigDecimal**| Latitude location in decimal degrees. | [optional] |
| **pLong** | **BigDecimal**| Longitude location in decimal degrees. | [optional] |
| **pRadius** | **BigDecimal**| Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities. | [optional] |
| **pDecouple** | **String**| Decouple Inspection Code Search Flag.  Enter \&quot;Y\&quot; to search for inspection code types with p_pityp without respect to the date range search provided with p_ysl* parameters. | [optional] [enum: Y, N] |
| **pEjscreenOver80cnt** | **String**| The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11. | [optional] [enum: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] |
| **queryset** | **BigDecimal**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] |
| **responseset** | **BigDecimal**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] |
| **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] [enum: Y, N] |
| **maplist** | **String**| Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria). | [optional] [enum: Y, N] |
| **summarylist** | **String**| Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service. | [optional] [enum: Y, N] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |

### Return type

[**AirRestServicesGetFacilitiesGet200Response**](AirRestServicesGetFacilitiesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are summary statistics for the query and a query identifier (QID). |  -  |

<a id="airRestServicesGetFacilitiesPost"></a>
# **airRestServicesGetFacilitiesPost**
> AirRestServicesGetFacilitiesGet200Response airRestServicesGetFacilitiesPost(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pLcon, pFrs, pReg, pSic, pNcs, pQnc, pPen, pOpst, pC1lat, pC1lon, pC2lat, pC2lon, pUsmex, pSic2, pSic4, pFa, pAct, pMaj, pMact, pNsps, pNspsm, pProg, pFea, pFeay, pFeaa, pIea, pIeay, pIeaa, pQiv, pNaa, pImpw, pTrep, pTriCat, pTriAmt, pTriAnyAmt, pTriPol, pGhgCat, pGhgAmt, pGhgAnyAmt, pGhgYr, pNeiPol, pNeiAmt, pNeiAnyAmt, pNeiYr, pNeiCat, pPm, pPd, pIco, pHuc, pWbd, pPid, pMed, pYsl, pYsly, pYsla, pStsl, pStsly, pStsla, pStres, pSttyp, pQs, pSfs, pTribeid, pTribename, pTribedist, pOwop, pAgoo, pIdt1, pIdt2, pStdt1, pStdt2, pPityp, pCifdi, pPfead1, pPfead2, pPfeat, pPsncq, pPctrack, pSwpa, pDes, pFntype, pHpvmth, pRecvio, pPollvio, pAr, pTriYr, pPidall, pFacIco, pIcoo, pFacIcos, pEjscreen, pLimitAddr, pLat, pLong, pRadius, pDecouple, pEjscreenOver80cnt, queryset, responseset, tablelist, maplist, summarylist, paramCallback, qcolumns)

Clean Air Act Facility Search

Validates query search parameters and returns query identifier.  Use the responseset parameter to set the page size

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilitiesApi apiInstance = new FacilitiesApi(defaultClient);
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String pFn = "pFn_example"; // String | Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
    String pSa = "pSa_example"; // String | Facility street address. Enter a complete or partial street address.
    String pSa1 = "pSa1_example"; // String | Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa.
    String pCt = "pCt_example"; // String | Facility City Filter. Enter a single case-insensitive city name to filter results.
    String pCo = "pCo_example"; // String | Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
    String pFips = "pFips_example"; // String | FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
    String pSt = "pSt_example"; // String | Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
    String pZip = "pZip_example"; // String | 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values.
    String pLcon = "pLcon_example"; // String | Air Program Local Control Region Code Filter.  Enter one or more local control region codes to filter results.  Provide multiple codes as a comma-delimited list.  Codes where they exist are specific by state.
    String pFrs = "pFrs_example"; // String | Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results.
    String pReg = "01"; // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    String pSic = "pSic_example"; // String | Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4.
    String pNcs = "pNcs_example"; // String | North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
    BigDecimal pQnc = new BigDecimal(78); // BigDecimal | Number of quarters in non-compliance limiter.  Enter an integer value between 1 and 4 to limit results.
    String pPen = "pPen_example"; // String | Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER = No Penalties - ANY = Any Penalty - LEXX = Less than or equal to XX months.  Provide a number in place of XX, e.g. \\\"LE5\\\" for a facility with a penalty within previous 5 months. - GTXX = Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago.
    String pOpst = "pOpst_example"; // String | Operating status filter.  Enter one or more operating status codes to limit results.   Provide multiple codes as a comma-delimited list.
    BigDecimal pC1lat = new BigDecimal(78); // BigDecimal | In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC1lon = new BigDecimal(78); // BigDecimal | In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC2lat = new BigDecimal(78); // BigDecimal | In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC2lon = new BigDecimal(78); // BigDecimal | In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    String pUsmex = "Y"; // String | US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
    String pSic2 = "pSic2_example"; // String | Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \\\"22\\\" to match all SIC codes beginning with 22.  Use the \\\"%\\\" character within strings to match any SIC values with the pattern.  For example, \\\"2%21\\\" matches 2021, 2121, 2221, etc.
    String pSic4 = "pSic4_example"; // String | Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker.
    String pFa = "pFa_example"; // String | Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values.
    String pAct = "Y"; // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
    String pMaj = "Y"; // String | Major Facility Flag.  Enter Y to restrict results to Major facilities only.
    String pMact = "pMact_example"; // String | CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility.
    String pNsps = "pNsps_example"; // String | Air Programl New Source Performance Standards (NSPS)  Subpart Code Search.  One or more valid Air Program NSPS Program codes cand be passed.  
    String pNspsm = "pNspsm_example"; // String | Air Programl New Source Performance Standards Minors (NSPSM) Subpart Code Search.  One or more valid Air Program NSPSM Subpart codes can be passed.  
    String pProg = "pProg_example"; // String | Air Program Code Filter.  Enter one or more Air program codes to filter results.  Provide multiple values as a comma-delimited list.
    String pFea = "W"; // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
    BigDecimal pFeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
    String pFeaa = "A"; // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
    String pIea = "W"; // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
    BigDecimal pIeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
    String pIeaa = "E"; // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
    String pQiv = "0"; // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    String pNaa = "pNaa_example"; // String | Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas.
    String pImpw = "Y"; // String | Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
    String pTrep = "CURR"; // String | Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR = Current TRI reporter. - NONCURR = Has reported to TRI in the past but not for the current reporting year.
    String pTriCat = "TOTAL"; // String | Toxic Release Inventory Released To Air Chemical Identifier Category Filter.  Enter the chemical identifier category code to limit results. Note when filtering by TRI chemical identifier categories one may not also filter by specific chemical identifiers via p_tri_pol.  You must also specify a release amount using p_tri_amt or p_tri_any_amt. - TOTAL = Total Released to Air - CARC = Total Carcinogens Released to Air - HAP = Total Hazardous Air Pollutants Released to Air
    String pTriAmt = "0"; // String | Toxic Release Inventory Release Amount Filter.  Enter a value in pounds to limit results to facilities releasing this amount or greateer of TRI releases.  Valid values are 0, GT0, GT1000, GT5000, GT10000 and GT50000. Note when filtering by TRI release amounts one may only use either p_tri_amt or p_tri_any_amt.
    BigDecimal pTriAnyAmt = new BigDecimal(78); // BigDecimal | Toxic Release Inventory Release Of Any Kind Above Value Filter.  Enter a value to limit results to facilities releasing this amount or more of TRI releases.  Note when filtering by TRI releases one may only use p_tri_any_amt or p_tri_amt and not both.
    String pTriPol = "pTriPol_example"; // String | Toxic Release Inventory Chemical Identifier Filter.  Enter one or more chemical identifier codes to limit results. Note when filtering by specific TRI chemical identifiers one may not also filter by chemical identifier categories via p_tri_cat.
    String pGhgCat = "ALL"; // String | Green House Gas (GHG) Gas Code Category.  Must be used with either a formatted (p_ghg_amt) or custom (p_ghg_any_amt) release amount.
    String pGhgAmt = "None"; // String | Green House Gas (GHG) CO2 Equivalent Formatted Release Amount.  First 2 characters must contain GT (greater than) followed by a number.
    BigDecimal pGhgAnyAmt = new BigDecimal(78); // BigDecimal | Green House Gas (GHG) C02 Equivalent Custom Amount.  The C02E value reported for the provided category, will be greater or equal to the amount provided.
    String pGhgYr = "pGhgYr_example"; // String | Green House Gas (GHG) Reporting Year. (2010 through 2015)
    String pNeiPol = "pNeiPol_example"; // String | National Emissions Inventory (NEI) Pollutant Identifier.  When a pollutant identifer is entered a corresponding formatted amount or custom amount must be entered.
    String pNeiAmt = "None"; // String | National Emissions Inventory (NEI) Formatted Pollutant Amount.  A formatted value where the 1st two characters must start with GT or LT followed by a number.  Identifies facilities that have a NEI Pollutant Emission  where the supplied value is > or < the pollutant emission amount.  
    BigDecimal pNeiAnyAmt = new BigDecimal(78); // BigDecimal | National Emissions Inventory (NEI) Custom Pollutant Amount.  Only a number can be entered.  Identifies facilities with where the NEI Pollutant Emission Amount is greater than the number entered.
    String pNeiYr = "pNeiYr_example"; // String | National Emissions Inventory (NEI) year:  2014 or 2011
    String pNeiCat = "pNeiCat_example"; // String | National Emissions Inventory (NEI) Pollutant Category.  When a pollutant category is entered, a corresponding formatted pollutant amount or custom amount must be entered.
    String pPm = "NONE"; // String | Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE = 0% - GT5 = greater than 5% - GT10 = greater than 10% - GT25 = greater than 25% - GT50 = greater than 50% - GT75 = greater than 75%
    String pPd = "NONE"; // String | Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE = 0 population density per square mile - GT100 = More than 100 population density per square mile - GT500 = More than 500 population density per square mile - GT1000 = More than 1000 population density per square mile - GT5000 = More than 5000 population density per square mile - GT10000 = More than 10000 population density per square mile - GT20000 = More than 20000 population density per square mile
    String pIco = "Y"; // String | Indian Country Flag.  Enter a \\\"Y\\\" or \\\"N\\\" to restrict searches to facilities inside or outside Indian Country.
    String pHuc = "pHuc_example"; // String | 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
    String pWbd = "pWbd_example"; // String | 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    String pPid = "pPid_example"; // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    String pMed = "M"; // String | Filter Results by Media. - M = RMP (Risk Management Plan) - R = RCRA (Hazardous Waste) - S = SDWA (Public Drinking Water Systems) - W = Water - ALL = Water and RCRA and SDWA
    String pYsl = "W"; // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
    BigDecimal pYsly = new BigDecimal("1"); // BigDecimal | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
    String pYsla = "E"; // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
    String pStsl = "W"; // String | Last Stack Test [within / not within] Specified Date Range Indicator. - W = within date range - N = not within date range
    BigDecimal pStsly = new BigDecimal("1"); // BigDecimal | Number of years (1 to 5) since date of last stack test. A value of 1 means it has been inspected within the year.
    String pStsla = "A"; // String | Stack Last Test Code Filter.  Enter a value to limit results: - A = All - E = EPA - S = State
    String pStres = "pStres_example"; // String | Air Stack Test Status Description Filter.  Enter one or more test status descriptions to filter results.  Enter multiple values as a comma-delimited list.
    String pSttyp = "pSttyp_example"; // String | Air Conductor Type Code Filter.  Enter one or more conductor type codes to filter results.  Provide multiple values as a comma-delimited list.
    String pQs = "pQs_example"; // String | Quick Search. Allows entry for city, state, and/or zip code.
    String pSfs = "pSfs_example"; // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
    BigDecimal pTribeid = new BigDecimal(78); // BigDecimal | Numeric code for tribe (or list of tribes).
    String pTribename = "pTribename_example"; // String | Tribe Name Filter.  Enter a single tribe name to filter results.
    BigDecimal pTribedist = new BigDecimal(78); // BigDecimal | Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
    String pOwop = "pOwop_example"; // String | Owner/Operator code filter.  Enter one or more codes to limit results. - CNG - COR - CTG - DIS - FDF - MWD - MXO - NON - POF - SDT - STF - TRB
    String pAgoo = "AND"; // String | Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
    String pIdt1 = "pIdt1_example"; // String | Beginning of date range of most recent facility inspection.
    String pIdt2 = "pIdt2_example"; // String | End of date range of most recent facility inspection.
    String pStdt1 = "pStdt1_example"; // String | Beginning of date range of most recent stack test.
    String pStdt2 = "pStdt2_example"; // String | End of date range of most recent stack test.
    String pPityp = "pPityp_example"; // String | Inspection Type: - CAC = Corrective Action Inspection - CAV = Compliance Assistance Visit - CDI = Case Development Inspection - CEI = Inspection Inspection - CSE = Compliance Schedule Evaluation - FCI = Focused Compliance - FRR = Financial Record Review - FSD = Facility Self Disclosure - FUI = Follow-Up Inspection - GME = Groundwater Monitoring Evaluation - NRR = Non-Financial Record Review - OAM = Operation and Maintenance Inspection May contain multiple comma-separated values.
    String pCifdi = "Any"; // String | Compliance issuess found during inspection.
    String pPfead1 = "pPfead1_example"; // String | Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    String pPfead2 = "pPfead2_example"; // String | Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    String pPfeat = "pPfeat_example"; // String | Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
    String pPsncq = "GT1"; // String | Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z = Zero quarters in significant noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in significant noncompliance.
    String pPctrack = "false"; // String | Compliance Tracking Limiter. Provide a keyword to indicate the extent to which data is being entered and effluent exceedances are being identified. - Off - Partial - On
    String pSwpa = "source water"; // String | Source water protection area
    String pDes = "pDes_example"; // String | Universe Designation Limiter.  Enter one or more universe designation codes.  Provide multiple values as a comma-delimited list.  Use code \\\"TSDF\\\" to return the full enforcement TSDF universe and \\\"Operating TSDF\\\" to return the operating TSDF universe.
    String pFntype = "ALL"; // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
    String pHpvmth = "pHpvmth_example"; // String | Months in high priority violation status out of the previous three years limiter.  Provide a number of months in the past three years.  Results will limited to facilities in high priority violation status during that time. 
    String pRecvio = "pRecvio_example"; // String | Recent Violation Status Filter.  Enter one or more recent violation codes to limit results.  Provide multiple values as a comma-delimited list. - NO VIOL = Selects facilities with no recent violations. - ANY HPV = Selects facilities with either addressed or unaddressed high priority violations. - ADDRS-EPA - Select facilities with recent EPA addressed violations. - ADDRS-LOCAL - Select facilities with recent locally addressed violations. - ADDRS-STATE - Select facilities with recent state addressed violations. - UNADDR-EPA - Select facilities with recent EPA unaddressed violations. - UNADDR-LOCAL - Select facilities with recent locally unaddressed violations. - UNADDR-STATE - Select facilities with recent state unaddressed violations. - FRV VIOL = Selects facilities with a recent federally reportable violation without a high priority violation.
    String pPollvio = "pPollvio_example"; // String | Air Pollutant Code For A Recent Violation Filter.  Provide one or more pollutant codes to select facilities with one or more of the entered pollutant codes for a recent air violation.  Provide multiple values as a comma-delimited list.
    String pAr = "pAr_example"; // String | Associated EPA Air Reports Program Filter.  Enter multiple values as a comma-delimited list.  Valid values are: - TRI = Toxic Release Inventory. - GHG = Green House Gas Reporter. - EIS = Emission Inventory System. - CAMD = Clean Air Markets Program Reporter.
    String pTriYr = "pTriYr_example"; // String | Toxic Release Inventory Reporting Year Filter.  Enter one or more year values to filter results by the TRI reporting year.  Provide multiple years as a comma-delimited list.
    String pPidall = "Y"; // String | Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc).
    String pFacIco = "Y"; // String | FRS tribal land code flag.  Enter \\\"Y\\\" or \\\"N\\\" to include or exclude facilities based on FRS tribal land code.
    String pIcoo = "pIcoo_example"; // String | Indian country search and/or flag.  Enter \\\"Y\\\" to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
    String pFacIcos = "pFacIcos_example"; // String | FRS tribal land spatial flag.  Enter \\\"Y\\\" or \\\"N\\\" to include or exclude facilities based on FRS tribal land spatial flag.
    String pEjscreen = "pEjscreen_example"; // String | Enter \\\"Y\\\" to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
    String pLimitAddr = "Y"; // String | Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
    BigDecimal pLat = new BigDecimal(78); // BigDecimal | Latitude location in decimal degrees.
    BigDecimal pLong = new BigDecimal(78); // BigDecimal | Longitude location in decimal degrees.
    BigDecimal pRadius = new BigDecimal(78); // BigDecimal | Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
    String pDecouple = "Y"; // String | Decouple Inspection Code Search Flag.  Enter \\\"Y\\\" to search for inspection code types with p_pityp without respect to the date range search provided with p_ysl* parameters.
    String pEjscreenOver80cnt = "1"; // String | The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
    BigDecimal queryset = new BigDecimal(78); // BigDecimal | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    BigDecimal responseset = new BigDecimal(78); // BigDecimal | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    String tablelist = "Y"; // String | Table List Flag. Enter a Y to display the first page of facility results.
    String maplist = "Y"; // String | Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria).
    String summarylist = "Y"; // String | Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    try {
      AirRestServicesGetFacilitiesGet200Response result = apiInstance.airRestServicesGetFacilitiesPost(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pLcon, pFrs, pReg, pSic, pNcs, pQnc, pPen, pOpst, pC1lat, pC1lon, pC2lat, pC2lon, pUsmex, pSic2, pSic4, pFa, pAct, pMaj, pMact, pNsps, pNspsm, pProg, pFea, pFeay, pFeaa, pIea, pIeay, pIeaa, pQiv, pNaa, pImpw, pTrep, pTriCat, pTriAmt, pTriAnyAmt, pTriPol, pGhgCat, pGhgAmt, pGhgAnyAmt, pGhgYr, pNeiPol, pNeiAmt, pNeiAnyAmt, pNeiYr, pNeiCat, pPm, pPd, pIco, pHuc, pWbd, pPid, pMed, pYsl, pYsly, pYsla, pStsl, pStsly, pStsla, pStres, pSttyp, pQs, pSfs, pTribeid, pTribename, pTribedist, pOwop, pAgoo, pIdt1, pIdt2, pStdt1, pStdt2, pPityp, pCifdi, pPfead1, pPfead2, pPfeat, pPsncq, pPctrack, pSwpa, pDes, pFntype, pHpvmth, pRecvio, pPollvio, pAr, pTriYr, pPidall, pFacIco, pIcoo, pFacIcos, pEjscreen, pLimitAddr, pLat, pLong, pRadius, pDecouple, pEjscreenOver80cnt, queryset, responseset, tablelist, maplist, summarylist, paramCallback, qcolumns);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilitiesApi#airRestServicesGetFacilitiesPost");
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
| **pLcon** | **String**| Air Program Local Control Region Code Filter.  Enter one or more local control region codes to filter results.  Provide multiple codes as a comma-delimited list.  Codes where they exist are specific by state. | [optional] |
| **pFrs** | **String**| Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results. | [optional] |
| **pReg** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] [enum: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10] |
| **pSic** | **String**| Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4. | [optional] |
| **pNcs** | **String**| North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values. | [optional] |
| **pQnc** | **BigDecimal**| Number of quarters in non-compliance limiter.  Enter an integer value between 1 and 4 to limit results. | [optional] |
| **pPen** | **String**| Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER &#x3D; No Penalties - ANY &#x3D; Any Penalty - LEXX &#x3D; Less than or equal to XX months.  Provide a number in place of XX, e.g. \\\&quot;LE5\\\&quot; for a facility with a penalty within previous 5 months. - GTXX &#x3D; Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago. | [optional] |
| **pOpst** | **String**| Operating status filter.  Enter one or more operating status codes to limit results.   Provide multiple codes as a comma-delimited list. | [optional] |
| **pC1lat** | **BigDecimal**| In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC1lon** | **BigDecimal**| In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC2lat** | **BigDecimal**| In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC2lon** | **BigDecimal**| In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pUsmex** | **String**| US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border. | [optional] [enum: Y, N] |
| **pSic2** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \\\&quot;22\\\&quot; to match all SIC codes beginning with 22.  Use the \\\&quot;%\\\&quot; character within strings to match any SIC values with the pattern.  For example, \\\&quot;2%21\\\&quot; matches 2021, 2121, 2221, etc. | [optional] |
| **pSic4** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker. | [optional] |
| **pFa** | **String**| Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values. | [optional] |
| **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits. | [optional] [enum: Y, N, A] |
| **pMaj** | **String**| Major Facility Flag.  Enter Y to restrict results to Major facilities only. | [optional] [enum: Y, N] |
| **pMact** | **String**| CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility. | [optional] |
| **pNsps** | **String**| Air Programl New Source Performance Standards (NSPS)  Subpart Code Search.  One or more valid Air Program NSPS Program codes cand be passed.   | [optional] |
| **pNspsm** | **String**| Air Programl New Source Performance Standards Minors (NSPSM) Subpart Code Search.  One or more valid Air Program NSPSM Subpart codes can be passed.   | [optional] |
| **pProg** | **String**| Air Program Code Filter.  Enter one or more Air program codes to filter results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pFeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] [enum: A, E, S] |
| **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pIeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S] |
| **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] [enum: 0, GT1, GT2, GT4, GT8, 12] |
| **pNaa** | **String**| Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas. | [optional] |
| **pImpw** | **String**| Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database. | [optional] [enum: Y, N] |
| **pTrep** | **String**| Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year. | [optional] [enum: CURR, NOTCURR] |
| **pTriCat** | **String**| Toxic Release Inventory Released To Air Chemical Identifier Category Filter.  Enter the chemical identifier category code to limit results. Note when filtering by TRI chemical identifier categories one may not also filter by specific chemical identifiers via p_tri_pol.  You must also specify a release amount using p_tri_amt or p_tri_any_amt. - TOTAL &#x3D; Total Released to Air - CARC &#x3D; Total Carcinogens Released to Air - HAP &#x3D; Total Hazardous Air Pollutants Released to Air | [optional] [enum: TOTAL, CARC, HAP] |
| **pTriAmt** | **String**| Toxic Release Inventory Release Amount Filter.  Enter a value in pounds to limit results to facilities releasing this amount or greateer of TRI releases.  Valid values are 0, GT0, GT1000, GT5000, GT10000 and GT50000. Note when filtering by TRI release amounts one may only use either p_tri_amt or p_tri_any_amt. | [optional] [enum: 0, GT0, GT1000, GT5000, GT10000, GT50000] |
| **pTriAnyAmt** | **BigDecimal**| Toxic Release Inventory Release Of Any Kind Above Value Filter.  Enter a value to limit results to facilities releasing this amount or more of TRI releases.  Note when filtering by TRI releases one may only use p_tri_any_amt or p_tri_amt and not both. | [optional] |
| **pTriPol** | **String**| Toxic Release Inventory Chemical Identifier Filter.  Enter one or more chemical identifier codes to limit results. Note when filtering by specific TRI chemical identifiers one may not also filter by chemical identifier categories via p_tri_cat. | [optional] |
| **pGhgCat** | **String**| Green House Gas (GHG) Gas Code Category.  Must be used with either a formatted (p_ghg_amt) or custom (p_ghg_any_amt) release amount. | [optional] [enum: ALL, BIOCO2, CH4, CO2, HFC, N2O, NF3, OTHER_L, PFC, SF6] |
| **pGhgAmt** | **String**| Green House Gas (GHG) CO2 Equivalent Formatted Release Amount.  First 2 characters must contain GT (greater than) followed by a number. | [optional] [enum: None, 0, GT0, GT10000, GT25000, GT250000, GT1000000] |
| **pGhgAnyAmt** | **BigDecimal**| Green House Gas (GHG) C02 Equivalent Custom Amount.  The C02E value reported for the provided category, will be greater or equal to the amount provided. | [optional] |
| **pGhgYr** | **String**| Green House Gas (GHG) Reporting Year. (2010 through 2015) | [optional] |
| **pNeiPol** | **String**| National Emissions Inventory (NEI) Pollutant Identifier.  When a pollutant identifer is entered a corresponding formatted amount or custom amount must be entered. | [optional] |
| **pNeiAmt** | **String**| National Emissions Inventory (NEI) Formatted Pollutant Amount.  A formatted value where the 1st two characters must start with GT or LT followed by a number.  Identifies facilities that have a NEI Pollutant Emission  where the supplied value is &gt; or &lt; the pollutant emission amount.   | [optional] [enum: None, 0, GT0, GT10000, GT25000, GT250000, GT1000000] |
| **pNeiAnyAmt** | **BigDecimal**| National Emissions Inventory (NEI) Custom Pollutant Amount.  Only a number can be entered.  Identifies facilities with where the NEI Pollutant Emission Amount is greater than the number entered. | [optional] |
| **pNeiYr** | **String**| National Emissions Inventory (NEI) year:  2014 or 2011 | [optional] |
| **pNeiCat** | **String**| National Emissions Inventory (NEI) Pollutant Category.  When a pollutant category is entered, a corresponding formatted pollutant amount or custom amount must be entered. | [optional] |
| **pPm** | **String**| Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75% | [optional] [enum: NONE, GT5, GT10, GT25, GT50, GT75] |
| **pPd** | **String**| Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile | [optional] [enum: NONE, GT100, GT500, GT1000, GT5000, GT10000, GT20000] |
| **pIco** | **String**| Indian Country Flag.  Enter a \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] [enum: Y, N] |
| **pHuc** | **String**| 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values. | [optional] |
| **pWbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] |
| **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] |
| **pMed** | **String**| Filter Results by Media. - M &#x3D; RMP (Risk Management Plan) - R &#x3D; RCRA (Hazardous Waste) - S &#x3D; SDWA (Public Drinking Water Systems) - W &#x3D; Water - ALL &#x3D; Water and RCRA and SDWA | [optional] [enum: M, R, S, W, ALL] |
| **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N, NV] |
| **pYsly** | **BigDecimal**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S, A] |
| **pStsl** | **String**| Last Stack Test [within / not within] Specified Date Range Indicator. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pStsly** | **BigDecimal**| Number of years (1 to 5) since date of last stack test. A value of 1 means it has been inspected within the year. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pStsla** | **String**| Stack Last Test Code Filter.  Enter a value to limit results: - A &#x3D; All - E &#x3D; EPA - S &#x3D; State | [optional] [enum: A, E, S] |
| **pStres** | **String**| Air Stack Test Status Description Filter.  Enter one or more test status descriptions to filter results.  Enter multiple values as a comma-delimited list. | [optional] |
| **pSttyp** | **String**| Air Conductor Type Code Filter.  Enter one or more conductor type codes to filter results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] |
| **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] |
| **pTribeid** | **BigDecimal**| Numeric code for tribe (or list of tribes). | [optional] |
| **pTribename** | **String**| Tribe Name Filter.  Enter a single tribe name to filter results. | [optional] |
| **pTribedist** | **BigDecimal**| Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated. | [optional] |
| **pOwop** | **String**| Owner/Operator code filter.  Enter one or more codes to limit results. - CNG - COR - CTG - DIS - FDF - MWD - MXO - NON - POF - SDT - STF - TRB | [optional] |
| **pAgoo** | **String**| Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters. | [optional] [enum: AND, OR] |
| **pIdt1** | **String**| Beginning of date range of most recent facility inspection. | [optional] |
| **pIdt2** | **String**| End of date range of most recent facility inspection. | [optional] |
| **pStdt1** | **String**| Beginning of date range of most recent stack test. | [optional] |
| **pStdt2** | **String**| End of date range of most recent stack test. | [optional] |
| **pPityp** | **String**| Inspection Type: - CAC &#x3D; Corrective Action Inspection - CAV &#x3D; Compliance Assistance Visit - CDI &#x3D; Case Development Inspection - CEI &#x3D; Inspection Inspection - CSE &#x3D; Compliance Schedule Evaluation - FCI &#x3D; Focused Compliance - FRR &#x3D; Financial Record Review - FSD &#x3D; Facility Self Disclosure - FUI &#x3D; Follow-Up Inspection - GME &#x3D; Groundwater Monitoring Evaluation - NRR &#x3D; Non-Financial Record Review - OAM &#x3D; Operation and Maintenance Inspection May contain multiple comma-separated values. | [optional] |
| **pCifdi** | **String**| Compliance issuess found during inspection. | [optional] [enum: Any, true, false, Undetermined] |
| **pPfead1** | **String**| Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] |
| **pPfead2** | **String**| Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] |
| **pPfeat** | **String**| Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list. | [optional] |
| **pPsncq** | **String**| Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z &#x3D; Zero quarters in significant noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in significant noncompliance. | [optional] [enum: GT1, GE1, GT2, GE2, GT4, GE4, GT8, GE8, GT12, GE12] |
| **pPctrack** | **String**| Compliance Tracking Limiter. Provide a keyword to indicate the extent to which data is being entered and effluent exceedances are being identified. - Off - Partial - On | [optional] [enum: false, Partial, true] |
| **pSwpa** | **String**| Source water protection area | [optional] [enum: source water, surface water, ground water, waiting for SSO] |
| **pDes** | **String**| Universe Designation Limiter.  Enter one or more universe designation codes.  Provide multiple values as a comma-delimited list.  Use code \\\&quot;TSDF\\\&quot; to return the full enforcement TSDF universe and \\\&quot;Operating TSDF\\\&quot; to return the operating TSDF universe. | [optional] |
| **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] [enum: ALL, CONTAINS, EXACT, BEGINS] |
| **pHpvmth** | **String**| Months in high priority violation status out of the previous three years limiter.  Provide a number of months in the past three years.  Results will limited to facilities in high priority violation status during that time.  | [optional] |
| **pRecvio** | **String**| Recent Violation Status Filter.  Enter one or more recent violation codes to limit results.  Provide multiple values as a comma-delimited list. - NO VIOL &#x3D; Selects facilities with no recent violations. - ANY HPV &#x3D; Selects facilities with either addressed or unaddressed high priority violations. - ADDRS-EPA - Select facilities with recent EPA addressed violations. - ADDRS-LOCAL - Select facilities with recent locally addressed violations. - ADDRS-STATE - Select facilities with recent state addressed violations. - UNADDR-EPA - Select facilities with recent EPA unaddressed violations. - UNADDR-LOCAL - Select facilities with recent locally unaddressed violations. - UNADDR-STATE - Select facilities with recent state unaddressed violations. - FRV VIOL &#x3D; Selects facilities with a recent federally reportable violation without a high priority violation. | [optional] |
| **pPollvio** | **String**| Air Pollutant Code For A Recent Violation Filter.  Provide one or more pollutant codes to select facilities with one or more of the entered pollutant codes for a recent air violation.  Provide multiple values as a comma-delimited list. | [optional] |
| **pAr** | **String**| Associated EPA Air Reports Program Filter.  Enter multiple values as a comma-delimited list.  Valid values are: - TRI &#x3D; Toxic Release Inventory. - GHG &#x3D; Green House Gas Reporter. - EIS &#x3D; Emission Inventory System. - CAMD &#x3D; Clean Air Markets Program Reporter. | [optional] |
| **pTriYr** | **String**| Toxic Release Inventory Reporting Year Filter.  Enter one or more year values to filter results by the TRI reporting year.  Provide multiple years as a comma-delimited list. | [optional] |
| **pPidall** | **String**| Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc). | [optional] [enum: Y, N] |
| **pFacIco** | **String**| FRS tribal land code flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land code. | [optional] [enum: Y, N] |
| **pIcoo** | **String**| Indian country search and/or flag.  Enter \\\&quot;Y\\\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned. | [optional] |
| **pFacIcos** | **String**| FRS tribal land spatial flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land spatial flag. | [optional] |
| **pEjscreen** | **String**| Enter \\\&quot;Y\\\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile. | [optional] |
| **pLimitAddr** | **String**| Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.   | [optional] [enum: Y, N] |
| **pLat** | **BigDecimal**| Latitude location in decimal degrees. | [optional] |
| **pLong** | **BigDecimal**| Longitude location in decimal degrees. | [optional] |
| **pRadius** | **BigDecimal**| Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities. | [optional] |
| **pDecouple** | **String**| Decouple Inspection Code Search Flag.  Enter \\\&quot;Y\\\&quot; to search for inspection code types with p_pityp without respect to the date range search provided with p_ysl* parameters. | [optional] [enum: Y, N] |
| **pEjscreenOver80cnt** | **String**| The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11. | [optional] [enum: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] |
| **queryset** | **BigDecimal**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] |
| **responseset** | **BigDecimal**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] |
| **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] [enum: Y, N] |
| **maplist** | **String**| Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria). | [optional] [enum: Y, N] |
| **summarylist** | **String**| Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service. | [optional] [enum: Y, N] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |

### Return type

[**AirRestServicesGetFacilitiesGet200Response**](AirRestServicesGetFacilitiesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are summary statistics for the query and a query identifier (QID). |  -  |

<a id="airRestServicesGetFacilityInfoGet"></a>
# **airRestServicesGetFacilityInfoGet**
> AirRestServicesGetFacilityInfoGet200Response airRestServicesGetFacilityInfoGet(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pLcon, pFrs, pReg, pSic, pNcs, pQnc, pPen, pOpst, xmin, ymin, xmax, ymax, pUsmex, pSic2, pSic4, pFa, pAct, pMaj, pMact, pNsps, pNspsm, pProg, pFea, pFeay, pFeaa, pIea, pIeay, pIeaa, pQiv, pNaa, pImpw, pTrep, pTriCat, pTriAmt, pTriAnyAmt, pTriPol, pGhgCat, pGhgAmt, pGhgAnyAmt, pGhgYr, pNeiPol, pNeiAmt, pNeiAnyAmt, pNeiYr, pNeiCat, pPm, pPd, pIco, pHuc, pWbd, pPid, pMed, pYsl, pYsly, pYsla, pStsl, pStsly, pStsla, pStres, pSttyp, pQs, pSfs, pTribeid, pTribename, pTribedist, pOwop, pAgoo, pIdt1, pIdt2, pStdt1, pStdt2, pPityp, pCifdi, pPfead1, pPfead2, pPfeat, pPsncq, pPctrack, pSwpa, pDes, pFntype, pHpvmth, pRecvio, pPollvio, pAr, pTriYr, pPidall, pFacIco, pIcoo, pFacIcos, pEjscreen, pLimitAddr, pLat, pLong, pRadius, pDecouple, pEjscreenOver80cnt, queryset, responseset, summarylist, paramCallback, qcolumns, pPrettyPrint)

Clean Air Act Facility Enhanced Search

Returns either an array of Facilities or an array of Clusters that meet the specified search criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilitiesApi apiInstance = new FacilitiesApi(defaultClient);
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language. - CSV = Facility results formatted as comma delimited file download. - GEOJSON = Facility results formatted as GeoJSON feature collection. - GEOJSONP = Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
    String pFn = "pFn_example"; // String | Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
    String pSa = "pSa_example"; // String | Facility street address. Enter a complete or partial street address.
    String pSa1 = "pSa1_example"; // String | Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa.
    String pCt = "pCt_example"; // String | Facility City Filter. Enter a single case-insensitive city name to filter results.
    String pCo = "pCo_example"; // String | Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
    String pFips = "pFips_example"; // String | FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
    String pSt = "pSt_example"; // String | Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
    String pZip = "pZip_example"; // String | 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values.
    String pLcon = "pLcon_example"; // String | Air Program Local Control Region Code Filter.  Enter one or more local control region codes to filter results.  Provide multiple codes as a comma-delimited list.  Codes where they exist are specific by state.
    String pFrs = "pFrs_example"; // String | Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results.
    String pReg = "01"; // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    String pSic = "pSic_example"; // String | Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4.
    String pNcs = "pNcs_example"; // String | North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
    BigDecimal pQnc = new BigDecimal(78); // BigDecimal | Number of quarters in non-compliance limiter.  Enter an integer value between 1 and 4 to limit results.
    String pPen = "pPen_example"; // String | Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER = No Penalties - ANY = Any Penalty - LEXX = Less than or equal to XX months.  Provide a number in place of XX, e.g. \"LE5\" for a facility with a penalty within previous 5 months. - GTXX = Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago.
    String pOpst = "pOpst_example"; // String | Operating status filter.  Enter one or more operating status codes to limit results.   Provide multiple codes as a comma-delimited list.
    BigDecimal xmin = new BigDecimal(78); // BigDecimal | Minimum longitude value in decimal degrees.
    BigDecimal ymin = new BigDecimal(78); // BigDecimal | Minimum latitude value in decimal degrees.
    BigDecimal xmax = new BigDecimal(78); // BigDecimal | Maximum longitude value in decimal degrees.
    BigDecimal ymax = new BigDecimal(78); // BigDecimal | Maximum latitude value in decimal degrees.
    String pUsmex = "Y"; // String | US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
    String pSic2 = "pSic2_example"; // String | Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \"22\" to match all SIC codes beginning with 22.  Use the \"%\" character within strings to match any SIC values with the pattern.  For example, \"2%21\" matches 2021, 2121, 2221, etc.
    String pSic4 = "pSic4_example"; // String | Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker.
    String pFa = "pFa_example"; // String | Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values.
    String pAct = "Y"; // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
    String pMaj = "Y"; // String | Major Facility Flag.  Enter Y to restrict results to Major facilities only.
    String pMact = "pMact_example"; // String | CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility.
    String pNsps = "pNsps_example"; // String | Air Programl New Source Performance Standards (NSPS)  Subpart Code Search.  One or more valid Air Program NSPS Program codes cand be passed.  
    String pNspsm = "pNspsm_example"; // String | Air Programl New Source Performance Standards Minors (NSPSM) Subpart Code Search.  One or more valid Air Program NSPSM Subpart codes can be passed.  
    String pProg = "pProg_example"; // String | Air Program Code Filter.  Enter one or more Air program codes to filter results.  Provide multiple values as a comma-delimited list.
    String pFea = "W"; // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
    BigDecimal pFeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
    String pFeaa = "A"; // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
    String pIea = "W"; // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
    BigDecimal pIeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
    String pIeaa = "E"; // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
    String pQiv = "0"; // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    String pNaa = "pNaa_example"; // String | Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas.
    String pImpw = "Y"; // String | Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
    String pTrep = "CURR"; // String | Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR = Current TRI reporter. - NONCURR = Has reported to TRI in the past but not for the current reporting year.
    String pTriCat = "TOTAL"; // String | Toxic Release Inventory Released To Air Chemical Identifier Category Filter.  Enter the chemical identifier category code to limit results. Note when filtering by TRI chemical identifier categories one may not also filter by specific chemical identifiers via p_tri_pol.  You must also specify a release amount using p_tri_amt or p_tri_any_amt. - TOTAL = Total Released to Air - CARC = Total Carcinogens Released to Air - HAP = Total Hazardous Air Pollutants Released to Air
    String pTriAmt = "0"; // String | Toxic Release Inventory Release Amount Filter.  Enter a value in pounds to limit results to facilities releasing this amount or greateer of TRI releases.  Valid values are 0, GT0, GT1000, GT5000, GT10000 and GT50000. Note when filtering by TRI release amounts one may only use either p_tri_amt or p_tri_any_amt.
    BigDecimal pTriAnyAmt = new BigDecimal(78); // BigDecimal | Toxic Release Inventory Release Of Any Kind Above Value Filter.  Enter a value to limit results to facilities releasing this amount or more of TRI releases.  Note when filtering by TRI releases one may only use p_tri_any_amt or p_tri_amt and not both.
    String pTriPol = "pTriPol_example"; // String | Toxic Release Inventory Chemical Identifier Filter.  Enter one or more chemical identifier codes to limit results. Note when filtering by specific TRI chemical identifiers one may not also filter by chemical identifier categories via p_tri_cat.
    String pGhgCat = "ALL"; // String | Green House Gas (GHG) Gas Code Category.  Must be used with either a formatted (p_ghg_amt) or custom (p_ghg_any_amt) release amount.
    String pGhgAmt = "None"; // String | Green House Gas (GHG) CO2 Equivalent Formatted Release Amount.  First 2 characters must contain GT (greater than) followed by a number.
    BigDecimal pGhgAnyAmt = new BigDecimal(78); // BigDecimal | Green House Gas (GHG) C02 Equivalent Custom Amount.  The C02E value reported for the provided category, will be greater or equal to the amount provided.
    String pGhgYr = "pGhgYr_example"; // String | Green House Gas (GHG) Reporting Year. (2010 through 2015)
    String pNeiPol = "pNeiPol_example"; // String | National Emissions Inventory (NEI) Pollutant Identifier.  When a pollutant identifer is entered a corresponding formatted amount or custom amount must be entered.
    String pNeiAmt = "None"; // String | National Emissions Inventory (NEI) Formatted Pollutant Amount.  A formatted value where the 1st two characters must start with GT or LT followed by a number.  Identifies facilities that have a NEI Pollutant Emission  where the supplied value is > or < the pollutant emission amount.  
    BigDecimal pNeiAnyAmt = new BigDecimal(78); // BigDecimal | National Emissions Inventory (NEI) Custom Pollutant Amount.  Only a number can be entered.  Identifies facilities with where the NEI Pollutant Emission Amount is greater than the number entered.
    String pNeiYr = "pNeiYr_example"; // String | National Emissions Inventory (NEI) year:  2014 or 2011
    String pNeiCat = "pNeiCat_example"; // String | National Emissions Inventory (NEI) Pollutant Category.  When a pollutant category is entered, a corresponding formatted pollutant amount or custom amount must be entered.
    String pPm = "NONE"; // String | Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE = 0% - GT5 = greater than 5% - GT10 = greater than 10% - GT25 = greater than 25% - GT50 = greater than 50% - GT75 = greater than 75%
    String pPd = "NONE"; // String | Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE = 0 population density per square mile - GT100 = More than 100 population density per square mile - GT500 = More than 500 population density per square mile - GT1000 = More than 1000 population density per square mile - GT5000 = More than 5000 population density per square mile - GT10000 = More than 10000 population density per square mile - GT20000 = More than 20000 population density per square mile
    String pIco = "Y"; // String | Indian Country Flag.  Enter a \"Y\" or \"N\" to restrict searches to facilities inside or outside Indian Country.
    String pHuc = "pHuc_example"; // String | 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
    String pWbd = "pWbd_example"; // String | 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    String pPid = "pPid_example"; // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    String pMed = "M"; // String | Filter Results by Media. - M = RMP (Risk Management Plan) - R = RCRA (Hazardous Waste) - S = SDWA (Public Drinking Water Systems) - W = Water - ALL = Water and RCRA and SDWA
    String pYsl = "W"; // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
    BigDecimal pYsly = new BigDecimal("1"); // BigDecimal | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
    String pYsla = "E"; // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
    String pStsl = "W"; // String | Last Stack Test [within / not within] Specified Date Range Indicator. - W = within date range - N = not within date range
    BigDecimal pStsly = new BigDecimal("1"); // BigDecimal | Number of years (1 to 5) since date of last stack test. A value of 1 means it has been inspected within the year.
    String pStsla = "A"; // String | Stack Last Test Code Filter.  Enter a value to limit results: - A = All - E = EPA - S = State
    String pStres = "pStres_example"; // String | Air Stack Test Status Description Filter.  Enter one or more test status descriptions to filter results.  Enter multiple values as a comma-delimited list.
    String pSttyp = "pSttyp_example"; // String | Air Conductor Type Code Filter.  Enter one or more conductor type codes to filter results.  Provide multiple values as a comma-delimited list.
    String pQs = "pQs_example"; // String | Quick Search. Allows entry for city, state, and/or zip code.
    String pSfs = "pSfs_example"; // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
    BigDecimal pTribeid = new BigDecimal(78); // BigDecimal | Numeric code for tribe (or list of tribes).
    String pTribename = "pTribename_example"; // String | Tribe Name Filter.  Enter a single tribe name to filter results.
    BigDecimal pTribedist = new BigDecimal(78); // BigDecimal | Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
    String pOwop = "pOwop_example"; // String | Owner/Operator code filter.  Enter one or more codes to limit results. - CNG - COR - CTG - DIS - FDF - MWD - MXO - NON - POF - SDT - STF - TRB
    String pAgoo = "AND"; // String | Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
    String pIdt1 = "pIdt1_example"; // String | Beginning of date range of most recent facility inspection.
    String pIdt2 = "pIdt2_example"; // String | End of date range of most recent facility inspection.
    String pStdt1 = "pStdt1_example"; // String | Beginning of date range of most recent stack test.
    String pStdt2 = "pStdt2_example"; // String | End of date range of most recent stack test.
    String pPityp = "pPityp_example"; // String | Inspection Type: - CAC = Corrective Action Inspection - CAV = Compliance Assistance Visit - CDI = Case Development Inspection - CEI = Inspection Inspection - CSE = Compliance Schedule Evaluation - FCI = Focused Compliance - FRR = Financial Record Review - FSD = Facility Self Disclosure - FUI = Follow-Up Inspection - GME = Groundwater Monitoring Evaluation - NRR = Non-Financial Record Review - OAM = Operation and Maintenance Inspection May contain multiple comma-separated values.
    String pCifdi = "Any"; // String | Compliance issuess found during inspection.
    String pPfead1 = "pPfead1_example"; // String | Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    String pPfead2 = "pPfead2_example"; // String | Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    String pPfeat = "pPfeat_example"; // String | Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
    String pPsncq = "GT1"; // String | Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z = Zero quarters in significant noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in significant noncompliance.
    String pPctrack = "false"; // String | Compliance Tracking Limiter. Provide a keyword to indicate the extent to which data is being entered and effluent exceedances are being identified. - Off - Partial - On
    String pSwpa = "source water"; // String | Source water protection area
    String pDes = "pDes_example"; // String | Universe Designation Limiter.  Enter one or more universe designation codes.  Provide multiple values as a comma-delimited list.  Use code \"TSDF\" to return the full enforcement TSDF universe and \"Operating TSDF\" to return the operating TSDF universe.
    String pFntype = "ALL"; // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
    String pHpvmth = "pHpvmth_example"; // String | Months in high priority violation status out of the previous three years limiter.  Provide a number of months in the past three years.  Results will limited to facilities in high priority violation status during that time. 
    String pRecvio = "pRecvio_example"; // String | Recent Violation Status Filter.  Enter one or more recent violation codes to limit results.  Provide multiple values as a comma-delimited list. - NO VIOL = Selects facilities with no recent violations. - ANY HPV = Selects facilities with either addressed or unaddressed high priority violations. - ADDRS-EPA - Select facilities with recent EPA addressed violations. - ADDRS-LOCAL - Select facilities with recent locally addressed violations. - ADDRS-STATE - Select facilities with recent state addressed violations. - UNADDR-EPA - Select facilities with recent EPA unaddressed violations. - UNADDR-LOCAL - Select facilities with recent locally unaddressed violations. - UNADDR-STATE - Select facilities with recent state unaddressed violations. - FRV VIOL = Selects facilities with a recent federally reportable violation without a high priority violation.
    String pPollvio = "pPollvio_example"; // String | Air Pollutant Code For A Recent Violation Filter.  Provide one or more pollutant codes to select facilities with one or more of the entered pollutant codes for a recent air violation.  Provide multiple values as a comma-delimited list.
    String pAr = "pAr_example"; // String | Associated EPA Air Reports Program Filter.  Enter multiple values as a comma-delimited list.  Valid values are: - TRI = Toxic Release Inventory. - GHG = Green House Gas Reporter. - EIS = Emission Inventory System. - CAMD = Clean Air Markets Program Reporter.
    String pTriYr = "pTriYr_example"; // String | Toxic Release Inventory Reporting Year Filter.  Enter one or more year values to filter results by the TRI reporting year.  Provide multiple years as a comma-delimited list.
    String pPidall = "Y"; // String | Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc).
    String pFacIco = "Y"; // String | FRS tribal land code flag.  Enter \"Y\" or \"N\" to include or exclude facilities based on FRS tribal land code.
    String pIcoo = "pIcoo_example"; // String | Indian country search and/or flag.  Enter \"Y\" to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
    String pFacIcos = "pFacIcos_example"; // String | FRS tribal land spatial flag.  Enter \"Y\" or \"N\" to include or exclude facilities based on FRS tribal land spatial flag.
    String pEjscreen = "pEjscreen_example"; // String | Enter \"Y\" to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
    String pLimitAddr = "Y"; // String | Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
    BigDecimal pLat = new BigDecimal(78); // BigDecimal | Latitude location in decimal degrees.
    BigDecimal pLong = new BigDecimal(78); // BigDecimal | Longitude location in decimal degrees.
    BigDecimal pRadius = new BigDecimal(78); // BigDecimal | Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
    String pDecouple = "Y"; // String | Decouple Inspection Code Search Flag.  Enter \"Y\" to search for inspection code types with p_pityp without respect to the date range search provided with p_ysl* parameters.
    String pEjscreenOver80cnt = "1"; // String | The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
    BigDecimal queryset = new BigDecimal(78); // BigDecimal | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    BigDecimal responseset = new BigDecimal(78); // BigDecimal | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    String summarylist = "Y"; // String | Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      AirRestServicesGetFacilityInfoGet200Response result = apiInstance.airRestServicesGetFacilityInfoGet(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pLcon, pFrs, pReg, pSic, pNcs, pQnc, pPen, pOpst, xmin, ymin, xmax, ymax, pUsmex, pSic2, pSic4, pFa, pAct, pMaj, pMact, pNsps, pNspsm, pProg, pFea, pFeay, pFeaa, pIea, pIeay, pIeaa, pQiv, pNaa, pImpw, pTrep, pTriCat, pTriAmt, pTriAnyAmt, pTriPol, pGhgCat, pGhgAmt, pGhgAnyAmt, pGhgYr, pNeiPol, pNeiAmt, pNeiAnyAmt, pNeiYr, pNeiCat, pPm, pPd, pIco, pHuc, pWbd, pPid, pMed, pYsl, pYsly, pYsla, pStsl, pStsly, pStsla, pStres, pSttyp, pQs, pSfs, pTribeid, pTribename, pTribedist, pOwop, pAgoo, pIdt1, pIdt2, pStdt1, pStdt2, pPityp, pCifdi, pPfead1, pPfead2, pPfeat, pPsncq, pPctrack, pSwpa, pDes, pFntype, pHpvmth, pRecvio, pPollvio, pAr, pTriYr, pPidall, pFacIco, pIcoo, pFacIcos, pEjscreen, pLimitAddr, pLat, pLong, pRadius, pDecouple, pEjscreenOver80cnt, queryset, responseset, summarylist, paramCallback, qcolumns, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilitiesApi#airRestServicesGetFacilityInfoGet");
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
| **pLcon** | **String**| Air Program Local Control Region Code Filter.  Enter one or more local control region codes to filter results.  Provide multiple codes as a comma-delimited list.  Codes where they exist are specific by state. | [optional] |
| **pFrs** | **String**| Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results. | [optional] |
| **pReg** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] [enum: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10] |
| **pSic** | **String**| Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4. | [optional] |
| **pNcs** | **String**| North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values. | [optional] |
| **pQnc** | **BigDecimal**| Number of quarters in non-compliance limiter.  Enter an integer value between 1 and 4 to limit results. | [optional] |
| **pPen** | **String**| Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER &#x3D; No Penalties - ANY &#x3D; Any Penalty - LEXX &#x3D; Less than or equal to XX months.  Provide a number in place of XX, e.g. \&quot;LE5\&quot; for a facility with a penalty within previous 5 months. - GTXX &#x3D; Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago. | [optional] |
| **pOpst** | **String**| Operating status filter.  Enter one or more operating status codes to limit results.   Provide multiple codes as a comma-delimited list. | [optional] |
| **xmin** | **BigDecimal**| Minimum longitude value in decimal degrees. | [optional] |
| **ymin** | **BigDecimal**| Minimum latitude value in decimal degrees. | [optional] |
| **xmax** | **BigDecimal**| Maximum longitude value in decimal degrees. | [optional] |
| **ymax** | **BigDecimal**| Maximum latitude value in decimal degrees. | [optional] |
| **pUsmex** | **String**| US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border. | [optional] [enum: Y, N] |
| **pSic2** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \&quot;22\&quot; to match all SIC codes beginning with 22.  Use the \&quot;%\&quot; character within strings to match any SIC values with the pattern.  For example, \&quot;2%21\&quot; matches 2021, 2121, 2221, etc. | [optional] |
| **pSic4** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker. | [optional] |
| **pFa** | **String**| Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values. | [optional] |
| **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits. | [optional] [enum: Y, N, A] |
| **pMaj** | **String**| Major Facility Flag.  Enter Y to restrict results to Major facilities only. | [optional] [enum: Y, N] |
| **pMact** | **String**| CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility. | [optional] |
| **pNsps** | **String**| Air Programl New Source Performance Standards (NSPS)  Subpart Code Search.  One or more valid Air Program NSPS Program codes cand be passed.   | [optional] |
| **pNspsm** | **String**| Air Programl New Source Performance Standards Minors (NSPSM) Subpart Code Search.  One or more valid Air Program NSPSM Subpart codes can be passed.   | [optional] |
| **pProg** | **String**| Air Program Code Filter.  Enter one or more Air program codes to filter results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pFeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] [enum: A, E, S] |
| **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pIeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S] |
| **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] [enum: 0, GT1, GT2, GT4, GT8, 12] |
| **pNaa** | **String**| Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas. | [optional] |
| **pImpw** | **String**| Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database. | [optional] [enum: Y, N] |
| **pTrep** | **String**| Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year. | [optional] [enum: CURR, NOTCURR] |
| **pTriCat** | **String**| Toxic Release Inventory Released To Air Chemical Identifier Category Filter.  Enter the chemical identifier category code to limit results. Note when filtering by TRI chemical identifier categories one may not also filter by specific chemical identifiers via p_tri_pol.  You must also specify a release amount using p_tri_amt or p_tri_any_amt. - TOTAL &#x3D; Total Released to Air - CARC &#x3D; Total Carcinogens Released to Air - HAP &#x3D; Total Hazardous Air Pollutants Released to Air | [optional] [enum: TOTAL, CARC, HAP] |
| **pTriAmt** | **String**| Toxic Release Inventory Release Amount Filter.  Enter a value in pounds to limit results to facilities releasing this amount or greateer of TRI releases.  Valid values are 0, GT0, GT1000, GT5000, GT10000 and GT50000. Note when filtering by TRI release amounts one may only use either p_tri_amt or p_tri_any_amt. | [optional] [enum: 0, GT0, GT1000, GT5000, GT10000, GT50000] |
| **pTriAnyAmt** | **BigDecimal**| Toxic Release Inventory Release Of Any Kind Above Value Filter.  Enter a value to limit results to facilities releasing this amount or more of TRI releases.  Note when filtering by TRI releases one may only use p_tri_any_amt or p_tri_amt and not both. | [optional] |
| **pTriPol** | **String**| Toxic Release Inventory Chemical Identifier Filter.  Enter one or more chemical identifier codes to limit results. Note when filtering by specific TRI chemical identifiers one may not also filter by chemical identifier categories via p_tri_cat. | [optional] |
| **pGhgCat** | **String**| Green House Gas (GHG) Gas Code Category.  Must be used with either a formatted (p_ghg_amt) or custom (p_ghg_any_amt) release amount. | [optional] [enum: ALL, BIOCO2, CH4, CO2, HFC, N2O, NF3, OTHER_L, PFC, SF6] |
| **pGhgAmt** | **String**| Green House Gas (GHG) CO2 Equivalent Formatted Release Amount.  First 2 characters must contain GT (greater than) followed by a number. | [optional] [enum: None, 0, GT0, GT10000, GT25000, GT250000, GT1000000] |
| **pGhgAnyAmt** | **BigDecimal**| Green House Gas (GHG) C02 Equivalent Custom Amount.  The C02E value reported for the provided category, will be greater or equal to the amount provided. | [optional] |
| **pGhgYr** | **String**| Green House Gas (GHG) Reporting Year. (2010 through 2015) | [optional] |
| **pNeiPol** | **String**| National Emissions Inventory (NEI) Pollutant Identifier.  When a pollutant identifer is entered a corresponding formatted amount or custom amount must be entered. | [optional] |
| **pNeiAmt** | **String**| National Emissions Inventory (NEI) Formatted Pollutant Amount.  A formatted value where the 1st two characters must start with GT or LT followed by a number.  Identifies facilities that have a NEI Pollutant Emission  where the supplied value is &gt; or &lt; the pollutant emission amount.   | [optional] [enum: None, 0, GT0, GT10000, GT25000, GT250000, GT1000000] |
| **pNeiAnyAmt** | **BigDecimal**| National Emissions Inventory (NEI) Custom Pollutant Amount.  Only a number can be entered.  Identifies facilities with where the NEI Pollutant Emission Amount is greater than the number entered. | [optional] |
| **pNeiYr** | **String**| National Emissions Inventory (NEI) year:  2014 or 2011 | [optional] |
| **pNeiCat** | **String**| National Emissions Inventory (NEI) Pollutant Category.  When a pollutant category is entered, a corresponding formatted pollutant amount or custom amount must be entered. | [optional] |
| **pPm** | **String**| Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75% | [optional] [enum: NONE, GT5, GT10, GT25, GT50, GT75] |
| **pPd** | **String**| Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile | [optional] [enum: NONE, GT100, GT500, GT1000, GT5000, GT10000, GT20000] |
| **pIco** | **String**| Indian Country Flag.  Enter a \&quot;Y\&quot; or \&quot;N\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] [enum: Y, N] |
| **pHuc** | **String**| 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values. | [optional] |
| **pWbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] |
| **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] |
| **pMed** | **String**| Filter Results by Media. - M &#x3D; RMP (Risk Management Plan) - R &#x3D; RCRA (Hazardous Waste) - S &#x3D; SDWA (Public Drinking Water Systems) - W &#x3D; Water - ALL &#x3D; Water and RCRA and SDWA | [optional] [enum: M, R, S, W, ALL] |
| **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N, NV] |
| **pYsly** | **BigDecimal**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S, A] |
| **pStsl** | **String**| Last Stack Test [within / not within] Specified Date Range Indicator. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pStsly** | **BigDecimal**| Number of years (1 to 5) since date of last stack test. A value of 1 means it has been inspected within the year. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pStsla** | **String**| Stack Last Test Code Filter.  Enter a value to limit results: - A &#x3D; All - E &#x3D; EPA - S &#x3D; State | [optional] [enum: A, E, S] |
| **pStres** | **String**| Air Stack Test Status Description Filter.  Enter one or more test status descriptions to filter results.  Enter multiple values as a comma-delimited list. | [optional] |
| **pSttyp** | **String**| Air Conductor Type Code Filter.  Enter one or more conductor type codes to filter results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] |
| **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] |
| **pTribeid** | **BigDecimal**| Numeric code for tribe (or list of tribes). | [optional] |
| **pTribename** | **String**| Tribe Name Filter.  Enter a single tribe name to filter results. | [optional] |
| **pTribedist** | **BigDecimal**| Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated. | [optional] |
| **pOwop** | **String**| Owner/Operator code filter.  Enter one or more codes to limit results. - CNG - COR - CTG - DIS - FDF - MWD - MXO - NON - POF - SDT - STF - TRB | [optional] |
| **pAgoo** | **String**| Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters. | [optional] [enum: AND, OR] |
| **pIdt1** | **String**| Beginning of date range of most recent facility inspection. | [optional] |
| **pIdt2** | **String**| End of date range of most recent facility inspection. | [optional] |
| **pStdt1** | **String**| Beginning of date range of most recent stack test. | [optional] |
| **pStdt2** | **String**| End of date range of most recent stack test. | [optional] |
| **pPityp** | **String**| Inspection Type: - CAC &#x3D; Corrective Action Inspection - CAV &#x3D; Compliance Assistance Visit - CDI &#x3D; Case Development Inspection - CEI &#x3D; Inspection Inspection - CSE &#x3D; Compliance Schedule Evaluation - FCI &#x3D; Focused Compliance - FRR &#x3D; Financial Record Review - FSD &#x3D; Facility Self Disclosure - FUI &#x3D; Follow-Up Inspection - GME &#x3D; Groundwater Monitoring Evaluation - NRR &#x3D; Non-Financial Record Review - OAM &#x3D; Operation and Maintenance Inspection May contain multiple comma-separated values. | [optional] |
| **pCifdi** | **String**| Compliance issuess found during inspection. | [optional] [enum: Any, true, false, Undetermined] |
| **pPfead1** | **String**| Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] |
| **pPfead2** | **String**| Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] |
| **pPfeat** | **String**| Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list. | [optional] |
| **pPsncq** | **String**| Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z &#x3D; Zero quarters in significant noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in significant noncompliance. | [optional] [enum: GT1, GE1, GT2, GE2, GT4, GE4, GT8, GE8, GT12, GE12] |
| **pPctrack** | **String**| Compliance Tracking Limiter. Provide a keyword to indicate the extent to which data is being entered and effluent exceedances are being identified. - Off - Partial - On | [optional] [enum: false, Partial, true] |
| **pSwpa** | **String**| Source water protection area | [optional] [enum: source water, surface water, ground water, waiting for SSO] |
| **pDes** | **String**| Universe Designation Limiter.  Enter one or more universe designation codes.  Provide multiple values as a comma-delimited list.  Use code \&quot;TSDF\&quot; to return the full enforcement TSDF universe and \&quot;Operating TSDF\&quot; to return the operating TSDF universe. | [optional] |
| **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] [enum: ALL, CONTAINS, EXACT, BEGINS] |
| **pHpvmth** | **String**| Months in high priority violation status out of the previous three years limiter.  Provide a number of months in the past three years.  Results will limited to facilities in high priority violation status during that time.  | [optional] |
| **pRecvio** | **String**| Recent Violation Status Filter.  Enter one or more recent violation codes to limit results.  Provide multiple values as a comma-delimited list. - NO VIOL &#x3D; Selects facilities with no recent violations. - ANY HPV &#x3D; Selects facilities with either addressed or unaddressed high priority violations. - ADDRS-EPA - Select facilities with recent EPA addressed violations. - ADDRS-LOCAL - Select facilities with recent locally addressed violations. - ADDRS-STATE - Select facilities with recent state addressed violations. - UNADDR-EPA - Select facilities with recent EPA unaddressed violations. - UNADDR-LOCAL - Select facilities with recent locally unaddressed violations. - UNADDR-STATE - Select facilities with recent state unaddressed violations. - FRV VIOL &#x3D; Selects facilities with a recent federally reportable violation without a high priority violation. | [optional] |
| **pPollvio** | **String**| Air Pollutant Code For A Recent Violation Filter.  Provide one or more pollutant codes to select facilities with one or more of the entered pollutant codes for a recent air violation.  Provide multiple values as a comma-delimited list. | [optional] |
| **pAr** | **String**| Associated EPA Air Reports Program Filter.  Enter multiple values as a comma-delimited list.  Valid values are: - TRI &#x3D; Toxic Release Inventory. - GHG &#x3D; Green House Gas Reporter. - EIS &#x3D; Emission Inventory System. - CAMD &#x3D; Clean Air Markets Program Reporter. | [optional] |
| **pTriYr** | **String**| Toxic Release Inventory Reporting Year Filter.  Enter one or more year values to filter results by the TRI reporting year.  Provide multiple years as a comma-delimited list. | [optional] |
| **pPidall** | **String**| Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc). | [optional] [enum: Y, N] |
| **pFacIco** | **String**| FRS tribal land code flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land code. | [optional] [enum: Y, N] |
| **pIcoo** | **String**| Indian country search and/or flag.  Enter \&quot;Y\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned. | [optional] |
| **pFacIcos** | **String**| FRS tribal land spatial flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land spatial flag. | [optional] |
| **pEjscreen** | **String**| Enter \&quot;Y\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile. | [optional] |
| **pLimitAddr** | **String**| Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.   | [optional] [enum: Y, N] |
| **pLat** | **BigDecimal**| Latitude location in decimal degrees. | [optional] |
| **pLong** | **BigDecimal**| Longitude location in decimal degrees. | [optional] |
| **pRadius** | **BigDecimal**| Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities. | [optional] |
| **pDecouple** | **String**| Decouple Inspection Code Search Flag.  Enter \&quot;Y\&quot; to search for inspection code types with p_pityp without respect to the date range search provided with p_ysl* parameters. | [optional] [enum: Y, N] |
| **pEjscreenOver80cnt** | **String**| The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11. | [optional] [enum: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] |
| **queryset** | **BigDecimal**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] |
| **responseset** | **BigDecimal**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] |
| **summarylist** | **String**| Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service. | [optional] [enum: Y, N] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |
| **pPrettyPrint** | **BigDecimal**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] |

### Return type

[**AirRestServicesGetFacilityInfoGet200Response**](AirRestServicesGetFacilityInfoGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results will either be an array of Facilities or an array of Clusters. The search will return clusters if the number of facilities returned is greater than the resposeset size, otherwise individual facility records will be returned. |  -  |

<a id="airRestServicesGetFacilityInfoPost"></a>
# **airRestServicesGetFacilityInfoPost**
> AirRestServicesGetFacilityInfoGet200Response airRestServicesGetFacilityInfoPost(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pLcon, pFrs, pReg, pSic, pNcs, pQnc, pPen, pOpst, xmin, ymin, xmax, ymax, pUsmex, pSic2, pSic4, pFa, pAct, pMaj, pMact, pNsps, pNspsm, pProg, pFea, pFeay, pFeaa, pIea, pIeay, pIeaa, pQiv, pNaa, pImpw, pTrep, pTriCat, pTriAmt, pTriAnyAmt, pTriPol, pGhgCat, pGhgAmt, pGhgAnyAmt, pGhgYr, pNeiPol, pNeiAmt, pNeiAnyAmt, pNeiYr, pNeiCat, pPm, pPd, pIco, pHuc, pWbd, pPid, pMed, pYsl, pYsly, pYsla, pStsl, pStsly, pStsla, pStres, pSttyp, pQs, pSfs, pTribeid, pTribename, pTribedist, pOwop, pAgoo, pIdt1, pIdt2, pStdt1, pStdt2, pPityp, pCifdi, pPfead1, pPfead2, pPfeat, pPsncq, pPctrack, pSwpa, pDes, pFntype, pHpvmth, pRecvio, pPollvio, pAr, pTriYr, pPidall, pFacIco, pIcoo, pFacIcos, pEjscreen, pLimitAddr, pLat, pLong, pRadius, pDecouple, pEjscreenOver80cnt, queryset, responseset, summarylist, paramCallback, qcolumns, pPrettyPrint)

Clean Air Act Facility Enhanced Search

Returns either an array of Facilities or an array of Clusters that meet the specified search criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilitiesApi apiInstance = new FacilitiesApi(defaultClient);
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language. - CSV = Facility results formatted as comma delimited file download. - GEOJSON = Facility results formatted as GeoJSON feature collection. - GEOJSONP = Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
    String pFn = "pFn_example"; // String | Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
    String pSa = "pSa_example"; // String | Facility street address. Enter a complete or partial street address.
    String pSa1 = "pSa1_example"; // String | Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa.
    String pCt = "pCt_example"; // String | Facility City Filter. Enter a single case-insensitive city name to filter results.
    String pCo = "pCo_example"; // String | Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
    String pFips = "pFips_example"; // String | FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
    String pSt = "pSt_example"; // String | Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
    String pZip = "pZip_example"; // String | 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values.
    String pLcon = "pLcon_example"; // String | Air Program Local Control Region Code Filter.  Enter one or more local control region codes to filter results.  Provide multiple codes as a comma-delimited list.  Codes where they exist are specific by state.
    String pFrs = "pFrs_example"; // String | Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results.
    String pReg = "01"; // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    String pSic = "pSic_example"; // String | Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4.
    String pNcs = "pNcs_example"; // String | North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
    BigDecimal pQnc = new BigDecimal(78); // BigDecimal | Number of quarters in non-compliance limiter.  Enter an integer value between 1 and 4 to limit results.
    String pPen = "pPen_example"; // String | Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER = No Penalties - ANY = Any Penalty - LEXX = Less than or equal to XX months.  Provide a number in place of XX, e.g. \\\"LE5\\\" for a facility with a penalty within previous 5 months. - GTXX = Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago.
    String pOpst = "pOpst_example"; // String | Operating status filter.  Enter one or more operating status codes to limit results.   Provide multiple codes as a comma-delimited list.
    BigDecimal xmin = new BigDecimal(78); // BigDecimal | Minimum longitude value in decimal degrees.
    BigDecimal ymin = new BigDecimal(78); // BigDecimal | Minimum latitude value in decimal degrees.
    BigDecimal xmax = new BigDecimal(78); // BigDecimal | Maximum longitude value in decimal degrees.
    BigDecimal ymax = new BigDecimal(78); // BigDecimal | Maximum latitude value in decimal degrees.
    String pUsmex = "Y"; // String | US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
    String pSic2 = "pSic2_example"; // String | Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \\\"22\\\" to match all SIC codes beginning with 22.  Use the \\\"%\\\" character within strings to match any SIC values with the pattern.  For example, \\\"2%21\\\" matches 2021, 2121, 2221, etc.
    String pSic4 = "pSic4_example"; // String | Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker.
    String pFa = "pFa_example"; // String | Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values.
    String pAct = "Y"; // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
    String pMaj = "Y"; // String | Major Facility Flag.  Enter Y to restrict results to Major facilities only.
    String pMact = "pMact_example"; // String | CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility.
    String pNsps = "pNsps_example"; // String | Air Programl New Source Performance Standards (NSPS)  Subpart Code Search.  One or more valid Air Program NSPS Program codes cand be passed.  
    String pNspsm = "pNspsm_example"; // String | Air Programl New Source Performance Standards Minors (NSPSM) Subpart Code Search.  One or more valid Air Program NSPSM Subpart codes can be passed.  
    String pProg = "pProg_example"; // String | Air Program Code Filter.  Enter one or more Air program codes to filter results.  Provide multiple values as a comma-delimited list.
    String pFea = "W"; // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
    BigDecimal pFeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
    String pFeaa = "A"; // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
    String pIea = "W"; // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
    BigDecimal pIeay = new BigDecimal("1"); // BigDecimal | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
    String pIeaa = "E"; // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
    String pQiv = "0"; // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    String pNaa = "pNaa_example"; // String | Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas.
    String pImpw = "Y"; // String | Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
    String pTrep = "CURR"; // String | Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR = Current TRI reporter. - NONCURR = Has reported to TRI in the past but not for the current reporting year.
    String pTriCat = "TOTAL"; // String | Toxic Release Inventory Released To Air Chemical Identifier Category Filter.  Enter the chemical identifier category code to limit results. Note when filtering by TRI chemical identifier categories one may not also filter by specific chemical identifiers via p_tri_pol.  You must also specify a release amount using p_tri_amt or p_tri_any_amt. - TOTAL = Total Released to Air - CARC = Total Carcinogens Released to Air - HAP = Total Hazardous Air Pollutants Released to Air
    String pTriAmt = "0"; // String | Toxic Release Inventory Release Amount Filter.  Enter a value in pounds to limit results to facilities releasing this amount or greateer of TRI releases.  Valid values are 0, GT0, GT1000, GT5000, GT10000 and GT50000. Note when filtering by TRI release amounts one may only use either p_tri_amt or p_tri_any_amt.
    BigDecimal pTriAnyAmt = new BigDecimal(78); // BigDecimal | Toxic Release Inventory Release Of Any Kind Above Value Filter.  Enter a value to limit results to facilities releasing this amount or more of TRI releases.  Note when filtering by TRI releases one may only use p_tri_any_amt or p_tri_amt and not both.
    String pTriPol = "pTriPol_example"; // String | Toxic Release Inventory Chemical Identifier Filter.  Enter one or more chemical identifier codes to limit results. Note when filtering by specific TRI chemical identifiers one may not also filter by chemical identifier categories via p_tri_cat.
    String pGhgCat = "ALL"; // String | Green House Gas (GHG) Gas Code Category.  Must be used with either a formatted (p_ghg_amt) or custom (p_ghg_any_amt) release amount.
    String pGhgAmt = "None"; // String | Green House Gas (GHG) CO2 Equivalent Formatted Release Amount.  First 2 characters must contain GT (greater than) followed by a number.
    BigDecimal pGhgAnyAmt = new BigDecimal(78); // BigDecimal | Green House Gas (GHG) C02 Equivalent Custom Amount.  The C02E value reported for the provided category, will be greater or equal to the amount provided.
    String pGhgYr = "pGhgYr_example"; // String | Green House Gas (GHG) Reporting Year. (2010 through 2015)
    String pNeiPol = "pNeiPol_example"; // String | National Emissions Inventory (NEI) Pollutant Identifier.  When a pollutant identifer is entered a corresponding formatted amount or custom amount must be entered.
    String pNeiAmt = "None"; // String | National Emissions Inventory (NEI) Formatted Pollutant Amount.  A formatted value where the 1st two characters must start with GT or LT followed by a number.  Identifies facilities that have a NEI Pollutant Emission  where the supplied value is > or < the pollutant emission amount.  
    BigDecimal pNeiAnyAmt = new BigDecimal(78); // BigDecimal | National Emissions Inventory (NEI) Custom Pollutant Amount.  Only a number can be entered.  Identifies facilities with where the NEI Pollutant Emission Amount is greater than the number entered.
    String pNeiYr = "pNeiYr_example"; // String | National Emissions Inventory (NEI) year:  2014 or 2011
    String pNeiCat = "pNeiCat_example"; // String | National Emissions Inventory (NEI) Pollutant Category.  When a pollutant category is entered, a corresponding formatted pollutant amount or custom amount must be entered.
    String pPm = "NONE"; // String | Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE = 0% - GT5 = greater than 5% - GT10 = greater than 10% - GT25 = greater than 25% - GT50 = greater than 50% - GT75 = greater than 75%
    String pPd = "NONE"; // String | Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE = 0 population density per square mile - GT100 = More than 100 population density per square mile - GT500 = More than 500 population density per square mile - GT1000 = More than 1000 population density per square mile - GT5000 = More than 5000 population density per square mile - GT10000 = More than 10000 population density per square mile - GT20000 = More than 20000 population density per square mile
    String pIco = "Y"; // String | Indian Country Flag.  Enter a \\\"Y\\\" or \\\"N\\\" to restrict searches to facilities inside or outside Indian Country.
    String pHuc = "pHuc_example"; // String | 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
    String pWbd = "pWbd_example"; // String | 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    String pPid = "pPid_example"; // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    String pMed = "M"; // String | Filter Results by Media. - M = RMP (Risk Management Plan) - R = RCRA (Hazardous Waste) - S = SDWA (Public Drinking Water Systems) - W = Water - ALL = Water and RCRA and SDWA
    String pYsl = "W"; // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
    BigDecimal pYsly = new BigDecimal("1"); // BigDecimal | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
    String pYsla = "E"; // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
    String pStsl = "W"; // String | Last Stack Test [within / not within] Specified Date Range Indicator. - W = within date range - N = not within date range
    BigDecimal pStsly = new BigDecimal("1"); // BigDecimal | Number of years (1 to 5) since date of last stack test. A value of 1 means it has been inspected within the year.
    String pStsla = "A"; // String | Stack Last Test Code Filter.  Enter a value to limit results: - A = All - E = EPA - S = State
    String pStres = "pStres_example"; // String | Air Stack Test Status Description Filter.  Enter one or more test status descriptions to filter results.  Enter multiple values as a comma-delimited list.
    String pSttyp = "pSttyp_example"; // String | Air Conductor Type Code Filter.  Enter one or more conductor type codes to filter results.  Provide multiple values as a comma-delimited list.
    String pQs = "pQs_example"; // String | Quick Search. Allows entry for city, state, and/or zip code.
    String pSfs = "pSfs_example"; // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
    BigDecimal pTribeid = new BigDecimal(78); // BigDecimal | Numeric code for tribe (or list of tribes).
    String pTribename = "pTribename_example"; // String | Tribe Name Filter.  Enter a single tribe name to filter results.
    BigDecimal pTribedist = new BigDecimal(78); // BigDecimal | Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
    String pOwop = "pOwop_example"; // String | Owner/Operator code filter.  Enter one or more codes to limit results. - CNG - COR - CTG - DIS - FDF - MWD - MXO - NON - POF - SDT - STF - TRB
    String pAgoo = "AND"; // String | Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
    String pIdt1 = "pIdt1_example"; // String | Beginning of date range of most recent facility inspection.
    String pIdt2 = "pIdt2_example"; // String | End of date range of most recent facility inspection.
    String pStdt1 = "pStdt1_example"; // String | Beginning of date range of most recent stack test.
    String pStdt2 = "pStdt2_example"; // String | End of date range of most recent stack test.
    String pPityp = "pPityp_example"; // String | Inspection Type: - CAC = Corrective Action Inspection - CAV = Compliance Assistance Visit - CDI = Case Development Inspection - CEI = Inspection Inspection - CSE = Compliance Schedule Evaluation - FCI = Focused Compliance - FRR = Financial Record Review - FSD = Facility Self Disclosure - FUI = Follow-Up Inspection - GME = Groundwater Monitoring Evaluation - NRR = Non-Financial Record Review - OAM = Operation and Maintenance Inspection May contain multiple comma-separated values.
    String pCifdi = "Any"; // String | Compliance issuess found during inspection.
    String pPfead1 = "pPfead1_example"; // String | Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    String pPfead2 = "pPfead2_example"; // String | Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    String pPfeat = "pPfeat_example"; // String | Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
    String pPsncq = "GT1"; // String | Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z = Zero quarters in significant noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in significant noncompliance.
    String pPctrack = "false"; // String | Compliance Tracking Limiter. Provide a keyword to indicate the extent to which data is being entered and effluent exceedances are being identified. - Off - Partial - On
    String pSwpa = "source water"; // String | Source water protection area
    String pDes = "pDes_example"; // String | Universe Designation Limiter.  Enter one or more universe designation codes.  Provide multiple values as a comma-delimited list.  Use code \\\"TSDF\\\" to return the full enforcement TSDF universe and \\\"Operating TSDF\\\" to return the operating TSDF universe.
    String pFntype = "ALL"; // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
    String pHpvmth = "pHpvmth_example"; // String | Months in high priority violation status out of the previous three years limiter.  Provide a number of months in the past three years.  Results will limited to facilities in high priority violation status during that time. 
    String pRecvio = "pRecvio_example"; // String | Recent Violation Status Filter.  Enter one or more recent violation codes to limit results.  Provide multiple values as a comma-delimited list. - NO VIOL = Selects facilities with no recent violations. - ANY HPV = Selects facilities with either addressed or unaddressed high priority violations. - ADDRS-EPA - Select facilities with recent EPA addressed violations. - ADDRS-LOCAL - Select facilities with recent locally addressed violations. - ADDRS-STATE - Select facilities with recent state addressed violations. - UNADDR-EPA - Select facilities with recent EPA unaddressed violations. - UNADDR-LOCAL - Select facilities with recent locally unaddressed violations. - UNADDR-STATE - Select facilities with recent state unaddressed violations. - FRV VIOL = Selects facilities with a recent federally reportable violation without a high priority violation.
    String pPollvio = "pPollvio_example"; // String | Air Pollutant Code For A Recent Violation Filter.  Provide one or more pollutant codes to select facilities with one or more of the entered pollutant codes for a recent air violation.  Provide multiple values as a comma-delimited list.
    String pAr = "pAr_example"; // String | Associated EPA Air Reports Program Filter.  Enter multiple values as a comma-delimited list.  Valid values are: - TRI = Toxic Release Inventory. - GHG = Green House Gas Reporter. - EIS = Emission Inventory System. - CAMD = Clean Air Markets Program Reporter.
    String pTriYr = "pTriYr_example"; // String | Toxic Release Inventory Reporting Year Filter.  Enter one or more year values to filter results by the TRI reporting year.  Provide multiple years as a comma-delimited list.
    String pPidall = "Y"; // String | Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc).
    String pFacIco = "Y"; // String | FRS tribal land code flag.  Enter \\\"Y\\\" or \\\"N\\\" to include or exclude facilities based on FRS tribal land code.
    String pIcoo = "pIcoo_example"; // String | Indian country search and/or flag.  Enter \\\"Y\\\" to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
    String pFacIcos = "pFacIcos_example"; // String | FRS tribal land spatial flag.  Enter \\\"Y\\\" or \\\"N\\\" to include or exclude facilities based on FRS tribal land spatial flag.
    String pEjscreen = "pEjscreen_example"; // String | Enter \\\"Y\\\" to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
    String pLimitAddr = "Y"; // String | Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
    BigDecimal pLat = new BigDecimal(78); // BigDecimal | Latitude location in decimal degrees.
    BigDecimal pLong = new BigDecimal(78); // BigDecimal | Longitude location in decimal degrees.
    BigDecimal pRadius = new BigDecimal(78); // BigDecimal | Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
    String pDecouple = "Y"; // String | Decouple Inspection Code Search Flag.  Enter \\\"Y\\\" to search for inspection code types with p_pityp without respect to the date range search provided with p_ysl* parameters.
    String pEjscreenOver80cnt = "1"; // String | The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
    BigDecimal queryset = new BigDecimal(78); // BigDecimal | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    BigDecimal responseset = new BigDecimal(78); // BigDecimal | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    String summarylist = "Y"; // String | Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      AirRestServicesGetFacilityInfoGet200Response result = apiInstance.airRestServicesGetFacilityInfoPost(output, pFn, pSa, pSa1, pCt, pCo, pFips, pSt, pZip, pLcon, pFrs, pReg, pSic, pNcs, pQnc, pPen, pOpst, xmin, ymin, xmax, ymax, pUsmex, pSic2, pSic4, pFa, pAct, pMaj, pMact, pNsps, pNspsm, pProg, pFea, pFeay, pFeaa, pIea, pIeay, pIeaa, pQiv, pNaa, pImpw, pTrep, pTriCat, pTriAmt, pTriAnyAmt, pTriPol, pGhgCat, pGhgAmt, pGhgAnyAmt, pGhgYr, pNeiPol, pNeiAmt, pNeiAnyAmt, pNeiYr, pNeiCat, pPm, pPd, pIco, pHuc, pWbd, pPid, pMed, pYsl, pYsly, pYsla, pStsl, pStsly, pStsla, pStres, pSttyp, pQs, pSfs, pTribeid, pTribename, pTribedist, pOwop, pAgoo, pIdt1, pIdt2, pStdt1, pStdt2, pPityp, pCifdi, pPfead1, pPfead2, pPfeat, pPsncq, pPctrack, pSwpa, pDes, pFntype, pHpvmth, pRecvio, pPollvio, pAr, pTriYr, pPidall, pFacIco, pIcoo, pFacIcos, pEjscreen, pLimitAddr, pLat, pLong, pRadius, pDecouple, pEjscreenOver80cnt, queryset, responseset, summarylist, paramCallback, qcolumns, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilitiesApi#airRestServicesGetFacilityInfoPost");
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
| **pLcon** | **String**| Air Program Local Control Region Code Filter.  Enter one or more local control region codes to filter results.  Provide multiple codes as a comma-delimited list.  Codes where they exist are specific by state. | [optional] |
| **pFrs** | **String**| Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results. | [optional] |
| **pReg** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] [enum: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10] |
| **pSic** | **String**| Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4. | [optional] |
| **pNcs** | **String**| North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values. | [optional] |
| **pQnc** | **BigDecimal**| Number of quarters in non-compliance limiter.  Enter an integer value between 1 and 4 to limit results. | [optional] |
| **pPen** | **String**| Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER &#x3D; No Penalties - ANY &#x3D; Any Penalty - LEXX &#x3D; Less than or equal to XX months.  Provide a number in place of XX, e.g. \\\&quot;LE5\\\&quot; for a facility with a penalty within previous 5 months. - GTXX &#x3D; Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago. | [optional] |
| **pOpst** | **String**| Operating status filter.  Enter one or more operating status codes to limit results.   Provide multiple codes as a comma-delimited list. | [optional] |
| **xmin** | **BigDecimal**| Minimum longitude value in decimal degrees. | [optional] |
| **ymin** | **BigDecimal**| Minimum latitude value in decimal degrees. | [optional] |
| **xmax** | **BigDecimal**| Maximum longitude value in decimal degrees. | [optional] |
| **ymax** | **BigDecimal**| Maximum latitude value in decimal degrees. | [optional] |
| **pUsmex** | **String**| US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border. | [optional] [enum: Y, N] |
| **pSic2** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \\\&quot;22\\\&quot; to match all SIC codes beginning with 22.  Use the \\\&quot;%\\\&quot; character within strings to match any SIC values with the pattern.  For example, \\\&quot;2%21\\\&quot; matches 2021, 2121, 2221, etc. | [optional] |
| **pSic4** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker. | [optional] |
| **pFa** | **String**| Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values. | [optional] |
| **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits. | [optional] [enum: Y, N, A] |
| **pMaj** | **String**| Major Facility Flag.  Enter Y to restrict results to Major facilities only. | [optional] [enum: Y, N] |
| **pMact** | **String**| CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility. | [optional] |
| **pNsps** | **String**| Air Programl New Source Performance Standards (NSPS)  Subpart Code Search.  One or more valid Air Program NSPS Program codes cand be passed.   | [optional] |
| **pNspsm** | **String**| Air Programl New Source Performance Standards Minors (NSPSM) Subpart Code Search.  One or more valid Air Program NSPSM Subpart codes can be passed.   | [optional] |
| **pProg** | **String**| Air Program Code Filter.  Enter one or more Air program codes to filter results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pFeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] [enum: A, E, S] |
| **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pIeay** | **BigDecimal**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S] |
| **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] [enum: 0, GT1, GT2, GT4, GT8, 12] |
| **pNaa** | **String**| Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas. | [optional] |
| **pImpw** | **String**| Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database. | [optional] [enum: Y, N] |
| **pTrep** | **String**| Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year. | [optional] [enum: CURR, NOTCURR] |
| **pTriCat** | **String**| Toxic Release Inventory Released To Air Chemical Identifier Category Filter.  Enter the chemical identifier category code to limit results. Note when filtering by TRI chemical identifier categories one may not also filter by specific chemical identifiers via p_tri_pol.  You must also specify a release amount using p_tri_amt or p_tri_any_amt. - TOTAL &#x3D; Total Released to Air - CARC &#x3D; Total Carcinogens Released to Air - HAP &#x3D; Total Hazardous Air Pollutants Released to Air | [optional] [enum: TOTAL, CARC, HAP] |
| **pTriAmt** | **String**| Toxic Release Inventory Release Amount Filter.  Enter a value in pounds to limit results to facilities releasing this amount or greateer of TRI releases.  Valid values are 0, GT0, GT1000, GT5000, GT10000 and GT50000. Note when filtering by TRI release amounts one may only use either p_tri_amt or p_tri_any_amt. | [optional] [enum: 0, GT0, GT1000, GT5000, GT10000, GT50000] |
| **pTriAnyAmt** | **BigDecimal**| Toxic Release Inventory Release Of Any Kind Above Value Filter.  Enter a value to limit results to facilities releasing this amount or more of TRI releases.  Note when filtering by TRI releases one may only use p_tri_any_amt or p_tri_amt and not both. | [optional] |
| **pTriPol** | **String**| Toxic Release Inventory Chemical Identifier Filter.  Enter one or more chemical identifier codes to limit results. Note when filtering by specific TRI chemical identifiers one may not also filter by chemical identifier categories via p_tri_cat. | [optional] |
| **pGhgCat** | **String**| Green House Gas (GHG) Gas Code Category.  Must be used with either a formatted (p_ghg_amt) or custom (p_ghg_any_amt) release amount. | [optional] [enum: ALL, BIOCO2, CH4, CO2, HFC, N2O, NF3, OTHER_L, PFC, SF6] |
| **pGhgAmt** | **String**| Green House Gas (GHG) CO2 Equivalent Formatted Release Amount.  First 2 characters must contain GT (greater than) followed by a number. | [optional] [enum: None, 0, GT0, GT10000, GT25000, GT250000, GT1000000] |
| **pGhgAnyAmt** | **BigDecimal**| Green House Gas (GHG) C02 Equivalent Custom Amount.  The C02E value reported for the provided category, will be greater or equal to the amount provided. | [optional] |
| **pGhgYr** | **String**| Green House Gas (GHG) Reporting Year. (2010 through 2015) | [optional] |
| **pNeiPol** | **String**| National Emissions Inventory (NEI) Pollutant Identifier.  When a pollutant identifer is entered a corresponding formatted amount or custom amount must be entered. | [optional] |
| **pNeiAmt** | **String**| National Emissions Inventory (NEI) Formatted Pollutant Amount.  A formatted value where the 1st two characters must start with GT or LT followed by a number.  Identifies facilities that have a NEI Pollutant Emission  where the supplied value is &gt; or &lt; the pollutant emission amount.   | [optional] [enum: None, 0, GT0, GT10000, GT25000, GT250000, GT1000000] |
| **pNeiAnyAmt** | **BigDecimal**| National Emissions Inventory (NEI) Custom Pollutant Amount.  Only a number can be entered.  Identifies facilities with where the NEI Pollutant Emission Amount is greater than the number entered. | [optional] |
| **pNeiYr** | **String**| National Emissions Inventory (NEI) year:  2014 or 2011 | [optional] |
| **pNeiCat** | **String**| National Emissions Inventory (NEI) Pollutant Category.  When a pollutant category is entered, a corresponding formatted pollutant amount or custom amount must be entered. | [optional] |
| **pPm** | **String**| Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75% | [optional] [enum: NONE, GT5, GT10, GT25, GT50, GT75] |
| **pPd** | **String**| Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile | [optional] [enum: NONE, GT100, GT500, GT1000, GT5000, GT10000, GT20000] |
| **pIco** | **String**| Indian Country Flag.  Enter a \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] [enum: Y, N] |
| **pHuc** | **String**| 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values. | [optional] |
| **pWbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] |
| **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] |
| **pMed** | **String**| Filter Results by Media. - M &#x3D; RMP (Risk Management Plan) - R &#x3D; RCRA (Hazardous Waste) - S &#x3D; SDWA (Public Drinking Water Systems) - W &#x3D; Water - ALL &#x3D; Water and RCRA and SDWA | [optional] [enum: M, R, S, W, ALL] |
| **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N, NV] |
| **pYsly** | **BigDecimal**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] [enum: E, S, A] |
| **pStsl** | **String**| Last Stack Test [within / not within] Specified Date Range Indicator. - W &#x3D; within date range - N &#x3D; not within date range | [optional] [enum: W, N] |
| **pStsly** | **BigDecimal**| Number of years (1 to 5) since date of last stack test. A value of 1 means it has been inspected within the year. | [optional] [enum: 1, 2, 3, 4, 5] |
| **pStsla** | **String**| Stack Last Test Code Filter.  Enter a value to limit results: - A &#x3D; All - E &#x3D; EPA - S &#x3D; State | [optional] [enum: A, E, S] |
| **pStres** | **String**| Air Stack Test Status Description Filter.  Enter one or more test status descriptions to filter results.  Enter multiple values as a comma-delimited list. | [optional] |
| **pSttyp** | **String**| Air Conductor Type Code Filter.  Enter one or more conductor type codes to filter results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] |
| **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] |
| **pTribeid** | **BigDecimal**| Numeric code for tribe (or list of tribes). | [optional] |
| **pTribename** | **String**| Tribe Name Filter.  Enter a single tribe name to filter results. | [optional] |
| **pTribedist** | **BigDecimal**| Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated. | [optional] |
| **pOwop** | **String**| Owner/Operator code filter.  Enter one or more codes to limit results. - CNG - COR - CTG - DIS - FDF - MWD - MXO - NON - POF - SDT - STF - TRB | [optional] |
| **pAgoo** | **String**| Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters. | [optional] [enum: AND, OR] |
| **pIdt1** | **String**| Beginning of date range of most recent facility inspection. | [optional] |
| **pIdt2** | **String**| End of date range of most recent facility inspection. | [optional] |
| **pStdt1** | **String**| Beginning of date range of most recent stack test. | [optional] |
| **pStdt2** | **String**| End of date range of most recent stack test. | [optional] |
| **pPityp** | **String**| Inspection Type: - CAC &#x3D; Corrective Action Inspection - CAV &#x3D; Compliance Assistance Visit - CDI &#x3D; Case Development Inspection - CEI &#x3D; Inspection Inspection - CSE &#x3D; Compliance Schedule Evaluation - FCI &#x3D; Focused Compliance - FRR &#x3D; Financial Record Review - FSD &#x3D; Facility Self Disclosure - FUI &#x3D; Follow-Up Inspection - GME &#x3D; Groundwater Monitoring Evaluation - NRR &#x3D; Non-Financial Record Review - OAM &#x3D; Operation and Maintenance Inspection May contain multiple comma-separated values. | [optional] |
| **pCifdi** | **String**| Compliance issuess found during inspection. | [optional] [enum: Any, true, false, Undetermined] |
| **pPfead1** | **String**| Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] |
| **pPfead2** | **String**| Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] |
| **pPfeat** | **String**| Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list. | [optional] |
| **pPsncq** | **String**| Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z &#x3D; Zero quarters in significant noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in significant noncompliance. | [optional] [enum: GT1, GE1, GT2, GE2, GT4, GE4, GT8, GE8, GT12, GE12] |
| **pPctrack** | **String**| Compliance Tracking Limiter. Provide a keyword to indicate the extent to which data is being entered and effluent exceedances are being identified. - Off - Partial - On | [optional] [enum: false, Partial, true] |
| **pSwpa** | **String**| Source water protection area | [optional] [enum: source water, surface water, ground water, waiting for SSO] |
| **pDes** | **String**| Universe Designation Limiter.  Enter one or more universe designation codes.  Provide multiple values as a comma-delimited list.  Use code \\\&quot;TSDF\\\&quot; to return the full enforcement TSDF universe and \\\&quot;Operating TSDF\\\&quot; to return the operating TSDF universe. | [optional] |
| **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] [enum: ALL, CONTAINS, EXACT, BEGINS] |
| **pHpvmth** | **String**| Months in high priority violation status out of the previous three years limiter.  Provide a number of months in the past three years.  Results will limited to facilities in high priority violation status during that time.  | [optional] |
| **pRecvio** | **String**| Recent Violation Status Filter.  Enter one or more recent violation codes to limit results.  Provide multiple values as a comma-delimited list. - NO VIOL &#x3D; Selects facilities with no recent violations. - ANY HPV &#x3D; Selects facilities with either addressed or unaddressed high priority violations. - ADDRS-EPA - Select facilities with recent EPA addressed violations. - ADDRS-LOCAL - Select facilities with recent locally addressed violations. - ADDRS-STATE - Select facilities with recent state addressed violations. - UNADDR-EPA - Select facilities with recent EPA unaddressed violations. - UNADDR-LOCAL - Select facilities with recent locally unaddressed violations. - UNADDR-STATE - Select facilities with recent state unaddressed violations. - FRV VIOL &#x3D; Selects facilities with a recent federally reportable violation without a high priority violation. | [optional] |
| **pPollvio** | **String**| Air Pollutant Code For A Recent Violation Filter.  Provide one or more pollutant codes to select facilities with one or more of the entered pollutant codes for a recent air violation.  Provide multiple values as a comma-delimited list. | [optional] |
| **pAr** | **String**| Associated EPA Air Reports Program Filter.  Enter multiple values as a comma-delimited list.  Valid values are: - TRI &#x3D; Toxic Release Inventory. - GHG &#x3D; Green House Gas Reporter. - EIS &#x3D; Emission Inventory System. - CAMD &#x3D; Clean Air Markets Program Reporter. | [optional] |
| **pTriYr** | **String**| Toxic Release Inventory Reporting Year Filter.  Enter one or more year values to filter results by the TRI reporting year.  Provide multiple years as a comma-delimited list. | [optional] |
| **pPidall** | **String**| Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc). | [optional] [enum: Y, N] |
| **pFacIco** | **String**| FRS tribal land code flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land code. | [optional] [enum: Y, N] |
| **pIcoo** | **String**| Indian country search and/or flag.  Enter \\\&quot;Y\\\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned. | [optional] |
| **pFacIcos** | **String**| FRS tribal land spatial flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land spatial flag. | [optional] |
| **pEjscreen** | **String**| Enter \\\&quot;Y\\\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile. | [optional] |
| **pLimitAddr** | **String**| Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.   | [optional] [enum: Y, N] |
| **pLat** | **BigDecimal**| Latitude location in decimal degrees. | [optional] |
| **pLong** | **BigDecimal**| Longitude location in decimal degrees. | [optional] |
| **pRadius** | **BigDecimal**| Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities. | [optional] |
| **pDecouple** | **String**| Decouple Inspection Code Search Flag.  Enter \\\&quot;Y\\\&quot; to search for inspection code types with p_pityp without respect to the date range search provided with p_ysl* parameters. | [optional] [enum: Y, N] |
| **pEjscreenOver80cnt** | **String**| The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11. | [optional] [enum: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] |
| **queryset** | **BigDecimal**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] |
| **responseset** | **BigDecimal**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] |
| **summarylist** | **String**| Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service. | [optional] [enum: Y, N] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |
| **pPrettyPrint** | **BigDecimal**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] |

### Return type

[**AirRestServicesGetFacilityInfoGet200Response**](AirRestServicesGetFacilityInfoGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results will either be an array of Facilities or an array of Clusters. The search will return clusters if the number of facilities returned is greater than the resposeset size, otherwise individual facility records will be returned. |  -  |

<a id="airRestServicesGetGeojsonGet"></a>
# **airRestServicesGetGeojsonGet**
> AirRestServicesGetGeojsonGet200Response airRestServicesGetGeojsonGet(qid, output, paramCallback, newsort, descending, qcolumns, pPrettyPrint)

Clean Air Act GeoJSON Service

Based on the QID obtained from a get_facilities or get_facility_info query, return GeoJSON of the facilities found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilitiesApi apiInstance = new FacilitiesApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - GEOJSON = Facility results formatted as GeoJSON feature collection (default). - GEOJSONP = Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    BigDecimal newsort = new BigDecimal(78); // BigDecimal | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
    String descending = "Y"; // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      AirRestServicesGetGeojsonGet200Response result = apiInstance.airRestServicesGetGeojsonGet(qid, output, paramCallback, newsort, descending, qcolumns, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilitiesApi#airRestServicesGetGeojsonGet");
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

[**AirRestServicesGetGeojsonGet200Response**](AirRestServicesGetGeojsonGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are formatted as a GeoJSON feature collection. |  -  |

<a id="airRestServicesGetGeojsonPost"></a>
# **airRestServicesGetGeojsonPost**
> AirRestServicesGetGeojsonGet200Response airRestServicesGetGeojsonPost(qid, output, paramCallback, newsort, descending, qcolumns, pPrettyPrint)

Clean Air Act GeoJSON Service

Based on the QID obtained from a get_facilities or get_facility_info query, return GeoJSON of the facilities found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilitiesApi apiInstance = new FacilitiesApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - GEOJSON = Facility results formatted as GeoJSON feature collection (default). - GEOJSONP = Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    BigDecimal newsort = new BigDecimal(78); // BigDecimal | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
    String descending = "Y"; // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      AirRestServicesGetGeojsonGet200Response result = apiInstance.airRestServicesGetGeojsonPost(qid, output, paramCallback, newsort, descending, qcolumns, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilitiesApi#airRestServicesGetGeojsonPost");
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

[**AirRestServicesGetGeojsonGet200Response**](AirRestServicesGetGeojsonGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are formatted as a GeoJSON feature collection. |  -  |

<a id="airRestServicesGetInfoClustersGet"></a>
# **airRestServicesGetInfoClustersGet**
> File airRestServicesGetInfoClustersGet(pQid, output, pPrettyPrint)

Clean Air Act Info Clusters Service

Based on the QID obtained from a clustered get_facility_info query, download cluster facility information as either a CSV or GEOJSON file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilitiesApi apiInstance = new FacilitiesApi(defaultClient);
    String pQid = "pQid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default). - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      File result = apiInstance.airRestServicesGetInfoClustersGet(pQid, output, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilitiesApi#airRestServicesGetInfoClustersGet");
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

<a id="airRestServicesGetInfoClustersPost"></a>
# **airRestServicesGetInfoClustersPost**
> File airRestServicesGetInfoClustersPost(pQid, output, pPrettyPrint)

Clean Air Act Info Clusters Service

Based on the QID obtained from a clustered get_facility_info query, download cluster facility information as either a CSV or GEOJSON file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilitiesApi apiInstance = new FacilitiesApi(defaultClient);
    String pQid = "pQid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default). - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    try {
      File result = apiInstance.airRestServicesGetInfoClustersPost(pQid, output, pPrettyPrint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilitiesApi#airRestServicesGetInfoClustersPost");
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

<a id="airRestServicesGetMapGet"></a>
# **airRestServicesGetMapGet**
> AirRestServicesGetMapGet200Response airRestServicesGetMapGet(qid, pId, output, paramCallback, tablelist, c1Lat, c1Long, c2Lat, c2Long)

Clean Air Act Map Service

The purpose of the GET_MAP service is to display facility coordinates and facility clusters related to a get_facilities facility query. Currently, the maximum number of coordinates returned is 500. GET_MAP performs automatic clustering at the state, county, and zip code levels to maximize the number of coordinates returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilitiesApi apiInstance = new FacilitiesApi(defaultClient);
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
      AirRestServicesGetMapGet200Response result = apiInstance.airRestServicesGetMapGet(qid, pId, output, paramCallback, tablelist, c1Lat, c1Long, c2Lat, c2Long);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilitiesApi#airRestServicesGetMapGet");
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

[**AirRestServicesGetMapGet200Response**](AirRestServicesGetMapGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are either an array of State, County, Zip Code facility cluster map coordinates or individual facility coordinates.  Coordinates provided are in WGS84. |  -  |

<a id="airRestServicesGetMapPost"></a>
# **airRestServicesGetMapPost**
> AirRestServicesGetMapGet200Response airRestServicesGetMapPost(qid, pId, output, paramCallback, tablelist, c1Lat, c1Long, c2Lat, c2Long)

Clean Air Act Map Service

The purpose of the GET_MAP service is to display facility coordinates and facility clusters related to a get_facilities facility query. Currently, the maximum number of coordinates returned is 500. GET_MAP performs automatic clustering at the state, county, and zip code levels to maximize the number of coordinates returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilitiesApi apiInstance = new FacilitiesApi(defaultClient);
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
      AirRestServicesGetMapGet200Response result = apiInstance.airRestServicesGetMapPost(qid, pId, output, paramCallback, tablelist, c1Lat, c1Long, c2Lat, c2Long);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilitiesApi#airRestServicesGetMapPost");
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

[**AirRestServicesGetMapGet200Response**](AirRestServicesGetMapGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are either an array of State, County, Zip Code facility cluster map coordinates or individual facility coordinates.  Coordinates provided are in WGS84. |  -  |

<a id="airRestServicesGetQidGet"></a>
# **airRestServicesGetQidGet**
> AirRestServicesGetQidGet200Response airRestServicesGetQidGet(qid, output, pageno, paramCallback, newsort, descending, qcolumns)

Clean Air Act Search by Query ID

GET_QID is passed with a query ID corresponding to a previously run get_facilities query. It then returns a Facility object containing all matching facilities. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilitiesApi apiInstance = new FacilitiesApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    BigDecimal pageno = new BigDecimal("1.0"); // BigDecimal | Indicates the number of the page to display. It is used only when the results are paginated.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    BigDecimal newsort = new BigDecimal(78); // BigDecimal | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
    String descending = "Y"; // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    try {
      AirRestServicesGetQidGet200Response result = apiInstance.airRestServicesGetQidGet(qid, output, pageno, paramCallback, newsort, descending, qcolumns);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilitiesApi#airRestServicesGetQidGet");
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

[**AirRestServicesGetQidGet200Response**](AirRestServicesGetQidGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are an array (page)  of CAA (ICIS Air) Facilities with the number of facilities equal to the responseset (page size). |  -  |

<a id="airRestServicesGetQidPost"></a>
# **airRestServicesGetQidPost**
> AirRestServicesGetQidGet200Response airRestServicesGetQidPost(qid, output, pageno, paramCallback, newsort, descending, qcolumns)

Clean Air Act Search by Query ID

GET_QID is passed with a query ID corresponding to a previously run get_facilities query. It then returns a Facility object containing all matching facilities. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    FacilitiesApi apiInstance = new FacilitiesApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    BigDecimal pageno = new BigDecimal("1.0"); // BigDecimal | Indicates the number of the page to display. It is used only when the results are paginated.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    BigDecimal newsort = new BigDecimal(78); // BigDecimal | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
    String descending = "Y"; // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    try {
      AirRestServicesGetQidGet200Response result = apiInstance.airRestServicesGetQidPost(qid, output, pageno, paramCallback, newsort, descending, qcolumns);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilitiesApi#airRestServicesGetQidPost");
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

[**AirRestServicesGetQidGet200Response**](AirRestServicesGetQidGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are an array (page)  of CAA (ICIS Air) Facilities with the number of facilities equal to the responseset (page size). |  -  |

