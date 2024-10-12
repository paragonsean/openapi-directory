# DataStoresApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dataStoresCreateOrUpdate**](DataStoresApi.md#dataStoresCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataStores/{dataStoreName} |  |
| [**dataStoresDelete**](DataStoresApi.md#dataStoresDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataStores/{dataStoreName} |  |
| [**dataStoresGet**](DataStoresApi.md#dataStoresGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataStores/{dataStoreName} |  |
| [**dataStoresListByDataManager**](DataStoresApi.md#dataStoresListByDataManager) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataStores |  |


<a id="dataStoresCreateOrUpdate"></a>
# **dataStoresCreateOrUpdate**
> DataStore dataStoresCreateOrUpdate(dataStoreName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, dataStore)



Creates or updates the data store/repository in the data manager.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataStoresApi apiInstance = new DataStoresApi(defaultClient);
    String dataStoreName = "dataStoreName_example"; // String | The data store/repository name to be created or updated.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    DataStore dataStore = new DataStore(); // DataStore | The data store/repository object to be created or updated.
    try {
      DataStore result = apiInstance.dataStoresCreateOrUpdate(dataStoreName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, dataStore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataStoresApi#dataStoresCreateOrUpdate");
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
| **dataStoreName** | **String**| The data store/repository name to be created or updated. | |
| **subscriptionId** | **String**| The Subscription Id | |
| **resourceGroupName** | **String**| The Resource Group Name | |
| **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | |
| **apiVersion** | **String**| The API Version | |
| **dataStore** | [**DataStore**](DataStore.md)| The data store/repository object to be created or updated. | |

### Return type

[**DataStore**](DataStore.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The data store/repository object. |  -  |
| **202** | Accepted request for create/update. |  -  |

<a id="dataStoresDelete"></a>
# **dataStoresDelete**
> dataStoresDelete(dataStoreName, subscriptionId, resourceGroupName, dataManagerName, apiVersion)



This method deletes the given data store/repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataStoresApi apiInstance = new DataStoresApi(defaultClient);
    String dataStoreName = "dataStoreName_example"; // String | The data store/repository name to be deleted.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    try {
      apiInstance.dataStoresDelete(dataStoreName, subscriptionId, resourceGroupName, dataManagerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataStoresApi#dataStoresDelete");
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
| **dataStoreName** | **String**| The data store/repository name to be deleted. | |
| **subscriptionId** | **String**| The Subscription Id | |
| **resourceGroupName** | **String**| The Resource Group Name | |
| **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | |
| **apiVersion** | **String**| The API Version | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted request for DataStore deletion. |  -  |
| **204** | DataStore deleted. |  -  |

<a id="dataStoresGet"></a>
# **dataStoresGet**
> DataStore dataStoresGet(dataStoreName, subscriptionId, resourceGroupName, dataManagerName, apiVersion)



This method gets the data store/repository by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataStoresApi apiInstance = new DataStoresApi(defaultClient);
    String dataStoreName = "dataStoreName_example"; // String | The data store/repository name queried.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    try {
      DataStore result = apiInstance.dataStoresGet(dataStoreName, subscriptionId, resourceGroupName, dataManagerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataStoresApi#dataStoresGet");
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
| **dataStoreName** | **String**| The data store/repository name queried. | |
| **subscriptionId** | **String**| The Subscription Id | |
| **resourceGroupName** | **String**| The Resource Group Name | |
| **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | |
| **apiVersion** | **String**| The API Version | |

### Return type

[**DataStore**](DataStore.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The data store/repository which matches the name given. |  -  |

<a id="dataStoresListByDataManager"></a>
# **dataStoresListByDataManager**
> DataStoreList dataStoresListByDataManager(subscriptionId, resourceGroupName, dataManagerName, apiVersion, $filter)



Gets all the data stores/repositories in the given resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataStoresApi apiInstance = new DataStoresApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    String $filter = "$filter_example"; // String | OData Filter options
    try {
      DataStoreList result = apiInstance.dataStoresListByDataManager(subscriptionId, resourceGroupName, dataManagerName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataStoresApi#dataStoresListByDataManager");
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
| **subscriptionId** | **String**| The Subscription Id | |
| **resourceGroupName** | **String**| The Resource Group Name | |
| **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | |
| **apiVersion** | **String**| The API Version | |
| **$filter** | **String**| OData Filter options | [optional] |

### Return type

[**DataStoreList**](DataStoreList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of data stores/repositories in the given resource. |  -  |

