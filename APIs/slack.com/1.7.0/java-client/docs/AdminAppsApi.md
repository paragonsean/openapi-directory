# AdminAppsApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminAppsApprove**](AdminAppsApi.md#adminAppsApprove) | **POST** /admin.apps.approve |  |
| [**adminAppsRestrict**](AdminAppsApi.md#adminAppsRestrict) | **POST** /admin.apps.restrict |  |


<a id="adminAppsApprove"></a>
# **adminAppsApprove**
> DefaultSuccessTemplate adminAppsApprove(token, appId, requestId, teamId)



Approve an app for installation on a workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminAppsApi apiInstance = new AdminAppsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.apps:write`
    String appId = "appId_example"; // String | The id of the app to approve.
    String requestId = "requestId_example"; // String | The id of the request to approve.
    String teamId = "teamId_example"; // String | 
    try {
      DefaultSuccessTemplate result = apiInstance.adminAppsApprove(token, appId, requestId, teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminAppsApi#adminAppsApprove");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.apps:write&#x60; | |
| **appId** | **String**| The id of the app to approve. | [optional] |
| **requestId** | **String**| The id of the request to approve. | [optional] |
| **teamId** | **String**|  | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="adminAppsRestrict"></a>
# **adminAppsRestrict**
> DefaultSuccessTemplate adminAppsRestrict(token, appId, requestId, teamId)



Restrict an app for installation on a workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminAppsApi apiInstance = new AdminAppsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.apps:write`
    String appId = "appId_example"; // String | The id of the app to restrict.
    String requestId = "requestId_example"; // String | The id of the request to restrict.
    String teamId = "teamId_example"; // String | 
    try {
      DefaultSuccessTemplate result = apiInstance.adminAppsRestrict(token, appId, requestId, teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminAppsApi#adminAppsRestrict");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.apps:write&#x60; | |
| **appId** | **String**| The id of the app to restrict. | [optional] |
| **requestId** | **String**| The id of the request to restrict. | [optional] |
| **teamId** | **String**|  | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

