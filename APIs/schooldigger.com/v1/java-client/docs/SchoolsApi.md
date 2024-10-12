# SchoolsApi

All URIs are relative to *https://api.schooldigger.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**schoolsGetAllSchools**](SchoolsApi.md#schoolsGetAllSchools) | **GET** /v1/schools | Returns a list of schools |
| [**schoolsGetSchool10**](SchoolsApi.md#schoolsGetSchool10) | **GET** /v1/schools/{id} | Returns a detailed record for one school |


<a id="schoolsGetAllSchools"></a>
# **schoolsGetAllSchools**
> APISchoolList schoolsGetAllSchools(st, appID, appKey, q, qSearchSchoolNameOnly, districtID, level, city, zip, isMagnet, isCharter, isVirtual, isTitleI, isTitleISchoolwide, nearLatitude, nearLongitude, boundaryAddress, distanceMiles, isInBoundaryOnly, boxLatitudeNW, boxLongitudeNW, boxLatitudeSE, boxLongitudeSE, page, perPage, sortBy, includeUnrankedSchoolsInRankSort)

Returns a list of schools

Search the SchoolDigger database for schools. You may use any combination of criteria as query parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.schooldigger.com");

    SchoolsApi apiInstance = new SchoolsApi(defaultClient);
    String st = "st_example"; // String | Two character state (e.g. 'CA') - required
    String appID = "appID_example"; // String | Your API app id
    String appKey = "appKey_example"; // String | Your API app key
    String q = "q_example"; // String | Search term - note: will match school name or city (optional)
    Boolean qSearchSchoolNameOnly = true; // Boolean | For parameter 'q', only search school names instead of school and city (optional)
    String districtID = "districtID_example"; // String | Search for schools within this district (7 digit district id) (optional)
    String level = "level_example"; // String | Search for schools at this level. Valid values: 'Elementary', 'Middle', 'High', 'Alt', 'Public', 'Private' (optional). 'Public' returns all Elementary, Middle, High and Alternative schools
    String city = "city_example"; // String | Search for schools in this city (optional)
    String zip = "zip_example"; // String | Search for schools in this 5-digit zip code (optional)
    Boolean isMagnet = true; // Boolean | True = return only magnet schools, False = return only non-magnet schools (optional) (Pro, Enterprise API levels only)
    Boolean isCharter = true; // Boolean | True = return only charter schools, False = return only non-charter schools (optional) (Pro, Enterprise API levels only)
    Boolean isVirtual = true; // Boolean | True = return only virtual schools, False = return only non-virtual schools (optional) (Pro, Enterprise API levels only)
    Boolean isTitleI = true; // Boolean | True = return only Title I schools, False = return only non-Title I schools (optional) (Pro, Enterprise API levels only)
    Boolean isTitleISchoolwide = true; // Boolean | True = return only Title I school-wide schools, False = return only non-Title I school-wide schools (optional) (Pro, Enterprise API levels only)
    Double nearLatitude = 3.4D; // Double | Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. 44.982560) (optional) (Pro, Enterprise API levels only. Enterprise API level will flag schools that include lat/long in its attendance boundary.)
    Double nearLongitude = 3.4D; // Double | Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. -124.289185) (optional) (Pro, Enterprise API levels only. Enterprise API level will flag schools that include lat/long in its attendance boundary.)
    String boundaryAddress = "boundaryAddress_example"; // String | Full U.S. address: flag returned schools that include this address in its attendance boundary. Example: '123 Main St. AnyTown CA 90001' (optional) (Enterprise API level only) IMPORTANT NOTE: If you have the lat/long of the address, use nearLatitude and nearLongitude instead for much faster response times
    Integer distanceMiles = 56; // Integer | Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (Default 5 miles) (optional) (Pro, Enterprise API levels only)
    Boolean isInBoundaryOnly = true; // Boolean | Return only the schools that include given location (nearLatitude/nearLongitude) or (boundaryAddress) in its attendance boundary (Enterprise API level only)
    Double boxLatitudeNW = 3.4D; // Double | Search for schools within a 'box' defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional)
    Double boxLongitudeNW = 3.4D; // Double | Search for schools within a 'box' defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional)
    Double boxLatitudeSE = 3.4D; // Double | Search for schools within a 'box' defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional)
    Double boxLongitudeSE = 3.4D; // Double | Search for schools within a 'box' defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional)
    Integer page = 56; // Integer | Page number to retrieve (optional, default: 1)
    Integer perPage = 56; // Integer | Number of schools to retrieve on a page (50 max) (optional, default: 10)
    String sortBy = "sortBy_example"; // String | Sort list. Values are: schoolname, distance, rank. For descending order, precede with '-' i.e. -schoolname (optional, default: schoolname)
    Boolean includeUnrankedSchoolsInRankSort = true; // Boolean | If sortBy is 'rank', this boolean determines if schools with no rank are included in the result (optional, default: false)
    try {
      APISchoolList result = apiInstance.schoolsGetAllSchools(st, appID, appKey, q, qSearchSchoolNameOnly, districtID, level, city, zip, isMagnet, isCharter, isVirtual, isTitleI, isTitleISchoolwide, nearLatitude, nearLongitude, boundaryAddress, distanceMiles, isInBoundaryOnly, boxLatitudeNW, boxLongitudeNW, boxLatitudeSE, boxLongitudeSE, page, perPage, sortBy, includeUnrankedSchoolsInRankSort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchoolsApi#schoolsGetAllSchools");
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
| **st** | **String**| Two character state (e.g. &#39;CA&#39;) - required | |
| **appID** | **String**| Your API app id | |
| **appKey** | **String**| Your API app key | |
| **q** | **String**| Search term - note: will match school name or city (optional) | [optional] |
| **qSearchSchoolNameOnly** | **Boolean**| For parameter &#39;q&#39;, only search school names instead of school and city (optional) | [optional] |
| **districtID** | **String**| Search for schools within this district (7 digit district id) (optional) | [optional] |
| **level** | **String**| Search for schools at this level. Valid values: &#39;Elementary&#39;, &#39;Middle&#39;, &#39;High&#39;, &#39;Alt&#39;, &#39;Public&#39;, &#39;Private&#39; (optional). &#39;Public&#39; returns all Elementary, Middle, High and Alternative schools | [optional] |
| **city** | **String**| Search for schools in this city (optional) | [optional] |
| **zip** | **String**| Search for schools in this 5-digit zip code (optional) | [optional] |
| **isMagnet** | **Boolean**| True &#x3D; return only magnet schools, False &#x3D; return only non-magnet schools (optional) (Pro, Enterprise API levels only) | [optional] |
| **isCharter** | **Boolean**| True &#x3D; return only charter schools, False &#x3D; return only non-charter schools (optional) (Pro, Enterprise API levels only) | [optional] |
| **isVirtual** | **Boolean**| True &#x3D; return only virtual schools, False &#x3D; return only non-virtual schools (optional) (Pro, Enterprise API levels only) | [optional] |
| **isTitleI** | **Boolean**| True &#x3D; return only Title I schools, False &#x3D; return only non-Title I schools (optional) (Pro, Enterprise API levels only) | [optional] |
| **isTitleISchoolwide** | **Boolean**| True &#x3D; return only Title I school-wide schools, False &#x3D; return only non-Title I school-wide schools (optional) (Pro, Enterprise API levels only) | [optional] |
| **nearLatitude** | **Double**| Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. 44.982560) (optional) (Pro, Enterprise API levels only. Enterprise API level will flag schools that include lat/long in its attendance boundary.) | [optional] |
| **nearLongitude** | **Double**| Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. -124.289185) (optional) (Pro, Enterprise API levels only. Enterprise API level will flag schools that include lat/long in its attendance boundary.) | [optional] |
| **boundaryAddress** | **String**| Full U.S. address: flag returned schools that include this address in its attendance boundary. Example: &#39;123 Main St. AnyTown CA 90001&#39; (optional) (Enterprise API level only) IMPORTANT NOTE: If you have the lat/long of the address, use nearLatitude and nearLongitude instead for much faster response times | [optional] |
| **distanceMiles** | **Integer**| Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (Default 5 miles) (optional) (Pro, Enterprise API levels only) | [optional] |
| **isInBoundaryOnly** | **Boolean**| Return only the schools that include given location (nearLatitude/nearLongitude) or (boundaryAddress) in its attendance boundary (Enterprise API level only) | [optional] |
| **boxLatitudeNW** | **Double**| Search for schools within a &#39;box&#39; defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional) | [optional] |
| **boxLongitudeNW** | **Double**| Search for schools within a &#39;box&#39; defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional) | [optional] |
| **boxLatitudeSE** | **Double**| Search for schools within a &#39;box&#39; defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional) | [optional] |
| **boxLongitudeSE** | **Double**| Search for schools within a &#39;box&#39; defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional) | [optional] |
| **page** | **Integer**| Page number to retrieve (optional, default: 1) | [optional] |
| **perPage** | **Integer**| Number of schools to retrieve on a page (50 max) (optional, default: 10) | [optional] |
| **sortBy** | **String**| Sort list. Values are: schoolname, distance, rank. For descending order, precede with &#39;-&#39; i.e. -schoolname (optional, default: schoolname) | [optional] |
| **includeUnrankedSchoolsInRankSort** | **Boolean**| If sortBy is &#39;rank&#39;, this boolean determines if schools with no rank are included in the result (optional, default: false) | [optional] |

### Return type

[**APISchoolList**](APISchoolList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="schoolsGetSchool10"></a>
# **schoolsGetSchool10**
> APISchool10Full schoolsGetSchool10(id, appID, appKey)

Returns a detailed record for one school

Retrieve a school record from the SchoolDigger database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.schooldigger.com");

    SchoolsApi apiInstance = new SchoolsApi(defaultClient);
    String id = "id_example"; // String | The 12 digit School ID (e.g. 064215006903)
    String appID = "appID_example"; // String | Your API app id
    String appKey = "appKey_example"; // String | Your API app key
    try {
      APISchool10Full result = apiInstance.schoolsGetSchool10(id, appID, appKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchoolsApi#schoolsGetSchool10");
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
| **id** | **String**| The 12 digit School ID (e.g. 064215006903) | |
| **appID** | **String**| Your API app id | |
| **appKey** | **String**| Your API app key | |

### Return type

[**APISchool10Full**](APISchool10Full.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

