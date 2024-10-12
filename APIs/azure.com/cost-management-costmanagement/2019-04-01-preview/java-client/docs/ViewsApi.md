# ViewsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**viewsCreateOrUpdate**](ViewsApi.md#viewsCreateOrUpdate) | **PUT** /providers/Microsoft.CostManagement/views/{viewName} |  |
| [**viewsCreateOrUpdateByScope**](ViewsApi.md#viewsCreateOrUpdateByScope) | **PUT** /{scope}/providers/Microsoft.CostManagement/views/{viewName} |  |
| [**viewsDelete**](ViewsApi.md#viewsDelete) | **DELETE** /providers/Microsoft.CostManagement/views/{viewName} |  |
| [**viewsDeleteByScope**](ViewsApi.md#viewsDeleteByScope) | **DELETE** /{scope}/providers/Microsoft.CostManagement/views/{viewName} |  |
| [**viewsGet**](ViewsApi.md#viewsGet) | **GET** /providers/Microsoft.CostManagement/views/{viewName} |  |
| [**viewsGetByScope**](ViewsApi.md#viewsGetByScope) | **GET** /{scope}/providers/Microsoft.CostManagement/views/{viewName} |  |
| [**viewsList**](ViewsApi.md#viewsList) | **GET** /providers/Microsoft.CostManagement/views |  |
| [**viewsListByScope**](ViewsApi.md#viewsListByScope) | **GET** /{scope}/providers/Microsoft.CostManagement/views |  |


<a id="viewsCreateOrUpdate"></a>
# **viewsCreateOrUpdate**
> View viewsCreateOrUpdate(apiVersion, viewName, parameters)



The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ViewsApi apiInstance = new ViewsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-04-01-preview
    String viewName = "viewName_example"; // String | View name
    View parameters = new View(); // View | Parameters supplied to the CreateOrUpdate View operation.
    try {
      View result = apiInstance.viewsCreateOrUpdate(apiVersion, viewName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewsApi#viewsCreateOrUpdate");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-04-01-preview | |
| **viewName** | **String**| View name | |
| **parameters** | [**View**](View.md)| Parameters supplied to the CreateOrUpdate View operation. | |

### Return type

[**View**](View.md)

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

<a id="viewsCreateOrUpdateByScope"></a>
# **viewsCreateOrUpdateByScope**
> View viewsCreateOrUpdateByScope(scope, apiVersion, viewName, parameters)



The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ViewsApi apiInstance = new ViewsApi(defaultClient);
    String scope = "scope_example"; // String | The scope associated with view operations. This includes 'subscriptions/{subscriptionId}' for subscription scope, 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for BillingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}' for InvoiceSection scope, 'providers/Microsoft.Management/managementGroups/{managementGroupId}' for Management Group scope, 'providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for External Billing Account scope and 'providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for External Subscription scope.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-04-01-preview
    String viewName = "viewName_example"; // String | View name
    View parameters = new View(); // View | Parameters supplied to the CreateOrUpdate View operation.
    try {
      View result = apiInstance.viewsCreateOrUpdateByScope(scope, apiVersion, viewName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewsApi#viewsCreateOrUpdateByScope");
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
| **scope** | **String**| The scope associated with view operations. This includes &#39;subscriptions/{subscriptionId}&#39; for subscription scope, &#39;subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for BillingProfile scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}&#39; for InvoiceSection scope, &#39;providers/Microsoft.Management/managementGroups/{managementGroupId}&#39; for Management Group scope, &#39;providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}&#39; for External Billing Account scope and &#39;providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}&#39; for External Subscription scope. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-04-01-preview | |
| **viewName** | **String**| View name | |
| **parameters** | [**View**](View.md)| Parameters supplied to the CreateOrUpdate View operation. | |

### Return type

[**View**](View.md)

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

<a id="viewsDelete"></a>
# **viewsDelete**
> viewsDelete(apiVersion, viewName)



The operation to delete a view.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ViewsApi apiInstance = new ViewsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-04-01-preview
    String viewName = "viewName_example"; // String | View name
    try {
      apiInstance.viewsDelete(apiVersion, viewName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewsApi#viewsDelete");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-04-01-preview | |
| **viewName** | **String**| View name | |

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
| **204** | NoContent. Resource is not available. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="viewsDeleteByScope"></a>
# **viewsDeleteByScope**
> viewsDeleteByScope(scope, apiVersion, viewName)



The operation to delete a view.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ViewsApi apiInstance = new ViewsApi(defaultClient);
    String scope = "scope_example"; // String | The scope associated with view operations. This includes 'subscriptions/{subscriptionId}' for subscription scope, 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for BillingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}' for InvoiceSection scope, 'providers/Microsoft.Management/managementGroups/{managementGroupId}' for Management Group scope, 'providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for External Billing Account scope and 'providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for External Subscription scope.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-04-01-preview
    String viewName = "viewName_example"; // String | View name
    try {
      apiInstance.viewsDeleteByScope(scope, apiVersion, viewName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewsApi#viewsDeleteByScope");
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
| **scope** | **String**| The scope associated with view operations. This includes &#39;subscriptions/{subscriptionId}&#39; for subscription scope, &#39;subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for BillingProfile scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}&#39; for InvoiceSection scope, &#39;providers/Microsoft.Management/managementGroups/{managementGroupId}&#39; for Management Group scope, &#39;providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}&#39; for External Billing Account scope and &#39;providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}&#39; for External Subscription scope. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-04-01-preview | |
| **viewName** | **String**| View name | |

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
| **204** | NoContent. Resource is not available. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="viewsGet"></a>
# **viewsGet**
> View viewsGet(apiVersion, viewName)



Gets the view by view name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ViewsApi apiInstance = new ViewsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-04-01-preview
    String viewName = "viewName_example"; // String | View name
    try {
      View result = apiInstance.viewsGet(apiVersion, viewName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewsApi#viewsGet");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-04-01-preview | |
| **viewName** | **String**| View name | |

### Return type

[**View**](View.md)

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

<a id="viewsGetByScope"></a>
# **viewsGetByScope**
> View viewsGetByScope(scope, apiVersion, viewName)



Gets the view for the defined scope by view name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ViewsApi apiInstance = new ViewsApi(defaultClient);
    String scope = "scope_example"; // String | The scope associated with view operations. This includes 'subscriptions/{subscriptionId}' for subscription scope, 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for BillingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}' for InvoiceSection scope, 'providers/Microsoft.Management/managementGroups/{managementGroupId}' for Management Group scope, 'providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for External Billing Account scope and 'providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for External Subscription scope.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-04-01-preview
    String viewName = "viewName_example"; // String | View name
    try {
      View result = apiInstance.viewsGetByScope(scope, apiVersion, viewName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewsApi#viewsGetByScope");
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
| **scope** | **String**| The scope associated with view operations. This includes &#39;subscriptions/{subscriptionId}&#39; for subscription scope, &#39;subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for BillingProfile scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}&#39; for InvoiceSection scope, &#39;providers/Microsoft.Management/managementGroups/{managementGroupId}&#39; for Management Group scope, &#39;providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}&#39; for External Billing Account scope and &#39;providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}&#39; for External Subscription scope. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-04-01-preview | |
| **viewName** | **String**| View name | |

### Return type

[**View**](View.md)

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

<a id="viewsList"></a>
# **viewsList**
> ViewListResult viewsList(apiVersion)



Lists all views by tenant and object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ViewsApi apiInstance = new ViewsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-04-01-preview
    try {
      ViewListResult result = apiInstance.viewsList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewsApi#viewsList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-04-01-preview | |

### Return type

[**ViewListResult**](ViewListResult.md)

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

<a id="viewsListByScope"></a>
# **viewsListByScope**
> ViewListResult viewsListByScope(scope, apiVersion)



Lists all views at the given scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ViewsApi apiInstance = new ViewsApi(defaultClient);
    String scope = "scope_example"; // String | The scope associated with view operations. This includes 'subscriptions/{subscriptionId}' for subscription scope, 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for BillingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}' for InvoiceSection scope, 'providers/Microsoft.Management/managementGroups/{managementGroupId}' for Management Group scope, 'providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for External Billing Account scope and 'providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for External Subscription scope.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-04-01-preview
    try {
      ViewListResult result = apiInstance.viewsListByScope(scope, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewsApi#viewsListByScope");
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
| **scope** | **String**| The scope associated with view operations. This includes &#39;subscriptions/{subscriptionId}&#39; for subscription scope, &#39;subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for BillingProfile scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}&#39; for InvoiceSection scope, &#39;providers/Microsoft.Management/managementGroups/{managementGroupId}&#39; for Management Group scope, &#39;providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}&#39; for External Billing Account scope and &#39;providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}&#39; for External Subscription scope. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-04-01-preview | |

### Return type

[**ViewListResult**](ViewListResult.md)

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

