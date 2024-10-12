# DistrictsApi

All URIs are relative to *https://api.schooldigger.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**districtsGetAllDistricts**](DistrictsApi.md#districtsGetAllDistricts) | **GET** /v1/districts | Returns a list of districts |
| [**districtsGetDistrict**](DistrictsApi.md#districtsGetDistrict) | **GET** /v1/districts/{id} | Returns a detailed record for one district |


<a id="districtsGetAllDistricts"></a>
# **districtsGetAllDistricts**
> APIDistrictList districtsGetAllDistricts(st, appID, appKey, q, city, zip, nearLatitude, nearLongitude, boundaryAddress, distanceMiles, isInBoundaryOnly, boxLatitudeNW, boxLongitudeNW, boxLatitudeSE, boxLongitudeSE, page, perPage, sortBy, includeUnrankedDistrictsInRankSort)

Returns a list of districts

Search the SchoolDigger database for districts. You may use any combination of criteria as query parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistrictsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.schooldigger.com");

    DistrictsApi apiInstance = new DistrictsApi(defaultClient);
    String st = "st_example"; // String | Two character state (e.g. 'CA') - required
    String appID = "appID_example"; // String | Your API app id
    String appKey = "appKey_example"; // String | Your API app key
    String q = "q_example"; // String | Search term - note: will match district name or city (optional)
    String city = "city_example"; // String | Search for districts in this city (optional)
    String zip = "zip_example"; // String | Search for districts in this 5-digit zip code (optional)
    Double nearLatitude = 3.4D; // Double | Search for districts within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. 44.982560) (optional) (Pro, Enterprise API levels only. Enterprise API level will flag districts that include lat/long in its attendance boundary.)
    Double nearLongitude = 3.4D; // Double | Search for districts within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. -124.289185) (optional) (Pro, Enterprise API levels only. Enterprise API level will flag districts that include lat/long in its attendance boundary.)
    String boundaryAddress = "boundaryAddress_example"; // String | Full U.S. address: flag returned districts that include this address in its attendance boundary. Example: '123 Main St. AnyTown CA 90001' (optional) (Enterprise API level only)
    Integer distanceMiles = 56; // Integer | Search for districts within (distanceMiles) of (nearLatitude)/(nearLongitude) (Default 50 miles) (optional) (Pro, Enterprise API levels only)
    Boolean isInBoundaryOnly = true; // Boolean | Return only the districts that include given location (nearLatitude/nearLongitude) or (boundaryAddress) in its attendance boundary (Enterprise API level only)
    Double boxLatitudeNW = 3.4D; // Double | Search for districts within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional)
    Double boxLongitudeNW = 3.4D; // Double | Search for districts within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional)
    Double boxLatitudeSE = 3.4D; // Double | Search for districts within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional)
    Double boxLongitudeSE = 3.4D; // Double | Search for districts within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional)
    Integer page = 56; // Integer | Page number to retrieve (optional, default: 1)
    Integer perPage = 56; // Integer | Number of districts to retrieve on a page (50 max) (optional, default: 10)
    String sortBy = "sortBy_example"; // String | Sort list. Values are: districtname, distance, rank. For descending order, precede with '-' i.e. -districtname (optional, default: districtname)
    Boolean includeUnrankedDistrictsInRankSort = true; // Boolean | If sortBy is 'rank', this boolean determines if districts with no rank are included in the result (optional, default: false)
    try {
      APIDistrictList result = apiInstance.districtsGetAllDistricts(st, appID, appKey, q, city, zip, nearLatitude, nearLongitude, boundaryAddress, distanceMiles, isInBoundaryOnly, boxLatitudeNW, boxLongitudeNW, boxLatitudeSE, boxLongitudeSE, page, perPage, sortBy, includeUnrankedDistrictsInRankSort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistrictsApi#districtsGetAllDistricts");
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
| **q** | **String**| Search term - note: will match district name or city (optional) | [optional] |
| **city** | **String**| Search for districts in this city (optional) | [optional] |
| **zip** | **String**| Search for districts in this 5-digit zip code (optional) | [optional] |
| **nearLatitude** | **Double**| Search for districts within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. 44.982560) (optional) (Pro, Enterprise API levels only. Enterprise API level will flag districts that include lat/long in its attendance boundary.) | [optional] |
| **nearLongitude** | **Double**| Search for districts within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. -124.289185) (optional) (Pro, Enterprise API levels only. Enterprise API level will flag districts that include lat/long in its attendance boundary.) | [optional] |
| **boundaryAddress** | **String**| Full U.S. address: flag returned districts that include this address in its attendance boundary. Example: &#39;123 Main St. AnyTown CA 90001&#39; (optional) (Enterprise API level only) | [optional] |
| **distanceMiles** | **Integer**| Search for districts within (distanceMiles) of (nearLatitude)/(nearLongitude) (Default 50 miles) (optional) (Pro, Enterprise API levels only) | [optional] |
| **isInBoundaryOnly** | **Boolean**| Return only the districts that include given location (nearLatitude/nearLongitude) or (boundaryAddress) in its attendance boundary (Enterprise API level only) | [optional] |
| **boxLatitudeNW** | **Double**| Search for districts within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional) | [optional] |
| **boxLongitudeNW** | **Double**| Search for districts within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional) | [optional] |
| **boxLatitudeSE** | **Double**| Search for districts within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional) | [optional] |
| **boxLongitudeSE** | **Double**| Search for districts within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional) | [optional] |
| **page** | **Integer**| Page number to retrieve (optional, default: 1) | [optional] |
| **perPage** | **Integer**| Number of districts to retrieve on a page (50 max) (optional, default: 10) | [optional] |
| **sortBy** | **String**| Sort list. Values are: districtname, distance, rank. For descending order, precede with &#39;-&#39; i.e. -districtname (optional, default: districtname) | [optional] |
| **includeUnrankedDistrictsInRankSort** | **Boolean**| If sortBy is &#39;rank&#39;, this boolean determines if districts with no rank are included in the result (optional, default: false) | [optional] |

### Return type

[**APIDistrictList**](APIDistrictList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="districtsGetDistrict"></a>
# **districtsGetDistrict**
> APIDistrict districtsGetDistrict(id, appID, appKey)

Returns a detailed record for one district

Retrieve a single district record from the SchoolDigger database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistrictsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.schooldigger.com");

    DistrictsApi apiInstance = new DistrictsApi(defaultClient);
    String id = "id_example"; // String | The 7 digit District ID (e.g. 0642150)
    String appID = "appID_example"; // String | Your API app id
    String appKey = "appKey_example"; // String | Your API app key
    try {
      APIDistrict result = apiInstance.districtsGetDistrict(id, appID, appKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistrictsApi#districtsGetDistrict");
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
| **id** | **String**| The 7 digit District ID (e.g. 0642150) | |
| **appID** | **String**| Your API app id | |
| **appKey** | **String**| Your API app key | |

### Return type

[**APIDistrict**](APIDistrict.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

