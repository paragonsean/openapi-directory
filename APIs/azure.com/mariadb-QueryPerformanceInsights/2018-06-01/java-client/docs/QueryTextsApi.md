# QueryTextsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**queryTextsGet**](QueryTextsApi.md#queryTextsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMariaDB/servers/{serverName}/queryTexts/{queryId} |  |
| [**queryTextsListByServer**](QueryTextsApi.md#queryTextsListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMariaDB/servers/{serverName}/queryTexts |  |


<a id="queryTextsGet"></a>
# **queryTextsGet**
> QueryText queryTextsGet(apiVersion, subscriptionId, resourceGroupName, serverName, queryId)



Retrieve the Query-Store query texts for the queryId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryTextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QueryTextsApi apiInstance = new QueryTextsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String serverName = "serverName_example"; // String | The name of the server.
    String queryId = "queryId_example"; // String | The Query-Store query identifier.
    try {
      QueryText result = apiInstance.queryTextsGet(apiVersion, subscriptionId, resourceGroupName, serverName, queryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryTextsApi#queryTextsGet");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **serverName** | **String**| The name of the server. | |
| **queryId** | **String**| The Query-Store query identifier. | |

### Return type

[**QueryText**](QueryText.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="queryTextsListByServer"></a>
# **queryTextsListByServer**
> QueryTextsResultList queryTextsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName, queryIds)



Retrieve the Query-Store query texts for specified queryIds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryTextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QueryTextsApi apiInstance = new QueryTextsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String serverName = "serverName_example"; // String | The name of the server.
    List<String> queryIds = Arrays.asList(); // List<String> | The query identifiers
    try {
      QueryTextsResultList result = apiInstance.queryTextsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName, queryIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryTextsApi#queryTextsListByServer");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **serverName** | **String**| The name of the server. | |
| **queryIds** | [**List&lt;String&gt;**](String.md)| The query identifiers | |

### Return type

[**QueryTextsResultList**](QueryTextsResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

