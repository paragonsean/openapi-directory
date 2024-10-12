# EntitiesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**entitiesList**](EntitiesApi.md#entitiesList) | **POST** /providers/Microsoft.Management/getEntities |  |


<a id="entitiesList"></a>
# **entitiesList**
> EntityListResult entitiesList(apiVersion, $skiptoken, groupName, cacheControl)



List all entities (Management Groups, Subscriptions, etc.) for the authenticated user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-01-01-preview.
    String $skiptoken = "$skiptoken_example"; // String | Page continuation token is only used if a previous operation returned a partial result.  If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls. 
    String groupName = "groupName_example"; // String | A filter which allows the call to be filtered for a specific group.
    String cacheControl = "no-cache"; // String | Indicates that the request shouldn't utilize any caches.
    try {
      EntityListResult result = apiInstance.entitiesList(apiVersion, $skiptoken, groupName, cacheControl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#entitiesList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-01-01-preview. | |
| **$skiptoken** | **String**| Page continuation token is only used if a previous operation returned a partial result.  If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls.  | [optional] |
| **groupName** | **String**| A filter which allows the call to be filtered for a specific group. | [optional] |
| **cacheControl** | **String**| Indicates that the request shouldn&#39;t utilize any caches. | [optional] [default to no-cache] |

### Return type

[**EntityListResult**](EntityListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

