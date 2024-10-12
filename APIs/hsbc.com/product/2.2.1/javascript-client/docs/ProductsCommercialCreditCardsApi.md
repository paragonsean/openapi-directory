# ProductFinderApi.ProductsCommercialCreditCardsApi

All URIs are relative to *https://dikpeqbnwi3kx.cloudfront.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**openBankingV22CommercialCreditCardsGet**](ProductsCommercialCreditCardsApi.md#openBankingV22CommercialCreditCardsGet) | **GET** /open-banking/v2.2/commercial-credit-cards | 
[**xOpenBankingV22CommercialCreditCardsSegmentSegmentGet**](ProductsCommercialCreditCardsApi.md#xOpenBankingV22CommercialCreditCardsSegmentSegmentGet) | **GET** /x-open-banking/v2.2/commercial-credit-cards/segment/{segment} | 



## openBankingV22CommercialCreditCardsGet

> CCCDefinitionMeta openBankingV22CommercialCreditCardsGet()



This API will return data about all commercial credit cards products and is prepared to the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. It is regulated by the UK Competition and Markets Authority (CMA). Data is only available for the United Kingdom.

### Example

```javascript
import ProductFinderApi from 'product_finder_api';

let apiInstance = new ProductFinderApi.ProductsCommercialCreditCardsApi();
apiInstance.openBankingV22CommercialCreditCardsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**CCCDefinitionMeta**](CCCDefinitionMeta.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/prs.openbanking.opendata.v2.2+json


## xOpenBankingV22CommercialCreditCardsSegmentSegmentGet

> CCCDefinitionMeta xOpenBankingV22CommercialCreditCardsSegmentSegmentGet(segment)



This extended API will return data about all commercial credit cards products for the specified segment. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

### Example

```javascript
import ProductFinderApi from 'product_finder_api';

let apiInstance = new ProductFinderApi.ProductsCommercialCreditCardsApi();
let segment = "segment_example"; // String | Segment name from this list&#58; &quot;General&quot;.
apiInstance.xOpenBankingV22CommercialCreditCardsSegmentSegmentGet(segment, (error, data, response) => {
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
 **segment** | **String**| Segment name from this list&amp;#58; &amp;quot;General&amp;quot;. | 

### Return type

[**CCCDefinitionMeta**](CCCDefinitionMeta.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/prs.openbanking.opendata.v2.2+json

