# LiveEventsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**liveEventsCreate**](LiveEventsApi.md#liveEventsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName} | Create Live Event |
| [**liveEventsDelete**](LiveEventsApi.md#liveEventsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName} | Delete Live Event |
| [**liveEventsGet**](LiveEventsApi.md#liveEventsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName} | Get Live Event |
| [**liveEventsList**](LiveEventsApi.md#liveEventsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents | List Live Events |
| [**liveEventsReset**](LiveEventsApi.md#liveEventsReset) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName}/reset | Reset Live Event |
| [**liveEventsStart**](LiveEventsApi.md#liveEventsStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName}/start | Start Live Event |
| [**liveEventsStop**](LiveEventsApi.md#liveEventsStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName}/stop | Stop Live Event |
| [**liveEventsUpdate**](LiveEventsApi.md#liveEventsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName} |  |


<a id="liveEventsCreate"></a>
# **liveEventsCreate**
> LiveEvent liveEventsCreate(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion, parameters, autoStart)

Create Live Event

Creates a Live Event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveEventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LiveEventsApi apiInstance = new LiveEventsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String liveEventName = "liveEventName_example"; // String | The name of the Live Event.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    LiveEvent parameters = new LiveEvent(); // LiveEvent | Live Event properties needed for creation.
    Boolean autoStart = true; // Boolean | The flag indicates if auto start the Live Event.
    try {
      LiveEvent result = apiInstance.liveEventsCreate(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion, parameters, autoStart);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveEventsApi#liveEventsCreate");
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
| **parameters** | [**LiveEvent**](LiveEvent.md)| Live Event properties needed for creation. | |
| **autoStart** | **Boolean**| The flag indicates if auto start the Live Event. | [optional] |

### Return type

[**LiveEvent**](LiveEvent.md)

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

<a id="liveEventsDelete"></a>
# **liveEventsDelete**
> liveEventsDelete(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion)

Delete Live Event

Deletes a Live Event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveEventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LiveEventsApi apiInstance = new LiveEventsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String liveEventName = "liveEventName_example"; // String | The name of the Live Event.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      apiInstance.liveEventsDelete(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveEventsApi#liveEventsDelete");
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
| **204** | No content. The request has been accepted but the Live Event was not found. |  -  |
| **0** | The streaming error response describing why the operation failed. |  -  |

<a id="liveEventsGet"></a>
# **liveEventsGet**
> LiveEvent liveEventsGet(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion)

Get Live Event

Gets a Live Event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveEventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LiveEventsApi apiInstance = new LiveEventsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String liveEventName = "liveEventName_example"; // String | The name of the Live Event.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      LiveEvent result = apiInstance.liveEventsGet(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveEventsApi#liveEventsGet");
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

[**LiveEvent**](LiveEvent.md)

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

<a id="liveEventsList"></a>
# **liveEventsList**
> LiveEventListResult liveEventsList(subscriptionId, resourceGroupName, accountName, apiVersion)

List Live Events

Lists the Live Events in the account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveEventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LiveEventsApi apiInstance = new LiveEventsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      LiveEventListResult result = apiInstance.liveEventsList(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveEventsApi#liveEventsList");
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

[**LiveEventListResult**](LiveEventListResult.md)

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

<a id="liveEventsReset"></a>
# **liveEventsReset**
> liveEventsReset(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion)

Reset Live Event

Resets an existing Live Event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveEventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LiveEventsApi apiInstance = new LiveEventsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String liveEventName = "liveEventName_example"; // String | The name of the Live Event.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      apiInstance.liveEventsReset(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveEventsApi#liveEventsReset");
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

<a id="liveEventsStart"></a>
# **liveEventsStart**
> liveEventsStart(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion)

Start Live Event

Starts an existing Live Event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveEventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LiveEventsApi apiInstance = new LiveEventsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String liveEventName = "liveEventName_example"; // String | The name of the Live Event.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      apiInstance.liveEventsStart(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveEventsApi#liveEventsStart");
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

<a id="liveEventsStop"></a>
# **liveEventsStop**
> liveEventsStop(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion, parameters)

Stop Live Event

Stops an existing Live Event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveEventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LiveEventsApi apiInstance = new LiveEventsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String liveEventName = "liveEventName_example"; // String | The name of the Live Event.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    LiveEventActionInput parameters = new LiveEventActionInput(); // LiveEventActionInput | LiveEvent stop parameters
    try {
      apiInstance.liveEventsStop(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveEventsApi#liveEventsStop");
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
| **parameters** | [**LiveEventActionInput**](LiveEventActionInput.md)| LiveEvent stop parameters | |

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

<a id="liveEventsUpdate"></a>
# **liveEventsUpdate**
> LiveEvent liveEventsUpdate(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion, parameters)



Updates a existing Live Event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveEventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LiveEventsApi apiInstance = new LiveEventsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String liveEventName = "liveEventName_example"; // String | The name of the Live Event.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    LiveEvent parameters = new LiveEvent(); // LiveEvent | Live Event properties needed for creation.
    try {
      LiveEvent result = apiInstance.liveEventsUpdate(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveEventsApi#liveEventsUpdate");
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
| **parameters** | [**LiveEvent**](LiveEvent.md)| Live Event properties needed for creation. | |

### Return type

[**LiveEvent**](LiveEvent.md)

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

