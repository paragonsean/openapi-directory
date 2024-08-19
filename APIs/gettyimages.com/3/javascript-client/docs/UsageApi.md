# GettyImages.UsageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3UsageBatchesIdPut**](UsageApi.md#v3UsageBatchesIdPut) | **PUT** /v3/usage-batches/{id} | Report usage of assets via a batch format.



## v3UsageBatchesIdPut

> ReportUsageBatchResponse v3UsageBatchesIdPut(id, opts)

Report usage of assets via a batch format.

# Report Usage  Use this endpoint to report the usages of a set of assets. The count of assets submitted in a single batch to this endpoint is limited to 1000. Note that all asset Ids specified must be valid or the operation will fail causing no usages to be recorded. In this case, you will need to remove the invalid asset Ids from the query request and re-submit the query.  ##  Quickstart  You&#39;ll need an API key and a [Resource Owner Grant](http://developers.gettyimages.com/en/authorization-faq.html) access token to use this resource. Please see our [Getting Started](http://developers.gettyimages.com/en/getting-started.html) page for more information on how to sign up for an API key.   _Note_: Date of use can be in any unambiguous date format. 

### Example

```javascript
import GettyImages from 'getty_images';
let defaultClient = GettyImages.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Api-Key
let Api-Key = defaultClient.authentications['Api-Key'];
Api-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Api-Key.apiKeyPrefix = 'Token';

let apiInstance = new GettyImages.UsageApi();
let id = "id_example"; // String | Specifies a unique batch transaction id to identify the report.
let opts = {
  'reportUsageBatchRequest': new GettyImages.ReportUsageBatchRequest() // ReportUsageBatchRequest | Specifies up to 1000 sets of asset Id, usage count, and date of use to submit usages for.               Note that all asset Ids specified must be valid or the operation will fail causing no usages to be recorded.               All dates must be on or before this date and the format should be ISO 8601 (ex: YYYY-MM-DD), time is not needed.
};
apiInstance.v3UsageBatchesIdPut(id, opts, (error, data, response) => {
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
 **id** | **String**| Specifies a unique batch transaction id to identify the report. | 
 **reportUsageBatchRequest** | [**ReportUsageBatchRequest**](ReportUsageBatchRequest.md)| Specifies up to 1000 sets of asset Id, usage count, and date of use to submit usages for.               Note that all asset Ids specified must be valid or the operation will fail causing no usages to be recorded.               All dates must be on or before this date and the format should be ISO 8601 (ex: YYYY-MM-DD), time is not needed. | [optional] 

### Return type

[**ReportUsageBatchResponse**](ReportUsageBatchResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

