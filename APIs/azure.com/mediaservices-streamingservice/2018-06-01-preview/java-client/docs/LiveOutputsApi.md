# LiveOutputsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**liveOutputsCreate**](LiveOutputsApi.md#liveOutputsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName}/liveOutputs/{liveOutputName} | Create Live Output |
| [**liveOutputsDelete**](LiveOutputsApi.md#liveOutputsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName}/liveOutputs/{liveOutputName} | Delete Live Output |
| [**liveOutputsGet**](LiveOutputsApi.md#liveOutputsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName}/liveOutputs/{liveOutputName} | Get Live Output |
| [**liveOutputsList**](LiveOutputsApi.md#liveOutputsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName}/liveOutputs | List Live Outputs |


<a id="liveOutputsCreate"></a>
# **liveOutputsCreate**
> LiveOutput liveOutputsCreate(subscriptionId, resourceGroupName, accountName, liveEventName, liveOutputName, apiVersion, parameters)

Create Live Output

Creates a Live Output.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveOutputsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LiveOutputsApi apiInstance = new LiveOutputsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String liveEventName = "liveEventName_example"; // String | The name of the Live Event.
    String liveOutputName = "liveOutputName_example"; // String | The name of the Live Output.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    LiveOutput parameters = new LiveOutput(); // LiveOutput | Live Output properties needed for creation.
    try {
      LiveOutput result = apiInstance.liveOutputsCreate(subscriptionId, resourceGroupName, accountName, liveEventName, liveOutputName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveOutputsApi#liveOutputsCreate");
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
| **liveEventName** | **String**| The name of the Live Event. | |
| **liveOutputName** | **String**| The name of the Live Output. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **parameters** | [**LiveOutput**](LiveOutput.md)| Live Output properties needed for creation. | |

### Return type

[**LiveOutput**](LiveOutput.md)

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

<a id="liveOutputsDelete"></a>
# **liveOutputsDelete**
> liveOutputsDelete(subscriptionId, resourceGroupName, accountName, liveEventName, liveOutputName, apiVersion)

Delete Live Output

Deletes a Live Output.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveOutputsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LiveOutputsApi apiInstance = new LiveOutputsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String liveEventName = "liveEventName_example"; // String | The name of the Live Event.
    String liveOutputName = "liveOutputName_example"; // String | The name of the Live Output.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      apiInstance.liveOutputsDelete(subscriptionId, resourceGroupName, accountName, liveEventName, liveOutputName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveOutputsApi#liveOutputsDelete");
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
| **liveEventName** | **String**| The name of the Live Event. | |
| **liveOutputName** | **String**| The name of the Live Output. | |
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
| **204** | No content. The request has been accepted but the Live Output was not found. |  -  |
| **0** | The streaming error response describing why the operation failed. |  -  |

<a id="liveOutputsGet"></a>
# **liveOutputsGet**
> LiveOutput liveOutputsGet(subscriptionId, resourceGroupName, accountName, liveEventName, liveOutputName, apiVersion)

Get Live Output

Gets a Live Output.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveOutputsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LiveOutputsApi apiInstance = new LiveOutputsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String liveEventName = "liveEventName_example"; // String | The name of the Live Event.
    String liveOutputName = "liveOutputName_example"; // String | The name of the Live Output.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      LiveOutput result = apiInstance.liveOutputsGet(subscriptionId, resourceGroupName, accountName, liveEventName, liveOutputName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveOutputsApi#liveOutputsGet");
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
| **liveEventName** | **String**| The name of the Live Event. | |
| **liveOutputName** | **String**| The name of the Live Output. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

[**LiveOutput**](LiveOutput.md)

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

<a id="liveOutputsList"></a>
# **liveOutputsList**
> LiveOutputListResult liveOutputsList(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion)

List Live Outputs

Lists the Live Outputs in the Live Event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveOutputsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LiveOutputsApi apiInstance = new LiveOutputsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String liveEventName = "liveEventName_example"; // String | The name of the Live Event.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      LiveOutputListResult result = apiInstance.liveOutputsList(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveOutputsApi#liveOutputsList");
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
| **liveEventName** | **String**| The name of the Live Event. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

[**LiveOutputListResult**](LiveOutputListResult.md)

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

