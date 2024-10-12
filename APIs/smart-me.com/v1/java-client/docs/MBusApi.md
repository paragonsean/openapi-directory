# MBusApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mBusPost**](MBusApi.md#mBusPost) | **POST** /api/MBus | M-BUS API: Adds data of a M-BUS Meter to the smart-me Cloud.              Just send us the M-BUS Telegram (RSP_UD) and we will do the Rest. |


<a id="mBusPost"></a>
# **mBusPost**
> Object mBusPost(mbusData)

M-BUS API: Adds data of a M-BUS Meter to the smart-me Cloud.              Just send us the M-BUS Telegram (RSP_UD) and we will do the Rest.

M-BUS API: Adds data of a M-BUS Meter to the smart-me Cloud.              Just send us the M-BUS Telegram (RSP_UD) and we will do the Rest.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MBusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    MBusApi apiInstance = new MBusApi(defaultClient);
    MBusData mbusData = new MBusData(); // MBusData | The M-BUS Telegram
    try {
      Object result = apiInstance.mBusPost(mbusData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MBusApi#mBusPost");
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
| **mbusData** | [**MBusData**](MBusData.md)| The M-BUS Telegram | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | BadRequest |  -  |
| **401** | Unauthorized |  -  |

