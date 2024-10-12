# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountFiltersCreateOrUpdate**](DefaultApi.md#accountFiltersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/accountFilters/{filterName} | Create or update an Account Filter |
| [**accountFiltersDelete**](DefaultApi.md#accountFiltersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/accountFilters/{filterName} | Delete an Account Filter. |
| [**accountFiltersGet**](DefaultApi.md#accountFiltersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/accountFilters/{filterName} | Get an Account Filter. |
| [**accountFiltersList**](DefaultApi.md#accountFiltersList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/accountFilters | List Account Filters |
| [**accountFiltersUpdate**](DefaultApi.md#accountFiltersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/accountFilters/{filterName} | Update an Account Filter |


<a id="accountFiltersCreateOrUpdate"></a>
# **accountFiltersCreateOrUpdate**
> AccountFilter accountFiltersCreateOrUpdate(subscriptionId, resourceGroupName, accountName, filterName, apiVersion, parameters)

Create or update an Account Filter

Creates or updates an Account Filter in the Media Services account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String filterName = "filterName_example"; // String | The Account Filter name
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    AccountFilter parameters = new AccountFilter(); // AccountFilter | The request parameters
    try {
      AccountFilter result = apiInstance.accountFiltersCreateOrUpdate(subscriptionId, resourceGroupName, accountName, filterName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#accountFiltersCreateOrUpdate");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **filterName** | **String**| The Account Filter name | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **parameters** | [**AccountFilter**](AccountFilter.md)| The request parameters | |

### Return type

[**AccountFilter**](AccountFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | Detailed error information. |  -  |

<a id="accountFiltersDelete"></a>
# **accountFiltersDelete**
> accountFiltersDelete(subscriptionId, resourceGroupName, accountName, filterName, apiVersion)

Delete an Account Filter.

Deletes an Account Filter in the Media Services account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String filterName = "filterName_example"; // String | The Account Filter name
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      apiInstance.accountFiltersDelete(subscriptionId, resourceGroupName, accountName, filterName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#accountFiltersDelete");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **filterName** | **String**| The Account Filter name | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | NoContent |  -  |
| **0** | Detailed error information. |  -  |

<a id="accountFiltersGet"></a>
# **accountFiltersGet**
> AccountFilter accountFiltersGet(subscriptionId, resourceGroupName, accountName, filterName, apiVersion)

Get an Account Filter.

Get the details of an Account Filter in the Media Services account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String filterName = "filterName_example"; // String | The Account Filter name
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      AccountFilter result = apiInstance.accountFiltersGet(subscriptionId, resourceGroupName, accountName, filterName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#accountFiltersGet");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **filterName** | **String**| The Account Filter name | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

[**AccountFilter**](AccountFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NotFound |  -  |
| **0** | Detailed error information. |  -  |

<a id="accountFiltersList"></a>
# **accountFiltersList**
> AccountFilterCollection accountFiltersList(subscriptionId, resourceGroupName, accountName, apiVersion)

List Account Filters

List Account Filters in the Media Services account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      AccountFilterCollection result = apiInstance.accountFiltersList(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#accountFiltersList");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

[**AccountFilterCollection**](AccountFilterCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

<a id="accountFiltersUpdate"></a>
# **accountFiltersUpdate**
> AccountFilter accountFiltersUpdate(subscriptionId, resourceGroupName, accountName, filterName, apiVersion, parameters)

Update an Account Filter

Updates an existing Account Filter in the Media Services account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String filterName = "filterName_example"; // String | The Account Filter name
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    AccountFilter parameters = new AccountFilter(); // AccountFilter | The request parameters
    try {
      AccountFilter result = apiInstance.accountFiltersUpdate(subscriptionId, resourceGroupName, accountName, filterName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#accountFiltersUpdate");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **filterName** | **String**| The Account Filter name | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **parameters** | [**AccountFilter**](AccountFilter.md)| The request parameters | |

### Return type

[**AccountFilter**](AccountFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

