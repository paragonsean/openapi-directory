# HetrasHotelApiVersion0.RatePlansApi

All URIs are relative to *https://api.hetras-certification.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ratePlansBatchUpdateRates**](RatePlansApi.md#ratePlansBatchUpdateRates) | **PUT** /api/hotel/v0/hotels/{hotelId}/rateplans/batch/$rates | Update a list of base rateplans for a given period and a given base price for single occupancy.
[**ratePlansGetRate**](RatePlansApi.md#ratePlansGetRate) | **GET** /api/hotel/v0/hotels/{hotelId}/rateplans/{rateplanCode}/rates/{businessDay} | Get the setup of a daily rate for a specific business day and rateplan.
[**ratePlansGetRateplan**](RatePlansApi.md#ratePlansGetRateplan) | **GET** /api/hotel/v0/hotels/{hotelId}/rateplans/{rateplanCode} | Get all the details for a specific rateplan in the hotel.
[**ratePlansGetRateplans**](RatePlansApi.md#ratePlansGetRateplans) | **GET** /api/hotel/v0/hotels/{hotelId}/rateplans | Get a list of rateplans for the specified hotel id matching the filter criteria.
[**ratePlansGetRateplansCount**](RatePlansApi.md#ratePlansGetRateplansCount) | **GET** /api/hotel/v0/hotels/{hotelId}/rateplans/$count | Get the count of all rateplans in the hotel matching the given filter criteria.
[**ratePlansGetRates**](RatePlansApi.md#ratePlansGetRates) | **GET** /api/hotel/v0/hotels/{hotelId}/rateplans/{rateplanCode}/rates | Get the setup of the daily rates for a specific rateplan and a defined timeperiod.
[**ratePlansGetRatesCount**](RatePlansApi.md#ratePlansGetRatesCount) | **GET** /api/hotel/v0/hotels/{hotelId}/rateplans/{rateplanCode}/rates/$count | Get the count of all active and loaded daily rates for the defined rateplan in a specified time period.
[**ratePlansPatchRate**](RatePlansApi.md#ratePlansPatchRate) | **PATCH** /api/hotel/v0/hotels/{hotelId}/rateplans/{rateplanCode}/rates/{businessDay} | Partially update a rate of the specified rateplan for a defined business day.
[**ratePlansPatchRates**](RatePlansApi.md#ratePlansPatchRates) | **PATCH** /api/hotel/v0/hotels/{hotelId}/rateplans/{rateplanCode}/rates | Partially update a rate of the specified rateplan for the defined time period.



## ratePlansBatchUpdateRates

> Object ratePlansBatchUpdateRates(appId, appKey, hotelId, request)

Update a list of base rateplans for a given period and a given base price for single occupancy.

Currently this call only allows to set the base price for non-derived rateplans if the rateplan              is active and already loaded for the specified time period.              &lt;br /&gt;&lt;br /&gt;              A request example:&lt;br /&gt;&lt;pre&gt;              [                {                  \&quot;rateplan\&quot;: \&quot;STDN01\&quot;, \&quot;from\&quot;: \&quot;2018-01-01\&quot;, \&quot;to\&quot;: \&quot;2018-01-30\&quot;, \&quot;base_price\&quot;: 120.00                }              ]              &lt;/pre&gt;&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.&lt;br /&gt;

### Example

```javascript
import HetrasHotelApiVersion0 from 'hetras_hotel_api_version_0';

let apiInstance = new HetrasHotelApiVersion0.RatePlansApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | The hotel id the rateplan belongs to.
let request = [new HetrasHotelApiVersion0.RatesBatchUpdateRequestItem()]; // [RatesBatchUpdateRequestItem] | 
apiInstance.ratePlansBatchUpdateRates(appId, appKey, hotelId, request, (error, data, response) => {
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
 **hotelId** | **Number**| The hotel id the rateplan belongs to. | 
 **request** | [**[RatesBatchUpdateRequestItem]**](RatesBatchUpdateRequestItem.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## ratePlansGetRate

> RateResponse ratePlansGetRate(appId, appKey, hotelId, rateplanCode, businessDay)

Get the setup of a daily rate for a specific business day and rateplan.

Read the setup of the daily rate for the defined rateplan for that specific business day.

### Example

```javascript
import HetrasHotelApiVersion0 from 'hetras_hotel_api_version_0';

let apiInstance = new HetrasHotelApiVersion0.RatePlansApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | The hotel id the rateplan belongs to.
let rateplanCode = "rateplanCode_example"; // String | The code of the rateplan you want to see details for.
let businessDay = new Date("2013-10-20T19:20:30+01:00"); // Date | The business day you want to get the rate setup for.
apiInstance.ratePlansGetRate(appId, appKey, hotelId, rateplanCode, businessDay, (error, data, response) => {
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
 **hotelId** | **Number**| The hotel id the rateplan belongs to. | 
 **rateplanCode** | **String**| The code of the rateplan you want to see details for. | 
 **businessDay** | **Date**| The business day you want to get the rate setup for. | 

### Return type

[**RateResponse**](RateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## ratePlansGetRateplan

> ExtendedRateplanEntry ratePlansGetRateplan(appId, appKey, hotelId, rateplanCode)

Get all the details for a specific rateplan in the hotel.

Read the details about a specific rateplan for the defined hotel.

### Example

```javascript
import HetrasHotelApiVersion0 from 'hetras_hotel_api_version_0';

let apiInstance = new HetrasHotelApiVersion0.RatePlansApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | The hotel id the rateplan belongs to.
let rateplanCode = "rateplanCode_example"; // String | The code of the rateplan you want to see details for.
apiInstance.ratePlansGetRateplan(appId, appKey, hotelId, rateplanCode, (error, data, response) => {
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
 **hotelId** | **Number**| The hotel id the rateplan belongs to. | 
 **rateplanCode** | **String**| The code of the rateplan you want to see details for. | 

### Return type

[**ExtendedRateplanEntry**](ExtendedRateplanEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## ratePlansGetRateplans

> RateplansListResponse ratePlansGetRateplans(appId, appKey, hotelId, opts)

Get a list of rateplans for the specified hotel id matching the filter criteria.

With this call you can find rateplans for a hotel by different filters. By default and without any filter criteria              defined it will return you all active rateplans.

### Example

```javascript
import HetrasHotelApiVersion0 from 'hetras_hotel_api_version_0';

let apiInstance = new HetrasHotelApiVersion0.RatePlansApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | The hotel id you are trying to find rateplans for.
let opts = {
  'sellingStatus': "sellingStatus_example", // String | Specify which rateplans to return. If you do not specify a value you will by default get active              rateplans.
  'commissionable': true, // Boolean | Return all rateplans having commisionable status
  'group': "group_example", // String | Return all rateplans belonging to the specified rateplan group
  'baseRateplan': "baseRateplan_example", // String | Return all rateplans having the specified rateplan as base rateplan
  'channelGroup': "channelGroup_example", // String | Return all rateplans that are sold through at least one channel out of the specified channel group
  'channelCode': "channelCode_example", // String | Return all rateplans sold through the specified channel
  'marketCodes': ["null"], // [String] | Return all rateplans having one of the specified values as a market code
  'roomTypes': ["null"], // [String] | Return all rateplans by which at least one of the specified room types are sold
  'includedServices': ["null"], // [String] | Return all rateplans having at least one of the specified services included
  'skip': 56, // Number | Amount of items to skip.
  'top': 56, // Number | Amount of items to select.
  'inlinecount': "inlinecount_example" // String | Return total number of items for a given filter criteria.
};
apiInstance.ratePlansGetRateplans(appId, appKey, hotelId, opts, (error, data, response) => {
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
 **hotelId** | **Number**| The hotel id you are trying to find rateplans for. | 
 **sellingStatus** | **String**| Specify which rateplans to return. If you do not specify a value you will by default get active              rateplans. | [optional] 
 **commissionable** | **Boolean**| Return all rateplans having commisionable status | [optional] 
 **group** | **String**| Return all rateplans belonging to the specified rateplan group | [optional] 
 **baseRateplan** | **String**| Return all rateplans having the specified rateplan as base rateplan | [optional] 
 **channelGroup** | **String**| Return all rateplans that are sold through at least one channel out of the specified channel group | [optional] 
 **channelCode** | **String**| Return all rateplans sold through the specified channel | [optional] 
 **marketCodes** | [**[String]**](String.md)| Return all rateplans having one of the specified values as a market code | [optional] 
 **roomTypes** | [**[String]**](String.md)| Return all rateplans by which at least one of the specified room types are sold | [optional] 
 **includedServices** | [**[String]**](String.md)| Return all rateplans having at least one of the specified services included | [optional] 
 **skip** | **Number**| Amount of items to skip. | [optional] 
 **top** | **Number**| Amount of items to select. | [optional] 
 **inlinecount** | **String**| Return total number of items for a given filter criteria. | [optional] 

### Return type

[**RateplansListResponse**](RateplansListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## ratePlansGetRateplansCount

> TotalCountResponse ratePlansGetRateplansCount(appId, appKey, hotelId, opts)

Get the count of all rateplans in the hotel matching the given filter criteria.

### Example

```javascript
import HetrasHotelApiVersion0 from 'hetras_hotel_api_version_0';

let apiInstance = new HetrasHotelApiVersion0.RatePlansApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | The hotel you are counting the rateplans for.
let opts = {
  'sellingStatus': "sellingStatus_example", // String | Specify which rateplans to return. If you do not specify a value you will by default get active              rateplans.
  'commissionable': true, // Boolean | Return all rateplans having commisionable status
  'group': "group_example", // String | Return all rateplans belonging to the specified rateplan group
  'baseRateplan': "baseRateplan_example", // String | Return all rateplans having the specified rateplan as base rateplan
  'channelGroup': "channelGroup_example", // String | Return all rateplans that are sold through at least one channel out of the specified channel group
  'channelCode': "channelCode_example", // String | Return all rateplans sold through the specified channel
  'marketCodes': ["null"], // [String] | Return all rateplans having one of the specified values as a market code
  'roomTypes': ["null"], // [String] | Return all rateplans by which at least one of the specified room types are sold
  'includedServices': ["null"] // [String] | Return all rateplans having at least one of the specified services included
};
apiInstance.ratePlansGetRateplansCount(appId, appKey, hotelId, opts, (error, data, response) => {
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
 **hotelId** | **Number**| The hotel you are counting the rateplans for. | 
 **sellingStatus** | **String**| Specify which rateplans to return. If you do not specify a value you will by default get active              rateplans. | [optional] 
 **commissionable** | **Boolean**| Return all rateplans having commisionable status | [optional] 
 **group** | **String**| Return all rateplans belonging to the specified rateplan group | [optional] 
 **baseRateplan** | **String**| Return all rateplans having the specified rateplan as base rateplan | [optional] 
 **channelGroup** | **String**| Return all rateplans that are sold through at least one channel out of the specified channel group | [optional] 
 **channelCode** | **String**| Return all rateplans sold through the specified channel | [optional] 
 **marketCodes** | [**[String]**](String.md)| Return all rateplans having one of the specified values as a market code | [optional] 
 **roomTypes** | [**[String]**](String.md)| Return all rateplans by which at least one of the specified room types are sold | [optional] 
 **includedServices** | [**[String]**](String.md)| Return all rateplans having at least one of the specified services included | [optional] 

### Return type

[**TotalCountResponse**](TotalCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## ratePlansGetRates

> RatesResponse ratePlansGetRates(appId, appKey, hotelId, rateplanCode, from, to, opts)

Get the setup of the daily rates for a specific rateplan and a defined timeperiod.

With this call you can read the daily rates setup including the cancellation policy and minimum guarantee per day for the              specified rateplan. You can specify a timeperiod to read the daily rates for. The rateplan needs to be active for at least              one business day in the defined time period and have rates loaded.

### Example

```javascript
import HetrasHotelApiVersion0 from 'hetras_hotel_api_version_0';

let apiInstance = new HetrasHotelApiVersion0.RatePlansApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | The hotel id the rateplan belongs to.
let rateplanCode = "rateplanCode_example"; // String | The code of the rateplan you want to see details for.
let from = new Date("2013-10-20T19:20:30+01:00"); // Date | Defines the last business day you would like to get rates for. The maximum time span between <i>from</i>´and <i>to</i>              is limited to 365 days.
let to = new Date("2013-10-20T19:20:30+01:00"); // Date | Defines the first business day you would like to get rates for.
let opts = {
  'expand': "expand_example", // String | You can expand the supplements per room type on demand. By default they are not shown.
  'skip': 56, // Number | Amount of items to skip.
  'top': 56, // Number | Amount of items to select.
  'inlinecount': "inlinecount_example" // String | Return total number of items for a given filter criteria.
};
apiInstance.ratePlansGetRates(appId, appKey, hotelId, rateplanCode, from, to, opts, (error, data, response) => {
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
 **hotelId** | **Number**| The hotel id the rateplan belongs to. | 
 **rateplanCode** | **String**| The code of the rateplan you want to see details for. | 
 **from** | **Date**| Defines the last business day you would like to get rates for. The maximum time span between &lt;i&gt;from&lt;/i&gt;´and &lt;i&gt;to&lt;/i&gt;              is limited to 365 days. | 
 **to** | **Date**| Defines the first business day you would like to get rates for. | 
 **expand** | **String**| You can expand the supplements per room type on demand. By default they are not shown. | [optional] 
 **skip** | **Number**| Amount of items to skip. | [optional] 
 **top** | **Number**| Amount of items to select. | [optional] 
 **inlinecount** | **String**| Return total number of items for a given filter criteria. | [optional] 

### Return type

[**RatesResponse**](RatesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## ratePlansGetRatesCount

> TotalCountResponse ratePlansGetRatesCount(appId, appKey, hotelId, rateplanCode, from, to)

Get the count of all active and loaded daily rates for the defined rateplan in a specified time period.

### Example

```javascript
import HetrasHotelApiVersion0 from 'hetras_hotel_api_version_0';

let apiInstance = new HetrasHotelApiVersion0.RatePlansApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | The hotel id the rateplan belongs to.
let rateplanCode = "rateplanCode_example"; // String | The code of the rateplan you want to count daily rates for.
let from = new Date("2013-10-20T19:20:30+01:00"); // Date | Defines the last business day you would like to get rates for. The maximum time span between <i>from</i>´and <i>to</i>              is limited to 365 days.
let to = new Date("2013-10-20T19:20:30+01:00"); // Date | Defines the first business day you would like to get rates for.
apiInstance.ratePlansGetRatesCount(appId, appKey, hotelId, rateplanCode, from, to, (error, data, response) => {
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
 **hotelId** | **Number**| The hotel id the rateplan belongs to. | 
 **rateplanCode** | **String**| The code of the rateplan you want to count daily rates for. | 
 **from** | **Date**| Defines the last business day you would like to get rates for. The maximum time span between &lt;i&gt;from&lt;/i&gt;´and &lt;i&gt;to&lt;/i&gt;              is limited to 365 days. | 
 **to** | **Date**| Defines the first business day you would like to get rates for. | 

### Return type

[**TotalCountResponse**](TotalCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## ratePlansPatchRate

> Object ratePlansPatchRate(appId, appKey, hotelId, rateplanCode, businessDay, patchRequest)

Partially update a rate of the specified rateplan for a defined business day.

The hetras API is using this &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/patch\&quot; onfocus&#x3D;\&quot;this.blur()\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Patch Specification&lt;/a&gt;              to partially update an existing resource. Currently this call only allows to set the base price for non-derived rateplans if the rateplan              is active and already loaded for the specified business day.              &lt;br /&gt;&lt;br /&gt;              A request example:&lt;br /&gt;&lt;pre&gt;              [                {                  \&quot;op\&quot;: \&quot;replace\&quot;, \&quot;path\&quot;: \&quot;/base_price\&quot;, \&quot;value\&quot;: 120.00                }              ]              &lt;/pre&gt;&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.&lt;br /&gt;

### Example

```javascript
import HetrasHotelApiVersion0 from 'hetras_hotel_api_version_0';

let apiInstance = new HetrasHotelApiVersion0.RatePlansApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | The hotel id the rateplan belongs to.
let rateplanCode = "rateplanCode_example"; // String | The code of the rateplan you want to update the daily rate details for.
let businessDay = new Date("2013-10-20T19:20:30+01:00"); // Date | The business day of the daily rate you want to update.
let patchRequest = [new HetrasHotelApiVersion0.OperationRatePatchRequest()]; // [OperationRatePatchRequest] | A set of JSON Patch operations.
apiInstance.ratePlansPatchRate(appId, appKey, hotelId, rateplanCode, businessDay, patchRequest, (error, data, response) => {
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
 **hotelId** | **Number**| The hotel id the rateplan belongs to. | 
 **rateplanCode** | **String**| The code of the rateplan you want to update the daily rate details for. | 
 **businessDay** | **Date**| The business day of the daily rate you want to update. | 
 **patchRequest** | [**[OperationRatePatchRequest]**](OperationRatePatchRequest.md)| A set of JSON Patch operations. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## ratePlansPatchRates

> Object ratePlansPatchRates(appId, appKey, hotelId, rateplanCode, from, to, patchRequest)

Partially update a rate of the specified rateplan for the defined time period.

The hetras API is using this &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/patch\&quot; onfocus&#x3D;\&quot;this.blur()\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Patch Specification&lt;/a&gt;              to partially update an existing resource. Currently this call only allows to set the base price for non-derived rateplans if the rateplan              is active and already loaded for the specified time period.              &lt;br /&gt;&lt;br /&gt;              A request example:&lt;br /&gt;&lt;pre&gt;              [                {                  \&quot;op\&quot;: \&quot;replace\&quot;, \&quot;path\&quot;: \&quot;/base_price\&quot;, \&quot;value\&quot;: 120.00                }              ]              &lt;/pre&gt;&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.&lt;br /&gt;

### Example

```javascript
import HetrasHotelApiVersion0 from 'hetras_hotel_api_version_0';

let apiInstance = new HetrasHotelApiVersion0.RatePlansApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | The hotel id the rateplan belongs to.
let rateplanCode = "rateplanCode_example"; // String | The code of the rateplan you want to update the daily rate details for.
let from = new Date("2013-10-20T19:20:30+01:00"); // Date | Defines the last business day you would like to get rates for. The maximum time span between <i>from</i>´and <i>to</i>              is limited to 365 days.
let to = new Date("2013-10-20T19:20:30+01:00"); // Date | Defines the first business day you would like to get rates for.
let patchRequest = [new HetrasHotelApiVersion0.OperationRatePatchRequest()]; // [OperationRatePatchRequest] | A set of JSON Patch operations.
apiInstance.ratePlansPatchRates(appId, appKey, hotelId, rateplanCode, from, to, patchRequest, (error, data, response) => {
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
 **hotelId** | **Number**| The hotel id the rateplan belongs to. | 
 **rateplanCode** | **String**| The code of the rateplan you want to update the daily rate details for. | 
 **from** | **Date**| Defines the last business day you would like to get rates for. The maximum time span between &lt;i&gt;from&lt;/i&gt;´and &lt;i&gt;to&lt;/i&gt;              is limited to 365 days. | 
 **to** | **Date**| Defines the first business day you would like to get rates for. | 
 **patchRequest** | [**[OperationRatePatchRequest]**](OperationRatePatchRequest.md)| A set of JSON Patch operations. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

