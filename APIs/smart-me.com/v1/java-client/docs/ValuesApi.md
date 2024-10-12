# ValuesApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**valuesGet**](ValuesApi.md#valuesGet) | **GET** /api/Values/{id} | Gets all (last) values of a device |


<a id="valuesGet"></a>
# **valuesGet**
> ValuesData valuesGet(id)

Gets all (last) values of a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    ValuesApi apiInstance = new ValuesApi(defaultClient);
    String id = "id_example"; // String | The ID of the device
    try {
      ValuesData result = apiInstance.valuesGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuesApi#valuesGet");
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
| **id** | **String**| The ID of the device | |

### Return type

[**ValuesData**](ValuesData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

