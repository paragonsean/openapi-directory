# FileApi

All URIs are relative to *https://cnab-online.herokuapp.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fileFileIdGet**](FileApi.md#fileFileIdGet) | **GET** /file/{fileId} | Retorna as informações básicas de um arquivo previamente processado |
| [**fileFileIdLinesGet**](FileApi.md#fileFileIdLinesGet) | **GET** /file/{fileId}/lines | Retorna todas as linhas e seus respectivos campos (de forma não processada, apenas indicando os campos reconhecidos) |
| [**fileFileIdOccurrencesGet**](FileApi.md#fileFileIdOccurrencesGet) | **GET** /file/{fileId}/occurrences | Retorna as informações de baixa de boletos e outros tipos de ocorrências |
| [**filePost**](FileApi.md#filePost) | **POST** /file | Faz o upload de um arquivo |


<a id="fileFileIdGet"></a>
# **fileFileIdGet**
> FilePost200Response fileFileIdGet(fileId)

Retorna as informações básicas de um arquivo previamente processado

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cnab-online.herokuapp.com/v1");

    FileApi apiInstance = new FileApi(defaultClient);
    String fileId = "fileId_example"; // String | ID Temporário gerado no endpoint file
    try {
      FilePost200Response result = apiInstance.fileFileIdGet(fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileApi#fileFileIdGet");
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
| **fileId** | **String**| ID Temporário gerado no endpoint file | |

### Return type

[**FilePost200Response**](FilePost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Informações básicas do arquivo |  -  |
| **0** | Unexpected error |  -  |

<a id="fileFileIdLinesGet"></a>
# **fileFileIdLinesGet**
> FileFileIdLinesGet200Response fileFileIdLinesGet(fileId)

Retorna todas as linhas e seus respectivos campos (de forma não processada, apenas indicando os campos reconhecidos)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cnab-online.herokuapp.com/v1");

    FileApi apiInstance = new FileApi(defaultClient);
    String fileId = "fileId_example"; // String | ID Temporário gerado no endpoint file
    try {
      FileFileIdLinesGet200Response result = apiInstance.fileFileIdLinesGet(fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileApi#fileFileIdLinesGet");
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
| **fileId** | **String**| ID Temporário gerado no endpoint file | |

### Return type

[**FileFileIdLinesGet200Response**](FileFileIdLinesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Informações básicas do arquivo |  -  |
| **0** | Unexpected error |  -  |

<a id="fileFileIdOccurrencesGet"></a>
# **fileFileIdOccurrencesGet**
> FileFileIdOccurrencesGet200Response fileFileIdOccurrencesGet(fileId)

Retorna as informações de baixa de boletos e outros tipos de ocorrências

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cnab-online.herokuapp.com/v1");

    FileApi apiInstance = new FileApi(defaultClient);
    String fileId = "fileId_example"; // String | ID Temporário gerado no endpoint file
    try {
      FileFileIdOccurrencesGet200Response result = apiInstance.fileFileIdOccurrencesGet(fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileApi#fileFileIdOccurrencesGet");
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
| **fileId** | **String**| ID Temporário gerado no endpoint file | |

### Return type

[**FileFileIdOccurrencesGet200Response**](FileFileIdOccurrencesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Informações básicas do arquivo |  -  |
| **0** | Unexpected error |  -  |

<a id="filePost"></a>
# **filePost**
> FilePost200Response filePost(_file)

Faz o upload de um arquivo

Processa um arquivo CNAB para obter informações sobre o mesmo. Retorna um ID temporário para o mesmo. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cnab-online.herokuapp.com/v1");

    FileApi apiInstance = new FileApi(defaultClient);
    File _file = new File("/path/to/file"); // File | Arquivo CNAB
    try {
      FilePost200Response result = apiInstance.filePost(_file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileApi#filePost");
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
| **_file** | **File**| Arquivo CNAB | |

### Return type

[**FilePost200Response**](FilePost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Informações básicas do arquivo |  -  |
| **0** | Unexpected error |  -  |

