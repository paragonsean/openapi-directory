# AutocompleteApi

All URIs are relative to *https://api.schooldigger.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**autocompleteGetSchools**](AutocompleteApi.md#autocompleteGetSchools) | **GET** /v2.0/autocomplete/schools | Returns a simple and quick list of schools for use in a client-typed autocomplete |


<a id="autocompleteGetSchools"></a>
# **autocompleteGetSchools**
> APIAutocompleteSchoolResult autocompleteGetSchools(appID, appKey, q, qSearchCityStateName, st, level, boxLatitudeNW, boxLongitudeNW, boxLatitudeSE, boxLongitudeSE, returnCount)

Returns a simple and quick list of schools for use in a client-typed autocomplete

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutocompleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.schooldigger.com");

    AutocompleteApi apiInstance = new AutocompleteApi(defaultClient);
    String appID = "appID_example"; // String | Your API app id
    String appKey = "appKey_example"; // String | Your API app key
    String q = "q_example"; // String | Search term for autocomplete (e.g. 'Lincol') (required)
    Boolean qSearchCityStateName = true; // Boolean | Extend the search term to include city and state (e.g. 'Lincoln el paso' matches Lincoln Middle School in El Paso) (optional)
    String st = "st_example"; // String | Two character state (e.g. 'CA') (optional -- leave blank to search entire U.S.)
    String level = "level_example"; // String | Search for schools at this level only. Valid values: 'Elementary', 'Middle', 'High', 'Alt', 'Private' (optional - leave blank to search for all schools)
    Double boxLatitudeNW = 3.4D; // Double | Search within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.)
    Double boxLongitudeNW = 3.4D; // Double | Search within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.)
    Double boxLatitudeSE = 3.4D; // Double | Search within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.)
    Double boxLongitudeSE = 3.4D; // Double | Search within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.)
    Integer returnCount = 56; // Integer | Number of schools to return. Valid values: 1-20. (default: 10)
    try {
      APIAutocompleteSchoolResult result = apiInstance.autocompleteGetSchools(appID, appKey, q, qSearchCityStateName, st, level, boxLatitudeNW, boxLongitudeNW, boxLatitudeSE, boxLongitudeSE, returnCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutocompleteApi#autocompleteGetSchools");
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
| **appID** | **String**| Your API app id | |
| **appKey** | **String**| Your API app key | |
| **q** | **String**| Search term for autocomplete (e.g. &#39;Lincol&#39;) (required) | [optional] |
| **qSearchCityStateName** | **Boolean**| Extend the search term to include city and state (e.g. &#39;Lincoln el paso&#39; matches Lincoln Middle School in El Paso) (optional) | [optional] |
| **st** | **String**| Two character state (e.g. &#39;CA&#39;) (optional -- leave blank to search entire U.S.) | [optional] |
| **level** | **String**| Search for schools at this level only. Valid values: &#39;Elementary&#39;, &#39;Middle&#39;, &#39;High&#39;, &#39;Alt&#39;, &#39;Private&#39; (optional - leave blank to search for all schools) | [optional] |
| **boxLatitudeNW** | **Double**| Search within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.) | [optional] |
| **boxLongitudeNW** | **Double**| Search within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.) | [optional] |
| **boxLatitudeSE** | **Double**| Search within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.) | [optional] |
| **boxLongitudeSE** | **Double**| Search within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.) | [optional] |
| **returnCount** | **Integer**| Number of schools to return. Valid values: 1-20. (default: 10) | [optional] |

### Return type

[**APIAutocompleteSchoolResult**](APIAutocompleteSchoolResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

