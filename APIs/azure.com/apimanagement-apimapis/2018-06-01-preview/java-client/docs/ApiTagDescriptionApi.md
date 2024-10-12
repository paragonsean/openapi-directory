# ApiTagDescriptionApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tagDescriptionCreateOrUpdate**](ApiTagDescriptionApi.md#tagDescriptionCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/tagDescriptions/{tagId} |  |
| [**tagDescriptionDelete**](ApiTagDescriptionApi.md#tagDescriptionDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/tagDescriptions/{tagId} |  |
| [**tagDescriptionGet**](ApiTagDescriptionApi.md#tagDescriptionGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/tagDescriptions/{tagId} |  |
| [**tagDescriptionGetEntityState**](ApiTagDescriptionApi.md#tagDescriptionGetEntityState) | **HEAD** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/tagDescriptions/{tagId} |  |
| [**tagDescriptionListByApi**](ApiTagDescriptionApi.md#tagDescriptionListByApi) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/tagDescriptions |  |


<a id="tagDescriptionCreateOrUpdate"></a>
# **tagDescriptionCreateOrUpdate**
> TagDescriptionGet200Response tagDescriptionCreateOrUpdate(resourceGroupName, serviceName, apiId, tagId, apiVersion, subscriptionId, parameters, ifMatch)



Create/Update tag description in scope of the Api.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiTagDescriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiTagDescriptionApi apiInstance = new ApiTagDescriptionApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    String tagId = "tagId_example"; // String | Tag identifier. Must be unique in the current API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    TagDescriptionCreateOrUpdateRequest parameters = new TagDescriptionCreateOrUpdateRequest(); // TagDescriptionCreateOrUpdateRequest | Create parameters.
    String ifMatch = "ifMatch_example"; // String | ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    try {
      TagDescriptionGet200Response result = apiInstance.tagDescriptionCreateOrUpdate(resourceGroupName, serviceName, apiId, tagId, apiVersion, subscriptionId, parameters, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiTagDescriptionApi#tagDescriptionCreateOrUpdate");
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
| **apiId** | **String**| API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number. | |
| **tagId** | **String**| Tag identifier. Must be unique in the current API Management service instance. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**TagDescriptionCreateOrUpdateRequest**](TagDescriptionCreateOrUpdateRequest.md)| Create parameters. | |
| **ifMatch** | **String**| ETag of the Entity. Not required when creating an entity, but required when updating an entity. | [optional] |

### Return type

[**TagDescriptionGet200Response**](TagDescriptionGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tag Description was updated for the Api. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **201** | Tag Description was created for the Api. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tagDescriptionDelete"></a>
# **tagDescriptionDelete**
> tagDescriptionDelete(resourceGroupName, serviceName, apiId, tagId, ifMatch, apiVersion, subscriptionId)



Delete tag description for the Api.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiTagDescriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiTagDescriptionApi apiInstance = new ApiTagDescriptionApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    String tagId = "tagId_example"; // String | Tag identifier. Must be unique in the current API Management service instance.
    String ifMatch = "ifMatch_example"; // String | ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.tagDescriptionDelete(resourceGroupName, serviceName, apiId, tagId, ifMatch, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiTagDescriptionApi#tagDescriptionDelete");
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
| **apiId** | **String**| API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number. | |
| **tagId** | **String**| Tag identifier. Must be unique in the current API Management service instance. | |
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
| **200** | Tag description successfully removed |  -  |
| **204** | Tag description successfully removed by previous request or does not exist |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tagDescriptionGet"></a>
# **tagDescriptionGet**
> TagDescriptionGet200Response tagDescriptionGet(resourceGroupName, serviceName, apiId, tagId, apiVersion, subscriptionId)



Get Tag description in scope of API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiTagDescriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiTagDescriptionApi apiInstance = new ApiTagDescriptionApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    String tagId = "tagId_example"; // String | Tag identifier. Must be unique in the current API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      TagDescriptionGet200Response result = apiInstance.tagDescriptionGet(resourceGroupName, serviceName, apiId, tagId, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiTagDescriptionApi#tagDescriptionGet");
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
| **apiId** | **String**| API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number. | |
| **tagId** | **String**| Tag identifier. Must be unique in the current API Management service instance. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**TagDescriptionGet200Response**](TagDescriptionGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets the description of the tag specified by its identifier in scope if the Api. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tagDescriptionGetEntityState"></a>
# **tagDescriptionGetEntityState**
> tagDescriptionGetEntityState(resourceGroupName, serviceName, apiId, tagId, apiVersion, subscriptionId)



Gets the entity state version of the tag specified by its identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiTagDescriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiTagDescriptionApi apiInstance = new ApiTagDescriptionApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    String tagId = "tagId_example"; // String | Tag identifier. Must be unique in the current API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.tagDescriptionGetEntityState(resourceGroupName, serviceName, apiId, tagId, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiTagDescriptionApi#tagDescriptionGetEntityState");
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
| **apiId** | **String**| API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number. | |
| **tagId** | **String**| Tag identifier. Must be unique in the current API Management service instance. | |
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
| **200** | Empty response body, ETag header entity state version. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tagDescriptionListByApi"></a>
# **tagDescriptionListByApi**
> TagDescriptionListByApi200Response tagDescriptionListByApi(resourceGroupName, serviceName, apiId, apiVersion, subscriptionId, $filter, $top, $skip)



Lists all Tags descriptions in scope of API. Model similar to swagger - tagDescription is defined on API level but tag may be assigned to the Operations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiTagDescriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiTagDescriptionApi apiInstance = new ApiTagDescriptionApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $filter = "$filter_example"; // String | | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------|   |displayName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |name | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| 
    Integer $top = 56; // Integer | Number of records to return.
    Integer $skip = 56; // Integer | Number of records to skip.
    try {
      TagDescriptionListByApi200Response result = apiInstance.tagDescriptionListByApi(resourceGroupName, serviceName, apiId, apiVersion, subscriptionId, $filter, $top, $skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiTagDescriptionApi#tagDescriptionListByApi");
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
| **apiId** | **String**| API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$filter** | **String**| | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------|   |displayName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |name | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith|  | [optional] |
| **$top** | **Integer**| Number of records to return. | [optional] |
| **$skip** | **Integer**| Number of records to skip. | [optional] |

### Return type

[**TagDescriptionListByApi200Response**](TagDescriptionListByApi200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation returns a collection of tagDescriptions associated with the Api entity. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

