# ApiDocumentation.AuthenticationApiControllerApi

All URIs are relative to *http://faceidentity-beta.azurewebsites.net/api/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticateUser**](AuthenticationApiControllerApi.md#authenticateUser) | **POST** /authentication/customer/token | Get Token
[**register**](AuthenticationApiControllerApi.md#register) | **POST** /authentication/customer/registration | Customer Registration



## authenticateUser

> JwtResponse authenticateUser(loginUser)

Get Token

### Example

```javascript
import ApiDocumentation from 'api_documentation';

let apiInstance = new ApiDocumentation.AuthenticationApiControllerApi();
let loginUser = new ApiDocumentation.LoginUser(); // LoginUser | The LoginUser definition used to returns the token for authentication
apiInstance.authenticateUser(loginUser, (error, data, response) => {
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
 **loginUser** | [**LoginUser**](LoginUser.md)| The LoginUser definition used to returns the token for authentication | 

### Return type

[**JwtResponse**](JwtResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## register

> ResponseStatus register(register)

Customer Registration

### Example

```javascript
import ApiDocumentation from 'api_documentation';

let apiInstance = new ApiDocumentation.AuthenticationApiControllerApi();
let register = new ApiDocumentation.Customer(); // Customer | The RegistrationForm definition is used to register the customer
apiInstance.register(register, (error, data, response) => {
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
 **register** | [**Customer**](Customer.md)| The RegistrationForm definition is used to register the customer | 

### Return type

[**ResponseStatus**](ResponseStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

