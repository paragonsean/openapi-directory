# AuxiliarApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEstadosAuxiliarResource**](AuxiliarApi.md#getEstadosAuxiliarResource) | **GET** /auxiliar/estados | Endpoint para retorno dos dados de estados utilizados na filtragem de focos |
| [**getMunicipiosAuxiliarResource**](AuxiliarApi.md#getMunicipiosAuxiliarResource) | **GET** /auxiliar/municipios | Endpoint para retorno dos dados de municípios utilizados na filtragem de focos |
| [**getPaisesAuxiliarResource**](AuxiliarApi.md#getPaisesAuxiliarResource) | **GET** /auxiliar/paises | Endpoint para retorno dos dados de países utilizados na filtragem de focos |
| [**getSateliteAuxiliarResource**](AuxiliarApi.md#getSateliteAuxiliarResource) | **GET** /auxiliar/satelites | Endpoint para retorno dos dados de satélites utilizados na filtragem de focos |


<a id="getEstadosAuxiliarResource"></a>
# **getEstadosAuxiliarResource**
> getEstadosAuxiliarResource(paisId)

Endpoint para retorno dos dados de estados utilizados na filtragem de focos

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuxiliarApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    AuxiliarApi apiInstance = new AuxiliarApi(defaultClient);
    List<Integer> paisId = Arrays.asList(); // List<Integer> | Código do país pelo qual será filtrado o resultado. Ver rotas auxiliares.
    try {
      apiInstance.getEstadosAuxiliarResource(paisId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuxiliarApi#getEstadosAuxiliarResource");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **paisId** | [**List&lt;Integer&gt;**](Integer.md)| Código do país pelo qual será filtrado o resultado. Ver rotas auxiliares. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sucesso |  -  |
| **400** | Erro de validação |  -  |

<a id="getMunicipiosAuxiliarResource"></a>
# **getMunicipiosAuxiliarResource**
> getMunicipiosAuxiliarResource(paisId, estadoId)

Endpoint para retorno dos dados de municípios utilizados na filtragem de focos

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuxiliarApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    AuxiliarApi apiInstance = new AuxiliarApi(defaultClient);
    Integer paisId = 56; // Integer | Código do país pelo qual será filtrado o resultado. Ver rotas auxiliares.
    List<Integer> estadoId = Arrays.asList(); // List<Integer> | Código do estado pelo qual será filtrado o resultado. Ver rotas auxiliares.
    try {
      apiInstance.getMunicipiosAuxiliarResource(paisId, estadoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuxiliarApi#getMunicipiosAuxiliarResource");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **paisId** | **Integer**| Código do país pelo qual será filtrado o resultado. Ver rotas auxiliares. | |
| **estadoId** | [**List&lt;Integer&gt;**](Integer.md)| Código do estado pelo qual será filtrado o resultado. Ver rotas auxiliares. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sucesso |  -  |
| **400** | Erro de validação |  -  |

<a id="getPaisesAuxiliarResource"></a>
# **getPaisesAuxiliarResource**
> getPaisesAuxiliarResource()

Endpoint para retorno dos dados de países utilizados na filtragem de focos

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuxiliarApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    AuxiliarApi apiInstance = new AuxiliarApi(defaultClient);
    try {
      apiInstance.getPaisesAuxiliarResource();
    } catch (ApiException e) {
      System.err.println("Exception when calling AuxiliarApi#getPaisesAuxiliarResource");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sucesso |  -  |

<a id="getSateliteAuxiliarResource"></a>
# **getSateliteAuxiliarResource**
> getSateliteAuxiliarResource()

Endpoint para retorno dos dados de satélites utilizados na filtragem de focos

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuxiliarApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    AuxiliarApi apiInstance = new AuxiliarApi(defaultClient);
    try {
      apiInstance.getSateliteAuxiliarResource();
    } catch (ApiException e) {
      System.err.println("Exception when calling AuxiliarApi#getSateliteAuxiliarResource");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sucesso |  -  |

