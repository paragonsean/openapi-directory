# Reverb.ShopsApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shopsIdStorefrontsGet**](ShopsApi.md#shopsIdStorefrontsGet) | **GET** /shops/{id}/storefronts | Get storefront details on a shop.
[**shopsShopIdShippingProfilesGet**](ShopsApi.md#shopsShopIdShippingProfilesGet) | **GET** /shops/{shop_id}/shipping_profiles | List of shipping profiles for your shop
[**shopsSlugFeedbackBuyerGet**](ShopsApi.md#shopsSlugFeedbackBuyerGet) | **GET** /shops/{slug}/feedback/buyer | Get seller&#39;s feedback as a buyer
[**shopsSlugFeedbackGet**](ShopsApi.md#shopsSlugFeedbackGet) | **GET** /shops/{slug}/feedback | Get seller&#39;s feedback
[**shopsSlugFeedbackSellerGet**](ShopsApi.md#shopsSlugFeedbackSellerGet) | **GET** /shops/{slug}/feedback/seller | Get seller&#39;s feedback as a seller
[**shopsSlugGet**](ShopsApi.md#shopsSlugGet) | **GET** /shops/{slug} | Get details on a shop.



## shopsIdStorefrontsGet

> shopsIdStorefrontsGet(id)

Get storefront details on a shop.

Get storefront details on a shop.

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ShopsApi();
let id = "id_example"; // String | 
apiInstance.shopsIdStorefrontsGet(id, (error, data, response) => {
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


## shopsShopIdShippingProfilesGet

> shopsShopIdShippingProfilesGet(shopId)

List of shipping profiles for your shop

List of shipping profiles for your shop

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ShopsApi();
let shopId = "shopId_example"; // String | 
apiInstance.shopsShopIdShippingProfilesGet(shopId, (error, data, response) => {
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
 **shopId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## shopsSlugFeedbackBuyerGet

> shopsSlugFeedbackBuyerGet(slug)

Get seller&#39;s feedback as a buyer

Get seller&#39;s feedback as a buyer

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ShopsApi();
let slug = "slug_example"; // String | 
apiInstance.shopsSlugFeedbackBuyerGet(slug, (error, data, response) => {
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
 **slug** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## shopsSlugFeedbackGet

> shopsSlugFeedbackGet(slug)

Get seller&#39;s feedback

Get seller&#39;s feedback

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ShopsApi();
let slug = "slug_example"; // String | 
apiInstance.shopsSlugFeedbackGet(slug, (error, data, response) => {
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
 **slug** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## shopsSlugFeedbackSellerGet

> shopsSlugFeedbackSellerGet(slug)

Get seller&#39;s feedback as a seller

Get seller&#39;s feedback as a seller

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ShopsApi();
let slug = "slug_example"; // String | 
apiInstance.shopsSlugFeedbackSellerGet(slug, (error, data, response) => {
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
 **slug** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## shopsSlugGet

> shopsSlugGet(slug, opts)

Get details on a shop.

Get details on a shop.

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ShopsApi();
let slug = "slug_example"; // String | 
let opts = {
  'includeListingCount': true // Boolean | Include the live listing count in the response.
};
apiInstance.shopsSlugGet(slug, opts, (error, data, response) => {
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
 **slug** | **String**|  | 
 **includeListingCount** | **Boolean**| Include the live listing count in the response. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

