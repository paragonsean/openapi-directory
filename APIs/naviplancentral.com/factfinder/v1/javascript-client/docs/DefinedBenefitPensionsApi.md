# AdvicentFactFinderService.DefinedBenefitPensionsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**definedBenefitPensionsDeleteDefinedBenefitPensionById**](DefinedBenefitPensionsApi.md#definedBenefitPensionsDeleteDefinedBenefitPensionById) | **DELETE** /api/DefinedBenefitPensions/{id} | 
[**definedBenefitPensionsGetById**](DefinedBenefitPensionsApi.md#definedBenefitPensionsGetById) | **GET** /api/DefinedBenefitPensions/{id} | 
[**definedBenefitPensionsGetDefinedBenefitPensionsByFactFinderIdByFactfinderid**](DefinedBenefitPensionsApi.md#definedBenefitPensionsGetDefinedBenefitPensionsByFactFinderIdByFactfinderid) | **GET** /api/DefinedBenefitPensions | 
[**definedBenefitPensionsPostByModel**](DefinedBenefitPensionsApi.md#definedBenefitPensionsPostByModel) | **POST** /api/DefinedBenefitPensions | 
[**definedBenefitPensionsPutDefinedBenefitPensionByIdModel**](DefinedBenefitPensionsApi.md#definedBenefitPensionsPutDefinedBenefitPensionByIdModel) | **PUT** /api/DefinedBenefitPensions/{id} | 



## definedBenefitPensionsDeleteDefinedBenefitPensionById

> Object definedBenefitPensionsDeleteDefinedBenefitPensionById(id)



Description: The operation removes a Defined Benefit Pension tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Defined Benefit Pension from a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.DefinedBenefitPensionsApi();
let id = 56; // Number | The Defined Benefit Pension ID used to identify which Defined Benefit Pension to remove
apiInstance.definedBenefitPensionsDeleteDefinedBenefitPensionById(id, (error, data, response) => {
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
 **id** | **Number**| The Defined Benefit Pension ID used to identify which Defined Benefit Pension to remove | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## definedBenefitPensionsGetById

> DefinedBenefitPensionWithIdModel definedBenefitPensionsGetById(id)



Description: This operation retrieves a single Defined Benefit Pension for the specified Defined Benefit Pension ID.&lt;br /&gt;                Purpose: Provides access to the Defined Benefit Pension including description and start date.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.DefinedBenefitPensionsApi();
let id = 56; // Number | The ID of the Defined Benefit Pension used to retreive the Defined Benefit Pension
apiInstance.definedBenefitPensionsGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the Defined Benefit Pension used to retreive the Defined Benefit Pension | 

### Return type

[**DefinedBenefitPensionWithIdModel**](DefinedBenefitPensionWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## definedBenefitPensionsGetDefinedBenefitPensionsByFactFinderIdByFactfinderid

> DefinedBenefitPensionsModel definedBenefitPensionsGetDefinedBenefitPensionsByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Defined Benefit Pensions for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Defined Benefit Pensions including description and start date.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.DefinedBenefitPensionsApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Defined Benefit Pensions
apiInstance.definedBenefitPensionsGetDefinedBenefitPensionsByFactFinderIdByFactfinderid(factFinderId, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to retrieve Defined Benefit Pensions | 

### Return type

[**DefinedBenefitPensionsModel**](DefinedBenefitPensionsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## definedBenefitPensionsPostByModel

> Object definedBenefitPensionsPostByModel(model)



Description: The operation creates a Defined Benefit Pension.&lt;br /&gt;                Purpose: Allows for creation of Defined Benefit Pensions on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.DefinedBenefitPensionsApi();
let model = new AdvicentFactFinderService.DefinedBenefitPensionModel(); // DefinedBenefitPensionModel | The Defined Benefit Pension to be added to the Fact Finder
apiInstance.definedBenefitPensionsPostByModel(model, (error, data, response) => {
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
 **model** | [**DefinedBenefitPensionModel**](DefinedBenefitPensionModel.md)| The Defined Benefit Pension to be added to the Fact Finder | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## definedBenefitPensionsPutDefinedBenefitPensionByIdModel

> DefinedBenefitPensionModel definedBenefitPensionsPutDefinedBenefitPensionByIdModel(id, model)



Description: The operation updates a Defined Benefit Pension.&lt;br /&gt;                Purpose: Allows for complete replacement of a Defined Benefit Pension on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.DefinedBenefitPensionsApi();
let id = 56; // Number | The existing Defined Benefit Pension ID used to identify which Defined Benefit Pension to update
let model = new AdvicentFactFinderService.DefinedBenefitPensionModel(); // DefinedBenefitPensionModel | The Defined Benefit Pension to be updated on a Fact Finder
apiInstance.definedBenefitPensionsPutDefinedBenefitPensionByIdModel(id, model, (error, data, response) => {
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
 **id** | **Number**| The existing Defined Benefit Pension ID used to identify which Defined Benefit Pension to update | 
 **model** | [**DefinedBenefitPensionModel**](DefinedBenefitPensionModel.md)| The Defined Benefit Pension to be updated on a Fact Finder | 

### Return type

[**DefinedBenefitPensionModel**](DefinedBenefitPensionModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

