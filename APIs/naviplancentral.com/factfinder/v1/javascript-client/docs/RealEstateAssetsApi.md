# AdvicentFactFinderService.RealEstateAssetsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realEstateAssetsDeleteById**](RealEstateAssetsApi.md#realEstateAssetsDeleteById) | **DELETE** /api/RealEstateAssets/{id} | 
[**realEstateAssetsGetById**](RealEstateAssetsApi.md#realEstateAssetsGetById) | **GET** /api/RealEstateAssets/{id} | 
[**realEstateAssetsGetRealEstateAssetsByFactFinderIdByFactfinderid**](RealEstateAssetsApi.md#realEstateAssetsGetRealEstateAssetsByFactFinderIdByFactfinderid) | **GET** /api/RealEstateAssets | 
[**realEstateAssetsPostByModel**](RealEstateAssetsApi.md#realEstateAssetsPostByModel) | **POST** /api/RealEstateAssets | 
[**realEstateAssetsPutByIdModel**](RealEstateAssetsApi.md#realEstateAssetsPutByIdModel) | **PUT** /api/RealEstateAssets/{id} | 



## realEstateAssetsDeleteById

> realEstateAssetsDeleteById(id)



Description: The operation removes a Real Estate Asset tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Real Estate Asset from a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.RealEstateAssetsApi();
let id = 56; // Number | The Real Estate Asset ID used to identify which Real Estate Asset to remove
apiInstance.realEstateAssetsDeleteById(id, (error, data, response) => {
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
 **id** | **Number**| The Real Estate Asset ID used to identify which Real Estate Asset to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realEstateAssetsGetById

> RealEstateAssetWithIdModel realEstateAssetsGetById(id)



Description: This operation retrieves a single Real Estate Asset for the specified Real Estate Asset ID.&lt;br /&gt;                Purpose: Provides access to the Real Estate Asset including description and market value.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.RealEstateAssetsApi();
let id = 56; // Number | The ID of the Real Estate Asset used to retreive the Real Estate Asset
apiInstance.realEstateAssetsGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the Real Estate Asset used to retreive the Real Estate Asset | 

### Return type

[**RealEstateAssetWithIdModel**](RealEstateAssetWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## realEstateAssetsGetRealEstateAssetsByFactFinderIdByFactfinderid

> RealEstateAssetsModel realEstateAssetsGetRealEstateAssetsByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Real Estate Assets for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Real Estate Assets including description and market value.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.RealEstateAssetsApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Real Estate Assets
apiInstance.realEstateAssetsGetRealEstateAssetsByFactFinderIdByFactfinderid(factFinderId, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to retrieve Real Estate Assets | 

### Return type

[**RealEstateAssetsModel**](RealEstateAssetsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## realEstateAssetsPostByModel

> RealEstateAssetWithIdModel realEstateAssetsPostByModel(model)



Description: The operation creates a Real Estate Asset.&lt;br /&gt;                Purpose: Allows for creation of Real Estate Assets on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.RealEstateAssetsApi();
let model = new AdvicentFactFinderService.RealEstateAssetModel(); // RealEstateAssetModel | The Real Estate Asset to be added to the Fact Finder
apiInstance.realEstateAssetsPostByModel(model, (error, data, response) => {
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
 **model** | [**RealEstateAssetModel**](RealEstateAssetModel.md)| The Real Estate Asset to be added to the Fact Finder | 

### Return type

[**RealEstateAssetWithIdModel**](RealEstateAssetWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## realEstateAssetsPutByIdModel

> RealEstateAssetWithIdModel realEstateAssetsPutByIdModel(id, model)



Description: The operation updates a Real Estate Asset.&lt;br /&gt;                Purpose: Allows for complete replacement of a Real Estate Asset on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.RealEstateAssetsApi();
let id = 56; // Number | The existing Real Estate Asset ID used to identify which Real Estate Asset to update
let model = new AdvicentFactFinderService.RealEstateAssetModel(); // RealEstateAssetModel | The Real Estate Asset to be updated on a Fact Finder
apiInstance.realEstateAssetsPutByIdModel(id, model, (error, data, response) => {
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
 **id** | **Number**| The existing Real Estate Asset ID used to identify which Real Estate Asset to update | 
 **model** | [**RealEstateAssetModel**](RealEstateAssetModel.md)| The Real Estate Asset to be updated on a Fact Finder | 

### Return type

[**RealEstateAssetWithIdModel**](RealEstateAssetWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

