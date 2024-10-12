# VictorOps.OnCallApi

All URIs are relative to *https://api.victorops.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPublicV1OncallCurrentGet**](OnCallApi.md#apiPublicV1OncallCurrentGet) | **GET** /api-public/v1/oncall/current | Get an organization&#39;s on-call users
[**apiPublicV1PoliciesPolicyOncallUserPatch**](OnCallApi.md#apiPublicV1PoliciesPolicyOncallUserPatch) | **PATCH** /api-public/v1/policies/{policy}/oncall/user | Create an on-call override (take on-call)
[**apiPublicV1TeamTeamOncallScheduleGet**](OnCallApi.md#apiPublicV1TeamTeamOncallScheduleGet) | **GET** /api-public/v1/team/{team}/oncall/schedule | Get a team&#39;s on-call schedule
[**apiPublicV1TeamTeamOncallUserPatch**](OnCallApi.md#apiPublicV1TeamTeamOncallUserPatch) | **PATCH** /api-public/v1/team/{team}/oncall/user | Create an on-call override (take on-call)
[**apiPublicV1UserUserOncallScheduleGet**](OnCallApi.md#apiPublicV1UserUserOncallScheduleGet) | **GET** /api-public/v1/user/{user}/oncall/schedule | Get a user&#39;s on-call schedule
[**apiPublicV2TeamTeamOncallScheduleGet**](OnCallApi.md#apiPublicV2TeamTeamOncallScheduleGet) | **GET** /api-public/v2/team/{team}/oncall/schedule | Get a team&#39;s on-call schedule
[**apiPublicV2UserUserOncallScheduleGet**](OnCallApi.md#apiPublicV2UserUserOncallScheduleGet) | **GET** /api-public/v2/user/{user}/oncall/schedule | Get a user&#39;s on-call schedule



## apiPublicV1OncallCurrentGet

> ApiPublicV1OncallCurrentGet200Response apiPublicV1OncallCurrentGet(xVOApiId, xVOApiKey)

Get an organization&#39;s on-call users

Get all on-call users/teams for your organization.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.OnCallApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
apiInstance.apiPublicV1OncallCurrentGet(xVOApiId, xVOApiKey, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 

### Return type

[**ApiPublicV1OncallCurrentGet200Response**](ApiPublicV1OncallCurrentGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1PoliciesPolicyOncallUserPatch

> TakeResult apiPublicV1PoliciesPolicyOncallUserPatch(xVOApiId, xVOApiKey, policy, body)

Create an on-call override (take on-call)

Replaces a currently on-call user in the escalation policy with another.  In many cases, the policy slug will match the slug of the team that contains it.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.OnCallApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let policy = "policy_example"; // String | The VictorOps policy 'slug'
let body = new VictorOps.TakeRequest(); // TakeRequest | The take on-call payload
apiInstance.apiPublicV1PoliciesPolicyOncallUserPatch(xVOApiId, xVOApiKey, policy, body, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **policy** | **String**| The VictorOps policy &#39;slug&#39; | 
 **body** | [**TakeRequest**](TakeRequest.md)| The take on-call payload | 

### Return type

[**TakeResult**](TakeResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1TeamTeamOncallScheduleGet

> OnCallAndOverrides apiPublicV1TeamTeamOncallScheduleGet(xVOApiId, xVOApiKey, team, opts)

Get a team&#39;s on-call schedule

__NOTE: This call is deprecated. Please use &#x60;GET /api-public/v2/team/{team}/oncall/schedule&#x60;.__  Get the on-call schedule for a team, including on-call overrides.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.OnCallApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let team = "team_example"; // String | The VictorOps team 'slug'
let opts = {
  'daysForward': 14.0, // Number | Days to include in returned schedule (30 max)
  'daysSkip': 0.0, // Number | Days to skip before computing schedule to return (90 max)
  'step': 0.0 // Number | Step of escalation policy (3 max)
};
apiInstance.apiPublicV1TeamTeamOncallScheduleGet(xVOApiId, xVOApiKey, team, opts, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **team** | **String**| The VictorOps team &#39;slug&#39; | 
 **daysForward** | **Number**| Days to include in returned schedule (30 max) | [optional] [default to 14.0]
 **daysSkip** | **Number**| Days to skip before computing schedule to return (90 max) | [optional] [default to 0.0]
 **step** | **Number**| Step of escalation policy (3 max) | [optional] [default to 0.0]

### Return type

[**OnCallAndOverrides**](OnCallAndOverrides.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1TeamTeamOncallUserPatch

> TakeResult apiPublicV1TeamTeamOncallUserPatch(xVOApiId, xVOApiKey, team, body)

Create an on-call override (take on-call)

__NOTE: This API call is deprecated. Please use &#x60;PATCH /api-public/v2/policies/{policy}/oncall/user&#x60;__  Replaces a currently on-call user on the team with another.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.OnCallApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let team = "team_example"; // String | The VictorOps team 'slug'
let body = new VictorOps.TakeRequest(); // TakeRequest | The take on-call payload
apiInstance.apiPublicV1TeamTeamOncallUserPatch(xVOApiId, xVOApiKey, team, body, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **team** | **String**| The VictorOps team &#39;slug&#39; | 
 **body** | [**TakeRequest**](TakeRequest.md)| The take on-call payload | 

### Return type

[**TakeResult**](TakeResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1UserUserOncallScheduleGet

> [OnCallAndOverrides] apiPublicV1UserUserOncallScheduleGet(xVOApiId, xVOApiKey, user, opts)

Get a user&#39;s on-call schedule

__NOTE: This call is deprecated. Please use &#x60;GET /api-public/v2/user/{user}/oncall/schedule&#x60;.__  Get the on-call schedule for a user for all teams, including on-call overrides.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.OnCallApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let user = "user_example"; // String | The VictorOps user ID
let opts = {
  'daysForward': 14.0, // Number | Days to include in returned schedule (30 max)
  'daysSkip': 0.0, // Number | Days to skip before computing schedule to return (90 max)
  'step': 0.0 // Number | Step of escalation policy (3 max)
};
apiInstance.apiPublicV1UserUserOncallScheduleGet(xVOApiId, xVOApiKey, user, opts, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **user** | **String**| The VictorOps user ID | 
 **daysForward** | **Number**| Days to include in returned schedule (30 max) | [optional] [default to 14.0]
 **daysSkip** | **Number**| Days to skip before computing schedule to return (90 max) | [optional] [default to 0.0]
 **step** | **Number**| Step of escalation policy (3 max) | [optional] [default to 0.0]

### Return type

[**[OnCallAndOverrides]**](OnCallAndOverrides.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV2TeamTeamOncallScheduleGet

> TeamSchedule apiPublicV2TeamTeamOncallScheduleGet(xVOApiId, xVOApiKey, team, opts)

Get a team&#39;s on-call schedule

Get the on-call schedule for a team, including on-call overrides.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.OnCallApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let team = "team_example"; // String | The VictorOps team 'slug'
let opts = {
  'daysForward': 14.0, // Number | Days to include in returned schedule (30 max)
  'daysSkip': 0.0, // Number | Days to skip before computing schedule to return (90 max)
  'step': 0.0 // Number | Step of escalation policy (3 max)
};
apiInstance.apiPublicV2TeamTeamOncallScheduleGet(xVOApiId, xVOApiKey, team, opts, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **team** | **String**| The VictorOps team &#39;slug&#39; | 
 **daysForward** | **Number**| Days to include in returned schedule (30 max) | [optional] [default to 14.0]
 **daysSkip** | **Number**| Days to skip before computing schedule to return (90 max) | [optional] [default to 0.0]
 **step** | **Number**| Step of escalation policy (3 max) | [optional] [default to 0.0]

### Return type

[**TeamSchedule**](TeamSchedule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV2UserUserOncallScheduleGet

> UserSchedule apiPublicV2UserUserOncallScheduleGet(xVOApiId, xVOApiKey, user, opts)

Get a user&#39;s on-call schedule

Get the on-call schedule for a user for all teams the user is on, including on-call overrides.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.OnCallApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let user = "user_example"; // String | The VictorOps user ID
let opts = {
  'daysForward': 14.0, // Number | Days to include in returned schedule (30 max)
  'daysSkip': 0.0, // Number | Days to skip before computing schedule to return (90 max)
  'step': 0.0 // Number | Step of escalation policy (3 max)
};
apiInstance.apiPublicV2UserUserOncallScheduleGet(xVOApiId, xVOApiKey, user, opts, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **user** | **String**| The VictorOps user ID | 
 **daysForward** | **Number**| Days to include in returned schedule (30 max) | [optional] [default to 14.0]
 **daysSkip** | **Number**| Days to skip before computing schedule to return (90 max) | [optional] [default to 0.0]
 **step** | **Number**| Step of escalation policy (3 max) | [optional] [default to 0.0]

### Return type

[**UserSchedule**](UserSchedule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

