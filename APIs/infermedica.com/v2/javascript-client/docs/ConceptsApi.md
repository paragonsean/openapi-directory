# InfermedicaApi.ConceptsApi

All URIs are relative to *https://api.infermedica.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getConcept**](ConceptsApi.md#getConcept) | **GET** /concepts/{id} | 
[**getConcepts**](ConceptsApi.md#getConcepts) | **GET** /concepts | 



## getConcept

> ConceptItemModelPublic getConcept(id)



### Example

```javascript
import InfermedicaApi from 'infermedica_api';

let apiInstance = new InfermedicaApi.ConceptsApi();
let id = "id_example"; // String | concept id
apiInstance.getConcept(id, (error, data, response) => {
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
 **id** | **String**| concept id | 

### Return type

[**ConceptItemModelPublic**](ConceptItemModelPublic.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getConcepts

> [ConceptItemModelPublic] getConcepts(opts)



### Example

```javascript
import InfermedicaApi from 'infermedica_api';

let apiInstance = new InfermedicaApi.ConceptsApi();
let opts = {
  'ids': "ids_example", // String | ids
  'types': "types_example" // String | types
};
apiInstance.getConcepts(opts, (error, data, response) => {
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
 **ids** | **String**| ids | [optional] 
 **types** | **String**| types | [optional] 

### Return type

[**[ConceptItemModelPublic]**](ConceptItemModelPublic.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

