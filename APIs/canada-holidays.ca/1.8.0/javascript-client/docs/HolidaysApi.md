# CanadaHolidaysApi.HolidaysApi

All URIs are relative to *https://canada-holidays.ca*

Method | HTTP request | Description
------------- | ------------- | -------------
[**holiday**](HolidaysApi.md#holiday) | **GET** /api/v1/holidays/{holidayId} | Get a holiday by id
[**holidays**](HolidaysApi.md#holidays) | **GET** /api/v1/holidays | Get all holidays



## holiday

> Holiday200Response holiday(holidayId, opts)

Get a holiday by id

Returns one Canadian statutory holiday by integer id. Returns a 404 response for invalid ids.

### Example

```javascript
import CanadaHolidaysApi from 'canada_holidays_api';

let apiInstance = new CanadaHolidaysApi.HolidaysApi();
let holidayId = 2; // Number | Primary key for a holiday
let opts = {
  'year': 2023, // Number | A calendar year
  'optional': "'false'" // String | A boolean parameter. If false or 0 (default), will return provinces for which this is a legislated holiday. If true or 1, will return provinces which optionally celebrate this holiday.
};
apiInstance.holiday(holidayId, opts, (error, data, response) => {
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
 **holidayId** | **Number**| Primary key for a holiday | 
 **year** | **Number**| A calendar year | [optional] [default to 2023]
 **optional** | **String**| A boolean parameter. If false or 0 (default), will return provinces for which this is a legislated holiday. If true or 1, will return provinces which optionally celebrate this holiday. | [optional] [default to &#39;false&#39;]

### Return type

[**Holiday200Response**](Holiday200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## holidays

> Holidays200Response holidays(opts)

Get all holidays

Returns Canadian public holidays. Each holiday lists the regions that observe it.

### Example

```javascript
import CanadaHolidaysApi from 'canada_holidays_api';

let apiInstance = new CanadaHolidaysApi.HolidaysApi();
let opts = {
  'year': 2023, // Number | A calendar year
  'federal': "federal_example", // String | A boolean parameter. If true or 1, will return only federal holidays. If false or 0, will return no federal holidays.
  'optional': "'false'" // String | A boolean parameter. If false or 0 (default), will return only legislated holidays. If true or 1, will return optional holidays from Alberta and BC.
};
apiInstance.holidays(opts, (error, data, response) => {
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
 **year** | **Number**| A calendar year | [optional] [default to 2023]
 **federal** | **String**| A boolean parameter. If true or 1, will return only federal holidays. If false or 0, will return no federal holidays. | [optional] 
 **optional** | **String**| A boolean parameter. If false or 0 (default), will return only legislated holidays. If true or 1, will return optional holidays from Alberta and BC. | [optional] [default to &#39;false&#39;]

### Return type

[**Holidays200Response**](Holidays200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

