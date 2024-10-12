# BudgetsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**budgetsCreateOrUpdate**](BudgetsApi.md#budgetsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Consumption/budgets/{budgetName} |  |
| [**budgetsCreateOrUpdateByResourceGroupName**](BudgetsApi.md#budgetsCreateOrUpdateByResourceGroupName) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Consumption/budgets/{budgetName} |  |
| [**budgetsDelete**](BudgetsApi.md#budgetsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Consumption/budgets/{budgetName} |  |
| [**budgetsDeleteByResourceGroupName**](BudgetsApi.md#budgetsDeleteByResourceGroupName) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Consumption/budgets/{budgetName} |  |
| [**budgetsGet**](BudgetsApi.md#budgetsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Consumption/budgets/{budgetName} |  |
| [**budgetsGetByResourceGroupName**](BudgetsApi.md#budgetsGetByResourceGroupName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Consumption/budgets/{budgetName} |  |
| [**budgetsList**](BudgetsApi.md#budgetsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Consumption/budgets |  |
| [**budgetsListByResourceGroupName**](BudgetsApi.md#budgetsListByResourceGroupName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Consumption/budgets |  |


<a id="budgetsCreateOrUpdate"></a>
# **budgetsCreateOrUpdate**
> Budget budgetsCreateOrUpdate(apiVersion, subscriptionId, budgetName, parameters)



The operation to create or update a budget. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BudgetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BudgetsApi apiInstance = new BudgetsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-10-01.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String budgetName = "budgetName_example"; // String | Budget Name.
    Budget parameters = new Budget(); // Budget | Parameters supplied to the Create Budget operation.
    try {
      Budget result = apiInstance.budgetsCreateOrUpdate(apiVersion, subscriptionId, budgetName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BudgetsApi#budgetsCreateOrUpdate");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-10-01. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **budgetName** | **String**| Budget Name. | |
| **parameters** | [**Budget**](Budget.md)| Parameters supplied to the Create Budget operation. | |

### Return type

[**Budget**](Budget.md)

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

<a id="budgetsCreateOrUpdateByResourceGroupName"></a>
# **budgetsCreateOrUpdateByResourceGroupName**
> Budget budgetsCreateOrUpdateByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, budgetName, parameters)



The operation to create or update a budget. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BudgetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BudgetsApi apiInstance = new BudgetsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-10-01.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
    String budgetName = "budgetName_example"; // String | Budget Name.
    Budget parameters = new Budget(); // Budget | Parameters supplied to the Create Budget operation.
    try {
      Budget result = apiInstance.budgetsCreateOrUpdateByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, budgetName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BudgetsApi#budgetsCreateOrUpdateByResourceGroupName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-10-01. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Azure Resource Group Name. | |
| **budgetName** | **String**| Budget Name. | |
| **parameters** | [**Budget**](Budget.md)| Parameters supplied to the Create Budget operation. | |

### Return type

[**Budget**](Budget.md)

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

<a id="budgetsDelete"></a>
# **budgetsDelete**
> budgetsDelete(apiVersion, subscriptionId, budgetName)



The operation to delete a budget.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BudgetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BudgetsApi apiInstance = new BudgetsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-10-01.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String budgetName = "budgetName_example"; // String | Budget Name.
    try {
      apiInstance.budgetsDelete(apiVersion, subscriptionId, budgetName);
    } catch (ApiException e) {
      System.err.println("Exception when calling BudgetsApi#budgetsDelete");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-10-01. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **budgetName** | **String**| Budget Name. | |

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

<a id="budgetsDeleteByResourceGroupName"></a>
# **budgetsDeleteByResourceGroupName**
> budgetsDeleteByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, budgetName)



The operation to delete a budget.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BudgetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BudgetsApi apiInstance = new BudgetsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-10-01.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
    String budgetName = "budgetName_example"; // String | Budget Name.
    try {
      apiInstance.budgetsDeleteByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, budgetName);
    } catch (ApiException e) {
      System.err.println("Exception when calling BudgetsApi#budgetsDeleteByResourceGroupName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-10-01. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Azure Resource Group Name. | |
| **budgetName** | **String**| Budget Name. | |

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

<a id="budgetsGet"></a>
# **budgetsGet**
> Budget budgetsGet(apiVersion, subscriptionId, budgetName)



Gets the budget for a subscription by budget name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BudgetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BudgetsApi apiInstance = new BudgetsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-10-01.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String budgetName = "budgetName_example"; // String | Budget Name.
    try {
      Budget result = apiInstance.budgetsGet(apiVersion, subscriptionId, budgetName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BudgetsApi#budgetsGet");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-10-01. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **budgetName** | **String**| Budget Name. | |

### Return type

[**Budget**](Budget.md)

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

<a id="budgetsGetByResourceGroupName"></a>
# **budgetsGetByResourceGroupName**
> Budget budgetsGetByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, budgetName)



Gets the budget for a resource group under a subscription by budget name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BudgetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BudgetsApi apiInstance = new BudgetsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-10-01.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
    String budgetName = "budgetName_example"; // String | Budget Name.
    try {
      Budget result = apiInstance.budgetsGetByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, budgetName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BudgetsApi#budgetsGetByResourceGroupName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-10-01. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Azure Resource Group Name. | |
| **budgetName** | **String**| Budget Name. | |

### Return type

[**Budget**](Budget.md)

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

<a id="budgetsList"></a>
# **budgetsList**
> BudgetsListResult budgetsList(apiVersion, subscriptionId)



Lists all budgets for a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BudgetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BudgetsApi apiInstance = new BudgetsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-10-01.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    try {
      BudgetsListResult result = apiInstance.budgetsList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BudgetsApi#budgetsList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-10-01. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |

### Return type

[**BudgetsListResult**](BudgetsListResult.md)

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

<a id="budgetsListByResourceGroupName"></a>
# **budgetsListByResourceGroupName**
> BudgetsListResult budgetsListByResourceGroupName(apiVersion, subscriptionId, resourceGroupName)



Lists all budgets for a resource group under a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BudgetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BudgetsApi apiInstance = new BudgetsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-10-01.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
    try {
      BudgetsListResult result = apiInstance.budgetsListByResourceGroupName(apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BudgetsApi#budgetsListByResourceGroupName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-10-01. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Azure Resource Group Name. | |

### Return type

[**BudgetsListResult**](BudgetsListResult.md)

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

