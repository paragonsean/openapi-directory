# TwilioApi.Api20100401AddressApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAddress**](Api20100401AddressApi.md#createAddress) | **POST** /2010-04-01/Accounts/{AccountSid}/Addresses.json | 
[**deleteAddress**](Api20100401AddressApi.md#deleteAddress) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json | 
[**fetchAddress**](Api20100401AddressApi.md#fetchAddress) | **GET** /2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json | 
[**listAddress**](Api20100401AddressApi.md#listAddress) | **GET** /2010-04-01/Accounts/{AccountSid}/Addresses.json | 
[**updateAddress**](Api20100401AddressApi.md#updateAddress) | **POST** /2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json | 



## createAddress

> ApiV2010AccountAddress createAddress(accountSid, city, customerName, isoCountry, postalCode, region, street, opts)





### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AddressApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will be responsible for the new Address resource.
let city = "city_example"; // String | The city of the new address.
let customerName = "customerName_example"; // String | The name to associate with the new address.
let isoCountry = "isoCountry_example"; // String | The ISO country code of the new address.
let postalCode = "postalCode_example"; // String | The postal code of the new address.
let region = "region_example"; // String | The state or region of the new address.
let street = "street_example"; // String | The number and street address of the new address.
let opts = {
  'autoCorrectAddress': true, // Boolean | Whether we should automatically correct the address. Can be: `true` or `false` and the default is `true`. If empty or `true`, we will correct the address you provide if necessary. If `false`, we won't alter the address you provide.
  'emergencyEnabled': true, // Boolean | Whether to enable emergency calling on the new address. Can be: `true` or `false`.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the new address. It can be up to 64 characters long.
  'streetSecondary': "streetSecondary_example" // String | The additional number and street address of the address.
};
apiInstance.createAddress(accountSid, city, customerName, isoCountry, postalCode, region, street, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will be responsible for the new Address resource. | 
 **city** | **String**| The city of the new address. | 
 **customerName** | **String**| The name to associate with the new address. | 
 **isoCountry** | **String**| The ISO country code of the new address. | 
 **postalCode** | **String**| The postal code of the new address. | 
 **region** | **String**| The state or region of the new address. | 
 **street** | **String**| The number and street address of the new address. | 
 **autoCorrectAddress** | **Boolean**| Whether we should automatically correct the address. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. If empty or &#x60;true&#x60;, we will correct the address you provide if necessary. If &#x60;false&#x60;, we won&#39;t alter the address you provide. | [optional] 
 **emergencyEnabled** | **Boolean**| Whether to enable emergency calling on the new address. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the new address. It can be up to 64 characters long. | [optional] 
 **streetSecondary** | **String**| The additional number and street address of the address. | [optional] 

### Return type

[**ApiV2010AccountAddress**](ApiV2010AccountAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteAddress

> deleteAddress(accountSid, sid)





### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AddressApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to delete.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Address resource to delete.
apiInstance.deleteAddress(accountSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to delete. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Address resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchAddress

> ApiV2010AccountAddress fetchAddress(accountSid, sid)





### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AddressApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to fetch.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Address resource to fetch.
apiInstance.fetchAddress(accountSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to fetch. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Address resource to fetch. | 

### Return type

[**ApiV2010AccountAddress**](ApiV2010AccountAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAddress

> ListAddressResponse listAddress(accountSid, opts)





### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AddressApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to read.
let opts = {
  'customerName': "customerName_example", // String | The `customer_name` of the Address resources to read.
  'friendlyName': "friendlyName_example", // String | The string that identifies the Address resources to read.
  'isoCountry': "isoCountry_example", // String | The ISO country code of the Address resources to read.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listAddress(accountSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to read. | 
 **customerName** | **String**| The &#x60;customer_name&#x60; of the Address resources to read. | [optional] 
 **friendlyName** | **String**| The string that identifies the Address resources to read. | [optional] 
 **isoCountry** | **String**| The ISO country code of the Address resources to read. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListAddressResponse**](ListAddressResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAddress

> ApiV2010AccountAddress updateAddress(accountSid, sid, opts)





### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AddressApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to update.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Address resource to update.
let opts = {
  'autoCorrectAddress': true, // Boolean | Whether we should automatically correct the address. Can be: `true` or `false` and the default is `true`. If empty or `true`, we will correct the address you provide if necessary. If `false`, we won't alter the address you provide.
  'city': "city_example", // String | The city of the address.
  'customerName': "customerName_example", // String | The name to associate with the address.
  'emergencyEnabled': true, // Boolean | Whether to enable emergency calling on the address. Can be: `true` or `false`.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the address. It can be up to 64 characters long.
  'postalCode': "postalCode_example", // String | The postal code of the address.
  'region': "region_example", // String | The state or region of the address.
  'street': "street_example", // String | The number and street address of the address.
  'streetSecondary': "streetSecondary_example" // String | The additional number and street address of the address.
};
apiInstance.updateAddress(accountSid, sid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to update. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Address resource to update. | 
 **autoCorrectAddress** | **Boolean**| Whether we should automatically correct the address. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. If empty or &#x60;true&#x60;, we will correct the address you provide if necessary. If &#x60;false&#x60;, we won&#39;t alter the address you provide. | [optional] 
 **city** | **String**| The city of the address. | [optional] 
 **customerName** | **String**| The name to associate with the address. | [optional] 
 **emergencyEnabled** | **Boolean**| Whether to enable emergency calling on the address. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the address. It can be up to 64 characters long. | [optional] 
 **postalCode** | **String**| The postal code of the address. | [optional] 
 **region** | **String**| The state or region of the address. | [optional] 
 **street** | **String**| The number and street address of the address. | [optional] 
 **streetSecondary** | **String**| The additional number and street address of the address. | [optional] 

### Return type

[**ApiV2010AccountAddress**](ApiV2010AccountAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

