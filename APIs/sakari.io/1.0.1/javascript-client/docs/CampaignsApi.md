# Sakari.CampaignsApi

All URIs are relative to *https://api.sakari.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**campaignsCreate**](CampaignsApi.md#campaignsCreate) | **POST** /v1/accounts/{accountId}/campaigns | Create campaign
[**campaignsFetch**](CampaignsApi.md#campaignsFetch) | **GET** /v1/accounts/{accountId}/campaigns/{campaignId} | Fetch campaign by ID
[**campaignsFetchAll**](CampaignsApi.md#campaignsFetchAll) | **GET** /v1/accounts/{accountId}/campaigns | Fetch campaigns
[**campaignsRemove**](CampaignsApi.md#campaignsRemove) | **DELETE** /v1/accounts/{accountId}/campaigns/{campaignId} | Deletes a campaign
[**campaignsUpdate**](CampaignsApi.md#campaignsUpdate) | **PUT** /v1/accounts/{accountId}/campaigns/{campaignId} | Updates a campaign



## campaignsCreate

> CampaignResponse campaignsCreate(accountId, opts)

Create campaign

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.CampaignsApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let opts = {
  'campaignRequest': new Sakari.CampaignRequest() // CampaignRequest | 
};
apiInstance.campaignsCreate(accountId, opts, (error, data, response) => {
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
 **accountId** | **String**| Account to apply operations to | 
 **campaignRequest** | [**CampaignRequest**](CampaignRequest.md)|  | [optional] 

### Return type

[**CampaignResponse**](CampaignResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## campaignsFetch

> CampaignResponse campaignsFetch(accountId, campaignId)

Fetch campaign by ID

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.CampaignsApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let campaignId = "campaignId_example"; // String | ID of campaign to return
apiInstance.campaignsFetch(accountId, campaignId, (error, data, response) => {
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
 **accountId** | **String**| Account to apply operations to | 
 **campaignId** | **String**| ID of campaign to return | 

### Return type

[**CampaignResponse**](CampaignResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## campaignsFetchAll

> CampaignsResponse campaignsFetchAll(accountId, opts)

Fetch campaigns

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.CampaignsApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let opts = {
  'offset': 789, // Number | Results to skip when paginating through a result set
  'limit': 789, // Number | Maximum number of results to return
  'name': "name_example" // String | Filter by name or part of
};
apiInstance.campaignsFetchAll(accountId, opts, (error, data, response) => {
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
 **accountId** | **String**| Account to apply operations to | 
 **offset** | **Number**| Results to skip when paginating through a result set | [optional] 
 **limit** | **Number**| Maximum number of results to return | [optional] 
 **name** | **String**| Filter by name or part of | [optional] 

### Return type

[**CampaignsResponse**](CampaignsResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## campaignsRemove

> CampaignsRemove200Response campaignsRemove(accountId, campaignId)

Deletes a campaign

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.CampaignsApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let campaignId = "campaignId_example"; // String | Campaign id to delete
apiInstance.campaignsRemove(accountId, campaignId, (error, data, response) => {
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
 **accountId** | **String**| Account to apply operations to | 
 **campaignId** | **String**| Campaign id to delete | 

### Return type

[**CampaignsRemove200Response**](CampaignsRemove200Response.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## campaignsUpdate

> CampaignResponse campaignsUpdate(accountId, campaignId)

Updates a campaign

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.CampaignsApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let campaignId = "campaignId_example"; // String | ID of campaign
apiInstance.campaignsUpdate(accountId, campaignId, (error, data, response) => {
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
 **accountId** | **String**| Account to apply operations to | 
 **campaignId** | **String**| ID of campaign | 

### Return type

[**CampaignResponse**](CampaignResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

