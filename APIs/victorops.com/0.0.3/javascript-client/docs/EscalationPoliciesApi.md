# VictorOps.EscalationPoliciesApi

All URIs are relative to *https://api.victorops.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPublicV1PoliciesGet**](EscalationPoliciesApi.md#apiPublicV1PoliciesGet) | **GET** /api-public/v1/policies | Get escalation policy info
[**apiPublicV1TeamTeamPoliciesGet**](EscalationPoliciesApi.md#apiPublicV1TeamTeamPoliciesGet) | **GET** /api-public/v1/team/{team}/policies | Retrieve a list of escalation policies for a team



## apiPublicV1PoliciesGet

> EscalationPolicyInfoList apiPublicV1PoliciesGet(xVOApiId, xVOApiKey)

Get escalation policy info

Retrieves a list of escalation policy information. This API may be called a maximum of once a minute.

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.EscalationPoliciesApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
apiInstance.apiPublicV1PoliciesGet(xVOApiId, xVOApiKey, (error, data, response) => {
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

[**EscalationPolicyInfoList**](EscalationPolicyInfoList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1TeamTeamPoliciesGet

> EscalationPolicyList apiPublicV1TeamTeamPoliciesGet(xVOApiId, xVOApiKey, team)

Retrieve a list of escalation policies for a team

Get the escalation policies for the specified team.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.EscalationPoliciesApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let team = "team_example"; // String | The VictorOps team to fetch
apiInstance.apiPublicV1TeamTeamPoliciesGet(xVOApiId, xVOApiKey, team, (error, data, response) => {
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
 **team** | **String**| The VictorOps team to fetch | 

### Return type

[**EscalationPolicyList**](EscalationPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

