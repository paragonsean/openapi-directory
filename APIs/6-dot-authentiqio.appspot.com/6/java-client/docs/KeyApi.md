# KeyApi

All URIs are relative to *https://6-dot-authentiqio.appspot.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**keyBind**](KeyApi.md#keyBind) | **PUT** /key/{PK} |  |
| [**keyPKHead**](KeyApi.md#keyPKHead) | **HEAD** /key/{PK} |  |
| [**keyRegister**](KeyApi.md#keyRegister) | **POST** /key |  |
| [**keyRetrieve**](KeyApi.md#keyRetrieve) | **GET** /key/{PK} |  |
| [**keyRevoke**](KeyApi.md#keyRevoke) | **DELETE** /key/{PK} |  |
| [**keyRevokeNosecret**](KeyApi.md#keyRevokeNosecret) | **DELETE** /key |  |
| [**keyUpdate**](KeyApi.md#keyUpdate) | **POST** /key/{PK} |  |


<a id="keyBind"></a>
# **keyBind**
> KeyBind200Response keyBind(PK, authentiqID)



Update Authentiq ID by replacing the object.  v4: &#x60;JWT(sub,email,phone)&#x60; to bind email/phone hash;   v5: POST issuer-signed email &amp; phone scopes and PUT to update registration &#x60;JWT(sub, pk, devtoken, ...)&#x60;  See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    KeyApi apiInstance = new KeyApi(defaultClient);
    String PK = "PK_example"; // String | Public Signing Key - Authentiq ID (43 chars)
    AuthentiqID authentiqID = new AuthentiqID(); // AuthentiqID | Authentiq ID to register
    try {
      KeyBind200Response result = apiInstance.keyBind(PK, authentiqID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyApi#keyBind");
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
| **409** | Already bound to another key &#x60;duplicate-hash&#x60; |  -  |
| **0** | Error response |  -  |

<a id="keyPKHead"></a>
# **keyPKHead**
> keyPKHead(PK)



HEAD info on Authentiq ID 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    KeyApi apiInstance = new KeyApi(defaultClient);
    String PK = "PK_example"; // String | Public Signing Key - Authentiq ID (43 chars)
    try {
      apiInstance.keyPKHead(PK);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyApi#keyPKHead");
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Key exists |  -  |
| **404** | Unknown key &#x60;unknown-key&#x60; |  -  |
| **410** | Key is revoked &#x60;revoked-key&#x60; |  -  |
| **0** | Error response |  -  |

<a id="keyRegister"></a>
# **keyRegister**
> KeyRegister201Response keyRegister(authentiqID)



Register a new ID &#x60;JWT(sub, devtoken)&#x60;  v5: &#x60;JWT(sub, pk, devtoken, ...)&#x60;  See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    KeyApi apiInstance = new KeyApi(defaultClient);
    AuthentiqID authentiqID = new AuthentiqID(); // AuthentiqID | Authentiq ID to register
    try {
      KeyRegister201Response result = apiInstance.keyRegister(authentiqID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyApi#keyRegister");
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

<a id="keyRetrieve"></a>
# **keyRetrieve**
> JWT keyRetrieve(PK)



Get public details of an Authentiq ID. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    KeyApi apiInstance = new KeyApi(defaultClient);
    String PK = "PK_example"; // String | Public Signing Key - Authentiq ID (43 chars)
    try {
      JWT result = apiInstance.keyRetrieve(PK);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyApi#keyRetrieve");
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

### Return type

[**JWT**](JWT.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved |  -  |
| **404** | Unknown key &#x60;unknown-key&#x60; |  -  |
| **410** | Key is revoked (gone). &#x60;revoked-key&#x60; |  -  |
| **0** | Error response |  -  |

<a id="keyRevoke"></a>
# **keyRevoke**
> KeyRevoke200Response keyRevoke(PK, secret)



Revoke an Identity (Key) with a revocation secret

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    KeyApi apiInstance = new KeyApi(defaultClient);
    String PK = "PK_example"; // String | Public Signing Key - Authentiq ID (43 chars)
    String secret = "secret_example"; // String | revokation secret
    try {
      KeyRevoke200Response result = apiInstance.keyRevoke(PK, secret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyApi#keyRevoke");
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
| **secret** | **String**| revokation secret | |

### Return type

[**KeyRevoke200Response**](KeyRevoke200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **401** | Key not found / wrong code &#x60;auth-error&#x60; |  -  |
| **404** | Unknown key &#x60;unknown-key&#x60; |  -  |
| **0** | Error response |  -  |

<a id="keyRevokeNosecret"></a>
# **keyRevokeNosecret**
> KeyRevokeNosecret200Response keyRevokeNosecret(email, phone, code)



Revoke an Authentiq ID using email &amp; phone.  If called with &#x60;email&#x60; and &#x60;phone&#x60; only, a verification code  will be sent by email. Do a second call adding &#x60;code&#x60; to  complete the revocation. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    KeyApi apiInstance = new KeyApi(defaultClient);
    String email = "email_example"; // String | primary email associated to Key (ID)
    String phone = "phone_example"; // String | primary phone number, international representation
    String code = "code_example"; // String | verification code sent by email
    try {
      KeyRevokeNosecret200Response result = apiInstance.keyRevokeNosecret(email, phone, code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyApi#keyRevokeNosecret");
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
| **email** | **String**| primary email associated to Key (ID) | |
| **phone** | **String**| primary phone number, international representation | |
| **code** | **String**| verification code sent by email | [optional] |

### Return type

[**KeyRevokeNosecret200Response**](KeyRevokeNosecret200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted |  -  |
| **401** | Authentication error &#x60;auth-error&#x60; |  -  |
| **404** | Unknown key &#x60;unknown-key&#x60; |  -  |
| **409** | Confirm with code sent &#x60;confirm-first&#x60; |  -  |
| **0** | Error response |  -  |

<a id="keyUpdate"></a>
# **keyUpdate**
> KeyBind200Response keyUpdate(PK, authentiqID)



update properties of an Authentiq ID. (not operational in v4; use PUT for now)  v5: POST issuer-signed email &amp; phone scopes in a self-signed JWT  See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    KeyApi apiInstance = new KeyApi(defaultClient);
    String PK = "PK_example"; // String | Public Signing Key - Authentiq ID (43 chars)
    AuthentiqID authentiqID = new AuthentiqID(); // AuthentiqID | Authentiq ID to register
    try {
      KeyBind200Response result = apiInstance.keyUpdate(PK, authentiqID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyApi#keyUpdate");
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

