# TwilioNumbers.NumbersV2BundleApi

All URIs are relative to *https://numbers.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createBundle**](NumbersV2BundleApi.md#createBundle) | **POST** /v2/RegulatoryCompliance/Bundles | 
[**deleteBundle**](NumbersV2BundleApi.md#deleteBundle) | **DELETE** /v2/RegulatoryCompliance/Bundles/{Sid} | 
[**fetchBundle**](NumbersV2BundleApi.md#fetchBundle) | **GET** /v2/RegulatoryCompliance/Bundles/{Sid} | 
[**listBundle**](NumbersV2BundleApi.md#listBundle) | **GET** /v2/RegulatoryCompliance/Bundles | 
[**updateBundle**](NumbersV2BundleApi.md#updateBundle) | **POST** /v2/RegulatoryCompliance/Bundles/{Sid} | 



## createBundle

> NumbersV2RegulatoryComplianceBundle createBundle(email, friendlyName, opts)



Create a new Bundle.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2BundleApi();
let email = "email_example"; // String | The email address that will receive updates when the Bundle resource changes status.
let friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
let opts = {
  'endUserType': "endUserType_example", // BundleEnumEndUserType | 
  'isoCountry': "isoCountry_example", // String | The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Bundle's phone number country ownership request.
  'numberType': "numberType_example", // String | The type of phone number of the Bundle's ownership request. Can be `local`, `mobile`, `national`, or `toll free`.
  'regulationSid': "regulationSid_example", // String | The unique string of a regulation that is associated to the Bundle resource.
  'statusCallback': "statusCallback_example" // String | The URL we call to inform your application of status changes.
};
apiInstance.createBundle(email, friendlyName, opts, (error, data, response) => {
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
 **email** | **String**| The email address that will receive updates when the Bundle resource changes status. | 
 **friendlyName** | **String**| The string that you assigned to describe the resource. | 
 **endUserType** | **BundleEnumEndUserType**|  | [optional] 
 **isoCountry** | **String**| The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Bundle&#39;s phone number country ownership request. | [optional] 
 **numberType** | **String**| The type of phone number of the Bundle&#39;s ownership request. Can be &#x60;local&#x60;, &#x60;mobile&#x60;, &#x60;national&#x60;, or &#x60;toll free&#x60;. | [optional] 
 **regulationSid** | **String**| The unique string of a regulation that is associated to the Bundle resource. | [optional] 
 **statusCallback** | **String**| The URL we call to inform your application of status changes. | [optional] 

### Return type

[**NumbersV2RegulatoryComplianceBundle**](NumbersV2RegulatoryComplianceBundle.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteBundle

> deleteBundle(sid)



Delete a specific Bundle.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2BundleApi();
let sid = "sid_example"; // String | The unique string that we created to identify the Bundle resource.
apiInstance.deleteBundle(sid, (error, data, response) => {
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
 **sid** | **String**| The unique string that we created to identify the Bundle resource. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchBundle

> NumbersV2RegulatoryComplianceBundle fetchBundle(sid)



Fetch a specific Bundle instance.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2BundleApi();
let sid = "sid_example"; // String | The unique string that we created to identify the Bundle resource.
apiInstance.fetchBundle(sid, (error, data, response) => {
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
 **sid** | **String**| The unique string that we created to identify the Bundle resource. | 

### Return type

[**NumbersV2RegulatoryComplianceBundle**](NumbersV2RegulatoryComplianceBundle.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBundle

> ListBundleResponse listBundle(opts)



Retrieve a list of all Bundles for an account.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2BundleApi();
let opts = {
  'status': "status_example", // BundleEnumStatus | The verification status of the Bundle resource. Please refer to [Bundle Statuses](https://www.twilio.com/docs/phone-numbers/regulatory/api/bundles#bundle-statuses) for more details.
  'friendlyName': "friendlyName_example", // String | The string that you assigned to describe the resource. The column can contain 255 variable characters.
  'regulationSid': "regulationSid_example", // String | The unique string of a [Regulation resource](https://www.twilio.com/docs/phone-numbers/regulatory/api/regulations) that is associated to the Bundle resource.
  'isoCountry': "isoCountry_example", // String | The 2-digit [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Bundle's phone number country ownership request.
  'numberType': "numberType_example", // String | The type of phone number of the Bundle's ownership request. Can be `local`, `mobile`, `national`, or `tollfree`.
  'hasValidUntilDate': true, // Boolean | Indicates that the Bundle is a valid Bundle until a specified expiration date.
  'sortBy': "sortBy_example", // BundleEnumSortBy | Can be `valid-until` or `date-updated`. Defaults to `date-created`.
  'sortDirection': "sortDirection_example", // BundleEnumSortDirection | Default is `DESC`. Can be `ASC` or `DESC`.
  'validUntilDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Date to filter Bundles having their `valid_until_date` before or after the specified date. Can be `ValidUntilDate>=` or `ValidUntilDate<=`. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format.
  'validUntilDate2': new Date("2013-10-20T19:20:30+01:00"), // Date | Date to filter Bundles having their `valid_until_date` before or after the specified date. Can be `ValidUntilDate>=` or `ValidUntilDate<=`. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format.
  'validUntilDate3': new Date("2013-10-20T19:20:30+01:00"), // Date | Date to filter Bundles having their `valid_until_date` before or after the specified date. Can be `ValidUntilDate>=` or `ValidUntilDate<=`. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listBundle(opts, (error, data, response) => {
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
 **status** | **BundleEnumStatus**| The verification status of the Bundle resource. Please refer to [Bundle Statuses](https://www.twilio.com/docs/phone-numbers/regulatory/api/bundles#bundle-statuses) for more details. | [optional] 
 **friendlyName** | **String**| The string that you assigned to describe the resource. The column can contain 255 variable characters. | [optional] 
 **regulationSid** | **String**| The unique string of a [Regulation resource](https://www.twilio.com/docs/phone-numbers/regulatory/api/regulations) that is associated to the Bundle resource. | [optional] 
 **isoCountry** | **String**| The 2-digit [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Bundle&#39;s phone number country ownership request. | [optional] 
 **numberType** | **String**| The type of phone number of the Bundle&#39;s ownership request. Can be &#x60;local&#x60;, &#x60;mobile&#x60;, &#x60;national&#x60;, or &#x60;tollfree&#x60;. | [optional] 
 **hasValidUntilDate** | **Boolean**| Indicates that the Bundle is a valid Bundle until a specified expiration date. | [optional] 
 **sortBy** | **BundleEnumSortBy**| Can be &#x60;valid-until&#x60; or &#x60;date-updated&#x60;. Defaults to &#x60;date-created&#x60;. | [optional] 
 **sortDirection** | **BundleEnumSortDirection**| Default is &#x60;DESC&#x60;. Can be &#x60;ASC&#x60; or &#x60;DESC&#x60;. | [optional] 
 **validUntilDate** | **Date**| Date to filter Bundles having their &#x60;valid_until_date&#x60; before or after the specified date. Can be &#x60;ValidUntilDate&gt;&#x3D;&#x60; or &#x60;ValidUntilDate&lt;&#x3D;&#x60;. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format. | [optional] 
 **validUntilDate2** | **Date**| Date to filter Bundles having their &#x60;valid_until_date&#x60; before or after the specified date. Can be &#x60;ValidUntilDate&gt;&#x3D;&#x60; or &#x60;ValidUntilDate&lt;&#x3D;&#x60;. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format. | [optional] 
 **validUntilDate3** | **Date**| Date to filter Bundles having their &#x60;valid_until_date&#x60; before or after the specified date. Can be &#x60;ValidUntilDate&gt;&#x3D;&#x60; or &#x60;ValidUntilDate&lt;&#x3D;&#x60;. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListBundleResponse**](ListBundleResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateBundle

> NumbersV2RegulatoryComplianceBundle updateBundle(sid, opts)



Updates a Bundle in an account.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2BundleApi();
let sid = "sid_example"; // String | The unique string that we created to identify the Bundle resource.
let opts = {
  'email': "email_example", // String | The email address that will receive updates when the Bundle resource changes status.
  'friendlyName': "friendlyName_example", // String | The string that you assigned to describe the resource.
  'status': "status_example", // BundleEnumStatus | 
  'statusCallback': "statusCallback_example" // String | The URL we call to inform your application of status changes.
};
apiInstance.updateBundle(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The unique string that we created to identify the Bundle resource. | 
 **email** | **String**| The email address that will receive updates when the Bundle resource changes status. | [optional] 
 **friendlyName** | **String**| The string that you assigned to describe the resource. | [optional] 
 **status** | **BundleEnumStatus**|  | [optional] 
 **statusCallback** | **String**| The URL we call to inform your application of status changes. | [optional] 

### Return type

[**NumbersV2RegulatoryComplianceBundle**](NumbersV2RegulatoryComplianceBundle.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

