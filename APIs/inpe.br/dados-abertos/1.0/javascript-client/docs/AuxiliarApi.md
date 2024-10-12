# DadosAbertosApi.AuxiliarApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEstadosAuxiliarResource**](AuxiliarApi.md#getEstadosAuxiliarResource) | **GET** /auxiliar/estados | Endpoint para retorno dos dados de estados utilizados na filtragem de focos
[**getMunicipiosAuxiliarResource**](AuxiliarApi.md#getMunicipiosAuxiliarResource) | **GET** /auxiliar/municipios | Endpoint para retorno dos dados de municípios utilizados na filtragem de focos
[**getPaisesAuxiliarResource**](AuxiliarApi.md#getPaisesAuxiliarResource) | **GET** /auxiliar/paises | Endpoint para retorno dos dados de países utilizados na filtragem de focos
[**getSateliteAuxiliarResource**](AuxiliarApi.md#getSateliteAuxiliarResource) | **GET** /auxiliar/satelites | Endpoint para retorno dos dados de satélites utilizados na filtragem de focos



## getEstadosAuxiliarResource

> getEstadosAuxiliarResource(opts)

Endpoint para retorno dos dados de estados utilizados na filtragem de focos

### Example

```javascript
import DadosAbertosApi from 'dados_abertos_api';

let apiInstance = new DadosAbertosApi.AuxiliarApi();
let opts = {
  'paisId': [null] // [Number] | Código do país pelo qual será filtrado o resultado. Ver rotas auxiliares.
};
apiInstance.getEstadosAuxiliarResource(opts, (error, data, response) => {
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
 **paisId** | [**[Number]**](Number.md)| Código do país pelo qual será filtrado o resultado. Ver rotas auxiliares. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getMunicipiosAuxiliarResource

> getMunicipiosAuxiliarResource(paisId, opts)

Endpoint para retorno dos dados de municípios utilizados na filtragem de focos

### Example

```javascript
import DadosAbertosApi from 'dados_abertos_api';

let apiInstance = new DadosAbertosApi.AuxiliarApi();
let paisId = 56; // Number | Código do país pelo qual será filtrado o resultado. Ver rotas auxiliares.
let opts = {
  'estadoId': [null] // [Number] | Código do estado pelo qual será filtrado o resultado. Ver rotas auxiliares.
};
apiInstance.getMunicipiosAuxiliarResource(paisId, opts, (error, data, response) => {
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
 **paisId** | **Number**| Código do país pelo qual será filtrado o resultado. Ver rotas auxiliares. | 
 **estadoId** | [**[Number]**](Number.md)| Código do estado pelo qual será filtrado o resultado. Ver rotas auxiliares. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPaisesAuxiliarResource

> getPaisesAuxiliarResource()

Endpoint para retorno dos dados de países utilizados na filtragem de focos

### Example

```javascript
import DadosAbertosApi from 'dados_abertos_api';

let apiInstance = new DadosAbertosApi.AuxiliarApi();
apiInstance.getPaisesAuxiliarResource((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSateliteAuxiliarResource

> getSateliteAuxiliarResource()

Endpoint para retorno dos dados de satélites utilizados na filtragem de focos

### Example

```javascript
import DadosAbertosApi from 'dados_abertos_api';

let apiInstance = new DadosAbertosApi.AuxiliarApi();
apiInstance.getSateliteAuxiliarResource((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

