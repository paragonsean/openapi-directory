# CastCrewCastCrewInMoviesTelevisionShowsApi

All URIs are relative to *https://api.hillbillysoftware.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**actorGet**](CastCrewCastCrewInMoviesTelevisionShowsApi.md#actorGet) | **GET** /Actors/Search/{accesstoken}/{Query} | Returns data on queried actor/actress. Result set limited to 5 records |
| [**actorInShowsGet**](CastCrewCastCrewInMoviesTelevisionShowsApi.md#actorInShowsGet) | **GET** /Cast/ActorBySearch/{AccessToken}/{Actor} | Returns all shows queried actor/actress is or has been in |
| [**actorsInTVShowGet**](CastCrewCastCrewInMoviesTelevisionShowsApi.md#actorsInTVShowGet) | **GET** /Cast/ByTVShow/{accesstoken}/{ShowName} | Returns all actors in queried tvshow |
| [**addActorPost**](CastCrewCastCrewInMoviesTelevisionShowsApi.md#addActorPost) | **POST** /AddActor | Add new actor or actress to database |
| [**castByActorGet**](CastCrewCastCrewInMoviesTelevisionShowsApi.md#castByActorGet) | **GET** /Cast/ByActor/{AccessToken}/{Actor} | Returns list of show actor is appearing in |
| [**crewByIDGet**](CastCrewCastCrewInMoviesTelevisionShowsApi.md#crewByIDGet) | **GET** /Crew/ByID/{AccessToken}/{ID} | Get crew list by ID |
| [**crewByPersonGet**](CastCrewCastCrewInMoviesTelevisionShowsApi.md#crewByPersonGet) | **GET** /Crew/ByPerson/{AccessToken}/{PersonName} | Gets list of productions searched person is/was involved in. |
| [**crewGet**](CastCrewCastCrewInMoviesTelevisionShowsApi.md#crewGet) | **GET** /Crew/Search/{AccessToken}/{Phrase} | Returns crew for queried show. |
| [**crewbyShownameGet**](CastCrewCastCrewInMoviesTelevisionShowsApi.md#crewbyShownameGet) | **GET** /Crew/ByShowName/{AccessToken}/{ShowName} | Get crew list by showname |


<a id="actorGet"></a>
# **actorGet**
> List&lt;Actor&gt; actorGet(accesstoken, query)

Returns data on queried actor/actress. Result set limited to 5 records

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CastCrewCastCrewInMoviesTelevisionShowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    CastCrewCastCrewInMoviesTelevisionShowsApi apiInstance = new CastCrewCastCrewInMoviesTelevisionShowsApi(defaultClient);
    String accesstoken = "accesstoken_example"; // String | 
    String query = "query_example"; // String | 
    try {
      List<Actor> result = apiInstance.actorGet(accesstoken, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CastCrewCastCrewInMoviesTelevisionShowsApi#actorGet");
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
| **accesstoken** | **String**|  | |
| **query** | **String**|  | |

### Return type

[**List&lt;Actor&gt;**](Actor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Actors |  -  |

<a id="actorInShowsGet"></a>
# **actorInShowsGet**
> List&lt;TVShowActor&gt; actorInShowsGet(accessToken, actor)

Returns all shows queried actor/actress is or has been in

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CastCrewCastCrewInMoviesTelevisionShowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    CastCrewCastCrewInMoviesTelevisionShowsApi apiInstance = new CastCrewCastCrewInMoviesTelevisionShowsApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String actor = "actor_example"; // String | Part of, or full name of actor
    try {
      List<TVShowActor> result = apiInstance.actorInShowsGet(accessToken, actor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CastCrewCastCrewInMoviesTelevisionShowsApi#actorInShowsGet");
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
| **accessToken** | **String**|  | |
| **actor** | **String**| Part of, or full name of actor | |

### Return type

[**List&lt;TVShowActor&gt;**](TVShowActor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of actors in show |  -  |

<a id="actorsInTVShowGet"></a>
# **actorsInTVShowGet**
> List&lt;TVShowActor&gt; actorsInTVShowGet(accesstoken, showName)

Returns all actors in queried tvshow

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CastCrewCastCrewInMoviesTelevisionShowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    CastCrewCastCrewInMoviesTelevisionShowsApi apiInstance = new CastCrewCastCrewInMoviesTelevisionShowsApi(defaultClient);
    String accesstoken = "accesstoken_example"; // String | 
    String showName = "showName_example"; // String | 
    try {
      List<TVShowActor> result = apiInstance.actorsInTVShowGet(accesstoken, showName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CastCrewCastCrewInMoviesTelevisionShowsApi#actorsInTVShowGet");
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
| **accesstoken** | **String**|  | |
| **showName** | **String**|  | |

### Return type

[**List&lt;TVShowActor&gt;**](TVShowActor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of actors in show |  -  |

<a id="addActorPost"></a>
# **addActorPost**
> PostResult addActorPost(value)

Add new actor or actress to database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CastCrewCastCrewInMoviesTelevisionShowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    CastCrewCastCrewInMoviesTelevisionShowsApi apiInstance = new CastCrewCastCrewInMoviesTelevisionShowsApi(defaultClient);
    ActorPost value = new ActorPost(); // ActorPost | 
    try {
      PostResult result = apiInstance.addActorPost(value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CastCrewCastCrewInMoviesTelevisionShowsApi#addActorPost");
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
| **value** | [**ActorPost**](ActorPost.md)|  | |

### Return type

[**PostResult**](PostResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result |  -  |
| **204** | Result |  -  |

<a id="castByActorGet"></a>
# **castByActorGet**
> List&lt;TVShowActor&gt; castByActorGet(accessToken, actor)

Returns list of show actor is appearing in

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CastCrewCastCrewInMoviesTelevisionShowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    CastCrewCastCrewInMoviesTelevisionShowsApi apiInstance = new CastCrewCastCrewInMoviesTelevisionShowsApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String actor = "actor_example"; // String | Full name of actor
    try {
      List<TVShowActor> result = apiInstance.castByActorGet(accessToken, actor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CastCrewCastCrewInMoviesTelevisionShowsApi#castByActorGet");
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
| **accessToken** | **String**|  | |
| **actor** | **String**| Full name of actor | |

### Return type

[**List&lt;TVShowActor&gt;**](TVShowActor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of shows Actor is appearing in |  -  |

<a id="crewByIDGet"></a>
# **crewByIDGet**
> List&lt;Crew&gt; crewByIDGet(accessToken, ID)

Get crew list by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CastCrewCastCrewInMoviesTelevisionShowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    CastCrewCastCrewInMoviesTelevisionShowsApi apiInstance = new CastCrewCastCrewInMoviesTelevisionShowsApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String ID = "ID_example"; // String | IMDBID, TVmazeID, or TVDBID
    try {
      List<Crew> result = apiInstance.crewByIDGet(accessToken, ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CastCrewCastCrewInMoviesTelevisionShowsApi#crewByIDGet");
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
| **accessToken** | **String**|  | |
| **ID** | **String**| IMDBID, TVmazeID, or TVDBID | |

### Return type

[**List&lt;Crew&gt;**](Crew.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of crew |  -  |

<a id="crewByPersonGet"></a>
# **crewByPersonGet**
> List&lt;Crew&gt; crewByPersonGet(accessToken, personName)

Gets list of productions searched person is/was involved in.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CastCrewCastCrewInMoviesTelevisionShowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    CastCrewCastCrewInMoviesTelevisionShowsApi apiInstance = new CastCrewCastCrewInMoviesTelevisionShowsApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String personName = "personName_example"; // String | 
    try {
      List<Crew> result = apiInstance.crewByPersonGet(accessToken, personName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CastCrewCastCrewInMoviesTelevisionShowsApi#crewByPersonGet");
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
| **accessToken** | **String**|  | |
| **personName** | **String**|  | |

### Return type

[**List&lt;Crew&gt;**](Crew.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of crew |  -  |

<a id="crewGet"></a>
# **crewGet**
> List&lt;Crew&gt; crewGet(accessToken, phrase)

Returns crew for queried show.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CastCrewCastCrewInMoviesTelevisionShowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    CastCrewCastCrewInMoviesTelevisionShowsApi apiInstance = new CastCrewCastCrewInMoviesTelevisionShowsApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String phrase = "phrase_example"; // String | Part of, or full showname to search for
    try {
      List<Crew> result = apiInstance.crewGet(accessToken, phrase);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CastCrewCastCrewInMoviesTelevisionShowsApi#crewGet");
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
| **accessToken** | **String**|  | |
| **phrase** | **String**| Part of, or full showname to search for | |

### Return type

[**List&lt;Crew&gt;**](Crew.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of crew |  -  |

<a id="crewbyShownameGet"></a>
# **crewbyShownameGet**
> List&lt;Crew&gt; crewbyShownameGet(accessToken, showName)

Get crew list by showname

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CastCrewCastCrewInMoviesTelevisionShowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    CastCrewCastCrewInMoviesTelevisionShowsApi apiInstance = new CastCrewCastCrewInMoviesTelevisionShowsApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String showName = "showName_example"; // String | Full exact showname
    try {
      List<Crew> result = apiInstance.crewbyShownameGet(accessToken, showName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CastCrewCastCrewInMoviesTelevisionShowsApi#crewbyShownameGet");
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
| **accessToken** | **String**|  | |
| **showName** | **String**| Full exact showname | |

### Return type

[**List&lt;Crew&gt;**](Crew.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of crew |  -  |

