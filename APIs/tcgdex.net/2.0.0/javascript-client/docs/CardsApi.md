# TcGdexApi.CardsApi

All URIs are relative to *https://api.tcgdex.net/v2/en*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cards**](CardsApi.md#cards) | **GET** /cards | fetch the list of cards
[**findPetsByTags**](CardsApi.md#findPetsByTags) | **GET** /cards/{cardId} | Finds Card by Global ID
[**setsSetCardLocalIdGet**](CardsApi.md#setsSetCardLocalIdGet) | **GET** /sets/{set}/{cardLocalId} | 



## cards

> [CardResume] cards()

fetch the list of cards

desc

### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.CardsApi();
apiInstance.cards((error, data, response) => {
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

[**[CardResume]**](CardResume.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findPetsByTags

> Card findPetsByTags(cardId)

Finds Card by Global ID

Find a defined card thatusing its global id

### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.CardsApi();
let cardId = "cardId_example"; // String | Tags to filter by
apiInstance.findPetsByTags(cardId, (error, data, response) => {
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
 **cardId** | **String**| Tags to filter by | 

### Return type

[**Card**](Card.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setsSetCardLocalIdGet

> Card setsSetCardLocalIdGet(set, cardLocalId)



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.CardsApi();
let set = "set_example"; // String | 
let cardLocalId = "cardLocalId_example"; // String | 
apiInstance.setsSetCardLocalIdGet(set, cardLocalId, (error, data, response) => {
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
 **set** | **String**|  | 
 **cardLocalId** | **String**|  | 

### Return type

[**Card**](Card.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

