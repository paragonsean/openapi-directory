# IbmContainersApi.AuthenticationApi

All URIs are relative to *https://containers-api.ng.bluemix.net/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tlskeyGet**](AuthenticationApi.md#tlskeyGet) | **GET** /tlskey | Retrieve the TLS Certificate
[**tlskeyRefreshPut**](AuthenticationApi.md#tlskeyRefreshPut) | **PUT** /tlskey/refresh | Refresh the TLS Certificate



## tlskeyGet

> Certificate tlskeyGet(xAuthToken, xAuthProjectId)

Retrieve the TLS Certificate

This endpoint returns the TLS (Transport Layer Security) certificate to the user (corresponding IBM Containers command: &#x60;cf ic login&#x60;). The TLS certificate is a SSL certificate that is used to authenticate the user&#39;s CLI with the IBM Containers service and to establish a secure communication between the user&#39;s local machine and the container in Bluemix.

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.AuthenticationApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
apiInstance.tlskeyGet(xAuthToken, xAuthProjectId, (error, data, response) => {
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
 **xAuthToken** | **String**| The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token. | 
 **xAuthProjectId** | **String**| The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. | 

### Return type

[**Certificate**](Certificate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tlskeyRefreshPut

> CertificateRefresh tlskeyRefreshPut(xAuthToken, xAuthProjectId)

Refresh the TLS Certificate

This endpoint requests to generate a new TLS (Transport Layer Security) certificate on the server and to update the existing user TLS certificate (corresponding IBM Containers command: &#x60;cf ic init&#x60;).

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.AuthenticationApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token. 
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
apiInstance.tlskeyRefreshPut(xAuthToken, xAuthProjectId, (error, data, response) => {
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
 **xAuthToken** | **String**| The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.  | 
 **xAuthProjectId** | **String**| The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. | 

### Return type

[**CertificateRefresh**](CertificateRefresh.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

