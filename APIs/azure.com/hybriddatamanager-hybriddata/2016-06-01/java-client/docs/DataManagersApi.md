# DataManagersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dataManagersCreate**](DataManagersApi.md#dataManagersCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName} |  |
| [**dataManagersDelete**](DataManagersApi.md#dataManagersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName} |  |
| [**dataManagersGet**](DataManagersApi.md#dataManagersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName} |  |
| [**dataManagersList**](DataManagersApi.md#dataManagersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.HybridData/dataManagers |  |
| [**dataManagersListByResourceGroup**](DataManagersApi.md#dataManagersListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers |  |
| [**dataManagersUpdate**](DataManagersApi.md#dataManagersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName} |  |


<a id="dataManagersCreate"></a>
# **dataManagersCreate**
> DataManager dataManagersCreate(subscriptionId, resourceGroupName, dataManagerName, apiVersion, dataManager)



Creates a new data manager resource with the specified parameters. Existing resources cannot be updated with this API  and should instead be updated with the Update data manager resource API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataManagersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataManagersApi apiInstance = new DataManagersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    DataManager dataManager = new DataManager(); // DataManager | Data manager resource details from request body.
    try {
      DataManager result = apiInstance.dataManagersCreate(subscriptionId, resourceGroupName, dataManagerName, apiVersion, dataManager);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataManagersApi#dataManagersCreate");
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
| **dataManager** | [**DataManager**](DataManager.md)| Data manager resource details from request body. | |

### Return type

[**DataManager**](DataManager.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data Manager Resource object. |  -  |
| **202** | Accepted request for create/update. |  -  |

<a id="dataManagersDelete"></a>
# **dataManagersDelete**
> dataManagersDelete(subscriptionId, resourceGroupName, dataManagerName, apiVersion)



Deletes a data manager resource in Microsoft Azure.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataManagersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataManagersApi apiInstance = new DataManagersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    try {
      apiInstance.dataManagersDelete(subscriptionId, resourceGroupName, dataManagerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataManagersApi#dataManagersDelete");
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

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Data Manager Resource deleted. |  -  |
| **204** | Data Manager Resource deleted. |  -  |

<a id="dataManagersGet"></a>
# **dataManagersGet**
> DataManager dataManagersGet(subscriptionId, resourceGroupName, dataManagerName, apiVersion)



Gets information about the specified data manager resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataManagersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataManagersApi apiInstance = new DataManagersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    try {
      DataManager result = apiInstance.dataManagersGet(subscriptionId, resourceGroupName, dataManagerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataManagersApi#dataManagersGet");
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

[**DataManager**](DataManager.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data Manager Resource object. |  -  |

<a id="dataManagersList"></a>
# **dataManagersList**
> DataManagerList dataManagersList(subscriptionId, apiVersion)



Lists all the data manager resources available under the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataManagersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataManagersApi apiInstance = new DataManagersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String apiVersion = "apiVersion_example"; // String | The API Version
    try {
      DataManagerList result = apiInstance.dataManagersList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataManagersApi#dataManagersList");
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
| **apiVersion** | **String**| The API Version | |

### Return type

[**DataManagerList**](DataManagerList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of data manager resources available under the subscription. |  -  |

<a id="dataManagersListByResourceGroup"></a>
# **dataManagersListByResourceGroup**
> DataManagerList dataManagersListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Lists all the data manager resources available under the given resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataManagersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataManagersApi apiInstance = new DataManagersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String apiVersion = "apiVersion_example"; // String | The API Version
    try {
      DataManagerList result = apiInstance.dataManagersListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataManagersApi#dataManagersListByResourceGroup");
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
| **apiVersion** | **String**| The API Version | |

### Return type

[**DataManagerList**](DataManagerList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of data manager resources by resource group. |  -  |

<a id="dataManagersUpdate"></a>
# **dataManagersUpdate**
> DataManager dataManagersUpdate(subscriptionId, resourceGroupName, dataManagerName, apiVersion, dataManagerUpdateParameter, ifMatch)



Updates the properties of an existing data manager resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataManagersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataManagersApi apiInstance = new DataManagersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    DataManagerUpdateParameter dataManagerUpdateParameter = new DataManagerUpdateParameter(); // DataManagerUpdateParameter | Data manager resource details from request body.
    String ifMatch = "ifMatch_example"; // String | Defines the If-Match condition. The patch will be performed only if the ETag of the data manager resource on the server matches this value.
    try {
      DataManager result = apiInstance.dataManagersUpdate(subscriptionId, resourceGroupName, dataManagerName, apiVersion, dataManagerUpdateParameter, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataManagersApi#dataManagersUpdate");
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
| **dataManagerUpdateParameter** | [**DataManagerUpdateParameter**](DataManagerUpdateParameter.md)| Data manager resource details from request body. | |
| **ifMatch** | **String**| Defines the If-Match condition. The patch will be performed only if the ETag of the data manager resource on the server matches this value. | [optional] |

### Return type

[**DataManager**](DataManager.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data Manager Resource object. |  -  |
| **202** | Data Manager Resource updated. |  -  |

