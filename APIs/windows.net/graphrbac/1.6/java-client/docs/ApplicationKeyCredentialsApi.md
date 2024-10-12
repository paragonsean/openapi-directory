# ApplicationKeyCredentialsApi

All URIs are relative to *https://graph.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applicationsListKeyCredentials**](ApplicationKeyCredentialsApi.md#applicationsListKeyCredentials) | **GET** /{tenantID}/applications/{applicationObjectId}/keyCredentials |  |
| [**applicationsUpdateKeyCredentials**](ApplicationKeyCredentialsApi.md#applicationsUpdateKeyCredentials) | **PATCH** /{tenantID}/applications/{applicationObjectId}/keyCredentials |  |


<a id="applicationsListKeyCredentials"></a>
# **applicationsListKeyCredentials**
> KeyCredentialListResult applicationsListKeyCredentials(applicationObjectId, apiVersion, tenantID)



Get the keyCredentials associated with an application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationKeyCredentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationKeyCredentialsApi apiInstance = new ApplicationKeyCredentialsApi(defaultClient);
    String applicationObjectId = "applicationObjectId_example"; // String | Application object ID.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    try {
      KeyCredentialListResult result = apiInstance.applicationsListKeyCredentials(applicationObjectId, apiVersion, tenantID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationKeyCredentialsApi#applicationsListKeyCredentials");
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

<a id="applicationsUpdateKeyCredentials"></a>
# **applicationsUpdateKeyCredentials**
> applicationsUpdateKeyCredentials(applicationObjectId, apiVersion, tenantID, keyCredentialsUpdateParameters)



Update the keyCredentials associated with an application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationKeyCredentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationKeyCredentialsApi apiInstance = new ApplicationKeyCredentialsApi(defaultClient);
    String applicationObjectId = "applicationObjectId_example"; // String | Application object ID.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    KeyCredentialsUpdateParameters keyCredentialsUpdateParameters = new KeyCredentialsUpdateParameters(); // KeyCredentialsUpdateParameters | Parameters to update the keyCredentials of an existing application.
    try {
      apiInstance.applicationsUpdateKeyCredentials(applicationObjectId, apiVersion, tenantID, keyCredentialsUpdateParameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationKeyCredentialsApi#applicationsUpdateKeyCredentials");
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
| **keyCredentialsUpdateParameters** | [**KeyCredentialsUpdateParameters**](KeyCredentialsUpdateParameters.md)| Parameters to update the keyCredentials of an existing application. | |

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

