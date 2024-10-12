# ProductFinderApi.ProductsBCAApi

All URIs are relative to *https://dikpeqbnwi3kx.cloudfront.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**openBankingV22BusinessCurrentAccountsGet**](ProductsBCAApi.md#openBankingV22BusinessCurrentAccountsGet) | **GET** /open-banking/v2.2/business-current-accounts | 
[**xOpenBankingV22BusinessCurrentAccountsSegmentSegmentGet**](ProductsBCAApi.md#xOpenBankingV22BusinessCurrentAccountsSegmentSegmentGet) | **GET** /x-open-banking/v2.2/business-current-accounts/segment/{segment} | 



## openBankingV22BusinessCurrentAccountsGet

> BCADefinitionMeta openBankingV22BusinessCurrentAccountsGet()



This API will return data about all BCA products and is prepared to the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. It is regulated by the UK Competition and Markets Authority (CMA). Data is only available for the United Kingdom.

### Example

```javascript
import ProductFinderApi from 'product_finder_api';

let apiInstance = new ProductFinderApi.ProductsBCAApi();
apiInstance.openBankingV22BusinessCurrentAccountsGet((error, data, response) => {
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

[**BCADefinitionMeta**](BCADefinitionMeta.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/prs.openbanking.opendata.v2.2+json


## xOpenBankingV22BusinessCurrentAccountsSegmentSegmentGet

> BCADefinitionMeta xOpenBankingV22BusinessCurrentAccountsSegmentSegmentGet(segment)



This extended API will return data about all BCA products for the specified segment. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

### Example

```javascript
import ProductFinderApi from 'product_finder_api';

let apiInstance = new ProductFinderApi.ProductsBCAApi();
let segment = "segment_example"; // String | Segment name from this list&#58; &quot;ClientAccount&quot;, &quot;Standard&quot;, &quot;NonCommercial&quot;, &quot;Religious&quot;, &quot;SectorSpecific&quot;, &quot;Startup&quot;, &quot;Switcher&quot;.
apiInstance.xOpenBankingV22BusinessCurrentAccountsSegmentSegmentGet(segment, (error, data, response) => {
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
 **segment** | **String**| Segment name from this list&amp;#58; &amp;quot;ClientAccount&amp;quot;, &amp;quot;Standard&amp;quot;, &amp;quot;NonCommercial&amp;quot;, &amp;quot;Religious&amp;quot;, &amp;quot;SectorSpecific&amp;quot;, &amp;quot;Startup&amp;quot;, &amp;quot;Switcher&amp;quot;. | 

### Return type

[**BCADefinitionMeta**](BCADefinitionMeta.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/prs.openbanking.opendata.v2.2+json

