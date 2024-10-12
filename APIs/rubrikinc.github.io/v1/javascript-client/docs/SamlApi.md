# RubrikRestApi.SamlApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configRubrikSamlMetadata**](SamlApi.md#configRubrikSamlMetadata) | **POST** /saml/rubrik_metadata | Configure and generate Rubrik SAML metadata
[**getSamlSsoStatus**](SamlApi.md#getSamlSsoStatus) | **GET** /saml/sso_status | Check SAML SSO Status
[**makeSamlAuthnRequest**](SamlApi.md#makeSamlAuthnRequest) | **POST** /saml/authn_request/{idp_name} | Make SAML authentication request



## configRubrikSamlMetadata

> RubrikSamlMetadataSummary configRubrikSamlMetadata(rubrikSamlMetadataInfo)

Configure and generate Rubrik SAML metadata

Configure and generate the SAML metadata for this Rubrik cluster. The call returns the download URL for the metadata.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.SamlApi();
let rubrikSamlMetadataInfo = new RubrikRestApi.RubrikSamlMetadataInfo(); // RubrikSamlMetadataInfo | Information for generating Rubrik SAML metadata file.
apiInstance.configRubrikSamlMetadata(rubrikSamlMetadataInfo, (error, data, response) => {
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
 **rubrikSamlMetadataInfo** | [**RubrikSamlMetadataInfo**](RubrikSamlMetadataInfo.md)| Information for generating Rubrik SAML metadata file. | 

### Return type

[**RubrikSamlMetadataSummary**](RubrikSamlMetadataSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSamlSsoStatus

> SamlSsoStatus getSamlSsoStatus()

Check SAML SSO Status

An object that contains two values. A Boolean value that determines whether or not SSO is enabled and an optional String value that indicates the name of the default IdP authentication domain for SSO login. When the boolean value is &#39;true,&#39; SAML SSO is enabled. When the Boolean value is &#39;false,&#39; SAML SSO is disabled.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.SamlApi();
apiInstance.getSamlSsoStatus((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**SamlSsoStatus**](SamlSsoStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## makeSamlAuthnRequest

> SamlSsoAuthnRequestDetail makeSamlAuthnRequest(idpName, opts)

Make SAML authentication request

Make a SAML authentication request for a specified IdP Authentication Domain.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.SamlApi();
let idpName = "idpName_example"; // String | Name of the IdP Authentication Domain to authenticate with.
let opts = {
  'samlSsoAuthnRequestInfo': new RubrikRestApi.SamlSsoAuthnRequestInfo() // SamlSsoAuthnRequestInfo | Additional information associated with a single sign-on (SSO) authentication request.
};
apiInstance.makeSamlAuthnRequest(idpName, opts, (error, data, response) => {
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
 **idpName** | **String**| Name of the IdP Authentication Domain to authenticate with. | 
 **samlSsoAuthnRequestInfo** | [**SamlSsoAuthnRequestInfo**](SamlSsoAuthnRequestInfo.md)| Additional information associated with a single sign-on (SSO) authentication request. | [optional] 

### Return type

[**SamlSsoAuthnRequestDetail**](SamlSsoAuthnRequestDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

