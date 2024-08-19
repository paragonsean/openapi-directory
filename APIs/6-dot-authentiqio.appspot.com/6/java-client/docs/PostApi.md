# PostApi

All URIs are relative to *https://6-dot-authentiqio.appspot.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**keyRegister_0**](PostApi.md#keyRegister_0) | **POST** /key |  |
| [**keyUpdate_0**](PostApi.md#keyUpdate_0) | **POST** /key/{PK} |  |
| [**pushLoginRequest_0**](PostApi.md#pushLoginRequest_0) | **POST** /login |  |
| [**signConfirm_0**](PostApi.md#signConfirm_0) | **POST** /scope/{job} |  |
| [**signRequest_0**](PostApi.md#signRequest_0) | **POST** /scope |  |


<a id="keyRegister_0"></a>
# **keyRegister_0**
> KeyRegister201Response keyRegister_0(authentiqID)



Register a new ID &#x60;JWT(sub, devtoken)&#x60;  v5: &#x60;JWT(sub, pk, devtoken, ...)&#x60;  See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    PostApi apiInstance = new PostApi(defaultClient);
    AuthentiqID authentiqID = new AuthentiqID(); // AuthentiqID | Authentiq ID to register
    try {
      KeyRegister201Response result = apiInstance.keyRegister_0(authentiqID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostApi#keyRegister_0");
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
| **authentiqID** | [**AuthentiqID**](AuthentiqID.md)| Authentiq ID to register | |

### Return type

[**KeyRegister201Response**](KeyRegister201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/jwt
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successfully registered |  -  |
| **409** | Key already registered &#x60;duplicate-key&#x60; |  -  |
| **0** | Error response |  -  |

<a id="keyUpdate_0"></a>
# **keyUpdate_0**
> KeyBind200Response keyUpdate_0(PK, authentiqID)



update properties of an Authentiq ID. (not operational in v4; use PUT for now)  v5: POST issuer-signed email &amp; phone scopes in a self-signed JWT  See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    PostApi apiInstance = new PostApi(defaultClient);
    String PK = "PK_example"; // String | Public Signing Key - Authentiq ID (43 chars)
    AuthentiqID authentiqID = new AuthentiqID(); // AuthentiqID | Authentiq ID to register
    try {
      KeyBind200Response result = apiInstance.keyUpdate_0(PK, authentiqID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostApi#keyUpdate_0");
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
| **PK** | **String**| Public Signing Key - Authentiq ID (43 chars) | |
| **authentiqID** | [**AuthentiqID**](AuthentiqID.md)| Authentiq ID to register | |

### Return type

[**KeyBind200Response**](KeyBind200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/jwt
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated |  -  |
| **404** | Unknown key &#x60;unknown-key&#x60; |  -  |
| **0** | Error response |  -  |

<a id="pushLoginRequest_0"></a>
# **pushLoginRequest_0**
> PushLoginRequest200Response pushLoginRequest_0(paramCallback, pushToken)



push sign-in request See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    PostApi apiInstance = new PostApi(defaultClient);
    String paramCallback = "paramCallback_example"; // String | URI App will connect to
    PushToken pushToken = new PushToken(); // PushToken | Push Token.
    try {
      PushLoginRequest200Response result = apiInstance.pushLoginRequest_0(paramCallback, pushToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostApi#pushLoginRequest_0");
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
| **paramCallback** | **String**| URI App will connect to | |
| **pushToken** | [**PushToken**](PushToken.md)| Push Token. | |

### Return type

[**PushLoginRequest200Response**](PushLoginRequest200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/jwt
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **401** | Unauthorized for this callback audience &#x60;aud-error&#x60; or JWT should be self-signed &#x60;auth-error&#x60; |  -  |
| **0** | Error response |  -  |

<a id="signConfirm_0"></a>
# **signConfirm_0**
> KeyBind200Response signConfirm_0(job)



this is a scope confirmation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    PostApi apiInstance = new PostApi(defaultClient);
    String job = "job_example"; // String | Job ID (20 chars)
    try {
      KeyBind200Response result = apiInstance.signConfirm_0(job);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostApi#signConfirm_0");
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
| **job** | **String**| Job ID (20 chars) | |

### Return type

[**KeyBind200Response**](KeyBind200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Successfully confirmed |  -  |
| **401** | Confirmation error &#x60;auth-error&#x60; |  -  |
| **404** | Job not found &#x60;unknown-job&#x60; |  -  |
| **405** | JWT POSTed to scope &#x60;not-supported&#x60; |  -  |
| **0** | Error response |  -  |

<a id="signRequest_0"></a>
# **signRequest_0**
> SignRequest201Response signRequest_0(claims, test)



scope verification request See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    PostApi apiInstance = new PostApi(defaultClient);
    Claims claims = new Claims(); // Claims | Claims of scope
    Integer test = 56; // Integer | test only mode, using test issuer
    try {
      SignRequest201Response result = apiInstance.signRequest_0(claims, test);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostApi#signRequest_0");
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
| **claims** | [**Claims**](Claims.md)| Claims of scope | |
| **test** | **Integer**| test only mode, using test issuer | [optional] |

### Return type

[**SignRequest201Response**](SignRequest201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/jwt
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response |  -  |
| **429** | Too Many Requests on same address / number &#x60;rate-limit&#x60; |  -  |
| **0** | Error response |  -  |

