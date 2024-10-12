# OpenIdConnectProvidersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**openIdConnectProviderCreateOrUpdate**](OpenIdConnectProvidersApi.md#openIdConnectProviderCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/openidConnectProviders/{opid} |  |
| [**openIdConnectProviderDelete**](OpenIdConnectProvidersApi.md#openIdConnectProviderDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/openidConnectProviders/{opid} |  |
| [**openIdConnectProviderGet**](OpenIdConnectProvidersApi.md#openIdConnectProviderGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/openidConnectProviders/{opid} |  |
| [**openIdConnectProviderGetEntityTag**](OpenIdConnectProvidersApi.md#openIdConnectProviderGetEntityTag) | **HEAD** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/openidConnectProviders/{opid} |  |
| [**openIdConnectProviderListByService**](OpenIdConnectProvidersApi.md#openIdConnectProviderListByService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/openidConnectProviders |  |
| [**openIdConnectProviderUpdate**](OpenIdConnectProvidersApi.md#openIdConnectProviderUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/openidConnectProviders/{opid} |  |


<a id="openIdConnectProviderCreateOrUpdate"></a>
# **openIdConnectProviderCreateOrUpdate**
> OpenidConnectProviderContract openIdConnectProviderCreateOrUpdate(resourceGroupName, serviceName, opid, apiVersion, subscriptionId, parameters)



Creates or updates the OpenID Connect Provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenIdConnectProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OpenIdConnectProvidersApi apiInstance = new OpenIdConnectProvidersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String opid = "opid_example"; // String | Identifier of the OpenID Connect Provider.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    OpenidConnectProviderContract parameters = new OpenidConnectProviderContract(); // OpenidConnectProviderContract | Create parameters.
    try {
      OpenidConnectProviderContract result = apiInstance.openIdConnectProviderCreateOrUpdate(resourceGroupName, serviceName, opid, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenIdConnectProvidersApi#openIdConnectProviderCreateOrUpdate");
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
| **opid** | **String**| Identifier of the OpenID Connect Provider. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**OpenidConnectProviderContract**](OpenidConnectProviderContract.md)| Create parameters. | |

### Return type

[**OpenidConnectProviderContract**](OpenidConnectProviderContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OpenIdConnect Provider was successfully updated. |  -  |
| **201** | OpenIdConnect Provider was successfully created. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="openIdConnectProviderDelete"></a>
# **openIdConnectProviderDelete**
> openIdConnectProviderDelete(resourceGroupName, serviceName, opid, ifMatch, apiVersion, subscriptionId)



Deletes specific OpenID Connect Provider of the API Management service instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenIdConnectProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OpenIdConnectProvidersApi apiInstance = new OpenIdConnectProvidersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String opid = "opid_example"; // String | Identifier of the OpenID Connect Provider.
    String ifMatch = "ifMatch_example"; // String | The entity state (Etag) version of the OpenID Connect Provider to delete. A value of \"*\" can be used for If-Match to unconditionally apply the operation.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.openIdConnectProviderDelete(resourceGroupName, serviceName, opid, ifMatch, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenIdConnectProvidersApi#openIdConnectProviderDelete");
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
| **opid** | **String**| Identifier of the OpenID Connect Provider. | |
| **ifMatch** | **String**| The entity state (Etag) version of the OpenID Connect Provider to delete. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation. | |
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
| **204** | OpenId Connect Provider was successfully deleted. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="openIdConnectProviderGet"></a>
# **openIdConnectProviderGet**
> OpenidConnectProviderContract openIdConnectProviderGet(resourceGroupName, serviceName, opid, apiVersion, subscriptionId)



Gets specific OpenID Connect Provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenIdConnectProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OpenIdConnectProvidersApi apiInstance = new OpenIdConnectProvidersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String opid = "opid_example"; // String | Identifier of the OpenID Connect Provider.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      OpenidConnectProviderContract result = apiInstance.openIdConnectProviderGet(resourceGroupName, serviceName, opid, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenIdConnectProvidersApi#openIdConnectProviderGet");
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
| **opid** | **String**| Identifier of the OpenID Connect Provider. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**OpenidConnectProviderContract**](OpenidConnectProviderContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body contains the specified OpenId Connect Provider entity. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="openIdConnectProviderGetEntityTag"></a>
# **openIdConnectProviderGetEntityTag**
> openIdConnectProviderGetEntityTag(resourceGroupName, serviceName, opid, apiVersion, subscriptionId)



Gets the entity state (Etag) version of the openIdConnectProvider specified by its identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenIdConnectProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OpenIdConnectProvidersApi apiInstance = new OpenIdConnectProvidersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String opid = "opid_example"; // String | Identifier of the OpenID Connect Provider.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.openIdConnectProviderGetEntityTag(resourceGroupName, serviceName, opid, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenIdConnectProvidersApi#openIdConnectProviderGetEntityTag");
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
| **opid** | **String**| Identifier of the OpenID Connect Provider. | |
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
| **200** | Specified openidConnectProvider entity exists and current entity state version is present in the ETag header. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="openIdConnectProviderListByService"></a>
# **openIdConnectProviderListByService**
> OpenIdConnectProviderCollection openIdConnectProviderListByService(resourceGroupName, serviceName, apiVersion, subscriptionId, $filter, $top, $skip)



Lists all OpenID Connect Providers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenIdConnectProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OpenIdConnectProvidersApi apiInstance = new OpenIdConnectProvidersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $filter = "$filter_example"; // String | | Field | Supported operators    | Supported functions                         | |-------|------------------------|---------------------------------------------| | id    | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name  | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith |
    Integer $top = 56; // Integer | Number of records to return.
    Integer $skip = 56; // Integer | Number of records to skip.
    try {
      OpenIdConnectProviderCollection result = apiInstance.openIdConnectProviderListByService(resourceGroupName, serviceName, apiVersion, subscriptionId, $filter, $top, $skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenIdConnectProvidersApi#openIdConnectProviderListByService");
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
| **$filter** | **String**| | Field | Supported operators    | Supported functions                         | |-------|------------------------|---------------------------------------------| | id    | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name  | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | [optional] |
| **$top** | **Integer**| Number of records to return. | [optional] |
| **$skip** | **Integer**| Number of records to skip. | [optional] |

### Return type

[**OpenIdConnectProviderCollection**](OpenIdConnectProviderCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lists of all the OpenId Connect Providers. |  -  |

<a id="openIdConnectProviderUpdate"></a>
# **openIdConnectProviderUpdate**
> openIdConnectProviderUpdate(resourceGroupName, serviceName, opid, ifMatch, apiVersion, subscriptionId, parameters)



Updates the specific OpenID Connect Provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenIdConnectProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OpenIdConnectProvidersApi apiInstance = new OpenIdConnectProvidersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String opid = "opid_example"; // String | Identifier of the OpenID Connect Provider.
    String ifMatch = "ifMatch_example"; // String | The entity state (Etag) version of the OpenID Connect Provider to update. A value of \"*\" can be used for If-Match to unconditionally apply the operation.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    OpenidConnectProviderUpdateContract parameters = new OpenidConnectProviderUpdateContract(); // OpenidConnectProviderUpdateContract | Update parameters.
    try {
      apiInstance.openIdConnectProviderUpdate(resourceGroupName, serviceName, opid, ifMatch, apiVersion, subscriptionId, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenIdConnectProvidersApi#openIdConnectProviderUpdate");
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
| **opid** | **String**| Identifier of the OpenID Connect Provider. | |
| **ifMatch** | **String**| The entity state (Etag) version of the OpenID Connect Provider to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**OpenidConnectProviderUpdateContract**](OpenidConnectProviderUpdateContract.md)| Update parameters. | |

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
| **204** | OpenId Connect Provider was successfully updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

