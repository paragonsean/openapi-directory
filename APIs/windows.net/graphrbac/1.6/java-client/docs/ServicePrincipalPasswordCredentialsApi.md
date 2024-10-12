# ServicePrincipalPasswordCredentialsApi

All URIs are relative to *https://graph.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**servicePrincipalsListPasswordCredentials**](ServicePrincipalPasswordCredentialsApi.md#servicePrincipalsListPasswordCredentials) | **GET** /{tenantID}/servicePrincipals/{objectId}/passwordCredentials |  |
| [**servicePrincipalsUpdatePasswordCredentials**](ServicePrincipalPasswordCredentialsApi.md#servicePrincipalsUpdatePasswordCredentials) | **PATCH** /{tenantID}/servicePrincipals/{objectId}/passwordCredentials |  |


<a id="servicePrincipalsListPasswordCredentials"></a>
# **servicePrincipalsListPasswordCredentials**
> PasswordCredentialListResult servicePrincipalsListPasswordCredentials(objectId, apiVersion, tenantID)



Gets the passwordCredentials associated with a service principal.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePrincipalPasswordCredentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicePrincipalPasswordCredentialsApi apiInstance = new ServicePrincipalPasswordCredentialsApi(defaultClient);
    String objectId = "objectId_example"; // String | The object ID of the service principal.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    try {
      PasswordCredentialListResult result = apiInstance.servicePrincipalsListPasswordCredentials(objectId, apiVersion, tenantID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePrincipalPasswordCredentialsApi#servicePrincipalsListPasswordCredentials");
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
| **objectId** | **String**| The object ID of the service principal. | |
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

<a id="servicePrincipalsUpdatePasswordCredentials"></a>
# **servicePrincipalsUpdatePasswordCredentials**
> servicePrincipalsUpdatePasswordCredentials(objectId, apiVersion, tenantID, passwordCredentialsUpdateParameters)



Updates the passwordCredentials associated with a service principal.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePrincipalPasswordCredentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicePrincipalPasswordCredentialsApi apiInstance = new ServicePrincipalPasswordCredentialsApi(defaultClient);
    String objectId = "objectId_example"; // String | The object ID of the service principal.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    PasswordCredentialsUpdateParameters passwordCredentialsUpdateParameters = new PasswordCredentialsUpdateParameters(); // PasswordCredentialsUpdateParameters | Parameters to update the passwordCredentials of an existing service principal.
    try {
      apiInstance.servicePrincipalsUpdatePasswordCredentials(objectId, apiVersion, tenantID, passwordCredentialsUpdateParameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePrincipalPasswordCredentialsApi#servicePrincipalsUpdatePasswordCredentials");
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
| **objectId** | **String**| The object ID of the service principal. | |
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |
| **passwordCredentialsUpdateParameters** | [**PasswordCredentialsUpdateParameters**](PasswordCredentialsUpdateParameters.md)| Parameters to update the passwordCredentials of an existing service principal. | |

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

