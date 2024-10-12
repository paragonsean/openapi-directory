# SignedInUserApi

All URIs are relative to *https://graph.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**signedInUserGet**](SignedInUserApi.md#signedInUserGet) | **GET** /{tenantID}/me |  |
| [**signedInUserListOwnedObjects**](SignedInUserApi.md#signedInUserListOwnedObjects) | **GET** /{tenantID}/me/ownedObjects |  |


<a id="signedInUserGet"></a>
# **signedInUserGet**
> User signedInUserGet(apiVersion, tenantID)



Gets the details for the currently logged-in user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SignedInUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SignedInUserApi apiInstance = new SignedInUserApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    try {
      User result = apiInstance.signedInUserGet(apiVersion, tenantID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SignedInUserApi#signedInUserGet");
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

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The operation was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="signedInUserListOwnedObjects"></a>
# **signedInUserListOwnedObjects**
> DirectoryObjectListResult signedInUserListOwnedObjects(apiVersion, tenantID)



Get the list of directory objects that are owned by the user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SignedInUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SignedInUserApi apiInstance = new SignedInUserApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    try {
      DirectoryObjectListResult result = apiInstance.signedInUserListOwnedObjects(apiVersion, tenantID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SignedInUserApi#signedInUserListOwnedObjects");
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

### Return type

[**DirectoryObjectListResult**](DirectoryObjectListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The operation was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

