# ComplianceResultsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**complianceResultsGet**](ComplianceResultsApi.md#complianceResultsGet) | **GET** /{resourceId}/providers/Microsoft.Security/complianceResults/{complianceResultName} |  |
| [**complianceResultsList**](ComplianceResultsApi.md#complianceResultsList) | **GET** /{scope}/providers/Microsoft.Security/complianceResults |  |


<a id="complianceResultsGet"></a>
# **complianceResultsGet**
> ComplianceResult complianceResultsGet(apiVersion, resourceId, complianceResultName)



Security Compliance Result

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComplianceResultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ComplianceResultsApi apiInstance = new ComplianceResultsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String resourceId = "resourceId_example"; // String | The identifier of the resource.
    String complianceResultName = "complianceResultName_example"; // String | name of the desired assessment compliance result
    try {
      ComplianceResult result = apiInstance.complianceResultsGet(apiVersion, resourceId, complianceResultName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComplianceResultsApi#complianceResultsGet");
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
| **apiVersion** | **String**| API version for the operation | |
| **resourceId** | **String**| The identifier of the resource. | |
| **complianceResultName** | **String**| name of the desired assessment compliance result | |

### Return type

[**ComplianceResult**](ComplianceResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="complianceResultsList"></a>
# **complianceResultsList**
> ComplianceResultList complianceResultsList(apiVersion, scope)



Security compliance results in the subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComplianceResultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ComplianceResultsApi apiInstance = new ComplianceResultsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String scope = "scope_example"; // String | Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName).
    try {
      ComplianceResultList result = apiInstance.complianceResultsList(apiVersion, scope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComplianceResultsApi#complianceResultsList");
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
| **apiVersion** | **String**| API version for the operation | |
| **scope** | **String**| Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName). | |

### Return type

[**ComplianceResultList**](ComplianceResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

