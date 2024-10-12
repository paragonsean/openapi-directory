# VirtualTariffsForPropertyApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualTariffsForPropertyGet**](VirtualTariffsForPropertyApi.md#virtualTariffsForPropertyGet) | **GET** /api/VirtualTariffsForProperty/{id} | Gets all Virtual Tariffs for a property (folder) |


<a id="virtualTariffsForPropertyGet"></a>
# **virtualTariffsForPropertyGet**
> List&lt;VirtualTariffsOfFolder&gt; virtualTariffsForPropertyGet(id)

Gets all Virtual Tariffs for a property (folder)

Gets all Virtual Tariffs for a property (folder)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualTariffsForPropertyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    VirtualTariffsForPropertyApi apiInstance = new VirtualTariffsForPropertyApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      List<VirtualTariffsOfFolder> result = apiInstance.virtualTariffsForPropertyGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualTariffsForPropertyApi#virtualTariffsForPropertyGet");
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
| **id** | **String**|  | |

### Return type

[**List&lt;VirtualTariffsOfFolder&gt;**](VirtualTariffsOfFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

