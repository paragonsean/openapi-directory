# ExportApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**exportCsvRegistrierkassenRegistrierkasseUuidBelegeGet**](ExportApi.md#exportCsvRegistrierkassenRegistrierkasseUuidBelegeGet) | **GET** /export/csv/registrierkassen/{registrierkasseUuid}/belege |  |
| [**exportDep131RegistrierkassenRegistrierkasseUuidBelegeGet**](ExportApi.md#exportDep131RegistrierkassenRegistrierkasseUuidBelegeGet) | **GET** /export/dep131/registrierkassen/{registrierkasseUuid}/belege |  |
| [**exportDep7RegistrierkassenRegistrierkasseUuidBelegeGet**](ExportApi.md#exportDep7RegistrierkassenRegistrierkasseUuidBelegeGet) | **GET** /export/dep7/registrierkassen/{registrierkasseUuid}/belege |  |
| [**exportGobdRegistrierkassenRegistrierkasseUuidGet**](ExportApi.md#exportGobdRegistrierkassenRegistrierkasseUuidGet) | **GET** /export/gobd/registrierkassen/{registrierkasseUuid} |  |
| [**exportHtmlBelegeBelegUuidGet**](ExportApi.md#exportHtmlBelegeBelegUuidGet) | **GET** /export/html/belege/{belegUuid} |  |
| [**exportPdfBelegeBelegUuidGet**](ExportApi.md#exportPdfBelegeBelegUuidGet) | **GET** /export/pdf/belege/{belegUuid} |  |
| [**exportQrBelegeBelegUuidGet**](ExportApi.md#exportQrBelegeBelegUuidGet) | **GET** /export/qr/belege/{belegUuid} |  |
| [**exportThermalPrintBelegeBelegUuidGet**](ExportApi.md#exportThermalPrintBelegeBelegUuidGet) | **GET** /export/thermal-print/belege/{belegUuid} |  |
| [**exportXlsRegistrierkassenRegistrierkasseUuidBelegeGet**](ExportApi.md#exportXlsRegistrierkassenRegistrierkasseUuidBelegeGet) | **GET** /export/xls/registrierkassen/{registrierkasseUuid}/belege |  |


<a id="exportCsvRegistrierkassenRegistrierkasseUuidBelegeGet"></a>
# **exportCsvRegistrierkassenRegistrierkasseUuidBelegeGet**
> exportCsvRegistrierkassenRegistrierkasseUuidBelegeGet(registrierkasseUuid, before, after, posten)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ExportApi apiInstance = new ExportApi(defaultClient);
    String registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse` to export.
    String before = "before_example"; // String | Only return results that were saved before the specified date-time string (i.e., anything that `Date.parse()` can parse).
    String after = "after_example"; // String | Only return results that were saved after the specified date-time string (i.e., anything that `Date.parse()` can parse).
    Boolean posten = true; // Boolean | Export `Posten` instead of `Belegdaten`.
    try {
      apiInstance.exportCsvRegistrierkassenRegistrierkasseUuidBelegeGet(registrierkasseUuid, before, after, posten);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportApi#exportCsvRegistrierkassenRegistrierkasseUuidBelegeGet");
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
| **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to export. | |
| **before** | **String**| Only return results that were saved before the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] |
| **after** | **String**| Only return results that were saved after the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] |
| **posten** | **Boolean**| Export &#x60;Posten&#x60; instead of &#x60;Belegdaten&#x60;. | [optional] |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The exported data of a particular &#x60;Registrierkasse&#x60; in its CSV representation. |  -  |

<a id="exportDep131RegistrierkassenRegistrierkasseUuidBelegeGet"></a>
# **exportDep131RegistrierkassenRegistrierkasseUuidBelegeGet**
> exportDep131RegistrierkassenRegistrierkasseUuidBelegeGet(registrierkasseUuid, before, after)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ExportApi apiInstance = new ExportApi(defaultClient);
    String registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse` to export.
    String before = "before_example"; // String | Only return results that were saved before the specified date-time string (i.e., anything that `Date.parse()` can parse).
    String after = "after_example"; // String | Only return results that were saved after the specified date-time string (i.e., anything that `Date.parse()` can parse).
    try {
      apiInstance.exportDep131RegistrierkassenRegistrierkasseUuidBelegeGet(registrierkasseUuid, before, after);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportApi#exportDep131RegistrierkassenRegistrierkasseUuidBelegeGet");
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
| **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to export. | |
| **before** | **String**| Only return results that were saved before the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] |
| **after** | **String**| Only return results that were saved after the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The exported data of a particular &#x60;Registrierkasse&#x60; in its DEP131 / CSV representation. |  -  |

<a id="exportDep7RegistrierkassenRegistrierkasseUuidBelegeGet"></a>
# **exportDep7RegistrierkassenRegistrierkasseUuidBelegeGet**
> exportDep7RegistrierkassenRegistrierkasseUuidBelegeGet(registrierkasseUuid, before, after)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ExportApi apiInstance = new ExportApi(defaultClient);
    String registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse` to export.
    String before = "before_example"; // String | Only return results that were saved before the specified date-time string (i.e., anything that `Date.parse()` can parse).
    String after = "after_example"; // String | Only return results that were saved after the specified date-time string (i.e., anything that `Date.parse()` can parse).
    try {
      apiInstance.exportDep7RegistrierkassenRegistrierkasseUuidBelegeGet(registrierkasseUuid, before, after);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportApi#exportDep7RegistrierkassenRegistrierkasseUuidBelegeGet");
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
| **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to export. | |
| **before** | **String**| Only return results that were saved before the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] |
| **after** | **String**| Only return results that were saved after the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The exported data of a particular &#x60;Registrierkasse&#x60; in its DEP7 representation. |  -  |

<a id="exportGobdRegistrierkassenRegistrierkasseUuidGet"></a>
# **exportGobdRegistrierkassenRegistrierkasseUuidGet**
> exportGobdRegistrierkassenRegistrierkasseUuidGet(registrierkasseUuid, before, after)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ExportApi apiInstance = new ExportApi(defaultClient);
    String registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse` to export.
    String before = "before_example"; // String | Only return results that were saved before the specified date-time string (i.e., anything that `Date.parse()` can parse).
    String after = "after_example"; // String | Only return results that were saved after the specified date-time string (i.e., anything that `Date.parse()` can parse).
    try {
      apiInstance.exportGobdRegistrierkassenRegistrierkasseUuidGet(registrierkasseUuid, before, after);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportApi#exportGobdRegistrierkassenRegistrierkasseUuidGet");
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
| **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to export. | |
| **before** | **String**| Only return results that were saved before the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] |
| **after** | **String**| Only return results that were saved after the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The exported data of a particular &#x60;Registrierkasse&#x60; in its GoBD representation. |  -  |

<a id="exportHtmlBelegeBelegUuidGet"></a>
# **exportHtmlBelegeBelegUuidGet**
> exportHtmlBelegeBelegUuidGet(belegUuid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");

    ExportApi apiInstance = new ExportApi(defaultClient);
    String belegUuid = "belegUuid_example"; // String | The `_uuid` of a particular `Beleg` to export.
    try {
      apiInstance.exportHtmlBelegeBelegUuidGet(belegUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportApi#exportHtmlBelegeBelegUuidGet");
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
| **belegUuid** | **String**| The &#x60;_uuid&#x60; of a particular &#x60;Beleg&#x60; to export. | |

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
| **200** | A particular &#x60;Beleg&#x60; in its HTML representation. |  -  |

<a id="exportPdfBelegeBelegUuidGet"></a>
# **exportPdfBelegeBelegUuidGet**
> exportPdfBelegeBelegUuidGet(belegUuid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");

    ExportApi apiInstance = new ExportApi(defaultClient);
    String belegUuid = "belegUuid_example"; // String | The `_uuid` of a particular `Beleg` to export.
    try {
      apiInstance.exportPdfBelegeBelegUuidGet(belegUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportApi#exportPdfBelegeBelegUuidGet");
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
| **belegUuid** | **String**| The &#x60;_uuid&#x60; of a particular &#x60;Beleg&#x60; to export. | |

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
| **200** | A particular &#x60;Beleg&#x60; in its PDF representation. |  -  |

<a id="exportQrBelegeBelegUuidGet"></a>
# **exportQrBelegeBelegUuidGet**
> exportQrBelegeBelegUuidGet(belegUuid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");

    ExportApi apiInstance = new ExportApi(defaultClient);
    String belegUuid = "belegUuid_example"; // String | The `_uuid` of a particular `Beleg` to export.
    try {
      apiInstance.exportQrBelegeBelegUuidGet(belegUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportApi#exportQrBelegeBelegUuidGet");
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
| **belegUuid** | **String**| The &#x60;_uuid&#x60; of a particular &#x60;Beleg&#x60; to export. | |

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
| **200** | The RKSV QR-Code as PNG file. |  -  |

<a id="exportThermalPrintBelegeBelegUuidGet"></a>
# **exportThermalPrintBelegeBelegUuidGet**
> exportThermalPrintBelegeBelegUuidGet(belegUuid, qr, width, dialect, encoding)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");

    ExportApi apiInstance = new ExportApi(defaultClient);
    String belegUuid = "belegUuid_example"; // String | The `_uuid` of a particular `Beleg` to export.
    Boolean qr = true; // Boolean | Should the RKSV QR code should be rendered?
    Integer width = 42; // Integer | Number of characters per line.
    String dialect = "escpos"; // String | The thermal printer dialect.
    String encoding = "raw"; // String | The encoding of the binary data.
    try {
      apiInstance.exportThermalPrintBelegeBelegUuidGet(belegUuid, qr, width, dialect, encoding);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportApi#exportThermalPrintBelegeBelegUuidGet");
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
| **belegUuid** | **String**| The &#x60;_uuid&#x60; of a particular &#x60;Beleg&#x60; to export. | |
| **qr** | **Boolean**| Should the RKSV QR code should be rendered? | [optional] [default to true] |
| **width** | **Integer**| Number of characters per line. | [optional] [default to 42] |
| **dialect** | **String**| The thermal printer dialect. | [optional] [default to escpos] [enum: escpos, escposlite, star, text] |
| **encoding** | **String**| The encoding of the binary data. | [optional] [default to raw] [enum: raw, base64] |

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
| **200** | A particular &#x60;Beleg&#x60; in its ESC/POS or STAR representation. |  -  |

<a id="exportXlsRegistrierkassenRegistrierkasseUuidBelegeGet"></a>
# **exportXlsRegistrierkassenRegistrierkasseUuidBelegeGet**
> exportXlsRegistrierkassenRegistrierkasseUuidBelegeGet(registrierkasseUuid, before, after)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ExportApi apiInstance = new ExportApi(defaultClient);
    String registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse` to export.
    String before = "before_example"; // String | Only return results that were saved before the specified date-time string (i.e., anything that `Date.parse()` can parse).
    String after = "after_example"; // String | Only return results that were saved after the specified date-time string (i.e., anything that `Date.parse()` can parse).
    try {
      apiInstance.exportXlsRegistrierkassenRegistrierkasseUuidBelegeGet(registrierkasseUuid, before, after);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportApi#exportXlsRegistrierkassenRegistrierkasseUuidBelegeGet");
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
| **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to export. | |
| **before** | **String**| Only return results that were saved before the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] |
| **after** | **String**| Only return results that were saved after the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The exported data of a particular &#x60;Registrierkasse&#x60; in its Microsoft Excel representation. |  -  |

