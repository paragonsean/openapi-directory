# ReportsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reportsCreateOrUpdate**](ReportsApi.md#reportsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/reports/{reportName} |  |
| [**reportsCreateOrUpdateByBillingAccount**](ReportsApi.md#reportsCreateOrUpdateByBillingAccount) | **PUT** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/reports/{reportName} |  |
| [**reportsCreateOrUpdateByDepartment**](ReportsApi.md#reportsCreateOrUpdateByDepartment) | **PUT** /providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.CostManagement/reports/{reportName} |  |
| [**reportsCreateOrUpdateByResourceGroupName**](ReportsApi.md#reportsCreateOrUpdateByResourceGroupName) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/reports/{reportName} |  |
| [**reportsDelete**](ReportsApi.md#reportsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/reports/{reportName} |  |
| [**reportsDeleteByBillingAccount**](ReportsApi.md#reportsDeleteByBillingAccount) | **DELETE** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/reports/{reportName} |  |
| [**reportsDeleteByDepartment**](ReportsApi.md#reportsDeleteByDepartment) | **DELETE** /providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.CostManagement/reports/{reportName} |  |
| [**reportsDeleteByResourceGroupName**](ReportsApi.md#reportsDeleteByResourceGroupName) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/reports/{reportName} |  |
| [**reportsExecute**](ReportsApi.md#reportsExecute) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/reports/{reportName}/run |  |
| [**reportsExecuteByBillingAccount**](ReportsApi.md#reportsExecuteByBillingAccount) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/reports/{reportName}/run |  |
| [**reportsExecuteByDepartment**](ReportsApi.md#reportsExecuteByDepartment) | **POST** /providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.CostManagement/reports/{reportName}/run |  |
| [**reportsExecuteByResourceGroupName**](ReportsApi.md#reportsExecuteByResourceGroupName) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/reports/{reportName}/run |  |
| [**reportsGet**](ReportsApi.md#reportsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/reports/{reportName} |  |
| [**reportsGetByBillingAccount**](ReportsApi.md#reportsGetByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/reports/{reportName} |  |
| [**reportsGetByDepartment**](ReportsApi.md#reportsGetByDepartment) | **GET** /providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.CostManagement/reports/{reportName} |  |
| [**reportsGetByResourceGroupName**](ReportsApi.md#reportsGetByResourceGroupName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/reports/{reportName} |  |
| [**reportsGetExecutionHistory**](ReportsApi.md#reportsGetExecutionHistory) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/reports/{reportName}/runHistory |  |
| [**reportsGetExecutionHistoryByBillingAccount**](ReportsApi.md#reportsGetExecutionHistoryByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/reports/{reportName}/runHistory |  |
| [**reportsGetExecutionHistoryByDepartment**](ReportsApi.md#reportsGetExecutionHistoryByDepartment) | **GET** /providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.CostManagement/reports/{reportName}/runHistory |  |
| [**reportsGetExecutionHistoryByResourceGroupName**](ReportsApi.md#reportsGetExecutionHistoryByResourceGroupName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/reports/{reportName}/runHistory |  |
| [**reportsList**](ReportsApi.md#reportsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/reports |  |
| [**reportsListByBillingAccount**](ReportsApi.md#reportsListByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/reports |  |
| [**reportsListByDepartment**](ReportsApi.md#reportsListByDepartment) | **GET** /providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.CostManagement/reports |  |
| [**reportsListByResourceGroupName**](ReportsApi.md#reportsListByResourceGroupName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/reports |  |


<a id="reportsCreateOrUpdate"></a>
# **reportsCreateOrUpdate**
> Report reportsCreateOrUpdate(apiVersion, subscriptionId, reportName, parameters)



The operation to create or update a report. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String reportName = "reportName_example"; // String | Report Name.
    Report parameters = new Report(); // Report | Parameters supplied to the CreateOrUpdate Report operation.
    try {
      Report result = apiInstance.reportsCreateOrUpdate(apiVersion, subscriptionId, reportName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsCreateOrUpdate");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **reportName** | **String**| Report Name. | |
| **parameters** | [**Report**](Report.md)| Parameters supplied to the CreateOrUpdate Report operation. | |

### Return type

[**Report**](Report.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **201** | Created. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="reportsCreateOrUpdateByBillingAccount"></a>
# **reportsCreateOrUpdateByBillingAccount**
> Report reportsCreateOrUpdateByBillingAccount(apiVersion, billingAccountId, reportName, parameters)



The operation to create or update a report for billingAccount. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String reportName = "reportName_example"; // String | Report Name.
    Report parameters = new Report(); // Report | Parameters supplied to the CreateOrUpdate Report operation.
    try {
      Report result = apiInstance.reportsCreateOrUpdateByBillingAccount(apiVersion, billingAccountId, reportName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsCreateOrUpdateByBillingAccount");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **billingAccountId** | **String**| BillingAccount ID | |
| **reportName** | **String**| Report Name. | |
| **parameters** | [**Report**](Report.md)| Parameters supplied to the CreateOrUpdate Report operation. | |

### Return type

[**Report**](Report.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **201** | Created. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="reportsCreateOrUpdateByDepartment"></a>
# **reportsCreateOrUpdateByDepartment**
> Report reportsCreateOrUpdateByDepartment(apiVersion, departmentId, reportName, parameters)



The operation to create or update a report for department. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String departmentId = "departmentId_example"; // String | Department ID
    String reportName = "reportName_example"; // String | Report Name.
    Report parameters = new Report(); // Report | Parameters supplied to the CreateOrUpdate Report operation.
    try {
      Report result = apiInstance.reportsCreateOrUpdateByDepartment(apiVersion, departmentId, reportName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsCreateOrUpdateByDepartment");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **departmentId** | **String**| Department ID | |
| **reportName** | **String**| Report Name. | |
| **parameters** | [**Report**](Report.md)| Parameters supplied to the CreateOrUpdate Report operation. | |

### Return type

[**Report**](Report.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **201** | Created. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="reportsCreateOrUpdateByResourceGroupName"></a>
# **reportsCreateOrUpdateByResourceGroupName**
> Report reportsCreateOrUpdateByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportName, parameters)



The operation to create or update a report. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
    String reportName = "reportName_example"; // String | Report Name.
    Report parameters = new Report(); // Report | Parameters supplied to the CreateOrUpdate Report operation.
    try {
      Report result = apiInstance.reportsCreateOrUpdateByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsCreateOrUpdateByResourceGroupName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Azure Resource Group Name. | |
| **reportName** | **String**| Report Name. | |
| **parameters** | [**Report**](Report.md)| Parameters supplied to the CreateOrUpdate Report operation. | |

### Return type

[**Report**](Report.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **201** | Created. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="reportsDelete"></a>
# **reportsDelete**
> reportsDelete(apiVersion, subscriptionId, reportName)



The operation to delete a report.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String reportName = "reportName_example"; // String | Report Name.
    try {
      apiInstance.reportsDelete(apiVersion, subscriptionId, reportName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsDelete");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **reportName** | **String**| Report Name. | |

### Return type

null (empty response body)

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

<a id="reportsDeleteByBillingAccount"></a>
# **reportsDeleteByBillingAccount**
> reportsDeleteByBillingAccount(apiVersion, billingAccountId, reportName)



The operation to delete a report for billing account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String reportName = "reportName_example"; // String | Report Name.
    try {
      apiInstance.reportsDeleteByBillingAccount(apiVersion, billingAccountId, reportName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsDeleteByBillingAccount");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **billingAccountId** | **String**| BillingAccount ID | |
| **reportName** | **String**| Report Name. | |

### Return type

null (empty response body)

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

<a id="reportsDeleteByDepartment"></a>
# **reportsDeleteByDepartment**
> reportsDeleteByDepartment(apiVersion, departmentId, reportName)



The operation to delete a report for department.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String departmentId = "departmentId_example"; // String | Department ID
    String reportName = "reportName_example"; // String | Report Name.
    try {
      apiInstance.reportsDeleteByDepartment(apiVersion, departmentId, reportName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsDeleteByDepartment");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **departmentId** | **String**| Department ID | |
| **reportName** | **String**| Report Name. | |

### Return type

null (empty response body)

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

<a id="reportsDeleteByResourceGroupName"></a>
# **reportsDeleteByResourceGroupName**
> reportsDeleteByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportName)



The operation to delete a report.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
    String reportName = "reportName_example"; // String | Report Name.
    try {
      apiInstance.reportsDeleteByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsDeleteByResourceGroupName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Azure Resource Group Name. | |
| **reportName** | **String**| Report Name. | |

### Return type

null (empty response body)

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

<a id="reportsExecute"></a>
# **reportsExecute**
> reportsExecute(apiVersion, subscriptionId, reportName)



The operation to execute a report.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String reportName = "reportName_example"; // String | Report Name.
    try {
      apiInstance.reportsExecute(apiVersion, subscriptionId, reportName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsExecute");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **reportName** | **String**| Report Name. | |

### Return type

null (empty response body)

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

<a id="reportsExecuteByBillingAccount"></a>
# **reportsExecuteByBillingAccount**
> reportsExecuteByBillingAccount(apiVersion, billingAccountId, reportName)



The operation to execute a report by billing account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String reportName = "reportName_example"; // String | Report Name.
    try {
      apiInstance.reportsExecuteByBillingAccount(apiVersion, billingAccountId, reportName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsExecuteByBillingAccount");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **billingAccountId** | **String**| BillingAccount ID | |
| **reportName** | **String**| Report Name. | |

### Return type

null (empty response body)

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

<a id="reportsExecuteByDepartment"></a>
# **reportsExecuteByDepartment**
> reportsExecuteByDepartment(apiVersion, departmentId, reportName)



The operation to execute a report by department.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String departmentId = "departmentId_example"; // String | Department ID
    String reportName = "reportName_example"; // String | Report Name.
    try {
      apiInstance.reportsExecuteByDepartment(apiVersion, departmentId, reportName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsExecuteByDepartment");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **departmentId** | **String**| Department ID | |
| **reportName** | **String**| Report Name. | |

### Return type

null (empty response body)

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

<a id="reportsExecuteByResourceGroupName"></a>
# **reportsExecuteByResourceGroupName**
> reportsExecuteByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportName)



The operation to execute a report.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
    String reportName = "reportName_example"; // String | Report Name.
    try {
      apiInstance.reportsExecuteByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsExecuteByResourceGroupName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Azure Resource Group Name. | |
| **reportName** | **String**| Report Name. | |

### Return type

null (empty response body)

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

<a id="reportsGet"></a>
# **reportsGet**
> Report reportsGet(apiVersion, subscriptionId, reportName)



Gets the report for a subscription by report name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String reportName = "reportName_example"; // String | Report Name.
    try {
      Report result = apiInstance.reportsGet(apiVersion, subscriptionId, reportName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsGet");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **reportName** | **String**| Report Name. | |

### Return type

[**Report**](Report.md)

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

<a id="reportsGetByBillingAccount"></a>
# **reportsGetByBillingAccount**
> Report reportsGetByBillingAccount(apiVersion, billingAccountId, reportName)



Gets the report for a billing account by report name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String reportName = "reportName_example"; // String | Report Name.
    try {
      Report result = apiInstance.reportsGetByBillingAccount(apiVersion, billingAccountId, reportName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsGetByBillingAccount");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **billingAccountId** | **String**| BillingAccount ID | |
| **reportName** | **String**| Report Name. | |

### Return type

[**Report**](Report.md)

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

<a id="reportsGetByDepartment"></a>
# **reportsGetByDepartment**
> Report reportsGetByDepartment(apiVersion, departmentId, reportName)



Gets the report for a department by report name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String departmentId = "departmentId_example"; // String | Department ID
    String reportName = "reportName_example"; // String | Report Name.
    try {
      Report result = apiInstance.reportsGetByDepartment(apiVersion, departmentId, reportName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsGetByDepartment");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **departmentId** | **String**| Department ID | |
| **reportName** | **String**| Report Name. | |

### Return type

[**Report**](Report.md)

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

<a id="reportsGetByResourceGroupName"></a>
# **reportsGetByResourceGroupName**
> Report reportsGetByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportName)



Gets the report for a resource group under a subscription by report name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
    String reportName = "reportName_example"; // String | Report Name.
    try {
      Report result = apiInstance.reportsGetByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsGetByResourceGroupName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Azure Resource Group Name. | |
| **reportName** | **String**| Report Name. | |

### Return type

[**Report**](Report.md)

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

<a id="reportsGetExecutionHistory"></a>
# **reportsGetExecutionHistory**
> ReportExecutionListResult reportsGetExecutionHistory(apiVersion, subscriptionId, reportName)



Gets the execution history of a report for a subscription by report name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String reportName = "reportName_example"; // String | Report Name.
    try {
      ReportExecutionListResult result = apiInstance.reportsGetExecutionHistory(apiVersion, subscriptionId, reportName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsGetExecutionHistory");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **reportName** | **String**| Report Name. | |

### Return type

[**ReportExecutionListResult**](ReportExecutionListResult.md)

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

<a id="reportsGetExecutionHistoryByBillingAccount"></a>
# **reportsGetExecutionHistoryByBillingAccount**
> ReportExecutionListResult reportsGetExecutionHistoryByBillingAccount(apiVersion, billingAccountId, reportName)



Gets the execution history of a report for a billing account by report name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String reportName = "reportName_example"; // String | Report Name.
    try {
      ReportExecutionListResult result = apiInstance.reportsGetExecutionHistoryByBillingAccount(apiVersion, billingAccountId, reportName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsGetExecutionHistoryByBillingAccount");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **billingAccountId** | **String**| BillingAccount ID | |
| **reportName** | **String**| Report Name. | |

### Return type

[**ReportExecutionListResult**](ReportExecutionListResult.md)

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

<a id="reportsGetExecutionHistoryByDepartment"></a>
# **reportsGetExecutionHistoryByDepartment**
> ReportExecutionListResult reportsGetExecutionHistoryByDepartment(apiVersion, departmentId, reportName)



Gets the execution history of a report for a department by report name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String departmentId = "departmentId_example"; // String | Department ID
    String reportName = "reportName_example"; // String | Report Name.
    try {
      ReportExecutionListResult result = apiInstance.reportsGetExecutionHistoryByDepartment(apiVersion, departmentId, reportName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsGetExecutionHistoryByDepartment");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **departmentId** | **String**| Department ID | |
| **reportName** | **String**| Report Name. | |

### Return type

[**ReportExecutionListResult**](ReportExecutionListResult.md)

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

<a id="reportsGetExecutionHistoryByResourceGroupName"></a>
# **reportsGetExecutionHistoryByResourceGroupName**
> ReportExecutionListResult reportsGetExecutionHistoryByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportName)



Gets the execution history of a report for a resource group by report name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
    String reportName = "reportName_example"; // String | Report Name.
    try {
      ReportExecutionListResult result = apiInstance.reportsGetExecutionHistoryByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsGetExecutionHistoryByResourceGroupName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Azure Resource Group Name. | |
| **reportName** | **String**| Report Name. | |

### Return type

[**ReportExecutionListResult**](ReportExecutionListResult.md)

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

<a id="reportsList"></a>
# **reportsList**
> ReportListResult reportsList(apiVersion, subscriptionId)



Lists all reports for a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    try {
      ReportListResult result = apiInstance.reportsList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |

### Return type

[**ReportListResult**](ReportListResult.md)

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

<a id="reportsListByBillingAccount"></a>
# **reportsListByBillingAccount**
> ReportListResult reportsListByBillingAccount(apiVersion, billingAccountId)



Lists all reports for a billing account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    try {
      ReportListResult result = apiInstance.reportsListByBillingAccount(apiVersion, billingAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsListByBillingAccount");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **billingAccountId** | **String**| BillingAccount ID | |

### Return type

[**ReportListResult**](ReportListResult.md)

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

<a id="reportsListByDepartment"></a>
# **reportsListByDepartment**
> ReportListResult reportsListByDepartment(apiVersion, departmentId)



Lists all reports for a department.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String departmentId = "departmentId_example"; // String | Department ID
    try {
      ReportListResult result = apiInstance.reportsListByDepartment(apiVersion, departmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsListByDepartment");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **departmentId** | **String**| Department ID | |

### Return type

[**ReportListResult**](ReportListResult.md)

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

<a id="reportsListByResourceGroupName"></a>
# **reportsListByResourceGroupName**
> ReportListResult reportsListByResourceGroupName(apiVersion, subscriptionId, resourceGroupName)



Lists all reports for a resource group under a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
    try {
      ReportListResult result = apiInstance.reportsListByResourceGroupName(apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsListByResourceGroupName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Azure Resource Group Name. | |

### Return type

[**ReportListResult**](ReportListResult.md)

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

