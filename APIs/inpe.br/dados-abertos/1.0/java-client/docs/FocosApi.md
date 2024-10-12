# FocosApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getFocosCountResource**](FocosApi.md#getFocosCountResource) | **GET** /focos/count | Endpoint para retorno da contagem dos focos de calor |
| [**getFocosResource**](FocosApi.md#getFocosResource) | **GET** /focos/ | Endpoint para retorno dos dados de focos de calor |


<a id="getFocosCountResource"></a>
# **getFocosCountResource**
> getFocosCountResource(paisId, estadoId, municipioId, satelite)

Endpoint para retorno da contagem dos focos de calor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FocosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    FocosApi apiInstance = new FocosApi(defaultClient);
    Integer paisId = 56; // Integer | Código do país pelo qual será filtrado o resultado. Ver rotas auxiliares.
    Integer estadoId = 56; // Integer | Código do estado pelo qual será filtrado o resultado. Ver rotas auxiliares.
    Integer municipioId = 56; // Integer | Código do município pelo qual será filtrado o resultado. Ver rotas auxiliares.
    List<String> satelite = Arrays.asList(); // List<String> | Nome do satélte pelo qual será filtrado o resultado. Ver rotas auxiliares.
    try {
      apiInstance.getFocosCountResource(paisId, estadoId, municipioId, satelite);
    } catch (ApiException e) {
      System.err.println("Exception when calling FocosApi#getFocosCountResource");
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
| **paisId** | **Integer**| Código do país pelo qual será filtrado o resultado. Ver rotas auxiliares. | [optional] |
| **estadoId** | **Integer**| Código do estado pelo qual será filtrado o resultado. Ver rotas auxiliares. | [optional] |
| **municipioId** | **Integer**| Código do município pelo qual será filtrado o resultado. Ver rotas auxiliares. | [optional] |
| **satelite** | [**List&lt;String&gt;**](String.md)| Nome do satélte pelo qual será filtrado o resultado. Ver rotas auxiliares. | [optional] |

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

<a id="getFocosResource"></a>
# **getFocosResource**
> getFocosResource(paisId, estadoId, municipioId, satelite, xFields)

Endpoint para retorno dos dados de focos de calor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FocosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    FocosApi apiInstance = new FocosApi(defaultClient);
    Integer paisId = 56; // Integer | Código do país pelo qual será filtrado o resultado. Ver rotas auxiliares.
    Integer estadoId = 56; // Integer | Código do estado pelo qual será filtrado o resultado. Ver rotas auxiliares.
    Integer municipioId = 56; // Integer | Código do município pelo qual será filtrado o resultado. Ver rotas auxiliares.
    List<String> satelite = Arrays.asList(); // List<String> | Nome do satélte pelo qual será filtrado o resultado. Ver rotas auxiliares.
    String xFields = "xFields_example"; // String | An optional fields mask
    try {
      apiInstance.getFocosResource(paisId, estadoId, municipioId, satelite, xFields);
    } catch (ApiException e) {
      System.err.println("Exception when calling FocosApi#getFocosResource");
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
| **paisId** | **Integer**| Código do país pelo qual será filtrado o resultado. Ver rotas auxiliares. | [optional] |
| **estadoId** | **Integer**| Código do estado pelo qual será filtrado o resultado. Ver rotas auxiliares. | [optional] |
| **municipioId** | **Integer**| Código do município pelo qual será filtrado o resultado. Ver rotas auxiliares. | [optional] |
| **satelite** | [**List&lt;String&gt;**](String.md)| Nome do satélte pelo qual será filtrado o resultado. Ver rotas auxiliares. | [optional] |
| **xFields** | **String**| An optional fields mask | [optional] |

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

