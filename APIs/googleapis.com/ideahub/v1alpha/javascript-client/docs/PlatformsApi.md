# IdeaHubApi.PlatformsApi

All URIs are relative to *https://ideahub.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ideahubPlatformsPropertiesIdeaActivitiesCreate**](PlatformsApi.md#ideahubPlatformsPropertiesIdeaActivitiesCreate) | **POST** /v1alpha/{parent}/ideaActivities | 
[**ideahubPlatformsPropertiesIdeasList**](PlatformsApi.md#ideahubPlatformsPropertiesIdeasList) | **GET** /v1alpha/{parent}/ideas | 
[**ideahubPlatformsPropertiesLocalesList**](PlatformsApi.md#ideahubPlatformsPropertiesLocalesList) | **GET** /v1alpha/{parent}/locales | 
[**ideahubPlatformsPropertiesTopicStatesPatch**](PlatformsApi.md#ideahubPlatformsPropertiesTopicStatesPatch) | **PATCH** /v1alpha/{name} | 



## ideahubPlatformsPropertiesIdeaActivitiesCreate

> GoogleSearchIdeahubV1alphaIdeaActivity ideahubPlatformsPropertiesIdeaActivitiesCreate(parent, opts)



Creates an idea activity entry.

### Example

```javascript
import IdeaHubApi from 'idea_hub_api';

let apiInstance = new IdeaHubApi.PlatformsApi();
let parent = "parent_example"; // String | Required. The parent resource where this idea activity will be created. Format: platforms/{platform}/property/{property}
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
  'googleSearchIdeahubV1alphaIdeaActivity': new IdeaHubApi.GoogleSearchIdeahubV1alphaIdeaActivity() // GoogleSearchIdeahubV1alphaIdeaActivity | 
};
apiInstance.ideahubPlatformsPropertiesIdeaActivitiesCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The parent resource where this idea activity will be created. Format: platforms/{platform}/property/{property} | 
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
 **googleSearchIdeahubV1alphaIdeaActivity** | [**GoogleSearchIdeahubV1alphaIdeaActivity**](GoogleSearchIdeahubV1alphaIdeaActivity.md)|  | [optional] 

### Return type

[**GoogleSearchIdeahubV1alphaIdeaActivity**](GoogleSearchIdeahubV1alphaIdeaActivity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ideahubPlatformsPropertiesIdeasList

> GoogleSearchIdeahubV1alphaListIdeasResponse ideahubPlatformsPropertiesIdeasList(parent, opts)



List ideas for a given Creator and filter and sort options.

### Example

```javascript
import IdeaHubApi from 'idea_hub_api';

let apiInstance = new IdeaHubApi.PlatformsApi();
let parent = "parent_example"; // String | If defined, specifies the creator for which to filter by. Format: publishers/{publisher}/properties/{property}
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
  'filter': "filter_example", // String | Allows filtering. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions are implicitly combined, as if the `AND` operator was always used. The `OR` operator is currently unsupported. * Supported functions: - `saved(bool)`: If set to true, fetches only saved ideas. If set to false, fetches all except saved ideas. Can't be simultaneously used with `dismissed(bool)`. - `dismissed(bool)`: If set to true, fetches only dismissed ideas. Can't be simultaneously used with `saved(bool)`. The `false` value is currently unsupported. Examples: * `saved(true)` * `saved(false)` * `dismissed(true)` The length of this field should be no more than 500 characters.
  'orderBy': "orderBy_example", // String | Order semantics described below.
  'pageSize': 56, // Number | The maximum number of ideas per page. If unspecified, at most 10 ideas will be returned. The maximum value is 2000; values above 2000 will be coerced to 2000.
  'pageToken': "pageToken_example" // String | Used to fetch next page.
};
apiInstance.ideahubPlatformsPropertiesIdeasList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| If defined, specifies the creator for which to filter by. Format: publishers/{publisher}/properties/{property} | 
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
 **filter** | **String**| Allows filtering. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions are implicitly combined, as if the &#x60;AND&#x60; operator was always used. The &#x60;OR&#x60; operator is currently unsupported. * Supported functions: - &#x60;saved(bool)&#x60;: If set to true, fetches only saved ideas. If set to false, fetches all except saved ideas. Can&#39;t be simultaneously used with &#x60;dismissed(bool)&#x60;. - &#x60;dismissed(bool)&#x60;: If set to true, fetches only dismissed ideas. Can&#39;t be simultaneously used with &#x60;saved(bool)&#x60;. The &#x60;false&#x60; value is currently unsupported. Examples: * &#x60;saved(true)&#x60; * &#x60;saved(false)&#x60; * &#x60;dismissed(true)&#x60; The length of this field should be no more than 500 characters. | [optional] 
 **orderBy** | **String**| Order semantics described below. | [optional] 
 **pageSize** | **Number**| The maximum number of ideas per page. If unspecified, at most 10 ideas will be returned. The maximum value is 2000; values above 2000 will be coerced to 2000. | [optional] 
 **pageToken** | **String**| Used to fetch next page. | [optional] 

### Return type

[**GoogleSearchIdeahubV1alphaListIdeasResponse**](GoogleSearchIdeahubV1alphaListIdeasResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ideahubPlatformsPropertiesLocalesList

> GoogleSearchIdeahubV1alphaListAvailableLocalesResponse ideahubPlatformsPropertiesLocalesList(parent, opts)



Returns which locales ideas are available in for a given Creator.

### Example

```javascript
import IdeaHubApi from 'idea_hub_api';

let apiInstance = new IdeaHubApi.PlatformsApi();
let parent = "parent_example"; // String | Required. The web property to check idea availability for Format: platforms/{platform}/property/{property}
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
  'pageSize': 56, // Number | The maximum number of locales to return. The service may return fewer than this value. If unspecified, at most 100 locales will be returned. The maximum value is 100; values above 100 will be coerced to 100.
  'pageToken': "pageToken_example" // String | A page token, received from a previous `ListAvailableLocales` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAvailableLocales` must match the call that provided the page token.
};
apiInstance.ideahubPlatformsPropertiesLocalesList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The web property to check idea availability for Format: platforms/{platform}/property/{property} | 
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
 **pageSize** | **Number**| The maximum number of locales to return. The service may return fewer than this value. If unspecified, at most 100 locales will be returned. The maximum value is 100; values above 100 will be coerced to 100. | [optional] 
 **pageToken** | **String**| A page token, received from a previous &#x60;ListAvailableLocales&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListAvailableLocales&#x60; must match the call that provided the page token. | [optional] 

### Return type

[**GoogleSearchIdeahubV1alphaListAvailableLocalesResponse**](GoogleSearchIdeahubV1alphaListAvailableLocalesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ideahubPlatformsPropertiesTopicStatesPatch

> GoogleSearchIdeahubV1alphaTopicState ideahubPlatformsPropertiesTopicStatesPatch(name, opts)



Update a topic state resource.

### Example

```javascript
import IdeaHubApi from 'idea_hub_api';

let apiInstance = new IdeaHubApi.PlatformsApi();
let name = "name_example"; // String | Unique identifier for the topic state. Format: platforms/{platform}/properties/{property}/topicStates/{topic_state}
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
  'updateMask': "updateMask_example", // String | The list of fields to be updated.
  'googleSearchIdeahubV1alphaTopicState': new IdeaHubApi.GoogleSearchIdeahubV1alphaTopicState() // GoogleSearchIdeahubV1alphaTopicState | 
};
apiInstance.ideahubPlatformsPropertiesTopicStatesPatch(name, opts, (error, data, response) => {
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
 **name** | **String**| Unique identifier for the topic state. Format: platforms/{platform}/properties/{property}/topicStates/{topic_state} | 
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
 **updateMask** | **String**| The list of fields to be updated. | [optional] 
 **googleSearchIdeahubV1alphaTopicState** | [**GoogleSearchIdeahubV1alphaTopicState**](GoogleSearchIdeahubV1alphaTopicState.md)|  | [optional] 

### Return type

[**GoogleSearchIdeahubV1alphaTopicState**](GoogleSearchIdeahubV1alphaTopicState.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

