# Pims.CategoriesApi

All URIs are relative to *https://demo.pims.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchAllCategories**](CategoriesApi.md#fetchAllCategories) | **GET** /categories | Find all categories
[**fetchAllEventsCategories**](CategoriesApi.md#fetchAllEventsCategories) | **GET** /events/{event_id}/categories | Find all categories for one event
[**fetchOneCategory**](CategoriesApi.md#fetchOneCategory) | **GET** /categories/{category_id} | Get one category by ID
[**fetchOneEventCategory**](CategoriesApi.md#fetchOneEventCategory) | **GET** /events/{event_id}/categories/{category_id} | Get one event category by ID



## fetchAllCategories

> [CategoriesEntity] fetchAllCategories(opts)

Find all categories

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.CategoriesApi();
let opts = {
  'label': "label_example", // String | Find only the categories whose label/short label contains this value.
  'showIgnored': false, // Boolean | If set to `false`, show only the categories which are not ignored. If set to `true`, show all categories.
  'sort': "'order'", // String | Sort the categories in the corresponding order.
  'pageSize': 25, // Number | Pagination size, i.e. maximum number of items to be displayed in the response.
  'acceptLanguage': "'en'" // String | Language used for the translatable labels.
};
apiInstance.fetchAllCategories(opts, (error, data, response) => {
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
 **label** | **String**| Find only the categories whose label/short label contains this value. | [optional] 
 **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the categories which are not ignored. If set to &#x60;true&#x60;, show all categories. | [optional] [default to false]
 **sort** | **String**| Sort the categories in the corresponding order. | [optional] [default to &#39;order&#39;]
 **pageSize** | **Number**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25]
 **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to &#39;en&#39;]

### Return type

[**[CategoriesEntity]**](CategoriesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json


## fetchAllEventsCategories

> [EventsCategoriesEntity] fetchAllEventsCategories(eventId, opts)

Find all categories for one event

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.CategoriesApi();
let eventId = 56; // Number | ID of the targeted event.
let opts = {
  'showIgnored': false, // Boolean | If set to `false`, show only the [event-]categories/[event-]price ranges which are not ignored. If set to `true`, show everything.
  'pageSize': 25 // Number | Pagination size, i.e. maximum number of items to be displayed in the response.
};
apiInstance.fetchAllEventsCategories(eventId, opts, (error, data, response) => {
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
 **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the [event-]categories/[event-]price ranges which are not ignored. If set to &#x60;true&#x60;, show everything. | [optional] [default to false]
 **pageSize** | **Number**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25]

### Return type

[**[EventsCategoriesEntity]**](EventsCategoriesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json


## fetchOneCategory

> CategoriesEntity fetchOneCategory(categoryId, opts)

Get one category by ID

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.CategoriesApi();
let categoryId = 56; // Number | ID of the targeted category.
let opts = {
  'acceptLanguage': "'en'" // String | Language used for the translatable labels.
};
apiInstance.fetchOneCategory(categoryId, opts, (error, data, response) => {
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
 **categoryId** | **Number**| ID of the targeted category. | 
 **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to &#39;en&#39;]

### Return type

[**CategoriesEntity**](CategoriesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json


## fetchOneEventCategory

> EventsCategoriesEntity fetchOneEventCategory(eventId, categoryId, opts)

Get one event category by ID

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.CategoriesApi();
let eventId = 56; // Number | ID of the targeted event.
let categoryId = 3.4; // Number | ID of the targeted event category.
let opts = {
  'showIgnored': false // Boolean | If set to `false`, show only the embedded [event-]price ranges which are not ignored. If set to `true`, show everything.
};
apiInstance.fetchOneEventCategory(eventId, categoryId, opts, (error, data, response) => {
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
 **categoryId** | **Number**| ID of the targeted event category. | 
 **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the embedded [event-]price ranges which are not ignored. If set to &#x60;true&#x60;, show everything. | [optional] [default to false]

### Return type

[**EventsCategoriesEntity**](EventsCategoriesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json

