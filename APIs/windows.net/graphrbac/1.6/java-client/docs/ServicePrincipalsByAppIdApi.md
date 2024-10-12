# ServicePrincipalsByAppIdApi

All URIs are relative to *https://graph.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applicationsGetServicePrincipalsIdByAppId**](ServicePrincipalsByAppIdApi.md#applicationsGetServicePrincipalsIdByAppId) | **GET** /{tenantID}/servicePrincipalsByAppId/{applicationID}/objectId |  |


<a id="applicationsGetServicePrincipalsIdByAppId"></a>
# **applicationsGetServicePrincipalsIdByAppId**
> ServicePrincipalObjectResult applicationsGetServicePrincipalsIdByAppId(apiVersion, tenantID, applicationID)



Gets an object id for a given application id from the current tenant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePrincipalsByAppIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicePrincipalsByAppIdApi apiInstance = new ServicePrincipalsByAppIdApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    String applicationID = "applicationID_example"; // String | The application ID.
    try {
      ServicePrincipalObjectResult result = apiInstance.applicationsGetServicePrincipalsIdByAppId(apiVersion, tenantID, applicationID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePrincipalsByAppIdApi#applicationsGetServicePrincipalsIdByAppId");
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
| **applicationID** | **String**| The application ID. | |

### Return type

[**ServicePrincipalObjectResult**](ServicePrincipalObjectResult.md)

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

