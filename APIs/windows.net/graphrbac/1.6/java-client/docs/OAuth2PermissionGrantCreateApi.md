# OAuth2PermissionGrantCreateApi

All URIs are relative to *https://graph.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**oAuth2PermissionGrantCreate**](OAuth2PermissionGrantCreateApi.md#oAuth2PermissionGrantCreate) | **POST** /{tenantID}/oauth2PermissionGrants |  |


<a id="oAuth2PermissionGrantCreate"></a>
# **oAuth2PermissionGrantCreate**
> OAuth2PermissionGrant oAuth2PermissionGrantCreate(apiVersion, tenantID, oauth2PermissionGrant)



Grants OAuth2 permissions for the relevant resource Ids of an app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OAuth2PermissionGrantCreateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OAuth2PermissionGrantCreateApi apiInstance = new OAuth2PermissionGrantCreateApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    OAuth2PermissionGrant oauth2PermissionGrant = new OAuth2PermissionGrant(); // OAuth2PermissionGrant | The relevant app Service Principal Object Id and the Service Principal Object Id you want to grant.
    try {
      OAuth2PermissionGrant result = apiInstance.oAuth2PermissionGrantCreate(apiVersion, tenantID, oauth2PermissionGrant);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OAuth2PermissionGrantCreateApi#oAuth2PermissionGrantCreate");
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
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |
| **oauth2PermissionGrant** | [**OAuth2PermissionGrant**](OAuth2PermissionGrant.md)| The relevant app Service Principal Object Id and the Service Principal Object Id you want to grant. | [optional] |

### Return type

[**OAuth2PermissionGrant**](OAuth2PermissionGrant.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK. The operation was successful. |  -  |

