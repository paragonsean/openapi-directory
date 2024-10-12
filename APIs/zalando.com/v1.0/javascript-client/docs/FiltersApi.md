# ZalandoShop.FiltersApi

All URIs are relative to *https://api.zalando.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filtersFilterNameGet**](FiltersApi.md#filtersFilterNameGet) | **GET** /filters/{filterName} | Get Single Filter by filterName
[**filtersGet**](FiltersApi.md#filtersGet) | **GET** /filters | Shop Filters



## filtersFilterNameGet

> Filter filtersFilterNameGet(filterName, opts)

Get Single Filter by filterName

Zalando API Filters Schema

### Example

```javascript
import ZalandoShop from 'zalando_shop';

let apiInstance = new ZalandoShop.FiltersApi();
let filterName = "filterName_example"; // String | To get Filter by filterName.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
  'fields': ["null"] // [String] | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
};
apiInstance.filtersFilterNameGet(filterName, opts, (error, data, response) => {
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
 **filterName** | **String**| To get Filter by filterName. | 
 **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] 
 **fields** | [**[String]**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] 

### Return type

[**Filter**](Filter.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## filtersGet

> [Filter] filtersGet(opts)

Shop Filters

Zalando API Filters Schema

### Example

```javascript
import ZalandoShop from 'zalando_shop';

let apiInstance = new ZalandoShop.FiltersApi();
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
  'fields': ["null"] // [String] | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
};
apiInstance.filtersGet(opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] 
 **fields** | [**[String]**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] 

### Return type

[**[Filter]**](Filter.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

