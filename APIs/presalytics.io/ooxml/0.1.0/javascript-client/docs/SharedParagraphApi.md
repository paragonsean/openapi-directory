# OoxmlAutomation.SharedParagraphApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedParagraphGetId**](SharedParagraphApi.md#sharedParagraphGetId) | **GET** /Shared/Paragraph/{id} | Paragraph: Get by Id



## sharedParagraphGetId

> SharedParagraph sharedParagraphGetId(id)

Paragraph: Get by Id

Get by Id: Use this method to retrieve a Paragraph object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedParagraphApi();
let id = "id_example"; // String | 
apiInstance.sharedParagraphGetId(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**SharedParagraph**](SharedParagraph.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

