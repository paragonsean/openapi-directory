# VirtualTariffConsumptionApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualTariffConsumptionGet**](VirtualTariffConsumptionApi.md#virtualTariffConsumptionGet) | **GET** /api/VirtualTariffConsumption | Gets the consumption of a folder with a virtuall tariffs. |


<a id="virtualTariffConsumptionGet"></a>
# **virtualTariffConsumptionGet**
> List&lt;VirtualTariffConsumptionData&gt; virtualTariffConsumptionGet(folderId, startDate, endDate)

Gets the consumption of a folder with a virtuall tariffs.

Gets the consumption of a folder with a virtuall tariffs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualTariffConsumptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    VirtualTariffConsumptionApi apiInstance = new VirtualTariffConsumptionApi(defaultClient);
    String folderId = "folderId_example"; // String | The ID of the Folder
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The start date (UTC)
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The end date (UTC)
    try {
      List<VirtualTariffConsumptionData> result = apiInstance.virtualTariffConsumptionGet(folderId, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualTariffConsumptionApi#virtualTariffConsumptionGet");
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
| **folderId** | **String**| The ID of the Folder | |
| **startDate** | **OffsetDateTime**| The start date (UTC) | |
| **endDate** | **OffsetDateTime**| The end date (UTC) | |

### Return type

[**List&lt;VirtualTariffConsumptionData&gt;**](VirtualTariffConsumptionData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

