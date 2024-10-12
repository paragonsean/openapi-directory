# OAuth2PermissionGrantListApi

All URIs are relative to *https://graph.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**oAuth2PermissionGrantList**](OAuth2PermissionGrantListApi.md#oAuth2PermissionGrantList) | **GET** /{tenantID}/oauth2PermissionGrants |  |


<a id="oAuth2PermissionGrantList"></a>
# **oAuth2PermissionGrantList**
> OAuth2PermissionGrantListResult oAuth2PermissionGrantList(apiVersion, tenantID, $filter)



Queries OAuth2 permissions grants for the relevant SP ObjectId of an app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OAuth2PermissionGrantListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OAuth2PermissionGrantListApi apiInstance = new OAuth2PermissionGrantListApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    String $filter = "clientId+eq+'61ed44c3-5a1d-4639-a215-07f25129c6c3"; // String | This is the Service Principal ObjectId associated with the app
    try {
      OAuth2PermissionGrantListResult result = apiInstance.oAuth2PermissionGrantList(apiVersion, tenantID, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OAuth2PermissionGrantListApi#oAuth2PermissionGrantList");
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
| **$filter** | **String**| This is the Service Principal ObjectId associated with the app | [optional] |

### Return type

[**OAuth2PermissionGrantListResult**](OAuth2PermissionGrantListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The operation was successful. |  -  |

