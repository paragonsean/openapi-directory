# OpenapiJsClient.V1Api

All URIs are relative to *http://api.ote-godaddy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addExpiryListings**](V1Api.md#addExpiryListings) | **POST** /v1/aftermarket/listings/expiry | Add expiry listings into GoDaddy Auction
[**deleteListings**](V1Api.md#deleteListings) | **DELETE** /v1/aftermarket/listings | Remove listings from GoDaddy Auction



## addExpiryListings

> AftermarketListingAction addExpiryListings(aftermarketListingExpiryCreate)

Add expiry listings into GoDaddy Auction

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let aftermarketListingExpiryCreate = [new OpenapiJsClient.AftermarketListingExpiryCreate()]; // [AftermarketListingExpiryCreate] | An array of expiry listings to be loaded
apiInstance.addExpiryListings(aftermarketListingExpiryCreate, (error, data, response) => {
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
 **aftermarketListingExpiryCreate** | [**[AftermarketListingExpiryCreate]**](AftermarketListingExpiryCreate.md)| An array of expiry listings to be loaded | 

### Return type

[**AftermarketListingAction**](AftermarketListingAction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml, text/xml
- **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml


## deleteListings

> AftermarketListingAction deleteListings(domains)

Remove listings from GoDaddy Auction

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let domains = ["null"]; // [String] | A comma separated list of domain names
apiInstance.deleteListings(domains, (error, data, response) => {
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
 **domains** | [**[String]**](String.md)| A comma separated list of domain names | 

### Return type

[**AftermarketListingAction**](AftermarketListingAction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml

