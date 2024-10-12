# MarketplaceRpService.PrivateStoresApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privateStoreCreateOrUpdate**](PrivateStoresApi.md#privateStoreCreateOrUpdate) | **PUT** /providers/Microsoft.Marketplace/privateStores/{PrivateStoreId} | 
[**privateStoreDelete**](PrivateStoresApi.md#privateStoreDelete) | **DELETE** /providers/Microsoft.Marketplace/privateStores/{PrivateStoreId} | 
[**privateStoreGet**](PrivateStoresApi.md#privateStoreGet) | **GET** /providers/Microsoft.Marketplace/privateStores/{PrivateStoreId} | 
[**privateStoreList**](PrivateStoresApi.md#privateStoreList) | **GET** /providers/Microsoft.Marketplace/privateStores | 
[**privateStoreOfferCreateOrUpdate**](PrivateStoresApi.md#privateStoreOfferCreateOrUpdate) | **PUT** /providers/Microsoft.Marketplace/privateStores/{PrivateStoreId}/offers/{OfferId} | 
[**privateStoreOfferDelete**](PrivateStoresApi.md#privateStoreOfferDelete) | **DELETE** /providers/Microsoft.Marketplace/privateStores/{PrivateStoreId}/offers/{OfferId} | 
[**privateStoreOfferGet**](PrivateStoresApi.md#privateStoreOfferGet) | **GET** /providers/Microsoft.Marketplace/privateStores/{PrivateStoreId}/offers/{OfferId} | 
[**privateStoreOffersList**](PrivateStoresApi.md#privateStoreOffersList) | **GET** /providers/Microsoft.Marketplace/privateStores/{PrivateStoreId}/offers | 



## privateStoreCreateOrUpdate

> PrivateStoreProperties privateStoreCreateOrUpdate(privateStoreId, apiVersion, opts)



Changes private store properties

### Example

```javascript
import MarketplaceRpService from 'marketplace_rp_service';

let apiInstance = new MarketplaceRpService.PrivateStoresApi();
let privateStoreId = "privateStoreId_example"; // String | The store ID - must use the tenant ID
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let opts = {
  'payload': new MarketplaceRpService.PrivateStoreProperties() // PrivateStoreProperties | 
};
apiInstance.privateStoreCreateOrUpdate(privateStoreId, apiVersion, opts, (error, data, response) => {
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
 **privateStoreId** | **String**| The store ID - must use the tenant ID | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **payload** | [**PrivateStoreProperties**](PrivateStoreProperties.md)|  | [optional] 

### Return type

[**PrivateStoreProperties**](PrivateStoreProperties.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateStoreDelete

> privateStoreDelete(privateStoreId, apiVersion)



Deletes the private store. All that is not saved will be lost.

### Example

```javascript
import MarketplaceRpService from 'marketplace_rp_service';

let apiInstance = new MarketplaceRpService.PrivateStoresApi();
let privateStoreId = "privateStoreId_example"; // String | The store ID - must use the tenant ID
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.privateStoreDelete(privateStoreId, apiVersion, (error, data, response) => {
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
 **privateStoreId** | **String**| The store ID - must use the tenant ID | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateStoreGet

> PrivateStoreProperties privateStoreGet(privateStoreId, apiVersion)



Get information about the private store

### Example

```javascript
import MarketplaceRpService from 'marketplace_rp_service';

let apiInstance = new MarketplaceRpService.PrivateStoresApi();
let privateStoreId = "privateStoreId_example"; // String | The store ID - must use the tenant ID
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.privateStoreGet(privateStoreId, apiVersion, (error, data, response) => {
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
 **privateStoreId** | **String**| The store ID - must use the tenant ID | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**PrivateStoreProperties**](PrivateStoreProperties.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateStoreList

> PrivateStoreList privateStoreList(apiVersion)



Gets the list of available private stores

### Example

```javascript
import MarketplaceRpService from 'marketplace_rp_service';

let apiInstance = new MarketplaceRpService.PrivateStoresApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.privateStoreList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**PrivateStoreList**](PrivateStoreList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateStoreOfferCreateOrUpdate

> Offer privateStoreOfferCreateOrUpdate(offerId, privateStoreId, apiVersion, opts)



Update or add an offer to the default collection of the private store.

### Example

```javascript
import MarketplaceRpService from 'marketplace_rp_service';

let apiInstance = new MarketplaceRpService.PrivateStoresApi();
let offerId = "offerId_example"; // String | The offer ID to update or delete
let privateStoreId = "privateStoreId_example"; // String | The store ID - must use the tenant ID
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let opts = {
  'payload': new MarketplaceRpService.Offer() // Offer | 
};
apiInstance.privateStoreOfferCreateOrUpdate(offerId, privateStoreId, apiVersion, opts, (error, data, response) => {
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
 **offerId** | **String**| The offer ID to update or delete | 
 **privateStoreId** | **String**| The store ID - must use the tenant ID | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **payload** | [**Offer**](Offer.md)|  | [optional] 

### Return type

[**Offer**](Offer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateStoreOfferDelete

> privateStoreOfferDelete(offerId, privateStoreId, apiVersion)



Deletes an offer from the given private store.

### Example

```javascript
import MarketplaceRpService from 'marketplace_rp_service';

let apiInstance = new MarketplaceRpService.PrivateStoresApi();
let offerId = "offerId_example"; // String | The offer ID to update or delete
let privateStoreId = "privateStoreId_example"; // String | The store ID - must use the tenant ID
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.privateStoreOfferDelete(offerId, privateStoreId, apiVersion, (error, data, response) => {
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
 **offerId** | **String**| The offer ID to update or delete | 
 **privateStoreId** | **String**| The store ID - must use the tenant ID | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## privateStoreOfferGet

> Offer privateStoreOfferGet(offerId, privateStoreId, apiVersion)



Gets information about a specific offer.

### Example

```javascript
import MarketplaceRpService from 'marketplace_rp_service';

let apiInstance = new MarketplaceRpService.PrivateStoresApi();
let offerId = "offerId_example"; // String | The offer ID to update or delete
let privateStoreId = "privateStoreId_example"; // String | The store ID - must use the tenant ID
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.privateStoreOfferGet(offerId, privateStoreId, apiVersion, (error, data, response) => {
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
 **offerId** | **String**| The offer ID to update or delete | 
 **privateStoreId** | **String**| The store ID - must use the tenant ID | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**Offer**](Offer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateStoreOffersList

> OfferListResponse privateStoreOffersList(privateStoreId, apiVersion)



Get a list of all private offers in the given private store

### Example

```javascript
import MarketplaceRpService from 'marketplace_rp_service';

let apiInstance = new MarketplaceRpService.PrivateStoresApi();
let privateStoreId = "privateStoreId_example"; // String | The store ID - must use the tenant ID
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.privateStoreOffersList(privateStoreId, apiVersion, (error, data, response) => {
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
 **privateStoreId** | **String**| The store ID - must use the tenant ID | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**OfferListResponse**](OfferListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

