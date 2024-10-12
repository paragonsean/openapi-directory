# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mediaGraphsCreateOrUpdate**](DefaultApi.md#mediaGraphsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/mediaGraphs/{mediaGraphName} | Create or update a Media Graph |
| [**mediaGraphsDelete**](DefaultApi.md#mediaGraphsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/mediaGraphs/{mediaGraphName} | Delete a Media Graph |
| [**mediaGraphsGet**](DefaultApi.md#mediaGraphsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/mediaGraphs/{mediaGraphName} | Get a Media Graph |
| [**mediaGraphsList**](DefaultApi.md#mediaGraphsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/mediaGraphs | List Media Graphs |
| [**mediaGraphsStart**](DefaultApi.md#mediaGraphsStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/mediaGraphs/{mediaGraphName}/start | Start a Media Graph |
| [**mediaGraphsStop**](DefaultApi.md#mediaGraphsStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/mediaGraphs/{mediaGraphName}/stop | Stop a Media Graph |
| [**operationResultsGet**](DefaultApi.md#operationResultsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/mediaGraphs/{mediaGraphName}/operationResults/{operationId} | Get the operation result |
| [**operationsStatusGet**](DefaultApi.md#operationsStatusGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/mediaGraphs/{mediaGraphName}/operationsStatus/{operationId} | Get the operation status |


<a id="mediaGraphsCreateOrUpdate"></a>
# **mediaGraphsCreateOrUpdate**
> MediaGraph mediaGraphsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, mediaGraphName, apiVersion, parameters)

Create or update a Media Graph

Create or update a Media Graph in the Media Services account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String mediaGraphName = "mediaGraphName_example"; // String | The Media Graph name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    MediaGraph parameters = new MediaGraph(); // MediaGraph | The request parameters
    try {
      MediaGraph result = apiInstance.mediaGraphsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, mediaGraphName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mediaGraphsCreateOrUpdate");
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
| **mediaGraphName** | **String**| The Media Graph name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **parameters** | [**MediaGraph**](MediaGraph.md)| The request parameters | |

### Return type

[**MediaGraph**](MediaGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

<a id="mediaGraphsDelete"></a>
# **mediaGraphsDelete**
> mediaGraphsDelete(subscriptionId, resourceGroupName, accountName, mediaGraphName, apiVersion)

Delete a Media Graph

Deletes a Media Graph in the Media Services account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String mediaGraphName = "mediaGraphName_example"; // String | The Media Graph name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      apiInstance.mediaGraphsDelete(subscriptionId, resourceGroupName, accountName, mediaGraphName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mediaGraphsDelete");
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
| **mediaGraphName** | **String**| The Media Graph name. | |
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
| **200** | OK |  -  |
| **204** | NoContent |  -  |
| **0** | Detailed error information. |  -  |

<a id="mediaGraphsGet"></a>
# **mediaGraphsGet**
> MediaGraph mediaGraphsGet(subscriptionId, resourceGroupName, accountName, mediaGraphName, apiVersion)

Get a Media Graph

Get the details of a Media Graph in the Media Services account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String mediaGraphName = "mediaGraphName_example"; // String | The Media Graph name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      MediaGraph result = apiInstance.mediaGraphsGet(subscriptionId, resourceGroupName, accountName, mediaGraphName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mediaGraphsGet");
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
| **mediaGraphName** | **String**| The Media Graph name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

[**MediaGraph**](MediaGraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NotFound |  -  |
| **0** | Detailed error information. |  -  |

<a id="mediaGraphsList"></a>
# **mediaGraphsList**
> MediaGraphCollection mediaGraphsList(subscriptionId, resourceGroupName, accountName, apiVersion, $top)

List Media Graphs

Lists Media Graphs in the Media Services account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    Integer $top = 56; // Integer | Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.
    try {
      MediaGraphCollection result = apiInstance.mediaGraphsList(subscriptionId, resourceGroupName, accountName, apiVersion, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mediaGraphsList");
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
| **$top** | **Integer**| Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n. | [optional] |

### Return type

[**MediaGraphCollection**](MediaGraphCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

<a id="mediaGraphsStart"></a>
# **mediaGraphsStart**
> mediaGraphsStart(subscriptionId, resourceGroupName, accountName, mediaGraphName, apiVersion)

Start a Media Graph

Start a Media Graph in the Media Services account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String mediaGraphName = "mediaGraphName_example"; // String | The Media Graph name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      apiInstance.mediaGraphsStart(subscriptionId, resourceGroupName, accountName, mediaGraphName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mediaGraphsStart");
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
| **mediaGraphName** | **String**| The Media Graph name. | |
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
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **0** | Detailed error information. |  -  |

<a id="mediaGraphsStop"></a>
# **mediaGraphsStop**
> mediaGraphsStop(subscriptionId, resourceGroupName, accountName, mediaGraphName, apiVersion)

Stop a Media Graph

Stop a Media Graph in the Media Services account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String mediaGraphName = "mediaGraphName_example"; // String | The Media Graph name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      apiInstance.mediaGraphsStop(subscriptionId, resourceGroupName, accountName, mediaGraphName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mediaGraphsStop");
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
| **mediaGraphName** | **String**| The Media Graph name. | |
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
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **0** | Detailed error information. |  -  |

<a id="operationResultsGet"></a>
# **operationResultsGet**
> Object operationResultsGet(subscriptionId, resourceGroupName, accountName, mediaGraphName, operationId, apiVersion)

Get the operation result

Get the operation result of a Media Graph in the Media Services account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String mediaGraphName = "mediaGraphName_example"; // String | The Media Graph name.
    String operationId = "operationId_example"; // String | The operation ID
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      Object result = apiInstance.operationResultsGet(subscriptionId, resourceGroupName, accountName, mediaGraphName, operationId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#operationResultsGet");
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
| **mediaGraphName** | **String**| The Media Graph name. | |
| **operationId** | **String**| The operation ID | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

<a id="operationsStatusGet"></a>
# **operationsStatusGet**
> MediaGraphOperationStatus operationsStatusGet(subscriptionId, resourceGroupName, accountName, mediaGraphName, operationId, apiVersion)

Get the operation status

Get the operation status of a Media Graph in the media services account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String mediaGraphName = "mediaGraphName_example"; // String | The Media Graph name.
    String operationId = "operationId_example"; // String | The operation ID
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      MediaGraphOperationStatus result = apiInstance.operationsStatusGet(subscriptionId, resourceGroupName, accountName, mediaGraphName, operationId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#operationsStatusGet");
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
| **mediaGraphName** | **String**| The Media Graph name. | |
| **operationId** | **String**| The operation ID | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

[**MediaGraphOperationStatus**](MediaGraphOperationStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

