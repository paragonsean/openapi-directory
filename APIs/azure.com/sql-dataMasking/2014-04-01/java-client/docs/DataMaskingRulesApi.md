# DataMaskingRulesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dataMaskingRulesCreateOrUpdate**](DataMaskingRulesApi.md#dataMaskingRulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/dataMaskingPolicies/{dataMaskingPolicyName}/rules/{dataMaskingRuleName} |  |
| [**dataMaskingRulesListByDatabase**](DataMaskingRulesApi.md#dataMaskingRulesListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/dataMaskingPolicies/{dataMaskingPolicyName}/rules |  |


<a id="dataMaskingRulesCreateOrUpdate"></a>
# **dataMaskingRulesCreateOrUpdate**
> DataMaskingRule dataMaskingRulesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, dataMaskingPolicyName, dataMaskingRuleName, parameters)



Creates or updates a database data masking rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataMaskingRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DataMaskingRulesApi apiInstance = new DataMaskingRulesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String dataMaskingPolicyName = "Default"; // String | The name of the database for which the data masking rule applies.
    String dataMaskingRuleName = "dataMaskingRuleName_example"; // String | The name of the data masking rule.
    DataMaskingRule parameters = new DataMaskingRule(); // DataMaskingRule | The required parameters for creating or updating a data masking rule.
    try {
      DataMaskingRule result = apiInstance.dataMaskingRulesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, dataMaskingPolicyName, dataMaskingRuleName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataMaskingRulesApi#dataMaskingRulesCreateOrUpdate");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **databaseName** | **String**| The name of the database. | |
| **dataMaskingPolicyName** | **String**| The name of the database for which the data masking rule applies. | [enum: Default] |
| **dataMaskingRuleName** | **String**| The name of the data masking rule. | |
| **parameters** | [**DataMaskingRule**](DataMaskingRule.md)| The required parameters for creating or updating a data masking rule. | |

### Return type

[**DataMaskingRule**](DataMaskingRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |

<a id="dataMaskingRulesListByDatabase"></a>
# **dataMaskingRulesListByDatabase**
> DataMaskingRuleListResult dataMaskingRulesListByDatabase(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, dataMaskingPolicyName)



Gets a list of database data masking rules.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataMaskingRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DataMaskingRulesApi apiInstance = new DataMaskingRulesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String dataMaskingPolicyName = "Default"; // String | The name of the database for which the data masking rule applies.
    try {
      DataMaskingRuleListResult result = apiInstance.dataMaskingRulesListByDatabase(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, dataMaskingPolicyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataMaskingRulesApi#dataMaskingRulesListByDatabase");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **databaseName** | **String**| The name of the database. | |
| **dataMaskingPolicyName** | **String**| The name of the database for which the data masking rule applies. | [enum: Default] |

### Return type

[**DataMaskingRuleListResult**](DataMaskingRuleListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

