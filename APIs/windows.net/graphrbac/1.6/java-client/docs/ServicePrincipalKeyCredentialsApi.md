# ServicePrincipalKeyCredentialsApi

All URIs are relative to *https://graph.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**servicePrincipalsListKeyCredentials**](ServicePrincipalKeyCredentialsApi.md#servicePrincipalsListKeyCredentials) | **GET** /{tenantID}/servicePrincipals/{objectId}/keyCredentials |  |
| [**servicePrincipalsUpdateKeyCredentials**](ServicePrincipalKeyCredentialsApi.md#servicePrincipalsUpdateKeyCredentials) | **PATCH** /{tenantID}/servicePrincipals/{objectId}/keyCredentials |  |


<a id="servicePrincipalsListKeyCredentials"></a>
# **servicePrincipalsListKeyCredentials**
> KeyCredentialListResult servicePrincipalsListKeyCredentials(objectId, apiVersion, tenantID)



Get the keyCredentials associated with the specified service principal.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePrincipalKeyCredentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicePrincipalKeyCredentialsApi apiInstance = new ServicePrincipalKeyCredentialsApi(defaultClient);
    String objectId = "objectId_example"; // String | The object ID of the service principal for which to get keyCredentials.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    try {
      KeyCredentialListResult result = apiInstance.servicePrincipalsListKeyCredentials(objectId, apiVersion, tenantID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePrincipalKeyCredentialsApi#servicePrincipalsListKeyCredentials");
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
| **objectId** | **String**| The object ID of the service principal for which to get keyCredentials. | |
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |

### Return type

[**KeyCredentialListResult**](KeyCredentialListResult.md)

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

<a id="servicePrincipalsUpdateKeyCredentials"></a>
# **servicePrincipalsUpdateKeyCredentials**
> servicePrincipalsUpdateKeyCredentials(objectId, apiVersion, tenantID, keyCredentialsUpdateParameters)



Update the keyCredentials associated with a service principal.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePrincipalKeyCredentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicePrincipalKeyCredentialsApi apiInstance = new ServicePrincipalKeyCredentialsApi(defaultClient);
    String objectId = "objectId_example"; // String | The object ID for which to get service principal information.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    KeyCredentialsUpdateParameters keyCredentialsUpdateParameters = new KeyCredentialsUpdateParameters(); // KeyCredentialsUpdateParameters | Parameters to update the keyCredentials of an existing service principal.
    try {
      apiInstance.servicePrincipalsUpdateKeyCredentials(objectId, apiVersion, tenantID, keyCredentialsUpdateParameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePrincipalKeyCredentialsApi#servicePrincipalsUpdateKeyCredentials");
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
| **objectId** | **String**| The object ID for which to get service principal information. | |
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |
| **keyCredentialsUpdateParameters** | [**KeyCredentialsUpdateParameters**](KeyCredentialsUpdateParameters.md)| Parameters to update the keyCredentials of an existing service principal. | |

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

