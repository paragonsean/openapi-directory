# PhantAuth.UserApi

All URIs are relative to *https://phantauth.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userPost**](UserApi.md#userPost) | **POST** /user | Create a User Selfie
[**userUsernameGet**](UserApi.md#userUsernameGet) | **GET** /user/{username} | Get a User
[**userUsernameTokenKindGet**](UserApi.md#userUsernameTokenKindGet) | **GET** /user/{username}/token/{kind} | Get a User Token



## userPost

> userPost(opts)

Create a User Selfie

To create a selfie token from the user data, you need an opaqe string token, which contains the encoded user properties sent in the request. Later, the selfie token can be used as a login name. In this case, the user data is included in the selfie token, that is, the user properties are taken from the token. By the use of a selfie token, you can use your own user objects during the authentication process.  Its use, however, is limited by its relatively large size (more than 100 characters), which exceeds the maximum size of the user name in several systems.

### Example

```javascript
import PhantAuth from 'phant_auth';

let apiInstance = new PhantAuth.UserApi();
let opts = {
  'userPostRequest': new PhantAuth.UserPostRequest() // UserPostRequest | 
};
apiInstance.userPost(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userPostRequest** | [**UserPostRequest**](UserPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain


## userUsernameGet

> UserUsernameGet200Response userUsernameGet(username)

Get a User

Use this endpoint to generate a random user. The user is generated in a deterministic way, on the bases of the user name given as a path parameter. In the case of identical user names, the endpoint will generate the same user object. The properties of the generated user object are randomly generated on the basis of the user name. In lack of a user name, all calls generate a different user object to the randomly generated user name.  By providing an email address as the &#x60;username&#x60; parameter, you can customize the user picture by the use of the gravatar associated with the email address.  If the &#x60;username&#x60; parameter contains at least one dot (&#x60;.&#x60;) or space (&#x60; &#x60;) character, the whole name is produced from the parameter, rather than being generated. In this case, these cahracters play the role of separator between the units of the full name (family name, given name).&#x60;  The result is always a user object. If you want to generate multiple users in one single step, you can do it by the use of *Team* generation. The members of a team are users randomly generated from the team name.

### Example

```javascript
import PhantAuth from 'phant_auth';

let apiInstance = new PhantAuth.UserApi();
let username = "username_example"; // String | The username or email used for generation purposes.
apiInstance.userUsernameGet(username, (error, data, response) => {
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
 **username** | **String**| The username or email used for generation purposes. | 

### Return type

[**UserUsernameGet200Response**](UserUsernameGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userUsernameTokenKindGet

> userUsernameTokenKindGet(username, kind, opts)

Get a User Token

It is used to generate OpenID Connect tokens as path parameters to a user of a given name.  This method is mainly used in the testing process, when, for example, the token received from the normal authenticaton flow is not available to the test code. Generating an access token, for example, will let you avoid authentication, and immediately call an operation requiring the access token.

### Example

```javascript
import PhantAuth from 'phant_auth';

let apiInstance = new PhantAuth.UserApi();
let username = "username_example"; // String | A username or email.
let kind = "kind_example"; // String | Token type
let opts = {
  'scope': "scope_example" // String | OpenID Connect scope
};
apiInstance.userUsernameTokenKindGet(username, kind, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| A username or email. | 
 **kind** | **String**| Token type | 
 **scope** | **String**| OpenID Connect scope | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

