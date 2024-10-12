# AdvicentFactFinderService.LiabilitiesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**liabilitiesDeleteById**](LiabilitiesApi.md#liabilitiesDeleteById) | **DELETE** /api/Liabilities/{id} | 
[**liabilitiesGetById**](LiabilitiesApi.md#liabilitiesGetById) | **GET** /api/Liabilities/{id} | 
[**liabilitiesGetLiabilitiesByFactFinderIdByFactfinderidExternalsourceid**](LiabilitiesApi.md#liabilitiesGetLiabilitiesByFactFinderIdByFactfinderidExternalsourceid) | **GET** /api/Liabilities | 
[**liabilitiesPostByModel**](LiabilitiesApi.md#liabilitiesPostByModel) | **POST** /api/Liabilities | 
[**liabilitiesPutByIdModel**](LiabilitiesApi.md#liabilitiesPutByIdModel) | **PUT** /api/Liabilities/{id} | 



## liabilitiesDeleteById

> liabilitiesDeleteById(id)



Description: The operation removes a Liability tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Liability from a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LiabilitiesApi();
let id = 56; // Number | The Liability ID used to identify which Liability to remove
apiInstance.liabilitiesDeleteById(id, (error, data, response) => {
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
 **id** | **Number**| The Liability ID used to identify which Liability to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## liabilitiesGetById

> LiabilityWithIdModel liabilitiesGetById(id)



Description: This operation retrieves a single Liability for the specified Liability ID.&lt;br /&gt;                Purpose: Provides access to the Liability including owner and type.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LiabilitiesApi();
let id = 56; // Number | The ID of the Liability used to retreive the Liability
apiInstance.liabilitiesGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the Liability used to retreive the Liability | 

### Return type

[**LiabilityWithIdModel**](LiabilityWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## liabilitiesGetLiabilitiesByFactFinderIdByFactfinderidExternalsourceid

> LiabilitiesModel liabilitiesGetLiabilitiesByFactFinderIdByFactfinderidExternalsourceid(factFinderId, opts)



Description: This operation retrieves all Liabilities for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Liabilities including owner and type.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LiabilitiesApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Liabilities
let opts = {
  'externalSourceId': "externalSourceId_example" // String | The external source ID used to filter Liabilities
};
apiInstance.liabilitiesGetLiabilitiesByFactFinderIdByFactfinderidExternalsourceid(factFinderId, opts, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to retrieve Liabilities | 
 **externalSourceId** | **String**| The external source ID used to filter Liabilities | [optional] 

### Return type

[**LiabilitiesModel**](LiabilitiesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## liabilitiesPostByModel

> LiabilityWithIdModel liabilitiesPostByModel(model)



Description: The operation creates a Liability.&lt;br /&gt;                Purpose: Allows for creation of Liabilities on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LiabilitiesApi();
let model = new AdvicentFactFinderService.LiabilityModel(); // LiabilityModel | The Liability to be added to the Fact Finder
apiInstance.liabilitiesPostByModel(model, (error, data, response) => {
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
 **model** | [**LiabilityModel**](LiabilityModel.md)| The Liability to be added to the Fact Finder | 

### Return type

[**LiabilityWithIdModel**](LiabilityWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## liabilitiesPutByIdModel

> LiabilityWithIdModel liabilitiesPutByIdModel(id, model)



Description: The operation updates a Liability.&lt;br /&gt;                Purpose: Allows for complete replacement of a Liability on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.LiabilitiesApi();
let id = 56; // Number | The existing Liability ID used to identify which Liability to update
let model = new AdvicentFactFinderService.LiabilityModel(); // LiabilityModel | The Liability to be updated on a Fact Finder
apiInstance.liabilitiesPutByIdModel(id, model, (error, data, response) => {
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
 **id** | **Number**| The existing Liability ID used to identify which Liability to update | 
 **model** | [**LiabilityModel**](LiabilityModel.md)| The Liability to be updated on a Fact Finder | 

### Return type

[**LiabilityWithIdModel**](LiabilityWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

