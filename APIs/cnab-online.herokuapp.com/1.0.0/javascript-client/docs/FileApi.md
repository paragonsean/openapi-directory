# CnabOnline.FileApi

All URIs are relative to *https://cnab-online.herokuapp.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fileFileIdGet**](FileApi.md#fileFileIdGet) | **GET** /file/{fileId} | Retorna as informações básicas de um arquivo previamente processado
[**fileFileIdLinesGet**](FileApi.md#fileFileIdLinesGet) | **GET** /file/{fileId}/lines | Retorna todas as linhas e seus respectivos campos (de forma não processada, apenas indicando os campos reconhecidos)
[**fileFileIdOccurrencesGet**](FileApi.md#fileFileIdOccurrencesGet) | **GET** /file/{fileId}/occurrences | Retorna as informações de baixa de boletos e outros tipos de ocorrências
[**filePost**](FileApi.md#filePost) | **POST** /file | Faz o upload de um arquivo



## fileFileIdGet

> FilePost200Response fileFileIdGet(fileId)

Retorna as informações básicas de um arquivo previamente processado

### Example

```javascript
import CnabOnline from 'cnab_online';

let apiInstance = new CnabOnline.FileApi();
let fileId = "fileId_example"; // String | ID Temporário gerado no endpoint file
apiInstance.fileFileIdGet(fileId, (error, data, response) => {
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
 **fileId** | **String**| ID Temporário gerado no endpoint file | 

### Return type

[**FilePost200Response**](FilePost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileFileIdLinesGet

> FileFileIdLinesGet200Response fileFileIdLinesGet(fileId)

Retorna todas as linhas e seus respectivos campos (de forma não processada, apenas indicando os campos reconhecidos)

### Example

```javascript
import CnabOnline from 'cnab_online';

let apiInstance = new CnabOnline.FileApi();
let fileId = "fileId_example"; // String | ID Temporário gerado no endpoint file
apiInstance.fileFileIdLinesGet(fileId, (error, data, response) => {
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
 **fileId** | **String**| ID Temporário gerado no endpoint file | 

### Return type

[**FileFileIdLinesGet200Response**](FileFileIdLinesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileFileIdOccurrencesGet

> FileFileIdOccurrencesGet200Response fileFileIdOccurrencesGet(fileId)

Retorna as informações de baixa de boletos e outros tipos de ocorrências

### Example

```javascript
import CnabOnline from 'cnab_online';

let apiInstance = new CnabOnline.FileApi();
let fileId = "fileId_example"; // String | ID Temporário gerado no endpoint file
apiInstance.fileFileIdOccurrencesGet(fileId, (error, data, response) => {
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
 **fileId** | **String**| ID Temporário gerado no endpoint file | 

### Return type

[**FileFileIdOccurrencesGet200Response**](FileFileIdOccurrencesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## filePost

> FilePost200Response filePost(file)

Faz o upload de um arquivo

Processa um arquivo CNAB para obter informações sobre o mesmo. Retorna um ID temporário para o mesmo. 

### Example

```javascript
import CnabOnline from 'cnab_online';

let apiInstance = new CnabOnline.FileApi();
let file = "/path/to/file"; // File | Arquivo CNAB
apiInstance.filePost(file, (error, data, response) => {
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
 **file** | **File**| Arquivo CNAB | 

### Return type

[**FilePost200Response**](FilePost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

