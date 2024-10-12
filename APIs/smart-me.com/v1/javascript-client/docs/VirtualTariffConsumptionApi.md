# SmartMe.VirtualTariffConsumptionApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualTariffConsumptionGet**](VirtualTariffConsumptionApi.md#virtualTariffConsumptionGet) | **GET** /api/VirtualTariffConsumption | Gets the consumption of a folder with a virtuall tariffs.



## virtualTariffConsumptionGet

> [VirtualTariffConsumptionData] virtualTariffConsumptionGet(folderId, startDate, endDate)

Gets the consumption of a folder with a virtuall tariffs.

Gets the consumption of a folder with a virtuall tariffs.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.VirtualTariffConsumptionApi();
let folderId = "folderId_example"; // String | The ID of the Folder
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The start date (UTC)
let endDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The end date (UTC)
apiInstance.virtualTariffConsumptionGet(folderId, startDate, endDate, (error, data, response) => {
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
 **folderId** | **String**| The ID of the Folder | 
 **startDate** | **Date**| The start date (UTC) | 
 **endDate** | **Date**| The end date (UTC) | 

### Return type

[**[VirtualTariffConsumptionData]**](VirtualTariffConsumptionData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

