# MembersApi.PartiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPartiesGetActiveHouseGet**](PartiesApi.md#apiPartiesGetActiveHouseGet) | **GET** /api/Parties/GetActive/{house} | Returns a list of current parties with at least one active member.
[**apiPartiesLordsByTypeForDateGet**](PartiesApi.md#apiPartiesLordsByTypeForDateGet) | **GET** /api/Parties/LordsByType/{forDate} | Returns the composition of the House of Lords by peerage type.
[**apiPartiesStateOfThePartiesHouseForDateGet**](PartiesApi.md#apiPartiesStateOfThePartiesHouseForDateGet) | **GET** /api/Parties/StateOfTheParties/{house}/{forDate} | Returns current state of parties



## apiPartiesGetActiveHouseGet

> PartyMembersServiceSearchResult apiPartiesGetActiveHouseGet(house)

Returns a list of current parties with at least one active member.

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.PartiesApi();
let house = new MembersApi.House(); // House | Current parties by house
apiInstance.apiPartiesGetActiveHouseGet(house, (error, data, response) => {
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
 **house** | [**House**](.md)| Current parties by house | 

### Return type

[**PartyMembersServiceSearchResult**](PartyMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiPartiesLordsByTypeForDateGet

> LordsByTypeMembersServiceSearchResult apiPartiesLordsByTypeForDateGet(forDate)

Returns the composition of the House of Lords by peerage type.

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.PartiesApi();
let forDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Composition of the Lords for date specified.
apiInstance.apiPartiesLordsByTypeForDateGet(forDate, (error, data, response) => {
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
 **forDate** | **Date**| Composition of the Lords for date specified. | 

### Return type

[**LordsByTypeMembersServiceSearchResult**](LordsByTypeMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiPartiesStateOfThePartiesHouseForDateGet

> PartySeatCountMembersServiceSearchResult apiPartiesStateOfThePartiesHouseForDateGet(house, forDate)

Returns current state of parties

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.PartiesApi();
let house = new MembersApi.House(); // House | State of parties in Commons or Lords.
let forDate = new Date("2013-10-20T19:20:30+01:00"); // Date | State of parties for the date specified
apiInstance.apiPartiesStateOfThePartiesHouseForDateGet(house, forDate, (error, data, response) => {
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
 **house** | [**House**](.md)| State of parties in Commons or Lords. | 
 **forDate** | **Date**| State of parties for the date specified | 

### Return type

[**PartySeatCountMembersServiceSearchResult**](PartySeatCountMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

