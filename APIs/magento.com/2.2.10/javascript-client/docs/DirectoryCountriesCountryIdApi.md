# MagentoB2B.DirectoryCountriesCountryIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**directoryCountryInformationAcquirerV1GetCountryInfoGet**](DirectoryCountriesCountryIdApi.md#directoryCountryInformationAcquirerV1GetCountryInfoGet) | **GET** /V1/directory/countries/{countryId} | directory/countries/{countryId}



## directoryCountryInformationAcquirerV1GetCountryInfoGet

> DirectoryDataCountryInformationInterface directoryCountryInformationAcquirerV1GetCountryInfoGet(countryId)

directory/countries/{countryId}

Get country and region information for the store.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.DirectoryCountriesCountryIdApi();
let countryId = "countryId_example"; // String | 
apiInstance.directoryCountryInformationAcquirerV1GetCountryInfoGet(countryId, (error, data, response) => {
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
 **countryId** | **String**|  | 

### Return type

[**DirectoryDataCountryInformationInterface**](DirectoryDataCountryInformationInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

