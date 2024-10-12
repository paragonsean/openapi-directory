# MeshGatewaysApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**meshGatewayCreateOrUpdate**](MeshGatewaysApi.md#meshGatewayCreateOrUpdate) | **PUT** /Resources/Gateways/{gatewayResourceName} | Creates or updates a Gateway resource. |
| [**meshGatewayDelete**](MeshGatewaysApi.md#meshGatewayDelete) | **DELETE** /Resources/Gateways/{gatewayResourceName} | Deletes the Gateway resource. |
| [**meshGatewayGet**](MeshGatewaysApi.md#meshGatewayGet) | **GET** /Resources/Gateways/{gatewayResourceName} | Gets the Gateway resource with the given name. |
| [**meshGatewayList**](MeshGatewaysApi.md#meshGatewayList) | **GET** /Resources/Gateways | Lists all the gateway resources. |


<a id="meshGatewayCreateOrUpdate"></a>
# **meshGatewayCreateOrUpdate**
> GatewayResourceDescription meshGatewayCreateOrUpdate(apiVersion, gatewayResourceName, gatewayResourceDescription)

Creates or updates a Gateway resource.

Creates a Gateway resource with the specified name, description and properties. If Gateway resource with the same name exists, then it is updated with the specified description and properties. Use Gateway resource to provide public connectivity to application services.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshGatewaysApi apiInstance = new MeshGatewaysApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String gatewayResourceName = "gatewayResourceName_example"; // String | The identity of the gateway.
    GatewayResourceDescription gatewayResourceDescription = new GatewayResourceDescription(); // GatewayResourceDescription | Description for creating a Gateway resource.
    try {
      GatewayResourceDescription result = apiInstance.meshGatewayCreateOrUpdate(apiVersion, gatewayResourceName, gatewayResourceDescription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshGatewaysApi#meshGatewayCreateOrUpdate");
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
| **gatewayResourceName** | **String**| The identity of the gateway. | |
| **gatewayResourceDescription** | [**GatewayResourceDescription**](GatewayResourceDescription.md)| Description for creating a Gateway resource. | |

### Return type

[**GatewayResourceDescription**](GatewayResourceDescription.md)

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

<a id="meshGatewayDelete"></a>
# **meshGatewayDelete**
> meshGatewayDelete(apiVersion, gatewayResourceName)

Deletes the Gateway resource.

Deletes the Gateway resource identified by the name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshGatewaysApi apiInstance = new MeshGatewaysApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String gatewayResourceName = "gatewayResourceName_example"; // String | The identity of the gateway.
    try {
      apiInstance.meshGatewayDelete(apiVersion, gatewayResourceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshGatewaysApi#meshGatewayDelete");
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
| **gatewayResourceName** | **String**| The identity of the gateway. | |

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
| **204** | No Content - the specified gateway was not found. |  -  |
| **0** | Error |  -  |

<a id="meshGatewayGet"></a>
# **meshGatewayGet**
> GatewayResourceDescription meshGatewayGet(apiVersion, gatewayResourceName)

Gets the Gateway resource with the given name.

Gets the information about the Gateway resource with the given name. The information include the description and other properties of the Gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshGatewaysApi apiInstance = new MeshGatewaysApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String gatewayResourceName = "gatewayResourceName_example"; // String | The identity of the gateway.
    try {
      GatewayResourceDescription result = apiInstance.meshGatewayGet(apiVersion, gatewayResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshGatewaysApi#meshGatewayGet");
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
| **gatewayResourceName** | **String**| The identity of the gateway. | |

### Return type

[**GatewayResourceDescription**](GatewayResourceDescription.md)

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

<a id="meshGatewayList"></a>
# **meshGatewayList**
> PagedGatewayResourceDescriptionList meshGatewayList(apiVersion)

Lists all the gateway resources.

Gets the information about all gateway resources in a given resource group. The information include the description and other properties of the Gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshGatewaysApi apiInstance = new MeshGatewaysApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    try {
      PagedGatewayResourceDescriptionList result = apiInstance.meshGatewayList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshGatewaysApi#meshGatewayList");
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

[**PagedGatewayResourceDescriptionList**](PagedGatewayResourceDescriptionList.md)

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

