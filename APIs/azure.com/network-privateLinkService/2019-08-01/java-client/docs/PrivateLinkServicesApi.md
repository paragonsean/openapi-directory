# PrivateLinkServicesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**privateLinkServicesCheckPrivateLinkServiceVisibility**](PrivateLinkServicesApi.md#privateLinkServicesCheckPrivateLinkServiceVisibility) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Network/locations/{location}/checkPrivateLinkServiceVisibility |  |
| [**privateLinkServicesCheckPrivateLinkServiceVisibilityByResourceGroup**](PrivateLinkServicesApi.md#privateLinkServicesCheckPrivateLinkServiceVisibilityByResourceGroup) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/locations/{location}/checkPrivateLinkServiceVisibility |  |
| [**privateLinkServicesDelete**](PrivateLinkServicesApi.md#privateLinkServicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateLinkServices/{serviceName} |  |
| [**privateLinkServicesDeletePrivateEndpointConnection**](PrivateLinkServicesApi.md#privateLinkServicesDeletePrivateEndpointConnection) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateLinkServices/{serviceName}/privateEndpointConnections/{peConnectionName} |  |
| [**privateLinkServicesGet**](PrivateLinkServicesApi.md#privateLinkServicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateLinkServices/{serviceName} |  |
| [**privateLinkServicesList**](PrivateLinkServicesApi.md#privateLinkServicesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateLinkServices |  |
| [**privateLinkServicesListAutoApprovedPrivateLinkServices**](PrivateLinkServicesApi.md#privateLinkServicesListAutoApprovedPrivateLinkServices) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/locations/{location}/autoApprovedPrivateLinkServices |  |
| [**privateLinkServicesListAutoApprovedPrivateLinkServicesByResourceGroup**](PrivateLinkServicesApi.md#privateLinkServicesListAutoApprovedPrivateLinkServicesByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/locations/{location}/autoApprovedPrivateLinkServices |  |
| [**privateLinkServicesListBySubscription**](PrivateLinkServicesApi.md#privateLinkServicesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/privateLinkServices |  |
| [**privateLinkServicesUpdatePrivateEndpointConnection**](PrivateLinkServicesApi.md#privateLinkServicesUpdatePrivateEndpointConnection) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateLinkServices/{serviceName}/privateEndpointConnections/{peConnectionName} |  |


<a id="privateLinkServicesCheckPrivateLinkServiceVisibility"></a>
# **privateLinkServicesCheckPrivateLinkServiceVisibility**
> PrivateLinkServiceVisibility privateLinkServicesCheckPrivateLinkServiceVisibility(location, apiVersion, subscriptionId, parameters)



Checks whether the subscription is visible to private link service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateLinkServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateLinkServicesApi apiInstance = new PrivateLinkServicesApi(defaultClient);
    String location = "location_example"; // String | The location of the domain name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    CheckPrivateLinkServiceVisibilityRequest parameters = new CheckPrivateLinkServiceVisibilityRequest(); // CheckPrivateLinkServiceVisibilityRequest | The request body of CheckPrivateLinkService API call.
    try {
      PrivateLinkServiceVisibility result = apiInstance.privateLinkServicesCheckPrivateLinkServiceVisibility(location, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateLinkServicesApi#privateLinkServicesCheckPrivateLinkServiceVisibility");
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
| **location** | **String**| The location of the domain name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**CheckPrivateLinkServiceVisibilityRequest**](CheckPrivateLinkServiceVisibilityRequest.md)| The request body of CheckPrivateLinkService API call. | |

### Return type

[**PrivateLinkServiceVisibility**](PrivateLinkServiceVisibility.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns whether the subscription is visible to private link service. |  -  |

<a id="privateLinkServicesCheckPrivateLinkServiceVisibilityByResourceGroup"></a>
# **privateLinkServicesCheckPrivateLinkServiceVisibilityByResourceGroup**
> PrivateLinkServiceVisibility privateLinkServicesCheckPrivateLinkServiceVisibilityByResourceGroup(location, resourceGroupName, apiVersion, subscriptionId, parameters)



Checks whether the subscription is visible to private link service in the specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateLinkServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateLinkServicesApi apiInstance = new PrivateLinkServicesApi(defaultClient);
    String location = "location_example"; // String | The location of the domain name.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    CheckPrivateLinkServiceVisibilityRequest parameters = new CheckPrivateLinkServiceVisibilityRequest(); // CheckPrivateLinkServiceVisibilityRequest | The request body of CheckPrivateLinkService API call.
    try {
      PrivateLinkServiceVisibility result = apiInstance.privateLinkServicesCheckPrivateLinkServiceVisibilityByResourceGroup(location, resourceGroupName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateLinkServicesApi#privateLinkServicesCheckPrivateLinkServiceVisibilityByResourceGroup");
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
| **location** | **String**| The location of the domain name. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**CheckPrivateLinkServiceVisibilityRequest**](CheckPrivateLinkServiceVisibilityRequest.md)| The request body of CheckPrivateLinkService API call. | |

### Return type

[**PrivateLinkServiceVisibility**](PrivateLinkServiceVisibility.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns whether the subscription is visible to private link service. |  -  |

<a id="privateLinkServicesDelete"></a>
# **privateLinkServicesDelete**
> privateLinkServicesDelete(resourceGroupName, serviceName, apiVersion, subscriptionId)



Deletes the specified private link service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateLinkServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateLinkServicesApi apiInstance = new PrivateLinkServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the private link service.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.privateLinkServicesDelete(resourceGroupName, serviceName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateLinkServicesApi#privateLinkServicesDelete");
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
| **serviceName** | **String**| The name of the private link service. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | Delete successful. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **204** | Delete successful. |  -  |
| **0** | Error. |  -  |

<a id="privateLinkServicesDeletePrivateEndpointConnection"></a>
# **privateLinkServicesDeletePrivateEndpointConnection**
> privateLinkServicesDeletePrivateEndpointConnection(resourceGroupName, serviceName, peConnectionName, apiVersion, subscriptionId)



Delete private end point connection for a private link service in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateLinkServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateLinkServicesApi apiInstance = new PrivateLinkServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the private link service.
    String peConnectionName = "peConnectionName_example"; // String | The name of the private end point connection.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.privateLinkServicesDeletePrivateEndpointConnection(resourceGroupName, serviceName, peConnectionName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateLinkServicesApi#privateLinkServicesDeletePrivateEndpointConnection");
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
| **serviceName** | **String**| The name of the private link service. | |
| **peConnectionName** | **String**| The name of the private end point connection. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | Delete successful. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **204** | Delete successful. |  -  |
| **0** | Error. |  -  |

<a id="privateLinkServicesGet"></a>
# **privateLinkServicesGet**
> PrivateLinkService privateLinkServicesGet(resourceGroupName, serviceName, apiVersion, subscriptionId, $expand)



Gets the specified private link service by resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateLinkServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateLinkServicesApi apiInstance = new PrivateLinkServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the private link service.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $expand = "$expand_example"; // String | Expands referenced resources.
    try {
      PrivateLinkService result = apiInstance.privateLinkServicesGet(resourceGroupName, serviceName, apiVersion, subscriptionId, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateLinkServicesApi#privateLinkServicesGet");
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
| **serviceName** | **String**| The name of the private link service. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$expand** | **String**| Expands referenced resources. | [optional] |

### Return type

[**PrivateLinkService**](PrivateLinkService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the resulting PrivateLinkService resource. |  -  |
| **0** | Error. |  -  |

<a id="privateLinkServicesList"></a>
# **privateLinkServicesList**
> PrivateLinkServiceListResult privateLinkServicesList(resourceGroupName, apiVersion, subscriptionId)



Gets all private link services in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateLinkServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateLinkServicesApi apiInstance = new PrivateLinkServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      PrivateLinkServiceListResult result = apiInstance.privateLinkServicesList(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateLinkServicesApi#privateLinkServicesList");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**PrivateLinkServiceListResult**](PrivateLinkServiceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of privateLinkService resources. |  -  |
| **0** | Error. |  -  |

<a id="privateLinkServicesListAutoApprovedPrivateLinkServices"></a>
# **privateLinkServicesListAutoApprovedPrivateLinkServices**
> AutoApprovedPrivateLinkServicesResult privateLinkServicesListAutoApprovedPrivateLinkServices(location, apiVersion, subscriptionId)



Returns all of the private link service ids that can be linked to a Private Endpoint with auto approved in this subscription in this region.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateLinkServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateLinkServicesApi apiInstance = new PrivateLinkServicesApi(defaultClient);
    String location = "location_example"; // String | The location of the domain name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      AutoApprovedPrivateLinkServicesResult result = apiInstance.privateLinkServicesListAutoApprovedPrivateLinkServices(location, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateLinkServicesApi#privateLinkServicesListAutoApprovedPrivateLinkServices");
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
| **location** | **String**| The location of the domain name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**AutoApprovedPrivateLinkServicesResult**](AutoApprovedPrivateLinkServicesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns all of the private link service ids that can be linked to a Private Endpoint with auto approved in this subscription in this region. |  -  |

<a id="privateLinkServicesListAutoApprovedPrivateLinkServicesByResourceGroup"></a>
# **privateLinkServicesListAutoApprovedPrivateLinkServicesByResourceGroup**
> AutoApprovedPrivateLinkServicesResult privateLinkServicesListAutoApprovedPrivateLinkServicesByResourceGroup(location, resourceGroupName, apiVersion, subscriptionId)



Returns all of the private link service ids that can be linked to a Private Endpoint with auto approved in this subscription in this region.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateLinkServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateLinkServicesApi apiInstance = new PrivateLinkServicesApi(defaultClient);
    String location = "location_example"; // String | The location of the domain name.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      AutoApprovedPrivateLinkServicesResult result = apiInstance.privateLinkServicesListAutoApprovedPrivateLinkServicesByResourceGroup(location, resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateLinkServicesApi#privateLinkServicesListAutoApprovedPrivateLinkServicesByResourceGroup");
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
| **location** | **String**| The location of the domain name. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**AutoApprovedPrivateLinkServicesResult**](AutoApprovedPrivateLinkServicesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns all of the private link service ids that can be linked to a Private Endpoint with auto approved in this subscription in this region. |  -  |

<a id="privateLinkServicesListBySubscription"></a>
# **privateLinkServicesListBySubscription**
> PrivateLinkServiceListResult privateLinkServicesListBySubscription(apiVersion, subscriptionId)



Gets all private link service in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateLinkServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateLinkServicesApi apiInstance = new PrivateLinkServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      PrivateLinkServiceListResult result = apiInstance.privateLinkServicesListBySubscription(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateLinkServicesApi#privateLinkServicesListBySubscription");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**PrivateLinkServiceListResult**](PrivateLinkServiceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of PrivateLinkService resources. |  -  |
| **0** | Error. |  -  |

<a id="privateLinkServicesUpdatePrivateEndpointConnection"></a>
# **privateLinkServicesUpdatePrivateEndpointConnection**
> PrivateEndpointConnection privateLinkServicesUpdatePrivateEndpointConnection(resourceGroupName, serviceName, peConnectionName, apiVersion, subscriptionId, parameters)



Approve or reject private end point connection for a private link service in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateLinkServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateLinkServicesApi apiInstance = new PrivateLinkServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the private link service.
    String peConnectionName = "peConnectionName_example"; // String | The name of the private end point connection.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    PrivateEndpointConnection parameters = new PrivateEndpointConnection(); // PrivateEndpointConnection | Parameters supplied to approve or reject the private end point connection.
    try {
      PrivateEndpointConnection result = apiInstance.privateLinkServicesUpdatePrivateEndpointConnection(resourceGroupName, serviceName, peConnectionName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateLinkServicesApi#privateLinkServicesUpdatePrivateEndpointConnection");
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
| **serviceName** | **String**| The name of the private link service. | |
| **peConnectionName** | **String**| The name of the private end point connection. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**PrivateEndpointConnection**](PrivateEndpointConnection.md)| Parameters supplied to approve or reject the private end point connection. | |

### Return type

[**PrivateEndpointConnection**](PrivateEndpointConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting PrivateEndpointConnection resource. |  -  |
| **0** | Error. |  -  |

