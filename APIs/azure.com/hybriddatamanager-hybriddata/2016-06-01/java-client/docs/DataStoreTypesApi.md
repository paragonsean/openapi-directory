# DataStoreTypesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dataStoreTypesGet**](DataStoreTypesApi.md#dataStoreTypesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataStoreTypes/{dataStoreTypeName} |  |
| [**dataStoreTypesListByDataManager**](DataStoreTypesApi.md#dataStoreTypesListByDataManager) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataStoreTypes |  |


<a id="dataStoreTypesGet"></a>
# **dataStoreTypesGet**
> DataStoreType dataStoreTypesGet(dataStoreTypeName, subscriptionId, resourceGroupName, dataManagerName, apiVersion)



Gets the data store/repository type given its name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataStoreTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataStoreTypesApi apiInstance = new DataStoreTypesApi(defaultClient);
    String dataStoreTypeName = "dataStoreTypeName_example"; // String | The data store/repository type name for which details are needed.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    try {
      DataStoreType result = apiInstance.dataStoreTypesGet(dataStoreTypeName, subscriptionId, resourceGroupName, dataManagerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataStoreTypesApi#dataStoreTypesGet");
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
| **dataStoreTypeName** | **String**| The data store/repository type name for which details are needed. | |
| **subscriptionId** | **String**| The Subscription Id | |
| **resourceGroupName** | **String**| The Resource Group Name | |
| **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | |
| **apiVersion** | **String**| The API Version | |

### Return type

[**DataStoreType**](DataStoreType.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The data store/repository type. |  -  |

<a id="dataStoreTypesListByDataManager"></a>
# **dataStoreTypesListByDataManager**
> DataStoreTypeList dataStoreTypesListByDataManager(subscriptionId, resourceGroupName, dataManagerName, apiVersion)



Gets all the data store/repository types that the resource supports.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataStoreTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataStoreTypesApi apiInstance = new DataStoreTypesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    try {
      DataStoreTypeList result = apiInstance.dataStoreTypesListByDataManager(subscriptionId, resourceGroupName, dataManagerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataStoreTypesApi#dataStoreTypesListByDataManager");
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

### Return type

[**DataStoreTypeList**](DataStoreTypeList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of data store types that are supported. |  -  |

