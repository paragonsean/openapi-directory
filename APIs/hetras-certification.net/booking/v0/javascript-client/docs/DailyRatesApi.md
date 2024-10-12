# HetrasBookingApiVersion0.DailyRatesApi

All URIs are relative to *https://api.hetras-certification.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dailyRatesGetDailyRates**](DailyRatesApi.md#dailyRatesGetDailyRates) | **GET** /api/booking/v0/daily_rates | Get a list of daily rates given a hotel Id, a channel code and a date range.



## dailyRatesGetDailyRates

> DailyRatesResponse dailyRatesGetDailyRates(appId, appKey, hotelId, from, to, channelCode, opts)

Get a list of daily rates given a hotel Id, a channel code and a date range.

With the rates request you can get a list of different daily rates. You will have to at least               specify the hotel, the channel code, and a calendar range. The channel code will define which rates will be               returned based on the access control configuration for the rates. Additionally rate plan codes may be specified in              the request in order to limit only those rates of the given plans, if they are not specified, it will return all the public rate plans.              If requested the caller may specify whether he wants policies or not.

### Example

```javascript
import HetrasBookingApiVersion0 from 'hetras_booking_api_version_0';

let apiInstance = new HetrasBookingApiVersion0.DailyRatesApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | Define the hotel id to request the availability for.
let from = new Date("2013-10-20T19:20:30+01:00"); // Date | Define the first business day you would like to get availability numbers for. The day should not be in the past.
let to = new Date("2013-10-20T19:20:30+01:00"); // Date | Define the last business day you would like to get rates for (inclusive). The maximum time span between <i>'From'</i> and <i>'To'</i>              is limited to 365 days. This can't be less than the 'From' date.
let channelCode = "channelCode_example"; // String | Define the channel code in order to look up the rates for.
let opts = {
  'expand': ["null"], // [String] | Define the sections you want to expand and get informed about rates for.
  'ratePlanCodes': ["null"], // [String] | Define the codes of rate plans to show in the response. A list of comma ',' separated rate plan codes.
  'skip': 56, // Number | Amount of items to skip.
  'top': 56, // Number | Amount of items to select.
  'inlinecount': "inlinecount_example" // String | Return total number of items for a given filter criteria.
};
apiInstance.dailyRatesGetDailyRates(appId, appKey, hotelId, from, to, channelCode, opts, (error, data, response) => {
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
 **hotelId** | **Number**| Define the hotel id to request the availability for. | 
 **from** | **Date**| Define the first business day you would like to get availability numbers for. The day should not be in the past. | 
 **to** | **Date**| Define the last business day you would like to get rates for (inclusive). The maximum time span between &lt;i&gt;&#39;From&#39;&lt;/i&gt; and &lt;i&gt;&#39;To&#39;&lt;/i&gt;              is limited to 365 days. This can&#39;t be less than the &#39;From&#39; date. | 
 **channelCode** | **String**| Define the channel code in order to look up the rates for. | 
 **expand** | [**[String]**](String.md)| Define the sections you want to expand and get informed about rates for. | [optional] 
 **ratePlanCodes** | [**[String]**](String.md)| Define the codes of rate plans to show in the response. A list of comma &#39;,&#39; separated rate plan codes. | [optional] 
 **skip** | **Number**| Amount of items to skip. | [optional] 
 **top** | **Number**| Amount of items to select. | [optional] 
 **inlinecount** | **String**| Return total number of items for a given filter criteria. | [optional] 

### Return type

[**DailyRatesResponse**](DailyRatesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

