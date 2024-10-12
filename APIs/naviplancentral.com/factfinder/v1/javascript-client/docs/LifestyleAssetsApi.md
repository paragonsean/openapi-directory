# AdvicentFactFinderService.LifestyleAssetsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lifestyleAssetsDeleteById**](LifestyleAssetsApi.md#lifestyleAssetsDeleteById) | **DELETE** /api/LifestyleAssets/{id} | 
[**lifestyleAssetsGetById**](LifestyleAssetsApi.md#lifestyleAssetsGetById) | **GET** /api/LifestyleAssets/{id} | 
[**lifestyleAssetsGetLifestyleAssetsByFactFinderIdByFactfinderid**](LifestyleAssetsApi.md#lifestyleAssetsGetLifestyleAssetsByFactFinderIdByFactfinderid) | **GET** /api/LifestyleAssets | 
[**lifestyleAssetsPostByModel**](LifestyleAssetsApi.md#lifestyleAssetsPostByModel) | **POST** /api/LifestyleAssets | 
[**lifestyleAssetsPutByIdModel**](LifestyleAssetsApi.md#lifestyleAssetsPutByIdModel) | **PUT** /api/LifestyleAssets/{id} | 



## lifestyleAssetsDeleteById

> lifestyleAssetsDeleteById(id)



Description: The operation removes a Lifestyle Asset tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Lifestyle Asset from a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LifestyleAssetsApi();
let id = 56; // Number | The Lifestyle Asset ID used to identify which Lifestyle Asset to remove
apiInstance.lifestyleAssetsDeleteById(id, (error, data, response) => {
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
 **id** | **Number**| The Lifestyle Asset ID used to identify which Lifestyle Asset to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## lifestyleAssetsGetById

> LifestyleAssetWithIdModel lifestyleAssetsGetById(id)



Description: This operation retrieves a single Lifestyle Asset for the specified Lifestyle Asset ID.&lt;br /&gt;                Purpose: Provides access to the Lifestyle Asset including description and market value.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LifestyleAssetsApi();
let id = 56; // Number | The ID of the Lifestyle Asset used to retreive the Lifestyle Asset
apiInstance.lifestyleAssetsGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the Lifestyle Asset used to retreive the Lifestyle Asset | 

### Return type

[**LifestyleAssetWithIdModel**](LifestyleAssetWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## lifestyleAssetsGetLifestyleAssetsByFactFinderIdByFactfinderid

> LifestyleAssetsModel lifestyleAssetsGetLifestyleAssetsByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Lifestyle Assets for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Lifestyle Assets including description and market value.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LifestyleAssetsApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Lifestyle Assets
apiInstance.lifestyleAssetsGetLifestyleAssetsByFactFinderIdByFactfinderid(factFinderId, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to retrieve Lifestyle Assets | 

### Return type

[**LifestyleAssetsModel**](LifestyleAssetsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## lifestyleAssetsPostByModel

> LifestyleAssetWithIdModel lifestyleAssetsPostByModel(model)



Description: The operation creates a Lifestyle Asset.&lt;br /&gt;                Purpose: Allows for creation of Lifestyle Assets on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LifestyleAssetsApi();
let model = new AdvicentFactFinderService.LifestyleAssetModel(); // LifestyleAssetModel | The Lifestyle Asset to be added to the Fact Finder
apiInstance.lifestyleAssetsPostByModel(model, (error, data, response) => {
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
 **model** | [**LifestyleAssetModel**](LifestyleAssetModel.md)| The Lifestyle Asset to be added to the Fact Finder | 

### Return type

[**LifestyleAssetWithIdModel**](LifestyleAssetWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## lifestyleAssetsPutByIdModel

> LifestyleAssetWithIdModel lifestyleAssetsPutByIdModel(id, model)



Description: The operation updates a Lifestyle Asset.&lt;br /&gt;                Purpose: Allows for complete replacement of a Lifestyle Asset on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LifestyleAssetsApi();
let id = 56; // Number | The existing Lifestyle Asset ID used to identify which Lifestyle Asset to update
let model = new AdvicentFactFinderService.LifestyleAssetModel(); // LifestyleAssetModel | The Lifestyle Asset to be updated on a Fact Finder
apiInstance.lifestyleAssetsPutByIdModel(id, model, (error, data, response) => {
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
 **id** | **Number**| The existing Lifestyle Asset ID used to identify which Lifestyle Asset to update | 
 **model** | [**LifestyleAssetModel**](LifestyleAssetModel.md)| The Lifestyle Asset to be updated on a Fact Finder | 

### Return type

[**LifestyleAssetWithIdModel**](LifestyleAssetWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

