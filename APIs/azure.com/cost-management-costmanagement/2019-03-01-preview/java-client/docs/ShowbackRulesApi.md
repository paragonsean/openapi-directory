# ShowbackRulesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**showbackRuleCreateUpdateRule**](ShowbackRulesApi.md#showbackRuleCreateUpdateRule) | **PUT** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/showbackRules/{ruleName} |  |
| [**showbackRuleGetBillingAccountId**](ShowbackRulesApi.md#showbackRuleGetBillingAccountId) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/showbackRules/{ruleName} |  |
| [**showbackRulesList**](ShowbackRulesApi.md#showbackRulesList) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/showbackRules |  |


<a id="showbackRuleCreateUpdateRule"></a>
# **showbackRuleCreateUpdateRule**
> ShowbackRule showbackRuleCreateUpdateRule(apiVersion, billingAccountId, ruleName, showbackRule)



Create/Update showback rule for billing account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShowbackRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShowbackRulesApi apiInstance = new ShowbackRulesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String ruleName = "ruleName_example"; // String | Showback rule name
    ShowbackRule showbackRule = new ShowbackRule(); // ShowbackRule | Showback rule to create or update.
    try {
      ShowbackRule result = apiInstance.showbackRuleCreateUpdateRule(apiVersion, billingAccountId, ruleName, showbackRule);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShowbackRulesApi#showbackRuleCreateUpdateRule");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | |
| **billingAccountId** | **String**| BillingAccount ID | |
| **ruleName** | **String**| Showback rule name | |
| **showbackRule** | [**ShowbackRule**](ShowbackRule.md)| Showback rule to create or update. | |

### Return type

[**ShowbackRule**](ShowbackRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="showbackRuleGetBillingAccountId"></a>
# **showbackRuleGetBillingAccountId**
> ShowbackRule showbackRuleGetBillingAccountId(apiVersion, billingAccountId, ruleName)



Gets the showback rule by rule name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShowbackRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShowbackRulesApi apiInstance = new ShowbackRulesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String ruleName = "ruleName_example"; // String | Showback rule name
    try {
      ShowbackRule result = apiInstance.showbackRuleGetBillingAccountId(apiVersion, billingAccountId, ruleName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShowbackRulesApi#showbackRuleGetBillingAccountId");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | |
| **billingAccountId** | **String**| BillingAccount ID | |
| **ruleName** | **String**| Showback rule name | |

### Return type

[**ShowbackRule**](ShowbackRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="showbackRulesList"></a>
# **showbackRulesList**
> ShowbackRuleListResult showbackRulesList(apiVersion, billingAccountId)



Get list all Showback Rules.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShowbackRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShowbackRulesApi apiInstance = new ShowbackRulesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    try {
      ShowbackRuleListResult result = apiInstance.showbackRulesList(apiVersion, billingAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShowbackRulesApi#showbackRulesList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | |
| **billingAccountId** | **String**| BillingAccount ID | |

### Return type

[**ShowbackRuleListResult**](ShowbackRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

