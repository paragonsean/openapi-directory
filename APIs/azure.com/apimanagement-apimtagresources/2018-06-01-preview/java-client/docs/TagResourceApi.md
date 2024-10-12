# TagResourceApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tagResourceListByService**](TagResourceApi.md#tagResourceListByService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/tagResources |  |


<a id="tagResourceListByService"></a>
# **tagResourceListByService**
> TagResourceListByService200Response tagResourceListByService(resourceGroupName, serviceName, apiVersion, subscriptionId, $filter, $top, $skip)



Lists a collection of resources associated with tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TagResourceApi apiInstance = new TagResourceApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $filter = "$filter_example"; // String | | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------|   |aid | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |name | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |displayName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |apiName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |apiRevision | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |path | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |serviceUrl | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |method | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |urlTemplate | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |terms | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |state | eq |    | |isCurrent | eq |    | 
    Integer $top = 56; // Integer | Number of records to return.
    Integer $skip = 56; // Integer | Number of records to skip.
    try {
      TagResourceListByService200Response result = apiInstance.tagResourceListByService(resourceGroupName, serviceName, apiVersion, subscriptionId, $filter, $top, $skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagResourceApi#tagResourceListByService");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$filter** | **String**| | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------|   |aid | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |name | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |displayName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |apiName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |apiRevision | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |path | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |serviceUrl | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |method | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |urlTemplate | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |terms | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |state | eq |    | |isCurrent | eq |    |  | [optional] |
| **$top** | **Integer**| Number of records to return. | [optional] |
| **$skip** | **Integer**| Number of records to skip. | [optional] |

### Return type

[**TagResourceListByService200Response**](TagResourceListByService200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lists a collection of TagResource entities. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

