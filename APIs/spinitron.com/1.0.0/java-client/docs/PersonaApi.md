# PersonaApi

All URIs are relative to *https://spinitron.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**personasGet**](PersonaApi.md#personasGet) | **GET** /personas | Get Personas |
| [**personasIdGet**](PersonaApi.md#personasIdGet) | **GET** /personas/{id} | Get Persona by id |


<a id="personasGet"></a>
# **personasGet**
> PersonasGet200Response personasGet(name, count, page, fields, expand)

Get Personas

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://spinitron.com/api");
    
    // Configure API key authorization: accessToken
    ApiKeyAuth accessToken = (ApiKeyAuth) defaultClient.getAuthentication("accessToken");
    accessToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //accessToken.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: httpBearer
    HttpBearerAuth httpBearer = (HttpBearerAuth) defaultClient.getAuthentication("httpBearer");
    httpBearer.setBearerToken("BEARER TOKEN");

    PersonaApi apiInstance = new PersonaApi(defaultClient);
    String name = "name_example"; // String | Filter by Persona name
    Integer count = 20; // Integer | Amount of items to return
    Integer page = 56; // Integer | Offset, used together with count
    List<String> fields = Arrays.asList(); // List<String> | Allows to select only needed fields
    List<String> expand = Arrays.asList(); // List<String> | Allows to select extra fields
    try {
      PersonasGet200Response result = apiInstance.personasGet(name, count, page, fields, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonaApi#personasGet");
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
| **name** | **String**| Filter by Persona name | [optional] |
| **count** | **Integer**| Amount of items to return | [optional] [default to 20] |
| **page** | **Integer**| Offset, used together with count | [optional] |
| **fields** | [**List&lt;String&gt;**](String.md)| Allows to select only needed fields | [optional] |
| **expand** | [**List&lt;String&gt;**](String.md)| Allows to select extra fields | [optional] |

### Return type

[**PersonasGet200Response**](PersonasGet200Response.md)

### Authorization

[accessToken](../README.md#accessToken), [httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The personas |  -  |

<a id="personasIdGet"></a>
# **personasIdGet**
> Persona personasIdGet(id, fields, expand)

Get Persona by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://spinitron.com/api");
    
    // Configure API key authorization: accessToken
    ApiKeyAuth accessToken = (ApiKeyAuth) defaultClient.getAuthentication("accessToken");
    accessToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //accessToken.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: httpBearer
    HttpBearerAuth httpBearer = (HttpBearerAuth) defaultClient.getAuthentication("httpBearer");
    httpBearer.setBearerToken("BEARER TOKEN");

    PersonaApi apiInstance = new PersonaApi(defaultClient);
    Integer id = 56; // Integer | 
    List<String> fields = Arrays.asList(); // List<String> | Allows to select only needed fields
    List<String> expand = Arrays.asList(); // List<String> | Allows to select extra fields
    try {
      Persona result = apiInstance.personasIdGet(id, fields, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonaApi#personasIdGet");
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
| **id** | **Integer**|  | |
| **fields** | [**List&lt;String&gt;**](String.md)| Allows to select only needed fields | [optional] |
| **expand** | [**List&lt;String&gt;**](String.md)| Allows to select extra fields | [optional] |

### Return type

[**Persona**](Persona.md)

### Authorization

[accessToken](../README.md#accessToken), [httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Persona |  -  |
| **404** | Persona not found |  -  |

