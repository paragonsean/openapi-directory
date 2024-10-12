# DimensionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dimensionsListByBillingAccount**](DimensionsApi.md#dimensionsListByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/dimensions |  |
| [**dimensionsListByDepartment**](DimensionsApi.md#dimensionsListByDepartment) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}/providers/Microsoft.CostManagement/dimensions |  |
| [**dimensionsListByEnrollmentAccount**](DimensionsApi.md#dimensionsListByEnrollmentAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}/providers/Microsoft.CostManagement/dimensions |  |
| [**dimensionsListByManagementGroup**](DimensionsApi.md#dimensionsListByManagementGroup) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.CostManagement/dimensions |  |
| [**dimensionsListByResourceGroup**](DimensionsApi.md#dimensionsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/dimensions |  |
| [**dimensionsListBySubscription**](DimensionsApi.md#dimensionsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/dimensions |  |


<a id="dimensionsListByBillingAccount"></a>
# **dimensionsListByBillingAccount**
> DimensionsListResult dimensionsListByBillingAccount(apiVersion, billingAccountId, $filter, $expand, $skiptoken, $top)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String $filter = "$filter_example"; // String | May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
    String $expand = "$expand_example"; // String | May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N dimension data.
    try {
      DimensionsListResult result = apiInstance.dimensionsListByBillingAccount(apiVersion, billingAccountId, $filter, $expand, $skiptoken, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DimensionsApi#dimensionsListByBillingAccount");
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

<a id="dimensionsListByDepartment"></a>
# **dimensionsListByDepartment**
> DimensionsListResult dimensionsListByDepartment(apiVersion, billingAccountId, departmentId, $filter, $expand, $skiptoken, $top)



Lists the dimensions by Department Id.

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String departmentId = "departmentId_example"; // String | Department ID
    String $filter = "$filter_example"; // String | May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
    String $expand = "$expand_example"; // String | May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N dimension data.
    try {
      DimensionsListResult result = apiInstance.dimensionsListByDepartment(apiVersion, billingAccountId, departmentId, $filter, $expand, $skiptoken, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DimensionsApi#dimensionsListByDepartment");
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
| **departmentId** | **String**| Department ID | |
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

<a id="dimensionsListByEnrollmentAccount"></a>
# **dimensionsListByEnrollmentAccount**
> DimensionsListResult dimensionsListByEnrollmentAccount(apiVersion, billingAccountId, enrollmentAccountId, $filter, $expand, $skiptoken, $top)



Lists the dimensions by Enrollment Account Id.

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String enrollmentAccountId = "enrollmentAccountId_example"; // String | Enrollment Account ID
    String $filter = "$filter_example"; // String | May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
    String $expand = "$expand_example"; // String | May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N dimension data.
    try {
      DimensionsListResult result = apiInstance.dimensionsListByEnrollmentAccount(apiVersion, billingAccountId, enrollmentAccountId, $filter, $expand, $skiptoken, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DimensionsApi#dimensionsListByEnrollmentAccount");
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
| **enrollmentAccountId** | **String**| Enrollment Account ID | |
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

<a id="dimensionsListByManagementGroup"></a>
# **dimensionsListByManagementGroup**
> DimensionsListResult dimensionsListByManagementGroup(apiVersion, managementGroupId, $filter, $expand, $skiptoken, $top)



Lists the dimensions by managementGroup Id.

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
    String managementGroupId = "managementGroupId_example"; // String | ManagementGroup ID
    String $filter = "$filter_example"; // String | May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
    String $expand = "$expand_example"; // String | May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N dimension data.
    try {
      DimensionsListResult result = apiInstance.dimensionsListByManagementGroup(apiVersion, managementGroupId, $filter, $expand, $skiptoken, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DimensionsApi#dimensionsListByManagementGroup");
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
| **managementGroupId** | **String**| ManagementGroup ID | |
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

<a id="dimensionsListByResourceGroup"></a>
# **dimensionsListByResourceGroup**
> DimensionsListResult dimensionsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, $filter, $expand, $skiptoken, $top)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
    String $filter = "$filter_example"; // String | May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
    String $expand = "$expand_example"; // String | May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N dimension data.
    try {
      DimensionsListResult result = apiInstance.dimensionsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, $filter, $expand, $skiptoken, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DimensionsApi#dimensionsListByResourceGroup");
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

<a id="dimensionsListBySubscription"></a>
# **dimensionsListBySubscription**
> DimensionsListResult dimensionsListBySubscription(apiVersion, subscriptionId, $filter, $expand, $skiptoken, $top)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String $filter = "$filter_example"; // String | May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
    String $expand = "$expand_example"; // String | May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N dimension data.
    try {
      DimensionsListResult result = apiInstance.dimensionsListBySubscription(apiVersion, subscriptionId, $filter, $expand, $skiptoken, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DimensionsApi#dimensionsListBySubscription");
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

