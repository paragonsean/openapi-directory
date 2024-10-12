# DatasetsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**datasetsCreateOrUpdate**](DatasetsApi.md#datasetsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/datasets/{datasetName} |  |
| [**datasetsDelete**](DatasetsApi.md#datasetsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/datasets/{datasetName} |  |
| [**datasetsGet**](DatasetsApi.md#datasetsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/datasets/{datasetName} |  |
| [**datasetsListByFactory**](DatasetsApi.md#datasetsListByFactory) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/datasets |  |


<a id="datasetsCreateOrUpdate"></a>
# **datasetsCreateOrUpdate**
> DatasetResource datasetsCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, datasetName, apiVersion, dataset, ifMatch)



Creates or updates a dataset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatasetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DatasetsApi apiInstance = new DatasetsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String datasetName = "datasetName_example"; // String | The dataset name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    DatasetResource dataset = new DatasetResource(); // DatasetResource | Dataset resource definition.
    String ifMatch = "ifMatch_example"; // String | ETag of the dataset entity.  Should only be specified for update, for which it should match existing entity or can be * for unconditional update.
    try {
      DatasetResource result = apiInstance.datasetsCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, datasetName, apiVersion, dataset, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatasetsApi#datasetsCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **datasetName** | **String**| The dataset name. | |
| **apiVersion** | **String**| The API version. | |
| **dataset** | [**DatasetResource**](DatasetResource.md)| Dataset resource definition. | |
| **ifMatch** | **String**| ETag of the dataset entity.  Should only be specified for update, for which it should match existing entity or can be * for unconditional update. | [optional] |

### Return type

[**DatasetResource**](DatasetResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="datasetsDelete"></a>
# **datasetsDelete**
> datasetsDelete(subscriptionId, resourceGroupName, factoryName, datasetName, apiVersion)



Deletes a dataset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatasetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DatasetsApi apiInstance = new DatasetsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String datasetName = "datasetName_example"; // String | The dataset name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.datasetsDelete(subscriptionId, resourceGroupName, factoryName, datasetName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatasetsApi#datasetsDelete");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **datasetName** | **String**| The dataset name. | |
| **apiVersion** | **String**| The API version. | |

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
| **200** | OK. |  -  |
| **204** | No Content. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="datasetsGet"></a>
# **datasetsGet**
> DatasetResource datasetsGet(subscriptionId, resourceGroupName, factoryName, datasetName, apiVersion, ifNoneMatch)



Gets a dataset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatasetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DatasetsApi apiInstance = new DatasetsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String datasetName = "datasetName_example"; // String | The dataset name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag of the dataset entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned.
    try {
      DatasetResource result = apiInstance.datasetsGet(subscriptionId, resourceGroupName, factoryName, datasetName, apiVersion, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatasetsApi#datasetsGet");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **datasetName** | **String**| The dataset name. | |
| **apiVersion** | **String**| The API version. | |
| **ifNoneMatch** | **String**| ETag of the dataset entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned. | [optional] |

### Return type

[**DatasetResource**](DatasetResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **304** | Not modified. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="datasetsListByFactory"></a>
# **datasetsListByFactory**
> DatasetListResponse datasetsListByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion)



Lists datasets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatasetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DatasetsApi apiInstance = new DatasetsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      DatasetListResponse result = apiInstance.datasetsListByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatasetsApi#datasetsListByFactory");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**DatasetListResponse**](DatasetListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

