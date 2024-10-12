# AppPkgmNotificationsApi

All URIs are relative to *http://etsi.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appPkgNotificationPOST**](AppPkgmNotificationsApi.md#appPkgNotificationPOST) | **POST** /user_defined_notification | Registers a notification endpoint to notify application package operations |


<a id="appPkgNotificationPOST"></a>
# **appPkgNotificationPOST**
> appPkgNotificationPOST(appPkgNotification)

Registers a notification endpoint to notify application package operations

Registers a notification endpoint to notify application package operations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPkgmNotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etsi.local");

    AppPkgmNotificationsApi apiInstance = new AppPkgmNotificationsApi(defaultClient);
    AppPkgNotification appPkgNotification = new AppPkgNotification(); // AppPkgNotification | Notification endpoint to be created
    try {
      apiInstance.appPkgNotificationPOST(appPkgNotification);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPkgmNotificationsApi#appPkgNotificationPOST");
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
| **appPkgNotification** | [**AppPkgNotification**](AppPkgNotification.md)| Notification endpoint to be created | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **401** | Unauthorized :  used when the client did not submit credentials. |  -  |
| **403** | Forbidden :  operation is not allowed given the current status of the resource. |  -  |
| **404** | Not Found :  used when a client provided a URI that cannot be mapped to a valid resource URI. |  -  |
| **429** | Too Many Requests : used when a rate limiter has triggered. |  -  |

