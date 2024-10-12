# TwilioPreview.PreviewMarketplaceInstalledAddOnApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMarketplaceInstalledAddOn**](PreviewMarketplaceInstalledAddOnApi.md#createMarketplaceInstalledAddOn) | **POST** /marketplace/InstalledAddOns | 
[**deleteMarketplaceInstalledAddOn**](PreviewMarketplaceInstalledAddOnApi.md#deleteMarketplaceInstalledAddOn) | **DELETE** /marketplace/InstalledAddOns/{Sid} | 
[**fetchMarketplaceInstalledAddOn**](PreviewMarketplaceInstalledAddOnApi.md#fetchMarketplaceInstalledAddOn) | **GET** /marketplace/InstalledAddOns/{Sid} | 
[**listMarketplaceInstalledAddOn**](PreviewMarketplaceInstalledAddOnApi.md#listMarketplaceInstalledAddOn) | **GET** /marketplace/InstalledAddOns | 
[**updateMarketplaceInstalledAddOn**](PreviewMarketplaceInstalledAddOnApi.md#updateMarketplaceInstalledAddOn) | **POST** /marketplace/InstalledAddOns/{Sid} | 



## createMarketplaceInstalledAddOn

> PreviewMarketplaceInstalledAddOn createMarketplaceInstalledAddOn(acceptTermsOfService, availableAddOnSid, opts)



Install an Add-on for the Account specified.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewMarketplaceInstalledAddOnApi();
let acceptTermsOfService = true; // Boolean | Whether the Terms of Service were accepted.
let availableAddOnSid = "availableAddOnSid_example"; // String | The SID of the AvaliableAddOn to install.
let opts = {
  'configuration': null, // Object | The JSON object that represents the configuration of the new Add-on being installed.
  'uniqueName': "uniqueName_example" // String | An application-defined string that uniquely identifies the resource. This value must be unique within the Account.
};
apiInstance.createMarketplaceInstalledAddOn(acceptTermsOfService, availableAddOnSid, opts, (error, data, response) => {
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
 **acceptTermsOfService** | **Boolean**| Whether the Terms of Service were accepted. | 
 **availableAddOnSid** | **String**| The SID of the AvaliableAddOn to install. | 
 **configuration** | [**Object**](Object.md)| The JSON object that represents the configuration of the new Add-on being installed. | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. This value must be unique within the Account. | [optional] 

### Return type

[**PreviewMarketplaceInstalledAddOn**](PreviewMarketplaceInstalledAddOn.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteMarketplaceInstalledAddOn

> deleteMarketplaceInstalledAddOn(sid)



Remove an Add-on installation from your account

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewMarketplaceInstalledAddOnApi();
let sid = "sid_example"; // String | The SID of the InstalledAddOn resource to delete.
apiInstance.deleteMarketplaceInstalledAddOn(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the InstalledAddOn resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchMarketplaceInstalledAddOn

> PreviewMarketplaceInstalledAddOn fetchMarketplaceInstalledAddOn(sid)



Fetch an instance of an Add-on currently installed on this Account.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewMarketplaceInstalledAddOnApi();
let sid = "sid_example"; // String | The SID of the InstalledAddOn resource to fetch.
apiInstance.fetchMarketplaceInstalledAddOn(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the InstalledAddOn resource to fetch. | 

### Return type

[**PreviewMarketplaceInstalledAddOn**](PreviewMarketplaceInstalledAddOn.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMarketplaceInstalledAddOn

> ListMarketplaceInstalledAddOnResponse listMarketplaceInstalledAddOn(opts)



Retrieve a list of Add-ons currently installed on this Account.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewMarketplaceInstalledAddOnApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listMarketplaceInstalledAddOn(opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListMarketplaceInstalledAddOnResponse**](ListMarketplaceInstalledAddOnResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateMarketplaceInstalledAddOn

> PreviewMarketplaceInstalledAddOn updateMarketplaceInstalledAddOn(sid, opts)



Update an Add-on installation for the Account specified.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewMarketplaceInstalledAddOnApi();
let sid = "sid_example"; // String | The SID of the InstalledAddOn resource to update.
let opts = {
  'configuration': null, // Object | Valid JSON object that conform to the configuration schema exposed by the associated AvailableAddOn resource. This is only required by Add-ons that need to be configured
  'uniqueName': "uniqueName_example" // String | An application-defined string that uniquely identifies the resource. This value must be unique within the Account.
};
apiInstance.updateMarketplaceInstalledAddOn(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The SID of the InstalledAddOn resource to update. | 
 **configuration** | [**Object**](Object.md)| Valid JSON object that conform to the configuration schema exposed by the associated AvailableAddOn resource. This is only required by Add-ons that need to be configured | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. This value must be unique within the Account. | [optional] 

### Return type

[**PreviewMarketplaceInstalledAddOn**](PreviewMarketplaceInstalledAddOn.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

