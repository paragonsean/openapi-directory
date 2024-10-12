# VersionhistoryGoogleapisComApi.PlatformsApi

All URIs are relative to *https://versionhistory.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**versionhistoryPlatformsChannelsList**](PlatformsApi.md#versionhistoryPlatformsChannelsList) | **GET** /v1/{parent}/channels | 
[**versionhistoryPlatformsChannelsVersionsList**](PlatformsApi.md#versionhistoryPlatformsChannelsVersionsList) | **GET** /v1/{parent}/versions | 
[**versionhistoryPlatformsChannelsVersionsReleasesList**](PlatformsApi.md#versionhistoryPlatformsChannelsVersionsReleasesList) | **GET** /v1/{parent}/releases | 
[**versionhistoryPlatformsList**](PlatformsApi.md#versionhistoryPlatformsList) | **GET** /v1/{parent}/platforms | 



## versionhistoryPlatformsChannelsList

> ListChannelsResponse versionhistoryPlatformsChannelsList(parent, opts)



Returns list of channels that are available for a given platform.

### Example

```javascript
import VersionhistoryGoogleapisComApi from 'versionhistory_googleapis_com_api';

let apiInstance = new VersionhistoryGoogleapisComApi.PlatformsApi();
let parent = "parent_example"; // String | Required. The platform, which owns this collection of channels. Format: {product}/platforms/{platform}
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
  'pageSize': 56, // Number | Optional. Optional limit on the number of channels to include in the response. If unspecified, the server will pick an appropriate default.
  'pageToken': "pageToken_example" // String | Optional. A page token, received from a previous `ListChannels` call. Provide this to retrieve the subsequent page.
};
apiInstance.versionhistoryPlatformsChannelsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The platform, which owns this collection of channels. Format: {product}/platforms/{platform} | 
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
 **pageSize** | **Number**| Optional. Optional limit on the number of channels to include in the response. If unspecified, the server will pick an appropriate default. | [optional] 
 **pageToken** | **String**| Optional. A page token, received from a previous &#x60;ListChannels&#x60; call. Provide this to retrieve the subsequent page. | [optional] 

### Return type

[**ListChannelsResponse**](ListChannelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## versionhistoryPlatformsChannelsVersionsList

> ListVersionsResponse versionhistoryPlatformsChannelsVersionsList(parent, opts)



Returns list of version for the given platform/channel.

### Example

```javascript
import VersionhistoryGoogleapisComApi from 'versionhistory_googleapis_com_api';

let apiInstance = new VersionhistoryGoogleapisComApi.PlatformsApi();
let parent = "parent_example"; // String | Required. The channel, which owns this collection of versions. Format: {product}/platforms/{platform}/channels/{channel}
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
  'filter': "filter_example", // String | Optional. Filter string. Format is a comma separated list of All comma separated filter clauses are conjoined with a logical \"and\". Valid field_names are \"version\", \"name\", \"platform\", and \"channel\". Valid operators are \"<\", \"<=\", \"=\", \">=\", and \">\". Channel comparison is done by distance from stable. Ex) stable < beta, beta < dev, canary < canary_asan. Version comparison is done numerically. If version is not entirely written, the version will be appended with 0 in missing fields. Ex) version > 80 becoms version > 80.0.0.0 Name and platform are filtered by string comparison. Ex) \"...?filter=channel<=beta, version >= 80 Ex) \"...?filter=version > 80, version < 81
  'orderBy': "orderBy_example", // String | Optional. Ordering string. Valid order_by strings are \"version\", \"name\", \"platform\", and \"channel\". Optionally, you can append \" desc\" or \" asc\" to specify the sorting order. Multiple order_by strings can be used in a comma separated list. Ordering by channel will sort by distance from the stable channel (not alphabetically). A list of channels sorted in this order is: stable, beta, dev, canary, and canary_asan. Sorting by name may cause unexpected behaviour as it is a naive string sort. For example, 1.0.0.8 will be before 1.0.0.10 in descending order. If order_by is not specified the response will be sorted by version in descending order. Ex) \"...?order_by=version asc\" Ex) \"...?order_by=platform desc, channel, version\"
  'pageSize': 56, // Number | Optional. Optional limit on the number of versions to include in the response. If unspecified, the server will pick an appropriate default.
  'pageToken': "pageToken_example" // String | Optional. A page token, received from a previous `ListVersions` call. Provide this to retrieve the subsequent page.
};
apiInstance.versionhistoryPlatformsChannelsVersionsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The channel, which owns this collection of versions. Format: {product}/platforms/{platform}/channels/{channel} | 
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
 **filter** | **String**| Optional. Filter string. Format is a comma separated list of All comma separated filter clauses are conjoined with a logical \&quot;and\&quot;. Valid field_names are \&quot;version\&quot;, \&quot;name\&quot;, \&quot;platform\&quot;, and \&quot;channel\&quot;. Valid operators are \&quot;&lt;\&quot;, \&quot;&lt;&#x3D;\&quot;, \&quot;&#x3D;\&quot;, \&quot;&gt;&#x3D;\&quot;, and \&quot;&gt;\&quot;. Channel comparison is done by distance from stable. Ex) stable &lt; beta, beta &lt; dev, canary &lt; canary_asan. Version comparison is done numerically. If version is not entirely written, the version will be appended with 0 in missing fields. Ex) version &gt; 80 becoms version &gt; 80.0.0.0 Name and platform are filtered by string comparison. Ex) \&quot;...?filter&#x3D;channel&lt;&#x3D;beta, version &gt;&#x3D; 80 Ex) \&quot;...?filter&#x3D;version &gt; 80, version &lt; 81 | [optional] 
 **orderBy** | **String**| Optional. Ordering string. Valid order_by strings are \&quot;version\&quot;, \&quot;name\&quot;, \&quot;platform\&quot;, and \&quot;channel\&quot;. Optionally, you can append \&quot; desc\&quot; or \&quot; asc\&quot; to specify the sorting order. Multiple order_by strings can be used in a comma separated list. Ordering by channel will sort by distance from the stable channel (not alphabetically). A list of channels sorted in this order is: stable, beta, dev, canary, and canary_asan. Sorting by name may cause unexpected behaviour as it is a naive string sort. For example, 1.0.0.8 will be before 1.0.0.10 in descending order. If order_by is not specified the response will be sorted by version in descending order. Ex) \&quot;...?order_by&#x3D;version asc\&quot; Ex) \&quot;...?order_by&#x3D;platform desc, channel, version\&quot; | [optional] 
 **pageSize** | **Number**| Optional. Optional limit on the number of versions to include in the response. If unspecified, the server will pick an appropriate default. | [optional] 
 **pageToken** | **String**| Optional. A page token, received from a previous &#x60;ListVersions&#x60; call. Provide this to retrieve the subsequent page. | [optional] 

### Return type

[**ListVersionsResponse**](ListVersionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## versionhistoryPlatformsChannelsVersionsReleasesList

> ListReleasesResponse versionhistoryPlatformsChannelsVersionsReleasesList(parent, opts)



Returns list of releases of the given version.

### Example

```javascript
import VersionhistoryGoogleapisComApi from 'versionhistory_googleapis_com_api';

let apiInstance = new VersionhistoryGoogleapisComApi.PlatformsApi();
let parent = "parent_example"; // String | Required. The version, which owns this collection of releases. Format: {product}/platforms/{platform}/channels/{channel}/versions/{version}
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
  'filter': "filter_example", // String | Optional. Filter string. Format is a comma separated list of All comma separated filter clauses are conjoined with a logical \"and\". Valid field_names are \"version\", \"name\", \"platform\", \"channel\", \"fraction\" \"starttime\", and \"endtime\". Valid operators are \"<\", \"<=\", \"=\", \">=\", and \">\". Channel comparison is done by distance from stable. must be a valid channel when filtering by channel. Ex) stable < beta, beta < dev, canary < canary_asan. Version comparison is done numerically. Ex) 1.0.0.8 < 1.0.0.10. If version is not entirely written, the version will be appended with 0 for the missing fields. Ex) version > 80 becoms version > 80.0.0.0 When filtering by starttime or endtime, string must be in RFC 3339 date string format. Name and platform are filtered by string comparison. Ex) \"...?filter=channel<=beta, version >= 80 Ex) \"...?filter=version > 80, version < 81 Ex) \"...?filter=starttime>2020-01-01T00:00:00Z
  'orderBy': "orderBy_example", // String | Optional. Ordering string. Valid order_by strings are \"version\", \"name\", \"starttime\", \"endtime\", \"platform\", \"channel\", and \"fraction\". Optionally, you can append \"desc\" or \"asc\" to specify the sorting order. Multiple order_by strings can be used in a comma separated list. Ordering by channel will sort by distance from the stable channel (not alphabetically). A list of channels sorted in this order is: stable, beta, dev, canary, and canary_asan. Sorting by name may cause unexpected behaviour as it is a naive string sort. For example, 1.0.0.8 will be before 1.0.0.10 in descending order. If order_by is not specified the response will be sorted by starttime in descending order. Ex) \"...?order_by=starttime asc\" Ex) \"...?order_by=platform desc, channel, startime desc\"
  'pageSize': 56, // Number | Optional. Optional limit on the number of releases to include in the response. If unspecified, the server will pick an appropriate default.
  'pageToken': "pageToken_example" // String | Optional. A page token, received from a previous `ListReleases` call. Provide this to retrieve the subsequent page.
};
apiInstance.versionhistoryPlatformsChannelsVersionsReleasesList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The version, which owns this collection of releases. Format: {product}/platforms/{platform}/channels/{channel}/versions/{version} | 
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
 **filter** | **String**| Optional. Filter string. Format is a comma separated list of All comma separated filter clauses are conjoined with a logical \&quot;and\&quot;. Valid field_names are \&quot;version\&quot;, \&quot;name\&quot;, \&quot;platform\&quot;, \&quot;channel\&quot;, \&quot;fraction\&quot; \&quot;starttime\&quot;, and \&quot;endtime\&quot;. Valid operators are \&quot;&lt;\&quot;, \&quot;&lt;&#x3D;\&quot;, \&quot;&#x3D;\&quot;, \&quot;&gt;&#x3D;\&quot;, and \&quot;&gt;\&quot;. Channel comparison is done by distance from stable. must be a valid channel when filtering by channel. Ex) stable &lt; beta, beta &lt; dev, canary &lt; canary_asan. Version comparison is done numerically. Ex) 1.0.0.8 &lt; 1.0.0.10. If version is not entirely written, the version will be appended with 0 for the missing fields. Ex) version &gt; 80 becoms version &gt; 80.0.0.0 When filtering by starttime or endtime, string must be in RFC 3339 date string format. Name and platform are filtered by string comparison. Ex) \&quot;...?filter&#x3D;channel&lt;&#x3D;beta, version &gt;&#x3D; 80 Ex) \&quot;...?filter&#x3D;version &gt; 80, version &lt; 81 Ex) \&quot;...?filter&#x3D;starttime&gt;2020-01-01T00:00:00Z | [optional] 
 **orderBy** | **String**| Optional. Ordering string. Valid order_by strings are \&quot;version\&quot;, \&quot;name\&quot;, \&quot;starttime\&quot;, \&quot;endtime\&quot;, \&quot;platform\&quot;, \&quot;channel\&quot;, and \&quot;fraction\&quot;. Optionally, you can append \&quot;desc\&quot; or \&quot;asc\&quot; to specify the sorting order. Multiple order_by strings can be used in a comma separated list. Ordering by channel will sort by distance from the stable channel (not alphabetically). A list of channels sorted in this order is: stable, beta, dev, canary, and canary_asan. Sorting by name may cause unexpected behaviour as it is a naive string sort. For example, 1.0.0.8 will be before 1.0.0.10 in descending order. If order_by is not specified the response will be sorted by starttime in descending order. Ex) \&quot;...?order_by&#x3D;starttime asc\&quot; Ex) \&quot;...?order_by&#x3D;platform desc, channel, startime desc\&quot; | [optional] 
 **pageSize** | **Number**| Optional. Optional limit on the number of releases to include in the response. If unspecified, the server will pick an appropriate default. | [optional] 
 **pageToken** | **String**| Optional. A page token, received from a previous &#x60;ListReleases&#x60; call. Provide this to retrieve the subsequent page. | [optional] 

### Return type

[**ListReleasesResponse**](ListReleasesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## versionhistoryPlatformsList

> ListPlatformsResponse versionhistoryPlatformsList(parent, opts)



Returns list of platforms that are available for a given product. The resource \&quot;product\&quot; has no resource name in its name.

### Example

```javascript
import VersionhistoryGoogleapisComApi from 'versionhistory_googleapis_com_api';

let apiInstance = new VersionhistoryGoogleapisComApi.PlatformsApi();
let parent = "parent_example"; // String | Required. The product, which owns this collection of platforms. Format: {product}
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
  'pageSize': 56, // Number | Optional. Optional limit on the number of channels to include in the response. If unspecified, the server will pick an appropriate default.
  'pageToken': "pageToken_example" // String | Optional. A page token, received from a previous `ListChannels` call. Provide this to retrieve the subsequent page.
};
apiInstance.versionhistoryPlatformsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The product, which owns this collection of platforms. Format: {product} | 
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
 **pageSize** | **Number**| Optional. Optional limit on the number of channels to include in the response. If unspecified, the server will pick an appropriate default. | [optional] 
 **pageToken** | **String**| Optional. A page token, received from a previous &#x60;ListChannels&#x60; call. Provide this to retrieve the subsequent page. | [optional] 

### Return type

[**ListPlatformsResponse**](ListPlatformsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

