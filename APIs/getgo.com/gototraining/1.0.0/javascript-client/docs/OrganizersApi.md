# GoToTraining.OrganizersApi

All URIs are relative to *https://api.getgo.com/G2T/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllOrganisers**](OrganizersApi.md#getAllOrganisers) | **GET** /accounts/{accountKey}/organizers | DEPRECATED: Get Organizers



## getAllOrganisers

> [Organizer] getAllOrganisers(authorization, accountKey)

DEPRECATED: Get Organizers

DEPRECATED: Please use the Admin API call &#39;Get all users&#39; instead. For details see https://goto-developer.logmein.com/get-all-users.

### Example

```javascript
import GoToTraining from 'go_to_training';

let apiInstance = new GoToTraining.OrganizersApi();
let authorization = "authorization_example"; // String | Access token
let accountKey = 789; // Number | The key of the multi-user account
apiInstance.getAllOrganisers(authorization, accountKey, (error, data, response) => {
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
 **authorization** | **String**| Access token | 
 **accountKey** | **Number**| The key of the multi-user account | 

### Return type

[**[Organizer]**](Organizer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

