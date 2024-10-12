# BeezUpMerchantApi.MarketplacesChannelCatalogsPublicationsApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPublications**](MarketplacesChannelCatalogsPublicationsApi.md#getPublications) | **GET** /v2/user/marketplaces/channelcatalogs/publications/{marketplaceTechnicalCode}/{accountId}/history | Fetch the publication history for an account, sorted by descending start date
[**publishCatalogToMarketplace**](MarketplacesChannelCatalogsPublicationsApi.md#publishCatalogToMarketplace) | **POST** /v2/user/marketplaces/channelcatalogs/publications/{marketplaceTechnicalCode}/{accountId}/publish | [PREVIEW] Launch a publication of the catalog to the marketplace



## getPublications

> AccountPublications getPublications(marketplaceTechnicalCode, accountId, publicationTypes, opts)

Fetch the publication history for an account, sorted by descending start date

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesChannelCatalogsPublicationsApi();
let marketplaceTechnicalCode = "marketplaceTechnicalCode_example"; // String | Marketplace Technical Code to query (required)
let accountId = 56; // Number | Account Id to query (required)
let publicationTypes = ["null"]; // [String] | Publication types by which to filter (optional)
let opts = {
  'channelCatalogId': "channelCatalogId_example", // String | Channel Catalog Id by which to filter (optional)
  'count': 56 // Number | Amount of entries to fetch (optional, default set to 10)
};
apiInstance.getPublications(marketplaceTechnicalCode, accountId, publicationTypes, opts, (error, data, response) => {
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
 **marketplaceTechnicalCode** | **String**| Marketplace Technical Code to query (required) | 
 **accountId** | **Number**| Account Id to query (required) | 
 **publicationTypes** | [**[String]**](String.md)| Publication types by which to filter (optional) | 
 **channelCatalogId** | **String**| Channel Catalog Id by which to filter (optional) | [optional] 
 **count** | **Number**| Amount of entries to fetch (optional, default set to 10) | [optional] 

### Return type

[**AccountPublications**](AccountPublications.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publishCatalogToMarketplace

> publishCatalogToMarketplace(marketplaceTechnicalCode, accountId, publishCatalogToMarketplaceRequest)

[PREVIEW] Launch a publication of the catalog to the marketplace

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesChannelCatalogsPublicationsApi();
let marketplaceTechnicalCode = "marketplaceTechnicalCode_example"; // String | Marketplace Technical Code to query (required)
let accountId = 56; // Number | Account Id to query (required)
let publishCatalogToMarketplaceRequest = new BeezUpMerchantApi.PublishCatalogToMarketplaceRequest(); // PublishCatalogToMarketplaceRequest | 
apiInstance.publishCatalogToMarketplace(marketplaceTechnicalCode, accountId, publishCatalogToMarketplaceRequest, (error, data, response) => {
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
 **marketplaceTechnicalCode** | **String**| Marketplace Technical Code to query (required) | 
 **accountId** | **Number**| Account Id to query (required) | 
 **publishCatalogToMarketplaceRequest** | [**PublishCatalogToMarketplaceRequest**](PublishCatalogToMarketplaceRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

