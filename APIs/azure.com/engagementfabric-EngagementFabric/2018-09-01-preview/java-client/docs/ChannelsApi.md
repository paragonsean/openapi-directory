# ChannelsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**channelsCreateOrUpdate**](ChannelsApi.md#channelsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName}/Channels/{channelName} | Create or Update the EngagementFabric channel |
| [**channelsDelete**](ChannelsApi.md#channelsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName}/Channels/{channelName} | Delete the EngagementFabric channel |
| [**channelsGet**](ChannelsApi.md#channelsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName}/Channels/{channelName} | Get the EngagementFabric channel |
| [**channelsListByAccount**](ChannelsApi.md#channelsListByAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName}/Channels | List the EngagementFabric channels |


<a id="channelsCreateOrUpdate"></a>
# **channelsCreateOrUpdate**
> Channel channelsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, channelName, apiVersion, channel)

Create or Update the EngagementFabric channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ChannelsApi apiInstance = new ChannelsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
    String accountName = "accountName_example"; // String | Account Name
    String channelName = "channelName_example"; // String | Channel Name
    String apiVersion = "apiVersion_example"; // String | API version
    Channel channel = new Channel(); // Channel | The EngagementFabric channel description
    try {
      Channel result = apiInstance.channelsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, channelName, apiVersion, channel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsApi#channelsCreateOrUpdate");
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
| **subscriptionId** | **String**| Subscription ID | |
| **resourceGroupName** | **String**| Resource Group Name | |
| **accountName** | **String**| Account Name | |
| **channelName** | **String**| Channel Name | |
| **apiVersion** | **String**| API version | |
| **channel** | [**Channel**](Channel.md)| The EngagementFabric channel description | |

### Return type

[**Channel**](Channel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="channelsDelete"></a>
# **channelsDelete**
> channelsDelete(subscriptionId, resourceGroupName, accountName, channelName, apiVersion)

Delete the EngagementFabric channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ChannelsApi apiInstance = new ChannelsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
    String accountName = "accountName_example"; // String | Account Name
    String channelName = "channelName_example"; // String | The EngagementFabric channel name
    String apiVersion = "apiVersion_example"; // String | API version
    try {
      apiInstance.channelsDelete(subscriptionId, resourceGroupName, accountName, channelName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsApi#channelsDelete");
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
| **subscriptionId** | **String**| Subscription ID | |
| **resourceGroupName** | **String**| Resource Group Name | |
| **accountName** | **String**| Account Name | |
| **channelName** | **String**| The EngagementFabric channel name | |
| **apiVersion** | **String**| API version | |

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
| **0** | Error response |  -  |

<a id="channelsGet"></a>
# **channelsGet**
> Channel channelsGet(subscriptionId, resourceGroupName, accountName, channelName, apiVersion)

Get the EngagementFabric channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ChannelsApi apiInstance = new ChannelsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
    String accountName = "accountName_example"; // String | Account Name
    String channelName = "channelName_example"; // String | Channel Name
    String apiVersion = "apiVersion_example"; // String | API version
    try {
      Channel result = apiInstance.channelsGet(subscriptionId, resourceGroupName, accountName, channelName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsApi#channelsGet");
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
| **subscriptionId** | **String**| Subscription ID | |
| **resourceGroupName** | **String**| Resource Group Name | |
| **accountName** | **String**| Account Name | |
| **channelName** | **String**| Channel Name | |
| **apiVersion** | **String**| API version | |

### Return type

[**Channel**](Channel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="channelsListByAccount"></a>
# **channelsListByAccount**
> ChannelList channelsListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion)

List the EngagementFabric channels

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ChannelsApi apiInstance = new ChannelsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
    String accountName = "accountName_example"; // String | Account Name
    String apiVersion = "apiVersion_example"; // String | API version
    try {
      ChannelList result = apiInstance.channelsListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsApi#channelsListByAccount");
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
| **subscriptionId** | **String**| Subscription ID | |
| **resourceGroupName** | **String**| Resource Group Name | |
| **accountName** | **String**| Account Name | |
| **apiVersion** | **String**| API version | |

### Return type

[**ChannelList**](ChannelList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

