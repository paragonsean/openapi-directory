# ZalandoShop.CategoriesApi

All URIs are relative to *https://api.zalando.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categoriesGet**](CategoriesApi.md#categoriesGet) | **GET** /categories | Shop Categories
[**categoriesKeyGet**](CategoriesApi.md#categoriesKeyGet) | **GET** /categories/{key} | Get Single Category by Key



## categoriesGet

> Categories categoriesGet(opts)

Shop Categories

Zalando API Categories Schema

### Example

```javascript
import ZalandoShop from 'zalando_shop';

let apiInstance = new ZalandoShop.CategoriesApi();
let opts = {
  'name': ["null"], // [String] | Request Categories by names
  'type': "type_example", // String | Request Categories by type
  'outlet': "outlet_example", // String | Request Categories by outlet
  'hidden': "hidden_example", // String | Request Categories by hidden
  'targetGroup': "targetGroup_example", // String | Request Categories by target group
  'key': ["null"], // [String] | Request Categories by keys
  'parentKey': ["null"], // [String] | Request Categories by parent keys
  'childKey': ["null"], // [String] | Request Categories by child keys
  'suggestedFilter': ["null"], // [String] | Request Categories by suggested filters
  'page': "page_example", // String | to request with required page number or pagination
  'pageSize': "pageSize_example", // String | to request with required page size in a page
  'acceptLanguage': "acceptLanguage_example", // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
  'fields': ["null"] // [String] | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
};
apiInstance.categoriesGet(opts, (error, data, response) => {
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
 **name** | [**[String]**](String.md)| Request Categories by names | [optional] 
 **type** | **String**| Request Categories by type | [optional] 
 **outlet** | **String**| Request Categories by outlet | [optional] 
 **hidden** | **String**| Request Categories by hidden | [optional] 
 **targetGroup** | **String**| Request Categories by target group | [optional] 
 **key** | [**[String]**](String.md)| Request Categories by keys | [optional] 
 **parentKey** | [**[String]**](String.md)| Request Categories by parent keys | [optional] 
 **childKey** | [**[String]**](String.md)| Request Categories by child keys | [optional] 
 **suggestedFilter** | [**[String]**](String.md)| Request Categories by suggested filters | [optional] 
 **page** | **String**| to request with required page number or pagination | [optional] 
 **pageSize** | **String**| to request with required page size in a page | [optional] 
 **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] 
 **fields** | [**[String]**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] 

### Return type

[**Categories**](Categories.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoriesKeyGet

> Category categoriesKeyGet(key, opts)

Get Single Category by Key

Zalando API Category Schema

### Example

```javascript
import ZalandoShop from 'zalando_shop';

let apiInstance = new ZalandoShop.CategoriesApi();
let key = ["null"]; // [String] | To get unique Category by key.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
  'fields': ["null"] // [String] | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
};
apiInstance.categoriesKeyGet(key, opts, (error, data, response) => {
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
 **key** | [**[String]**](String.md)| To get unique Category by key. | 
 **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] 
 **fields** | [**[String]**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] 

### Return type

[**Category**](Category.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

