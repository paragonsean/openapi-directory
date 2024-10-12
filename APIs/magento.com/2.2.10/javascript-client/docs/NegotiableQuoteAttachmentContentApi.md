# MagentoB2B.NegotiableQuoteAttachmentContentApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**negotiableQuoteAttachmentContentManagementV1GetGet**](NegotiableQuoteAttachmentContentApi.md#negotiableQuoteAttachmentContentManagementV1GetGet) | **GET** /V1/negotiableQuote/attachmentContent | negotiableQuote/attachmentContent



## negotiableQuoteAttachmentContentManagementV1GetGet

> [NegotiableQuoteDataAttachmentContentInterface] negotiableQuoteAttachmentContentManagementV1GetGet(attachmentIds)

negotiableQuote/attachmentContent

Returns content for one or more files attached on the quote comment.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.NegotiableQuoteAttachmentContentApi();
let attachmentIds = [null]; // [Number] | 
apiInstance.negotiableQuoteAttachmentContentManagementV1GetGet(attachmentIds, (error, data, response) => {
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
 **attachmentIds** | [**[Number]**](Number.md)|  | 

### Return type

[**[NegotiableQuoteDataAttachmentContentInterface]**](NegotiableQuoteDataAttachmentContentInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

