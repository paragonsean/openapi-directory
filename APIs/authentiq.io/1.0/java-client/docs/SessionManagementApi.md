# SessionManagementApi

All URIs are relative to *https://connect.authentiq.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authorizeIframe**](SessionManagementApi.md#authorizeIframe) | **GET** /{client_id}/iframe | Include a session iframe |


<a id="authorizeIframe"></a>
# **authorizeIframe**
> authorizeIframe(clientId)

Include a session iframe

An OpenID Connect Session Management iframe to facilitate e.g. single sign-on or remote logouts.  The iframe implements the OIDC postMessage-based [change notification protocol](http://openid.net/specs/openid-connect-session-1_0.html#ChangeNotification) via which a client can receive notifications about session state changes. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.authentiq.io");

    SessionManagementApi apiInstance = new SessionManagementApi(defaultClient);
    String clientId = "clientId_example"; // String | Client identifier
    try {
      apiInstance.authorizeIframe(clientId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionManagementApi#authorizeIframe");
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
| **clientId** | **String**| Client identifier | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Cache-Control - public, max-age&#x3D;7200 <br>  |

