# AdvicentFactFinderService.ClientsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clientsPostByModel**](ClientsApi.md#clientsPostByModel) | **POST** /api/Clients | 



## clientsPostByModel

> ClientModel clientsPostByModel(model)



Description: This operation submits the Fact Finder data to an external system.&lt;br /&gt;                Purpose: Allows Fact Finder data to be persisted in another system for that system&#39;s consumption and use.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.ClientsApi();
let model = new AdvicentFactFinderService.ClientsModel(); // ClientsModel | 
apiInstance.clientsPostByModel(model, (error, data, response) => {
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
 **model** | [**ClientsModel**](ClientsModel.md)|  | 

### Return type

[**ClientModel**](ClientModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

