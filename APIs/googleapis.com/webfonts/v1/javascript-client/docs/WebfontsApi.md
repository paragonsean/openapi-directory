# WebFontsDeveloperApi.WebfontsApi

All URIs are relative to *https://webfonts.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webfontsWebfontsList**](WebfontsApi.md#webfontsWebfontsList) | **GET** /v1/webfonts | 



## webfontsWebfontsList

> WebfontList webfontsWebfontsList(opts)



Retrieves the list of fonts currently served by the Google Fonts Developer API.

### Example

```javascript
import WebFontsDeveloperApi from 'web_fonts_developer_api';

let apiInstance = new WebFontsDeveloperApi.WebfontsApi();
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
  'capability': ["null"], // [String] | Controls the font urls in `Webfont.files`, by default, static ttf fonts are sent.
  'family': ["null"], // [String] | Filters by Webfont.family, using literal match. If not set, returns all families
  'sort': "sort_example", // String | Enables sorting of the list.
  'subset': "subset_example" // String | Filters by Webfont.subset, if subset is found in Webfont.subsets. If not set, returns all families.
};
apiInstance.webfontsWebfontsList(opts, (error, data, response) => {
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
 **capability** | [**[String]**](String.md)| Controls the font urls in &#x60;Webfont.files&#x60;, by default, static ttf fonts are sent. | [optional] 
 **family** | [**[String]**](String.md)| Filters by Webfont.family, using literal match. If not set, returns all families | [optional] 
 **sort** | **String**| Enables sorting of the list. | [optional] 
 **subset** | **String**| Filters by Webfont.subset, if subset is found in Webfont.subsets. If not set, returns all families. | [optional] 

### Return type

[**WebfontList**](WebfontList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

