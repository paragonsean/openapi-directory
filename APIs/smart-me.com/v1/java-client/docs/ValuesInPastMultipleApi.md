# ValuesInPastMultipleApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**valuesInPastMultipleGet**](ValuesInPastMultipleApi.md#valuesInPastMultipleGet) | **GET** /api/ValuesInPastMultiple/{id} | Gets multiple values of a device. This call needs a smart-me professional licence. |


<a id="valuesInPastMultipleGet"></a>
# **valuesInPastMultipleGet**
> List&lt;ValuesData&gt; valuesInPastMultipleGet(id, startDate, endDate, interval)

Gets multiple values of a device. This call needs a smart-me professional licence.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValuesInPastMultipleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    ValuesInPastMultipleApi apiInstance = new ValuesInPastMultipleApi(defaultClient);
    String id = "id_example"; // String | The ID of the device
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The date when the first value should start
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The date when the last value should start
    Integer interval = 56; // Integer | The interval in minutes betwenn the values. 0 means as fast as possible. Only 1000 values can be get in one call.
    try {
      List<ValuesData> result = apiInstance.valuesInPastMultipleGet(id, startDate, endDate, interval);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValuesInPastMultipleApi#valuesInPastMultipleGet");
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
| **startDate** | **OffsetDateTime**| The date when the first value should start | |
| **endDate** | **OffsetDateTime**| The date when the last value should start | |
| **interval** | **Integer**| The interval in minutes betwenn the values. 0 means as fast as possible. Only 1000 values can be get in one call. | |

### Return type

[**List&lt;ValuesData&gt;**](ValuesData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

