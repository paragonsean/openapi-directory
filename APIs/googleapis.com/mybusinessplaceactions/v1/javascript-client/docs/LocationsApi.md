# MyBusinessPlaceActionsApi.LocationsApi

All URIs are relative to *https://mybusinessplaceactions.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mybusinessplaceactionsLocationsPlaceActionLinksCreate**](LocationsApi.md#mybusinessplaceactionsLocationsPlaceActionLinksCreate) | **POST** /v1/{parent}/placeActionLinks | 
[**mybusinessplaceactionsLocationsPlaceActionLinksDelete**](LocationsApi.md#mybusinessplaceactionsLocationsPlaceActionLinksDelete) | **DELETE** /v1/{name} | 
[**mybusinessplaceactionsLocationsPlaceActionLinksGet**](LocationsApi.md#mybusinessplaceactionsLocationsPlaceActionLinksGet) | **GET** /v1/{name} | 
[**mybusinessplaceactionsLocationsPlaceActionLinksList**](LocationsApi.md#mybusinessplaceactionsLocationsPlaceActionLinksList) | **GET** /v1/{parent}/placeActionLinks | 
[**mybusinessplaceactionsLocationsPlaceActionLinksPatch**](LocationsApi.md#mybusinessplaceactionsLocationsPlaceActionLinksPatch) | **PATCH** /v1/{name} | 



## mybusinessplaceactionsLocationsPlaceActionLinksCreate

> PlaceActionLink mybusinessplaceactionsLocationsPlaceActionLinksCreate(parent, opts)



Creates a place action link associated with the specified location, and returns it. The request is considered duplicate if the &#x60;parent&#x60;, &#x60;place_action_link.uri&#x60; and &#x60;place_action_link.place_action_type&#x60; are the same as a previous request.

### Example

```javascript
import MyBusinessPlaceActionsApi from 'my_business_place_actions_api';

let apiInstance = new MyBusinessPlaceActionsApi.LocationsApi();
let parent = "parent_example"; // String | Required. The resource name of the location where to create this place action link. `locations/{location_id}`.
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
  'placeActionLink': new MyBusinessPlaceActionsApi.PlaceActionLink() // PlaceActionLink | 
};
apiInstance.mybusinessplaceactionsLocationsPlaceActionLinksCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The resource name of the location where to create this place action link. &#x60;locations/{location_id}&#x60;. | 
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
 **placeActionLink** | [**PlaceActionLink**](PlaceActionLink.md)|  | [optional] 

### Return type

[**PlaceActionLink**](PlaceActionLink.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mybusinessplaceactionsLocationsPlaceActionLinksDelete

> Object mybusinessplaceactionsLocationsPlaceActionLinksDelete(name, opts)



Deletes a place action link from the specified location.

### Example

```javascript
import MyBusinessPlaceActionsApi from 'my_business_place_actions_api';

let apiInstance = new MyBusinessPlaceActionsApi.LocationsApi();
let name = "name_example"; // String | Required. The resource name of the place action link to remove from the location.
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
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.mybusinessplaceactionsLocationsPlaceActionLinksDelete(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The resource name of the place action link to remove from the location. | 
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

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mybusinessplaceactionsLocationsPlaceActionLinksGet

> PlaceActionLink mybusinessplaceactionsLocationsPlaceActionLinksGet(name, opts)



Gets the specified place action link.

### Example

```javascript
import MyBusinessPlaceActionsApi from 'my_business_place_actions_api';

let apiInstance = new MyBusinessPlaceActionsApi.LocationsApi();
let name = "name_example"; // String | Required. The name of the place action link to fetch.
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
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.mybusinessplaceactionsLocationsPlaceActionLinksGet(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The name of the place action link to fetch. | 
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

### Return type

[**PlaceActionLink**](PlaceActionLink.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mybusinessplaceactionsLocationsPlaceActionLinksList

> ListPlaceActionLinksResponse mybusinessplaceactionsLocationsPlaceActionLinksList(parent, opts)



Lists the place action links for the specified location.

### Example

```javascript
import MyBusinessPlaceActionsApi from 'my_business_place_actions_api';

let apiInstance = new MyBusinessPlaceActionsApi.LocationsApi();
let parent = "parent_example"; // String | Required. The name of the location whose place action links will be listed. `locations/{location_id}`.
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
  'filter': "filter_example", // String | Optional. A filter constraining the place action links to return. The response includes entries that match the filter. We support only the following filter: 1. place_action_type=XYZ where XYZ is a valid PlaceActionType.
  'pageSize': 56, // Number | Optional. How many place action links to return per page. Default of 10. The minimum is 1.
  'pageToken': "pageToken_example" // String | Optional. If specified, returns the next page of place action links.
};
apiInstance.mybusinessplaceactionsLocationsPlaceActionLinksList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The name of the location whose place action links will be listed. &#x60;locations/{location_id}&#x60;. | 
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
 **filter** | **String**| Optional. A filter constraining the place action links to return. The response includes entries that match the filter. We support only the following filter: 1. place_action_type&#x3D;XYZ where XYZ is a valid PlaceActionType. | [optional] 
 **pageSize** | **Number**| Optional. How many place action links to return per page. Default of 10. The minimum is 1. | [optional] 
 **pageToken** | **String**| Optional. If specified, returns the next page of place action links. | [optional] 

### Return type

[**ListPlaceActionLinksResponse**](ListPlaceActionLinksResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mybusinessplaceactionsLocationsPlaceActionLinksPatch

> PlaceActionLink mybusinessplaceactionsLocationsPlaceActionLinksPatch(name, opts)



Updates the specified place action link and returns it.

### Example

```javascript
import MyBusinessPlaceActionsApi from 'my_business_place_actions_api';

let apiInstance = new MyBusinessPlaceActionsApi.LocationsApi();
let name = "name_example"; // String | Optional. The resource name, in the format `locations/{location_id}/placeActionLinks/{place_action_link_id}`. The name field will only be considered in UpdatePlaceActionLink and DeletePlaceActionLink requests for updating and deleting links respectively. However, it will be ignored in CreatePlaceActionLink request, where `place_action_link_id` will be assigned by the server on successful creation of a new link and returned as part of the response.
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
  'updateMask': "updateMask_example", // String | Required. The specific fields to update. The only editable fields are `uri`, `place_action_type` and `is_preferred`. If the updated link already exists at the same location with the same `place_action_type` and `uri`, fails with an `ALREADY_EXISTS` error.
  'placeActionLink': new MyBusinessPlaceActionsApi.PlaceActionLink() // PlaceActionLink | 
};
apiInstance.mybusinessplaceactionsLocationsPlaceActionLinksPatch(name, opts, (error, data, response) => {
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
 **name** | **String**| Optional. The resource name, in the format &#x60;locations/{location_id}/placeActionLinks/{place_action_link_id}&#x60;. The name field will only be considered in UpdatePlaceActionLink and DeletePlaceActionLink requests for updating and deleting links respectively. However, it will be ignored in CreatePlaceActionLink request, where &#x60;place_action_link_id&#x60; will be assigned by the server on successful creation of a new link and returned as part of the response. | 
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
 **updateMask** | **String**| Required. The specific fields to update. The only editable fields are &#x60;uri&#x60;, &#x60;place_action_type&#x60; and &#x60;is_preferred&#x60;. If the updated link already exists at the same location with the same &#x60;place_action_type&#x60; and &#x60;uri&#x60;, fails with an &#x60;ALREADY_EXISTS&#x60; error. | [optional] 
 **placeActionLink** | [**PlaceActionLink**](PlaceActionLink.md)|  | [optional] 

### Return type

[**PlaceActionLink**](PlaceActionLink.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

