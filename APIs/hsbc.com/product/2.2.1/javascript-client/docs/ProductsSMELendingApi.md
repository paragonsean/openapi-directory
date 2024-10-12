# ProductFinderApi.ProductsSMELendingApi

All URIs are relative to *https://dikpeqbnwi3kx.cloudfront.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**openBankingV22UnsecuredSmeLoansGet**](ProductsSMELendingApi.md#openBankingV22UnsecuredSmeLoansGet) | **GET** /open-banking/v2.2/unsecured-sme-loans | 
[**xOpenBankingV22UnsecuredSmeLoansSegmentSegmentGet**](ProductsSMELendingApi.md#xOpenBankingV22UnsecuredSmeLoansSegmentSegmentGet) | **GET** /x-open-banking/v2.2/unsecured-sme-loans/segment/{segment} | 



## openBankingV22UnsecuredSmeLoansGet

> SMELendingDefinitionMeta openBankingV22UnsecuredSmeLoansGet()



This API will return data about all SME lending products and is prepared to the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. It is regulated by the UK Competition and Markets Authority (CMA). Data is only available for the United Kingdom.

### Example

```javascript
import ProductFinderApi from 'product_finder_api';

let apiInstance = new ProductFinderApi.ProductsSMELendingApi();
apiInstance.openBankingV22UnsecuredSmeLoansGet((error, data, response) => {
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

[**SMELendingDefinitionMeta**](SMELendingDefinitionMeta.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/prs.openbanking.opendata.v2.2+json


## xOpenBankingV22UnsecuredSmeLoansSegmentSegmentGet

> SMELendingDefinitionMeta xOpenBankingV22UnsecuredSmeLoansSegmentSegmentGet(segment)



This extended API will return data about all SME lending products for the specified segment. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

### Example

```javascript
import ProductFinderApi from 'product_finder_api';

let apiInstance = new ProductFinderApi.ProductsSMELendingApi();
let segment = "segment_example"; // String | Segment name from this list&#58; &quot;AgricultureSector&quot;, &quot;Business&quot;, &quot;FixedGroup&quot;, &quot;FlexibleBusinessLoan&quot;, &quot;GovernmentScheme&quot;, &quot;Other&quot;, &quot;SectorSpecific&quot;.
apiInstance.xOpenBankingV22UnsecuredSmeLoansSegmentSegmentGet(segment, (error, data, response) => {
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
 **segment** | **String**| Segment name from this list&amp;#58; &amp;quot;AgricultureSector&amp;quot;, &amp;quot;Business&amp;quot;, &amp;quot;FixedGroup&amp;quot;, &amp;quot;FlexibleBusinessLoan&amp;quot;, &amp;quot;GovernmentScheme&amp;quot;, &amp;quot;Other&amp;quot;, &amp;quot;SectorSpecific&amp;quot;. | 

### Return type

[**SMELendingDefinitionMeta**](SMELendingDefinitionMeta.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/prs.openbanking.opendata.v2.2+json

