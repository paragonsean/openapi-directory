# ResourcesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resources**](ResourcesApi.md#resources) | **POST** /providers/Microsoft.ResourceGraph/resources |  |


<a id="resources"></a>
# **resources**
> QueryResponse resources(apiVersion, query)



Queries the resources managed by Azure Resource Manager for all subscriptions specified in the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version.
    QueryRequest query = new QueryRequest(); // QueryRequest | Request specifying query and its options.
    try {
      QueryResponse result = apiInstance.resources(apiVersion, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#resources");
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
| **apiVersion** | **String**| API version. | |
| **query** | [**QueryRequest**](QueryRequest.md)| Request specifying query and its options. | |

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of the query operation |  -  |
| **0** | An error occurred while processing the request. See the error.code parameter to identify the specific error. |  -  |

