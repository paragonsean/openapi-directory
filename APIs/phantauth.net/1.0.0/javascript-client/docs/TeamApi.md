# PhantAuth.TeamApi

All URIs are relative to *https://phantauth.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teamTeamnameGet**](TeamApi.md#teamTeamnameGet) | **GET** /team/{teamname} | Get a Team



## teamTeamnameGet

> TeamTeamnameGet200Response teamTeamnameGet(teamname)

Get a Team

Use this endpoint to generate a random group of users. The team is generated in a deterministic way, on the basis of the team name given as the path parameter. In the case of identical team names, the endpoint will generate the same team object. The properties of the generated team object are randomly generated on the basis of the team name. In lack of a team name, all calls generate a different team object to the randomly generated team name.

### Example

```javascript
import PhantAuth from 'phant_auth';

let apiInstance = new PhantAuth.TeamApi();
let teamname = "teamname_example"; // String |  The identifier or email address of the team; it is integrated in the `sub` property and is the basis of the other generated properties. 
apiInstance.teamTeamnameGet(teamname, (error, data, response) => {
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
 **teamname** | **String**|  The identifier or email address of the team; it is integrated in the &#x60;sub&#x60; property and is the basis of the other generated properties.  | 

### Return type

[**TeamTeamnameGet200Response**](TeamTeamnameGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

