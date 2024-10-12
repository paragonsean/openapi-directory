# StreamingEndpointsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**streamingEndpointsCreate**](StreamingEndpointsApi.md#streamingEndpointsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/streamingEndpoints/{streamingEndpointName} | Create StreamingEndpoint |
| [**streamingEndpointsDelete**](StreamingEndpointsApi.md#streamingEndpointsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/streamingEndpoints/{streamingEndpointName} | Delete StreamingEndpoint |
| [**streamingEndpointsGet**](StreamingEndpointsApi.md#streamingEndpointsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/streamingEndpoints/{streamingEndpointName} | Get StreamingEndpoint |
| [**streamingEndpointsList**](StreamingEndpointsApi.md#streamingEndpointsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/streamingEndpoints | List StreamingEndpoints |
| [**streamingEndpointsScale**](StreamingEndpointsApi.md#streamingEndpointsScale) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/streamingEndpoints/{streamingEndpointName}/scale | Scale StreamingEndpoint |
| [**streamingEndpointsStart**](StreamingEndpointsApi.md#streamingEndpointsStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/streamingEndpoints/{streamingEndpointName}/start | Start StreamingEndpoint |
| [**streamingEndpointsStop**](StreamingEndpointsApi.md#streamingEndpointsStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/streamingEndpoints/{streamingEndpointName}/stop | Stop StreamingEndpoint |


<a id="streamingEndpointsCreate"></a>
# **streamingEndpointsCreate**
> StreamingEndpoint streamingEndpointsCreate(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion, parameters, autoStart)

Create StreamingEndpoint

Creates a StreamingEndpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamingEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    StreamingEndpointsApi apiInstance = new StreamingEndpointsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String streamingEndpointName = "streamingEndpointName_example"; // String | The name of the StreamingEndpoint.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    StreamingEndpoint parameters = new StreamingEndpoint(); // StreamingEndpoint | StreamingEndpoint properties needed for creation.
    Boolean autoStart = true; // Boolean | The flag indicates if auto start the Live Event.
    try {
      StreamingEndpoint result = apiInstance.streamingEndpointsCreate(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion, parameters, autoStart);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamingEndpointsApi#streamingEndpointsCreate");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **streamingEndpointName** | **String**| The name of the StreamingEndpoint. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **parameters** | [**StreamingEndpoint**](StreamingEndpoint.md)| StreamingEndpoint properties needed for creation. | |
| **autoStart** | **Boolean**| The flag indicates if auto start the Live Event. | [optional] |

### Return type

[**StreamingEndpoint**](StreamingEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted. The request has been accepted for processing and the operation will complete asynchronously. |  -  |
| **0** | The streaming error response describing why the operation failed. |  -  |

<a id="streamingEndpointsDelete"></a>
# **streamingEndpointsDelete**
> streamingEndpointsDelete(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion)

Delete StreamingEndpoint

Deletes a StreamingEndpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamingEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    StreamingEndpointsApi apiInstance = new StreamingEndpointsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String streamingEndpointName = "streamingEndpointName_example"; // String | The name of the StreamingEndpoint.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      apiInstance.streamingEndpointsDelete(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamingEndpointsApi#streamingEndpointsDelete");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **streamingEndpointName** | **String**| The name of the StreamingEndpoint. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

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
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted. The request has been accepted for processing and the operation will complete asynchronously. |  -  |
| **204** | No content. The request has been accepted but the Streaming Endpoint was not found. |  -  |
| **0** | The streaming error response describing why the operation failed. |  -  |

<a id="streamingEndpointsGet"></a>
# **streamingEndpointsGet**
> StreamingEndpoint streamingEndpointsGet(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion)

Get StreamingEndpoint

Gets a StreamingEndpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamingEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    StreamingEndpointsApi apiInstance = new StreamingEndpointsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String streamingEndpointName = "streamingEndpointName_example"; // String | The name of the StreamingEndpoint.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      StreamingEndpoint result = apiInstance.streamingEndpointsGet(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamingEndpointsApi#streamingEndpointsGet");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **streamingEndpointName** | **String**| The name of the StreamingEndpoint. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

[**StreamingEndpoint**](StreamingEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **404** | NotFound |  -  |
| **0** | The streaming error response describing why the operation failed. |  -  |

<a id="streamingEndpointsList"></a>
# **streamingEndpointsList**
> StreamingEndpointListResult streamingEndpointsList(subscriptionId, resourceGroupName, accountName, apiVersion)

List StreamingEndpoints

Lists the StreamingEndpoints in the account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamingEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    StreamingEndpointsApi apiInstance = new StreamingEndpointsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      StreamingEndpointListResult result = apiInstance.streamingEndpointsList(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamingEndpointsApi#streamingEndpointsList");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

[**StreamingEndpointListResult**](StreamingEndpointListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | The streaming error response describing why the operation failed. |  -  |

<a id="streamingEndpointsScale"></a>
# **streamingEndpointsScale**
> streamingEndpointsScale(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion, parameters)

Scale StreamingEndpoint

Scales an existing StreamingEndpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamingEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    StreamingEndpointsApi apiInstance = new StreamingEndpointsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String streamingEndpointName = "streamingEndpointName_example"; // String | The name of the StreamingEndpoint.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    StreamingEntityScaleUnit parameters = new StreamingEntityScaleUnit(); // StreamingEntityScaleUnit | StreamingEndpoint scale parameters
    try {
      apiInstance.streamingEndpointsScale(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamingEndpointsApi#streamingEndpointsScale");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **streamingEndpointName** | **String**| The name of the StreamingEndpoint. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **parameters** | [**StreamingEntityScaleUnit**](StreamingEntityScaleUnit.md)| StreamingEndpoint scale parameters | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted. The request has been accepted for processing and the operation will complete asynchronously. |  -  |
| **0** | The streaming error response describing why the operation failed. |  -  |

<a id="streamingEndpointsStart"></a>
# **streamingEndpointsStart**
> streamingEndpointsStart(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion)

Start StreamingEndpoint

Starts an existing StreamingEndpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamingEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    StreamingEndpointsApi apiInstance = new StreamingEndpointsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String streamingEndpointName = "streamingEndpointName_example"; // String | The name of the StreamingEndpoint.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      apiInstance.streamingEndpointsStart(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamingEndpointsApi#streamingEndpointsStart");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **streamingEndpointName** | **String**| The name of the StreamingEndpoint. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

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
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted. The request has been accepted for processing and the operation will complete asynchronously. |  -  |
| **0** | The streaming error response describing why the operation failed. |  -  |

<a id="streamingEndpointsStop"></a>
# **streamingEndpointsStop**
> streamingEndpointsStop(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion)

Stop StreamingEndpoint

Stops an existing StreamingEndpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamingEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    StreamingEndpointsApi apiInstance = new StreamingEndpointsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String streamingEndpointName = "streamingEndpointName_example"; // String | The name of the StreamingEndpoint.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      apiInstance.streamingEndpointsStop(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamingEndpointsApi#streamingEndpointsStop");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **streamingEndpointName** | **String**| The name of the StreamingEndpoint. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

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
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted. The request has been accepted for processing and the operation will complete asynchronously. |  -  |
| **0** | The streaming error response describing why the operation failed. |  -  |

