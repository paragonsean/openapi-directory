# LogisticsApi.ScheduledDeliveryApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addBlockedDeliveryWindows**](ScheduledDeliveryApi.md#addBlockedDeliveryWindows) | **POST** /api/logistics/pvt/configuration/carriers/{carrierId}/adddayofweekblocked | Add blocked delivery windows
[**apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesGet**](ScheduledDeliveryApi.md#apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesGet) | **GET** /api/logistics-capacity/resources/carrier@{capacityType}@{shippingPolicyId}/time-frames | Search capacity reservations in time range
[**apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesWindowDayFwindowStartTimeTwindowEndTimeGet**](ScheduledDeliveryApi.md#apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesWindowDayFwindowStartTimeTwindowEndTimeGet) | **GET** /api/logistics-capacity/resources/carrier@{capacityType}@{shippingPolicyId}/time-frames/{windowDay}F{windowStartTime}T{windowEndTime} | Get capacity reservation usage by window
[**removeBlockedDeliveryWindows**](ScheduledDeliveryApi.md#removeBlockedDeliveryWindows) | **POST** /api/logistics/pvt/configuration/carriers/{carrierId}/removedayofweekblocked | Remove blocked delivery windows
[**retrieveBlockedDeliveryWindows**](ScheduledDeliveryApi.md#retrieveBlockedDeliveryWindows) | **GET** /api/logistics/pvt/configuration/carriers/{carrierId}/getdayofweekblocked | Retrieve blocked delivery windows



## addBlockedDeliveryWindows

> addBlockedDeliveryWindows(contentType, accept, carrierId, body)

Add blocked delivery windows

Adds blocked delivery windows for your store&#39;s shipping policies.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns time adjusted to the configured time zone of the account.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LogisticsApi.ScheduledDeliveryApi();
let contentType = "'application/json'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let carrierId = "carrierId_example"; // String | 
let body = "2016-08-09T08:00:00"; // String | 
apiInstance.addBlockedDeliveryWindows(contentType, accept, carrierId, body, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **carrierId** | **String**|  | 
 **body** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json; charset=utf-8
- **Accept**: Not defined


## apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesGet

> apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesGet(contentType, accept, capacityType, shippingPolicyId, rangeStart, rangeEnd)

Search capacity reservations in time range

Get information on all capacity reservations made to scheduled delivery windows in a given time range.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns time adjusted to the configured time zone of the account.    &gt; Note that the combined string &#x60;carrier@{capacityType}@{shippingPolicyId}&#x60; can be referred to as a \&quot;resource\&quot; in the API&#39;s messages.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LogisticsApi.ScheduledDeliveryApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "application/vnd.vtex.availability.v1+json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let capacityType = "{{capacityType}}"; // String | How the delivery capacity is measured as defined in the shipping policy. Capacity can be measured by maximum number of orders (`\"orders_quantity\"`) or SKUs (`\"skus_quantity\"`).
let shippingPolicyId = "{{shippingPolicyId}}"; // String | ID of shipping policy to search.
let rangeStart = "yyyy-mm-dd"; // String | Starting date of time range
let rangeEnd = "yyyy-mm-dd"; // String | End date of time range.
apiInstance.apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesGet(contentType, accept, capacityType, shippingPolicyId, rangeStart, rangeEnd, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | 
 **capacityType** | **String**| How the delivery capacity is measured as defined in the shipping policy. Capacity can be measured by maximum number of orders (&#x60;\&quot;orders_quantity\&quot;&#x60;) or SKUs (&#x60;\&quot;skus_quantity\&quot;&#x60;). | 
 **shippingPolicyId** | **String**| ID of shipping policy to search. | 
 **rangeStart** | **String**| Starting date of time range | 
 **rangeEnd** | **String**| End date of time range. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesWindowDayFwindowStartTimeTwindowEndTimeGet

> apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesWindowDayFwindowStartTimeTwindowEndTimeGet(contentType, accept, capacityType, shippingPolicyId, windowDay, windowStartTime, windowEndTime)

Get capacity reservation usage by window

Retrieves capacity usage of a specific scheduled delivery reservation window.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns time adjusted to the configured time zone of the account.    &gt; Note that the combined string &#x60;carrier@{capacityType}@{shippingPolicyId}&#x60; can be referred to as a \&quot;resource\&quot; in the API&#39;s messages.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LogisticsApi.ScheduledDeliveryApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "application/vnd.vtex.availability.v1+json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let capacityType = "{{capacityType}}"; // String | How the delivery capacity is measured as defined in the shipping policy. Capacity can be measured by maximum number of orders (`\"orders_quantity\"`) or SKUs (`\"skus_quantity\"`).
let shippingPolicyId = "{{shippingPolicyId}}"; // String | ID of shipping policy to search.
let windowDay = "yyyy-mm-dd"; // String | Day of the specific scheduled delivery window to be consulted for reservations.
let windowStartTime = "hhmm"; // String | Start time of specific scheduled delivery window to be consulted for reservations.
let windowEndTime = "hhmm"; // String | End time of specific scheduled delivery window to be consulted for reservations.
apiInstance.apiLogisticsCapacityResourcesCarriercapacityTypeshippingPolicyIdTimeFramesWindowDayFwindowStartTimeTwindowEndTimeGet(contentType, accept, capacityType, shippingPolicyId, windowDay, windowStartTime, windowEndTime, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | 
 **capacityType** | **String**| How the delivery capacity is measured as defined in the shipping policy. Capacity can be measured by maximum number of orders (&#x60;\&quot;orders_quantity\&quot;&#x60;) or SKUs (&#x60;\&quot;skus_quantity\&quot;&#x60;). | 
 **shippingPolicyId** | **String**| ID of shipping policy to search. | 
 **windowDay** | **String**| Day of the specific scheduled delivery window to be consulted for reservations. | 
 **windowStartTime** | **String**| Start time of specific scheduled delivery window to be consulted for reservations. | 
 **windowEndTime** | **String**| End time of specific scheduled delivery window to be consulted for reservations. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeBlockedDeliveryWindows

> removeBlockedDeliveryWindows(contentType, accept, carrierId, body)

Remove blocked delivery windows

Removes the blocked delivery windows set to your store&#39;s shipping policies.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns time adjusted to the configured time zone of the account.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LogisticsApi.ScheduledDeliveryApi();
let contentType = "'application/json'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let carrierId = "carrierId_example"; // String | 
let body = "2016-08-09T08:00:00"; // String | 
apiInstance.removeBlockedDeliveryWindows(contentType, accept, carrierId, body, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **carrierId** | **String**|  | 
 **body** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json; charset=utf-8
- **Accept**: Not defined


## retrieveBlockedDeliveryWindows

> retrieveBlockedDeliveryWindows(contentType, accept, carrierId)

Retrieve blocked delivery windows

Lists all blocked delivery windows of your store&#39;s shipping policies, searching by carrier ID.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns **Scheduled Delivery** related time fields adjusted to the configured time zone of the account.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LogisticsApi.ScheduledDeliveryApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let carrierId = "carrierId_example"; // String | 
apiInstance.retrieveBlockedDeliveryWindows(contentType, accept, carrierId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **carrierId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

