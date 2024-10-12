# OAuth2PermissionGrantDeleteApi

All URIs are relative to *https://graph.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**oAuth2PermissionGrantDelete**](OAuth2PermissionGrantDeleteApi.md#oAuth2PermissionGrantDelete) | **DELETE** /{tenantID}/oauth2PermissionGrants/{objectId} |  |


<a id="oAuth2PermissionGrantDelete"></a>
# **oAuth2PermissionGrantDelete**
> oAuth2PermissionGrantDelete(objectId, apiVersion, tenantID)



Delete a OAuth2 permission grant for the relevant resource Ids of an app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OAuth2PermissionGrantDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OAuth2PermissionGrantDeleteApi apiInstance = new OAuth2PermissionGrantDeleteApi(defaultClient);
    String objectId = "objectId_example"; // String | The object ID of a permission grant.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    try {
      apiInstance.oAuth2PermissionGrantDelete(objectId, apiVersion, tenantID);
    } catch (ApiException e) {
      System.err.println("Exception when calling OAuth2PermissionGrantDeleteApi#oAuth2PermissionGrantDelete");
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
| **objectId** | **String**| The object ID of a permission grant. | |
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

