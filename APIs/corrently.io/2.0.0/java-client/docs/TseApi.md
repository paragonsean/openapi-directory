# TseApi

All URIs are relative to *https://api.corrently.io/v2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quittungTSEData_0**](TseApi.md#quittungTSEData_0) | **POST** /quittung/tsedata | Retrieve TSE (Technische Sicherheitseinrichtung) raw data  only for a given receipt (Strom-Quittung). |
| [**quittungTSE_0**](TseApi.md#quittungTSE_0) | **POST** /quittung/tse | Retrieve TSE (Technische Sicherheitseinrichtung) Data for a given receipt (Strom-Quittung). |
| [**quittungTSEsignature_0**](TseApi.md#quittungTSEsignature_0) | **POST** /quittung/tsesignature | Retrieve TSE (Technische Sicherheitseinrichtung) Signature only for a given receipt (Strom-Quittung). |
| [**quittungZugferd_0**](TseApi.md#quittungZugferd_0) | **GET** /quittung/zugferd | Retrieve Zugferd XML for a given receipt (Strom-Quittung). |


<a id="quittungTSEData_0"></a>
# **quittungTSEData_0**
> quittungTSEData_0(account)

Retrieve TSE (Technische Sicherheitseinrichtung) raw data  only for a given receipt (Strom-Quittung).

Allows to retrieve input string for a signing process. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.corrently.io/v2.0");

    TseApi apiInstance = new TseApi(defaultClient);
    String account = "account_example"; // String | Quittung Identifier  (serialnumber generated during receipt generation process)
    try {
      apiInstance.quittungTSEData_0(account);
    } catch (ApiException e) {
      System.err.println("Exception when calling TseApi#quittungTSEData_0");
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
| **account** | **String**| Quittung Identifier  (serialnumber generated during receipt generation process) | [optional] |

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
| **200** | Success |  -  |

<a id="quittungTSE_0"></a>
# **quittungTSE_0**
> QuittungTSE200Response quittungTSE_0(account)

Retrieve TSE (Technische Sicherheitseinrichtung) Data for a given receipt (Strom-Quittung).

Allows to retrieve all relevant data assiciated to a TSE service call. E.q. Input parameters, public key and signature. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.corrently.io/v2.0");

    TseApi apiInstance = new TseApi(defaultClient);
    String account = "account_example"; // String | Quittung Identifier  (serialnumber generated during receipt generation process)
    try {
      QuittungTSE200Response result = apiInstance.quittungTSE_0(account);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TseApi#quittungTSE_0");
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
| **account** | **String**| Quittung Identifier  (serialnumber generated during receipt generation process) | [optional] |

### Return type

[**QuittungTSE200Response**](QuittungTSE200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="quittungTSEsignature_0"></a>
# **quittungTSEsignature_0**
> quittungTSEsignature_0(account)

Retrieve TSE (Technische Sicherheitseinrichtung) Signature only for a given receipt (Strom-Quittung).

Allows to retrieve digital signature for a given receipt. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.corrently.io/v2.0");

    TseApi apiInstance = new TseApi(defaultClient);
    String account = "account_example"; // String | Quittung Identifier  (serialnumber generated during receipt generation process)
    try {
      apiInstance.quittungTSEsignature_0(account);
    } catch (ApiException e) {
      System.err.println("Exception when calling TseApi#quittungTSEsignature_0");
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
| **account** | **String**| Quittung Identifier  (serialnumber generated during receipt generation process) | [optional] |

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
| **200** | Success |  -  |

<a id="quittungZugferd_0"></a>
# **quittungZugferd_0**
> quittungZugferd_0(account)

Retrieve Zugferd XML for a given receipt (Strom-Quittung).

Allows to retrieve XML of the zugferd invoice. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.corrently.io/v2.0");

    TseApi apiInstance = new TseApi(defaultClient);
    String account = "account_example"; // String | Quittung Identifier  (serialnumber generated during receipt generation process)
    try {
      apiInstance.quittungZugferd_0(account);
    } catch (ApiException e) {
      System.err.println("Exception when calling TseApi#quittungZugferd_0");
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
| **account** | **String**| Quittung Identifier  (serialnumber generated during receipt generation process) | [optional] |

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
| **200** | Success |  -  |

