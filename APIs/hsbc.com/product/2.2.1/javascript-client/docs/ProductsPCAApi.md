# ProductFinderApi.ProductsPCAApi

All URIs are relative to *https://dikpeqbnwi3kx.cloudfront.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**openBankingV22PersonalCurrentAccountsGet**](ProductsPCAApi.md#openBankingV22PersonalCurrentAccountsGet) | **GET** /open-banking/v2.2/personal-current-accounts | 
[**xOpenBankingV22PersonalCurrentAccountsSegmentSegmentGet**](ProductsPCAApi.md#xOpenBankingV22PersonalCurrentAccountsSegmentSegmentGet) | **GET** /x-open-banking/v2.2/personal-current-accounts/segment/{segment} | 



## openBankingV22PersonalCurrentAccountsGet

> PCADefinitionMeta openBankingV22PersonalCurrentAccountsGet()



This API will return data about all PCA products and is prepared to the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. It is regulated by the UK Competition and Markets Authority (CMA). Data is only available for the United Kingdom.

### Example

```javascript
import ProductFinderApi from 'product_finder_api';

let apiInstance = new ProductFinderApi.ProductsPCAApi();
apiInstance.openBankingV22PersonalCurrentAccountsGet((error, data, response) => {
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

[**PCADefinitionMeta**](PCADefinitionMeta.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/prs.openbanking.opendata.v2.2+json


## xOpenBankingV22PersonalCurrentAccountsSegmentSegmentGet

> PCADefinitionMeta xOpenBankingV22PersonalCurrentAccountsSegmentSegmentGet(segment)



This extended API will return data about all PCA products for the specified segment. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

### Example

```javascript
import ProductFinderApi from 'product_finder_api';

let apiInstance = new ProductFinderApi.ProductsPCAApi();
let segment = "segment_example"; // String | Segment name from this list&#58; &quot;Basic&quot;, &quot;General&quot;, &quot;Graduate&quot;, &quot;Packaged&quot;, &quot;Premium&quot;, &quot;Reward&quot;, &quot;Student&quot;, &quot;YoungAdult&quot;, &quot;Youth&quot;.
apiInstance.xOpenBankingV22PersonalCurrentAccountsSegmentSegmentGet(segment, (error, data, response) => {
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
 **segment** | **String**| Segment name from this list&amp;#58; &amp;quot;Basic&amp;quot;, &amp;quot;General&amp;quot;, &amp;quot;Graduate&amp;quot;, &amp;quot;Packaged&amp;quot;, &amp;quot;Premium&amp;quot;, &amp;quot;Reward&amp;quot;, &amp;quot;Student&amp;quot;, &amp;quot;YoungAdult&amp;quot;, &amp;quot;Youth&amp;quot;. | 

### Return type

[**PCADefinitionMeta**](PCADefinitionMeta.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/prs.openbanking.opendata.v2.2+json

