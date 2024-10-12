# PeopleApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**peopleGeoPeopleGeoGet**](PeopleApi.md#peopleGeoPeopleGeoGet) | **GET** /people.geo | People Geo |
| [**peopleSearchPeopleGet**](PeopleApi.md#peopleSearchPeopleGet) | **GET** /people | People Search |


<a id="peopleGeoPeopleGeoGet"></a>
# **peopleGeoPeopleGeoGet**
> PersonList peopleGeoPeopleGeoGet(lat, lng, include, apikey, xApiKey)

People Geo

Get list of people currently representing a given location.  **Note:** Currently limited to state legislators and US Congress.  Governors &amp; mayors are not included.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeopleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PeopleApi apiInstance = new PeopleApi(defaultClient);
    BigDecimal lat = new BigDecimal(78); // BigDecimal | Latitude of point.
    BigDecimal lng = new BigDecimal(78); // BigDecimal | Longitude of point.
    List<PersonInclude> include = Arrays.asList(); // List<PersonInclude> | Additional information to include in the response.
    String apikey = "apikey_example"; // String | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      PersonList result = apiInstance.peopleGeoPeopleGeoGet(lat, lng, include, apikey, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeopleApi#peopleGeoPeopleGeoGet");
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
| **lat** | **BigDecimal**| Latitude of point. | |
| **lng** | **BigDecimal**| Longitude of point. | |
| **include** | [**List&lt;PersonInclude&gt;**](PersonInclude.md)| Additional information to include in the response. | [optional] |
| **apikey** | **String**|  | [optional] |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**PersonList**](PersonList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="peopleSearchPeopleGet"></a>
# **peopleSearchPeopleGet**
> PersonList peopleSearchPeopleGet(jurisdiction, name, id, orgClassification, district, include, page, perPage, apikey, xApiKey)

People Search

Get list of people matching selected criteria.  Must provide either **jurisdiction**, **name**, or one or more **id** parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeopleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PeopleApi apiInstance = new PeopleApi(defaultClient);
    String jurisdiction = "jurisdiction_example"; // String | Filter by jurisdiction name or id.
    String name = "name_example"; // String | Filter by name, case-insensitive match.
    List<String> id = Arrays.asList(); // List<String> | Filter by id, can be specified multiple times for multiple people.
    OrgClassification orgClassification = OrgClassification.fromValue("legislature"); // OrgClassification | Filter by current role.
    String district = "district_example"; // String | Filter by district name.
    List<PersonInclude> include = Arrays.asList(); // List<PersonInclude> | Additional information to include in response.
    Integer page = 1; // Integer | 
    Integer perPage = 10; // Integer | 
    String apikey = "apikey_example"; // String | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      PersonList result = apiInstance.peopleSearchPeopleGet(jurisdiction, name, id, orgClassification, district, include, page, perPage, apikey, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeopleApi#peopleSearchPeopleGet");
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
| **jurisdiction** | **String**| Filter by jurisdiction name or id. | [optional] |
| **name** | **String**| Filter by name, case-insensitive match. | [optional] |
| **id** | [**List&lt;String&gt;**](String.md)| Filter by id, can be specified multiple times for multiple people. | [optional] |
| **orgClassification** | [**OrgClassification**](.md)| Filter by current role. | [optional] [enum: legislature, executive, lower, upper, government] |
| **district** | **String**| Filter by district name. | [optional] |
| **include** | [**List&lt;PersonInclude&gt;**](PersonInclude.md)| Additional information to include in response. | [optional] |
| **page** | **Integer**|  | [optional] [default to 1] |
| **perPage** | **Integer**|  | [optional] [default to 10] |
| **apikey** | **String**|  | [optional] |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**PersonList**](PersonList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

