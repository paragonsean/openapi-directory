# DataSetMappingApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dataSetMappingsCreate**](DataSetMappingApi.md#dataSetMappingsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/dataSetMappings/{dataSetMappingName} | Maps a source data set in the source share to a sink data set in the share subscription.  Enables copying the data set from source to destination. |
| [**dataSetMappingsDelete**](DataSetMappingApi.md#dataSetMappingsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/dataSetMappings/{dataSetMappingName} | Delete DataSetMapping in a shareSubscription. |
| [**dataSetMappingsGet**](DataSetMappingApi.md#dataSetMappingsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/dataSetMappings/{dataSetMappingName} | Get DataSetMapping in a shareSubscription. |
| [**dataSetMappingsListByShareSubscription**](DataSetMappingApi.md#dataSetMappingsListByShareSubscription) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/dataSetMappings | List DataSetMappings in a share subscription. |


<a id="dataSetMappingsCreate"></a>
# **dataSetMappingsCreate**
> DataSetMapping dataSetMappingsCreate(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, dataSetMappingName, apiVersion, dataSetMapping)

Maps a source data set in the source share to a sink data set in the share subscription.  Enables copying the data set from source to destination.

Create a DataSetMapping 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataSetMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataSetMappingApi apiInstance = new DataSetMappingApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the share subscription which will hold the data set sink.
    String dataSetMappingName = "dataSetMappingName_example"; // String | The name of the data set mapping to be created.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    DataSetMapping dataSetMapping = new DataSetMapping(); // DataSetMapping | Destination data set configuration details.
    try {
      DataSetMapping result = apiInstance.dataSetMappingsCreate(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, dataSetMappingName, apiVersion, dataSetMapping);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSetMappingApi#dataSetMappingsCreate");
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
| **shareSubscriptionName** | **String**| The name of the share subscription which will hold the data set sink. | |
| **dataSetMappingName** | **String**| The name of the data set mapping to be created. | |
| **apiVersion** | **String**| The api version to use. | |
| **dataSetMapping** | [**DataSetMapping**](DataSetMapping.md)| Destination data set configuration details. | |

### Return type

[**DataSetMapping**](DataSetMapping.md)

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

<a id="dataSetMappingsDelete"></a>
# **dataSetMappingsDelete**
> dataSetMappingsDelete(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, dataSetMappingName, apiVersion)

Delete DataSetMapping in a shareSubscription.

Delete a DataSetMapping in a shareSubscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataSetMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataSetMappingApi apiInstance = new DataSetMappingApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the shareSubscription.
    String dataSetMappingName = "dataSetMappingName_example"; // String | The name of the dataSetMapping.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    try {
      apiInstance.dataSetMappingsDelete(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, dataSetMappingName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSetMappingApi#dataSetMappingsDelete");
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
| **shareSubscriptionName** | **String**| The name of the shareSubscription. | |
| **dataSetMappingName** | **String**| The name of the dataSetMapping. | |
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
| **204** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="dataSetMappingsGet"></a>
# **dataSetMappingsGet**
> DataSetMapping dataSetMappingsGet(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, dataSetMappingName, apiVersion)

Get DataSetMapping in a shareSubscription.

Get a DataSetMapping in a shareSubscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataSetMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataSetMappingApi apiInstance = new DataSetMappingApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the shareSubscription.
    String dataSetMappingName = "dataSetMappingName_example"; // String | The name of the dataSetMapping.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    try {
      DataSetMapping result = apiInstance.dataSetMappingsGet(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, dataSetMappingName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSetMappingApi#dataSetMappingsGet");
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
| **shareSubscriptionName** | **String**| The name of the shareSubscription. | |
| **dataSetMappingName** | **String**| The name of the dataSetMapping. | |
| **apiVersion** | **String**| The api version to use. | |

### Return type

[**DataSetMapping**](DataSetMapping.md)

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

<a id="dataSetMappingsListByShareSubscription"></a>
# **dataSetMappingsListByShareSubscription**
> DataSetMappingList dataSetMappingsListByShareSubscription(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, $skipToken)

List DataSetMappings in a share subscription.

List DataSetMappings in a share subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataSetMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataSetMappingApi apiInstance = new DataSetMappingApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the share subscription.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    String $skipToken = "$skipToken_example"; // String | Continuation token
    try {
      DataSetMappingList result = apiInstance.dataSetMappingsListByShareSubscription(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSetMappingApi#dataSetMappingsListByShareSubscription");
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
| **shareSubscriptionName** | **String**| The name of the share subscription. | |
| **apiVersion** | **String**| The api version to use. | |
| **$skipToken** | **String**| Continuation token | [optional] |

### Return type

[**DataSetMappingList**](DataSetMappingList.md)

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

