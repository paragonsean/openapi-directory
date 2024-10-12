# ReleasesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiReleaseCreate**](ReleasesApi.md#apiReleaseCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/releases/{releaseId} |  |
| [**apiReleaseDelete**](ReleasesApi.md#apiReleaseDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/releases/{releaseId} |  |
| [**apiReleaseGet**](ReleasesApi.md#apiReleaseGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/releases/{releaseId} |  |
| [**apiReleaseGetEntityTag**](ReleasesApi.md#apiReleaseGetEntityTag) | **HEAD** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/releases/{releaseId} |  |
| [**apiReleaseList**](ReleasesApi.md#apiReleaseList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/releases |  |
| [**apiReleaseUpdate**](ReleasesApi.md#apiReleaseUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/releases/{releaseId} |  |


<a id="apiReleaseCreate"></a>
# **apiReleaseCreate**
> ApiReleaseContract apiReleaseCreate(resourceGroupName, serviceName, apiVersion, subscriptionId, apiId, releaseId, parameters)



Creates a new Release for the API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReleasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReleasesApi apiInstance = new ReleasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String releaseId = "releaseId_example"; // String | Release identifier within an API. Must be unique in the current API Management service instance.
    ApiReleaseContract parameters = new ApiReleaseContract(); // ApiReleaseContract | Create parameters.
    try {
      ApiReleaseContract result = apiInstance.apiReleaseCreate(resourceGroupName, serviceName, apiVersion, subscriptionId, apiId, releaseId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReleasesApi#apiReleaseCreate");
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
| **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | |
| **releaseId** | **String**| Release identifier within an API. Must be unique in the current API Management service instance. | |
| **parameters** | [**ApiReleaseContract**](ApiReleaseContract.md)| Create parameters. | |

### Return type

[**ApiReleaseContract**](ApiReleaseContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Release was successfully updated. |  -  |
| **201** | Release was successfully created. |  -  |
| **0** | Error response describing why the release failed. |  -  |

<a id="apiReleaseDelete"></a>
# **apiReleaseDelete**
> apiReleaseDelete(resourceGroupName, serviceName, apiVersion, subscriptionId, apiId, releaseId, ifMatch)



Deletes the specified release in the API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReleasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReleasesApi apiInstance = new ReleasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String releaseId = "releaseId_example"; // String | Release identifier within an API. Must be unique in the current API Management service instance.
    String ifMatch = "ifMatch_example"; // String | ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    try {
      apiInstance.apiReleaseDelete(resourceGroupName, serviceName, apiVersion, subscriptionId, apiId, releaseId, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReleasesApi#apiReleaseDelete");
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
| **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | |
| **releaseId** | **String**| Release identifier within an API. Must be unique in the current API Management service instance. | |
| **ifMatch** | **String**| ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update. | |

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
| **200** | The release was successfully deleted. |  -  |
| **204** | The release was successfully deleted. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiReleaseGet"></a>
# **apiReleaseGet**
> ApiReleaseContract apiReleaseGet(resourceGroupName, serviceName, apiVersion, subscriptionId, apiId, releaseId)



Returns the details of an API release.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReleasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReleasesApi apiInstance = new ReleasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String releaseId = "releaseId_example"; // String | Release identifier within an API. Must be unique in the current API Management service instance.
    try {
      ApiReleaseContract result = apiInstance.apiReleaseGet(resourceGroupName, serviceName, apiVersion, subscriptionId, apiId, releaseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReleasesApi#apiReleaseGet");
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
| **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | |
| **releaseId** | **String**| Release identifier within an API. Must be unique in the current API Management service instance. | |

### Return type

[**ApiReleaseContract**](ApiReleaseContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation returns the details of an API Release. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiReleaseGetEntityTag"></a>
# **apiReleaseGetEntityTag**
> apiReleaseGetEntityTag(resourceGroupName, serviceName, apiVersion, subscriptionId, apiId, releaseId)



Returns the etag of an API release.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReleasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReleasesApi apiInstance = new ReleasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String releaseId = "releaseId_example"; // String | Release identifier within an API. Must be unique in the current API Management service instance.
    try {
      apiInstance.apiReleaseGetEntityTag(resourceGroupName, serviceName, apiVersion, subscriptionId, apiId, releaseId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReleasesApi#apiReleaseGetEntityTag");
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
| **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | |
| **releaseId** | **String**| Release identifier within an API. Must be unique in the current API Management service instance. | |

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
| **200** | The operation returns the details of an API Release. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiReleaseList"></a>
# **apiReleaseList**
> ApiReleaseCollection apiReleaseList(resourceGroupName, serviceName, apiId, apiVersion, subscriptionId, $filter, $top, $skip)



Lists all releases of an API. An API release is created when making an API Revision current. Releases are also used to rollback to previous revisions. Results will be paged and can be constrained by the $top and $skip parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReleasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReleasesApi apiInstance = new ReleasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $filter = "$filter_example"; // String | | Field | Supported operators    | Supported functions                         | |-------|------------------------|---------------------------------------------| | name  | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | |notes|ge le eq ne gt lt|substringof contains startswith endswith|
    Integer $top = 56; // Integer | Number of records to return.
    Integer $skip = 56; // Integer | Number of records to skip.
    try {
      ApiReleaseCollection result = apiInstance.apiReleaseList(resourceGroupName, serviceName, apiId, apiVersion, subscriptionId, $filter, $top, $skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReleasesApi#apiReleaseList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$filter** | **String**| | Field | Supported operators    | Supported functions                         | |-------|------------------------|---------------------------------------------| | name  | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | |notes|ge le eq ne gt lt|substringof contains startswith endswith| | [optional] |
| **$top** | **Integer**| Number of records to return. | [optional] |
| **$skip** | **Integer**| Number of records to skip. | [optional] |

### Return type

[**ApiReleaseCollection**](ApiReleaseCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation returns a list of API Releases. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiReleaseUpdate"></a>
# **apiReleaseUpdate**
> apiReleaseUpdate(resourceGroupName, serviceName, apiVersion, subscriptionId, apiId, releaseId, ifMatch, parameters)



Updates the details of the release of the API specified by its identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReleasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReleasesApi apiInstance = new ReleasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String releaseId = "releaseId_example"; // String | Release identifier within an API. Must be unique in the current API Management service instance.
    String ifMatch = "ifMatch_example"; // String | ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    ApiReleaseContract parameters = new ApiReleaseContract(); // ApiReleaseContract | API Release Update parameters.
    try {
      apiInstance.apiReleaseUpdate(resourceGroupName, serviceName, apiVersion, subscriptionId, apiId, releaseId, ifMatch, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReleasesApi#apiReleaseUpdate");
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
| **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | |
| **releaseId** | **String**| Release identifier within an API. Must be unique in the current API Management service instance. | |
| **ifMatch** | **String**| ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update. | |
| **parameters** | [**ApiReleaseContract**](ApiReleaseContract.md)| API Release Update parameters. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The operation was successfully updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

