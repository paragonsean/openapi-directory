# MyBusinessPlaceActionsApi.PlaceActionTypeMetadataApi

All URIs are relative to *https://mybusinessplaceactions.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mybusinessplaceactionsPlaceActionTypeMetadataList**](PlaceActionTypeMetadataApi.md#mybusinessplaceactionsPlaceActionTypeMetadataList) | **GET** /v1/placeActionTypeMetadata | 



## mybusinessplaceactionsPlaceActionTypeMetadataList

> ListPlaceActionTypeMetadataResponse mybusinessplaceactionsPlaceActionTypeMetadataList(opts)



Returns the list of available place action types for a location or country.

### Example

```javascript
import MyBusinessPlaceActionsApi from 'my_business_place_actions_api';

let apiInstance = new MyBusinessPlaceActionsApi.PlaceActionTypeMetadataApi();
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
  'filter': "filter_example", // String | Optional. A filter constraining the place action types to return metadata for. The response includes entries that match the filter. We support only the following filters: 1. location=XYZ where XYZ is a string indicating the resource name of a location, in the format `locations/{location_id}`. 2. region_code=XYZ where XYZ is a Unicode CLDR region code to find available action types. If no filter is provided, all place action types are returned.
  'languageCode': "languageCode_example", // String | Optional. The IETF BCP-47 code of language to get display names in. If this language is not available, they will be provided in English.
  'pageSize': 56, // Number | Optional. How many action types to include per page. Default is 10, minimum is 1.
  'pageToken': "pageToken_example" // String | Optional. If specified, the next page of place action type metadata is retrieved. The `pageToken` is returned when a call to `placeActionTypeMetadata.list` returns more results than can fit into the requested page size.
};
apiInstance.mybusinessplaceactionsPlaceActionTypeMetadataList(opts, (error, data, response) => {
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
 **filter** | **String**| Optional. A filter constraining the place action types to return metadata for. The response includes entries that match the filter. We support only the following filters: 1. location&#x3D;XYZ where XYZ is a string indicating the resource name of a location, in the format &#x60;locations/{location_id}&#x60;. 2. region_code&#x3D;XYZ where XYZ is a Unicode CLDR region code to find available action types. If no filter is provided, all place action types are returned. | [optional] 
 **languageCode** | **String**| Optional. The IETF BCP-47 code of language to get display names in. If this language is not available, they will be provided in English. | [optional] 
 **pageSize** | **Number**| Optional. How many action types to include per page. Default is 10, minimum is 1. | [optional] 
 **pageToken** | **String**| Optional. If specified, the next page of place action type metadata is retrieved. The &#x60;pageToken&#x60; is returned when a call to &#x60;placeActionTypeMetadata.list&#x60; returns more results than can fit into the requested page size. | [optional] 

### Return type

[**ListPlaceActionTypeMetadataResponse**](ListPlaceActionTypeMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

