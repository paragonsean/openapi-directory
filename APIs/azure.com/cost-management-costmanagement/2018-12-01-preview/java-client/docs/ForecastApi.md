# ForecastApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**forecastUsageByBillingAccount**](ForecastApi.md#forecastUsageByBillingAccount) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/Forecast |  |
| [**forecastUsageByDepartment**](ForecastApi.md#forecastUsageByDepartment) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}/providers/Microsoft.CostManagement/Forecast |  |
| [**forecastUsageByEnrollmentAccount**](ForecastApi.md#forecastUsageByEnrollmentAccount) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}/providers/Microsoft.CostManagement/Forecast |  |
| [**forecastUsageByManagmentGroup**](ForecastApi.md#forecastUsageByManagmentGroup) | **POST** /providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.CostManagement/Forecast |  |
| [**forecastUsageByResourceGroup**](ForecastApi.md#forecastUsageByResourceGroup) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.CostManagement/Forecast |  |
| [**forecastUsageBySubscription**](ForecastApi.md#forecastUsageBySubscription) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/Forecast |  |


<a id="forecastUsageByBillingAccount"></a>
# **forecastUsageByBillingAccount**
> QueryResult forecastUsageByBillingAccount(apiVersion, billingAccountId, parameters)



Forecast the usage data for billing account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForecastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ForecastApi apiInstance = new ForecastApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    ReportConfigDefinition parameters = new ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
    try {
      QueryResult result = apiInstance.forecastUsageByBillingAccount(apiVersion, billingAccountId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForecastApi#forecastUsageByBillingAccount");
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

<a id="forecastUsageByDepartment"></a>
# **forecastUsageByDepartment**
> QueryResult forecastUsageByDepartment(apiVersion, billingAccountId, departmentId, parameters)



Forecast the usage data for department.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForecastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ForecastApi apiInstance = new ForecastApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String departmentId = "departmentId_example"; // String | Department ID
    ReportConfigDefinition parameters = new ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
    try {
      QueryResult result = apiInstance.forecastUsageByDepartment(apiVersion, billingAccountId, departmentId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForecastApi#forecastUsageByDepartment");
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

<a id="forecastUsageByEnrollmentAccount"></a>
# **forecastUsageByEnrollmentAccount**
> QueryResult forecastUsageByEnrollmentAccount(apiVersion, billingAccountId, enrollmentAccountId, parameters)



Forecast the usage data for an enrollment account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForecastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ForecastApi apiInstance = new ForecastApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String enrollmentAccountId = "enrollmentAccountId_example"; // String | Enrollment Account ID
    ReportConfigDefinition parameters = new ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
    try {
      QueryResult result = apiInstance.forecastUsageByEnrollmentAccount(apiVersion, billingAccountId, enrollmentAccountId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForecastApi#forecastUsageByEnrollmentAccount");
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

<a id="forecastUsageByManagmentGroup"></a>
# **forecastUsageByManagmentGroup**
> QueryResult forecastUsageByManagmentGroup(apiVersion, managementGroupId, parameters)



Lists the usage data for management group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForecastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ForecastApi apiInstance = new ForecastApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String managementGroupId = "managementGroupId_example"; // String | ManagementGroup ID
    ReportConfigDefinition parameters = new ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
    try {
      QueryResult result = apiInstance.forecastUsageByManagmentGroup(apiVersion, managementGroupId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForecastApi#forecastUsageByManagmentGroup");
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

<a id="forecastUsageByResourceGroup"></a>
# **forecastUsageByResourceGroup**
> QueryResult forecastUsageByResourceGroup(apiVersion, subscriptionId, resourceGroupName, parameters)



Forecast the usage data for subscriptionId and resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForecastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ForecastApi apiInstance = new ForecastApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
    ReportConfigDefinition parameters = new ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
    try {
      QueryResult result = apiInstance.forecastUsageByResourceGroup(apiVersion, subscriptionId, resourceGroupName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForecastApi#forecastUsageByResourceGroup");
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

<a id="forecastUsageBySubscription"></a>
# **forecastUsageBySubscription**
> QueryResult forecastUsageBySubscription(apiVersion, subscriptionId, parameters)



Forecast the usage data for subscriptionId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForecastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ForecastApi apiInstance = new ForecastApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    ReportConfigDefinition parameters = new ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
    try {
      QueryResult result = apiInstance.forecastUsageBySubscription(apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForecastApi#forecastUsageBySubscription");
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

