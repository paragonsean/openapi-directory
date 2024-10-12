# EveSwaggerInterface.ContactsApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteCharactersCharacterIdContacts**](ContactsApi.md#deleteCharactersCharacterIdContacts) | **DELETE** /characters/{character_id}/contacts/ | Delete contacts
[**getAlliancesAllianceIdContacts**](ContactsApi.md#getAlliancesAllianceIdContacts) | **GET** /alliances/{alliance_id}/contacts/ | Get alliance contacts
[**getAlliancesAllianceIdContactsLabels**](ContactsApi.md#getAlliancesAllianceIdContactsLabels) | **GET** /alliances/{alliance_id}/contacts/labels/ | Get alliance contact labels
[**getCharactersCharacterIdContacts**](ContactsApi.md#getCharactersCharacterIdContacts) | **GET** /characters/{character_id}/contacts/ | Get contacts
[**getCharactersCharacterIdContactsLabels**](ContactsApi.md#getCharactersCharacterIdContactsLabels) | **GET** /characters/{character_id}/contacts/labels/ | Get contact labels
[**getCorporationsCorporationIdContacts**](ContactsApi.md#getCorporationsCorporationIdContacts) | **GET** /corporations/{corporation_id}/contacts/ | Get corporation contacts
[**getCorporationsCorporationIdContactsLabels**](ContactsApi.md#getCorporationsCorporationIdContactsLabels) | **GET** /corporations/{corporation_id}/contacts/labels/ | Get corporation contact labels
[**postCharactersCharacterIdContacts**](ContactsApi.md#postCharactersCharacterIdContacts) | **POST** /characters/{character_id}/contacts/ | Add contacts
[**putCharactersCharacterIdContacts**](ContactsApi.md#putCharactersCharacterIdContacts) | **PUT** /characters/{character_id}/contacts/ | Edit contacts



## deleteCharactersCharacterIdContacts

> deleteCharactersCharacterIdContacts(characterId, contactIds, opts)

Delete contacts

Bulk delete contacts  --- Alternate route: &#x60;/dev/characters/{character_id}/contacts/&#x60;  Alternate route: &#x60;/v2/characters/{character_id}/contacts/&#x60; 

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.ContactsApi();
let characterId = 56; // Number | An EVE character ID
let contactIds = [null]; // [Number] | A list of contacts to delete
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.deleteCharactersCharacterIdContacts(characterId, contactIds, opts, (error, data, response) => {
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
 **characterId** | **Number**| An EVE character ID | 
 **contactIds** | [**[Number]**](Number.md)| A list of contacts to delete | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAlliancesAllianceIdContacts

> [GetAlliancesAllianceIdContacts200Ok] getAlliancesAllianceIdContacts(allianceId, opts)

Get alliance contacts

Return contacts of an alliance  --- Alternate route: &#x60;/dev/alliances/{alliance_id}/contacts/&#x60;  Alternate route: &#x60;/v2/alliances/{alliance_id}/contacts/&#x60;  --- This route is cached for up to 300 seconds

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.ContactsApi();
let allianceId = 56; // Number | An EVE alliance ID
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example", // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
  'page': 1, // Number | Which page of results to return
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.getAlliancesAllianceIdContacts(allianceId, opts, (error, data, response) => {
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
 **allianceId** | **Number**| An EVE alliance ID | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **Number**| Which page of results to return | [optional] [default to 1]
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

[**[GetAlliancesAllianceIdContacts200Ok]**](GetAlliancesAllianceIdContacts200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAlliancesAllianceIdContactsLabels

> [GetAlliancesAllianceIdContactsLabels200Ok] getAlliancesAllianceIdContactsLabels(allianceId, opts)

Get alliance contact labels

Return custom labels for an alliance&#39;s contacts  --- Alternate route: &#x60;/dev/alliances/{alliance_id}/contacts/labels/&#x60;  Alternate route: &#x60;/legacy/alliances/{alliance_id}/contacts/labels/&#x60;  Alternate route: &#x60;/v1/alliances/{alliance_id}/contacts/labels/&#x60;  --- This route is cached for up to 300 seconds

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.ContactsApi();
let allianceId = 56; // Number | An EVE alliance ID
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example", // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.getAlliancesAllianceIdContactsLabels(allianceId, opts, (error, data, response) => {
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
 **allianceId** | **Number**| An EVE alliance ID | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

[**[GetAlliancesAllianceIdContactsLabels200Ok]**](GetAlliancesAllianceIdContactsLabels200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCharactersCharacterIdContacts

> [GetCharactersCharacterIdContacts200Ok] getCharactersCharacterIdContacts(characterId, opts)

Get contacts

Return contacts of a character  --- Alternate route: &#x60;/dev/characters/{character_id}/contacts/&#x60;  Alternate route: &#x60;/v2/characters/{character_id}/contacts/&#x60;  --- This route is cached for up to 300 seconds

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.ContactsApi();
let characterId = 56; // Number | An EVE character ID
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example", // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
  'page': 1, // Number | Which page of results to return
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.getCharactersCharacterIdContacts(characterId, opts, (error, data, response) => {
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

[**[GetCharactersCharacterIdContacts200Ok]**](GetCharactersCharacterIdContacts200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCharactersCharacterIdContactsLabels

> [GetCharactersCharacterIdContactsLabels200Ok] getCharactersCharacterIdContactsLabels(characterId, opts)

Get contact labels

Return custom labels for a character&#39;s contacts  --- Alternate route: &#x60;/dev/characters/{character_id}/contacts/labels/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/contacts/labels/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/contacts/labels/&#x60;  --- This route is cached for up to 300 seconds

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.ContactsApi();
let characterId = 56; // Number | An EVE character ID
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example", // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.getCharactersCharacterIdContactsLabels(characterId, opts, (error, data, response) => {
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
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

[**[GetCharactersCharacterIdContactsLabels200Ok]**](GetCharactersCharacterIdContactsLabels200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCorporationsCorporationIdContacts

> [GetCorporationsCorporationIdContacts200Ok] getCorporationsCorporationIdContacts(corporationId, opts)

Get corporation contacts

Return contacts of a corporation  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/contacts/&#x60;  Alternate route: &#x60;/v2/corporations/{corporation_id}/contacts/&#x60;  --- This route is cached for up to 300 seconds

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.ContactsApi();
let corporationId = 56; // Number | An EVE corporation ID
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example", // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
  'page': 1, // Number | Which page of results to return
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.getCorporationsCorporationIdContacts(corporationId, opts, (error, data, response) => {
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

[**[GetCorporationsCorporationIdContacts200Ok]**](GetCorporationsCorporationIdContacts200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCorporationsCorporationIdContactsLabels

> [GetCorporationsCorporationIdContactsLabels200Ok] getCorporationsCorporationIdContactsLabels(corporationId, opts)

Get corporation contact labels

Return custom labels for a corporation&#39;s contacts  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/contacts/labels/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/contacts/labels/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/contacts/labels/&#x60;  --- This route is cached for up to 300 seconds

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.ContactsApi();
let corporationId = 56; // Number | An EVE corporation ID
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example", // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.getCorporationsCorporationIdContactsLabels(corporationId, opts, (error, data, response) => {
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
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

[**[GetCorporationsCorporationIdContactsLabels200Ok]**](GetCorporationsCorporationIdContactsLabels200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postCharactersCharacterIdContacts

> [Number] postCharactersCharacterIdContacts(characterId, standing, contactIds, opts)

Add contacts

Bulk add contacts with same settings  --- Alternate route: &#x60;/dev/characters/{character_id}/contacts/&#x60;  Alternate route: &#x60;/v2/characters/{character_id}/contacts/&#x60; 

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.ContactsApi();
let characterId = 56; // Number | An EVE character ID
let standing = 3.4; // Number | Standing for the contact
let contactIds = [null]; // [Number] | A list of contacts
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'labelIds': [null], // [Number] | Add custom labels to the new contact
  'token': "token_example", // String | Access token to use if unable to set a header
  'watched': false // Boolean | Whether the contact should be watched, note this is only effective on characters
};
apiInstance.postCharactersCharacterIdContacts(characterId, standing, contactIds, opts, (error, data, response) => {
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
 **standing** | **Number**| Standing for the contact | 
 **contactIds** | [**[Number]**](Number.md)| A list of contacts | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **labelIds** | [**[Number]**](Number.md)| Add custom labels to the new contact | [optional] 
 **token** | **String**| Access token to use if unable to set a header | [optional] 
 **watched** | **Boolean**| Whether the contact should be watched, note this is only effective on characters | [optional] [default to false]

### Return type

**[Number]**

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putCharactersCharacterIdContacts

> putCharactersCharacterIdContacts(characterId, standing, contactIds, opts)

Edit contacts

Bulk edit contacts with same settings  --- Alternate route: &#x60;/dev/characters/{character_id}/contacts/&#x60;  Alternate route: &#x60;/v2/characters/{character_id}/contacts/&#x60; 

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.ContactsApi();
let characterId = 56; // Number | An EVE character ID
let standing = 3.4; // Number | Standing for the contact
let contactIds = [null]; // [Number] | A list of contacts
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'labelIds': [null], // [Number] | Add custom labels to the contact
  'token': "token_example", // String | Access token to use if unable to set a header
  'watched': false // Boolean | Whether the contact should be watched, note this is only effective on characters
};
apiInstance.putCharactersCharacterIdContacts(characterId, standing, contactIds, opts, (error, data, response) => {
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
 **characterId** | **Number**| An EVE character ID | 
 **standing** | **Number**| Standing for the contact | 
 **contactIds** | [**[Number]**](Number.md)| A list of contacts | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **labelIds** | [**[Number]**](Number.md)| Add custom labels to the contact | [optional] 
 **token** | **String**| Access token to use if unable to set a header | [optional] 
 **watched** | **Boolean**| Whether the contact should be watched, note this is only effective on characters | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

