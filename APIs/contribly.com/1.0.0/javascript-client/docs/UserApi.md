# Contribly.UserApi

All URIs are relative to *https://api.contribly.com/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersGet**](UserApi.md#usersGet) | **GET** /users | List users
[**usersIdGet**](UserApi.md#usersIdGet) | **GET** /users/{id} | Retrieve a single user by id
[**usersIdLinkedTypeGet**](UserApi.md#usersIdLinkedTypeGet) | **GET** /users/{id}/linked/{type} | Retrieve a users linked profile by type



## usersGet

> [User] usersGet(opts)

List users

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.UserApi();
let opts = {
  'assignment': "assignment_example", // String | Restrict results to the users who have contributed to this assignment.
  'country': "country_example", // String | Restrict results to the users who have submitted a contribution with a public location located within this country.
  'minimumContributions': 3.4, // Number | Restrict results to the users who have submitted at least this many contributions.
  'linkedProfile': "linkedProfile_example", // String | Restrict results to the users who a linked profile of this type.
  'ownedBy': "ownedBy_example", // String | Restrict results to the users who are owned by of this owner.
  'submittedBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Limit results to users who have submitted at least one contribution before this date time.
  'submittedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Limit results to users who have submitted at least one contribution after this date time.
  'username': "username_example" // String | Restrict results to the user with this username.
};
apiInstance.usersGet(opts, (error, data, response) => {
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
 **assignment** | **String**| Restrict results to the users who have contributed to this assignment. | [optional] 
 **country** | **String**| Restrict results to the users who have submitted a contribution with a public location located within this country. | [optional] 
 **minimumContributions** | **Number**| Restrict results to the users who have submitted at least this many contributions. | [optional] 
 **linkedProfile** | **String**| Restrict results to the users who a linked profile of this type. | [optional] 
 **ownedBy** | **String**| Restrict results to the users who are owned by of this owner. | [optional] 
 **submittedBefore** | **Date**| Limit results to users who have submitted at least one contribution before this date time. | [optional] 
 **submittedAfter** | **Date**| Limit results to users who have submitted at least one contribution after this date time. | [optional] 
 **username** | **String**| Restrict results to the user with this username. | [optional] 

### Return type

[**[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdGet

> User usersIdGet(id)

Retrieve a single user by id

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.UserApi();
let id = "id_example"; // String | Id of the user to return
apiInstance.usersIdGet(id, (error, data, response) => {
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
 **id** | **String**| Id of the user to return | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdLinkedTypeGet

> LinkedProfile usersIdLinkedTypeGet(id, type)

Retrieve a users linked profile by type

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.UserApi();
let id = "id_example"; // String | Id of the user to return
let type = "type_example"; // String | Type of the linked profile to fetch
apiInstance.usersIdLinkedTypeGet(id, type, (error, data, response) => {
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
 **id** | **String**| Id of the user to return | 
 **type** | **String**| Type of the linked profile to fetch | 

### Return type

[**LinkedProfile**](LinkedProfile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

