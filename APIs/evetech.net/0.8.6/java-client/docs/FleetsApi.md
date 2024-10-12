# FleetsApi

All URIs are relative to *https://esi.evetech.net/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteFleetsFleetIdMembersMemberId**](FleetsApi.md#deleteFleetsFleetIdMembersMemberId) | **DELETE** /fleets/{fleet_id}/members/{member_id}/ | Kick fleet member |
| [**deleteFleetsFleetIdSquadsSquadId**](FleetsApi.md#deleteFleetsFleetIdSquadsSquadId) | **DELETE** /fleets/{fleet_id}/squads/{squad_id}/ | Delete fleet squad |
| [**deleteFleetsFleetIdWingsWingId**](FleetsApi.md#deleteFleetsFleetIdWingsWingId) | **DELETE** /fleets/{fleet_id}/wings/{wing_id}/ | Delete fleet wing |
| [**getCharactersCharacterIdFleet**](FleetsApi.md#getCharactersCharacterIdFleet) | **GET** /characters/{character_id}/fleet/ | Get character fleet info |
| [**getFleetsFleetId**](FleetsApi.md#getFleetsFleetId) | **GET** /fleets/{fleet_id}/ | Get fleet information |
| [**getFleetsFleetIdMembers**](FleetsApi.md#getFleetsFleetIdMembers) | **GET** /fleets/{fleet_id}/members/ | Get fleet members |
| [**getFleetsFleetIdWings**](FleetsApi.md#getFleetsFleetIdWings) | **GET** /fleets/{fleet_id}/wings/ | Get fleet wings |
| [**postFleetsFleetIdMembers**](FleetsApi.md#postFleetsFleetIdMembers) | **POST** /fleets/{fleet_id}/members/ | Create fleet invitation |
| [**postFleetsFleetIdWings**](FleetsApi.md#postFleetsFleetIdWings) | **POST** /fleets/{fleet_id}/wings/ | Create fleet wing |
| [**postFleetsFleetIdWingsWingIdSquads**](FleetsApi.md#postFleetsFleetIdWingsWingIdSquads) | **POST** /fleets/{fleet_id}/wings/{wing_id}/squads/ | Create fleet squad |
| [**putFleetsFleetId**](FleetsApi.md#putFleetsFleetId) | **PUT** /fleets/{fleet_id}/ | Update fleet |
| [**putFleetsFleetIdMembersMemberId**](FleetsApi.md#putFleetsFleetIdMembersMemberId) | **PUT** /fleets/{fleet_id}/members/{member_id}/ | Move fleet member |
| [**putFleetsFleetIdSquadsSquadId**](FleetsApi.md#putFleetsFleetIdSquadsSquadId) | **PUT** /fleets/{fleet_id}/squads/{squad_id}/ | Rename fleet squad |
| [**putFleetsFleetIdWingsWingId**](FleetsApi.md#putFleetsFleetIdWingsWingId) | **PUT** /fleets/{fleet_id}/wings/{wing_id}/ | Rename fleet wing |


<a id="deleteFleetsFleetIdMembersMemberId"></a>
# **deleteFleetsFleetIdMembersMemberId**
> deleteFleetsFleetIdMembersMemberId(fleetId, memberId, datasource, token)

Kick fleet member

Kick a fleet member  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/members/{member_id}/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/members/{member_id}/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/members/{member_id}/&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FleetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    FleetsApi apiInstance = new FleetsApi(defaultClient);
    Long fleetId = 56L; // Long | ID for a fleet
    Integer memberId = 56; // Integer | The character ID of a member in this fleet
    String datasource = "tranquility"; // String | The server name you would like data from
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      apiInstance.deleteFleetsFleetIdMembersMemberId(fleetId, memberId, datasource, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetsApi#deleteFleetsFleetIdMembersMemberId");
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
| **fleetId** | **Long**| ID for a fleet | |
| **memberId** | **Integer**| The character ID of a member in this fleet | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Fleet member kicked |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The fleet does not exist or you don&#39;t have access to it |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="deleteFleetsFleetIdSquadsSquadId"></a>
# **deleteFleetsFleetIdSquadsSquadId**
> deleteFleetsFleetIdSquadsSquadId(fleetId, squadId, datasource, token)

Delete fleet squad

Delete a fleet squad, only empty squads can be deleted  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/squads/{squad_id}/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/squads/{squad_id}/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/squads/{squad_id}/&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FleetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    FleetsApi apiInstance = new FleetsApi(defaultClient);
    Long fleetId = 56L; // Long | ID for a fleet
    Long squadId = 56L; // Long | The squad to delete
    String datasource = "tranquility"; // String | The server name you would like data from
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      apiInstance.deleteFleetsFleetIdSquadsSquadId(fleetId, squadId, datasource, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetsApi#deleteFleetsFleetIdSquadsSquadId");
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
| **fleetId** | **Long**| ID for a fleet | |
| **squadId** | **Long**| The squad to delete | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Squad deleted |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The fleet does not exist or you don&#39;t have access to it |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="deleteFleetsFleetIdWingsWingId"></a>
# **deleteFleetsFleetIdWingsWingId**
> deleteFleetsFleetIdWingsWingId(fleetId, wingId, datasource, token)

Delete fleet wing

Delete a fleet wing, only empty wings can be deleted. The wing may contain squads, but the squads must be empty  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/wings/{wing_id}/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/wings/{wing_id}/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/wings/{wing_id}/&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FleetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    FleetsApi apiInstance = new FleetsApi(defaultClient);
    Long fleetId = 56L; // Long | ID for a fleet
    Long wingId = 56L; // Long | The wing to delete
    String datasource = "tranquility"; // String | The server name you would like data from
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      apiInstance.deleteFleetsFleetIdWingsWingId(fleetId, wingId, datasource, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetsApi#deleteFleetsFleetIdWingsWingId");
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
| **fleetId** | **Long**| ID for a fleet | |
| **wingId** | **Long**| The wing to delete | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Wing deleted |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The fleet does not exist or you don&#39;t have access to it |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="getCharactersCharacterIdFleet"></a>
# **getCharactersCharacterIdFleet**
> GetCharactersCharacterIdFleetOk getCharactersCharacterIdFleet(characterId, datasource, ifNoneMatch, token)

Get character fleet info

Return the fleet ID the character is in, if any.  --- Alternate route: &#x60;/dev/characters/{character_id}/fleet/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/fleet/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/fleet/&#x60;  --- This route is cached for up to 60 seconds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FleetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    FleetsApi apiInstance = new FleetsApi(defaultClient);
    Integer characterId = 56; // Integer | An EVE character ID
    String datasource = "tranquility"; // String | The server name you would like data from
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      GetCharactersCharacterIdFleetOk result = apiInstance.getCharactersCharacterIdFleet(characterId, datasource, ifNoneMatch, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetsApi#getCharactersCharacterIdFleet");
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

[**GetCharactersCharacterIdFleetOk**](GetCharactersCharacterIdFleetOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details about the character&#39;s fleet |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The character is not in a fleet |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="getFleetsFleetId"></a>
# **getFleetsFleetId**
> GetFleetsFleetIdOk getFleetsFleetId(fleetId, datasource, ifNoneMatch, token)

Get fleet information

Return details about a fleet  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/&#x60;  --- This route is cached for up to 5 seconds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FleetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    FleetsApi apiInstance = new FleetsApi(defaultClient);
    Long fleetId = 56L; // Long | ID for a fleet
    String datasource = "tranquility"; // String | The server name you would like data from
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      GetFleetsFleetIdOk result = apiInstance.getFleetsFleetId(fleetId, datasource, ifNoneMatch, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetsApi#getFleetsFleetId");
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
| **fleetId** | **Long**| ID for a fleet | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

[**GetFleetsFleetIdOk**](GetFleetsFleetIdOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details about a fleet |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The fleet does not exist or you don&#39;t have access to it |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="getFleetsFleetIdMembers"></a>
# **getFleetsFleetIdMembers**
> List&lt;GetFleetsFleetIdMembers200Ok&gt; getFleetsFleetIdMembers(fleetId, acceptLanguage, datasource, ifNoneMatch, language, token)

Get fleet members

Return information about fleet members  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/members/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/members/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/members/&#x60;  --- This route is cached for up to 5 seconds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FleetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    FleetsApi apiInstance = new FleetsApi(defaultClient);
    Long fleetId = 56L; // Long | ID for a fleet
    String acceptLanguage = "de"; // String | Language to use in the response
    String datasource = "tranquility"; // String | The server name you would like data from
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
    String language = "de"; // String | Language to use in the response, takes precedence over Accept-Language
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      List<GetFleetsFleetIdMembers200Ok> result = apiInstance.getFleetsFleetIdMembers(fleetId, acceptLanguage, datasource, ifNoneMatch, language, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetsApi#getFleetsFleetIdMembers");
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
| **fleetId** | **Long**| ID for a fleet | |
| **acceptLanguage** | **String**| Language to use in the response | [optional] [default to en-us] [enum: de, en-us, fr, ja, ru, zh] |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] |
| **language** | **String**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to en-us] [enum: de, en-us, fr, ja, ru, zh] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

[**List&lt;GetFleetsFleetIdMembers200Ok&gt;**](GetFleetsFleetIdMembers200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of fleet members |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * Content-Language - The language used in the response <br>  |
| **304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The fleet does not exist or you don&#39;t have access to it |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="getFleetsFleetIdWings"></a>
# **getFleetsFleetIdWings**
> List&lt;GetFleetsFleetIdWings200Ok&gt; getFleetsFleetIdWings(fleetId, acceptLanguage, datasource, ifNoneMatch, language, token)

Get fleet wings

Return information about wings in a fleet  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/wings/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/wings/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/wings/&#x60;  --- This route is cached for up to 5 seconds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FleetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    FleetsApi apiInstance = new FleetsApi(defaultClient);
    Long fleetId = 56L; // Long | ID for a fleet
    String acceptLanguage = "de"; // String | Language to use in the response
    String datasource = "tranquility"; // String | The server name you would like data from
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
    String language = "de"; // String | Language to use in the response, takes precedence over Accept-Language
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      List<GetFleetsFleetIdWings200Ok> result = apiInstance.getFleetsFleetIdWings(fleetId, acceptLanguage, datasource, ifNoneMatch, language, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetsApi#getFleetsFleetIdWings");
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
| **fleetId** | **Long**| ID for a fleet | |
| **acceptLanguage** | **String**| Language to use in the response | [optional] [default to en-us] [enum: de, en-us, fr, ja, ru, zh] |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] |
| **language** | **String**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to en-us] [enum: de, en-us, fr, ja, ru, zh] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

[**List&lt;GetFleetsFleetIdWings200Ok&gt;**](GetFleetsFleetIdWings200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of fleet wings |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * Content-Language - The language used in the response <br>  |
| **304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The fleet does not exist or you don&#39;t have access to it |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="postFleetsFleetIdMembers"></a>
# **postFleetsFleetIdMembers**
> postFleetsFleetIdMembers(fleetId, invitation, datasource, token)

Create fleet invitation

Invite a character into the fleet. If a character has a CSPA charge set it is not possible to invite them to the fleet using ESI  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/members/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/members/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/members/&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FleetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    FleetsApi apiInstance = new FleetsApi(defaultClient);
    Long fleetId = 56L; // Long | ID for a fleet
    PostFleetsFleetIdMembersInvitation invitation = new PostFleetsFleetIdMembersInvitation(); // PostFleetsFleetIdMembersInvitation | Details of the invitation
    String datasource = "tranquility"; // String | The server name you would like data from
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      apiInstance.postFleetsFleetIdMembers(fleetId, invitation, datasource, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetsApi#postFleetsFleetIdMembers");
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
| **fleetId** | **Long**| ID for a fleet | |
| **invitation** | [**PostFleetsFleetIdMembersInvitation**](PostFleetsFleetIdMembersInvitation.md)| Details of the invitation | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Fleet invitation sent |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The fleet does not exist or you don&#39;t have access to it |  -  |
| **420** | Error limited |  -  |
| **422** | Errors in invitation |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="postFleetsFleetIdWings"></a>
# **postFleetsFleetIdWings**
> PostFleetsFleetIdWingsCreated postFleetsFleetIdWings(fleetId, datasource, token)

Create fleet wing

Create a new wing in a fleet  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/wings/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/wings/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/wings/&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FleetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    FleetsApi apiInstance = new FleetsApi(defaultClient);
    Long fleetId = 56L; // Long | ID for a fleet
    String datasource = "tranquility"; // String | The server name you would like data from
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      PostFleetsFleetIdWingsCreated result = apiInstance.postFleetsFleetIdWings(fleetId, datasource, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetsApi#postFleetsFleetIdWings");
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
| **fleetId** | **Long**| ID for a fleet | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

[**PostFleetsFleetIdWingsCreated**](PostFleetsFleetIdWingsCreated.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Wing created |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The fleet does not exist or you don&#39;t have access to it |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="postFleetsFleetIdWingsWingIdSquads"></a>
# **postFleetsFleetIdWingsWingIdSquads**
> PostFleetsFleetIdWingsWingIdSquadsCreated postFleetsFleetIdWingsWingIdSquads(fleetId, wingId, datasource, token)

Create fleet squad

Create a new squad in a fleet  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/wings/{wing_id}/squads/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/wings/{wing_id}/squads/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/wings/{wing_id}/squads/&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FleetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    FleetsApi apiInstance = new FleetsApi(defaultClient);
    Long fleetId = 56L; // Long | ID for a fleet
    Long wingId = 56L; // Long | The wing_id to create squad in
    String datasource = "tranquility"; // String | The server name you would like data from
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      PostFleetsFleetIdWingsWingIdSquadsCreated result = apiInstance.postFleetsFleetIdWingsWingIdSquads(fleetId, wingId, datasource, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetsApi#postFleetsFleetIdWingsWingIdSquads");
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
| **fleetId** | **Long**| ID for a fleet | |
| **wingId** | **Long**| The wing_id to create squad in | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

[**PostFleetsFleetIdWingsWingIdSquadsCreated**](PostFleetsFleetIdWingsWingIdSquadsCreated.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Squad created |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The fleet does not exist or you don&#39;t have access to it |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="putFleetsFleetId"></a>
# **putFleetsFleetId**
> putFleetsFleetId(fleetId, newSettings, datasource, token)

Update fleet

Update settings about a fleet  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FleetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    FleetsApi apiInstance = new FleetsApi(defaultClient);
    Long fleetId = 56L; // Long | ID for a fleet
    PutFleetsFleetIdNewSettings newSettings = new PutFleetsFleetIdNewSettings(); // PutFleetsFleetIdNewSettings | What to update for this fleet
    String datasource = "tranquility"; // String | The server name you would like data from
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      apiInstance.putFleetsFleetId(fleetId, newSettings, datasource, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetsApi#putFleetsFleetId");
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
| **fleetId** | **Long**| ID for a fleet | |
| **newSettings** | [**PutFleetsFleetIdNewSettings**](PutFleetsFleetIdNewSettings.md)| What to update for this fleet | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Fleet updated |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The fleet does not exist or you don&#39;t have access to it |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="putFleetsFleetIdMembersMemberId"></a>
# **putFleetsFleetIdMembersMemberId**
> putFleetsFleetIdMembersMemberId(fleetId, memberId, movement, datasource, token)

Move fleet member

Move a fleet member around  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/members/{member_id}/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/members/{member_id}/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/members/{member_id}/&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FleetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    FleetsApi apiInstance = new FleetsApi(defaultClient);
    Long fleetId = 56L; // Long | ID for a fleet
    Integer memberId = 56; // Integer | The character ID of a member in this fleet
    PutFleetsFleetIdMembersMemberIdMovement movement = new PutFleetsFleetIdMembersMemberIdMovement(); // PutFleetsFleetIdMembersMemberIdMovement | Details of the invitation
    String datasource = "tranquility"; // String | The server name you would like data from
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      apiInstance.putFleetsFleetIdMembersMemberId(fleetId, memberId, movement, datasource, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetsApi#putFleetsFleetIdMembersMemberId");
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
| **fleetId** | **Long**| ID for a fleet | |
| **memberId** | **Integer**| The character ID of a member in this fleet | |
| **movement** | [**PutFleetsFleetIdMembersMemberIdMovement**](PutFleetsFleetIdMembersMemberIdMovement.md)| Details of the invitation | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Fleet invitation sent |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The fleet does not exist or you don&#39;t have access to it |  -  |
| **420** | Error limited |  -  |
| **422** | Errors in invitation |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="putFleetsFleetIdSquadsSquadId"></a>
# **putFleetsFleetIdSquadsSquadId**
> putFleetsFleetIdSquadsSquadId(fleetId, squadId, naming, datasource, token)

Rename fleet squad

Rename a fleet squad  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/squads/{squad_id}/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/squads/{squad_id}/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/squads/{squad_id}/&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FleetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    FleetsApi apiInstance = new FleetsApi(defaultClient);
    Long fleetId = 56L; // Long | ID for a fleet
    Long squadId = 56L; // Long | The squad to rename
    PutFleetsFleetIdSquadsSquadIdNaming naming = new PutFleetsFleetIdSquadsSquadIdNaming(); // PutFleetsFleetIdSquadsSquadIdNaming | New name of the squad
    String datasource = "tranquility"; // String | The server name you would like data from
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      apiInstance.putFleetsFleetIdSquadsSquadId(fleetId, squadId, naming, datasource, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetsApi#putFleetsFleetIdSquadsSquadId");
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
| **fleetId** | **Long**| ID for a fleet | |
| **squadId** | **Long**| The squad to rename | |
| **naming** | [**PutFleetsFleetIdSquadsSquadIdNaming**](PutFleetsFleetIdSquadsSquadIdNaming.md)| New name of the squad | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Squad renamed |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The fleet does not exist or you don&#39;t have access to it |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="putFleetsFleetIdWingsWingId"></a>
# **putFleetsFleetIdWingsWingId**
> putFleetsFleetIdWingsWingId(fleetId, wingId, naming, datasource, token)

Rename fleet wing

Rename a fleet wing  --- Alternate route: &#x60;/dev/fleets/{fleet_id}/wings/{wing_id}/&#x60;  Alternate route: &#x60;/legacy/fleets/{fleet_id}/wings/{wing_id}/&#x60;  Alternate route: &#x60;/v1/fleets/{fleet_id}/wings/{wing_id}/&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FleetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    FleetsApi apiInstance = new FleetsApi(defaultClient);
    Long fleetId = 56L; // Long | ID for a fleet
    Long wingId = 56L; // Long | The wing to rename
    PutFleetsFleetIdWingsWingIdNaming naming = new PutFleetsFleetIdWingsWingIdNaming(); // PutFleetsFleetIdWingsWingIdNaming | New name of the wing
    String datasource = "tranquility"; // String | The server name you would like data from
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      apiInstance.putFleetsFleetIdWingsWingId(fleetId, wingId, naming, datasource, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetsApi#putFleetsFleetIdWingsWingId");
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
| **fleetId** | **Long**| ID for a fleet | |
| **wingId** | **Long**| The wing to rename | |
| **naming** | [**PutFleetsFleetIdWingsWingIdNaming**](PutFleetsFleetIdWingsWingIdNaming.md)| New name of the wing | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Wing renamed |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The fleet does not exist or you don&#39;t have access to it |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

