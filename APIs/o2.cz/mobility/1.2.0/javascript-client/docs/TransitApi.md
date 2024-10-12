# MobilityApi.TransitApi

All URIs are relative to *https://developer.o2.cz/mobility/sandbox/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transit**](TransitApi.md#transit) | **GET** /transit/{from}/{to} | Transit between basic residential units



## transit

> CountResult transit(from, to, uniques, opts)

Transit between basic residential units

Get count of objects that were moving between basic residential units or objects that were visiting these basic residential units. Specific object&#39;s occurence type in the base residential unit can be requested. If none occurence type is present in the request or both occurence types are zero, the result will be aggregation of all types of occurence for given base residential units. More about base residential units can be found at https://www.czso.cz/csu/rso/zsj_rso (czech).

### Example

```javascript
import MobilityApi from 'mobility_api';

let apiInstance = new MobilityApi.TransitApi();
let from = "127752"; // String | source basic residential unit
let to = "127761"; // String | destination basic residential unit
let uniques = "0"; // String | all or only uniques (0 - all, 1 - uniques)
let opts = {
  'fromType': "fromType_example", // String | occurence type in the source basic residential unit (1 - transit, 2 - visit, 0 - both)
  'toType': "toType_example" // String | occurence type in the destination basic residential unit (1 - transit, 2 - visit, 0 - both)
};
apiInstance.transit(from, to, uniques, opts, (error, data, response) => {
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
 **from** | **String**| source basic residential unit | 
 **to** | **String**| destination basic residential unit | 
 **uniques** | **String**| all or only uniques (0 - all, 1 - uniques) | 
 **fromType** | **String**| occurence type in the source basic residential unit (1 - transit, 2 - visit, 0 - both) | [optional] 
 **toType** | **String**| occurence type in the destination basic residential unit (1 - transit, 2 - visit, 0 - both) | [optional] 

### Return type

[**CountResult**](CountResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

