# FactCheckToolsApi.ClaimsApi

All URIs are relative to *https://factchecktools.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**factchecktoolsClaimsSearch**](ClaimsApi.md#factchecktoolsClaimsSearch) | **GET** /v1alpha1/claims:search | 



## factchecktoolsClaimsSearch

> GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponse factchecktoolsClaimsSearch(opts)



Search through fact-checked claims.

### Example

```javascript
import FactCheckToolsApi from 'fact_check_tools_api';

let apiInstance = new FactCheckToolsApi.ClaimsApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'languageCode': "languageCode_example", // String | The BCP-47 language code, such as \"en-US\" or \"sr-Latn\". Can be used to restrict results by language, though we do not currently consider the region.
  'maxAgeDays': 56, // Number | The maximum age of the returned search results, in days. Age is determined by either claim date or review date, whichever is newer.
  'offset': 56, // Number | An integer that specifies the current offset (that is, starting result location) in search results. This field is only considered if `page_token` is unset. For example, 0 means to return results starting from the first matching result, and 10 means to return from the 11th result.
  'pageSize': 56, // Number | The pagination size. We will return up to that many results. Defaults to 10 if not set.
  'pageToken': "pageToken_example", // String | The pagination token. You may provide the `next_page_token` returned from a previous List request, if any, in order to get the next page. All other fields must have the same values as in the previous request.
  'query': "query_example", // String | Textual query string. Required unless `review_publisher_site_filter` is specified.
  'reviewPublisherSiteFilter': "reviewPublisherSiteFilter_example" // String | The review publisher site to filter results by, e.g. nytimes.com.
};
apiInstance.factchecktoolsClaimsSearch(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **languageCode** | **String**| The BCP-47 language code, such as \&quot;en-US\&quot; or \&quot;sr-Latn\&quot;. Can be used to restrict results by language, though we do not currently consider the region. | [optional] 
 **maxAgeDays** | **Number**| The maximum age of the returned search results, in days. Age is determined by either claim date or review date, whichever is newer. | [optional] 
 **offset** | **Number**| An integer that specifies the current offset (that is, starting result location) in search results. This field is only considered if &#x60;page_token&#x60; is unset. For example, 0 means to return results starting from the first matching result, and 10 means to return from the 11th result. | [optional] 
 **pageSize** | **Number**| The pagination size. We will return up to that many results. Defaults to 10 if not set. | [optional] 
 **pageToken** | **String**| The pagination token. You may provide the &#x60;next_page_token&#x60; returned from a previous List request, if any, in order to get the next page. All other fields must have the same values as in the previous request. | [optional] 
 **query** | **String**| Textual query string. Required unless &#x60;review_publisher_site_filter&#x60; is specified. | [optional] 
 **reviewPublisherSiteFilter** | **String**| The review publisher site to filter results by, e.g. nytimes.com. | [optional] 

### Return type

[**GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponse**](GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

