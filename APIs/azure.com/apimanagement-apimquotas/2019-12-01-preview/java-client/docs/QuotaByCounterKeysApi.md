# QuotaByCounterKeysApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quotaByCounterKeysListByService**](QuotaByCounterKeysApi.md#quotaByCounterKeysListByService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/quotas/{quotaCounterKey} |  |
| [**quotaByCounterKeysUpdate**](QuotaByCounterKeysApi.md#quotaByCounterKeysUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/quotas/{quotaCounterKey} |  |


<a id="quotaByCounterKeysListByService"></a>
# **quotaByCounterKeysListByService**
> QuotaByCounterKeysListByService200Response quotaByCounterKeysListByService(resourceGroupName, serviceName, quotaCounterKey, apiVersion, subscriptionId)



Lists a collection of current quota counter periods associated with the counter-key configured in the policy on the specified service instance. The api does not support paging yet.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotaByCounterKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QuotaByCounterKeysApi apiInstance = new QuotaByCounterKeysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String quotaCounterKey = "quotaCounterKey_example"; // String | Quota counter key identifier.This is the result of expression defined in counter-key attribute of the quota-by-key policy.For Example, if you specify counter-key=\"boo\" in the policy, then it’s accessible by \"boo\" counter key. But if it’s defined as counter-key=\"@(\"b\"+\"a\")\" then it will be accessible by \"ba\" key
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      QuotaByCounterKeysListByService200Response result = apiInstance.quotaByCounterKeysListByService(resourceGroupName, serviceName, quotaCounterKey, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotaByCounterKeysApi#quotaByCounterKeysListByService");
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
| **quotaCounterKey** | **String**| Quota counter key identifier.This is the result of expression defined in counter-key attribute of the quota-by-key policy.For Example, if you specify counter-key&#x3D;\&quot;boo\&quot; in the policy, then it’s accessible by \&quot;boo\&quot; counter key. But if it’s defined as counter-key&#x3D;\&quot;@(\&quot;b\&quot;+\&quot;a\&quot;)\&quot; then it will be accessible by \&quot;ba\&quot; key | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**QuotaByCounterKeysListByService200Response**](QuotaByCounterKeysListByService200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lists a collection of the quota counter values. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="quotaByCounterKeysUpdate"></a>
# **quotaByCounterKeysUpdate**
> quotaByCounterKeysUpdate(resourceGroupName, serviceName, quotaCounterKey, apiVersion, subscriptionId, parameters)



Updates all the quota counter values specified with the existing quota counter key to a value in the specified service instance. This should be used for reset of the quota counter values.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotaByCounterKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QuotaByCounterKeysApi apiInstance = new QuotaByCounterKeysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String quotaCounterKey = "quotaCounterKey_example"; // String | Quota counter key identifier.This is the result of expression defined in counter-key attribute of the quota-by-key policy.For Example, if you specify counter-key=\"boo\" in the policy, then it’s accessible by \"boo\" counter key. But if it’s defined as counter-key=\"@(\"b\"+\"a\")\" then it will be accessible by \"ba\" key
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    QuotaByCounterKeysListByService200ResponseValueInnerValue parameters = new QuotaByCounterKeysListByService200ResponseValueInnerValue(); // QuotaByCounterKeysListByService200ResponseValueInnerValue | The value of the quota counter to be applied to all quota counter periods.
    try {
      apiInstance.quotaByCounterKeysUpdate(resourceGroupName, serviceName, quotaCounterKey, apiVersion, subscriptionId, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotaByCounterKeysApi#quotaByCounterKeysUpdate");
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
| **quotaCounterKey** | **String**| Quota counter key identifier.This is the result of expression defined in counter-key attribute of the quota-by-key policy.For Example, if you specify counter-key&#x3D;\&quot;boo\&quot; in the policy, then it’s accessible by \&quot;boo\&quot; counter key. But if it’s defined as counter-key&#x3D;\&quot;@(\&quot;b\&quot;+\&quot;a\&quot;)\&quot; then it will be accessible by \&quot;ba\&quot; key | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**QuotaByCounterKeysListByService200ResponseValueInnerValue**](QuotaByCounterKeysListByService200ResponseValueInnerValue.md)| The value of the quota counter to be applied to all quota counter periods. | |

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
| **204** | Quota counter period was successfully updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

