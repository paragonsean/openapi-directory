# AdvicentFactFinderService.AccountsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsDeleteAccountById**](AccountsApi.md#accountsDeleteAccountById) | **DELETE** /api/Accounts/{id} | 
[**accountsDeleteAccountHoldingByAccountidId**](AccountsApi.md#accountsDeleteAccountHoldingByAccountidId) | **DELETE** /api/Accounts/{accountId}/Holdings/{id} | 
[**accountsDeleteSavingsStrategiesByAccountid**](AccountsApi.md#accountsDeleteSavingsStrategiesByAccountid) | **DELETE** /api/Accounts/{accountId}/SavingsStrategies | 
[**accountsDeleteSavingsStrategyByAccountidId**](AccountsApi.md#accountsDeleteSavingsStrategyByAccountidId) | **DELETE** /api/Accounts/{accountId}/SavingsStrategies/{id} | 
[**accountsGetAccountHoldingByAccountidId**](AccountsApi.md#accountsGetAccountHoldingByAccountidId) | **GET** /api/Accounts/{accountId}/Holdings/{id} | 
[**accountsGetAccountHoldingsByAccountid**](AccountsApi.md#accountsGetAccountHoldingsByAccountid) | **GET** /api/Accounts/{accountId}/Holdings | 
[**accountsGetAccountsByFactFinderIdByFactfinderidExternalsourceid**](AccountsApi.md#accountsGetAccountsByFactFinderIdByFactfinderidExternalsourceid) | **GET** /api/Accounts | 
[**accountsGetById**](AccountsApi.md#accountsGetById) | **GET** /api/Accounts/{id} | 
[**accountsGetSavingsStrategiesByAccountIdAndSavingsStrategyIdByAccountidId**](AccountsApi.md#accountsGetSavingsStrategiesByAccountIdAndSavingsStrategyIdByAccountidId) | **GET** /api/Accounts/{accountId}/SavingsStrategies/{id} | 
[**accountsGetSavingsStrategiesByAccountIdByAccountid**](AccountsApi.md#accountsGetSavingsStrategiesByAccountIdByAccountid) | **GET** /api/Accounts/{accountId}/SavingsStrategies | 
[**accountsPostAccountHoldingByAccountidModel**](AccountsApi.md#accountsPostAccountHoldingByAccountidModel) | **POST** /api/Accounts/{accountId}/Holdings | 
[**accountsPostByModel**](AccountsApi.md#accountsPostByModel) | **POST** /api/Accounts | 
[**accountsPostSavingsStrategyByAccountidSavingsstrategy**](AccountsApi.md#accountsPostSavingsStrategyByAccountidSavingsstrategy) | **POST** /api/Accounts/{accountId}/SavingsStrategies | 
[**accountsPutByAccountidIdHolding**](AccountsApi.md#accountsPutByAccountidIdHolding) | **PUT** /api/Accounts/{accountId}/Holdings/{id} | 
[**accountsPutByIdModel**](AccountsApi.md#accountsPutByIdModel) | **PUT** /api/Accounts/{id} | 
[**accountsPutHoldingsByAccountidHoldings**](AccountsApi.md#accountsPutHoldingsByAccountidHoldings) | **PUT** /api/Accounts/{accountId}/Holdings | 
[**accountsPutSavingsStrategyByAccountidIdSavingsstrategy**](AccountsApi.md#accountsPutSavingsStrategyByAccountidIdSavingsstrategy) | **PUT** /api/Accounts/{accountId}/SavingsStrategies/{id} | 



## accountsDeleteAccountById

> accountsDeleteAccountById(id)



Description: The operation removes an Account tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of an Account from a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.AccountsApi();
let id = 56; // Number | The Account ID used to identify which Account to remove
apiInstance.accountsDeleteAccountById(id, (error, data, response) => {
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
 **id** | **Number**| The Account ID used to identify which Account to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## accountsDeleteAccountHoldingByAccountidId

> accountsDeleteAccountHoldingByAccountidId(accountId, id)



Description: This operation deletes a single Account Holding for the specified Account Holding ID and Account ID.&lt;br /&gt;                Purpose: Provides the ability to remove individual holdings from a specified Account.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.AccountsApi();
let accountId = 56; // Number | The ID of the Account used to retrieve the Account data that the specified holding belongs to.
let id = 56; // Number | The ID of the Account Holding used to delete the Account Holding
apiInstance.accountsDeleteAccountHoldingByAccountidId(accountId, id, (error, data, response) => {
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
 **accountId** | **Number**| The ID of the Account used to retrieve the Account data that the specified holding belongs to. | 
 **id** | **Number**| The ID of the Account Holding used to delete the Account Holding | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## accountsDeleteSavingsStrategiesByAccountid

> accountsDeleteSavingsStrategiesByAccountid(accountId)



Deletes all savings strategies tied to an account

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.AccountsApi();
let accountId = 56; // Number | Id of the account that holds the savings strategies
apiInstance.accountsDeleteSavingsStrategiesByAccountid(accountId, (error, data, response) => {
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
 **accountId** | **Number**| Id of the account that holds the savings strategies | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## accountsDeleteSavingsStrategyByAccountidId

> accountsDeleteSavingsStrategyByAccountidId(accountId, id)



Deletes a specific savings strategy

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.AccountsApi();
let accountId = 56; // Number | Id of the account that holds the savings strategy
let id = 56; // Number | Id of the savings strategy to be deleted
apiInstance.accountsDeleteSavingsStrategyByAccountidId(accountId, id, (error, data, response) => {
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
 **accountId** | **Number**| Id of the account that holds the savings strategy | 
 **id** | **Number**| Id of the savings strategy to be deleted | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## accountsGetAccountHoldingByAccountidId

> AccountHoldingWithIdModel accountsGetAccountHoldingByAccountidId(accountId, id)



Description: This operation retrieves a single Account Holding for the specified Account Holding ID and Account ID.&lt;br /&gt;                Purpose: Provides access to the Account Holding information including description and market value.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.AccountsApi();
let accountId = 56; // Number | The ID of the Account used to retrieve the Account Holding data
let id = 56; // Number | The ID of the Account Holding used to retrieve the Account Holding data
apiInstance.accountsGetAccountHoldingByAccountidId(accountId, id, (error, data, response) => {
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
 **accountId** | **Number**| The ID of the Account used to retrieve the Account Holding data | 
 **id** | **Number**| The ID of the Account Holding used to retrieve the Account Holding data | 

### Return type

[**AccountHoldingWithIdModel**](AccountHoldingWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## accountsGetAccountHoldingsByAccountid

> AccountHoldingsModel accountsGetAccountHoldingsByAccountid(accountId)



Retrieves all holdings in the specified Account.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.AccountsApi();
let accountId = 56; // Number | The ID of the Account used to retrieve the Account Holding data
apiInstance.accountsGetAccountHoldingsByAccountid(accountId, (error, data, response) => {
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
 **accountId** | **Number**| The ID of the Account used to retrieve the Account Holding data | 

### Return type

[**AccountHoldingsModel**](AccountHoldingsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## accountsGetAccountsByFactFinderIdByFactfinderidExternalsourceid

> AccountsModel accountsGetAccountsByFactFinderIdByFactfinderidExternalsourceid(factFinderId, opts)



Description: This operation retrieves all Accounts for the specified Fact Finder ID and/or external source ID.&lt;br /&gt;                Purpose: Provides access to the Account information including description and market value.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.AccountsApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Accounts
let opts = {
  'externalSourceId': "externalSourceId_example" // String | The external ID used to filter Accounts
};
apiInstance.accountsGetAccountsByFactFinderIdByFactfinderidExternalsourceid(factFinderId, opts, (error, data, response) => {
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

[**AccountsModel**](AccountsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## accountsGetById

> AccountWithIdModel accountsGetById(id)



Description: This operation retrieves a single Account for the specified Account ID.&lt;br /&gt;                Purpose: Provides access to the Account information including description and market value.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.AccountsApi();
let id = 56; // Number | The ID of the Account used to retrieve the Account data
apiInstance.accountsGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the Account used to retrieve the Account data | 

### Return type

[**AccountWithIdModel**](AccountWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## accountsGetSavingsStrategiesByAccountIdAndSavingsStrategyIdByAccountidId

> SavingsStrategyWithIdModel accountsGetSavingsStrategiesByAccountIdAndSavingsStrategyIdByAccountidId(accountId, id)



Get a specific savings strategy for an account

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.AccountsApi();
let accountId = 56; // Number | The id of the account to retrieve the savings strategies from
let id = 56; // Number | The id of the savings strategy to get
apiInstance.accountsGetSavingsStrategiesByAccountIdAndSavingsStrategyIdByAccountidId(accountId, id, (error, data, response) => {
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
 **accountId** | **Number**| The id of the account to retrieve the savings strategies from | 
 **id** | **Number**| The id of the savings strategy to get | 

### Return type

[**SavingsStrategyWithIdModel**](SavingsStrategyWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## accountsGetSavingsStrategiesByAccountIdByAccountid

> SavingsStrategiesModel accountsGetSavingsStrategiesByAccountIdByAccountid(accountId)



Get all of the savings strategies for a specific account

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.AccountsApi();
let accountId = 56; // Number | The id of the account to retrieve the savings strategies from
apiInstance.accountsGetSavingsStrategiesByAccountIdByAccountid(accountId, (error, data, response) => {
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
 **accountId** | **Number**| The id of the account to retrieve the savings strategies from | 

### Return type

[**SavingsStrategiesModel**](SavingsStrategiesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## accountsPostAccountHoldingByAccountidModel

> AccountHoldingWithIdModel accountsPostAccountHoldingByAccountidModel(accountId, model)



Creates a holding and adds it to an existing Account.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.AccountsApi();
let accountId = 56; // Number | The existing Account ID used to identify which Account to add the holding to
let model = new AdvicentFactFinderService.AccountHoldingModel(); // AccountHoldingModel | The holding data
apiInstance.accountsPostAccountHoldingByAccountidModel(accountId, model, (error, data, response) => {
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
 **accountId** | **Number**| The existing Account ID used to identify which Account to add the holding to | 
 **model** | [**AccountHoldingModel**](AccountHoldingModel.md)| The holding data | 

### Return type

[**AccountHoldingWithIdModel**](AccountHoldingWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## accountsPostByModel

> AccountWithIdModel accountsPostByModel(model)



Description: The operation creates an Account.&lt;br /&gt;                Purpose: Allows for creation of Accounts on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.AccountsApi();
let model = new AdvicentFactFinderService.AccountModel(); // AccountModel | The Account to be added to the Fact Finder
apiInstance.accountsPostByModel(model, (error, data, response) => {
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
 **model** | [**AccountModel**](AccountModel.md)| The Account to be added to the Fact Finder | 

### Return type

[**AccountWithIdModel**](AccountWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## accountsPostSavingsStrategyByAccountidSavingsstrategy

> SavingsStrategyWithIdModel accountsPostSavingsStrategyByAccountidSavingsstrategy(accountId, savingsStrategy)



Creates a savings strategy on a specific account

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.AccountsApi();
let accountId = 56; // Number | Id of the account to create a savings strategy for
let savingsStrategy = new AdvicentFactFinderService.SavingsStrategyModel(); // SavingsStrategyModel | Values for the strategy to be created
apiInstance.accountsPostSavingsStrategyByAccountidSavingsstrategy(accountId, savingsStrategy, (error, data, response) => {
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
 **accountId** | **Number**| Id of the account to create a savings strategy for | 
 **savingsStrategy** | [**SavingsStrategyModel**](SavingsStrategyModel.md)| Values for the strategy to be created | 

### Return type

[**SavingsStrategyWithIdModel**](SavingsStrategyWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## accountsPutByAccountidIdHolding

> AccountHoldingModel accountsPutByAccountidIdHolding(accountId, id, holding)



Updates a holding associated with an account

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.AccountsApi();
let accountId = 56; // Number | The account with the holding to be updated
let id = 56; // Number | The id of the holding to update
let holding = new AdvicentFactFinderService.AccountHoldingModel(); // AccountHoldingModel | The holding values used to update the current holding
apiInstance.accountsPutByAccountidIdHolding(accountId, id, holding, (error, data, response) => {
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
 **accountId** | **Number**| The account with the holding to be updated | 
 **id** | **Number**| The id of the holding to update | 
 **holding** | [**AccountHoldingModel**](AccountHoldingModel.md)| The holding values used to update the current holding | 

### Return type

[**AccountHoldingModel**](AccountHoldingModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## accountsPutByIdModel

> AccountWithIdModel accountsPutByIdModel(id, model)



Description: The operation updates an Account, deletes associated saving strategies if the account type changes.&lt;br /&gt;                Purpose: Allows for complete replacement of an Account on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.AccountsApi();
let id = 56; // Number | The existing Account ID used to identify which Account to update
let model = new AdvicentFactFinderService.AccountModel(); // AccountModel | The Account to be updated on a Fact Finder
apiInstance.accountsPutByIdModel(id, model, (error, data, response) => {
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
 **id** | **Number**| The existing Account ID used to identify which Account to update | 
 **model** | [**AccountModel**](AccountModel.md)| The Account to be updated on a Fact Finder | 

### Return type

[**AccountWithIdModel**](AccountWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## accountsPutHoldingsByAccountidHoldings

> AccountHoldingsModel accountsPutHoldingsByAccountidHoldings(accountId, holdings)



Updates all holdings associated with an account

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.AccountsApi();
let accountId = 56; // Number | The account with the holding to be updated
let holdings = new AdvicentFactFinderService.AccountHoldingsWithoutIdModel(); // AccountHoldingsWithoutIdModel | The list of holdings for an account
apiInstance.accountsPutHoldingsByAccountidHoldings(accountId, holdings, (error, data, response) => {
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
 **accountId** | **Number**| The account with the holding to be updated | 
 **holdings** | [**AccountHoldingsWithoutIdModel**](AccountHoldingsWithoutIdModel.md)| The list of holdings for an account | 

### Return type

[**AccountHoldingsModel**](AccountHoldingsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## accountsPutSavingsStrategyByAccountidIdSavingsstrategy

> SavingsStrategyWithIdModel accountsPutSavingsStrategyByAccountidIdSavingsstrategy(accountId, id, savingsStrategy)



Updates a specific savings strategy

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.AccountsApi();
let accountId = 56; // Number | Id of the account that holds the savings strategy
let id = 56; // Number | Id of the savings strategy to update
let savingsStrategy = new AdvicentFactFinderService.SavingsStrategyModel(); // SavingsStrategyModel | The model with which to update the savings strategy with
apiInstance.accountsPutSavingsStrategyByAccountidIdSavingsstrategy(accountId, id, savingsStrategy, (error, data, response) => {
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
 **accountId** | **Number**| Id of the account that holds the savings strategy | 
 **id** | **Number**| Id of the savings strategy to update | 
 **savingsStrategy** | [**SavingsStrategyModel**](SavingsStrategyModel.md)| The model with which to update the savings strategy with | 

### Return type

[**SavingsStrategyWithIdModel**](SavingsStrategyWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

