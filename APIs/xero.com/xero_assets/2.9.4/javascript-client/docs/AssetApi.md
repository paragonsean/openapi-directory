# XeroAssetsApi.AssetApi

All URIs are relative to *https://api.xero.com/assets.xro/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAsset**](AssetApi.md#createAsset) | **POST** /Assets | adds a fixed asset
[**createAssetType**](AssetApi.md#createAssetType) | **POST** /AssetTypes | adds a fixed asset type
[**getAssetById**](AssetApi.md#getAssetById) | **GET** /Assets/{id} | Retrieves fixed asset by id
[**getAssetSettings**](AssetApi.md#getAssetSettings) | **GET** /Settings | searches fixed asset settings
[**getAssetTypes**](AssetApi.md#getAssetTypes) | **GET** /AssetTypes | searches fixed asset types
[**getAssets**](AssetApi.md#getAssets) | **GET** /Assets | searches fixed asset



## createAsset

> Asset createAsset(xeroTenantId, asset)

adds a fixed asset

Adds an asset to the system

### Example

```javascript
import XeroAssetsApi from 'xero_assets_api';
let defaultClient = XeroAssetsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAssetsApi.AssetApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let asset = { "assetName":"Computer74863", "assetNumber":"123477544", "purchaseDate":"2020-01-01", "purchasePrice":100.0, "disposalPrice":23.23, "assetStatus":"Draft", "bookDepreciationSetting":{ "depreciationMethod":"StraightLine", "averagingMethod":"ActualDays", "depreciationRate":0.5, "depreciationCalculationMethod":"None" }, "bookDepreciationDetail":{ "currentCapitalGain":5.32, "currentGainLoss":3.88, "depreciationStartDate":"2020-01-02", "costLimit":100.0, "currentAccumDepreciationAmount":2.25 }, "AccountingBookValue":99.5 }; // Asset | Fixed asset you are creating
apiInstance.createAsset(xeroTenantId, asset, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **asset** | [**Asset**](Asset.md)| Fixed asset you are creating | 

### Return type

[**Asset**](Asset.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAssetType

> AssetType createAssetType(xeroTenantId, opts)

adds a fixed asset type

Adds an fixed asset type to the system

### Example

```javascript
import XeroAssetsApi from 'xero_assets_api';
let defaultClient = XeroAssetsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAssetsApi.AssetApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'assetType': { "assetTypeName":"Machinery11004", "fixedAssetAccountId":"3d8d063a-c148-4bb8-8b3c-a5e2ad3b1e82", "depreciationExpenseAccountId":"d1602f69-f900-4616-8d34-90af393fa368", "accumulatedDepreciationAccountId":"9195cadd-8645-41e6-9f67-7bcd421defe8", "bookDepreciationSetting":{ "depreciationMethod":"DiminishingValue100", "averagingMethod":"ActualDays", "depreciationRate":0.05, "depreciationCalculationMethod":"None" } } // AssetType | Asset type to add
};
apiInstance.createAssetType(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **assetType** | [**AssetType**](AssetType.md)| Asset type to add | [optional] 

### Return type

[**AssetType**](AssetType.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAssetById

> Asset getAssetById(xeroTenantId, id)

Retrieves fixed asset by id

By passing in the appropriate asset id, you can search for a specific fixed asset in the system 

### Example

```javascript
import XeroAssetsApi from 'xero_assets_api';
let defaultClient = XeroAssetsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAssetsApi.AssetApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let id = "4f7bcdcb-5ec1-4258-9558-19f662fccdfe"; // String | fixed asset id for single object
apiInstance.getAssetById(xeroTenantId, id, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **id** | **String**| fixed asset id for single object | 

### Return type

[**Asset**](Asset.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAssetSettings

> Setting getAssetSettings(xeroTenantId)

searches fixed asset settings

By passing in the appropriate options, you can search for available fixed asset types in the system

### Example

```javascript
import XeroAssetsApi from 'xero_assets_api';
let defaultClient = XeroAssetsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAssetsApi.AssetApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
apiInstance.getAssetSettings(xeroTenantId, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 

### Return type

[**Setting**](Setting.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAssetTypes

> [AssetType] getAssetTypes(xeroTenantId)

searches fixed asset types

By passing in the appropriate options, you can search for available fixed asset types in the system

### Example

```javascript
import XeroAssetsApi from 'xero_assets_api';
let defaultClient = XeroAssetsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAssetsApi.AssetApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
apiInstance.getAssetTypes(xeroTenantId, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 

### Return type

[**[AssetType]**](AssetType.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAssets

> Assets getAssets(xeroTenantId, status, opts)

searches fixed asset

By passing in the appropriate options, you can search for available fixed asset in the system

### Example

```javascript
import XeroAssetsApi from 'xero_assets_api';
let defaultClient = XeroAssetsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAssetsApi.AssetApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let status = new XeroAssetsApi.AssetStatusQueryParam(); // AssetStatusQueryParam | Required when retrieving a collection of assets. See Asset Status Codes
let opts = {
  'page': 1, // Number | Results are paged. This specifies which page of the results to return. The default page is 1.
  'pageSize': 5, // Number | The number of records returned per page. By default the number of records returned is 10.
  'orderBy': "AssetName", // String | Requests can be ordered by AssetType, AssetName, AssetNumber, PurchaseDate and PurchasePrice. If the asset status is DISPOSED it also allows DisposalDate and DisposalPrice.
  'sortDirection': "ASC", // String | ASC or DESC
  'filterBy': "Company Car" // String | A string that can be used to filter the list to only return assets containing the text. Checks it against the AssetName, AssetNumber, Description and AssetTypeName fields.
};
apiInstance.getAssets(xeroTenantId, status, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **status** | [**AssetStatusQueryParam**](.md)| Required when retrieving a collection of assets. See Asset Status Codes | 
 **page** | **Number**| Results are paged. This specifies which page of the results to return. The default page is 1. | [optional] 
 **pageSize** | **Number**| The number of records returned per page. By default the number of records returned is 10. | [optional] 
 **orderBy** | **String**| Requests can be ordered by AssetType, AssetName, AssetNumber, PurchaseDate and PurchasePrice. If the asset status is DISPOSED it also allows DisposalDate and DisposalPrice. | [optional] 
 **sortDirection** | **String**| ASC or DESC | [optional] 
 **filterBy** | **String**| A string that can be used to filter the list to only return assets containing the text. Checks it against the AssetName, AssetNumber, Description and AssetTypeName fields. | [optional] 

### Return type

[**Assets**](Assets.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

