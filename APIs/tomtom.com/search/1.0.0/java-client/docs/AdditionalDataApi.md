# AdditionalDataApi

All URIs are relative to *https://api.tomtom.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchVersionNumberAdditionalDataExtGet**](AdditionalDataApi.md#searchVersionNumberAdditionalDataExtGet) | **GET** /search/{versionNumber}/additionalData.{ext} | Additional Data |


<a id="searchVersionNumberAdditionalDataExtGet"></a>
# **searchVersionNumberAdditionalDataExtGet**
> searchVersionNumberAdditionalDataExtGet(versionNumber, ext, geometries, geometriesZoom)

Additional Data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdditionalDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AdditionalDataApi apiInstance = new AdditionalDataApi(defaultClient);
    Integer versionNumber = 2; // Integer | Service version number. The current value is 2.
    String ext = "json"; // String | Expected response format.
    String geometries = "00004631-3400-3c00-0000-0000673c4d2e,00004631-3400-3c00-0000-0000673c42fe"; // String | Comma separated list of geometry UUIDs, previously retrieved from an Search API request.
    Integer geometriesZoom = 0; // Integer | Defines the precision of the geometries.
    try {
      apiInstance.searchVersionNumberAdditionalDataExtGet(versionNumber, ext, geometries, geometriesZoom);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdditionalDataApi#searchVersionNumberAdditionalDataExtGet");
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
| **versionNumber** | **Integer**| Service version number. The current value is 2. | [enum: 2] |
| **ext** | **String**| Expected response format. | [enum: json] |
| **geometries** | **String**| Comma separated list of geometry UUIDs, previously retrieved from an Search API request. | |
| **geometriesZoom** | **Integer**| Defines the precision of the geometries. | [optional] [enum: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK: additional data were retrieved and the body of the response contains requested data. |  -  |
| **400** | Bad request: one or more parameters(i.e. geometries, ext) were incorrectly specified. |  -  |
| **403** | Permission, capacity, or authentication issues:   - Forbidden   - Not authorized   - Account inactive   - Account over queries per second limit   - Account over rate limit   - Rate limit exceeded |  -  |
| **404** | Not Found: the requested resource could not be found, but it may be available again in the future. |  -  |
| **405** | Method Not Allowed: the client used a HTTP method other than GET. |  -  |
| **408** | Request timeout. |  -  |
| **414** | Requested uri is too long. |  -  |
| **500** | An error occurred while processing the request. Please try again later. |  -  |
| **502** | Internal network connectivity issue. |  -  |
| **503** | Service currently unavailable. |  -  |
| **504** | Internal network connectivity issue or a request that has taken too long to complete. |  -  |
| **596** | Service not found. |  -  |

