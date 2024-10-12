# PublicIpPrefixesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**publicIPPrefixesCreateOrUpdate**](PublicIpPrefixesApi.md#publicIPPrefixesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPPrefixes/{publicIpPrefixName} |  |
| [**publicIPPrefixesDelete**](PublicIpPrefixesApi.md#publicIPPrefixesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPPrefixes/{publicIpPrefixName} |  |
| [**publicIPPrefixesGet**](PublicIpPrefixesApi.md#publicIPPrefixesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPPrefixes/{publicIpPrefixName} |  |
| [**publicIPPrefixesList**](PublicIpPrefixesApi.md#publicIPPrefixesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPPrefixes |  |
| [**publicIPPrefixesListAll**](PublicIpPrefixesApi.md#publicIPPrefixesListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/publicIPPrefixes |  |
| [**publicIPPrefixesUpdateTags**](PublicIpPrefixesApi.md#publicIPPrefixesUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPPrefixes/{publicIpPrefixName} |  |


<a id="publicIPPrefixesCreateOrUpdate"></a>
# **publicIPPrefixesCreateOrUpdate**
> PublicIPPrefix publicIPPrefixesCreateOrUpdate(resourceGroupName, publicIpPrefixName, apiVersion, subscriptionId, parameters)



Creates or updates a static or dynamic public IP prefix.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicIpPrefixesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PublicIpPrefixesApi apiInstance = new PublicIpPrefixesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String publicIpPrefixName = "publicIpPrefixName_example"; // String | The name of the public IP prefix.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    PublicIPPrefix parameters = new PublicIPPrefix(); // PublicIPPrefix | Parameters supplied to the create or update public IP prefix operation.
    try {
      PublicIPPrefix result = apiInstance.publicIPPrefixesCreateOrUpdate(resourceGroupName, publicIpPrefixName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicIpPrefixesApi#publicIPPrefixesCreateOrUpdate");
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
| **publicIpPrefixName** | **String**| The name of the public IP prefix. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**PublicIPPrefix**](PublicIPPrefix.md)| Parameters supplied to the create or update public IP prefix operation. | |

### Return type

[**PublicIPPrefix**](PublicIPPrefix.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting PublicIPPrefix resource. |  -  |
| **201** | Create successful. The operation returns the resulting PublicIPPrefix resource. |  -  |

<a id="publicIPPrefixesDelete"></a>
# **publicIPPrefixesDelete**
> publicIPPrefixesDelete(resourceGroupName, publicIpPrefixName, apiVersion, subscriptionId)



Deletes the specified public IP prefix.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicIpPrefixesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PublicIpPrefixesApi apiInstance = new PublicIpPrefixesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String publicIpPrefixName = "publicIpPrefixName_example"; // String | The name of the PublicIpPrefix.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.publicIPPrefixesDelete(resourceGroupName, publicIpPrefixName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicIpPrefixesApi#publicIPPrefixesDelete");
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
| **publicIpPrefixName** | **String**| The name of the PublicIpPrefix. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete successful. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **204** | Request successful. Resource does not exist. |  -  |

<a id="publicIPPrefixesGet"></a>
# **publicIPPrefixesGet**
> PublicIPPrefix publicIPPrefixesGet(resourceGroupName, publicIpPrefixName, apiVersion, subscriptionId, $expand)



Gets the specified public IP prefix in a specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicIpPrefixesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PublicIpPrefixesApi apiInstance = new PublicIpPrefixesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String publicIpPrefixName = "publicIpPrefixName_example"; // String | The name of the PublicIPPrefix.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $expand = "$expand_example"; // String | Expands referenced resources.
    try {
      PublicIPPrefix result = apiInstance.publicIPPrefixesGet(resourceGroupName, publicIpPrefixName, apiVersion, subscriptionId, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicIpPrefixesApi#publicIPPrefixesGet");
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
| **publicIpPrefixName** | **String**| The name of the PublicIPPrefix. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$expand** | **String**| Expands referenced resources. | [optional] |

### Return type

[**PublicIPPrefix**](PublicIPPrefix.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the resulting PublicIPPrefix resource. |  -  |

<a id="publicIPPrefixesList"></a>
# **publicIPPrefixesList**
> PublicIPPrefixListResult publicIPPrefixesList(resourceGroupName, apiVersion, subscriptionId)



Gets all public IP prefixes in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicIpPrefixesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PublicIpPrefixesApi apiInstance = new PublicIpPrefixesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      PublicIPPrefixListResult result = apiInstance.publicIPPrefixesList(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicIpPrefixesApi#publicIPPrefixesList");
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

[**PublicIPPrefixListResult**](PublicIPPrefixListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of PublicIPPrefix resources. |  -  |

<a id="publicIPPrefixesListAll"></a>
# **publicIPPrefixesListAll**
> PublicIPPrefixListResult publicIPPrefixesListAll(apiVersion, subscriptionId)



Gets all the public IP prefixes in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicIpPrefixesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PublicIpPrefixesApi apiInstance = new PublicIpPrefixesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      PublicIPPrefixListResult result = apiInstance.publicIPPrefixesListAll(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicIpPrefixesApi#publicIPPrefixesListAll");
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

[**PublicIPPrefixListResult**](PublicIPPrefixListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of PublicIPPrefix resources. |  -  |

<a id="publicIPPrefixesUpdateTags"></a>
# **publicIPPrefixesUpdateTags**
> PublicIPPrefix publicIPPrefixesUpdateTags(resourceGroupName, publicIpPrefixName, apiVersion, subscriptionId, parameters)



Updates public IP prefix tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicIpPrefixesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PublicIpPrefixesApi apiInstance = new PublicIpPrefixesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String publicIpPrefixName = "publicIpPrefixName_example"; // String | The name of the public IP prefix.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    PublicIPPrefixesUpdateTagsRequest parameters = new PublicIPPrefixesUpdateTagsRequest(); // PublicIPPrefixesUpdateTagsRequest | Parameters supplied to update public IP prefix tags.
    try {
      PublicIPPrefix result = apiInstance.publicIPPrefixesUpdateTags(resourceGroupName, publicIpPrefixName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicIpPrefixesApi#publicIPPrefixesUpdateTags");
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
| **publicIpPrefixName** | **String**| The name of the public IP prefix. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**PublicIPPrefixesUpdateTagsRequest**](PublicIPPrefixesUpdateTagsRequest.md)| Parameters supplied to update public IP prefix tags. | |

### Return type

[**PublicIPPrefix**](PublicIPPrefix.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting PublicIPPrefix resource. |  -  |

