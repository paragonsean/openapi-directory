# AirbyteConfigurationApi.SourceOauthApi

All URIs are relative to *http://airbyte.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**completeSourceOAuth**](SourceOauthApi.md#completeSourceOAuth) | **POST** /v1/source_oauths/complete_oauth | Given a source def ID generate an access/refresh token etc.
[**getSourceOAuthConsent**](SourceOauthApi.md#getSourceOAuthConsent) | **POST** /v1/source_oauths/get_consent_url | Given a source connector definition ID, return the URL to the consent screen where to redirect the user to.
[**setInstancewideSourceOauthParams**](SourceOauthApi.md#setInstancewideSourceOauthParams) | **POST** /v1/source_oauths/oauth_params/create | Sets instancewide variables to be used for the oauth flow when creating this source. When set, these variables will be injected into a connector&#39;s configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company&#39;s Google Ads developer_token, client_id, and client_secret without the user having to know about these variables. 



## completeSourceOAuth

> {String: Object} completeSourceOAuth(completeSourceOauthRequest)

Given a source def ID generate an access/refresh token etc.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceOauthApi();
let completeSourceOauthRequest = new AirbyteConfigurationApi.CompleteSourceOauthRequest(); // CompleteSourceOauthRequest | 
apiInstance.completeSourceOAuth(completeSourceOauthRequest, (error, data, response) => {
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
 **completeSourceOauthRequest** | [**CompleteSourceOauthRequest**](CompleteSourceOauthRequest.md)|  | 

### Return type

**{String: Object}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSourceOAuthConsent

> OAuthConsentRead getSourceOAuthConsent(sourceOauthConsentRequest)

Given a source connector definition ID, return the URL to the consent screen where to redirect the user to.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceOauthApi();
let sourceOauthConsentRequest = new AirbyteConfigurationApi.SourceOauthConsentRequest(); // SourceOauthConsentRequest | 
apiInstance.getSourceOAuthConsent(sourceOauthConsentRequest, (error, data, response) => {
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
 **sourceOauthConsentRequest** | [**SourceOauthConsentRequest**](SourceOauthConsentRequest.md)|  | 

### Return type

[**OAuthConsentRead**](OAuthConsentRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setInstancewideSourceOauthParams

> setInstancewideSourceOauthParams(setInstancewideSourceOauthParamsRequestBody)

Sets instancewide variables to be used for the oauth flow when creating this source. When set, these variables will be injected into a connector&#39;s configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company&#39;s Google Ads developer_token, client_id, and client_secret without the user having to know about these variables. 

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceOauthApi();
let setInstancewideSourceOauthParamsRequestBody = new AirbyteConfigurationApi.SetInstancewideSourceOauthParamsRequestBody(); // SetInstancewideSourceOauthParamsRequestBody | 
apiInstance.setInstancewideSourceOauthParams(setInstancewideSourceOauthParamsRequestBody, (error, data, response) => {
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
 **setInstancewideSourceOauthParamsRequestBody** | [**SetInstancewideSourceOauthParamsRequestBody**](SetInstancewideSourceOauthParamsRequestBody.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

