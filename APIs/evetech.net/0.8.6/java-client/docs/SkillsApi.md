# SkillsApi

All URIs are relative to *https://esi.evetech.net/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCharactersCharacterIdAttributes**](SkillsApi.md#getCharactersCharacterIdAttributes) | **GET** /characters/{character_id}/attributes/ | Get character attributes |
| [**getCharactersCharacterIdSkillqueue**](SkillsApi.md#getCharactersCharacterIdSkillqueue) | **GET** /characters/{character_id}/skillqueue/ | Get character&#39;s skill queue |
| [**getCharactersCharacterIdSkills**](SkillsApi.md#getCharactersCharacterIdSkills) | **GET** /characters/{character_id}/skills/ | Get character skills |


<a id="getCharactersCharacterIdAttributes"></a>
# **getCharactersCharacterIdAttributes**
> GetCharactersCharacterIdAttributesOk getCharactersCharacterIdAttributes(characterId, datasource, ifNoneMatch, token)

Get character attributes

Return attributes of a character  --- Alternate route: &#x60;/dev/characters/{character_id}/attributes/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/attributes/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/attributes/&#x60;  --- This route is cached for up to 3600 seconds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkillsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    SkillsApi apiInstance = new SkillsApi(defaultClient);
    Integer characterId = 56; // Integer | An EVE character ID
    String datasource = "tranquility"; // String | The server name you would like data from
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      GetCharactersCharacterIdAttributesOk result = apiInstance.getCharactersCharacterIdAttributes(characterId, datasource, ifNoneMatch, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkillsApi#getCharactersCharacterIdAttributes");
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
| **characterId** | **Integer**| An EVE character ID | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

[**GetCharactersCharacterIdAttributesOk**](GetCharactersCharacterIdAttributesOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Attributes of a character |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="getCharactersCharacterIdSkillqueue"></a>
# **getCharactersCharacterIdSkillqueue**
> List&lt;GetCharactersCharacterIdSkillqueue200Ok&gt; getCharactersCharacterIdSkillqueue(characterId, datasource, ifNoneMatch, token)

Get character&#39;s skill queue

List the configured skill queue for the given character  --- Alternate route: &#x60;/dev/characters/{character_id}/skillqueue/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/skillqueue/&#x60;  Alternate route: &#x60;/v2/characters/{character_id}/skillqueue/&#x60;  --- This route is cached for up to 120 seconds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkillsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    SkillsApi apiInstance = new SkillsApi(defaultClient);
    Integer characterId = 56; // Integer | An EVE character ID
    String datasource = "tranquility"; // String | The server name you would like data from
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      List<GetCharactersCharacterIdSkillqueue200Ok> result = apiInstance.getCharactersCharacterIdSkillqueue(characterId, datasource, ifNoneMatch, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkillsApi#getCharactersCharacterIdSkillqueue");
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
| **characterId** | **Integer**| An EVE character ID | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

[**List&lt;GetCharactersCharacterIdSkillqueue200Ok&gt;**](GetCharactersCharacterIdSkillqueue200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The current skill queue, sorted ascending by finishing time |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="getCharactersCharacterIdSkills"></a>
# **getCharactersCharacterIdSkills**
> GetCharactersCharacterIdSkillsOk getCharactersCharacterIdSkills(characterId, datasource, ifNoneMatch, token)

Get character skills

List all trained skills for the given character  --- Alternate route: &#x60;/dev/characters/{character_id}/skills/&#x60;  Alternate route: &#x60;/v4/characters/{character_id}/skills/&#x60;  --- This route is cached for up to 120 seconds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkillsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    SkillsApi apiInstance = new SkillsApi(defaultClient);
    Integer characterId = 56; // Integer | An EVE character ID
    String datasource = "tranquility"; // String | The server name you would like data from
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      GetCharactersCharacterIdSkillsOk result = apiInstance.getCharactersCharacterIdSkills(characterId, datasource, ifNoneMatch, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkillsApi#getCharactersCharacterIdSkills");
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
| **characterId** | **Integer**| An EVE character ID | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

[**GetCharactersCharacterIdSkillsOk**](GetCharactersCharacterIdSkillsOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Known skills for the character |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

