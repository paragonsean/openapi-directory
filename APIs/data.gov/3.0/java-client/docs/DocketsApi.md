# DocketsApi

All URIs are relative to *https://api.data.gov/regulations/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**docket**](DocketsApi.md#docket) | **GET** /docket.{response_format} | Returns Docket information |


<a id="docket"></a>
# **docket**
> docket(responseFormat, docketId)

Returns Docket information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.data.gov/regulations/v3");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocketsApi apiInstance = new DocketsApi(defaultClient);
    String responseFormat = "json"; // String | Format
    String docketId = "EPA-HQ-OAR-2011-0028"; // String | Docket ID
    try {
      apiInstance.docket(responseFormat, docketId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocketsApi#docket");
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
| **responseFormat** | **String**| Format | [default to json] [enum: json, xml] |
| **docketId** | **String**| Docket ID | [default to EPA-HQ-OAR-2011-0028] |

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
| **200** | No response was specified |  -  |
| **400** | Bad request. The content is either empty or has been withdrawn. |  -  |
| **404** | File not found. |  -  |

