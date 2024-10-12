# QuotaByPeriodKeysApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quotaByPeriodKeysGet**](QuotaByPeriodKeysApi.md#quotaByPeriodKeysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/quotas/{quotaCounterKey}/{quotaPeriodKey} |  |
| [**quotaByPeriodKeysUpdate**](QuotaByPeriodKeysApi.md#quotaByPeriodKeysUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/quotas/{quotaCounterKey}/{quotaPeriodKey} |  |


<a id="quotaByPeriodKeysGet"></a>
# **quotaByPeriodKeysGet**
> QuotaCounterContract quotaByPeriodKeysGet(subscriptionId, resourceGroupName, serviceName, quotaCounterKey, quotaPeriodKey, apiVersion)



Gets the value of the quota counter associated with the counter-key in the policy for the specific period in service instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotaByPeriodKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QuotaByPeriodKeysApi apiInstance = new QuotaByPeriodKeysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String quotaCounterKey = "quotaCounterKey_example"; // String | Quota counter key identifier.
    String quotaPeriodKey = "quotaPeriodKey_example"; // String | Quota period key identifier.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      QuotaCounterContract result = apiInstance.quotaByPeriodKeysGet(subscriptionId, resourceGroupName, serviceName, quotaCounterKey, quotaPeriodKey, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotaByPeriodKeysApi#quotaByPeriodKeysGet");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **quotaCounterKey** | **String**| Quota counter key identifier. | |
| **quotaPeriodKey** | **String**| Quota period key identifier. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**QuotaCounterContract**](QuotaCounterContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body contains the Quota counter details for the specified period. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="quotaByPeriodKeysUpdate"></a>
# **quotaByPeriodKeysUpdate**
> quotaByPeriodKeysUpdate(resourceGroupName, serviceName, quotaCounterKey, quotaPeriodKey, apiVersion, subscriptionId, parameters)



Updates an existing quota counter value in the specified service instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotaByPeriodKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QuotaByPeriodKeysApi apiInstance = new QuotaByPeriodKeysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String quotaCounterKey = "quotaCounterKey_example"; // String | Quota counter key identifier.
    String quotaPeriodKey = "quotaPeriodKey_example"; // String | Quota period key identifier.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    QuotaCounterValueContract parameters = new QuotaCounterValueContract(); // QuotaCounterValueContract | The value of the Quota counter to be applied on the specified period.
    try {
      apiInstance.quotaByPeriodKeysUpdate(resourceGroupName, serviceName, quotaCounterKey, quotaPeriodKey, apiVersion, subscriptionId, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotaByPeriodKeysApi#quotaByPeriodKeysUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **quotaCounterKey** | **String**| Quota counter key identifier. | |
| **quotaPeriodKey** | **String**| Quota period key identifier. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**QuotaCounterValueContract**](QuotaCounterValueContract.md)| The value of the Quota counter to be applied on the specified period. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The quota counter value was successfully updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

