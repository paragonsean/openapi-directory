# ZalandoShop.BrandsApi

All URIs are relative to *https://api.zalando.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**brandsGet**](BrandsApi.md#brandsGet) | **GET** /brands | Shop Brands
[**brandsKeyGet**](BrandsApi.md#brandsKeyGet) | **GET** /brands/{key} | Get Single Brand by Key



## brandsGet

> Brands brandsGet(opts)

Shop Brands

Zalando API Brands Schema

### Example

```javascript
import ZalandoShop from 'zalando_shop';

let apiInstance = new ZalandoShop.BrandsApi();
let opts = {
  'key': ["null"], // [String] | Request Brand by key
  'name': ["null"], // [String] | Request Brand by name
  'brandFamilyName': ["null"], // [String] | Request Brand by brandFamilyName
  'brandFamilyKey': ["null"], // [String] | Request Brand by brandFamilyKey
  'page': "page_example", // String | to request with required page number or pagination
  'pageSize': "pageSize_example", // String | to request with required page size in a page
  'acceptLanguage': "acceptLanguage_example", // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
  'fields': ["null"] // [String] | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
};
apiInstance.brandsGet(opts, (error, data, response) => {
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
 **key** | [**[String]**](String.md)| Request Brand by key | [optional] 
 **name** | [**[String]**](String.md)| Request Brand by name | [optional] 
 **brandFamilyName** | [**[String]**](String.md)| Request Brand by brandFamilyName | [optional] 
 **brandFamilyKey** | [**[String]**](String.md)| Request Brand by brandFamilyKey | [optional] 
 **page** | **String**| to request with required page number or pagination | [optional] 
 **pageSize** | **String**| to request with required page size in a page | [optional] 
 **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] 
 **fields** | [**[String]**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] 

### Return type

[**Brands**](Brands.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## brandsKeyGet

> Brand brandsKeyGet(key, opts)

Get Single Brand by Key

Zalando API Brand Schema

### Example

```javascript
import ZalandoShop from 'zalando_shop';

let apiInstance = new ZalandoShop.BrandsApi();
let key = "key_example"; // String | To get unique Brand by key.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
  'fields': ["null"] // [String] | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
};
apiInstance.brandsKeyGet(key, opts, (error, data, response) => {
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
 **key** | **String**| To get unique Brand by key. | 
 **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] 
 **fields** | [**[String]**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] 

### Return type

[**Brand**](Brand.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

