# DataSetApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dataSetsCreate**](DataSetApi.md#dataSetsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/dataSets/{dataSetName} | Adds a new data set to an existing share or updates it if existing. |
| [**dataSetsDelete**](DataSetApi.md#dataSetsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/dataSets/{dataSetName} | Delete DataSet in a share. |
| [**dataSetsGet**](DataSetApi.md#dataSetsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/dataSets/{dataSetName} | Get DataSet in a share. |
| [**dataSetsListByShare**](DataSetApi.md#dataSetsListByShare) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/dataSets | List DataSets in a share. |


<a id="dataSetsCreate"></a>
# **dataSetsCreate**
> DataSet dataSetsCreate(subscriptionId, resourceGroupName, accountName, shareName, dataSetName, apiVersion, dataSet)

Adds a new data set to an existing share or updates it if existing.

Create a DataSet 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataSetApi apiInstance = new DataSetApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareName = "shareName_example"; // String | The name of the share to add the data set to.
    String dataSetName = "dataSetName_example"; // String | The name of the dataSet.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    DataSet dataSet = new DataSet(); // DataSet | The new data set information.
    try {
      DataSet result = apiInstance.dataSetsCreate(subscriptionId, resourceGroupName, accountName, shareName, dataSetName, apiVersion, dataSet);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSetApi#dataSetsCreate");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **shareName** | **String**| The name of the share to add the data set to. | |
| **dataSetName** | **String**| The name of the dataSet. | |
| **apiVersion** | **String**| The api version to use. | |
| **dataSet** | [**DataSet**](DataSet.md)| The new data set information. | |

### Return type

[**DataSet**](DataSet.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **201** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="dataSetsDelete"></a>
# **dataSetsDelete**
> dataSetsDelete(subscriptionId, resourceGroupName, accountName, shareName, dataSetName, apiVersion)

Delete DataSet in a share.

Delete a DataSet in a share

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataSetApi apiInstance = new DataSetApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareName = "shareName_example"; // String | The name of the share.
    String dataSetName = "dataSetName_example"; // String | The name of the dataSet.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    try {
      apiInstance.dataSetsDelete(subscriptionId, resourceGroupName, accountName, shareName, dataSetName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSetApi#dataSetsDelete");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **shareName** | **String**| The name of the share. | |
| **dataSetName** | **String**| The name of the dataSet. | |
| **apiVersion** | **String**| The api version to use. | |

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
| **200** | Success |  -  |
| **202** | Accepted |  -  |
| **204** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="dataSetsGet"></a>
# **dataSetsGet**
> DataSet dataSetsGet(subscriptionId, resourceGroupName, accountName, shareName, dataSetName, apiVersion)

Get DataSet in a share.

Get a DataSet in a share

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataSetApi apiInstance = new DataSetApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareName = "shareName_example"; // String | The name of the share.
    String dataSetName = "dataSetName_example"; // String | The name of the dataSet.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    try {
      DataSet result = apiInstance.dataSetsGet(subscriptionId, resourceGroupName, accountName, shareName, dataSetName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSetApi#dataSetsGet");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **shareName** | **String**| The name of the share. | |
| **dataSetName** | **String**| The name of the dataSet. | |
| **apiVersion** | **String**| The api version to use. | |

### Return type

[**DataSet**](DataSet.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="dataSetsListByShare"></a>
# **dataSetsListByShare**
> DataSetList dataSetsListByShare(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, $skipToken)

List DataSets in a share.

List DataSets in a share

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataSetApi apiInstance = new DataSetApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareName = "shareName_example"; // String | The name of the share.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    String $skipToken = "$skipToken_example"; // String | continuation token
    try {
      DataSetList result = apiInstance.dataSetsListByShare(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSetApi#dataSetsListByShare");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **shareName** | **String**| The name of the share. | |
| **apiVersion** | **String**| The api version to use. | |
| **$skipToken** | **String**| continuation token | [optional] |

### Return type

[**DataSetList**](DataSetList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

