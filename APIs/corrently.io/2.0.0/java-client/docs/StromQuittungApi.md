# StromQuittungApi

All URIs are relative to *https://api.corrently.io/v2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quittungComit**](StromQuittungApi.md#quittungComit) | **POST** /quittung/commit | Finishs a collection of data and finalizes receipt. Use this method after collecting all data via quittung/prepare |
| [**quittungCreate**](StromQuittungApi.md#quittungCreate) | **POST** /quittung/create | Create a receipt for an energy delivery (only valid in Germany). |
| [**quittungPrepare**](StromQuittungApi.md#quittungPrepare) | **POST** /quittung/prepare | Allows to collect data with several requests (or a single) for a receipt. |
| [**quittungTSE**](StromQuittungApi.md#quittungTSE) | **POST** /quittung/tse | Retrieve TSE (Technische Sicherheitseinrichtung) Data for a given receipt (Strom-Quittung). |
| [**quittungTSEData**](StromQuittungApi.md#quittungTSEData) | **POST** /quittung/tsedata | Retrieve TSE (Technische Sicherheitseinrichtung) raw data  only for a given receipt (Strom-Quittung). |
| [**quittungTSEsignature**](StromQuittungApi.md#quittungTSEsignature) | **POST** /quittung/tsesignature | Retrieve TSE (Technische Sicherheitseinrichtung) Signature only for a given receipt (Strom-Quittung). |
| [**quittungZugferd**](StromQuittungApi.md#quittungZugferd) | **GET** /quittung/zugferd | Retrieve Zugferd XML for a given receipt (Strom-Quittung). |


<a id="quittungComit"></a>
# **quittungComit**
> String quittungComit(quittungComitRequest)

Finishs a collection of data and finalizes receipt. Use this method after collecting all data via quittung/prepare

Uses collected fields or provided fields to create a final receipt (Strom-Quittung). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StromQuittungApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.corrently.io/v2.0");

    StromQuittungApi apiInstance = new StromQuittungApi(defaultClient);
    QuittungComitRequest quittungComitRequest = new QuittungComitRequest(); // QuittungComitRequest | 
    try {
      String result = apiInstance.quittungComit(quittungComitRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StromQuittungApi#quittungComit");
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
| **quittungComitRequest** | [**QuittungComitRequest**](QuittungComitRequest.md)|  | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="quittungCreate"></a>
# **quittungCreate**
> String quittungCreate(quittungCreateRequest)

Create a receipt for an energy delivery (only valid in Germany).

Creates a full featured receipt (Quittung) for an energy delivery as it appears on a charging session or similar events. Allows to embed receipt generation directly into external services. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StromQuittungApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.corrently.io/v2.0");

    StromQuittungApi apiInstance = new StromQuittungApi(defaultClient);
    QuittungCreateRequest quittungCreateRequest = new QuittungCreateRequest(); // QuittungCreateRequest | 
    try {
      String result = apiInstance.quittungCreate(quittungCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StromQuittungApi#quittungCreate");
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
| **quittungCreateRequest** | [**QuittungCreateRequest**](QuittungCreateRequest.md)|  | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="quittungPrepare"></a>
# **quittungPrepare**
> String quittungPrepare(quittungComitRequest)

Allows to collect data with several requests (or a single) for a receipt.

During the first call an account parameter will be returned within the result object. Any other parameter will be set inside the preperation. If account is put into body/request in following requests, the existing collection will be extended/updated with the provided body parameters/values. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StromQuittungApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.corrently.io/v2.0");

    StromQuittungApi apiInstance = new StromQuittungApi(defaultClient);
    QuittungComitRequest quittungComitRequest = new QuittungComitRequest(); // QuittungComitRequest | 
    try {
      String result = apiInstance.quittungPrepare(quittungComitRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StromQuittungApi#quittungPrepare");
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
| **quittungComitRequest** | [**QuittungComitRequest**](QuittungComitRequest.md)|  | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="quittungTSE"></a>
# **quittungTSE**
> QuittungTSE200Response quittungTSE(account)

Retrieve TSE (Technische Sicherheitseinrichtung) Data for a given receipt (Strom-Quittung).

Allows to retrieve all relevant data assiciated to a TSE service call. E.q. Input parameters, public key and signature. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StromQuittungApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.corrently.io/v2.0");

    StromQuittungApi apiInstance = new StromQuittungApi(defaultClient);
    String account = "account_example"; // String | Quittung Identifier  (serialnumber generated during receipt generation process)
    try {
      QuittungTSE200Response result = apiInstance.quittungTSE(account);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StromQuittungApi#quittungTSE");
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

<a id="quittungTSEData"></a>
# **quittungTSEData**
> quittungTSEData(account)

Retrieve TSE (Technische Sicherheitseinrichtung) raw data  only for a given receipt (Strom-Quittung).

Allows to retrieve input string for a signing process. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StromQuittungApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.corrently.io/v2.0");

    StromQuittungApi apiInstance = new StromQuittungApi(defaultClient);
    String account = "account_example"; // String | Quittung Identifier  (serialnumber generated during receipt generation process)
    try {
      apiInstance.quittungTSEData(account);
    } catch (ApiException e) {
      System.err.println("Exception when calling StromQuittungApi#quittungTSEData");
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

<a id="quittungTSEsignature"></a>
# **quittungTSEsignature**
> quittungTSEsignature(account)

Retrieve TSE (Technische Sicherheitseinrichtung) Signature only for a given receipt (Strom-Quittung).

Allows to retrieve digital signature for a given receipt. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StromQuittungApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.corrently.io/v2.0");

    StromQuittungApi apiInstance = new StromQuittungApi(defaultClient);
    String account = "account_example"; // String | Quittung Identifier  (serialnumber generated during receipt generation process)
    try {
      apiInstance.quittungTSEsignature(account);
    } catch (ApiException e) {
      System.err.println("Exception when calling StromQuittungApi#quittungTSEsignature");
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

<a id="quittungZugferd"></a>
# **quittungZugferd**
> quittungZugferd(account)

Retrieve Zugferd XML for a given receipt (Strom-Quittung).

Allows to retrieve XML of the zugferd invoice. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StromQuittungApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.corrently.io/v2.0");

    StromQuittungApi apiInstance = new StromQuittungApi(defaultClient);
    String account = "account_example"; // String | Quittung Identifier  (serialnumber generated during receipt generation process)
    try {
      apiInstance.quittungZugferd(account);
    } catch (ApiException e) {
      System.err.println("Exception when calling StromQuittungApi#quittungZugferd");
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

