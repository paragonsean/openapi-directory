# CadenceExportsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2CadenceExportsIdJsonGet**](CadenceExportsApi.md#v2CadenceExportsIdJsonGet) | **GET** /v2/cadence_exports/{id}.json | Export a cadence |


<a id="v2CadenceExportsIdJsonGet"></a>
# **v2CadenceExportsIdJsonGet**
> CadenceExport v2CadenceExportsIdJsonGet(id)

Export a cadence

Exports a cadence as JSON. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CadenceExportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    CadenceExportsApi apiInstance = new CadenceExportsApi(defaultClient);
    String id = "id_example"; // String | Cadence ID
    try {
      CadenceExport result = apiInstance.v2CadenceExportsIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CadenceExportsApi#v2CadenceExportsIdJsonGet");
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
| **id** | **String**| Cadence ID | |

### Return type

[**CadenceExport**](CadenceExport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

