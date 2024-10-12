# EngagementFabric.ChannelsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channelsCreateOrUpdate**](ChannelsApi.md#channelsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName}/Channels/{channelName} | Create or Update the EngagementFabric channel
[**channelsDelete**](ChannelsApi.md#channelsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName}/Channels/{channelName} | Delete the EngagementFabric channel
[**channelsGet**](ChannelsApi.md#channelsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName}/Channels/{channelName} | Get the EngagementFabric channel
[**channelsListByAccount**](ChannelsApi.md#channelsListByAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName}/Channels | List the EngagementFabric channels



## channelsCreateOrUpdate

> Channel channelsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, channelName, apiVersion, channel)

Create or Update the EngagementFabric channel

### Example

```javascript
import EngagementFabric from 'engagement_fabric';

let apiInstance = new EngagementFabric.ChannelsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
let accountName = "accountName_example"; // String | Account Name
let channelName = "channelName_example"; // String | Channel Name
let apiVersion = "apiVersion_example"; // String | API version
let channel = new EngagementFabric.Channel(); // Channel | The EngagementFabric channel description
apiInstance.channelsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, channelName, apiVersion, channel, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Subscription ID | 
 **resourceGroupName** | **String**| Resource Group Name | 
 **accountName** | **String**| Account Name | 
 **channelName** | **String**| Channel Name | 
 **apiVersion** | **String**| API version | 
 **channel** | [**Channel**](Channel.md)| The EngagementFabric channel description | 

### Return type

[**Channel**](Channel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## channelsDelete

> channelsDelete(subscriptionId, resourceGroupName, accountName, channelName, apiVersion)

Delete the EngagementFabric channel

### Example

```javascript
import EngagementFabric from 'engagement_fabric';

let apiInstance = new EngagementFabric.ChannelsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
let accountName = "accountName_example"; // String | Account Name
let channelName = "channelName_example"; // String | The EngagementFabric channel name
let apiVersion = "apiVersion_example"; // String | API version
apiInstance.channelsDelete(subscriptionId, resourceGroupName, accountName, channelName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Subscription ID | 
 **resourceGroupName** | **String**| Resource Group Name | 
 **accountName** | **String**| Account Name | 
 **channelName** | **String**| The EngagementFabric channel name | 
 **apiVersion** | **String**| API version | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## channelsGet

> Channel channelsGet(subscriptionId, resourceGroupName, accountName, channelName, apiVersion)

Get the EngagementFabric channel

### Example

```javascript
import EngagementFabric from 'engagement_fabric';

let apiInstance = new EngagementFabric.ChannelsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
let accountName = "accountName_example"; // String | Account Name
let channelName = "channelName_example"; // String | Channel Name
let apiVersion = "apiVersion_example"; // String | API version
apiInstance.channelsGet(subscriptionId, resourceGroupName, accountName, channelName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Subscription ID | 
 **resourceGroupName** | **String**| Resource Group Name | 
 **accountName** | **String**| Account Name | 
 **channelName** | **String**| Channel Name | 
 **apiVersion** | **String**| API version | 

### Return type

[**Channel**](Channel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## channelsListByAccount

> ChannelList channelsListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion)

List the EngagementFabric channels

### Example

```javascript
import EngagementFabric from 'engagement_fabric';

let apiInstance = new EngagementFabric.ChannelsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
let accountName = "accountName_example"; // String | Account Name
let apiVersion = "apiVersion_example"; // String | API version
apiInstance.channelsListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Subscription ID | 
 **resourceGroupName** | **String**| Resource Group Name | 
 **accountName** | **String**| Account Name | 
 **apiVersion** | **String**| API version | 

### Return type

[**ChannelList**](ChannelList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

