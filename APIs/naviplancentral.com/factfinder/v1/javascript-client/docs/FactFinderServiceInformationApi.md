# AdvicentFactFinderService.FactFinderServiceInformationApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**factFinderServiceInformationGet**](FactFinderServiceInformationApi.md#factFinderServiceInformationGet) | **GET** /api/ServiceInformation | 



## factFinderServiceInformationGet

> ServiceInformationModel factFinderServiceInformationGet()



Description: This operation retrieves information statistics for the current service.&lt;br /&gt;                Purpose: Provides access to Service Information.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.FactFinderServiceInformationApi();
apiInstance.factFinderServiceInformationGet((error, data, response) => {
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

[**ServiceInformationModel**](ServiceInformationModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

