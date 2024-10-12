# ExternalBillingAccountsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**externalBillingAccountGet**](ExternalBillingAccountsApi.md#externalBillingAccountGet) | **GET** /providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName} |  |
| [**externalBillingAccountList**](ExternalBillingAccountsApi.md#externalBillingAccountList) | **GET** /providers/Microsoft.CostManagement/externalBillingAccounts |  |


<a id="externalBillingAccountGet"></a>
# **externalBillingAccountGet**
> ExternalBillingAccountDefinition externalBillingAccountGet(apiVersion, externalBillingAccountName, $expand)



Get a ExternalBillingAccount definition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalBillingAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExternalBillingAccountsApi apiInstance = new ExternalBillingAccountsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
    String externalBillingAccountName = "externalBillingAccountName_example"; // String | External Billing Account Name. (eg 'aws-{PayerAccountId}')
    String $expand = "$expand_example"; // String | May be used to expand the collectionInfo property. By default, collectionInfo is not included.
    try {
      ExternalBillingAccountDefinition result = apiInstance.externalBillingAccountGet(apiVersion, externalBillingAccountName, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalBillingAccountsApi#externalBillingAccountGet");
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
| **externalBillingAccountName** | **String**| External Billing Account Name. (eg &#39;aws-{PayerAccountId}&#39;) | |
| **$expand** | **String**| May be used to expand the collectionInfo property. By default, collectionInfo is not included. | [optional] |

### Return type

[**ExternalBillingAccountDefinition**](ExternalBillingAccountDefinition.md)

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

<a id="externalBillingAccountList"></a>
# **externalBillingAccountList**
> ExternalBillingAccountDefinitionListResult externalBillingAccountList(apiVersion)



List all ExternalBillingAccount definitions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalBillingAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExternalBillingAccountsApi apiInstance = new ExternalBillingAccountsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
    try {
      ExternalBillingAccountDefinitionListResult result = apiInstance.externalBillingAccountList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalBillingAccountsApi#externalBillingAccountList");
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

### Return type

[**ExternalBillingAccountDefinitionListResult**](ExternalBillingAccountDefinitionListResult.md)

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

