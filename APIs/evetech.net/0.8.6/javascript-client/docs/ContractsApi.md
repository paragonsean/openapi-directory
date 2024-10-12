# EveSwaggerInterface.ContractsApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCharactersCharacterIdContracts**](ContractsApi.md#getCharactersCharacterIdContracts) | **GET** /characters/{character_id}/contracts/ | Get contracts
[**getCharactersCharacterIdContractsContractIdBids**](ContractsApi.md#getCharactersCharacterIdContractsContractIdBids) | **GET** /characters/{character_id}/contracts/{contract_id}/bids/ | Get contract bids
[**getCharactersCharacterIdContractsContractIdItems**](ContractsApi.md#getCharactersCharacterIdContractsContractIdItems) | **GET** /characters/{character_id}/contracts/{contract_id}/items/ | Get contract items
[**getContractsPublicBidsContractId**](ContractsApi.md#getContractsPublicBidsContractId) | **GET** /contracts/public/bids/{contract_id}/ | Get public contract bids
[**getContractsPublicItemsContractId**](ContractsApi.md#getContractsPublicItemsContractId) | **GET** /contracts/public/items/{contract_id}/ | Get public contract items
[**getContractsPublicRegionId**](ContractsApi.md#getContractsPublicRegionId) | **GET** /contracts/public/{region_id}/ | Get public contracts
[**getCorporationsCorporationIdContracts**](ContractsApi.md#getCorporationsCorporationIdContracts) | **GET** /corporations/{corporation_id}/contracts/ | Get corporation contracts
[**getCorporationsCorporationIdContractsContractIdBids**](ContractsApi.md#getCorporationsCorporationIdContractsContractIdBids) | **GET** /corporations/{corporation_id}/contracts/{contract_id}/bids/ | Get corporation contract bids
[**getCorporationsCorporationIdContractsContractIdItems**](ContractsApi.md#getCorporationsCorporationIdContractsContractIdItems) | **GET** /corporations/{corporation_id}/contracts/{contract_id}/items/ | Get corporation contract items



## getCharactersCharacterIdContracts

> [GetCharactersCharacterIdContracts200Ok] getCharactersCharacterIdContracts(characterId, opts)

Get contracts

Returns contracts available to a character, only if the character is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is \&quot;in_progress\&quot;.  --- Alternate route: &#x60;/dev/characters/{character_id}/contracts/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/contracts/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/contracts/&#x60;  --- This route is cached for up to 300 seconds

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.ContractsApi();
let characterId = 56; // Number | An EVE character ID
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example", // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
  'page': 1, // Number | Which page of results to return
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.getCharactersCharacterIdContracts(characterId, opts, (error, data, response) => {
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
 **characterId** | **Number**| An EVE character ID | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **Number**| Which page of results to return | [optional] [default to 1]
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

[**[GetCharactersCharacterIdContracts200Ok]**](GetCharactersCharacterIdContracts200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCharactersCharacterIdContractsContractIdBids

> [GetCharactersCharacterIdContractsContractIdBids200Ok] getCharactersCharacterIdContractsContractIdBids(characterId, contractId, opts)

Get contract bids

Lists bids on a particular auction contract  --- Alternate route: &#x60;/dev/characters/{character_id}/contracts/{contract_id}/bids/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/contracts/{contract_id}/bids/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/contracts/{contract_id}/bids/&#x60;  --- This route is cached for up to 300 seconds

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.ContractsApi();
let characterId = 56; // Number | An EVE character ID
let contractId = 56; // Number | ID of a contract
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example", // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.getCharactersCharacterIdContractsContractIdBids(characterId, contractId, opts, (error, data, response) => {
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
 **characterId** | **Number**| An EVE character ID | 
 **contractId** | **Number**| ID of a contract | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

[**[GetCharactersCharacterIdContractsContractIdBids200Ok]**](GetCharactersCharacterIdContractsContractIdBids200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCharactersCharacterIdContractsContractIdItems

> [GetCharactersCharacterIdContractsContractIdItems200Ok] getCharactersCharacterIdContractsContractIdItems(characterId, contractId, opts)

Get contract items

Lists items of a particular contract  --- Alternate route: &#x60;/dev/characters/{character_id}/contracts/{contract_id}/items/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/contracts/{contract_id}/items/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/contracts/{contract_id}/items/&#x60;  --- This route is cached for up to 3600 seconds

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.ContractsApi();
let characterId = 56; // Number | An EVE character ID
let contractId = 56; // Number | ID of a contract
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example", // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.getCharactersCharacterIdContractsContractIdItems(characterId, contractId, opts, (error, data, response) => {
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
 **characterId** | **Number**| An EVE character ID | 
 **contractId** | **Number**| ID of a contract | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

[**[GetCharactersCharacterIdContractsContractIdItems200Ok]**](GetCharactersCharacterIdContractsContractIdItems200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContractsPublicBidsContractId

> [GetContractsPublicBidsContractId200Ok] getContractsPublicBidsContractId(contractId, opts)

Get public contract bids

Lists bids on a public auction contract  --- Alternate route: &#x60;/dev/contracts/public/bids/{contract_id}/&#x60;  Alternate route: &#x60;/legacy/contracts/public/bids/{contract_id}/&#x60;  Alternate route: &#x60;/v1/contracts/public/bids/{contract_id}/&#x60;  --- This route is cached for up to 300 seconds

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';

let apiInstance = new EveSwaggerInterface.ContractsApi();
let contractId = 56; // Number | ID of a contract
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example", // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
  'page': 1 // Number | Which page of results to return
};
apiInstance.getContractsPublicBidsContractId(contractId, opts, (error, data, response) => {
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
 **contractId** | **Number**| ID of a contract | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **Number**| Which page of results to return | [optional] [default to 1]

### Return type

[**[GetContractsPublicBidsContractId200Ok]**](GetContractsPublicBidsContractId200Ok.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContractsPublicItemsContractId

> [GetContractsPublicItemsContractId200Ok] getContractsPublicItemsContractId(contractId, opts)

Get public contract items

Lists items of a public contract  --- Alternate route: &#x60;/dev/contracts/public/items/{contract_id}/&#x60;  Alternate route: &#x60;/legacy/contracts/public/items/{contract_id}/&#x60;  Alternate route: &#x60;/v1/contracts/public/items/{contract_id}/&#x60;  --- This route is cached for up to 3600 seconds

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';

let apiInstance = new EveSwaggerInterface.ContractsApi();
let contractId = 56; // Number | ID of a contract
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example", // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
  'page': 1 // Number | Which page of results to return
};
apiInstance.getContractsPublicItemsContractId(contractId, opts, (error, data, response) => {
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
 **contractId** | **Number**| ID of a contract | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **Number**| Which page of results to return | [optional] [default to 1]

### Return type

[**[GetContractsPublicItemsContractId200Ok]**](GetContractsPublicItemsContractId200Ok.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContractsPublicRegionId

> [GetContractsPublicRegionId200Ok] getContractsPublicRegionId(regionId, opts)

Get public contracts

Returns a paginated list of all public contracts in the given region  --- Alternate route: &#x60;/dev/contracts/public/{region_id}/&#x60;  Alternate route: &#x60;/legacy/contracts/public/{region_id}/&#x60;  Alternate route: &#x60;/v1/contracts/public/{region_id}/&#x60;  --- This route is cached for up to 1800 seconds

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';

let apiInstance = new EveSwaggerInterface.ContractsApi();
let regionId = 56; // Number | An EVE region id
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example", // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
  'page': 1 // Number | Which page of results to return
};
apiInstance.getContractsPublicRegionId(regionId, opts, (error, data, response) => {
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
 **regionId** | **Number**| An EVE region id | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **Number**| Which page of results to return | [optional] [default to 1]

### Return type

[**[GetContractsPublicRegionId200Ok]**](GetContractsPublicRegionId200Ok.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCorporationsCorporationIdContracts

> [GetCorporationsCorporationIdContracts200Ok] getCorporationsCorporationIdContracts(corporationId, opts)

Get corporation contracts

Returns contracts available to a corporation, only if the corporation is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is \&quot;in_progress\&quot;.  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/contracts/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/contracts/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/contracts/&#x60;  --- This route is cached for up to 300 seconds

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.ContractsApi();
let corporationId = 56; // Number | An EVE corporation ID
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example", // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
  'page': 1, // Number | Which page of results to return
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.getCorporationsCorporationIdContracts(corporationId, opts, (error, data, response) => {
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
 **corporationId** | **Number**| An EVE corporation ID | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **Number**| Which page of results to return | [optional] [default to 1]
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

[**[GetCorporationsCorporationIdContracts200Ok]**](GetCorporationsCorporationIdContracts200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCorporationsCorporationIdContractsContractIdBids

> [GetCorporationsCorporationIdContractsContractIdBids200Ok] getCorporationsCorporationIdContractsContractIdBids(contractId, corporationId, opts)

Get corporation contract bids

Lists bids on a particular auction contract  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/contracts/{contract_id}/bids/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/contracts/{contract_id}/bids/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/contracts/{contract_id}/bids/&#x60;  --- This route is cached for up to 3600 seconds

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.ContractsApi();
let contractId = 56; // Number | ID of a contract
let corporationId = 56; // Number | An EVE corporation ID
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example", // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
  'page': 1, // Number | Which page of results to return
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.getCorporationsCorporationIdContractsContractIdBids(contractId, corporationId, opts, (error, data, response) => {
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
 **contractId** | **Number**| ID of a contract | 
 **corporationId** | **Number**| An EVE corporation ID | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **Number**| Which page of results to return | [optional] [default to 1]
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

[**[GetCorporationsCorporationIdContractsContractIdBids200Ok]**](GetCorporationsCorporationIdContractsContractIdBids200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCorporationsCorporationIdContractsContractIdItems

> [GetCorporationsCorporationIdContractsContractIdItems200Ok] getCorporationsCorporationIdContractsContractIdItems(contractId, corporationId, opts)

Get corporation contract items

Lists items of a particular contract  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/contracts/{contract_id}/items/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/contracts/{contract_id}/items/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/contracts/{contract_id}/items/&#x60;  --- This route is cached for up to 3600 seconds

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.ContractsApi();
let contractId = 56; // Number | ID of a contract
let corporationId = 56; // Number | An EVE corporation ID
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example", // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.getCorporationsCorporationIdContractsContractIdItems(contractId, corporationId, opts, (error, data, response) => {
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
 **contractId** | **Number**| ID of a contract | 
 **corporationId** | **Number**| An EVE corporation ID | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

[**[GetCorporationsCorporationIdContractsContractIdItems200Ok]**](GetCorporationsCorporationIdContractsContractIdItems200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

