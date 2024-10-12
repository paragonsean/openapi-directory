# Reverb.ComparisonShoppingPagesApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comparisonShoppingPagesFindGet**](ComparisonShoppingPagesApi.md#comparisonShoppingPagesFindGet) | **GET** /comparison_shopping_pages/find | Show comparison shopping page
[**comparisonShoppingPagesGet**](ComparisonShoppingPagesApi.md#comparisonShoppingPagesGet) | **GET** /comparison_shopping_pages | Returns a set of comparison shopping pages based on the current params
[**comparisonShoppingPagesIdGet**](ComparisonShoppingPagesApi.md#comparisonShoppingPagesIdGet) | **GET** /comparison_shopping_pages/{id} | 
[**comparisonShoppingPagesIdListingsGet**](ComparisonShoppingPagesApi.md#comparisonShoppingPagesIdListingsGet) | **GET** /comparison_shopping_pages/{id}/listings | Return new or used listings for a comparison shopping page
[**comparisonShoppingPagesIdReviewsGet**](ComparisonShoppingPagesApi.md#comparisonShoppingPagesIdReviewsGet) | **GET** /comparison_shopping_pages/{id}/reviews | View reviews of a comparison shopping page



## comparisonShoppingPagesFindGet

> comparisonShoppingPagesFindGet(opts)

Show comparison shopping page

Show comparison shopping page

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ComparisonShoppingPagesApi();
let opts = {
  'id': "id_example", // String | ID of the comparison shopping page
  'slug': "slug_example" // String | Slug of the comparison shopping page
};
apiInstance.comparisonShoppingPagesFindGet(opts, (error, data, response) => {
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
 **id** | **String**| ID of the comparison shopping page | [optional] 
 **slug** | **String**| Slug of the comparison shopping page | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## comparisonShoppingPagesGet

> comparisonShoppingPagesGet()

Returns a set of comparison shopping pages based on the current params

Returns a set of comparison shopping pages based on the current params

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ComparisonShoppingPagesApi();
apiInstance.comparisonShoppingPagesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## comparisonShoppingPagesIdGet

> comparisonShoppingPagesIdGet(id)



### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ComparisonShoppingPagesApi();
let id = "id_example"; // String | 
apiInstance.comparisonShoppingPagesIdGet(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## comparisonShoppingPagesIdListingsGet

> comparisonShoppingPagesIdListingsGet(id, condition, opts)

Return new or used listings for a comparison shopping page

Return new or used listings for a comparison shopping page

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ComparisonShoppingPagesApi();
let id = "id_example"; // String | 
let condition = "condition_example"; // String | Condition of the listing
let opts = {
  'page': 1, // Number | 
  'perPage': 24, // Number | 
  'offset': 56 // Number | 
};
apiInstance.comparisonShoppingPagesIdListingsGet(id, condition, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **condition** | **String**| Condition of the listing | 
 **page** | **Number**|  | [optional] [default to 1]
 **perPage** | **Number**|  | [optional] [default to 24]
 **offset** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## comparisonShoppingPagesIdReviewsGet

> comparisonShoppingPagesIdReviewsGet(id)

View reviews of a comparison shopping page

View reviews of a comparison shopping page

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ComparisonShoppingPagesApi();
let id = "id_example"; // String | 
apiInstance.comparisonShoppingPagesIdReviewsGet(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

