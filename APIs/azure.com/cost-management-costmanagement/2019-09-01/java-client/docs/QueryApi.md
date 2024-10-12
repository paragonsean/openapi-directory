# QueryApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**queryUsageByScope**](QueryApi.md#queryUsageByScope) | **POST** /{scope}/providers/Microsoft.CostManagement/query |  |


<a id="queryUsageByScope"></a>
# **queryUsageByScope**
> QueryResult queryUsageByScope(scope, apiVersion, parameters)



Query the usage data for scope defined.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QueryApi apiInstance = new QueryApi(defaultClient);
    String scope = "scope_example"; // String | The scope associated with query and export operations. This includes '/subscriptions/{subscriptionId}/' for subscription scope, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope and '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group scope..
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    QueryDefinition parameters = new QueryDefinition(); // QueryDefinition | Parameters supplied to the CreateOrUpdate Query Config operation.
    try {
      QueryResult result = apiInstance.queryUsageByScope(scope, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApi#queryUsageByScope");
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
| **scope** | **String**| The scope associated with query and export operations. This includes &#39;/subscriptions/{subscriptionId}/&#39; for subscription scope, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope and &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope and &#39;/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group scope.. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-05-31. | |
| **parameters** | [**QueryDefinition**](QueryDefinition.md)| Parameters supplied to the CreateOrUpdate Query Config operation. | |

### Return type

[**QueryResult**](QueryResult.md)

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

