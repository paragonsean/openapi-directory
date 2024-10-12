# ConfigApiApi

All URIs are relative to *http://openpolicy.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getConfig**](ConfigApiApi.md#getConfig) | **GET** /v1/config | Get configurations |


<a id="getConfig"></a>
# **getConfig**
> Model200SingleResult getConfig(pretty)

Get configurations

This API endpoint responds with active configuration (result response)  --- **Note** The &#x60;credentials&#x60; field in the &#x60;services&#x60; configuration and  The &#x60;private_key&#x60; and &#x60;key&#x60; fields in the &#x60;keys&#x60; configuration will be omitted from the API response  ---

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openpolicy.local");

    ConfigApiApi apiInstance = new ConfigApiApi(defaultClient);
    Boolean pretty = true; // Boolean | If true, response will be in a human-readable format.
    try {
      Model200SingleResult result = apiInstance.getConfig(pretty);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApiApi#getConfig");
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
| **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] |

### Return type

[**Model200SingleResult**](Model200SingleResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **500** | Server error |  -  |

