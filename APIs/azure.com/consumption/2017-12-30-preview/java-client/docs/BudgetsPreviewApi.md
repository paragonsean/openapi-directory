# BudgetsPreviewApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**budgetsCreateOrUpdate**](BudgetsPreviewApi.md#budgetsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Consumption/budgets/{name} |  |
| [**budgetsDelete**](BudgetsPreviewApi.md#budgetsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Consumption/budgets/{name} |  |
| [**budgetsGet**](BudgetsPreviewApi.md#budgetsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Consumption/budgets/{name} |  |
| [**budgetsList**](BudgetsPreviewApi.md#budgetsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Consumption/budgets |  |


<a id="budgetsCreateOrUpdate"></a>
# **budgetsCreateOrUpdate**
> Budget budgetsCreateOrUpdate(apiVersion, subscriptionId, name, parameters)



The operation to create or update a budget. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BudgetsPreviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BudgetsPreviewApi apiInstance = new BudgetsPreviewApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-12-30-preview.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String name = "name_example"; // String | Budget name.
    Budget parameters = new Budget(); // Budget | Parameters supplied to the Create Budget operation.
    try {
      Budget result = apiInstance.budgetsCreateOrUpdate(apiVersion, subscriptionId, name, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BudgetsPreviewApi#budgetsCreateOrUpdate");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-12-30-preview. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **name** | **String**| Budget name. | |
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
> budgetsDelete(apiVersion, subscriptionId, name)



The operation to delete a budget.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BudgetsPreviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BudgetsPreviewApi apiInstance = new BudgetsPreviewApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-12-30-preview.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String name = "name_example"; // String | Budget name.
    try {
      apiInstance.budgetsDelete(apiVersion, subscriptionId, name);
    } catch (ApiException e) {
      System.err.println("Exception when calling BudgetsPreviewApi#budgetsDelete");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-12-30-preview. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **name** | **String**| Budget name. | |

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
> Budget budgetsGet(apiVersion, subscriptionId, name)



Gets the budget for a subscription by budget name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BudgetsPreviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BudgetsPreviewApi apiInstance = new BudgetsPreviewApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-12-30-preview.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String name = "name_example"; // String | Budget name.
    try {
      Budget result = apiInstance.budgetsGet(apiVersion, subscriptionId, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BudgetsPreviewApi#budgetsGet");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-12-30-preview. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **name** | **String**| Budget name. | |

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
import org.openapitools.client.api.BudgetsPreviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BudgetsPreviewApi apiInstance = new BudgetsPreviewApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-12-30-preview.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    try {
      BudgetsListResult result = apiInstance.budgetsList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BudgetsPreviewApi#budgetsList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-12-30-preview. | |
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

