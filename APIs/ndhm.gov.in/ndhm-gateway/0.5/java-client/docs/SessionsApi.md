# SessionsApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v05CertsGet**](SessionsApi.md#v05CertsGet) | **GET** /v0.5/certs | Get certs for JWT verification |
| [**v05SessionsPost**](SessionsApi.md#v05SessionsPost) | **POST** /v0.5/sessions | Get access token |
| [**v05WellKnownOpenidConfigurationGet**](SessionsApi.md#v05WellKnownOpenidConfigurationGet) | **GET** /v0.5/.well-known/openid-configuration | Get openid configuration |


<a id="v05CertsGet"></a>
# **v05CertsGet**
> Certs v05CertsGet()

Get certs for JWT verification

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    try {
      Certs result = apiInstance.v05CertsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#v05CertsGet");
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

[**Certs**](Certs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | **Causes:**   * Invalid consent request id  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

<a id="v05SessionsPost"></a>
# **v05SessionsPost**
> SessionResponse v05SessionsPost(sessionRequest)

Get access token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    SessionRequest sessionRequest = new SessionRequest(); // SessionRequest | 
    try {
      SessionResponse result = apiInstance.v05SessionsPost(sessionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#v05SessionsPost");
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
| **sessionRequest** | [**SessionRequest**](SessionRequest.md)|  | |

### Return type

[**SessionResponse**](SessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | **Causes:**   * Invalid client Id or secret.  |  -  |
| **404** | **Causes:**   * Invalid consent request id  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

<a id="v05WellKnownOpenidConfigurationGet"></a>
# **v05WellKnownOpenidConfigurationGet**
> OpenIdConfiguration v05WellKnownOpenidConfigurationGet()

Get openid configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    try {
      OpenIdConfiguration result = apiInstance.v05WellKnownOpenidConfigurationGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#v05WellKnownOpenidConfigurationGet");
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

[**OpenIdConfiguration**](OpenIdConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | **Causes:**   * Invalid consent request id  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

