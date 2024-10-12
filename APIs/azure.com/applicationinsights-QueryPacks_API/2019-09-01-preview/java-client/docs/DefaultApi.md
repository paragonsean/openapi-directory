# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**queryPacksCreateOrUpdate**](DefaultApi.md#queryPacksCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/queryPacks/{queryPackName} |  |
| [**queryPacksDelete**](DefaultApi.md#queryPacksDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/queryPacks/{queryPackName} |  |
| [**queryPacksGet**](DefaultApi.md#queryPacksGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/queryPacks/{queryPackName} |  |
| [**queryPacksList**](DefaultApi.md#queryPacksList) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/queryPacks |  |
| [**queryPacksListByResourceGroup**](DefaultApi.md#queryPacksListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/queryPacks |  |
| [**queryPacksUpdateTags**](DefaultApi.md#queryPacksUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/queryPacks/{queryPackName} |  |


<a id="queryPacksCreateOrUpdate"></a>
# **queryPacksCreateOrUpdate**
> LogAnalyticsQueryPack queryPacksCreateOrUpdate(resourceGroupName, apiVersion, subscriptionId, queryPackName, logAnalyticsQueryPackPayload)



Creates (or updates) a Log Analytics QueryPack. Note: You cannot specify a different value for InstrumentationKey nor AppId in the Put operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String queryPackName = "queryPackName_example"; // String | The name of the Log Analytics QueryPack resource.
    LogAnalyticsQueryPack logAnalyticsQueryPackPayload = new LogAnalyticsQueryPack(); // LogAnalyticsQueryPack | Properties that need to be specified to create or update a Log Analytics QueryPack.
    try {
      LogAnalyticsQueryPack result = apiInstance.queryPacksCreateOrUpdate(resourceGroupName, apiVersion, subscriptionId, queryPackName, logAnalyticsQueryPackPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#queryPacksCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **queryPackName** | **String**| The name of the Log Analytics QueryPack resource. | |
| **logAnalyticsQueryPackPayload** | [**LogAnalyticsQueryPack**](LogAnalyticsQueryPack.md)| Properties that need to be specified to create or update a Log Analytics QueryPack. | |

### Return type

[**LogAnalyticsQueryPack**](LogAnalyticsQueryPack.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request when creating or updating a Log Analytics QueryPack. The updated QueryPack is returned. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="queryPacksDelete"></a>
# **queryPacksDelete**
> queryPacksDelete(resourceGroupName, apiVersion, subscriptionId, queryPackName)



Deletes a Log Analytics QueryPack.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String queryPackName = "queryPackName_example"; // String | The name of the Log Analytics QueryPack resource.
    try {
      apiInstance.queryPacksDelete(resourceGroupName, apiVersion, subscriptionId, queryPackName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#queryPacksDelete");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **queryPackName** | **String**| The name of the Log Analytics QueryPack resource. | |

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
| **200** | Successful request when deleting a Log Analytics QueryPack. |  -  |
| **204** | The specified QueryPack does not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="queryPacksGet"></a>
# **queryPacksGet**
> LogAnalyticsQueryPack queryPacksGet(resourceGroupName, apiVersion, subscriptionId, queryPackName)



Returns a Log Analytics QueryPack.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String queryPackName = "queryPackName_example"; // String | The name of the Log Analytics QueryPack resource.
    try {
      LogAnalyticsQueryPack result = apiInstance.queryPacksGet(resourceGroupName, apiVersion, subscriptionId, queryPackName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#queryPacksGet");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **queryPackName** | **String**| The name of the Log Analytics QueryPack resource. | |

### Return type

[**LogAnalyticsQueryPack**](LogAnalyticsQueryPack.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Log Analytics QueryPack definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="queryPacksList"></a>
# **queryPacksList**
> LogAnalyticsQueryPackListResult queryPacksList(apiVersion, subscriptionId)



Gets a list of all Log Analytics QueryPacks within a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      LogAnalyticsQueryPackListResult result = apiInstance.queryPacksList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#queryPacksList");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**LogAnalyticsQueryPackListResult**](LogAnalyticsQueryPackListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list containing 0 or more Log Analytics QueryPack definitions. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="queryPacksListByResourceGroup"></a>
# **queryPacksListByResourceGroup**
> LogAnalyticsQueryPackListResult queryPacksListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets a list of Log Analytics QueryPacks within a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      LogAnalyticsQueryPackListResult result = apiInstance.queryPacksListByResourceGroup(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#queryPacksListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**LogAnalyticsQueryPackListResult**](LogAnalyticsQueryPackListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list containing 0 or more Log Analytics QueryPack definitions. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="queryPacksUpdateTags"></a>
# **queryPacksUpdateTags**
> LogAnalyticsQueryPack queryPacksUpdateTags(resourceGroupName, apiVersion, subscriptionId, queryPackName, queryPackTags)



Updates an existing QueryPack&#39;s tags. To update other fields use the CreateOrUpdate method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String queryPackName = "queryPackName_example"; // String | The name of the Log Analytics QueryPack resource.
    TagsResource queryPackTags = new TagsResource(); // TagsResource | Updated tag information to set into the QueryPack instance.
    try {
      LogAnalyticsQueryPack result = apiInstance.queryPacksUpdateTags(resourceGroupName, apiVersion, subscriptionId, queryPackName, queryPackTags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#queryPacksUpdateTags");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **queryPackName** | **String**| The name of the Log Analytics QueryPack resource. | |
| **queryPackTags** | [**TagsResource**](TagsResource.md)| Updated tag information to set into the QueryPack instance. | |

### Return type

[**LogAnalyticsQueryPack**](LogAnalyticsQueryPack.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updating the Log Analytics QueryPack&#39;s tags was successful. QueryPack tags are updated and returned with the rest of the QueryPack&#39;s object properties. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

