# FigshareApi.OtherApi

All URIs are relative to *https://api.figshare.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categoriesList**](OtherApi.md#categoriesList) | **GET** /categories | Public Categories
[**fileDownload**](OtherApi.md#fileDownload) | **GET** /file/download/{file_id} | Public File Download
[**itemTypesList**](OtherApi.md#itemTypesList) | **GET** /item_types | Item Types
[**licensesList**](OtherApi.md#licensesList) | **GET** /licenses | Public Licenses
[**privateAccount**](OtherApi.md#privateAccount) | **GET** /account | Private Account information
[**privateFundingSearch**](OtherApi.md#privateFundingSearch) | **POST** /account/funding/search | Search Funding
[**privateLicensesList**](OtherApi.md#privateLicensesList) | **GET** /account/licenses | Private Account Licenses



## categoriesList

> [Category] categoriesList()

Public Categories

Returns a list of public categories

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.OtherApi();
apiInstance.categoriesList((error, data, response) => {
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

[**[Category]**](Category.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileDownload

> fileDownload(fileId)

Public File Download

Starts the download of a file

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.OtherApi();
let fileId = 789; // Number | 
apiInstance.fileDownload(fileId, (error, data, response) => {
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
 **fileId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## itemTypesList

> [ItemType] itemTypesList(opts)

Item Types

Returns the list of Item Types of the requested group. If no user is authenticated, returns the item types available for Figshare.

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.OtherApi();
let opts = {
  'groupId': 0 // Number | Identifier of the group for which the item types are requested
};
apiInstance.itemTypesList(opts, (error, data, response) => {
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
 **groupId** | **Number**| Identifier of the group for which the item types are requested | [optional] [default to 0]

### Return type

[**[ItemType]**](ItemType.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## licensesList

> [License] licensesList()

Public Licenses

Returns a list of public licenses

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.OtherApi();
apiInstance.licensesList((error, data, response) => {
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

[**[License]**](License.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateAccount

> Account privateAccount()

Private Account information

Account information for token/personal token

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.OtherApi();
apiInstance.privateAccount((error, data, response) => {
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

[**Account**](Account.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateFundingSearch

> [FundingInformation] privateFundingSearch(opts)

Search Funding

Search for fundings

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.OtherApi();
let opts = {
  'fundingSearch': new FigshareApi.FundingSearch() // FundingSearch | Search Parameters
};
apiInstance.privateFundingSearch(opts, (error, data, response) => {
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
 **fundingSearch** | [**FundingSearch**](FundingSearch.md)| Search Parameters | [optional] 

### Return type

[**[FundingInformation]**](FundingInformation.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateLicensesList

> [License] privateLicensesList()

Private Account Licenses

This is a private endpoint that requires OAuth. It will return a list with figshare public licenses AND licenses defined for account&#39;s institution.

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.OtherApi();
apiInstance.privateLicensesList((error, data, response) => {
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

[**[License]**](License.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

