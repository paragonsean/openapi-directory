# ChannelApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**channelsCreate**](ChannelApi.md#channelsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/channels/{channelName} |  |
| [**channelsDelete**](ChannelApi.md#channelsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/channels/{channelName} |  |
| [**channelsGet**](ChannelApi.md#channelsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/channels/{channelName} |  |
| [**channelsListByResourceGroup**](ChannelApi.md#channelsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/channels |  |
| [**channelsListWithKeys**](ChannelApi.md#channelsListWithKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/channels/{channelName}/listChannelWithKeys |  |
| [**channelsUpdate**](ChannelApi.md#channelsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/channels/{channelName} |  |


<a id="channelsCreate"></a>
# **channelsCreate**
> BotChannel channelsCreate(resourceGroupName, resourceName, channelName, apiVersion, subscriptionId, parameters)



Creates a Channel registration for a Bot Service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ChannelApi apiInstance = new ChannelApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String resourceName = "resourceName_example"; // String | The name of the Bot resource.
    String channelName = "FacebookChannel"; // String | The name of the Channel resource.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    BotChannel parameters = new BotChannel(); // BotChannel | The parameters to provide for the created bot.
    try {
      BotChannel result = apiInstance.channelsCreate(resourceGroupName, resourceName, channelName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelApi#channelsCreate");
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
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **resourceName** | **String**| The name of the Bot resource. | |
| **channelName** | **String**| The name of the Channel resource. | [enum: FacebookChannel, EmailChannel, KikChannel, TelegramChannel, SlackChannel, MsTeamsChannel, SkypeChannel, WebChatChannel, DirectLineChannel, SmsChannel] |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **parameters** | [**BotChannel**](BotChannel.md)| The parameters to provide for the created bot. | |

### Return type

[**BotChannel**](BotChannel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If resource is created successfully or already existed, the service should return 200 (OK). |  -  |
| **201** | If resource is created successfully, the service should return 201 (Created). Execution to continue asynchronously. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="channelsDelete"></a>
# **channelsDelete**
> channelsDelete(resourceGroupName, resourceName, channelName, apiVersion, subscriptionId)



Deletes a Channel registration from a Bot Service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ChannelApi apiInstance = new ChannelApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String resourceName = "resourceName_example"; // String | The name of the Bot resource.
    String channelName = "channelName_example"; // String | The name of the Bot resource.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    try {
      apiInstance.channelsDelete(resourceGroupName, resourceName, channelName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelApi#channelsDelete");
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
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **resourceName** | **String**| The name of the Bot resource. | |
| **channelName** | **String**| The name of the Bot resource. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |

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
| **200** | A 200 (OK) should be returned if the object exists and was deleted successfully; |  -  |
| **204** | a 204 (NoContent) should be used if the resource does not exist and the request is well formed. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="channelsGet"></a>
# **channelsGet**
> BotChannel channelsGet(resourceGroupName, resourceName, channelName, apiVersion, subscriptionId)



Returns a BotService Channel registration specified by the parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ChannelApi apiInstance = new ChannelApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String resourceName = "resourceName_example"; // String | The name of the Bot resource.
    String channelName = "channelName_example"; // String | The name of the Bot resource.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    try {
      BotChannel result = apiInstance.channelsGet(resourceGroupName, resourceName, channelName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelApi#channelsGet");
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
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **resourceName** | **String**| The name of the Bot resource. | |
| **channelName** | **String**| The name of the Bot resource. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |

### Return type

[**BotChannel**](BotChannel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The resource provider should return 200 (OK) to indicate that the operation completed successfully.  |  -  |
| **0** | Error response describing why the operation failed. If the resource group *or* resource does not exist, 404 (NotFound) should be returned. |  -  |

<a id="channelsListByResourceGroup"></a>
# **channelsListByResourceGroup**
> ChannelResponseList channelsListByResourceGroup(resourceGroupName, resourceName, subscriptionId, apiVersion)



Returns all the Channel registrations of a particular BotService resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ChannelApi apiInstance = new ChannelApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String resourceName = "resourceName_example"; // String | The name of the Bot resource.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      ChannelResponseList result = apiInstance.channelsListByResourceGroup(resourceGroupName, resourceName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelApi#channelsListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **resourceName** | **String**| The name of the Bot resource. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**ChannelResponseList**](ChannelResponseList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The resource provider should return 200 (OK) to indicate that the operation completed successfully. For other errors (e.g. internal errors) use the appropriate HTTP error code. The nextLink field is expected to point to the URL the client should use to fetch the next page (per server side paging). This matches the OData guidelines for paged responses here. If a resource provider does not support paging, it should return the same body (JSON object with “value” property) but omit nextLink entirely (or set to null, *not* empty string) for future compatibility. The nextLink should be implemented using following query parameters: · skipToken: opaque token that allows the resource provider to skip resources already enumerated. This value is defined and returned by the RP after first request via nextLink. · top: the optional client query parameter which defines the maximum number of records to be returned by the server. Implementation details: · NextLink may include all the query parameters (specifically OData $filter) used by the client in the first query.  · Server may return less records than requested with nextLink. Returning zero records with NextLink is an acceptable response.  Clients must fetch records until the nextLink is not returned back / null. Clients should never rely on number of returned records to determinate if pagination is completed. |  -  |
| **0** | Error response describing why the operation failed. If the resource group does not exist, 404 (NotFound) will be returned. |  -  |

<a id="channelsListWithKeys"></a>
# **channelsListWithKeys**
> BotChannel channelsListWithKeys(resourceGroupName, resourceName, channelName, apiVersion, subscriptionId)



Lists a Channel registration for a Bot Service including secrets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ChannelApi apiInstance = new ChannelApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String resourceName = "resourceName_example"; // String | The name of the Bot resource.
    String channelName = "FacebookChannel"; // String | The name of the Channel resource.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    try {
      BotChannel result = apiInstance.channelsListWithKeys(resourceGroupName, resourceName, channelName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelApi#channelsListWithKeys");
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
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **resourceName** | **String**| The name of the Bot resource. | |
| **channelName** | **String**| The name of the Channel resource. | [enum: FacebookChannel, EmailChannel, KikChannel, TelegramChannel, SlackChannel, MsTeamsChannel, SkypeChannel, WebChatChannel, DirectLineChannel, SmsChannel] |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |

### Return type

[**BotChannel**](BotChannel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If resource is retrieved successfully, the service should return 200 (OK). |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="channelsUpdate"></a>
# **channelsUpdate**
> BotChannel channelsUpdate(resourceGroupName, resourceName, channelName, apiVersion, subscriptionId, parameters)



Updates a Channel registration for a Bot Service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ChannelApi apiInstance = new ChannelApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String resourceName = "resourceName_example"; // String | The name of the Bot resource.
    String channelName = "FacebookChannel"; // String | The name of the Channel resource.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    BotChannel parameters = new BotChannel(); // BotChannel | The parameters to provide for the created bot.
    try {
      BotChannel result = apiInstance.channelsUpdate(resourceGroupName, resourceName, channelName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelApi#channelsUpdate");
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
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **resourceName** | **String**| The name of the Bot resource. | |
| **channelName** | **String**| The name of the Channel resource. | [enum: FacebookChannel, EmailChannel, KikChannel, TelegramChannel, SlackChannel, MsTeamsChannel, SkypeChannel, WebChatChannel, DirectLineChannel, SmsChannel] |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **parameters** | [**BotChannel**](BotChannel.md)| The parameters to provide for the created bot. | |

### Return type

[**BotChannel**](BotChannel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The resource provider should return 200 (OK) to indicate that the operation completed successfully.  |  -  |
| **201** | If resource is updated successfully, the service should return 201 (Created). Execution to continue asynchronously. |  -  |
| **0** | Error response describing why the operation failed. If the resource group *or* resource does not exist, 404 (NotFound) should be returned. |  -  |

