# ApiIssueCommentApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiIssueCommentCreateOrUpdate**](ApiIssueCommentApi.md#apiIssueCommentCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/issues/{issueId}/comments/{commentId} |  |
| [**apiIssueCommentDelete**](ApiIssueCommentApi.md#apiIssueCommentDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/issues/{issueId}/comments/{commentId} |  |
| [**apiIssueCommentGet**](ApiIssueCommentApi.md#apiIssueCommentGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/issues/{issueId}/comments/{commentId} |  |
| [**apiIssueCommentGetEntityTag**](ApiIssueCommentApi.md#apiIssueCommentGetEntityTag) | **HEAD** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/issues/{issueId}/comments/{commentId} |  |
| [**apiIssueCommentListByService**](ApiIssueCommentApi.md#apiIssueCommentListByService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/issues/{issueId}/comments |  |


<a id="apiIssueCommentCreateOrUpdate"></a>
# **apiIssueCommentCreateOrUpdate**
> ApiIssueCommentGet200Response apiIssueCommentCreateOrUpdate(resourceGroupName, serviceName, apiId, issueId, commentId, apiVersion, subscriptionId, parameters, ifMatch)



Creates a new Comment for the Issue in an API or updates an existing one.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiIssueCommentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiIssueCommentApi apiInstance = new ApiIssueCommentApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String issueId = "issueId_example"; // String | Issue identifier. Must be unique in the current API Management service instance.
    String commentId = "commentId_example"; // String | Comment identifier within an Issue. Must be unique in the current Issue.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ApiIssueCommentGet200Response parameters = new ApiIssueCommentGet200Response(); // ApiIssueCommentGet200Response | Create parameters.
    String ifMatch = "ifMatch_example"; // String | ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    try {
      ApiIssueCommentGet200Response result = apiInstance.apiIssueCommentCreateOrUpdate(resourceGroupName, serviceName, apiId, issueId, commentId, apiVersion, subscriptionId, parameters, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiIssueCommentApi#apiIssueCommentCreateOrUpdate");
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
| **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | |
| **issueId** | **String**| Issue identifier. Must be unique in the current API Management service instance. | |
| **commentId** | **String**| Comment identifier within an Issue. Must be unique in the current Issue. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ApiIssueCommentGet200Response**](ApiIssueCommentGet200Response.md)| Create parameters. | |
| **ifMatch** | **String**| ETag of the Entity. Not required when creating an entity, but required when updating an entity. | [optional] |

### Return type

[**ApiIssueCommentGet200Response**](ApiIssueCommentGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Api issue comment successfully updated |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **201** | New api issue comment successfully added |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiIssueCommentDelete"></a>
# **apiIssueCommentDelete**
> apiIssueCommentDelete(resourceGroupName, serviceName, apiId, issueId, commentId, ifMatch, apiVersion, subscriptionId)



Deletes the specified comment from an Issue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiIssueCommentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiIssueCommentApi apiInstance = new ApiIssueCommentApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String issueId = "issueId_example"; // String | Issue identifier. Must be unique in the current API Management service instance.
    String commentId = "commentId_example"; // String | Comment identifier within an Issue. Must be unique in the current Issue.
    String ifMatch = "ifMatch_example"; // String | ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.apiIssueCommentDelete(resourceGroupName, serviceName, apiId, issueId, commentId, ifMatch, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiIssueCommentApi#apiIssueCommentDelete");
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
| **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | |
| **issueId** | **String**| Issue identifier. Must be unique in the current API Management service instance. | |
| **commentId** | **String**| Comment identifier within an Issue. Must be unique in the current Issue. | |
| **ifMatch** | **String**| ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | Comment successfully removed |  -  |
| **204** | Comment successfully removed by previous request or does not exist |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiIssueCommentGet"></a>
# **apiIssueCommentGet**
> ApiIssueCommentGet200Response apiIssueCommentGet(resourceGroupName, serviceName, apiId, issueId, commentId, apiVersion, subscriptionId)



Gets the details of the issue Comment for an API specified by its identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiIssueCommentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiIssueCommentApi apiInstance = new ApiIssueCommentApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String issueId = "issueId_example"; // String | Issue identifier. Must be unique in the current API Management service instance.
    String commentId = "commentId_example"; // String | Comment identifier within an Issue. Must be unique in the current Issue.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ApiIssueCommentGet200Response result = apiInstance.apiIssueCommentGet(resourceGroupName, serviceName, apiId, issueId, commentId, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiIssueCommentApi#apiIssueCommentGet");
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
| **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | |
| **issueId** | **String**| Issue identifier. Must be unique in the current API Management service instance. | |
| **commentId** | **String**| Comment identifier within an Issue. Must be unique in the current Issue. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ApiIssueCommentGet200Response**](ApiIssueCommentGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body contains the specified issue Comment entity. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiIssueCommentGetEntityTag"></a>
# **apiIssueCommentGetEntityTag**
> apiIssueCommentGetEntityTag(resourceGroupName, serviceName, apiId, issueId, commentId, apiVersion, subscriptionId)



Gets the entity state (Etag) version of the issue Comment for an API specified by its identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiIssueCommentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiIssueCommentApi apiInstance = new ApiIssueCommentApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String issueId = "issueId_example"; // String | Issue identifier. Must be unique in the current API Management service instance.
    String commentId = "commentId_example"; // String | Comment identifier within an Issue. Must be unique in the current Issue.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.apiIssueCommentGetEntityTag(resourceGroupName, serviceName, apiId, issueId, commentId, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiIssueCommentApi#apiIssueCommentGetEntityTag");
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
| **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | |
| **issueId** | **String**| Issue identifier. Must be unique in the current API Management service instance. | |
| **commentId** | **String**| Comment identifier within an Issue. Must be unique in the current Issue. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | Operation completed successfully. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiIssueCommentListByService"></a>
# **apiIssueCommentListByService**
> ApiIssueCommentListByService200Response apiIssueCommentListByService(resourceGroupName, serviceName, apiId, issueId, apiVersion, subscriptionId, $filter, $top, $skip)



Lists all comments for the Issue associated with the specified API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiIssueCommentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiIssueCommentApi apiInstance = new ApiIssueCommentApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String issueId = "issueId_example"; // String | Issue identifier. Must be unique in the current API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $filter = "$filter_example"; // String | |   Field     |     Usage     |     Supported operators     |     Supported functions     |</br>|-------------|-------------|-------------|-------------|</br>| name | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | </br>| userId | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | </br>
    Integer $top = 56; // Integer | Number of records to return.
    Integer $skip = 56; // Integer | Number of records to skip.
    try {
      ApiIssueCommentListByService200Response result = apiInstance.apiIssueCommentListByService(resourceGroupName, serviceName, apiId, issueId, apiVersion, subscriptionId, $filter, $top, $skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiIssueCommentApi#apiIssueCommentListByService");
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
| **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | |
| **issueId** | **String**| Issue identifier. Must be unique in the current API Management service instance. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$filter** | **String**| |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| name | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| userId | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt; | [optional] |
| **$top** | **Integer**| Number of records to return. | [optional] |
| **$skip** | **Integer**| Number of records to skip. | [optional] |

### Return type

[**ApiIssueCommentListByService200Response**](ApiIssueCommentListByService200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paged Result response of issue comments for the API. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

