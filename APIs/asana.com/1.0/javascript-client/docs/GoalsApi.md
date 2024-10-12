# Asana.GoalsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addFollowers**](GoalsApi.md#addFollowers) | **POST** /goals/{goal_gid}/addFollowers | Add a collaborator to a goal
[**createGoal**](GoalsApi.md#createGoal) | **POST** /goals | Create a goal
[**createGoalMetric**](GoalsApi.md#createGoalMetric) | **POST** /goals/{goal_gid}/setMetric | Create a goal metric
[**deleteGoal**](GoalsApi.md#deleteGoal) | **DELETE** /goals/{goal_gid} | Delete a goal
[**getGoal**](GoalsApi.md#getGoal) | **GET** /goals/{goal_gid} | Get a goal
[**getGoals**](GoalsApi.md#getGoals) | **GET** /goals | Get goals
[**getParentGoalsForGoal**](GoalsApi.md#getParentGoalsForGoal) | **GET** /goals/{goal_gid}/parentGoals | Get parent goals from a goal
[**removeFollowers**](GoalsApi.md#removeFollowers) | **POST** /goals/{goal_gid}/removeFollowers | Remove a collaborator from a goal
[**updateGoal**](GoalsApi.md#updateGoal) | **PUT** /goals/{goal_gid} | Update a goal
[**updateGoalMetric**](GoalsApi.md#updateGoalMetric) | **POST** /goals/{goal_gid}/setMetricCurrentValue | Update a goal metric



## addFollowers

> CreateGoal201Response addFollowers(goalGid, addFollowersRequest, opts)

Add a collaborator to a goal

Adds followers to a goal. Returns the goal the followers were added to. Each goal can be associated with zero or more followers in the system. Requests to add/remove followers, if successful, will return the complete updated goal record, described above.

### Example

```javascript
import Asana from 'asana';
let defaultClient = Asana.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Asana.GoalsApi();
let goalGid = "12345"; // String | Globally unique identifier for the goal.
let addFollowersRequest = new Asana.AddFollowersRequest(); // AddFollowersRequest | The followers to be added as collaborators
let opts = {
  'optPretty': true, // Boolean | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
  'optFields': ["null"] // [String] | Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
};
apiInstance.addFollowers(goalGid, addFollowersRequest, opts, (error, data, response) => {
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
 **goalGid** | **String**| Globally unique identifier for the goal. | 
 **addFollowersRequest** | [**AddFollowersRequest**](AddFollowersRequest.md)| The followers to be added as collaborators | 
 **optPretty** | **Boolean**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **optFields** | [**[String]**](String.md)| Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options. | [optional] 

### Return type

[**CreateGoal201Response**](CreateGoal201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createGoal

> CreateGoal201Response createGoal(createGoalRequest, opts)

Create a goal

Creates a new goal in a workspace or team.  Returns the full record of the newly created goal.

### Example

```javascript
import Asana from 'asana';
let defaultClient = Asana.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Asana.GoalsApi();
let createGoalRequest = new Asana.CreateGoalRequest(); // CreateGoalRequest | The goal to create.
let opts = {
  'optPretty': true, // Boolean | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
  'optFields': ["null"], // [String] | Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
  'limit': 50, // Number | Results per page. The number of objects to return per page. The value must be between 1 and 100.
  'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9" // String | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
};
apiInstance.createGoal(createGoalRequest, opts, (error, data, response) => {
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
 **createGoalRequest** | [**CreateGoalRequest**](CreateGoalRequest.md)| The goal to create. | 
 **optPretty** | **Boolean**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **optFields** | [**[String]**](String.md)| Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options. | [optional] 
 **limit** | **Number**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **String**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional] 

### Return type

[**CreateGoal201Response**](CreateGoal201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createGoalMetric

> CreateGoal201Response createGoalMetric(goalGid, createGoalMetricRequest, opts)

Create a goal metric

Creates and adds a goal metric to a specified goal. Note that this replaces an existing goal metric if one already exists.

### Example

```javascript
import Asana from 'asana';
let defaultClient = Asana.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Asana.GoalsApi();
let goalGid = "12345"; // String | Globally unique identifier for the goal.
let createGoalMetricRequest = new Asana.CreateGoalMetricRequest(); // CreateGoalMetricRequest | The goal metric to create.
let opts = {
  'optPretty': true, // Boolean | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
  'optFields': ["null"] // [String] | Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
};
apiInstance.createGoalMetric(goalGid, createGoalMetricRequest, opts, (error, data, response) => {
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
 **goalGid** | **String**| Globally unique identifier for the goal. | 
 **createGoalMetricRequest** | [**CreateGoalMetricRequest**](CreateGoalMetricRequest.md)| The goal metric to create. | 
 **optPretty** | **Boolean**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **optFields** | [**[String]**](String.md)| Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options. | [optional] 

### Return type

[**CreateGoal201Response**](CreateGoal201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteGoal

> DeleteAttachment200Response deleteGoal(goalGid, opts)

Delete a goal

A specific, existing goal can be deleted by making a DELETE request on the URL for that goal.  Returns an empty data record.

### Example

```javascript
import Asana from 'asana';
let defaultClient = Asana.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Asana.GoalsApi();
let goalGid = "12345"; // String | Globally unique identifier for the goal.
let opts = {
  'optPretty': true, // Boolean | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
  'optFields': ["null"] // [String] | Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
};
apiInstance.deleteGoal(goalGid, opts, (error, data, response) => {
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
 **goalGid** | **String**| Globally unique identifier for the goal. | 
 **optPretty** | **Boolean**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **optFields** | [**[String]**](String.md)| Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options. | [optional] 

### Return type

[**DeleteAttachment200Response**](DeleteAttachment200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGoal

> CreateGoal201Response getGoal(goalGid, opts)

Get a goal

Returns the complete goal record for a single goal.

### Example

```javascript
import Asana from 'asana';
let defaultClient = Asana.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Asana.GoalsApi();
let goalGid = "12345"; // String | Globally unique identifier for the goal.
let opts = {
  'optPretty': true, // Boolean | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
  'optFields': ["null"] // [String] | Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
};
apiInstance.getGoal(goalGid, opts, (error, data, response) => {
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
 **goalGid** | **String**| Globally unique identifier for the goal. | 
 **optPretty** | **Boolean**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **optFields** | [**[String]**](String.md)| Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options. | [optional] 

### Return type

[**CreateGoal201Response**](CreateGoal201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGoals

> GetGoals200Response getGoals(opts)

Get goals

Returns compact goal records.

### Example

```javascript
import Asana from 'asana';
let defaultClient = Asana.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Asana.GoalsApi();
let opts = {
  'optPretty': true, // Boolean | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
  'optFields': ["null"], // [String] | Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
  'limit': 50, // Number | Results per page. The number of objects to return per page. The value must be between 1 and 100.
  'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", // String | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
  'portfolio': "159874", // String | Globally unique identifier for supporting portfolio.
  'project': "512241", // String | Globally unique identifier for supporting project.
  'isWorkspaceLevel': false, // Boolean | Filter to goals with is_workspace_level set to query value. Must be used with the workspace parameter.
  'team': "31326", // String | Globally unique identifier for the team.
  'workspace': "31326", // String | Globally unique identifier for the workspace.
  'timePeriods': ["null"] // [String] | Globally unique identifiers for the time periods.
};
apiInstance.getGoals(opts, (error, data, response) => {
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
 **optPretty** | **Boolean**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **optFields** | [**[String]**](String.md)| Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options. | [optional] 
 **limit** | **Number**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **String**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional] 
 **portfolio** | **String**| Globally unique identifier for supporting portfolio. | [optional] 
 **project** | **String**| Globally unique identifier for supporting project. | [optional] 
 **isWorkspaceLevel** | **Boolean**| Filter to goals with is_workspace_level set to query value. Must be used with the workspace parameter. | [optional] 
 **team** | **String**| Globally unique identifier for the team. | [optional] 
 **workspace** | **String**| Globally unique identifier for the workspace. | [optional] 
 **timePeriods** | [**[String]**](String.md)| Globally unique identifiers for the time periods. | [optional] 

### Return type

[**GetGoals200Response**](GetGoals200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getParentGoalsForGoal

> GetGoals200Response getParentGoalsForGoal(goalGid, opts)

Get parent goals from a goal

Returns a compact representation of all of the parent goals of a goal.

### Example

```javascript
import Asana from 'asana';
let defaultClient = Asana.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Asana.GoalsApi();
let goalGid = "12345"; // String | Globally unique identifier for the goal.
let opts = {
  'optPretty': true, // Boolean | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
  'optFields': ["null"] // [String] | Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
};
apiInstance.getParentGoalsForGoal(goalGid, opts, (error, data, response) => {
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
 **goalGid** | **String**| Globally unique identifier for the goal. | 
 **optPretty** | **Boolean**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **optFields** | [**[String]**](String.md)| Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options. | [optional] 

### Return type

[**GetGoals200Response**](GetGoals200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeFollowers

> CreateGoal201Response removeFollowers(goalGid, addFollowersRequest, opts)

Remove a collaborator from a goal

Removes followers from a goal. Returns the goal the followers were removed from. Each goal can be associated with zero or more followers in the system. Requests to add/remove followers, if successful, will return the complete updated goal record, described above.

### Example

```javascript
import Asana from 'asana';
let defaultClient = Asana.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Asana.GoalsApi();
let goalGid = "12345"; // String | Globally unique identifier for the goal.
let addFollowersRequest = new Asana.AddFollowersRequest(); // AddFollowersRequest | The followers to be removed as collaborators
let opts = {
  'optPretty': true, // Boolean | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
  'optFields': ["null"] // [String] | Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
};
apiInstance.removeFollowers(goalGid, addFollowersRequest, opts, (error, data, response) => {
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
 **goalGid** | **String**| Globally unique identifier for the goal. | 
 **addFollowersRequest** | [**AddFollowersRequest**](AddFollowersRequest.md)| The followers to be removed as collaborators | 
 **optPretty** | **Boolean**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **optFields** | [**[String]**](String.md)| Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options. | [optional] 

### Return type

[**CreateGoal201Response**](CreateGoal201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateGoal

> CreateGoal201Response updateGoal(goalGid, createGoalRequest, opts)

Update a goal

An existing goal can be updated by making a PUT request on the URL for that goal. Only the fields provided in the &#x60;data&#x60; block will be updated; any unspecified fields will remain unchanged.  Returns the complete updated goal record.

### Example

```javascript
import Asana from 'asana';
let defaultClient = Asana.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Asana.GoalsApi();
let goalGid = "12345"; // String | Globally unique identifier for the goal.
let createGoalRequest = new Asana.CreateGoalRequest(); // CreateGoalRequest | The updated fields for the goal.
let opts = {
  'optPretty': true, // Boolean | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
  'optFields': ["null"] // [String] | Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
};
apiInstance.updateGoal(goalGid, createGoalRequest, opts, (error, data, response) => {
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
 **goalGid** | **String**| Globally unique identifier for the goal. | 
 **createGoalRequest** | [**CreateGoalRequest**](CreateGoalRequest.md)| The updated fields for the goal. | 
 **optPretty** | **Boolean**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **optFields** | [**[String]**](String.md)| Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options. | [optional] 

### Return type

[**CreateGoal201Response**](CreateGoal201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateGoalMetric

> CreateGoal201Response updateGoalMetric(goalGid, updateGoalMetricRequest, opts)

Update a goal metric

Updates a goal&#39;s existing metric&#39;s &#x60;current_number_value&#x60; if one exists, otherwise responds with a 400 status code.  Returns the complete updated goal metric record.

### Example

```javascript
import Asana from 'asana';
let defaultClient = Asana.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Asana.GoalsApi();
let goalGid = "12345"; // String | Globally unique identifier for the goal.
let updateGoalMetricRequest = new Asana.UpdateGoalMetricRequest(); // UpdateGoalMetricRequest | The updated fields for the goal metric.
let opts = {
  'optPretty': true, // Boolean | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
  'optFields': ["null"] // [String] | Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
};
apiInstance.updateGoalMetric(goalGid, updateGoalMetricRequest, opts, (error, data, response) => {
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
 **goalGid** | **String**| Globally unique identifier for the goal. | 
 **updateGoalMetricRequest** | [**UpdateGoalMetricRequest**](UpdateGoalMetricRequest.md)| The updated fields for the goal metric. | 
 **optPretty** | **Boolean**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **optFields** | [**[String]**](String.md)| Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options. | [optional] 

### Return type

[**CreateGoal201Response**](CreateGoal201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

