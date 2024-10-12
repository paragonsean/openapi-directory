# ApiDocumentation.AuthenticationApiControllerApi

All URIs are relative to *http://apibeta.uscann.net/apiv1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticateUser**](AuthenticationApiControllerApi.md#authenticateUser) | **POST** /authentication/token | authenticate the user and returns the token
[**forgotPassword**](AuthenticationApiControllerApi.md#forgotPassword) | **POST** /authentication/forgotPassword | forgotPassword
[**register**](AuthenticationApiControllerApi.md#register) | **POST** /authentication/register | register
[**setForgotPassword**](AuthenticationApiControllerApi.md#setForgotPassword) | **POST** /authentication/setForgotPassword | validates the mail token and set new password
[**validateMailToken**](AuthenticationApiControllerApi.md#validateMailToken) | **POST** /authentication/validateMailToken | validates the mail token



## authenticateUser

> JwtResponse authenticateUser(contentType, loginUser)

authenticate the user and returns the token

### Example

```javascript
import ApiDocumentation from 'api_documentation';

let apiInstance = new ApiDocumentation.AuthenticationApiControllerApi();
let contentType = "'application/json'"; // String | 
let loginUser = new ApiDocumentation.LoginUser(); // LoginUser | The LoginUser definition used to returns the token for authentication
apiInstance.authenticateUser(contentType, loginUser, (error, data, response) => {
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
 **contentType** | **String**|  | [default to &#39;application/json&#39;]
 **loginUser** | [**LoginUser**](LoginUser.md)| The LoginUser definition used to returns the token for authentication | 

### Return type

[**JwtResponse**](JwtResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## forgotPassword

> ResponseStatus forgotPassword(contentType, forgotPassword)

forgotPassword

### Example

```javascript
import ApiDocumentation from 'api_documentation';

let apiInstance = new ApiDocumentation.AuthenticationApiControllerApi();
let contentType = "'application/json'"; // String | 
let forgotPassword = new ApiDocumentation.EmailModel(); // EmailModel | The User email used to send email
apiInstance.forgotPassword(contentType, forgotPassword, (error, data, response) => {
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
 **contentType** | **String**|  | [default to &#39;application/json&#39;]
 **forgotPassword** | [**EmailModel**](EmailModel.md)| The User email used to send email | 

### Return type

[**ResponseStatus**](ResponseStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## register

> ResponseStatus register(contentType, register)

register

### Example

```javascript
import ApiDocumentation from 'api_documentation';

let apiInstance = new ApiDocumentation.AuthenticationApiControllerApi();
let contentType = "'application/json'"; // String | 
let register = new ApiDocumentation.RegistrationModel(); // RegistrationModel | The RegistrationForm definition is used to register the customer
apiInstance.register(contentType, register, (error, data, response) => {
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
 **contentType** | **String**|  | [default to &#39;application/json&#39;]
 **register** | [**RegistrationModel**](RegistrationModel.md)| The RegistrationForm definition is used to register the customer | 

### Return type

[**ResponseStatus**](ResponseStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setForgotPassword

> ResponseStatus setForgotPassword(contentType, token)

validates the mail token and set new password

### Example

```javascript
import ApiDocumentation from 'api_documentation';

let apiInstance = new ApiDocumentation.AuthenticationApiControllerApi();
let contentType = "'application/json'"; // String | 
let token = new ApiDocumentation.ForgotMailToken(); // ForgotMailToken | The ForgotMailToken definition used to returns status of password reset
apiInstance.setForgotPassword(contentType, token, (error, data, response) => {
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
 **contentType** | **String**|  | [default to &#39;application/json&#39;]
 **token** | [**ForgotMailToken**](ForgotMailToken.md)| The ForgotMailToken definition used to returns status of password reset | 

### Return type

[**ResponseStatus**](ResponseStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## validateMailToken

> ResponseStatus validateMailToken(contentType, token)

validates the mail token

### Example

```javascript
import ApiDocumentation from 'api_documentation';

let apiInstance = new ApiDocumentation.AuthenticationApiControllerApi();
let contentType = "'application/json'"; // String | 
let token = new ApiDocumentation.MailToken(); // MailToken | The MailToken definition used to returns status of validation
apiInstance.validateMailToken(contentType, token, (error, data, response) => {
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
 **contentType** | **String**|  | [default to &#39;application/json&#39;]
 **token** | [**MailToken**](MailToken.md)| The MailToken definition used to returns status of validation | 

### Return type

[**ResponseStatus**](ResponseStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

