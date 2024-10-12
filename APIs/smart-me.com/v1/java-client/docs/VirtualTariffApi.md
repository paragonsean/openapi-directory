# VirtualTariffApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiVirtualTariffIdGet**](VirtualTariffApi.md#apiVirtualTariffIdGet) | **GET** /api/VirtualTariff/{id} | Gets all virtual tariffs of a folder |
| [**virtualTariffGet**](VirtualTariffApi.md#virtualTariffGet) | **GET** /api/VirtualTariff | Gets all Virtual Tariffs of a user |


<a id="apiVirtualTariffIdGet"></a>
# **apiVirtualTariffIdGet**
> VirtualTariffsOfFolder apiVirtualTariffIdGet(id)

Gets all virtual tariffs of a folder

Gets all virtual tariffs of a folder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualTariffApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    VirtualTariffApi apiInstance = new VirtualTariffApi(defaultClient);
    String id = "id_example"; // String | The ID of the Folder
    try {
      VirtualTariffsOfFolder result = apiInstance.apiVirtualTariffIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualTariffApi#apiVirtualTariffIdGet");
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
| **id** | **String**| The ID of the Folder | |

### Return type

[**VirtualTariffsOfFolder**](VirtualTariffsOfFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="virtualTariffGet"></a>
# **virtualTariffGet**
> List&lt;VirtualTariffsOfFolder&gt; virtualTariffGet()

Gets all Virtual Tariffs of a user

Gets all Virtual Tariffs of a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualTariffApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    VirtualTariffApi apiInstance = new VirtualTariffApi(defaultClient);
    try {
      List<VirtualTariffsOfFolder> result = apiInstance.virtualTariffGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualTariffApi#virtualTariffGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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

