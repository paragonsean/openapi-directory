# QuotaByPeriodKeysApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quotaByPeriodKeysGet**](QuotaByPeriodKeysApi.md#quotaByPeriodKeysGet) | **GET** /quotas/{quotaCounterKey}/{quotaPeriodKey} |  |
| [**quotaByPeriodKeysUpdate**](QuotaByPeriodKeysApi.md#quotaByPeriodKeysUpdate) | **PATCH** /quotas/{quotaCounterKey}/{quotaPeriodKey} |  |


<a id="quotaByPeriodKeysGet"></a>
# **quotaByPeriodKeysGet**
> QuotaCounterContract quotaByPeriodKeysGet(quotaCounterKey, quotaPeriodKey, apiVersion)



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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    QuotaByPeriodKeysApi apiInstance = new QuotaByPeriodKeysApi(defaultClient);
    String quotaCounterKey = "quotaCounterKey_example"; // String | Quota counter key identifier.This is the result of expression defined in counter-key attribute of the quota-by-key policy.For Example, if you specify counter-key=\"boo\" in the policy, then it’s accessible by \"boo\" counter key. But if it’s defined as counter-key=\"@(\"b\"+\"a\")\" then it will be accessible by \"ba\" key
    String quotaPeriodKey = "quotaPeriodKey_example"; // String | Quota period key identifier.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      QuotaCounterContract result = apiInstance.quotaByPeriodKeysGet(quotaCounterKey, quotaPeriodKey, apiVersion);
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
| **quotaCounterKey** | **String**| Quota counter key identifier.This is the result of expression defined in counter-key attribute of the quota-by-key policy.For Example, if you specify counter-key&#x3D;\&quot;boo\&quot; in the policy, then it’s accessible by \&quot;boo\&quot; counter key. But if it’s defined as counter-key&#x3D;\&quot;@(\&quot;b\&quot;+\&quot;a\&quot;)\&quot; then it will be accessible by \&quot;ba\&quot; key | |
| **quotaPeriodKey** | **String**| Quota period key identifier. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**QuotaCounterContract**](QuotaCounterContract.md)

### Authorization

[apim_key](../README.md#apim_key)

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
> quotaByPeriodKeysUpdate(quotaCounterKey, quotaPeriodKey, apiVersion, parameters)



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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    QuotaByPeriodKeysApi apiInstance = new QuotaByPeriodKeysApi(defaultClient);
    String quotaCounterKey = "quotaCounterKey_example"; // String | Quota counter key identifier.This is the result of expression defined in counter-key attribute of the quota-by-key policy.For Example, if you specify counter-key=\"boo\" in the policy, then it’s accessible by \"boo\" counter key. But if it’s defined as counter-key=\"@(\"b\"+\"a\")\" then it will be accessible by \"ba\" key
    String quotaPeriodKey = "quotaPeriodKey_example"; // String | Quota period key identifier.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    QuotaCounterValueContractProperties parameters = new QuotaCounterValueContractProperties(); // QuotaCounterValueContractProperties | The value of the Quota counter to be applied on the specified period.
    try {
      apiInstance.quotaByPeriodKeysUpdate(quotaCounterKey, quotaPeriodKey, apiVersion, parameters);
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
| **quotaCounterKey** | **String**| Quota counter key identifier.This is the result of expression defined in counter-key attribute of the quota-by-key policy.For Example, if you specify counter-key&#x3D;\&quot;boo\&quot; in the policy, then it’s accessible by \&quot;boo\&quot; counter key. But if it’s defined as counter-key&#x3D;\&quot;@(\&quot;b\&quot;+\&quot;a\&quot;)\&quot; then it will be accessible by \&quot;ba\&quot; key | |
| **quotaPeriodKey** | **String**| Quota period key identifier. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **parameters** | [**QuotaCounterValueContractProperties**](QuotaCounterValueContractProperties.md)| The value of the Quota counter to be applied on the specified period. | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The quota counter value was successfully updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

