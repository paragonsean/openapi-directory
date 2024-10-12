# ClientApi

All URIs are relative to *https://phantauth.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**clientClientIdGet**](ClientApi.md#clientClientIdGet) | **GET** /client/{client_id} | Get a Client |
| [**clientClientIdTokenKindGet**](ClientApi.md#clientClientIdTokenKindGet) | **GET** /client/{client_id}/token/{kind} | Get a Client Token |
| [**clientPost**](ClientApi.md#clientPost) | **POST** /client | Create a Client Selfie |


<a id="clientClientIdGet"></a>
# **clientClientIdGet**
> ClientClientIdGet200Response clientClientIdGet(clientId)

Get a Client

Use this endpoint to generate a random client. The client is generated in a deterministic way, on the bases of the client ID given as a path parameter. In the case of identical client IDs, the endpoint will generate the same client object. The properties of the generated client object are randomly generated on the basis of the client ID. In lack of a client ID, all calls generate a different client object to the randomly generated client ID.  By providing an email address as the &#x60;client_id&#x60; parameter, you can customize the client logo by the use of the gravatar associated with the email address.  If the &#x60;client_id&#x60; parameter contains minimum one dot (&#x60;.&#x60;) or space (&#x60; &#x60;) character, the client_name is produced from the parameter, rather than being generated.&#x60;  The result is always a client object. If you want to generate multiple clients in one single step, you can do it by the use of *Fleet* generation. The members of a fleet are clients randomly generated from the fleet name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://phantauth.net");

    ClientApi apiInstance = new ClientApi(defaultClient);
    String clientId = "clientId_example"; // String | A client ID or email.
    try {
      ClientClientIdGet200Response result = apiInstance.clientClientIdGet(clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientApi#clientClientIdGet");
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
| **clientId** | **String**| A client ID or email. | |

### Return type

[**ClientClientIdGet200Response**](ClientClientIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="clientClientIdTokenKindGet"></a>
# **clientClientIdTokenKindGet**
> clientClientIdTokenKindGet(clientId, kind)

Get a Client Token

It is used to generate a OpenID Connect token as a path parameter to a client of a given client ID.  It is primarily used for testing purposes, when, for example, the token from the standard authentication flow is not available to the test code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://phantauth.net");

    ClientApi apiInstance = new ClientApi(defaultClient);
    String clientId = "clientId_example"; // String | A client ID or email.
    String kind = "'registration'"; // String | Token type
    try {
      apiInstance.clientClientIdTokenKindGet(clientId, kind);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientApi#clientClientIdTokenKindGet");
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
| **clientId** | **String**| A client ID or email. | |
| **kind** | **String**| Token type | [enum: 'registration', 'selfie', 'plain'] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="clientPost"></a>
# **clientPost**
> clientPost(clientPostRequest)

Create a Client Selfie

To create a selfie token from the client data, you need an opaqe string token, which contains the encoded client properties sent in the request. Later, the selfie token can be used as a client ID. In this case, the client data is included in the selfie token, that is, the client properties are taken from the token. By the use of a selfie token, you can use your own client objects in the authentication process.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://phantauth.net");

    ClientApi apiInstance = new ClientApi(defaultClient);
    ClientPostRequest clientPostRequest = new ClientPostRequest(); // ClientPostRequest | 
    try {
      apiInstance.clientPost(clientPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientApi#clientPost");
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
| **clientPostRequest** | [**ClientPostRequest**](ClientPostRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

