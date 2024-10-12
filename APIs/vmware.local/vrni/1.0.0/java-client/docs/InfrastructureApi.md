# InfrastructureApi

All URIs are relative to *http://vmware.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNode**](InfrastructureApi.md#getNode) | **GET** /infra/nodes/{id} | Show node details |
| [**listNodes**](InfrastructureApi.md#listNodes) | **GET** /infra/nodes | List nodes |


<a id="getNode"></a>
# **getNode**
> Node getNode(id)

Show node details

Get details of infrastructure nodes. Only admin users can get this information. The proxy id is required for adding a data source for selecting appropriate proxy node to add the data source.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfrastructureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    InfrastructureApi apiInstance = new InfrastructureApi(defaultClient);
    String id = "id_example"; // String | entity id
    try {
      Node result = apiInstance.getNode(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfrastructureApi#getNode");
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
| **id** | **String**| entity id | |

### Return type

[**Node**](Node.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, entity_type, id, ip_address, node_id, node_type

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="listNodes"></a>
# **listNodes**
> NodeListResult listNodes()

List nodes

Get list of infrastructure nodes. Only admin users can retrieve this information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfrastructureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    InfrastructureApi apiInstance = new InfrastructureApi(defaultClient);
    try {
      NodeListResult result = apiInstance.listNodes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfrastructureApi#listNodes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeListResult**](NodeListResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, results, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Error |  -  |

