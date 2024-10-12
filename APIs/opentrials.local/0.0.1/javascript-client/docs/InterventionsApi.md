# OpenTrialsApi.InterventionsApi

All URIs are relative to *http://opentrials.local/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getIntervention**](InterventionsApi.md#getIntervention) | **GET** /interventions/{id} | 



## getIntervention

> Intervention getIntervention(id)



Returns intervention details

### Example

```javascript
import OpenTrialsApi from 'open_trials_api';

let apiInstance = new OpenTrialsApi.InterventionsApi();
let id = "id_example"; // String | ID of the intervention
apiInstance.getIntervention(id, (error, data, response) => {
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
 **id** | **String**| ID of the intervention | 

### Return type

[**Intervention**](Intervention.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

