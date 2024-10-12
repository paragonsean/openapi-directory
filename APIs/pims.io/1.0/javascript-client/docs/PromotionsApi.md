# Pims.PromotionsApi

All URIs are relative to *https://demo.pims.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchAllEventsPromotions**](PromotionsApi.md#fetchAllEventsPromotions) | **GET** /events/{event_id}/promotions | Find all promotions for one event
[**fetchAllPromotions**](PromotionsApi.md#fetchAllPromotions) | **GET** /promotions | Find all promotions
[**fetchAllSeriesPromotions**](PromotionsApi.md#fetchAllSeriesPromotions) | **GET** /series/{series_id}/promotions | Find all promotions for one series
[**fetchOnePromotion**](PromotionsApi.md#fetchOnePromotion) | **GET** /promotions/{promotion_id} | Get one promotion by ID



## fetchAllEventsPromotions

> [PromotionsEntity] fetchAllEventsPromotions(eventId, opts)

Find all promotions for one event

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.PromotionsApi();
let eventId = 56; // Number | ID of the targeted event.
let opts = {
  'label': "label_example", // String | Find only the promotions whose label contains this value.
  'fromDate': new Date("2013-10-20"), // Date | Find only the promotions starting after this date.
  'toDate': new Date("2013-10-20"), // Date | Find only the promotions ending before this date.
  'type': "type_example", // String | Find only the promotions whose type is equal to this value.
  'family': "family_example", // String | Find only the promotions whose family is equal to this value.
  'sort': "'date'", // String | Sort the promotions in the corresponding order.
  'pageSize': 25, // Number | Pagination size, i.e. maximum number of items to be displayed in the response.
  'acceptLanguage': "'en'" // String | Language used for the translatable labels.
};
apiInstance.fetchAllEventsPromotions(eventId, opts, (error, data, response) => {
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
 **eventId** | **Number**| ID of the targeted event. | 
 **label** | **String**| Find only the promotions whose label contains this value. | [optional] 
 **fromDate** | **Date**| Find only the promotions starting after this date. | [optional] 
 **toDate** | **Date**| Find only the promotions ending before this date. | [optional] 
 **type** | **String**| Find only the promotions whose type is equal to this value. | [optional] 
 **family** | **String**| Find only the promotions whose family is equal to this value. | [optional] 
 **sort** | **String**| Sort the promotions in the corresponding order. | [optional] [default to &#39;date&#39;]
 **pageSize** | **Number**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25]
 **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to &#39;en&#39;]

### Return type

[**[PromotionsEntity]**](PromotionsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json


## fetchAllPromotions

> [PromotionsEntity] fetchAllPromotions(opts)

Find all promotions

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.PromotionsApi();
let opts = {
  'label': "label_example", // String | Find only the promotions whose label contains this value.
  'fromDate': new Date("2013-10-20"), // Date | Find only the promotions starting after this date.
  'toDate': new Date("2013-10-20"), // Date | Find only the promotions ending before this date.
  'type': "type_example", // String | Find only the promotions whose type is equal to this value.
  'family': "family_example", // String | Find only the promotions whose family is equal to this value.
  'sort': "'date'", // String | Sort the promotions in the corresponding order.
  'pageSize': 25, // Number | Pagination size, i.e. maximum number of items to be displayed in the response.
  'acceptLanguage': "'en'" // String | Language used for the translatable labels.
};
apiInstance.fetchAllPromotions(opts, (error, data, response) => {
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
 **label** | **String**| Find only the promotions whose label contains this value. | [optional] 
 **fromDate** | **Date**| Find only the promotions starting after this date. | [optional] 
 **toDate** | **Date**| Find only the promotions ending before this date. | [optional] 
 **type** | **String**| Find only the promotions whose type is equal to this value. | [optional] 
 **family** | **String**| Find only the promotions whose family is equal to this value. | [optional] 
 **sort** | **String**| Sort the promotions in the corresponding order. | [optional] [default to &#39;date&#39;]
 **pageSize** | **Number**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25]
 **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to &#39;en&#39;]

### Return type

[**[PromotionsEntity]**](PromotionsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json


## fetchAllSeriesPromotions

> [PromotionsEntity] fetchAllSeriesPromotions(seriesId, opts)

Find all promotions for one series

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.PromotionsApi();
let seriesId = 56; // Number | ID of the targeted series.
let opts = {
  'label': "label_example", // String | Find only the promotions whose label contains this value.
  'fromDate': new Date("2013-10-20"), // Date | Find only the promotions starting after this date.
  'toDate': new Date("2013-10-20"), // Date | Find only the promotions ending before this date.
  'type': "type_example", // String | Find only the promotions whose type is equal to this value.
  'family': "family_example", // String | Find only the promotions whose family is equal to this value.
  'sort': "'date'", // String | Sort the promotions in the corresponding order.
  'pageSize': 25, // Number | Pagination size, i.e. maximum number of items to be displayed in the response.
  'acceptLanguage': "'en'" // String | Language used for the translatable labels.
};
apiInstance.fetchAllSeriesPromotions(seriesId, opts, (error, data, response) => {
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
 **seriesId** | **Number**| ID of the targeted series. | 
 **label** | **String**| Find only the promotions whose label contains this value. | [optional] 
 **fromDate** | **Date**| Find only the promotions starting after this date. | [optional] 
 **toDate** | **Date**| Find only the promotions ending before this date. | [optional] 
 **type** | **String**| Find only the promotions whose type is equal to this value. | [optional] 
 **family** | **String**| Find only the promotions whose family is equal to this value. | [optional] 
 **sort** | **String**| Sort the promotions in the corresponding order. | [optional] [default to &#39;date&#39;]
 **pageSize** | **Number**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25]
 **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to &#39;en&#39;]

### Return type

[**[PromotionsEntity]**](PromotionsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json


## fetchOnePromotion

> PromotionsEntity fetchOnePromotion(promotionId, opts)

Get one promotion by ID

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.PromotionsApi();
let promotionId = 56; // Number | ID of the targeted promotion.
let opts = {
  'acceptLanguage': "'en'" // String | Language used for the translatable labels.
};
apiInstance.fetchOnePromotion(promotionId, opts, (error, data, response) => {
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
 **promotionId** | **Number**| ID of the targeted promotion. | 
 **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to &#39;en&#39;]

### Return type

[**PromotionsEntity**](PromotionsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json

