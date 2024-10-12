# ValuesInPastApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**valuesInPastGet**](ValuesInPastApi.md#valuesInPastGet) | **GET** /api/ValuesInPast/{id} | Gets all (last) values of a device              The first Value found before the given Date is returned. |


<a id="valuesInPastGet"></a>
# **valuesInPastGet**
> ValuesData valuesInPastGet(id, date)

Gets all (last) values of a device              The first Value found before the given Date is returned.

Gets the Values for a device at a given Date. The first Value found before the given Date is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuesInPastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    ValuesInPastApi apiInstance = new ValuesInPastApi(defaultClient);
    String id = "id_example"; // String | The ID of the device
    OffsetDateTime date = OffsetDateTime.now(); // OffsetDateTime | the date of the value
    try {
      ValuesData result = apiInstance.valuesInPastGet(id, date);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuesInPastApi#valuesInPastGet");
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
| **date** | **OffsetDateTime**| the date of the value | |

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

