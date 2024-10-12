# FitbitPlusApi.HealthQuestionDefinitionApi

All URIs are relative to *https://api.twinehealth.com/pub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchHealthQuestionDefinition**](HealthQuestionDefinitionApi.md#fetchHealthQuestionDefinition) | **GET** /health_question_definition/{id} | Get a health question definition
[**fetchHealthQuestionDefinitions**](HealthQuestionDefinitionApi.md#fetchHealthQuestionDefinitions) | **GET** /health_question_definition | List health question definitions



## fetchHealthQuestionDefinition

> FetchHealthQuestionDefinitionResponse fetchHealthQuestionDefinition(id)

Get a health question definition

Get a health question definition by id

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.HealthQuestionDefinitionApi();
let id = "id_example"; // String | Health question definition identifier
apiInstance.fetchHealthQuestionDefinition(id, (error, data, response) => {
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
 **id** | **String**| Health question definition identifier | 

### Return type

[**FetchHealthQuestionDefinitionResponse**](FetchHealthQuestionDefinitionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## fetchHealthQuestionDefinitions

> FetchHealthQuestionDefinitionsResponse fetchHealthQuestionDefinitions()

List health question definitions

Get a list of all health question definitions

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.HealthQuestionDefinitionApi();
apiInstance.fetchHealthQuestionDefinitions((error, data, response) => {
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

[**FetchHealthQuestionDefinitionsResponse**](FetchHealthQuestionDefinitionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

