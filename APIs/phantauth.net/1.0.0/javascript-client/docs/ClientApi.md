# PhantAuth.ClientApi

All URIs are relative to *https://phantauth.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clientClientIdGet**](ClientApi.md#clientClientIdGet) | **GET** /client/{client_id} | Get a Client
[**clientClientIdTokenKindGet**](ClientApi.md#clientClientIdTokenKindGet) | **GET** /client/{client_id}/token/{kind} | Get a Client Token
[**clientPost**](ClientApi.md#clientPost) | **POST** /client | Create a Client Selfie



## clientClientIdGet

> ClientClientIdGet200Response clientClientIdGet(clientId)

Get a Client

Use this endpoint to generate a random client. The client is generated in a deterministic way, on the bases of the client ID given as a path parameter. In the case of identical client IDs, the endpoint will generate the same client object. The properties of the generated client object are randomly generated on the basis of the client ID. In lack of a client ID, all calls generate a different client object to the randomly generated client ID.  By providing an email address as the &#x60;client_id&#x60; parameter, you can customize the client logo by the use of the gravatar associated with the email address.  If the &#x60;client_id&#x60; parameter contains minimum one dot (&#x60;.&#x60;) or space (&#x60; &#x60;) character, the client_name is produced from the parameter, rather than being generated.&#x60;  The result is always a client object. If you want to generate multiple clients in one single step, you can do it by the use of *Fleet* generation. The members of a fleet are clients randomly generated from the fleet name.

### Example

```javascript
import PhantAuth from 'phant_auth';

let apiInstance = new PhantAuth.ClientApi();
let clientId = "clientId_example"; // String | A client ID or email.
apiInstance.clientClientIdGet(clientId, (error, data, response) => {
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
 **clientId** | **String**| A client ID or email. | 

### Return type

[**ClientClientIdGet200Response**](ClientClientIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clientClientIdTokenKindGet

> clientClientIdTokenKindGet(clientId, kind)

Get a Client Token

It is used to generate a OpenID Connect token as a path parameter to a client of a given client ID.  It is primarily used for testing purposes, when, for example, the token from the standard authentication flow is not available to the test code.

### Example

```javascript
import PhantAuth from 'phant_auth';

let apiInstance = new PhantAuth.ClientApi();
let clientId = "clientId_example"; // String | A client ID or email.
let kind = "kind_example"; // String | Token type
apiInstance.clientClientIdTokenKindGet(clientId, kind, (error, data, response) => {
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
 **clientId** | **String**| A client ID or email. | 
 **kind** | **String**| Token type | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## clientPost

> clientPost(opts)

Create a Client Selfie

To create a selfie token from the client data, you need an opaqe string token, which contains the encoded client properties sent in the request. Later, the selfie token can be used as a client ID. In this case, the client data is included in the selfie token, that is, the client properties are taken from the token. By the use of a selfie token, you can use your own client objects in the authentication process.

### Example

```javascript
import PhantAuth from 'phant_auth';

let apiInstance = new PhantAuth.ClientApi();
let opts = {
  'clientPostRequest': new PhantAuth.ClientPostRequest() // ClientPostRequest | 
};
apiInstance.clientPost(opts, (error, data, response) => {
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
 **clientPostRequest** | [**ClientPostRequest**](ClientPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain

