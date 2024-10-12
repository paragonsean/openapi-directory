# MeshNetworksApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**meshNetworkCreateOrUpdate**](MeshNetworksApi.md#meshNetworkCreateOrUpdate) | **PUT** /Resources/Networks/{networkResourceName} | Creates or updates a Network resource. |
| [**meshNetworkDelete**](MeshNetworksApi.md#meshNetworkDelete) | **DELETE** /Resources/Networks/{networkResourceName} | Deletes the Network resource. |
| [**meshNetworkGet**](MeshNetworksApi.md#meshNetworkGet) | **GET** /Resources/Networks/{networkResourceName} | Gets the Network resource with the given name. |
| [**meshNetworkList**](MeshNetworksApi.md#meshNetworkList) | **GET** /Resources/Networks | Lists all the network resources. |


<a id="meshNetworkCreateOrUpdate"></a>
# **meshNetworkCreateOrUpdate**
> NetworkResourceDescription meshNetworkCreateOrUpdate(apiVersion, networkResourceName, networkResourceDescription)

Creates or updates a Network resource.

Creates a Network resource with the specified name, description and properties. If Network resource with the same name exists, then it is updated with the specified description and properties. Network resource provides connectivity between application services.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshNetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshNetworksApi apiInstance = new MeshNetworksApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String networkResourceName = "networkResourceName_example"; // String | The identity of the network.
    NetworkResourceDescription networkResourceDescription = new NetworkResourceDescription(); // NetworkResourceDescription | Description for creating a Network resource.
    try {
      NetworkResourceDescription result = apiInstance.meshNetworkCreateOrUpdate(apiVersion, networkResourceName, networkResourceDescription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshNetworksApi#meshNetworkCreateOrUpdate");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to 6.4-preview] [enum: 6.4-preview] |
| **networkResourceName** | **String**| The identity of the network. | |
| **networkResourceDescription** | [**NetworkResourceDescription**](NetworkResourceDescription.md)| Description for creating a Network resource. | |

### Return type

[**NetworkResourceDescription**](NetworkResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **202** | Accepted |  -  |
| **0** | Error |  -  |

<a id="meshNetworkDelete"></a>
# **meshNetworkDelete**
> meshNetworkDelete(apiVersion, networkResourceName)

Deletes the Network resource.

Deletes the Network resource identified by the name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshNetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshNetworksApi apiInstance = new MeshNetworksApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String networkResourceName = "networkResourceName_example"; // String | The identity of the network.
    try {
      apiInstance.meshNetworkDelete(apiVersion, networkResourceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshNetworksApi#meshNetworkDelete");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to 6.4-preview] [enum: 6.4-preview] |
| **networkResourceName** | **String**| The identity of the network. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **204** | No Content - the specified network was not found. |  -  |
| **0** | Error |  -  |

<a id="meshNetworkGet"></a>
# **meshNetworkGet**
> NetworkResourceDescription meshNetworkGet(apiVersion, networkResourceName)

Gets the Network resource with the given name.

Gets the information about the Network resource with the given name. The information include the description and other properties of the Network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshNetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshNetworksApi apiInstance = new MeshNetworksApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String networkResourceName = "networkResourceName_example"; // String | The identity of the network.
    try {
      NetworkResourceDescription result = apiInstance.meshNetworkGet(apiVersion, networkResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshNetworksApi#meshNetworkGet");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to 6.4-preview] [enum: 6.4-preview] |
| **networkResourceName** | **String**| The identity of the network. | |

### Return type

[**NetworkResourceDescription**](NetworkResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

<a id="meshNetworkList"></a>
# **meshNetworkList**
> PagedNetworkResourceDescriptionList meshNetworkList(apiVersion)

Lists all the network resources.

Gets the information about all network resources in a given resource group. The information include the description and other properties of the Network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshNetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshNetworksApi apiInstance = new MeshNetworksApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    try {
      PagedNetworkResourceDescriptionList result = apiInstance.meshNetworkList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshNetworksApi#meshNetworkList");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to 6.4-preview] [enum: 6.4-preview] |

### Return type

[**PagedNetworkResourceDescriptionList**](PagedNetworkResourceDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

