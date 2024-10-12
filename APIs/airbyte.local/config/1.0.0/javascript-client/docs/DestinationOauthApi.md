# AirbyteConfigurationApi.DestinationOauthApi

All URIs are relative to *http://airbyte.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**completeDestinationOAuth**](DestinationOauthApi.md#completeDestinationOAuth) | **POST** /v1/destination_oauths/complete_oauth | Given a destination def ID generate an access/refresh token etc.
[**getDestinationOAuthConsent**](DestinationOauthApi.md#getDestinationOAuthConsent) | **POST** /v1/destination_oauths/get_consent_url | Given a destination connector definition ID, return the URL to the consent screen where to redirect the user to.
[**setInstancewideDestinationOauthParams**](DestinationOauthApi.md#setInstancewideDestinationOauthParams) | **POST** /v1/destination_oauths/oauth_params/create | Sets instancewide variables to be used for the oauth flow when creating this destination. When set, these variables will be injected into a connector&#39;s configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company&#39;s Google Ads developer_token, client_id, and client_secret without the user having to know about these variables. 



## completeDestinationOAuth

> {String: Object} completeDestinationOAuth(completeDestinationOAuthRequest)

Given a destination def ID generate an access/refresh token etc.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationOauthApi();
let completeDestinationOAuthRequest = new AirbyteConfigurationApi.CompleteDestinationOAuthRequest(); // CompleteDestinationOAuthRequest | 
apiInstance.completeDestinationOAuth(completeDestinationOAuthRequest, (error, data, response) => {
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
 **completeDestinationOAuthRequest** | [**CompleteDestinationOAuthRequest**](CompleteDestinationOAuthRequest.md)|  | 

### Return type

**{String: Object}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getDestinationOAuthConsent

> OAuthConsentRead getDestinationOAuthConsent(destinationOauthConsentRequest)

Given a destination connector definition ID, return the URL to the consent screen where to redirect the user to.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationOauthApi();
let destinationOauthConsentRequest = new AirbyteConfigurationApi.DestinationOauthConsentRequest(); // DestinationOauthConsentRequest | 
apiInstance.getDestinationOAuthConsent(destinationOauthConsentRequest, (error, data, response) => {
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
 **destinationOauthConsentRequest** | [**DestinationOauthConsentRequest**](DestinationOauthConsentRequest.md)|  | 

### Return type

[**OAuthConsentRead**](OAuthConsentRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setInstancewideDestinationOauthParams

> setInstancewideDestinationOauthParams(setInstancewideDestinationOauthParamsRequestBody)

Sets instancewide variables to be used for the oauth flow when creating this destination. When set, these variables will be injected into a connector&#39;s configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company&#39;s Google Ads developer_token, client_id, and client_secret without the user having to know about these variables. 

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationOauthApi();
let setInstancewideDestinationOauthParamsRequestBody = new AirbyteConfigurationApi.SetInstancewideDestinationOauthParamsRequestBody(); // SetInstancewideDestinationOauthParamsRequestBody | 
apiInstance.setInstancewideDestinationOauthParams(setInstancewideDestinationOauthParamsRequestBody, (error, data, response) => {
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
 **setInstancewideDestinationOauthParamsRequestBody** | [**SetInstancewideDestinationOauthParamsRequestBody**](SetInstancewideDestinationOauthParamsRequestBody.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

