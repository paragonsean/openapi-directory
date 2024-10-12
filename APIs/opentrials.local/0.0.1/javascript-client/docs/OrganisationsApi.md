# OpenTrialsApi.OrganisationsApi

All URIs are relative to *http://opentrials.local/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOrganisation**](OrganisationsApi.md#getOrganisation) | **GET** /organisations/{id} | 



## getOrganisation

> Organisation getOrganisation(id)



Returns organisation details

### Example

```javascript
import OpenTrialsApi from 'open_trials_api';

let apiInstance = new OpenTrialsApi.OrganisationsApi();
let id = "id_example"; // String | ID of the organisation
apiInstance.getOrganisation(id, (error, data, response) => {
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
 **id** | **String**| ID of the organisation | 

### Return type

[**Organisation**](Organisation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

