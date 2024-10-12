# HetrasBookingApiVersion0.BlocksApi

All URIs are relative to *https://api.hetras-certification.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blocksGetBlocksAsync**](BlocksApi.md#blocksGetBlocksAsync) | **GET** /api/booking/v0/blocks | Gets a list of blocks.
[**blocksGetBlocksCountAsync**](BlocksApi.md#blocksGetBlocksCountAsync) | **GET** /api/booking/v0/blocks/$count | Get total blocks count that match the given filter criteria.
[**blocksGetSingleBlockAsync**](BlocksApi.md#blocksGetSingleBlockAsync) | **GET** /api/booking/v0/blocks/{blockCode} | Gets the details for a specific block.



## blocksGetBlocksAsync

> Object blocksGetBlocksAsync(appId, appKey, token, opts)

Gets a list of blocks.

With this endpoint you can request a list of blocks for the hotel chain. Currently we only support to optionally              filter by the group code linked to the block. Additional filters will be available soon.

### Example

```javascript
import HetrasBookingApiVersion0 from 'hetras_booking_api_version_0';

let apiInstance = new HetrasBookingApiVersion0.BlocksApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let token = new HetrasBookingApiVersion0.CancellationToken(); // CancellationToken | 
let opts = {
  'hotelId': 56, // Number | Only return blocks for this specific hotel.
  'groupCode': "groupCode_example", // String | Filter the blocks by the specified group code
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | Return all blocks where the block's last_departure is greater than specified date.
  'to': new Date("2013-10-20T19:20:30+01:00"), // Date | Return all blocks where the block's last_departure is less than specified date.
  'status': "status_example", // String | Return all blocks where the block status is one of the specified values.
  'ratePlanCodes': ["null"], // [String] | Return all blocks that have related the specified comma-separated rate plans.
  'countDetails': true, // Boolean | If true it will include also details of block count per each room type.
  'skip': 56, // Number | Amount of items to skip.
  'top': 56, // Number | Amount of items to select.
  'inlinecount': "inlinecount_example" // String | Return total number of items for a given filter criteria.
};
apiInstance.blocksGetBlocksAsync(appId, appKey, token, opts, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **token** | [**CancellationToken**](CancellationToken.md)|  | 
 **hotelId** | **Number**| Only return blocks for this specific hotel. | [optional] 
 **groupCode** | **String**| Filter the blocks by the specified group code | [optional] 
 **from** | **Date**| Return all blocks where the block&#39;s last_departure is greater than specified date. | [optional] 
 **to** | **Date**| Return all blocks where the block&#39;s last_departure is less than specified date. | [optional] 
 **status** | **String**| Return all blocks where the block status is one of the specified values. | [optional] 
 **ratePlanCodes** | [**[String]**](String.md)| Return all blocks that have related the specified comma-separated rate plans. | [optional] 
 **countDetails** | **Boolean**| If true it will include also details of block count per each room type. | [optional] 
 **skip** | **Number**| Amount of items to skip. | [optional] 
 **top** | **Number**| Amount of items to select. | [optional] 
 **inlinecount** | **String**| Return total number of items for a given filter criteria. | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## blocksGetBlocksCountAsync

> TotalCountResponse blocksGetBlocksCountAsync(appId, appKey, token, opts)

Get total blocks count that match the given filter criteria.

### Example

```javascript
import HetrasBookingApiVersion0 from 'hetras_booking_api_version_0';

let apiInstance = new HetrasBookingApiVersion0.BlocksApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let token = new HetrasBookingApiVersion0.CancellationToken(); // CancellationToken | 
let opts = {
  'hotelId': 56, // Number | Only return blocks for this specific hotel.
  'groupCode': "groupCode_example", // String | Filter the blocks by the specified group code
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | Return all blocks where the block's last_departure is greater than specified date.
  'to': new Date("2013-10-20T19:20:30+01:00"), // Date | Return all blocks where the block's last_departure is less than specified date.
  'status': "status_example", // String | Return all blocks where the block status is one of the specified values.
  'ratePlanCodes': ["null"], // [String] | Return all blocks that have related the specified comma-separated rate plans.
  'countDetails': true // Boolean | If true it will include also details of block count per each room type.
};
apiInstance.blocksGetBlocksCountAsync(appId, appKey, token, opts, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **token** | [**CancellationToken**](CancellationToken.md)|  | 
 **hotelId** | **Number**| Only return blocks for this specific hotel. | [optional] 
 **groupCode** | **String**| Filter the blocks by the specified group code | [optional] 
 **from** | **Date**| Return all blocks where the block&#39;s last_departure is greater than specified date. | [optional] 
 **to** | **Date**| Return all blocks where the block&#39;s last_departure is less than specified date. | [optional] 
 **status** | **String**| Return all blocks where the block status is one of the specified values. | [optional] 
 **ratePlanCodes** | [**[String]**](String.md)| Return all blocks that have related the specified comma-separated rate plans. | [optional] 
 **countDetails** | **Boolean**| If true it will include also details of block count per each room type. | [optional] 

### Return type

[**TotalCountResponse**](TotalCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## blocksGetSingleBlockAsync

> Object blocksGetSingleBlockAsync(appId, appKey, blockCode, token)

Gets the details for a specific block.

Read all informationen about a block including the numbers of blocked rooms per room type and business day.

### Example

```javascript
import HetrasBookingApiVersion0 from 'hetras_booking_api_version_0';

let apiInstance = new HetrasBookingApiVersion0.BlocksApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let blockCode = "blockCode_example"; // String | Specifies the block code. The block code is composed of the hotel code, a dash and the block code               as shown in the hetras UI.
let token = new HetrasBookingApiVersion0.CancellationToken(); // CancellationToken | 
apiInstance.blocksGetSingleBlockAsync(appId, appKey, blockCode, token, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **blockCode** | **String**| Specifies the block code. The block code is composed of the hotel code, a dash and the block code               as shown in the hetras UI. | 
 **token** | [**CancellationToken**](CancellationToken.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

