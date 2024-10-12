# ApplicationPasswordCredentialsApi

All URIs are relative to *https://graph.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applicationsListPasswordCredentials**](ApplicationPasswordCredentialsApi.md#applicationsListPasswordCredentials) | **GET** /{tenantID}/applications/{applicationObjectId}/passwordCredentials |  |
| [**applicationsUpdatePasswordCredentials**](ApplicationPasswordCredentialsApi.md#applicationsUpdatePasswordCredentials) | **PATCH** /{tenantID}/applications/{applicationObjectId}/passwordCredentials |  |


<a id="applicationsListPasswordCredentials"></a>
# **applicationsListPasswordCredentials**
> PasswordCredentialListResult applicationsListPasswordCredentials(applicationObjectId, apiVersion, tenantID)



Get the passwordCredentials associated with an application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationPasswordCredentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationPasswordCredentialsApi apiInstance = new ApplicationPasswordCredentialsApi(defaultClient);
    String applicationObjectId = "applicationObjectId_example"; // String | Application object ID.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    try {
      PasswordCredentialListResult result = apiInstance.applicationsListPasswordCredentials(applicationObjectId, apiVersion, tenantID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationPasswordCredentialsApi#applicationsListPasswordCredentials");
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
| **applicationObjectId** | **String**| Application object ID. | |
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |

### Return type

[**PasswordCredentialListResult**](PasswordCredentialListResult.md)

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

<a id="applicationsUpdatePasswordCredentials"></a>
# **applicationsUpdatePasswordCredentials**
> applicationsUpdatePasswordCredentials(applicationObjectId, apiVersion, tenantID, passwordCredentialsUpdateParameters)



Update passwordCredentials associated with an application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationPasswordCredentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationPasswordCredentialsApi apiInstance = new ApplicationPasswordCredentialsApi(defaultClient);
    String applicationObjectId = "applicationObjectId_example"; // String | Application object ID.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    PasswordCredentialsUpdateParameters passwordCredentialsUpdateParameters = new PasswordCredentialsUpdateParameters(); // PasswordCredentialsUpdateParameters | Parameters to update passwordCredentials of an existing application.
    try {
      apiInstance.applicationsUpdatePasswordCredentials(applicationObjectId, apiVersion, tenantID, passwordCredentialsUpdateParameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationPasswordCredentialsApi#applicationsUpdatePasswordCredentials");
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
| **applicationObjectId** | **String**| Application object ID. | |
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |
| **passwordCredentialsUpdateParameters** | [**PasswordCredentialsUpdateParameters**](PasswordCredentialsUpdateParameters.md)| Parameters to update passwordCredentials of an existing application. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

