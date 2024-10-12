# QuotaApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quotasList**](QuotaApi.md#quotasList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MachineLearningServices/locations/{location}/Quotas |  |
| [**quotasUpdate**](QuotaApi.md#quotasUpdate) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.MachineLearningServices/locations/{location}/updateQuotas |  |


<a id="quotasList"></a>
# **quotasList**
> ListWorkspaceQuotas quotasList(apiVersion, subscriptionId, location)



Gets the currently assigned Workspace Quotas based on VMFamily.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QuotaApi apiInstance = new QuotaApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    String location = "location_example"; // String | The location for which resource usage is queried.
    try {
      ListWorkspaceQuotas result = apiInstance.quotasList(apiVersion, subscriptionId, location);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotaApi#quotasList");
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
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **location** | **String**| The location for which resource usage is queried. | |

### Return type

[**ListWorkspaceQuotas**](ListWorkspaceQuotas.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="quotasUpdate"></a>
# **quotasUpdate**
> UpdateWorkspaceQuotasResult quotasUpdate(location, apiVersion, subscriptionId, parameters)



Update quota for each VM family in workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QuotaApi apiInstance = new QuotaApi(defaultClient);
    String location = "location_example"; // String | The location for update quota is queried.
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    QuotaUpdateParameters parameters = new QuotaUpdateParameters(); // QuotaUpdateParameters | Quota update parameters.
    try {
      UpdateWorkspaceQuotasResult result = apiInstance.quotasUpdate(location, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotaApi#quotasUpdate");
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
| **location** | **String**| The location for update quota is queried. | |
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **parameters** | [**QuotaUpdateParameters**](QuotaUpdateParameters.md)| Quota update parameters. | |

### Return type

[**UpdateWorkspaceQuotasResult**](UpdateWorkspaceQuotasResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

