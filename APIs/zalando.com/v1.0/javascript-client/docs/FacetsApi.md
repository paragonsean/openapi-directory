# ZalandoShop.FacetsApi

All URIs are relative to *https://api.zalando.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**facetsGet**](FacetsApi.md#facetsGet) | **GET** /facets | Shop Facets



## facetsGet

> [Facet] facetsGet(opts)

Shop Facets

Zalando API Facets Schema

### Example

```javascript
import ZalandoShop from 'zalando_shop';

let apiInstance = new ZalandoShop.FacetsApi();
let opts = {
  'ageGroup': ["null"], // [String] | filters by age group (eg: kids)
  'articleId': ["null"], // [String] | The `articleIds` to use use for filtering.  One or more `articleIds` might be used as a filter criteria. Submit multiple `articleId` request parameters for more than one to be used. They will be treated as `OR` criteria.
  'activationDate': ["null"], // [String] | period or time the articles are activated for selling in the shop
  'articleModelId': ["null"], // [String] | filters by article ModelId
  'assortmentArea': ["null"], // [String] | filters by classification of articles (eg: maternity) 
  'brand': ["null"], // [String] | filters by brand key given by user (eg: SA5)
  'brandfamily': ["null"], // [String] | filters by brand family key (eg: nike) 
  'category': ["null"], // [String] | filters by category (eg: Socks, Rain Coats)
  'color': ["null"], // [String] | filters by color (eg: red, blue)
  'den': ["null"], // [String] | filters by den 
  'filling': ["null"], // [String] | filters by different kinds of garment filling materials (eg: satin, wolle)
  'gender': ["null"], // [String] | filters by gender
  'heelForm': ["null"], // [String] | filters by heel form (eg: flat)
  'heelHeight': ["null"], // [String] | filters by height of the heel size or length (eg: xs)
  'length': "length_example", // String | filters by garments length (eg: 3/4 length, knee-length)
  'occasion': ["null"], // [String] | filters by type of occasion (eg: party, business)
  'pattern': ["null"], // [String] | filters by pattern on the garments (eg: animal print, plain)
  'price': "price_example", // String | filters all articles in price range (eg: 9-90)
  'sale': ["null"], // [String] | filters discounted articles marked as sale
  'season': ["null"], // [String] | filters by season (Autumn/Winter or Spring/Summer)
  'shaftHeight': ["null"], // [String] | filters by shaft height (eg: s, xs)
  'shaftWidth': ["null"], // [String] | filters by shaft width (eg: s, l)
  'shirtCollar': ["null"], // [String] | filters by shirt collar styles (eg: low V neck, lined collar)
  'shoeFastener': ["null"], // [String] | filters by shoe fastener types (eg: buckle, lacing)
  'shoeToecap': ["null"], // [String] | filters by shoe toe cap variants (eg: pointed, square)
  'shopArea': ["null"], // [String] | filters by classification of articles
  'size': "size_example", // String | filters by size
  'sports': ["null"], // [String] | filters by different sport activities (eg: football)
  'technology': ["null"], // [String] | filters by technology used to produce the articles
  'trouserRise': ["null"], // [String] | filters by trouser rise
  'upperMaterial': ["null"], // [String] | filters by different type of upper material used on garments (eg: lace)
  'volume': ["null"], // [String] | filters by volume
  'acceptLanguage': "acceptLanguage_example", // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
  'fields': ["null"] // [String] | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
};
apiInstance.facetsGet(opts, (error, data, response) => {
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
 **ageGroup** | [**[String]**](String.md)| filters by age group (eg: kids) | [optional] 
 **articleId** | [**[String]**](String.md)| The &#x60;articleIds&#x60; to use use for filtering.  One or more &#x60;articleIds&#x60; might be used as a filter criteria. Submit multiple &#x60;articleId&#x60; request parameters for more than one to be used. They will be treated as &#x60;OR&#x60; criteria. | [optional] 
 **activationDate** | [**[String]**](String.md)| period or time the articles are activated for selling in the shop | [optional] 
 **articleModelId** | [**[String]**](String.md)| filters by article ModelId | [optional] 
 **assortmentArea** | [**[String]**](String.md)| filters by classification of articles (eg: maternity)  | [optional] 
 **brand** | [**[String]**](String.md)| filters by brand key given by user (eg: SA5) | [optional] 
 **brandfamily** | [**[String]**](String.md)| filters by brand family key (eg: nike)  | [optional] 
 **category** | [**[String]**](String.md)| filters by category (eg: Socks, Rain Coats) | [optional] 
 **color** | [**[String]**](String.md)| filters by color (eg: red, blue) | [optional] 
 **den** | [**[String]**](String.md)| filters by den  | [optional] 
 **filling** | [**[String]**](String.md)| filters by different kinds of garment filling materials (eg: satin, wolle) | [optional] 
 **gender** | [**[String]**](String.md)| filters by gender | [optional] 
 **heelForm** | [**[String]**](String.md)| filters by heel form (eg: flat) | [optional] 
 **heelHeight** | [**[String]**](String.md)| filters by height of the heel size or length (eg: xs) | [optional] 
 **length** | **String**| filters by garments length (eg: 3/4 length, knee-length) | [optional] 
 **occasion** | [**[String]**](String.md)| filters by type of occasion (eg: party, business) | [optional] 
 **pattern** | [**[String]**](String.md)| filters by pattern on the garments (eg: animal print, plain) | [optional] 
 **price** | **String**| filters all articles in price range (eg: 9-90) | [optional] 
 **sale** | [**[String]**](String.md)| filters discounted articles marked as sale | [optional] 
 **season** | [**[String]**](String.md)| filters by season (Autumn/Winter or Spring/Summer) | [optional] 
 **shaftHeight** | [**[String]**](String.md)| filters by shaft height (eg: s, xs) | [optional] 
 **shaftWidth** | [**[String]**](String.md)| filters by shaft width (eg: s, l) | [optional] 
 **shirtCollar** | [**[String]**](String.md)| filters by shirt collar styles (eg: low V neck, lined collar) | [optional] 
 **shoeFastener** | [**[String]**](String.md)| filters by shoe fastener types (eg: buckle, lacing) | [optional] 
 **shoeToecap** | [**[String]**](String.md)| filters by shoe toe cap variants (eg: pointed, square) | [optional] 
 **shopArea** | [**[String]**](String.md)| filters by classification of articles | [optional] 
 **size** | **String**| filters by size | [optional] 
 **sports** | [**[String]**](String.md)| filters by different sport activities (eg: football) | [optional] 
 **technology** | [**[String]**](String.md)| filters by technology used to produce the articles | [optional] 
 **trouserRise** | [**[String]**](String.md)| filters by trouser rise | [optional] 
 **upperMaterial** | [**[String]**](String.md)| filters by different type of upper material used on garments (eg: lace) | [optional] 
 **volume** | [**[String]**](String.md)| filters by volume | [optional] 
 **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] 
 **fields** | [**[String]**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] 

### Return type

[**[Facet]**](Facet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

