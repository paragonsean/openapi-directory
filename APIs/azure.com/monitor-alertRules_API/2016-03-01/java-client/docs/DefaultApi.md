# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**alertRulesUpdate**](DefaultApi.md#alertRulesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/alertrules/{ruleName} |  |


<a id="alertRulesUpdate"></a>
# **alertRulesUpdate**
> AlertRuleResource alertRulesUpdate(subscriptionId, resourceGroupName, ruleName, apiVersion, alertRulesResource)



Updates an existing AlertRuleResource. To update other fields use the CreateOrUpdate method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String ruleName = "ruleName_example"; // String | The name of the rule.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    AlertRuleResourcePatch alertRulesResource = new AlertRuleResourcePatch(); // AlertRuleResourcePatch | Parameters supplied to the operation.
    try {
      AlertRuleResource result = apiInstance.alertRulesUpdate(subscriptionId, resourceGroupName, ruleName, apiVersion, alertRulesResource);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#alertRulesUpdate");
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
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **ruleName** | **String**| The name of the rule. | |
| **apiVersion** | **String**| Client Api Version. | |
| **alertRulesResource** | [**AlertRuleResourcePatch**](AlertRuleResourcePatch.md)| Parameters supplied to the operation. | |

### Return type

[**AlertRuleResource**](AlertRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to update an alert rule |  -  |
| **201** | Successful request to update an alert rule that resulted in a creation of the alert rule |  -  |
| **0** | Error response describing why the operation failed. |  -  |

