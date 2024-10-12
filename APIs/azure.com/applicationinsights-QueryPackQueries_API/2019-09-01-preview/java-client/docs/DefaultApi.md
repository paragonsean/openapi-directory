# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**queriesDelete**](DefaultApi.md#queriesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/queryPacks/{queryPackName}/queries/{queryId} |  |
| [**queriesGet**](DefaultApi.md#queriesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/queryPacks/{queryPackName}/queries/{queryId} |  |
| [**queriesList**](DefaultApi.md#queriesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/queryPacks/{queryPackName}/queries |  |
| [**queriesPut**](DefaultApi.md#queriesPut) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/queryPacks/{queryPackName}/queries/{queryId} |  |
| [**queriesSearch**](DefaultApi.md#queriesSearch) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/queryPacks/{queryPackName}/queries/search |  |


<a id="queriesDelete"></a>
# **queriesDelete**
> queriesDelete(subscriptionId, resourceGroupName, queryPackName, queryId, apiVersion)



Deletes a specific Query defined within an Log Analytics QueryPack.

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
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String queryPackName = "queryPackName_example"; // String | The name of the Log Analytics QueryPack resource.
    String queryId = "queryId_example"; // String | The id of a specific query defined in the Log Analytics QueryPack
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      apiInstance.queriesDelete(subscriptionId, resourceGroupName, queryPackName, queryId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#queriesDelete");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **queryPackName** | **String**| The name of the Log Analytics QueryPack resource. | |
| **queryId** | **String**| The id of a specific query defined in the Log Analytics QueryPack | |
| **apiVersion** | **String**| The API version to use for this operation. | |

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
| **200** | The query has been successfully removed from the Log Analytics QueryPack |  -  |
| **204** | The specified query or associated QueryPack does not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="queriesGet"></a>
# **queriesGet**
> LogAnalyticsQueryPackQuery queriesGet(subscriptionId, resourceGroupName, queryPackName, queryId, apiVersion)



Gets a specific Log Analytics Query defined within a Log Analytics QueryPack.

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
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String queryPackName = "queryPackName_example"; // String | The name of the Log Analytics QueryPack resource.
    String queryId = "queryId_example"; // String | The id of a specific query defined in the Log Analytics QueryPack
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      LogAnalyticsQueryPackQuery result = apiInstance.queriesGet(subscriptionId, resourceGroupName, queryPackName, queryId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#queriesGet");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **queryPackName** | **String**| The name of the Log Analytics QueryPack resource. | |
| **queryId** | **String**| The id of a specific query defined in the Log Analytics QueryPack | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**LogAnalyticsQueryPackQuery**](LogAnalyticsQueryPackQuery.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A single query contained within the Log Analytics QueryPack. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="queriesList"></a>
# **queriesList**
> LogAnalyticsQueryPackQueryListResult queriesList(subscriptionId, resourceGroupName, queryPackName, apiVersion, $top, includeBody, $skipToken)



Gets a list of Queries defined within a Log Analytics QueryPack.

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
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String queryPackName = "queryPackName_example"; // String | The name of the Log Analytics QueryPack resource.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    Integer $top = 56; // Integer | Maximum items returned in page.
    Boolean includeBody = true; // Boolean | Flag indicating whether or not to return the body of each applicable query. If false, only return the query information.
    String $skipToken = "$skipToken_example"; // String | Base64 encoded token used to fetch the next page of items. Default is null.
    try {
      LogAnalyticsQueryPackQueryListResult result = apiInstance.queriesList(subscriptionId, resourceGroupName, queryPackName, apiVersion, $top, includeBody, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#queriesList");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **queryPackName** | **String**| The name of the Log Analytics QueryPack resource. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **$top** | **Integer**| Maximum items returned in page. | [optional] |
| **includeBody** | **Boolean**| Flag indicating whether or not to return the body of each applicable query. If false, only return the query information. | [optional] |
| **$skipToken** | **String**| Base64 encoded token used to fetch the next page of items. Default is null. | [optional] |

### Return type

[**LogAnalyticsQueryPackQueryListResult**](LogAnalyticsQueryPackQueryListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list containing 0 or more queries contained within the Log Analytics QueryPack. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="queriesPut"></a>
# **queriesPut**
> LogAnalyticsQueryPackQuery queriesPut(subscriptionId, resourceGroupName, queryPackName, queryId, apiVersion, queryPayload)



Adds or Updates a specific Query within a Log Analytics QueryPack.

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
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String queryPackName = "queryPackName_example"; // String | The name of the Log Analytics QueryPack resource.
    String queryId = "queryId_example"; // String | The id of a specific query defined in the Log Analytics QueryPack
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    LogAnalyticsQueryPackQuery queryPayload = new LogAnalyticsQueryPackQuery(); // LogAnalyticsQueryPackQuery | Properties that need to be specified to create a new query and add it to a Log Analytics QueryPack.
    try {
      LogAnalyticsQueryPackQuery result = apiInstance.queriesPut(subscriptionId, resourceGroupName, queryPackName, queryId, apiVersion, queryPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#queriesPut");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **queryPackName** | **String**| The name of the Log Analytics QueryPack resource. | |
| **queryId** | **String**| The id of a specific query defined in the Log Analytics QueryPack | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **queryPayload** | [**LogAnalyticsQueryPackQuery**](LogAnalyticsQueryPackQuery.md)| Properties that need to be specified to create a new query and add it to a Log Analytics QueryPack. | |

### Return type

[**LogAnalyticsQueryPackQuery**](LogAnalyticsQueryPackQuery.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The new or updated query contained within the Log Analytics QueryPack. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="queriesSearch"></a>
# **queriesSearch**
> LogAnalyticsQueryPackQueryListResult queriesSearch(subscriptionId, resourceGroupName, queryPackName, apiVersion, querySearchProperties, $top, includeBody, $skipToken)



Search a list of Queries defined within a Log Analytics QueryPack according to given search properties.

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
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String queryPackName = "queryPackName_example"; // String | The name of the Log Analytics QueryPack resource.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    LogAnalyticsQueryPackQuerySearchProperties querySearchProperties = new LogAnalyticsQueryPackQuerySearchProperties(); // LogAnalyticsQueryPackQuerySearchProperties | Properties by which to search queries in the given Log Analytics QueryPack.
    Integer $top = 56; // Integer | Maximum items returned in page.
    Boolean includeBody = true; // Boolean | Flag indicating whether or not to return the body of each applicable query. If false, only return the query information.
    String $skipToken = "$skipToken_example"; // String | Base64 encoded token used to fetch the next page of items. Default is null.
    try {
      LogAnalyticsQueryPackQueryListResult result = apiInstance.queriesSearch(subscriptionId, resourceGroupName, queryPackName, apiVersion, querySearchProperties, $top, includeBody, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#queriesSearch");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **queryPackName** | **String**| The name of the Log Analytics QueryPack resource. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **querySearchProperties** | [**LogAnalyticsQueryPackQuerySearchProperties**](LogAnalyticsQueryPackQuerySearchProperties.md)| Properties by which to search queries in the given Log Analytics QueryPack. | |
| **$top** | **Integer**| Maximum items returned in page. | [optional] |
| **includeBody** | **Boolean**| Flag indicating whether or not to return the body of each applicable query. If false, only return the query information. | [optional] |
| **$skipToken** | **String**| Base64 encoded token used to fetch the next page of items. Default is null. | [optional] |

### Return type

[**LogAnalyticsQueryPackQueryListResult**](LogAnalyticsQueryPackQueryListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list containing 0 or more queries contained within the Log Analytics QueryPack. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

