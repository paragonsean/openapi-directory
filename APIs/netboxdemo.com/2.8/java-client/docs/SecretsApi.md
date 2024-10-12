# SecretsApi

All URIs are relative to *https://netboxdemo.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**secretsGenerateRsaKeyPairList**](SecretsApi.md#secretsGenerateRsaKeyPairList) | **GET** /secrets/generate-rsa-key-pair/ | This endpoint can be used to generate a new RSA key pair. The keys are returned in PEM format. |
| [**secretsGetSessionKeyCreate**](SecretsApi.md#secretsGetSessionKeyCreate) | **POST** /secrets/get-session-key/ |  |
| [**secretsSecretRolesCreate**](SecretsApi.md#secretsSecretRolesCreate) | **POST** /secrets/secret-roles/ |  |
| [**secretsSecretRolesDelete**](SecretsApi.md#secretsSecretRolesDelete) | **DELETE** /secrets/secret-roles/{id}/ |  |
| [**secretsSecretRolesList**](SecretsApi.md#secretsSecretRolesList) | **GET** /secrets/secret-roles/ |  |
| [**secretsSecretRolesPartialUpdate**](SecretsApi.md#secretsSecretRolesPartialUpdate) | **PATCH** /secrets/secret-roles/{id}/ |  |
| [**secretsSecretRolesRead**](SecretsApi.md#secretsSecretRolesRead) | **GET** /secrets/secret-roles/{id}/ |  |
| [**secretsSecretRolesUpdate**](SecretsApi.md#secretsSecretRolesUpdate) | **PUT** /secrets/secret-roles/{id}/ |  |
| [**secretsSecretsCreate**](SecretsApi.md#secretsSecretsCreate) | **POST** /secrets/secrets/ |  |
| [**secretsSecretsDelete**](SecretsApi.md#secretsSecretsDelete) | **DELETE** /secrets/secrets/{id}/ |  |
| [**secretsSecretsList**](SecretsApi.md#secretsSecretsList) | **GET** /secrets/secrets/ |  |
| [**secretsSecretsPartialUpdate**](SecretsApi.md#secretsSecretsPartialUpdate) | **PATCH** /secrets/secrets/{id}/ |  |
| [**secretsSecretsRead**](SecretsApi.md#secretsSecretsRead) | **GET** /secrets/secrets/{id}/ |  |
| [**secretsSecretsUpdate**](SecretsApi.md#secretsSecretsUpdate) | **PUT** /secrets/secrets/{id}/ |  |


<a id="secretsGenerateRsaKeyPairList"></a>
# **secretsGenerateRsaKeyPairList**
> secretsGenerateRsaKeyPairList()

This endpoint can be used to generate a new RSA key pair. The keys are returned in PEM format.

{         \&quot;public_key\&quot;: \&quot;&lt;public key&gt;\&quot;,         \&quot;private_key\&quot;: \&quot;&lt;private key&gt;\&quot;     }

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    try {
      apiInstance.secretsGenerateRsaKeyPairList();
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsGenerateRsaKeyPairList");
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="secretsGetSessionKeyCreate"></a>
# **secretsGetSessionKeyCreate**
> secretsGetSessionKeyCreate()



Retrieve a temporary session key to use for encrypting and decrypting secrets via the API. The user&#39;s private RSA key is POSTed with the name &#x60;private_key&#x60;. An example:      curl -v -X POST -H \&quot;Authorization: Token &lt;token&gt;\&quot; -H \&quot;Accept: application/json; indent&#x3D;4\&quot; \\     --data-urlencode \&quot;private_key@&lt;filename&gt;\&quot; https://netbox/api/secrets/get-session-key/  This request will yield a base64-encoded session key to be included in an &#x60;X-Session-Key&#x60; header in future requests:      {         \&quot;session_key\&quot;: \&quot;+8t4SI6XikgVmB5+/urhozx9O5qCQANyOk1MNe6taRf&#x3D;\&quot;     }  This endpoint accepts one optional parameter: &#x60;preserve_key&#x60;. If True and a session key exists, the existing session key will be returned instead of a new one.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    try {
      apiInstance.secretsGetSessionKeyCreate();
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsGetSessionKeyCreate");
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="secretsSecretRolesCreate"></a>
# **secretsSecretRolesCreate**
> SecretRole secretsSecretRolesCreate(secretRole)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    SecretRole secretRole = new SecretRole(); // SecretRole | 
    try {
      SecretRole result = apiInstance.secretsSecretRolesCreate(secretRole);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsSecretRolesCreate");
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
| **secretRole** | [**SecretRole**](SecretRole.md)|  | |

### Return type

[**SecretRole**](SecretRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="secretsSecretRolesDelete"></a>
# **secretsSecretRolesDelete**
> secretsSecretRolesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this secret role.
    try {
      apiInstance.secretsSecretRolesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsSecretRolesDelete");
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
| **id** | **Integer**| A unique integer value identifying this secret role. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="secretsSecretRolesList"></a>
# **secretsSecretRolesList**
> SecretsSecretRolesList200Response secretsSecretRolesList(id, name, slug, q, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, limit, offset)



Call to super to allow for caching

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String id = "id_example"; // String | 
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    String q = "q_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String nameN = "nameN_example"; // String | 
    String nameIc = "nameIc_example"; // String | 
    String nameNic = "nameNic_example"; // String | 
    String nameIew = "nameIew_example"; // String | 
    String nameNiew = "nameNiew_example"; // String | 
    String nameIsw = "nameIsw_example"; // String | 
    String nameNisw = "nameNisw_example"; // String | 
    String nameIe = "nameIe_example"; // String | 
    String nameNie = "nameNie_example"; // String | 
    String slugN = "slugN_example"; // String | 
    String slugIc = "slugIc_example"; // String | 
    String slugNic = "slugNic_example"; // String | 
    String slugIew = "slugIew_example"; // String | 
    String slugNiew = "slugNiew_example"; // String | 
    String slugIsw = "slugIsw_example"; // String | 
    String slugNisw = "slugNisw_example"; // String | 
    String slugIe = "slugIe_example"; // String | 
    String slugNie = "slugNie_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      SecretsSecretRolesList200Response result = apiInstance.secretsSecretRolesList(id, name, slug, q, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsSecretRolesList");
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
| **id** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **nameN** | **String**|  | [optional] |
| **nameIc** | **String**|  | [optional] |
| **nameNic** | **String**|  | [optional] |
| **nameIew** | **String**|  | [optional] |
| **nameNiew** | **String**|  | [optional] |
| **nameIsw** | **String**|  | [optional] |
| **nameNisw** | **String**|  | [optional] |
| **nameIe** | **String**|  | [optional] |
| **nameNie** | **String**|  | [optional] |
| **slugN** | **String**|  | [optional] |
| **slugIc** | **String**|  | [optional] |
| **slugNic** | **String**|  | [optional] |
| **slugIew** | **String**|  | [optional] |
| **slugNiew** | **String**|  | [optional] |
| **slugIsw** | **String**|  | [optional] |
| **slugNisw** | **String**|  | [optional] |
| **slugIe** | **String**|  | [optional] |
| **slugNie** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**SecretsSecretRolesList200Response**](SecretsSecretRolesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="secretsSecretRolesPartialUpdate"></a>
# **secretsSecretRolesPartialUpdate**
> SecretRole secretsSecretRolesPartialUpdate(id, secretRole)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this secret role.
    SecretRole secretRole = new SecretRole(); // SecretRole | 
    try {
      SecretRole result = apiInstance.secretsSecretRolesPartialUpdate(id, secretRole);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsSecretRolesPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this secret role. | |
| **secretRole** | [**SecretRole**](SecretRole.md)|  | |

### Return type

[**SecretRole**](SecretRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="secretsSecretRolesRead"></a>
# **secretsSecretRolesRead**
> SecretRole secretsSecretRolesRead(id)



Call to super to allow for caching

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this secret role.
    try {
      SecretRole result = apiInstance.secretsSecretRolesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsSecretRolesRead");
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
| **id** | **Integer**| A unique integer value identifying this secret role. | |

### Return type

[**SecretRole**](SecretRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="secretsSecretRolesUpdate"></a>
# **secretsSecretRolesUpdate**
> SecretRole secretsSecretRolesUpdate(id, secretRole)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this secret role.
    SecretRole secretRole = new SecretRole(); // SecretRole | 
    try {
      SecretRole result = apiInstance.secretsSecretRolesUpdate(id, secretRole);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsSecretRolesUpdate");
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
| **id** | **Integer**| A unique integer value identifying this secret role. | |
| **secretRole** | [**SecretRole**](SecretRole.md)|  | |

### Return type

[**SecretRole**](SecretRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="secretsSecretsCreate"></a>
# **secretsSecretsCreate**
> Secret secretsSecretsCreate(writableSecret)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    WritableSecret writableSecret = new WritableSecret(); // WritableSecret | 
    try {
      Secret result = apiInstance.secretsSecretsCreate(writableSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsSecretsCreate");
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
| **writableSecret** | [**WritableSecret**](WritableSecret.md)|  | |

### Return type

[**Secret**](Secret.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="secretsSecretsDelete"></a>
# **secretsSecretsDelete**
> secretsSecretsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this secret.
    try {
      apiInstance.secretsSecretsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsSecretsDelete");
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
| **id** | **Integer**| A unique integer value identifying this secret. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="secretsSecretsList"></a>
# **secretsSecretsList**
> SecretsSecretsList200Response secretsSecretsList(id, name, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, roleId, role, deviceId, device, tag, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, roleIdN, roleN, deviceIdN, deviceN, tagN, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String id = "id_example"; // String | 
    String name = "name_example"; // String | 
    String created = "created_example"; // String | 
    String createdGte = "createdGte_example"; // String | 
    String createdLte = "createdLte_example"; // String | 
    String lastUpdated = "lastUpdated_example"; // String | 
    String lastUpdatedGte = "lastUpdatedGte_example"; // String | 
    String lastUpdatedLte = "lastUpdatedLte_example"; // String | 
    String q = "q_example"; // String | 
    String roleId = "roleId_example"; // String | 
    String role = "role_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    String device = "device_example"; // String | 
    String tag = "tag_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String nameN = "nameN_example"; // String | 
    String nameIc = "nameIc_example"; // String | 
    String nameNic = "nameNic_example"; // String | 
    String nameIew = "nameIew_example"; // String | 
    String nameNiew = "nameNiew_example"; // String | 
    String nameIsw = "nameIsw_example"; // String | 
    String nameNisw = "nameNisw_example"; // String | 
    String nameIe = "nameIe_example"; // String | 
    String nameNie = "nameNie_example"; // String | 
    String roleIdN = "roleIdN_example"; // String | 
    String roleN = "roleN_example"; // String | 
    String deviceIdN = "deviceIdN_example"; // String | 
    String deviceN = "deviceN_example"; // String | 
    String tagN = "tagN_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      SecretsSecretsList200Response result = apiInstance.secretsSecretsList(id, name, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, roleId, role, deviceId, device, tag, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, roleIdN, roleN, deviceIdN, deviceN, tagN, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsSecretsList");
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
| **id** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **created** | **String**|  | [optional] |
| **createdGte** | **String**|  | [optional] |
| **createdLte** | **String**|  | [optional] |
| **lastUpdated** | **String**|  | [optional] |
| **lastUpdatedGte** | **String**|  | [optional] |
| **lastUpdatedLte** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **roleId** | **String**|  | [optional] |
| **role** | **String**|  | [optional] |
| **deviceId** | **String**|  | [optional] |
| **device** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **nameN** | **String**|  | [optional] |
| **nameIc** | **String**|  | [optional] |
| **nameNic** | **String**|  | [optional] |
| **nameIew** | **String**|  | [optional] |
| **nameNiew** | **String**|  | [optional] |
| **nameIsw** | **String**|  | [optional] |
| **nameNisw** | **String**|  | [optional] |
| **nameIe** | **String**|  | [optional] |
| **nameNie** | **String**|  | [optional] |
| **roleIdN** | **String**|  | [optional] |
| **roleN** | **String**|  | [optional] |
| **deviceIdN** | **String**|  | [optional] |
| **deviceN** | **String**|  | [optional] |
| **tagN** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**SecretsSecretsList200Response**](SecretsSecretsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="secretsSecretsPartialUpdate"></a>
# **secretsSecretsPartialUpdate**
> Secret secretsSecretsPartialUpdate(id, writableSecret)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this secret.
    WritableSecret writableSecret = new WritableSecret(); // WritableSecret | 
    try {
      Secret result = apiInstance.secretsSecretsPartialUpdate(id, writableSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsSecretsPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this secret. | |
| **writableSecret** | [**WritableSecret**](WritableSecret.md)|  | |

### Return type

[**Secret**](Secret.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="secretsSecretsRead"></a>
# **secretsSecretsRead**
> Secret secretsSecretsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this secret.
    try {
      Secret result = apiInstance.secretsSecretsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsSecretsRead");
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
| **id** | **Integer**| A unique integer value identifying this secret. | |

### Return type

[**Secret**](Secret.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="secretsSecretsUpdate"></a>
# **secretsSecretsUpdate**
> Secret secretsSecretsUpdate(id, writableSecret)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this secret.
    WritableSecret writableSecret = new WritableSecret(); // WritableSecret | 
    try {
      Secret result = apiInstance.secretsSecretsUpdate(id, writableSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsSecretsUpdate");
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
| **id** | **Integer**| A unique integer value identifying this secret. | |
| **writableSecret** | [**WritableSecret**](WritableSecret.md)|  | |

### Return type

[**Secret**](Secret.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

