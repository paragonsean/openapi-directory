# Tafqit.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert**](DefaultApi.md#convert) | **POST** /convert | 



## convert

> convert(opts)



Convert the number into its Arabic text representation حول العدد إلى ما يقابله كتابة

### Example

```javascript
import Tafqit from 'tafqit';

let apiInstance = new Tafqit.DefaultApi();
let opts = {
  'hundredsForm': "hundredsForm_example", // String | Some use مائة others use مئة , both works in Arabic. If left empty the default is مائة 
  'theNumber': "theNumber_example", // String | Put the number here. Decimal is supported by most units.
  'unit': "unit_example" // String | The counted subject, be it a currency like درهم إماراتي  or a size unit like متر مربع If the unit does not appear in the text result, it may not be supported. Please contact us to add it.
};
apiInstance.convert(opts, (error, data, response) => {
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
 **hundredsForm** | **String**| Some use مائة others use مئة , both works in Arabic. If left empty the default is مائة  | [optional] 
 **theNumber** | **String**| Put the number here. Decimal is supported by most units. | [optional] 
 **unit** | **String**| The counted subject, be it a currency like درهم إماراتي  or a size unit like متر مربع If the unit does not appear in the text result, it may not be supported. Please contact us to add it. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined

