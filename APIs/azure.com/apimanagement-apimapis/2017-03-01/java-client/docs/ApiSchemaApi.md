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
> SchemaContract apiSchemaCreateOrUpdate(resourceGroupName, serviceName, apiId, schemaId, apiVersion, subscriptionId, parameters, ifMatch)



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
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String schemaId = "schemaId_example"; // String | Schema identifier within an API. Must be unique in the current API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    SchemaContract parameters = new SchemaContract(); // SchemaContract | The schema contents to apply.
    String ifMatch = "ifMatch_example"; // String | The entity state (Etag) version of the Api Schema to update. A value of \"*\" can be used for If-Match to unconditionally apply the operation.
    try {
      SchemaContract result = apiInstance.apiSchemaCreateOrUpdate(resourceGroupName, serviceName, apiId, schemaId, apiVersion, subscriptionId, parameters, ifMatch);
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
| **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | |
| **schemaId** | **String**| Schema identifier within an API. Must be unique in the current API Management service instance. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**SchemaContract**](SchemaContract.md)| The schema contents to apply. | |
| **ifMatch** | **String**| The entity state (Etag) version of the Api Schema to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation. | [optional] |

### Return type

[**SchemaContract**](SchemaContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Api schema configuration of the tenant was successfully updated. |  -  |
| **201** | Api schema configuration was successfully created. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiSchemaDelete"></a>
# **apiSchemaDelete**
> apiSchemaDelete(resourceGroupName, serviceName, apiId, schemaId, ifMatch, apiVersion, subscriptionId)



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
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String schemaId = "schemaId_example"; // String | Schema identifier within an API. Must be unique in the current API Management service instance.
    String ifMatch = "ifMatch_example"; // String | The entity state (Etag) version of the Api schema to update. A value of \"*\" can be used for If-Match to unconditionally apply the operation.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.apiSchemaDelete(resourceGroupName, serviceName, apiId, schemaId, ifMatch, apiVersion, subscriptionId);
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
| **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | |
| **schemaId** | **String**| Schema identifier within an API. Must be unique in the current API Management service instance. | |
| **ifMatch** | **String**| The entity state (Etag) version of the Api schema to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation. | |
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
| **204** | Successfully deleted the schema configuration at the API level. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiSchemaGet"></a>
# **apiSchemaGet**
> SchemaContract apiSchemaGet(resourceGroupName, serviceName, apiId, schemaId, apiVersion, subscriptionId)



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
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String schemaId = "schemaId_example"; // String | Schema identifier within an API. Must be unique in the current API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SchemaContract result = apiInstance.apiSchemaGet(resourceGroupName, serviceName, apiId, schemaId, apiVersion, subscriptionId);
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
| **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | |
| **schemaId** | **String**| Schema identifier within an API. Must be unique in the current API Management service instance. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**SchemaContract**](SchemaContract.md)

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
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
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
| **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | |
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
> SchemaCollection apiSchemaListByApi(resourceGroupName, serviceName, apiId, apiVersion, subscriptionId)



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
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SchemaCollection result = apiInstance.apiSchemaListByApi(resourceGroupName, serviceName, apiId, apiVersion, subscriptionId);
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
| **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**SchemaCollection**](SchemaCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Apis Schema Collection. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

