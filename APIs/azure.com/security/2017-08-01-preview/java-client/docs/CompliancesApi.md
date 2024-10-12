# CompliancesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**compliancesGet**](CompliancesApi.md#compliancesGet) | **GET** /{scope}/providers/Microsoft.Security/compliances/{complianceName} |  |
| [**compliancesList**](CompliancesApi.md#compliancesList) | **GET** /{scope}/providers/Microsoft.Security/compliances |  |


<a id="compliancesGet"></a>
# **compliancesGet**
> Compliance compliancesGet(apiVersion, scope, complianceName)



Details of a specific Compliance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompliancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CompliancesApi apiInstance = new CompliancesApi(defaultClient);
    String apiVersion = "2017-08-01-preview"; // String | API version for the operation
    String scope = "scope_example"; // String | Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName).
    String complianceName = "complianceName_example"; // String | name of the Compliance
    try {
      Compliance result = apiInstance.compliancesGet(apiVersion, scope, complianceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompliancesApi#compliancesGet");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2017-08-01-preview] |
| **scope** | **String**| Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName). | |
| **complianceName** | **String**| name of the Compliance | |

### Return type

[**Compliance**](Compliance.md)

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

<a id="compliancesList"></a>
# **compliancesList**
> ComplianceList compliancesList(apiVersion, scope)



The Compliance scores of the specific management group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompliancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CompliancesApi apiInstance = new CompliancesApi(defaultClient);
    String apiVersion = "2017-08-01-preview"; // String | API version for the operation
    String scope = "scope_example"; // String | Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName).
    try {
      ComplianceList result = apiInstance.compliancesList(apiVersion, scope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompliancesApi#compliancesList");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2017-08-01-preview] |
| **scope** | **String**| Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName). | |

### Return type

[**ComplianceList**](ComplianceList.md)

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

