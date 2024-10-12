# QueryApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**queryUsageByBillingAccount**](QueryApi.md#queryUsageByBillingAccount) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/Query |  |
| [**queryUsageByDepartment**](QueryApi.md#queryUsageByDepartment) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}/providers/Microsoft.CostManagement/Query |  |
| [**queryUsageByEnrollmentAccount**](QueryApi.md#queryUsageByEnrollmentAccount) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}/providers/Microsoft.CostManagement/Query |  |
| [**queryUsageByManagmentGroup**](QueryApi.md#queryUsageByManagmentGroup) | **POST** /providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.CostManagement/Query |  |
| [**queryUsageByResourceGroup**](QueryApi.md#queryUsageByResourceGroup) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.CostManagement/Query |  |
| [**queryUsageBySubscription**](QueryApi.md#queryUsageBySubscription) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/Query |  |


<a id="queryUsageByBillingAccount"></a>
# **queryUsageByBillingAccount**
> QueryResult queryUsageByBillingAccount(apiVersion, billingAccountId, parameters)



Query the usage data for billing account.

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    ReportConfigDefinition parameters = new ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
    try {
      QueryResult result = apiInstance.queryUsageByBillingAccount(apiVersion, billingAccountId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApi#queryUsageByBillingAccount");
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
| **parameters** | [**ReportConfigDefinition**](ReportConfigDefinition.md)| Parameters supplied to the CreateOrUpdate Report Config operation. | |

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

<a id="queryUsageByDepartment"></a>
# **queryUsageByDepartment**
> QueryResult queryUsageByDepartment(apiVersion, billingAccountId, departmentId, parameters)



Query the usage data for department.

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String departmentId = "departmentId_example"; // String | Department ID
    ReportConfigDefinition parameters = new ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
    try {
      QueryResult result = apiInstance.queryUsageByDepartment(apiVersion, billingAccountId, departmentId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApi#queryUsageByDepartment");
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
| **departmentId** | **String**| Department ID | |
| **parameters** | [**ReportConfigDefinition**](ReportConfigDefinition.md)| Parameters supplied to the CreateOrUpdate Report Config operation. | |

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

<a id="queryUsageByEnrollmentAccount"></a>
# **queryUsageByEnrollmentAccount**
> QueryResult queryUsageByEnrollmentAccount(apiVersion, billingAccountId, enrollmentAccountId, parameters)



Query the usage data for an enrollment account.

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String enrollmentAccountId = "enrollmentAccountId_example"; // String | Enrollment Account ID
    ReportConfigDefinition parameters = new ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
    try {
      QueryResult result = apiInstance.queryUsageByEnrollmentAccount(apiVersion, billingAccountId, enrollmentAccountId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApi#queryUsageByEnrollmentAccount");
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
| **enrollmentAccountId** | **String**| Enrollment Account ID | |
| **parameters** | [**ReportConfigDefinition**](ReportConfigDefinition.md)| Parameters supplied to the CreateOrUpdate Report Config operation. | |

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

<a id="queryUsageByManagmentGroup"></a>
# **queryUsageByManagmentGroup**
> QueryResult queryUsageByManagmentGroup(apiVersion, managementGroupId, parameters)



Lists the usage data for management group.

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String managementGroupId = "managementGroupId_example"; // String | ManagementGroup ID
    ReportConfigDefinition parameters = new ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
    try {
      QueryResult result = apiInstance.queryUsageByManagmentGroup(apiVersion, managementGroupId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApi#queryUsageByManagmentGroup");
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
| **managementGroupId** | **String**| ManagementGroup ID | |
| **parameters** | [**ReportConfigDefinition**](ReportConfigDefinition.md)| Parameters supplied to the CreateOrUpdate Report Config operation. | |

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

<a id="queryUsageByResourceGroup"></a>
# **queryUsageByResourceGroup**
> QueryResult queryUsageByResourceGroup(apiVersion, subscriptionId, resourceGroupName, parameters)



Query the usage data for subscriptionId and resource group.

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
    ReportConfigDefinition parameters = new ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
    try {
      QueryResult result = apiInstance.queryUsageByResourceGroup(apiVersion, subscriptionId, resourceGroupName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApi#queryUsageByResourceGroup");
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
| **parameters** | [**ReportConfigDefinition**](ReportConfigDefinition.md)| Parameters supplied to the CreateOrUpdate Report Config operation. | |

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

<a id="queryUsageBySubscription"></a>
# **queryUsageBySubscription**
> QueryResult queryUsageBySubscription(apiVersion, subscriptionId, parameters)



Query the usage data for subscriptionId.

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    ReportConfigDefinition parameters = new ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
    try {
      QueryResult result = apiInstance.queryUsageBySubscription(apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApi#queryUsageBySubscription");
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
| **parameters** | [**ReportConfigDefinition**](ReportConfigDefinition.md)| Parameters supplied to the CreateOrUpdate Report Config operation. | |

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

