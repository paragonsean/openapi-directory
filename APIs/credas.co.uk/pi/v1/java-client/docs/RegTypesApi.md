# RegTypesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAll**](RegTypesApi.md#getAll) | **GET** /api/reg-types | Gets all available RegTypes. |


<a id="getAll"></a>
# **getAll**
> List&lt;CredasApiModelsRegTypesRegType&gt; getAll(apikey)

Gets all available RegTypes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegTypesApi apiInstance = new RegTypesApi(defaultClient);
    String apikey = "apikey_example"; // String | ApiKey supplied.
    try {
      List<CredasApiModelsRegTypesRegType> result = apiInstance.getAll(apikey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegTypesApi#getAll");
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
| **apikey** | **String**| ApiKey supplied. | |

### Return type

[**List&lt;CredasApiModelsRegTypesRegType&gt;**](CredasApiModelsRegTypesRegType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A collection of available RegTypes. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

