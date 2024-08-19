# AlertsApi

All URIs are relative to *https://api.victorops.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPublicV1AlertsUuidGet**](AlertsApi.md#apiPublicV1AlertsUuidGet) | **GET** /api-public/v1/alerts/{uuid} | Retrieve alert details. |


<a id="apiPublicV1AlertsUuidGet"></a>
# **apiPublicV1AlertsUuidGet**
> GetAlertResponse apiPublicV1AlertsUuidGet(xVOApiId, xVOApiKey, uuid)

Retrieve alert details.

Retrieve the details of an alert that was sent VictorOps by you.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String uuid = "uuid_example"; // String | The VictorOps uuid of the alert
    try {
      GetAlertResponse result = apiInstance.apiPublicV1AlertsUuidGet(xVOApiId, xVOApiKey, uuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#apiPublicV1AlertsUuidGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **uuid** | **String**| The VictorOps uuid of the alert | |

### Return type

[**GetAlertResponse**](GetAlertResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The alert, if found.  |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

