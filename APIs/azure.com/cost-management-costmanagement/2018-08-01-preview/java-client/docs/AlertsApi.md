# AlertsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**alertsGetAlertByManagementGroups**](AlertsApi.md#alertsGetAlertByManagementGroups) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.CostManagement/alerts/{alertId} |  |
| [**alertsGetByAccount**](AlertsApi.md#alertsGetByAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}/providers/Microsoft.CostManagement/alerts/{alertId} |  |
| [**alertsGetByDepartment**](AlertsApi.md#alertsGetByDepartment) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}/providers/Microsoft.CostManagement/alerts/{alertId} |  |
| [**alertsGetByEnrollment**](AlertsApi.md#alertsGetByEnrollment) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/alerts/{alertId} |  |
| [**alertsGetByResourceGroupName**](AlertsApi.md#alertsGetByResourceGroupName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/alerts/{alertId} |  |
| [**alertsGetBySubscription**](AlertsApi.md#alertsGetBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/alerts/{alertId} |  |
| [**alertsList**](AlertsApi.md#alertsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/alerts |  |
| [**alertsListByAccount**](AlertsApi.md#alertsListByAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}/providers/Microsoft.CostManagement/alerts |  |
| [**alertsListByDepartment**](AlertsApi.md#alertsListByDepartment) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}/providers/Microsoft.CostManagement/alerts |  |
| [**alertsListByEnrollment**](AlertsApi.md#alertsListByEnrollment) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/alerts |  |
| [**alertsListByManagementGroups**](AlertsApi.md#alertsListByManagementGroups) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.CostManagement/alerts |  |
| [**alertsListByResourceGroupName**](AlertsApi.md#alertsListByResourceGroupName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/alerts |  |
| [**alertsUpdateBillingAccountAlertStatus**](AlertsApi.md#alertsUpdateBillingAccountAlertStatus) | **PATCH** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/alerts/{alertId}/updateStatus |  |
| [**alertsUpdateDepartmentsAlertStatus**](AlertsApi.md#alertsUpdateDepartmentsAlertStatus) | **PATCH** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}/providers/Microsoft.CostManagement/alerts/{alertId}/updateStatus |  |
| [**alertsUpdateEnrollmentAccountAlertStatus**](AlertsApi.md#alertsUpdateEnrollmentAccountAlertStatus) | **PATCH** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}/providers/Microsoft.CostManagement/alerts/{alertId}/updateStatus |  |
| [**alertsUpdateManagementGroupAlertStatus**](AlertsApi.md#alertsUpdateManagementGroupAlertStatus) | **PATCH** /providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.CostManagement/alerts/{alertId}/UpdateStatus |  |
| [**alertsUpdateResourceGroupNameAlertStatus**](AlertsApi.md#alertsUpdateResourceGroupNameAlertStatus) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/alerts/{alertId}/updateStatus |  |
| [**alertsUpdateSubscriptionAlertStatus**](AlertsApi.md#alertsUpdateSubscriptionAlertStatus) | **PATCH** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/alerts/{alertId}/updateStatus |  |


<a id="alertsGetAlertByManagementGroups"></a>
# **alertsGetAlertByManagementGroups**
> Alert alertsGetAlertByManagementGroups(apiVersion, managementGroupId, alertId)



Gets an alert for Management Groups by alert ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String managementGroupId = "managementGroupId_example"; // String | Management Group ID
    String alertId = "alertId_example"; // String | Alert ID.
    try {
      Alert result = apiInstance.alertsGetAlertByManagementGroups(apiVersion, managementGroupId, alertId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsGetAlertByManagementGroups");
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
| **managementGroupId** | **String**| Management Group ID | |
| **alertId** | **String**| Alert ID. | |

### Return type

[**Alert**](Alert.md)

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

<a id="alertsGetByAccount"></a>
# **alertsGetByAccount**
> Alert alertsGetByAccount(apiVersion, billingAccountId, enrollmentAccountId, alertId)



Gets the alert for an account by alert ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String enrollmentAccountId = "enrollmentAccountId_example"; // String | Enrollment Account Id
    String alertId = "alertId_example"; // String | Alert ID.
    try {
      Alert result = apiInstance.alertsGetByAccount(apiVersion, billingAccountId, enrollmentAccountId, alertId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsGetByAccount");
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
| **enrollmentAccountId** | **String**| Enrollment Account Id | |
| **alertId** | **String**| Alert ID. | |

### Return type

[**Alert**](Alert.md)

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

<a id="alertsGetByDepartment"></a>
# **alertsGetByDepartment**
> Alert alertsGetByDepartment(apiVersion, billingAccountId, departmentId, alertId)



Gets the alert for a department by alert ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String departmentId = "departmentId_example"; // String | Department ID
    String alertId = "alertId_example"; // String | Alert ID.
    try {
      Alert result = apiInstance.alertsGetByDepartment(apiVersion, billingAccountId, departmentId, alertId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsGetByDepartment");
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
| **departmentId** | **String**| Department ID | |
| **alertId** | **String**| Alert ID. | |

### Return type

[**Alert**](Alert.md)

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

<a id="alertsGetByEnrollment"></a>
# **alertsGetByEnrollment**
> Alert alertsGetByEnrollment(apiVersion, billingAccountId, alertId)



Gets the alert for an enrollment by alert ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String alertId = "alertId_example"; // String | Alert ID.
    try {
      Alert result = apiInstance.alertsGetByEnrollment(apiVersion, billingAccountId, alertId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsGetByEnrollment");
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
| **alertId** | **String**| Alert ID. | |

### Return type

[**Alert**](Alert.md)

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

<a id="alertsGetByResourceGroupName"></a>
# **alertsGetByResourceGroupName**
> Alert alertsGetByResourceGroupName(subscriptionId, resourceGroupName, apiVersion, alertId)



Gets the alert for a resource group under a subscription by alert ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String alertId = "alertId_example"; // String | Alert ID.
    try {
      Alert result = apiInstance.alertsGetByResourceGroupName(subscriptionId, resourceGroupName, apiVersion, alertId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsGetByResourceGroupName");
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
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Azure Resource Group Name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **alertId** | **String**| Alert ID. | |

### Return type

[**Alert**](Alert.md)

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

<a id="alertsGetBySubscription"></a>
# **alertsGetBySubscription**
> Alert alertsGetBySubscription(apiVersion, subscriptionId, alertId)



Gets the alert for a subscription by alert ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String alertId = "alertId_example"; // String | Alert ID.
    try {
      Alert result = apiInstance.alertsGetBySubscription(apiVersion, subscriptionId, alertId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsGetBySubscription");
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
| **alertId** | **String**| Alert ID. | |

### Return type

[**Alert**](Alert.md)

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

<a id="alertsList"></a>
# **alertsList**
> AlertListResult alertsList(apiVersion, subscriptionId, $filter, $skiptoken, $top)



List all alerts for a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String $filter = "$filter_example"; // String | May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N alerts.
    try {
      AlertListResult result = apiInstance.alertsList(apiVersion, subscriptionId, $filter, $skiptoken, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsList");
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
| **$filter** | **String**| May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;. | [optional] |
| **$skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] |
| **$top** | **Integer**| May be used to limit the number of results to the most recent N alerts. | [optional] |

### Return type

[**AlertListResult**](AlertListResult.md)

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

<a id="alertsListByAccount"></a>
# **alertsListByAccount**
> AlertListResult alertsListByAccount(apiVersion, billingAccountId, enrollmentAccountId, $filter, $skiptoken, $top)



List all alerts for an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String enrollmentAccountId = "enrollmentAccountId_example"; // String | Enrollment Account Id
    String $filter = "$filter_example"; // String | May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N alerts.
    try {
      AlertListResult result = apiInstance.alertsListByAccount(apiVersion, billingAccountId, enrollmentAccountId, $filter, $skiptoken, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsListByAccount");
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
| **enrollmentAccountId** | **String**| Enrollment Account Id | |
| **$filter** | **String**| May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;. | [optional] |
| **$skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] |
| **$top** | **Integer**| May be used to limit the number of results to the most recent N alerts. | [optional] |

### Return type

[**AlertListResult**](AlertListResult.md)

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

<a id="alertsListByDepartment"></a>
# **alertsListByDepartment**
> AlertListResult alertsListByDepartment(apiVersion, billingAccountId, departmentId, $filter, $skiptoken, $top)



List all alerts for a department.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String departmentId = "departmentId_example"; // String | Department ID
    String $filter = "$filter_example"; // String | May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N alerts.
    try {
      AlertListResult result = apiInstance.alertsListByDepartment(apiVersion, billingAccountId, departmentId, $filter, $skiptoken, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsListByDepartment");
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
| **departmentId** | **String**| Department ID | |
| **$filter** | **String**| May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;. | [optional] |
| **$skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] |
| **$top** | **Integer**| May be used to limit the number of results to the most recent N alerts. | [optional] |

### Return type

[**AlertListResult**](AlertListResult.md)

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

<a id="alertsListByEnrollment"></a>
# **alertsListByEnrollment**
> AlertListResult alertsListByEnrollment(apiVersion, billingAccountId, $filter, $skiptoken, $top)



List all alerts for an enrollment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String $filter = "$filter_example"; // String | May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N alerts.
    try {
      AlertListResult result = apiInstance.alertsListByEnrollment(apiVersion, billingAccountId, $filter, $skiptoken, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsListByEnrollment");
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
| **$filter** | **String**| May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;. | [optional] |
| **$skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] |
| **$top** | **Integer**| May be used to limit the number of results to the most recent N alerts. | [optional] |

### Return type

[**AlertListResult**](AlertListResult.md)

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

<a id="alertsListByManagementGroups"></a>
# **alertsListByManagementGroups**
> AlertListResult alertsListByManagementGroups(apiVersion, managementGroupId, $filter, $skiptoken, $top)



List all alerts for Management Groups.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String managementGroupId = "managementGroupId_example"; // String | Management Group ID
    String $filter = "$filter_example"; // String | May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N alerts.
    try {
      AlertListResult result = apiInstance.alertsListByManagementGroups(apiVersion, managementGroupId, $filter, $skiptoken, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsListByManagementGroups");
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
| **managementGroupId** | **String**| Management Group ID | |
| **$filter** | **String**| May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;. | [optional] |
| **$skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] |
| **$top** | **Integer**| May be used to limit the number of results to the most recent N alerts. | [optional] |

### Return type

[**AlertListResult**](AlertListResult.md)

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

<a id="alertsListByResourceGroupName"></a>
# **alertsListByResourceGroupName**
> AlertListResult alertsListByResourceGroupName(subscriptionId, resourceGroupName, apiVersion, $filter, $skiptoken, $top)



List all alerts for a resource group under a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String $filter = "$filter_example"; // String | May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N alerts.
    try {
      AlertListResult result = apiInstance.alertsListByResourceGroupName(subscriptionId, resourceGroupName, apiVersion, $filter, $skiptoken, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsListByResourceGroupName");
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
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Azure Resource Group Name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **$filter** | **String**| May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;. | [optional] |
| **$skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] |
| **$top** | **Integer**| May be used to limit the number of results to the most recent N alerts. | [optional] |

### Return type

[**AlertListResult**](AlertListResult.md)

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

<a id="alertsUpdateBillingAccountAlertStatus"></a>
# **alertsUpdateBillingAccountAlertStatus**
> Alert alertsUpdateBillingAccountAlertStatus(apiVersion, billingAccountId, alertId, parameters)



Update alerts status for billing account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String alertId = "alertId_example"; // String | Alert ID.
    Alert parameters = new Alert(); // Alert | Parameters supplied to the update alerts status operation.
    try {
      Alert result = apiInstance.alertsUpdateBillingAccountAlertStatus(apiVersion, billingAccountId, alertId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsUpdateBillingAccountAlertStatus");
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
| **alertId** | **String**| Alert ID. | |
| **parameters** | [**Alert**](Alert.md)| Parameters supplied to the update alerts status operation. | |

### Return type

[**Alert**](Alert.md)

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

<a id="alertsUpdateDepartmentsAlertStatus"></a>
# **alertsUpdateDepartmentsAlertStatus**
> Alert alertsUpdateDepartmentsAlertStatus(apiVersion, billingAccountId, departmentId, alertId, parameters)



Update alerts status for a department.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String departmentId = "departmentId_example"; // String | Department ID
    String alertId = "alertId_example"; // String | Alert ID.
    Alert parameters = new Alert(); // Alert | Parameters supplied to the update alerts status operation.
    try {
      Alert result = apiInstance.alertsUpdateDepartmentsAlertStatus(apiVersion, billingAccountId, departmentId, alertId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsUpdateDepartmentsAlertStatus");
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
| **departmentId** | **String**| Department ID | |
| **alertId** | **String**| Alert ID. | |
| **parameters** | [**Alert**](Alert.md)| Parameters supplied to the update alerts status operation. | |

### Return type

[**Alert**](Alert.md)

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

<a id="alertsUpdateEnrollmentAccountAlertStatus"></a>
# **alertsUpdateEnrollmentAccountAlertStatus**
> Alert alertsUpdateEnrollmentAccountAlertStatus(apiVersion, billingAccountId, enrollmentAccountId, alertId, parameters)



Update alerts status for an enrollment account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String enrollmentAccountId = "enrollmentAccountId_example"; // String | Enrollment Account Id
    String alertId = "alertId_example"; // String | Alert ID.
    Alert parameters = new Alert(); // Alert | Parameters supplied to the update alerts status operation.
    try {
      Alert result = apiInstance.alertsUpdateEnrollmentAccountAlertStatus(apiVersion, billingAccountId, enrollmentAccountId, alertId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsUpdateEnrollmentAccountAlertStatus");
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
| **enrollmentAccountId** | **String**| Enrollment Account Id | |
| **alertId** | **String**| Alert ID. | |
| **parameters** | [**Alert**](Alert.md)| Parameters supplied to the update alerts status operation. | |

### Return type

[**Alert**](Alert.md)

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

<a id="alertsUpdateManagementGroupAlertStatus"></a>
# **alertsUpdateManagementGroupAlertStatus**
> Alert alertsUpdateManagementGroupAlertStatus(apiVersion, managementGroupId, alertId, parameters)



Update alerts status for management group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String managementGroupId = "managementGroupId_example"; // String | Management Group ID
    String alertId = "alertId_example"; // String | Alert ID.
    Alert parameters = new Alert(); // Alert | Parameters supplied to the update alerts status operation.
    try {
      Alert result = apiInstance.alertsUpdateManagementGroupAlertStatus(apiVersion, managementGroupId, alertId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsUpdateManagementGroupAlertStatus");
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
| **managementGroupId** | **String**| Management Group ID | |
| **alertId** | **String**| Alert ID. | |
| **parameters** | [**Alert**](Alert.md)| Parameters supplied to the update alerts status operation. | |

### Return type

[**Alert**](Alert.md)

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

<a id="alertsUpdateResourceGroupNameAlertStatus"></a>
# **alertsUpdateResourceGroupNameAlertStatus**
> Alert alertsUpdateResourceGroupNameAlertStatus(subscriptionId, resourceGroupName, alertId, apiVersion, parameters)



Update alerts status for a resource group under a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
    String alertId = "alertId_example"; // String | Alert ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    Alert parameters = new Alert(); // Alert | Parameters supplied to the update alerts status operation.
    try {
      Alert result = apiInstance.alertsUpdateResourceGroupNameAlertStatus(subscriptionId, resourceGroupName, alertId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsUpdateResourceGroupNameAlertStatus");
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
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Azure Resource Group Name. | |
| **alertId** | **String**| Alert ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | |
| **parameters** | [**Alert**](Alert.md)| Parameters supplied to the update alerts status operation. | |

### Return type

[**Alert**](Alert.md)

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

<a id="alertsUpdateSubscriptionAlertStatus"></a>
# **alertsUpdateSubscriptionAlertStatus**
> Alert alertsUpdateSubscriptionAlertStatus(apiVersion, subscriptionId, alertId, parameters)



Update alerts status for a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String alertId = "alertId_example"; // String | Alert ID.
    Alert parameters = new Alert(); // Alert | Parameters supplied to the update alerts status operation.
    try {
      Alert result = apiInstance.alertsUpdateSubscriptionAlertStatus(apiVersion, subscriptionId, alertId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsUpdateSubscriptionAlertStatus");
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
| **alertId** | **String**| Alert ID. | |
| **parameters** | [**Alert**](Alert.md)| Parameters supplied to the update alerts status operation. | |

### Return type

[**Alert**](Alert.md)

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

