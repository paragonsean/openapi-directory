# DadosAbertosApi.FocosApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFocosCountResource**](FocosApi.md#getFocosCountResource) | **GET** /focos/count | Endpoint para retorno da contagem dos focos de calor
[**getFocosResource**](FocosApi.md#getFocosResource) | **GET** /focos/ | Endpoint para retorno dos dados de focos de calor



## getFocosCountResource

> getFocosCountResource(opts)

Endpoint para retorno da contagem dos focos de calor

### Example

```javascript
import DadosAbertosApi from 'dados_abertos_api';

let apiInstance = new DadosAbertosApi.FocosApi();
let opts = {
  'paisId': 56, // Number | Código do país pelo qual será filtrado o resultado. Ver rotas auxiliares.
  'estadoId': 56, // Number | Código do estado pelo qual será filtrado o resultado. Ver rotas auxiliares.
  'municipioId': 56, // Number | Código do município pelo qual será filtrado o resultado. Ver rotas auxiliares.
  'satelite': ["null"] // [String] | Nome do satélte pelo qual será filtrado o resultado. Ver rotas auxiliares.
};
apiInstance.getFocosCountResource(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paisId** | **Number**| Código do país pelo qual será filtrado o resultado. Ver rotas auxiliares. | [optional] 
 **estadoId** | **Number**| Código do estado pelo qual será filtrado o resultado. Ver rotas auxiliares. | [optional] 
 **municipioId** | **Number**| Código do município pelo qual será filtrado o resultado. Ver rotas auxiliares. | [optional] 
 **satelite** | [**[String]**](String.md)| Nome do satélte pelo qual será filtrado o resultado. Ver rotas auxiliares. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getFocosResource

> getFocosResource(opts)

Endpoint para retorno dos dados de focos de calor

### Example

```javascript
import DadosAbertosApi from 'dados_abertos_api';

let apiInstance = new DadosAbertosApi.FocosApi();
let opts = {
  'paisId': 56, // Number | Código do país pelo qual será filtrado o resultado. Ver rotas auxiliares.
  'estadoId': 56, // Number | Código do estado pelo qual será filtrado o resultado. Ver rotas auxiliares.
  'municipioId': 56, // Number | Código do município pelo qual será filtrado o resultado. Ver rotas auxiliares.
  'satelite': ["null"], // [String] | Nome do satélte pelo qual será filtrado o resultado. Ver rotas auxiliares.
  'xFields': "xFields_example" // String | An optional fields mask
};
apiInstance.getFocosResource(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paisId** | **Number**| Código do país pelo qual será filtrado o resultado. Ver rotas auxiliares. | [optional] 
 **estadoId** | **Number**| Código do estado pelo qual será filtrado o resultado. Ver rotas auxiliares. | [optional] 
 **municipioId** | **Number**| Código do município pelo qual será filtrado o resultado. Ver rotas auxiliares. | [optional] 
 **satelite** | [**[String]**](String.md)| Nome do satélte pelo qual será filtrado o resultado. Ver rotas auxiliares. | [optional] 
 **xFields** | **String**| An optional fields mask | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

