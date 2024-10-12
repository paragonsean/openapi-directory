# PolicyAnalyzerApi.ProjectsApi

All URIs are relative to *https://policyanalyzer.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policyanalyzerProjectsLocationsActivityTypesActivitiesQuery**](ProjectsApi.md#policyanalyzerProjectsLocationsActivityTypesActivitiesQuery) | **GET** /v1/{parent}/activities:query | 



## policyanalyzerProjectsLocationsActivityTypesActivitiesQuery

> GoogleCloudPolicyanalyzerV1QueryActivityResponse policyanalyzerProjectsLocationsActivityTypesActivitiesQuery(parent, opts)



Queries policy activities on Google Cloud resources.

### Example

```javascript
import PolicyAnalyzerApi from 'policy_analyzer_api';
let defaultClient = PolicyAnalyzerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyAnalyzerApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The container resource on which to execute the request. Acceptable formats: `projects/[PROJECT_ID|PROJECT_NUMBER]/locations/[LOCATION]/activityTypes/[ACTIVITY_TYPE]` LOCATION here refers to Google Cloud Locations: https://cloud.google.com/about/locations/
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
  'filter': "filter_example", // String | Optional. Filter expression to restrict the activities returned. For serviceAccountLastAuthentication activities, supported filters are: - `activities.full_resource_name {=} [STRING]` - `activities.fullResourceName {=} [STRING]` where `[STRING]` is the full resource name of the service account. For serviceAccountKeyLastAuthentication activities, supported filters are: - `activities.full_resource_name {=} [STRING]` - `activities.fullResourceName {=} [STRING]` where `[STRING]` is the full resource name of the service account key.
  'pageSize': 56, // Number | Optional. The maximum number of results to return from this request. Max limit is 1000. Non-positive values are ignored. The presence of `nextPageToken` in the response indicates that more results might be available.
  'pageToken': "pageToken_example" // String | Optional. If present, then retrieve the next batch of results from the preceding call to this method. `pageToken` must be the value of `nextPageToken` from the previous response. The values of other method parameters should be identical to those in the previous call.
};
apiInstance.policyanalyzerProjectsLocationsActivityTypesActivitiesQuery(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The container resource on which to execute the request. Acceptable formats: &#x60;projects/[PROJECT_ID|PROJECT_NUMBER]/locations/[LOCATION]/activityTypes/[ACTIVITY_TYPE]&#x60; LOCATION here refers to Google Cloud Locations: https://cloud.google.com/about/locations/ | 
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
 **filter** | **String**| Optional. Filter expression to restrict the activities returned. For serviceAccountLastAuthentication activities, supported filters are: - &#x60;activities.full_resource_name {&#x3D;} [STRING]&#x60; - &#x60;activities.fullResourceName {&#x3D;} [STRING]&#x60; where &#x60;[STRING]&#x60; is the full resource name of the service account. For serviceAccountKeyLastAuthentication activities, supported filters are: - &#x60;activities.full_resource_name {&#x3D;} [STRING]&#x60; - &#x60;activities.fullResourceName {&#x3D;} [STRING]&#x60; where &#x60;[STRING]&#x60; is the full resource name of the service account key. | [optional] 
 **pageSize** | **Number**| Optional. The maximum number of results to return from this request. Max limit is 1000. Non-positive values are ignored. The presence of &#x60;nextPageToken&#x60; in the response indicates that more results might be available. | [optional] 
 **pageToken** | **String**| Optional. If present, then retrieve the next batch of results from the preceding call to this method. &#x60;pageToken&#x60; must be the value of &#x60;nextPageToken&#x60; from the previous response. The values of other method parameters should be identical to those in the previous call. | [optional] 

### Return type

[**GoogleCloudPolicyanalyzerV1QueryActivityResponse**](GoogleCloudPolicyanalyzerV1QueryActivityResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

