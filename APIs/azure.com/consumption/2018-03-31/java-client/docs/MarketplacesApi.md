# MarketplacesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**marketplacesByBillingAccountList**](MarketplacesApi.md#marketplacesByBillingAccountList) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.Consumption/marketplaces |  |
| [**marketplacesByBillingAccountListByBillingPeriod**](MarketplacesApi.md#marketplacesByBillingAccountListByBillingPeriod) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}/providers/Microsoft.Consumption/marketplaces |  |
| [**marketplacesByDepartmentList**](MarketplacesApi.md#marketplacesByDepartmentList) | **GET** /providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.Consumption/marketplaces |  |
| [**marketplacesByDepartmentListByBillingPeriod**](MarketplacesApi.md#marketplacesByDepartmentListByBillingPeriod) | **GET** /providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}/providers/Microsoft.Consumption/marketplaces |  |
| [**marketplacesByEnrollmentAccountsList**](MarketplacesApi.md#marketplacesByEnrollmentAccountsList) | **GET** /providers/Microsoft.Billing/enrollmentAccounts/{enrollmentAccountId}/providers/Microsoft.Consumption/marketplaces |  |
| [**marketplacesByEnrollmentAccountsListByBillingPeriod**](MarketplacesApi.md#marketplacesByEnrollmentAccountsListByBillingPeriod) | **GET** /providers/Microsoft.Billing/enrollmentAccounts/{enrollmentAccountId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}/providers/Microsoft.Consumption/marketplaces |  |
| [**marketplacesList**](MarketplacesApi.md#marketplacesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Consumption/marketplaces |  |
| [**marketplacesListByBillingPeriod**](MarketplacesApi.md#marketplacesListByBillingPeriod) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}/providers/Microsoft.Consumption/marketplaces |  |


<a id="marketplacesByBillingAccountList"></a>
# **marketplacesByBillingAccountList**
> MarketplacesListResult marketplacesByBillingAccountList(apiVersion, billingAccountId, $filter, $top, $skiptoken)



Lists the marketplaces for a scope by billingAccountId and current billing period. Marketplaces are available via this API only for May 1, 2014 or later.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MarketplacesApi apiInstance = new MarketplacesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-31.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String $filter = "$filter_example"; // String | May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N marketplaces.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    try {
      MarketplacesListResult result = apiInstance.marketplacesByBillingAccountList(apiVersion, billingAccountId, $filter, $top, $skiptoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesApi#marketplacesByBillingAccountList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-31. | |
| **billingAccountId** | **String**| BillingAccount ID | |
| **$filter** | **String**| May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. | [optional] |
| **$top** | **Integer**| May be used to limit the number of results to the most recent N marketplaces. | [optional] |
| **$skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] |

### Return type

[**MarketplacesListResult**](MarketplacesListResult.md)

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

<a id="marketplacesByBillingAccountListByBillingPeriod"></a>
# **marketplacesByBillingAccountListByBillingPeriod**
> MarketplacesListResult marketplacesByBillingAccountListByBillingPeriod(apiVersion, billingAccountId, billingPeriodName, $filter, $top, $skiptoken)



Lists the marketplaces for a scope by billing period and billingAccountId. Marketplaces are available via this API only for May 1, 2014 or later.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MarketplacesApi apiInstance = new MarketplacesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-31.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String billingPeriodName = "billingPeriodName_example"; // String | Billing Period Name.
    String $filter = "$filter_example"; // String | May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N marketplaces.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    try {
      MarketplacesListResult result = apiInstance.marketplacesByBillingAccountListByBillingPeriod(apiVersion, billingAccountId, billingPeriodName, $filter, $top, $skiptoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesApi#marketplacesByBillingAccountListByBillingPeriod");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-31. | |
| **billingAccountId** | **String**| BillingAccount ID | |
| **billingPeriodName** | **String**| Billing Period Name. | |
| **$filter** | **String**| May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. | [optional] |
| **$top** | **Integer**| May be used to limit the number of results to the most recent N marketplaces. | [optional] |
| **$skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] |

### Return type

[**MarketplacesListResult**](MarketplacesListResult.md)

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

<a id="marketplacesByDepartmentList"></a>
# **marketplacesByDepartmentList**
> MarketplacesListResult marketplacesByDepartmentList(apiVersion, departmentId, $filter, $top, $skiptoken)



Lists the marketplaces for a scope by departmentId and current billing period. Marketplaces are available via this API only for May 1, 2014 or later.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MarketplacesApi apiInstance = new MarketplacesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-31.
    String departmentId = "departmentId_example"; // String | Department ID
    String $filter = "$filter_example"; // String | May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N marketplaces.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    try {
      MarketplacesListResult result = apiInstance.marketplacesByDepartmentList(apiVersion, departmentId, $filter, $top, $skiptoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesApi#marketplacesByDepartmentList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-31. | |
| **departmentId** | **String**| Department ID | |
| **$filter** | **String**| May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. | [optional] |
| **$top** | **Integer**| May be used to limit the number of results to the most recent N marketplaces. | [optional] |
| **$skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] |

### Return type

[**MarketplacesListResult**](MarketplacesListResult.md)

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

<a id="marketplacesByDepartmentListByBillingPeriod"></a>
# **marketplacesByDepartmentListByBillingPeriod**
> MarketplacesListResult marketplacesByDepartmentListByBillingPeriod(apiVersion, departmentId, billingPeriodName, $filter, $top, $skiptoken)



Lists the marketplaces for a scope by billing period and departmentId. Marketplaces are available via this API only for May 1, 2014 or later.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MarketplacesApi apiInstance = new MarketplacesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-31.
    String departmentId = "departmentId_example"; // String | Department ID
    String billingPeriodName = "billingPeriodName_example"; // String | Billing Period Name.
    String $filter = "$filter_example"; // String | May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N marketplaces.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    try {
      MarketplacesListResult result = apiInstance.marketplacesByDepartmentListByBillingPeriod(apiVersion, departmentId, billingPeriodName, $filter, $top, $skiptoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesApi#marketplacesByDepartmentListByBillingPeriod");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-31. | |
| **departmentId** | **String**| Department ID | |
| **billingPeriodName** | **String**| Billing Period Name. | |
| **$filter** | **String**| May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. | [optional] |
| **$top** | **Integer**| May be used to limit the number of results to the most recent N marketplaces. | [optional] |
| **$skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] |

### Return type

[**MarketplacesListResult**](MarketplacesListResult.md)

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

<a id="marketplacesByEnrollmentAccountsList"></a>
# **marketplacesByEnrollmentAccountsList**
> MarketplacesListResult marketplacesByEnrollmentAccountsList(apiVersion, enrollmentAccountId, $filter, $top, $skiptoken)



Lists the marketplaces for a scope by enrollmentAccountId and current billing period. Marketplaces are available via this API only for May 1, 2014 or later.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MarketplacesApi apiInstance = new MarketplacesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-31.
    String enrollmentAccountId = "enrollmentAccountId_example"; // String | EnrollmentAccount ID
    String $filter = "$filter_example"; // String | May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N marketplaces.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    try {
      MarketplacesListResult result = apiInstance.marketplacesByEnrollmentAccountsList(apiVersion, enrollmentAccountId, $filter, $top, $skiptoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesApi#marketplacesByEnrollmentAccountsList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-31. | |
| **enrollmentAccountId** | **String**| EnrollmentAccount ID | |
| **$filter** | **String**| May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. | [optional] |
| **$top** | **Integer**| May be used to limit the number of results to the most recent N marketplaces. | [optional] |
| **$skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] |

### Return type

[**MarketplacesListResult**](MarketplacesListResult.md)

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

<a id="marketplacesByEnrollmentAccountsListByBillingPeriod"></a>
# **marketplacesByEnrollmentAccountsListByBillingPeriod**
> MarketplacesListResult marketplacesByEnrollmentAccountsListByBillingPeriod(apiVersion, enrollmentAccountId, billingPeriodName, $filter, $top, $skiptoken)



Lists the marketplaces for a scope by billing period and enrollmentAccountId. Marketplaces are available via this API only for May 1, 2014 or later.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MarketplacesApi apiInstance = new MarketplacesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-31.
    String enrollmentAccountId = "enrollmentAccountId_example"; // String | EnrollmentAccount ID
    String billingPeriodName = "billingPeriodName_example"; // String | Billing Period Name.
    String $filter = "$filter_example"; // String | May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N marketplaces.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    try {
      MarketplacesListResult result = apiInstance.marketplacesByEnrollmentAccountsListByBillingPeriod(apiVersion, enrollmentAccountId, billingPeriodName, $filter, $top, $skiptoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesApi#marketplacesByEnrollmentAccountsListByBillingPeriod");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-31. | |
| **enrollmentAccountId** | **String**| EnrollmentAccount ID | |
| **billingPeriodName** | **String**| Billing Period Name. | |
| **$filter** | **String**| May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. | [optional] |
| **$top** | **Integer**| May be used to limit the number of results to the most recent N marketplaces. | [optional] |
| **$skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] |

### Return type

[**MarketplacesListResult**](MarketplacesListResult.md)

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

<a id="marketplacesList"></a>
# **marketplacesList**
> MarketplacesListResult marketplacesList(apiVersion, subscriptionId, $filter, $top, $skiptoken)



Lists the marketplaces for a scope by subscriptionId and current billing period. Marketplaces are available via this API only for May 1, 2014 or later.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MarketplacesApi apiInstance = new MarketplacesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-31.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String $filter = "$filter_example"; // String | May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N marketplaces.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    try {
      MarketplacesListResult result = apiInstance.marketplacesList(apiVersion, subscriptionId, $filter, $top, $skiptoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesApi#marketplacesList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-31. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **$filter** | **String**| May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. | [optional] |
| **$top** | **Integer**| May be used to limit the number of results to the most recent N marketplaces. | [optional] |
| **$skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] |

### Return type

[**MarketplacesListResult**](MarketplacesListResult.md)

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

<a id="marketplacesListByBillingPeriod"></a>
# **marketplacesListByBillingPeriod**
> MarketplacesListResult marketplacesListByBillingPeriod(apiVersion, subscriptionId, billingPeriodName, $filter, $top, $skiptoken)



Lists the marketplaces for a scope by billing period and subscriptionId. Marketplaces are available via this API only for May 1, 2014 or later.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MarketplacesApi apiInstance = new MarketplacesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-31.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String billingPeriodName = "billingPeriodName_example"; // String | Billing Period Name.
    String $filter = "$filter_example"; // String | May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N marketplaces.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    try {
      MarketplacesListResult result = apiInstance.marketplacesListByBillingPeriod(apiVersion, subscriptionId, billingPeriodName, $filter, $top, $skiptoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesApi#marketplacesListByBillingPeriod");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-31. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **billingPeriodName** | **String**| Billing Period Name. | |
| **$filter** | **String**| May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. | [optional] |
| **$top** | **Integer**| May be used to limit the number of results to the most recent N marketplaces. | [optional] |
| **$skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] |

### Return type

[**MarketplacesListResult**](MarketplacesListResult.md)

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

