# AdvicentFactFinderService.PresentationApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**presentationGetAccountsByFactfinderidExternalsourceid**](PresentationApi.md#presentationGetAccountsByFactfinderidExternalsourceid) | **GET** /api/Presentation/Accounts | 
[**presentationGetDemographicOwnersByFactfinderid**](PresentationApi.md#presentationGetDemographicOwnersByFactfinderid) | **GET** /api/Presentation/Demographics/Owners | 
[**presentationGetDemographicRelationships**](PresentationApi.md#presentationGetDemographicRelationships) | **GET** /api/Presentation/Demographics/Relationships | 
[**presentationGetIncomesByFactfinderid**](PresentationApi.md#presentationGetIncomesByFactfinderid) | **GET** /api/Presentation/Incomes | 
[**presentationGetLiabilitiesByFactfinderid**](PresentationApi.md#presentationGetLiabilitiesByFactfinderid) | **GET** /api/Presentation/Liabilities | 
[**presentationGetLifeInsurancePoliciesByFactfinderid**](PresentationApi.md#presentationGetLifeInsurancePoliciesByFactfinderid) | **GET** /api/Presentation/LifeInsurancePolicies | 
[**presentationGetPensionsByFactfinderid**](PresentationApi.md#presentationGetPensionsByFactfinderid) | **GET** /api/Presentation/Pensions | 



## presentationGetAccountsByFactfinderidExternalsourceid

> AccountsWithSubEntitiesModel presentationGetAccountsByFactfinderidExternalsourceid(factFinderId, opts)



Description: This operation retrieves all current Accounts for the specified Fact Finder ID, as well as                             all of the holdings and savings strategies belonging to those accounts.&lt;br /&gt;                Purpose: Provides access to the Accounts in a Fact Finder as well as any sub-entities belonging to them.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.PresentationApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Accounts
let opts = {
  'externalSourceId': "externalSourceId_example" // String | The external ID used to filter Accounts
};
apiInstance.presentationGetAccountsByFactfinderidExternalsourceid(factFinderId, opts, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to retrieve Accounts | 
 **externalSourceId** | **String**| The external ID used to filter Accounts | [optional] 

### Return type

[**AccountsWithSubEntitiesModel**](AccountsWithSubEntitiesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## presentationGetDemographicOwnersByFactfinderid

> OwnersModel presentationGetDemographicOwnersByFactfinderid(factFinderId)



Description: This operation retrieves owner values for the fact finder based on demographics data                Purpose: Provides the list of valid options for owner, student, beneficiary, etc.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.PresentationApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve owners.
apiInstance.presentationGetDemographicOwnersByFactfinderid(factFinderId, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to retrieve owners. | 

### Return type

[**OwnersModel**](OwnersModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## presentationGetDemographicRelationships

> RelationshipTypesModel presentationGetDemographicRelationships()



Description: This operation retrieves all relationship types relevant to demographics.&lt;br /&gt;                Purpose: Provides a list of relationship types organized by whether or not they can be defined as children.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.PresentationApi();
apiInstance.presentationGetDemographicRelationships((error, data, response) => {
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

[**RelationshipTypesModel**](RelationshipTypesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## presentationGetIncomesByFactfinderid

> IncomesModel presentationGetIncomesByFactfinderid(factFinderId)



Description: This operation retrieves all current Incomes for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Incomes in a Fact Finder, filtered by Incomes that are current.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.PresentationApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Incomes
apiInstance.presentationGetIncomesByFactfinderid(factFinderId, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to retrieve Incomes | 

### Return type

[**IncomesModel**](IncomesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## presentationGetLiabilitiesByFactfinderid

> LiabilitiesModel presentationGetLiabilitiesByFactfinderid(factFinderId)



Description: This operation retrieves all current Liabilities for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Liabilities in a Fact Finder, filtered by Liabilities that are current.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.PresentationApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Liabilities
apiInstance.presentationGetLiabilitiesByFactfinderid(factFinderId, (error, data, response) => {
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

### Return type

[**LiabilitiesModel**](LiabilitiesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## presentationGetLifeInsurancePoliciesByFactfinderid

> LifeInsurancePoliciesWithSubEntitiesModel presentationGetLifeInsurancePoliciesByFactfinderid(factFinderId)



Description: This operation retrieves all life insurance policies, including subaccounts if available, for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Life Insurance Policies in a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.PresentationApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Life Insurance Policies.
apiInstance.presentationGetLifeInsurancePoliciesByFactfinderid(factFinderId, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to retrieve Life Insurance Policies. | 

### Return type

[**LifeInsurancePoliciesWithSubEntitiesModel**](LifeInsurancePoliciesWithSubEntitiesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## presentationGetPensionsByFactfinderid

> DefinedBenefitPensionsModel presentationGetPensionsByFactfinderid(factFinderId)



Description: This operation retrieves all future Defined Benefit Pensions for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Pensions in a Fact Finder, filtered by Pensions that are in the future.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.PresentationApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Pensions.
apiInstance.presentationGetPensionsByFactfinderid(factFinderId, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to retrieve Pensions. | 

### Return type

[**DefinedBenefitPensionsModel**](DefinedBenefitPensionsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

