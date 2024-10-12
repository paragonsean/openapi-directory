# SearchAds360Api.ConversionApi

All URIs are relative to *https://doubleclicksearch.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**doubleclicksearchConversionGet**](ConversionApi.md#doubleclicksearchConversionGet) | **GET** /doubleclicksearch/v2/agency/{agencyId}/advertiser/{advertiserId}/engine/{engineAccountId}/conversion | 
[**doubleclicksearchConversionGetByCustomerId**](ConversionApi.md#doubleclicksearchConversionGetByCustomerId) | **GET** /doubleclicksearch/v2/customer/{customerId}/conversion | 
[**doubleclicksearchConversionInsert**](ConversionApi.md#doubleclicksearchConversionInsert) | **POST** /doubleclicksearch/v2/conversion | 
[**doubleclicksearchConversionUpdate**](ConversionApi.md#doubleclicksearchConversionUpdate) | **PUT** /doubleclicksearch/v2/conversion | 
[**doubleclicksearchConversionUpdateAvailability**](ConversionApi.md#doubleclicksearchConversionUpdateAvailability) | **POST** /doubleclicksearch/v2/conversion/updateAvailability | 



## doubleclicksearchConversionGet

> ConversionList doubleclicksearchConversionGet(agencyId, advertiserId, engineAccountId, endDate, rowCount, startDate, startRow, opts)



Retrieves a list of conversions from a DoubleClick Search engine account.

### Example

```javascript
import SearchAds360Api from 'search_ads_360_api';
let defaultClient = SearchAds360Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SearchAds360Api.ConversionApi();
let agencyId = "agencyId_example"; // String | Numeric ID of the agency.
let advertiserId = "advertiserId_example"; // String | Numeric ID of the advertiser.
let engineAccountId = "engineAccountId_example"; // String | Numeric ID of the engine account.
let endDate = 56; // Number | Last date (inclusive) on which to retrieve conversions. Format is yyyymmdd.
let rowCount = 56; // Number | The number of conversions to return per call.
let startDate = 56; // Number | First date (inclusive) on which to retrieve conversions. Format is yyyymmdd.
let startRow = 56; // Number | The 0-based starting index for retrieving conversions results.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'adGroupId': "adGroupId_example", // String | Numeric ID of the ad group.
  'adId': "adId_example", // String | Numeric ID of the ad.
  'campaignId': "campaignId_example", // String | Numeric ID of the campaign.
  'criterionId': "criterionId_example", // String | Numeric ID of the criterion.
  'customerId': "customerId_example" // String | Customer ID of a client account in the new Search Ads 360 experience.
};
apiInstance.doubleclicksearchConversionGet(agencyId, advertiserId, engineAccountId, endDate, rowCount, startDate, startRow, opts, (error, data, response) => {
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
 **agencyId** | **String**| Numeric ID of the agency. | 
 **advertiserId** | **String**| Numeric ID of the advertiser. | 
 **engineAccountId** | **String**| Numeric ID of the engine account. | 
 **endDate** | **Number**| Last date (inclusive) on which to retrieve conversions. Format is yyyymmdd. | 
 **rowCount** | **Number**| The number of conversions to return per call. | 
 **startDate** | **Number**| First date (inclusive) on which to retrieve conversions. Format is yyyymmdd. | 
 **startRow** | **Number**| The 0-based starting index for retrieving conversions results. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **adGroupId** | **String**| Numeric ID of the ad group. | [optional] 
 **adId** | **String**| Numeric ID of the ad. | [optional] 
 **campaignId** | **String**| Numeric ID of the campaign. | [optional] 
 **criterionId** | **String**| Numeric ID of the criterion. | [optional] 
 **customerId** | **String**| Customer ID of a client account in the new Search Ads 360 experience. | [optional] 

### Return type

[**ConversionList**](ConversionList.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## doubleclicksearchConversionGetByCustomerId

> ConversionList doubleclicksearchConversionGetByCustomerId(customerId, endDate, rowCount, startDate, startRow, opts)



Retrieves a list of conversions from a DoubleClick Search engine account.

### Example

```javascript
import SearchAds360Api from 'search_ads_360_api';
let defaultClient = SearchAds360Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SearchAds360Api.ConversionApi();
let customerId = "customerId_example"; // String | Customer ID of a client account in the new Search Ads 360 experience.
let endDate = 56; // Number | Last date (inclusive) on which to retrieve conversions. Format is yyyymmdd.
let rowCount = 56; // Number | The number of conversions to return per call.
let startDate = 56; // Number | First date (inclusive) on which to retrieve conversions. Format is yyyymmdd.
let startRow = 56; // Number | The 0-based starting index for retrieving conversions results.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'adGroupId': "adGroupId_example", // String | Numeric ID of the ad group.
  'adId': "adId_example", // String | Numeric ID of the ad.
  'advertiserId': "advertiserId_example", // String | Numeric ID of the advertiser.
  'agencyId': "agencyId_example", // String | Numeric ID of the agency.
  'campaignId': "campaignId_example", // String | Numeric ID of the campaign.
  'criterionId': "criterionId_example", // String | Numeric ID of the criterion.
  'engineAccountId': "engineAccountId_example" // String | Numeric ID of the engine account.
};
apiInstance.doubleclicksearchConversionGetByCustomerId(customerId, endDate, rowCount, startDate, startRow, opts, (error, data, response) => {
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
 **customerId** | **String**| Customer ID of a client account in the new Search Ads 360 experience. | 
 **endDate** | **Number**| Last date (inclusive) on which to retrieve conversions. Format is yyyymmdd. | 
 **rowCount** | **Number**| The number of conversions to return per call. | 
 **startDate** | **Number**| First date (inclusive) on which to retrieve conversions. Format is yyyymmdd. | 
 **startRow** | **Number**| The 0-based starting index for retrieving conversions results. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **adGroupId** | **String**| Numeric ID of the ad group. | [optional] 
 **adId** | **String**| Numeric ID of the ad. | [optional] 
 **advertiserId** | **String**| Numeric ID of the advertiser. | [optional] 
 **agencyId** | **String**| Numeric ID of the agency. | [optional] 
 **campaignId** | **String**| Numeric ID of the campaign. | [optional] 
 **criterionId** | **String**| Numeric ID of the criterion. | [optional] 
 **engineAccountId** | **String**| Numeric ID of the engine account. | [optional] 

### Return type

[**ConversionList**](ConversionList.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## doubleclicksearchConversionInsert

> ConversionList doubleclicksearchConversionInsert(opts)



Inserts a batch of new conversions into DoubleClick Search.

### Example

```javascript
import SearchAds360Api from 'search_ads_360_api';
let defaultClient = SearchAds360Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SearchAds360Api.ConversionApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'conversionList': new SearchAds360Api.ConversionList() // ConversionList | 
};
apiInstance.doubleclicksearchConversionInsert(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **conversionList** | [**ConversionList**](ConversionList.md)|  | [optional] 

### Return type

[**ConversionList**](ConversionList.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## doubleclicksearchConversionUpdate

> ConversionList doubleclicksearchConversionUpdate(opts)



Updates a batch of conversions in DoubleClick Search.

### Example

```javascript
import SearchAds360Api from 'search_ads_360_api';
let defaultClient = SearchAds360Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SearchAds360Api.ConversionApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'conversionList': new SearchAds360Api.ConversionList() // ConversionList | 
};
apiInstance.doubleclicksearchConversionUpdate(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **conversionList** | [**ConversionList**](ConversionList.md)|  | [optional] 

### Return type

[**ConversionList**](ConversionList.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## doubleclicksearchConversionUpdateAvailability

> UpdateAvailabilityResponse doubleclicksearchConversionUpdateAvailability(opts)



Updates the availabilities of a batch of floodlight activities in DoubleClick Search.

### Example

```javascript
import SearchAds360Api from 'search_ads_360_api';
let defaultClient = SearchAds360Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SearchAds360Api.ConversionApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'updateAvailabilityRequest': new SearchAds360Api.UpdateAvailabilityRequest() // UpdateAvailabilityRequest | 
};
apiInstance.doubleclicksearchConversionUpdateAvailability(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **updateAvailabilityRequest** | [**UpdateAvailabilityRequest**](UpdateAvailabilityRequest.md)|  | [optional] 

### Return type

[**UpdateAvailabilityResponse**](UpdateAvailabilityResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

