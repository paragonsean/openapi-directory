# ApiSchemaApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiSchemaCreateOrUpdate**](ApiSchemaApi.md#apiSchemaCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/schemas/{schemaId} |  |
| [**apiSchemaDelete**](ApiSchemaApi.md#apiSchemaDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/schemas/{schemaId} |  |
| [**apiSchemaGet**](ApiSchemaApi.md#apiSchemaGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/schemas/{schemaId} |  |
| [**apiSchemaGetEntityTag**](ApiSchemaApi.md#apiSchemaGetEntityTag) | **HEAD** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/schemas/{schemaId} |  |
| [**apiSchemaListByApi**](ApiSchemaApi.md#apiSchemaListByApi) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/schemas |  |


<a id="apiSchemaCreateOrUpdate"></a>
# **apiSchemaCreateOrUpdate**
> ApiSchemaGet200Response apiSchemaCreateOrUpdate(resourceGroupName, serviceName, apiId, schemaId, apiVersion, subscriptionId, parameters, ifMatch)



Creates or updates schema configuration for the API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiSchemaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiSchemaApi apiInstance = new ApiSchemaApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    String schemaId = "schemaId_example"; // String | Schema identifier within an API. Must be unique in the current API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ApiSchemaGet200Response parameters = new ApiSchemaGet200Response(); // ApiSchemaGet200Response | The schema contents to apply.
    String ifMatch = "ifMatch_example"; // String | ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    try {
      ApiSchemaGet200Response result = apiInstance.apiSchemaCreateOrUpdate(resourceGroupName, serviceName, apiId, schemaId, apiVersion, subscriptionId, parameters, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiSchemaApi#apiSchemaCreateOrUpdate");
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
| **schemaId** | **String**| Schema identifier within an API. Must be unique in the current API Management service instance. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ApiSchemaGet200Response**](ApiSchemaGet200Response.md)| The schema contents to apply. | |
| **ifMatch** | **String**| ETag of the Entity. Not required when creating an entity, but required when updating an entity. | [optional] |

### Return type

[**ApiSchemaGet200Response**](ApiSchemaGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Api schema configuration of the tenant was successfully updated. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **201** | Api schema configuration was successfully created. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **202** | Request to create or update Api schema configuration was accepted. Location header contains the URL where the status of the long running operation can be checked. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiSchemaDelete"></a>
# **apiSchemaDelete**
> apiSchemaDelete(resourceGroupName, serviceName, apiId, schemaId, ifMatch, apiVersion, subscriptionId, force)



Deletes the schema configuration at the Api.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiSchemaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiSchemaApi apiInstance = new ApiSchemaApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    String schemaId = "schemaId_example"; // String | Schema identifier within an API. Must be unique in the current API Management service instance.
    String ifMatch = "ifMatch_example"; // String | ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Boolean force = true; // Boolean | If true removes all references to the schema before deleting it.
    try {
      apiInstance.apiSchemaDelete(resourceGroupName, serviceName, apiId, schemaId, ifMatch, apiVersion, subscriptionId, force);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiSchemaApi#apiSchemaDelete");
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
| **schemaId** | **String**| Schema identifier within an API. Must be unique in the current API Management service instance. | |
| **ifMatch** | **String**| ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **force** | **Boolean**| If true removes all references to the schema before deleting it. | [optional] |

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
| **200** | Successfully deleted the schema configuration at the API level. |  -  |
| **204** | Successfully deleted the schema configuration at the API level. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiSchemaGet"></a>
# **apiSchemaGet**
> ApiSchemaGet200Response apiSchemaGet(resourceGroupName, serviceName, apiId, schemaId, apiVersion, subscriptionId)



Get the schema configuration at the API level.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiSchemaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiSchemaApi apiInstance = new ApiSchemaApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    String schemaId = "schemaId_example"; // String | Schema identifier within an API. Must be unique in the current API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ApiSchemaGet200Response result = apiInstance.apiSchemaGet(resourceGroupName, serviceName, apiId, schemaId, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiSchemaApi#apiSchemaGet");
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
| **schemaId** | **String**| Schema identifier within an API. Must be unique in the current API Management service instance. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ApiSchemaGet200Response**](ApiSchemaGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Api Schema information. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiSchemaGetEntityTag"></a>
# **apiSchemaGetEntityTag**
> apiSchemaGetEntityTag(resourceGroupName, serviceName, apiId, schemaId, apiVersion, subscriptionId)



Gets the entity state (Etag) version of the schema specified by its identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiSchemaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiSchemaApi apiInstance = new ApiSchemaApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    String schemaId = "schemaId_example"; // String | Schema identifier within an API. Must be unique in the current API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.apiSchemaGetEntityTag(resourceGroupName, serviceName, apiId, schemaId, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiSchemaApi#apiSchemaGetEntityTag");
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
| **schemaId** | **String**| Schema identifier within an API. Must be unique in the current API Management service instance. | |
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
| **200** | Specified schema entity exists and current entity state version is present in the ETag header. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiSchemaListByApi"></a>
# **apiSchemaListByApi**
> ApiSchemaListByApi200Response apiSchemaListByApi(resourceGroupName, serviceName, apiId, apiVersion, subscriptionId, $filter, $top, $skip)



Get the schema configuration at the API level.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiSchemaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiSchemaApi apiInstance = new ApiSchemaApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $filter = "$filter_example"; // String | |   Field     |     Usage     |     Supported operators     |     Supported functions     |</br>|-------------|-------------|-------------|-------------|</br>| contentType | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | </br>
    Integer $top = 56; // Integer | Number of records to return.
    Integer $skip = 56; // Integer | Number of records to skip.
    try {
      ApiSchemaListByApi200Response result = apiInstance.apiSchemaListByApi(resourceGroupName, serviceName, apiId, apiVersion, subscriptionId, $filter, $top, $skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiSchemaApi#apiSchemaListByApi");
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
| **$filter** | **String**| |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| contentType | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt; | [optional] |
| **$top** | **Integer**| Number of records to return. | [optional] |
| **$skip** | **Integer**| Number of records to skip. | [optional] |

### Return type

[**ApiSchemaListByApi200Response**](ApiSchemaListByApi200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Apis Schema Collection. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

