# CleverCloudApi.OauthApi

All URIs are relative to *https://api.clever-cloud.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOauthAuthorize_0**](OauthApi.md#getOauthAuthorize_0) | **GET** /oauth/authorize | 
[**getOauthRights_0**](OauthApi.md#getOauthRights_0) | **GET** /oauth/rights | 
[**oauthAccessTokenQueryPost_0**](OauthApi.md#oauthAccessTokenQueryPost_0) | **POST** /oauth/access_token_query | 
[**oauthRequestTokenQueryPost_0**](OauthApi.md#oauthRequestTokenQueryPost_0) | **POST** /oauth/request_token_query | 
[**postOauthAccessToken_0**](OauthApi.md#postOauthAccessToken_0) | **POST** /oauth/access_token | 
[**postOauthAuthorize_0**](OauthApi.md#postOauthAuthorize_0) | **POST** /oauth/authorize | 
[**postOauthRequestToken_0**](OauthApi.md#postOauthRequestToken_0) | **POST** /oauth/request_token | 



## getOauthAuthorize_0

> getOauthAuthorize_0(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OauthApi();
let opts = {
  'oauthToken': "oauthToken_example", // String | 
  'cookie': "cookie_example" // String | 
};
apiInstance.getOauthAuthorize_0(opts, (error, data, response) => {
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
 **oauthToken** | **String**|  | [optional] 
 **cookie** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOauthRights_0

> Rights getOauthRights_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OauthApi();
apiInstance.getOauthRights_0((error, data, response) => {
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

[**Rights**](Rights.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## oauthAccessTokenQueryPost_0

> oauthAccessTokenQueryPost_0(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OauthApi();
let opts = {
  'oauthConsumerKey': "oauthConsumerKey_example", // String | 
  'oauthToken': "oauthToken_example", // String | 
  'oauthSignatureMethod': "oauthSignatureMethod_example", // String | 
  'oauthSignature': "oauthSignature_example", // String | 
  'oauthTimestamp': "oauthTimestamp_example", // String | 
  'oauthNonce': "oauthNonce_example", // String | 
  'oauthVersion': "oauthVersion_example", // String | 
  'oauthVerifier': "oauthVerifier_example", // String | 
  'oauthCallback': "oauthCallback_example", // String | 
  'oauthTokenSecret': "oauthTokenSecret_example", // String | 
  'oauthCallbackConfirmed': "oauthCallbackConfirmed_example" // String | 
};
apiInstance.oauthAccessTokenQueryPost_0(opts, (error, data, response) => {
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
 **oauthConsumerKey** | **String**|  | [optional] 
 **oauthToken** | **String**|  | [optional] 
 **oauthSignatureMethod** | **String**|  | [optional] 
 **oauthSignature** | **String**|  | [optional] 
 **oauthTimestamp** | **String**|  | [optional] 
 **oauthNonce** | **String**|  | [optional] 
 **oauthVersion** | **String**|  | [optional] 
 **oauthVerifier** | **String**|  | [optional] 
 **oauthCallback** | **String**|  | [optional] 
 **oauthTokenSecret** | **String**|  | [optional] 
 **oauthCallbackConfirmed** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## oauthRequestTokenQueryPost_0

> oauthRequestTokenQueryPost_0(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OauthApi();
let opts = {
  'oauthConsumerKey': "oauthConsumerKey_example", // String | 
  'oauthToken': "oauthToken_example", // String | 
  'oauthSignatureMethod': "oauthSignatureMethod_example", // String | 
  'oauthSignature': "oauthSignature_example", // String | 
  'oauthTimestamp': "oauthTimestamp_example", // String | 
  'oauthNonce': "oauthNonce_example", // String | 
  'oauthVersion': "oauthVersion_example", // String | 
  'oauthVerifier': "oauthVerifier_example", // String | 
  'oauthCallback': "oauthCallback_example", // String | 
  'oauthTokenSecret': "oauthTokenSecret_example", // String | 
  'oauthCallbackConfirmed': "oauthCallbackConfirmed_example" // String | 
};
apiInstance.oauthRequestTokenQueryPost_0(opts, (error, data, response) => {
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
 **oauthConsumerKey** | **String**|  | [optional] 
 **oauthToken** | **String**|  | [optional] 
 **oauthSignatureMethod** | **String**|  | [optional] 
 **oauthSignature** | **String**|  | [optional] 
 **oauthTimestamp** | **String**|  | [optional] 
 **oauthNonce** | **String**|  | [optional] 
 **oauthVersion** | **String**|  | [optional] 
 **oauthVerifier** | **String**|  | [optional] 
 **oauthCallback** | **String**|  | [optional] 
 **oauthTokenSecret** | **String**|  | [optional] 
 **oauthCallbackConfirmed** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postOauthAccessToken_0

> postOauthAccessToken_0(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OauthApi();
let opts = {
  'oauthConsumerKey': "oauthConsumerKey_example", // String | 
  'oauthToken': "oauthToken_example", // String | 
  'oauthSignatureMethod': "oauthSignatureMethod_example", // String | 
  'oauthSignature': "oauthSignature_example", // String | 
  'oauthTimestamp': "oauthTimestamp_example", // String | 
  'oauthNonce': "oauthNonce_example", // String | 
  'oauthVersion': "oauthVersion_example", // String | 
  'oauthVerifier': "oauthVerifier_example", // String | 
  'oauthCallback': "oauthCallback_example", // String | 
  'oauthTokenSecret': "oauthTokenSecret_example", // String | 
  'oauthCallbackConfirmed': "oauthCallbackConfirmed_example" // String | 
};
apiInstance.postOauthAccessToken_0(opts, (error, data, response) => {
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
 **oauthConsumerKey** | **String**|  | [optional] 
 **oauthToken** | **String**|  | [optional] 
 **oauthSignatureMethod** | **String**|  | [optional] 
 **oauthSignature** | **String**|  | [optional] 
 **oauthTimestamp** | **String**|  | [optional] 
 **oauthNonce** | **String**|  | [optional] 
 **oauthVersion** | **String**|  | [optional] 
 **oauthVerifier** | **String**|  | [optional] 
 **oauthCallback** | **String**|  | [optional] 
 **oauthTokenSecret** | **String**|  | [optional] 
 **oauthCallbackConfirmed** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postOauthAuthorize_0

> postOauthAuthorize_0(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OauthApi();
let opts = {
  'almighty': "almighty_example", // String | 
  'accessOrganisations': "accessOrganisations_example", // String | 
  'manageOrganisations': "manageOrganisations_example", // String | 
  'manageOrganisationsServices': "manageOrganisationsServices_example", // String | 
  'manageOrganisationsApplications': "manageOrganisationsApplications_example", // String | 
  'manageOrganisationsMembers': "manageOrganisationsMembers_example", // String | 
  'accessOrganisationsBills': "accessOrganisationsBills_example", // String | 
  'accessOrganisationsCreditCount': "accessOrganisationsCreditCount_example", // String | 
  'accessOrganisationsConsumptionStatistics': "accessOrganisationsConsumptionStatistics_example", // String | 
  'accessPersonalInformation': "accessPersonalInformation_example", // String | 
  'managePersonalInformation': "managePersonalInformation_example", // String | 
  'manageSshKeys': "manageSshKeys_example", // String | 
  'manageServices': "manageServices_example", // String | 
  'manageApplications': "manageApplications_example", // String | 
  'accessBills': "accessBills_example", // String | 
  'accessCreditCount': "accessCreditCount_example", // String | 
  'accessConsumptionStatistics': "accessConsumptionStatistics_example", // String | 
  'cookie': "cookie_example" // String | 
};
apiInstance.postOauthAuthorize_0(opts, (error, data, response) => {
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
 **almighty** | **String**|  | [optional] 
 **accessOrganisations** | **String**|  | [optional] 
 **manageOrganisations** | **String**|  | [optional] 
 **manageOrganisationsServices** | **String**|  | [optional] 
 **manageOrganisationsApplications** | **String**|  | [optional] 
 **manageOrganisationsMembers** | **String**|  | [optional] 
 **accessOrganisationsBills** | **String**|  | [optional] 
 **accessOrganisationsCreditCount** | **String**|  | [optional] 
 **accessOrganisationsConsumptionStatistics** | **String**|  | [optional] 
 **accessPersonalInformation** | **String**|  | [optional] 
 **managePersonalInformation** | **String**|  | [optional] 
 **manageSshKeys** | **String**|  | [optional] 
 **manageServices** | **String**|  | [optional] 
 **manageApplications** | **String**|  | [optional] 
 **accessBills** | **String**|  | [optional] 
 **accessCreditCount** | **String**|  | [optional] 
 **accessConsumptionStatistics** | **String**|  | [optional] 
 **cookie** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postOauthRequestToken_0

> postOauthRequestToken_0(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.OauthApi();
let opts = {
  'oauthConsumerKey': "oauthConsumerKey_example", // String | 
  'oauthToken': "oauthToken_example", // String | 
  'oauthSignatureMethod': "oauthSignatureMethod_example", // String | 
  'oauthSignature': "oauthSignature_example", // String | 
  'oauthTimestamp': "oauthTimestamp_example", // String | 
  'oauthNonce': "oauthNonce_example", // String | 
  'oauthVersion': "oauthVersion_example", // String | 
  'oauthVerifier': "oauthVerifier_example", // String | 
  'oauthCallback': "oauthCallback_example", // String | 
  'oauthTokenSecret': "oauthTokenSecret_example", // String | 
  'oauthCallbackConfirmed': "oauthCallbackConfirmed_example" // String | 
};
apiInstance.postOauthRequestToken_0(opts, (error, data, response) => {
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
 **oauthConsumerKey** | **String**|  | [optional] 
 **oauthToken** | **String**|  | [optional] 
 **oauthSignatureMethod** | **String**|  | [optional] 
 **oauthSignature** | **String**|  | [optional] 
 **oauthTimestamp** | **String**|  | [optional] 
 **oauthNonce** | **String**|  | [optional] 
 **oauthVersion** | **String**|  | [optional] 
 **oauthVerifier** | **String**|  | [optional] 
 **oauthCallback** | **String**|  | [optional] 
 **oauthTokenSecret** | **String**|  | [optional] 
 **oauthCallbackConfirmed** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

