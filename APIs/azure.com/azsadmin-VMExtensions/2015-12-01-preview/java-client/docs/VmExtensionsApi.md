# VmExtensionsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**vMExtensionsCreate**](VmExtensionsApi.md#vMExtensionsCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/artifactTypes/VMExtension/publishers/{publisher}/types/{type}/versions/{version} | Create a Virtual Machine Extension Image. |
| [**vMExtensionsDelete**](VmExtensionsApi.md#vMExtensionsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/artifactTypes/VMExtension/publishers/{publisher}/types/{type}/versions/{version} | Deletes a Virtual Machine Extension Image. |
| [**vMExtensionsGet**](VmExtensionsApi.md#vMExtensionsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/artifactTypes/VMExtension/publishers/{publisher}/types/{type}/versions/{version} | Returns requested Virtual Machine Extension Image. |
| [**vMExtensionsList**](VmExtensionsApi.md#vMExtensionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/artifactTypes/VMExtension | Returns a list of all Virtual Machine Extension Images. |


<a id="vMExtensionsCreate"></a>
# **vMExtensionsCreate**
> VMExtension vMExtensionsCreate(subscriptionId, location, publisher, type, version, apiVersion, extension)

Create a Virtual Machine Extension Image.

Create a Virtual Machine Extension Image with publisher, version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VmExtensionsApi apiInstance = new VmExtensionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | Location of the resource.
    String publisher = "publisher_example"; // String | Name of the publisher.
    String type = "type_example"; // String | Type of extension.
    String version = "version_example"; // String | The version of the resource.
    String apiVersion = "2015-12-01-preview"; // String | Client API Version.
    VMExtensionParameters extension = new VMExtensionParameters(); // VMExtensionParameters | Virtual Machine Extension Image creation properties.
    try {
      VMExtension result = apiInstance.vMExtensionsCreate(subscriptionId, location, publisher, type, version, apiVersion, extension);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmExtensionsApi#vMExtensionsCreate");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **location** | **String**| Location of the resource. | |
| **publisher** | **String**| Name of the publisher. | |
| **type** | **String**| Type of extension. | |
| **version** | **String**| The version of the resource. | |
| **apiVersion** | **String**| Client API Version. | [default to 2015-12-01-preview] |
| **extension** | [**VMExtensionParameters**](VMExtensionParameters.md)| Virtual Machine Extension Image creation properties. | |

### Return type

[**VMExtension**](VMExtension.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | OK |  -  |

<a id="vMExtensionsDelete"></a>
# **vMExtensionsDelete**
> vMExtensionsDelete(subscriptionId, location, publisher, type, version, apiVersion)

Deletes a Virtual Machine Extension Image.

Deletes specified Virtual Machine Extension Image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VmExtensionsApi apiInstance = new VmExtensionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | Location of the resource.
    String publisher = "publisher_example"; // String | Name of the publisher.
    String type = "type_example"; // String | Type of extension.
    String version = "version_example"; // String | The version of the resource.
    String apiVersion = "2015-12-01-preview"; // String | Client API Version.
    try {
      apiInstance.vMExtensionsDelete(subscriptionId, location, publisher, type, version, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmExtensionsApi#vMExtensionsDelete");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **location** | **String**| Location of the resource. | |
| **publisher** | **String**| Name of the publisher. | |
| **type** | **String**| Type of extension. | |
| **version** | **String**| The version of the resource. | |
| **apiVersion** | **String**| Client API Version. | [default to 2015-12-01-preview] |

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
| **200** | OK |  -  |

<a id="vMExtensionsGet"></a>
# **vMExtensionsGet**
> VMExtension vMExtensionsGet(subscriptionId, location, publisher, type, version, apiVersion)

Returns requested Virtual Machine Extension Image.

Returns requested Virtual Machine Extension Image matching publisher, type, version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VmExtensionsApi apiInstance = new VmExtensionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | Location of the resource.
    String publisher = "publisher_example"; // String | Name of the publisher.
    String type = "type_example"; // String | Type of extension.
    String version = "version_example"; // String | The version of the resource.
    String apiVersion = "2015-12-01-preview"; // String | Client API Version.
    try {
      VMExtension result = apiInstance.vMExtensionsGet(subscriptionId, location, publisher, type, version, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmExtensionsApi#vMExtensionsGet");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **location** | **String**| Location of the resource. | |
| **publisher** | **String**| Name of the publisher. | |
| **type** | **String**| Type of extension. | |
| **version** | **String**| The version of the resource. | |
| **apiVersion** | **String**| Client API Version. | [default to 2015-12-01-preview] |

### Return type

[**VMExtension**](VMExtension.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="vMExtensionsList"></a>
# **vMExtensionsList**
> List&lt;VMExtension&gt; vMExtensionsList(subscriptionId, location, apiVersion)

Returns a list of all Virtual Machine Extension Images.

List of all Virtual Machine Extension Images for the current location are returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VmExtensionsApi apiInstance = new VmExtensionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | Location of the resource.
    String apiVersion = "2015-12-01-preview"; // String | Client API Version.
    try {
      List<VMExtension> result = apiInstance.vMExtensionsList(subscriptionId, location, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmExtensionsApi#vMExtensionsList");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **location** | **String**| Location of the resource. | |
| **apiVersion** | **String**| Client API Version. | [default to 2015-12-01-preview] |

### Return type

[**List&lt;VMExtension&gt;**](VMExtension.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

