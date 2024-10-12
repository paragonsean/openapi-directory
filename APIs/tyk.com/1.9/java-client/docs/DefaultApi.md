# DefaultApi

All URIs are relative to *http://tyk.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tykApisApiIDDelete**](DefaultApi.md#tykApisApiIDDelete) | **DELETE** /tyk/apis/{apiID} |  |
| [**tykApisApiIDGet**](DefaultApi.md#tykApisApiIDGet) | **GET** /tyk/apis/{apiID} |  |
| [**tykApisApiIDPut**](DefaultApi.md#tykApisApiIDPut) | **PUT** /tyk/apis/{apiID} |  |
| [**tykApisGet**](DefaultApi.md#tykApisGet) | **GET** /tyk/apis/ |  |
| [**tykApisPost**](DefaultApi.md#tykApisPost) | **POST** /tyk/apis/ |  |
| [**tykHealthGet**](DefaultApi.md#tykHealthGet) | **GET** /tyk/health/ |  |
| [**tykKeysCreatePost**](DefaultApi.md#tykKeysCreatePost) | **POST** /tyk/keys/create |  |
| [**tykKeysGet**](DefaultApi.md#tykKeysGet) | **GET** /tyk/keys/ |  |
| [**tykKeysKeyIdDelete**](DefaultApi.md#tykKeysKeyIdDelete) | **DELETE** /tyk/keys/{keyId} |  |
| [**tykKeysKeyIdPost**](DefaultApi.md#tykKeysKeyIdPost) | **POST** /tyk/keys/{keyId} |  |
| [**tykKeysKeyIdPut**](DefaultApi.md#tykKeysKeyIdPut) | **PUT** /tyk/keys/{keyId} |  |
| [**tykOauthAuthorizeClientPost**](DefaultApi.md#tykOauthAuthorizeClientPost) | **POST** /tyk/oauth/authorize-client/ |  |
| [**tykOauthClientsApiIdClientIdDelete**](DefaultApi.md#tykOauthClientsApiIdClientIdDelete) | **DELETE** /tyk/oauth/clients/{apiId}/{clientId} |  |
| [**tykOauthClientsApiIdGet**](DefaultApi.md#tykOauthClientsApiIdGet) | **GET** /tyk/oauth/clients/{apiId} |  |
| [**tykOauthClientsCreatePost**](DefaultApi.md#tykOauthClientsCreatePost) | **POST** /tyk/oauth/clients/create |  |
| [**tykOauthRefreshKeyIdDelete**](DefaultApi.md#tykOauthRefreshKeyIdDelete) | **DELETE** /tyk/oauth/refresh/{keyId} |  |
| [**tykReloadGet**](DefaultApi.md#tykReloadGet) | **GET** /tyk/reload/ |  |
| [**tykReloadGroupGet**](DefaultApi.md#tykReloadGroupGet) | **GET** /tyk/reload/group |  |


<a id="tykApisApiIDDelete"></a>
# **tykApisApiIDDelete**
> TykApisApiIDDelete200Response tykApisApiIDDelete(xTykAuthorization, apiID)



Deletes an *API Definition* object, if it exists 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://tyk.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
    String apiID = "apiID_example"; // String | API ID
    try {
      TykApisApiIDDelete200Response result = apiInstance.tykApisApiIDDelete(xTykAuthorization, apiID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tykApisApiIDDelete");
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
| **xTykAuthorization** | **String**| tyk gateway shared secret | |
| **apiID** | **String**| API ID | |

### Return type

[**TykApisApiIDDelete200Response**](TykApisApiIDDelete200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Succesful API Deletion |  -  |

<a id="tykApisApiIDGet"></a>
# **tykApisApiIDGet**
> APIDefinition tykApisApiIDGet(xTykAuthorization, apiID)



Gets an *API Definition* object, if it exists 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://tyk.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
    String apiID = "apiID_example"; // String | API ID
    try {
      APIDefinition result = apiInstance.tykApisApiIDGet(xTykAuthorization, apiID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tykApisApiIDGet");
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
| **xTykAuthorization** | **String**| tyk gateway shared secret | |
| **apiID** | **String**| API ID | |

### Return type

[**APIDefinition**](APIDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Succesful API response |  -  |

<a id="tykApisApiIDPut"></a>
# **tykApisApiIDPut**
> TykApisPost200Response tykApisApiIDPut(xTykAuthorization, apiID, apiDefinition)



Updates an *API Definition* object, if it exists 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://tyk.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
    String apiID = "apiID_example"; // String | API ID
    APIDefinition apiDefinition = new APIDefinition(); // APIDefinition | 
    try {
      TykApisPost200Response result = apiInstance.tykApisApiIDPut(xTykAuthorization, apiID, apiDefinition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tykApisApiIDPut");
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
| **xTykAuthorization** | **String**| tyk gateway shared secret | |
| **apiID** | **String**| API ID | |
| **apiDefinition** | [**APIDefinition**](APIDefinition.md)|  | [optional] |

### Return type

[**TykApisPost200Response**](TykApisPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Succesful API Deletion |  -  |

<a id="tykApisGet"></a>
# **tykApisGet**
> List&lt;APIDefinition&gt; tykApisGet(xTykAuthorization)



Gets a list of *API Definition* objects that are currently live on the gateway  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://tyk.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
    try {
      List<APIDefinition> result = apiInstance.tykApisGet(xTykAuthorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tykApisGet");
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
| **xTykAuthorization** | **String**| tyk gateway shared secret | |

### Return type

[**List&lt;APIDefinition&gt;**](APIDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Succesful list response |  -  |

<a id="tykApisPost"></a>
# **tykApisPost**
> TykApisPost200Response tykApisPost(apiDefinition)



Create an *API Definition* object 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://tyk.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    APIDefinition apiDefinition = new APIDefinition(); // APIDefinition | 
    try {
      TykApisPost200Response result = apiInstance.tykApisPost(apiDefinition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tykApisPost");
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
| **apiDefinition** | [**APIDefinition**](APIDefinition.md)|  | [optional] |

### Return type

[**TykApisPost200Response**](TykApisPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Succesful API Deletion |  -  |

<a id="tykHealthGet"></a>
# **tykHealthGet**
> TykHealthGet200Response tykHealthGet(xTykAuthorization, apiId)



Gets the health check values for an API if it is being recorded 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://tyk.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
    String apiId = "apiId_example"; // String | API ID to query
    try {
      TykHealthGet200Response result = apiInstance.tykHealthGet(xTykAuthorization, apiId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tykHealthGet");
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
| **xTykAuthorization** | **String**| tyk gateway shared secret | |
| **apiId** | **String**| API ID to query | |

### Return type

[**TykHealthGet200Response**](TykHealthGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Succesful healthcheck response |  -  |

<a id="tykKeysCreatePost"></a>
# **tykKeysCreatePost**
> TykKeysCreatePost200Response tykKeysCreatePost(xTykAuthorization, suppressReset, sessionObject)



Create a new *API token* with the *session object* defined in the body 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://tyk.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
    BigDecimal suppressReset = new BigDecimal(78); // BigDecimal | Adding the `suppress_reset` parameter and setting it to `1`, will cause Tyk to not reset the quota limit that is in the current live quota manager. By default Tyk will reset the quota in the live quota manager (initialising it) when ADDing a key. Adding the `suppress_reset` flag to the URL parameters will avoid this behaviour.
    SessionObject sessionObject = new SessionObject(); // SessionObject | 
    try {
      TykKeysCreatePost200Response result = apiInstance.tykKeysCreatePost(xTykAuthorization, suppressReset, sessionObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tykKeysCreatePost");
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
| **xTykAuthorization** | **String**| tyk gateway shared secret | |
| **suppressReset** | **BigDecimal**| Adding the &#x60;suppress_reset&#x60; parameter and setting it to &#x60;1&#x60;, will cause Tyk to not reset the quota limit that is in the current live quota manager. By default Tyk will reset the quota in the live quota manager (initialising it) when ADDing a key. Adding the &#x60;suppress_reset&#x60; flag to the URL parameters will avoid this behaviour. | [optional] |
| **sessionObject** | [**SessionObject**](SessionObject.md)|  | [optional] |

### Return type

[**TykKeysCreatePost200Response**](TykKeysCreatePost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Key Created Response |  -  |

<a id="tykKeysGet"></a>
# **tykKeysGet**
> TykKeysGet200Response tykKeysGet(apiId, xTykAuthorization)



Gets a list of *key* IDs (will only work with non-hashed installations) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://tyk.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiId = "apiId_example"; // String | Back-end to target
    String xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
    try {
      TykKeysGet200Response result = apiInstance.tykKeysGet(apiId, xTykAuthorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tykKeysGet");
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
| **apiId** | **String**| Back-end to target | |
| **xTykAuthorization** | **String**| tyk gateway shared secret | |

### Return type

[**TykKeysGet200Response**](TykKeysGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="tykKeysKeyIdDelete"></a>
# **tykKeysKeyIdDelete**
> TykApisApiIDDelete200Response tykKeysKeyIdDelete(xTykAuthorization, keyId, apiId)



Remove this *API token* from the gateway, this will completely destroy the token and metadata associated with the token and instantly stop access from being granted 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://tyk.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
    String keyId = "keyId_example"; // String | Access Token
    String apiId = "apiId_example"; // String | Back-end to target
    try {
      TykApisApiIDDelete200Response result = apiInstance.tykKeysKeyIdDelete(xTykAuthorization, keyId, apiId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tykKeysKeyIdDelete");
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
| **xTykAuthorization** | **String**| tyk gateway shared secret | |
| **keyId** | **String**| Access Token | |
| **apiId** | **String**| Back-end to target | |

### Return type

[**TykApisApiIDDelete200Response**](TykApisApiIDDelete200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Key Deleted Response |  -  |

<a id="tykKeysKeyIdPost"></a>
# **tykKeysKeyIdPost**
> TykKeysKeyIdPost200Response tykKeysKeyIdPost(xTykAuthorization, keyId, sessionObject)



Add a pre-specified *API token* with the *session object* defined in the body, this operatin creates a custom token that dsoes not use the gateway naming convention for tokens 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://tyk.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
    String keyId = "keyId_example"; // String | Access Token
    SessionObject sessionObject = new SessionObject(); // SessionObject | 
    try {
      TykKeysKeyIdPost200Response result = apiInstance.tykKeysKeyIdPost(xTykAuthorization, keyId, sessionObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tykKeysKeyIdPost");
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
| **xTykAuthorization** | **String**| tyk gateway shared secret | |
| **keyId** | **String**| Access Token | |
| **sessionObject** | [**SessionObject**](SessionObject.md)|  | [optional] |

### Return type

[**TykKeysKeyIdPost200Response**](TykKeysKeyIdPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Key Added Response |  -  |

<a id="tykKeysKeyIdPut"></a>
# **tykKeysKeyIdPut**
> TykKeysKeyIdPut200Response tykKeysKeyIdPut(xTykAuthorization, keyId, apiId, suppressReset, sessionObject)



Update an *API token* with the *session object* defined in the body, this operatin overwrites the existing object 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://tyk.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
    String keyId = "keyId_example"; // String | Access Token
    String apiId = "apiId_example"; // String | Back-end to target
    BigDecimal suppressReset = new BigDecimal(78); // BigDecimal | Adding the `suppress_reset` parameter and setting it to `1`, will cause Tyk to not reset the quota limit that is in the current live quota manager. By default Tyk will reset the quota in the live quota manager (initialising it) when ADDing a key. Adding the `suppress_reset` flag to the URL parameters will avoid this behaviour.
    SessionObject sessionObject = new SessionObject(); // SessionObject | 
    try {
      TykKeysKeyIdPut200Response result = apiInstance.tykKeysKeyIdPut(xTykAuthorization, keyId, apiId, suppressReset, sessionObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tykKeysKeyIdPut");
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
| **xTykAuthorization** | **String**| tyk gateway shared secret | |
| **keyId** | **String**| Access Token | |
| **apiId** | **String**| Back-end to target | |
| **suppressReset** | **BigDecimal**| Adding the &#x60;suppress_reset&#x60; parameter and setting it to &#x60;1&#x60;, will cause Tyk to not reset the quota limit that is in the current live quota manager. By default Tyk will reset the quota in the live quota manager (initialising it) when ADDing a key. Adding the &#x60;suppress_reset&#x60; flag to the URL parameters will avoid this behaviour. | [optional] |
| **sessionObject** | [**SessionObject**](SessionObject.md)|  | [optional] |

### Return type

[**TykKeysKeyIdPut200Response**](TykKeysKeyIdPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Key Updated Response |  -  |

<a id="tykOauthAuthorizeClientPost"></a>
# **tykOauthAuthorizeClientPost**
> TykOauthAuthorizeClientPost200Response tykOauthAuthorizeClientPost(xTykAuthorization, responseType, clientId, redirectUri, keyRules)



The final request from an authorising party for a redirect URI during the Tyk OAuth flow 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://tyk.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
    String responseType = "responseType_example"; // String | Should be provided by requesting client as part of authorisation request, this should be either `code` or `token` depending on the methods you have specified for the API
    String clientId = "clientId_example"; // String | Should be provided by requesting client as part of authorisation request. The Client ID that is making the request
    String redirectUri = "redirectUri_example"; // String | Should be provided by requesting client as part of authorisation request. Must match with the record stored with Tyk
    String keyRules = "keyRules_example"; // String | A string representation of a *Session Object (form-encoded)*. This should be provided by your application in order to apply any quotas or rules to the key
    try {
      TykOauthAuthorizeClientPost200Response result = apiInstance.tykOauthAuthorizeClientPost(xTykAuthorization, responseType, clientId, redirectUri, keyRules);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tykOauthAuthorizeClientPost");
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
| **xTykAuthorization** | **String**| tyk gateway shared secret | |
| **responseType** | **String**| Should be provided by requesting client as part of authorisation request, this should be either &#x60;code&#x60; or &#x60;token&#x60; depending on the methods you have specified for the API | |
| **clientId** | **String**| Should be provided by requesting client as part of authorisation request. The Client ID that is making the request | |
| **redirectUri** | **String**| Should be provided by requesting client as part of authorisation request. Must match with the record stored with Tyk | |
| **keyRules** | **String**| A string representation of a *Session Object (form-encoded)*. This should be provided by your application in order to apply any quotas or rules to the key | |

### Return type

[**TykOauthAuthorizeClientPost200Response**](TykOauthAuthorizeClientPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Succesful token response |  -  |

<a id="tykOauthClientsApiIdClientIdDelete"></a>
# **tykOauthClientsApiIdClientIdDelete**
> TykApisApiIDDelete200Response tykOauthClientsApiIdClientIdDelete(xTykAuthorization, apiId, clientId)



Delete the OAuth client 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://tyk.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
    String apiId = "apiId_example"; // String | API ID that owns this client (back end)
    String clientId = "clientId_example"; // String | OAuth Client ID to delete
    try {
      TykApisApiIDDelete200Response result = apiInstance.tykOauthClientsApiIdClientIdDelete(xTykAuthorization, apiId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tykOauthClientsApiIdClientIdDelete");
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
| **xTykAuthorization** | **String**| tyk gateway shared secret | |
| **apiId** | **String**| API ID that owns this client (back end) | |
| **clientId** | **String**| OAuth Client ID to delete | |

### Return type

[**TykApisApiIDDelete200Response**](TykApisApiIDDelete200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Succesful OAuth client deletion |  -  |

<a id="tykOauthClientsApiIdGet"></a>
# **tykOauthClientsApiIdGet**
> List&lt;OAuthClient&gt; tykOauthClientsApiIdGet(xTykAuthorization, apiId)



Get a list of OAuth clients bound to this back end  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://tyk.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
    String apiId = "apiId_example"; // String | API ID that owns this client (back end)
    try {
      List<OAuthClient> result = apiInstance.tykOauthClientsApiIdGet(xTykAuthorization, apiId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tykOauthClientsApiIdGet");
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
| **xTykAuthorization** | **String**| tyk gateway shared secret | |
| **apiId** | **String**| API ID that owns this client (back end) | |

### Return type

[**List&lt;OAuthClient&gt;**](OAuthClient.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Succesful listy response |  -  |

<a id="tykOauthClientsCreatePost"></a>
# **tykOauthClientsCreatePost**
> OAuthClient tykOauthClientsCreatePost(xTykAuthorization, oauthClient)



Create a new OAuth client 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://tyk.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
    TykOauthClientsCreatePostRequest oauthClient = new TykOauthClientsCreatePostRequest(); // TykOauthClientsCreatePostRequest | 
    try {
      OAuthClient result = apiInstance.tykOauthClientsCreatePost(xTykAuthorization, oauthClient);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tykOauthClientsCreatePost");
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
| **xTykAuthorization** | **String**| tyk gateway shared secret | |
| **oauthClient** | [**TykOauthClientsCreatePostRequest**](TykOauthClientsCreatePostRequest.md)|  | [optional] |

### Return type

[**OAuthClient**](OAuthClient.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Succesful create response |  -  |

<a id="tykOauthRefreshKeyIdDelete"></a>
# **tykOauthRefreshKeyIdDelete**
> TykApisApiIDDelete200Response tykOauthRefreshKeyIdDelete(xTykAuthorization, keyId, apiID)



Invalidate a refresh token 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://tyk.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
    String keyId = "keyId_example"; // String | Access Token
    String apiID = "apiID_example"; // String | API ID
    try {
      TykApisApiIDDelete200Response result = apiInstance.tykOauthRefreshKeyIdDelete(xTykAuthorization, keyId, apiID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tykOauthRefreshKeyIdDelete");
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
| **xTykAuthorization** | **String**| tyk gateway shared secret | |
| **keyId** | **String**| Access Token | |
| **apiID** | **String**| API ID | |

### Return type

[**TykApisApiIDDelete200Response**](TykApisApiIDDelete200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Succesful token revoked |  -  |

<a id="tykReloadGet"></a>
# **tykReloadGet**
> TykReloadGet200Response tykReloadGet(xTykAuthorization)



Will reload the targetted gateway 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://tyk.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
    try {
      TykReloadGet200Response result = apiInstance.tykReloadGet(xTykAuthorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tykReloadGet");
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
| **xTykAuthorization** | **String**| tyk gateway shared secret | |

### Return type

[**TykReloadGet200Response**](TykReloadGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Succesful reload response |  -  |

<a id="tykReloadGroupGet"></a>
# **tykReloadGroupGet**
> TykReloadGet200Response tykReloadGroupGet(xTykAuthorization)



Will reload the cluster via the targeted gateway 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://tyk.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xTykAuthorization = "xTykAuthorization_example"; // String | tyk gateway shared secret
    try {
      TykReloadGet200Response result = apiInstance.tykReloadGroupGet(xTykAuthorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tykReloadGroupGet");
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
| **xTykAuthorization** | **String**| tyk gateway shared secret | |

### Return type

[**TykReloadGet200Response**](TykReloadGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Succesful reload response |  -  |

