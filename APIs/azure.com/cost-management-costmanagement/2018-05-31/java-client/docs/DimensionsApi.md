# DimensionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**billingAccountDimensionsList**](DimensionsApi.md#billingAccountDimensionsList) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/dimensions |  |
| [**resourceGroupDimensionsList**](DimensionsApi.md#resourceGroupDimensionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/dimensions |  |
| [**subscriptionDimensionsList**](DimensionsApi.md#subscriptionDimensionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/dimensions |  |


<a id="billingAccountDimensionsList"></a>
# **billingAccountDimensionsList**
> DimensionsListResult billingAccountDimensionsList(apiVersion, billingAccountId, $filter, $expand, $skiptoken, $top)



Lists the dimensions by billingAccount Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DimensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DimensionsApi apiInstance = new DimensionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String $filter = "$filter_example"; // String | May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
    String $expand = "$expand_example"; // String | May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N dimension data.
    try {
      DimensionsListResult result = apiInstance.billingAccountDimensionsList(apiVersion, billingAccountId, $filter, $expand, $skiptoken, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DimensionsApi#billingAccountDimensionsList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-05-31. | |
| **billingAccountId** | **String**| BillingAccount ID | |
| **$filter** | **String**| May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;. | [optional] |
| **$expand** | **String**| May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions. | [optional] |
| **$skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] |
| **$top** | **Integer**| May be used to limit the number of results to the most recent N dimension data. | [optional] |

### Return type

[**DimensionsListResult**](DimensionsListResult.md)

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

<a id="resourceGroupDimensionsList"></a>
# **resourceGroupDimensionsList**
> DimensionsListResult resourceGroupDimensionsList(apiVersion, subscriptionId, resourceGroupName, $filter, $expand, $skiptoken, $top)



Lists the dimensions by resource group Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DimensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DimensionsApi apiInstance = new DimensionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
    String $filter = "$filter_example"; // String | May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
    String $expand = "$expand_example"; // String | May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N dimension data.
    try {
      DimensionsListResult result = apiInstance.resourceGroupDimensionsList(apiVersion, subscriptionId, resourceGroupName, $filter, $expand, $skiptoken, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DimensionsApi#resourceGroupDimensionsList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-05-31. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Azure Resource Group Name. | |
| **$filter** | **String**| May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;. | [optional] |
| **$expand** | **String**| May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions. | [optional] |
| **$skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] |
| **$top** | **Integer**| May be used to limit the number of results to the most recent N dimension data. | [optional] |

### Return type

[**DimensionsListResult**](DimensionsListResult.md)

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

<a id="subscriptionDimensionsList"></a>
# **subscriptionDimensionsList**
> DimensionsListResult subscriptionDimensionsList(apiVersion, subscriptionId, $filter, $expand, $skiptoken, $top)



Lists the dimensions by subscription Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DimensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DimensionsApi apiInstance = new DimensionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String $filter = "$filter_example"; // String | May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
    String $expand = "$expand_example"; // String | May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N dimension data.
    try {
      DimensionsListResult result = apiInstance.subscriptionDimensionsList(apiVersion, subscriptionId, $filter, $expand, $skiptoken, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DimensionsApi#subscriptionDimensionsList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-05-31. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **$filter** | **String**| May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;. | [optional] |
| **$expand** | **String**| May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions. | [optional] |
| **$skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] |
| **$top** | **Integer**| May be used to limit the number of results to the most recent N dimension data. | [optional] |

### Return type

[**DimensionsListResult**](DimensionsListResult.md)

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

