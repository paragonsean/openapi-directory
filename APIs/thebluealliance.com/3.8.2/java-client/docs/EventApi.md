# EventApi

All URIs are relative to *https://www.thebluealliance.com/api/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDistrictEventsKeys_0**](EventApi.md#getDistrictEventsKeys_0) | **GET** /district/{district_key}/events/keys |  |
| [**getDistrictEventsSimple_0**](EventApi.md#getDistrictEventsSimple_0) | **GET** /district/{district_key}/events/simple |  |
| [**getDistrictEvents_0**](EventApi.md#getDistrictEvents_0) | **GET** /district/{district_key}/events |  |
| [**getEvent**](EventApi.md#getEvent) | **GET** /event/{event_key} |  |
| [**getEventAlliances**](EventApi.md#getEventAlliances) | **GET** /event/{event_key}/alliances |  |
| [**getEventAwards**](EventApi.md#getEventAwards) | **GET** /event/{event_key}/awards |  |
| [**getEventDistrictPoints**](EventApi.md#getEventDistrictPoints) | **GET** /event/{event_key}/district_points |  |
| [**getEventInsights**](EventApi.md#getEventInsights) | **GET** /event/{event_key}/insights |  |
| [**getEventMatchTimeseries**](EventApi.md#getEventMatchTimeseries) | **GET** /event/{event_key}/matches/timeseries |  |
| [**getEventMatches**](EventApi.md#getEventMatches) | **GET** /event/{event_key}/matches |  |
| [**getEventMatchesKeys**](EventApi.md#getEventMatchesKeys) | **GET** /event/{event_key}/matches/keys |  |
| [**getEventMatchesSimple**](EventApi.md#getEventMatchesSimple) | **GET** /event/{event_key}/matches/simple |  |
| [**getEventOPRs**](EventApi.md#getEventOPRs) | **GET** /event/{event_key}/oprs |  |
| [**getEventPredictions**](EventApi.md#getEventPredictions) | **GET** /event/{event_key}/predictions |  |
| [**getEventRankings**](EventApi.md#getEventRankings) | **GET** /event/{event_key}/rankings |  |
| [**getEventSimple**](EventApi.md#getEventSimple) | **GET** /event/{event_key}/simple |  |
| [**getEventTeams**](EventApi.md#getEventTeams) | **GET** /event/{event_key}/teams |  |
| [**getEventTeamsKeys**](EventApi.md#getEventTeamsKeys) | **GET** /event/{event_key}/teams/keys |  |
| [**getEventTeamsSimple**](EventApi.md#getEventTeamsSimple) | **GET** /event/{event_key}/teams/simple |  |
| [**getEventTeamsStatuses**](EventApi.md#getEventTeamsStatuses) | **GET** /event/{event_key}/teams/statuses |  |
| [**getEventsByYear**](EventApi.md#getEventsByYear) | **GET** /events/{year} |  |
| [**getEventsByYearKeys**](EventApi.md#getEventsByYearKeys) | **GET** /events/{year}/keys |  |
| [**getEventsByYearSimple**](EventApi.md#getEventsByYearSimple) | **GET** /events/{year}/simple |  |
| [**getTeamEventAwards_0**](EventApi.md#getTeamEventAwards_0) | **GET** /team/{team_key}/event/{event_key}/awards |  |
| [**getTeamEventMatchesKeys_0**](EventApi.md#getTeamEventMatchesKeys_0) | **GET** /team/{team_key}/event/{event_key}/matches/keys |  |
| [**getTeamEventMatchesSimple_0**](EventApi.md#getTeamEventMatchesSimple_0) | **GET** /team/{team_key}/event/{event_key}/matches/simple |  |
| [**getTeamEventMatches_0**](EventApi.md#getTeamEventMatches_0) | **GET** /team/{team_key}/event/{event_key}/matches |  |
| [**getTeamEventStatus_0**](EventApi.md#getTeamEventStatus_0) | **GET** /team/{team_key}/event/{event_key}/status |  |
| [**getTeamEventsByYearKeys_0**](EventApi.md#getTeamEventsByYearKeys_0) | **GET** /team/{team_key}/events/{year}/keys |  |
| [**getTeamEventsByYearSimple_0**](EventApi.md#getTeamEventsByYearSimple_0) | **GET** /team/{team_key}/events/{year}/simple |  |
| [**getTeamEventsByYear_0**](EventApi.md#getTeamEventsByYear_0) | **GET** /team/{team_key}/events/{year} |  |
| [**getTeamEventsKeys_0**](EventApi.md#getTeamEventsKeys_0) | **GET** /team/{team_key}/events/keys |  |
| [**getTeamEventsSimple_0**](EventApi.md#getTeamEventsSimple_0) | **GET** /team/{team_key}/events/simple |  |
| [**getTeamEventsStatusesByYear_1**](EventApi.md#getTeamEventsStatusesByYear_1) | **GET** /team/{team_key}/events/{year}/statuses |  |
| [**getTeamEvents_0**](EventApi.md#getTeamEvents_0) | **GET** /team/{team_key}/events |  |


<a id="getDistrictEventsKeys_0"></a>
# **getDistrictEventsKeys_0**
> List&lt;String&gt; getDistrictEventsKeys_0(districtKey, ifNoneMatch)



Gets a list of event keys for events in the given district.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String districtKey = "districtKey_example"; // String | TBA District Key, eg `2016fim`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<String> result = apiInstance.getDistrictEventsKeys_0(districtKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getDistrictEventsKeys_0");
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
| **districtKey** | **String**| TBA District Key, eg &#x60;2016fim&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getDistrictEventsSimple_0"></a>
# **getDistrictEventsSimple_0**
> List&lt;EventSimple&gt; getDistrictEventsSimple_0(districtKey, ifNoneMatch)



Gets a short-form list of events in the given district.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String districtKey = "districtKey_example"; // String | TBA District Key, eg `2016fim`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<EventSimple> result = apiInstance.getDistrictEventsSimple_0(districtKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getDistrictEventsSimple_0");
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
| **districtKey** | **String**| TBA District Key, eg &#x60;2016fim&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**List&lt;EventSimple&gt;**](EventSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getDistrictEvents_0"></a>
# **getDistrictEvents_0**
> List&lt;Event&gt; getDistrictEvents_0(districtKey, ifNoneMatch)



Gets a list of events in the given district.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String districtKey = "districtKey_example"; // String | TBA District Key, eg `2016fim`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<Event> result = apiInstance.getDistrictEvents_0(districtKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getDistrictEvents_0");
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
| **districtKey** | **String**| TBA District Key, eg &#x60;2016fim&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**List&lt;Event&gt;**](Event.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getEvent"></a>
# **getEvent**
> Event getEvent(eventKey, ifNoneMatch)



Gets an Event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      Event result = apiInstance.getEvent(eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEvent");
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
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**Event**](Event.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getEventAlliances"></a>
# **getEventAlliances**
> List&lt;EliminationAlliance&gt; getEventAlliances(eventKey, ifNoneMatch)



Gets a list of Elimination Alliances for the given Event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<EliminationAlliance> result = apiInstance.getEventAlliances(eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEventAlliances");
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
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**List&lt;EliminationAlliance&gt;**](EliminationAlliance.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getEventAwards"></a>
# **getEventAwards**
> List&lt;Award&gt; getEventAwards(eventKey, ifNoneMatch)



Gets a list of awards from the given event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<Award> result = apiInstance.getEventAwards(eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEventAwards");
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
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**List&lt;Award&gt;**](Award.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getEventDistrictPoints"></a>
# **getEventDistrictPoints**
> EventDistrictPoints getEventDistrictPoints(eventKey, ifNoneMatch)



Gets a list of team rankings for the Event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      EventDistrictPoints result = apiInstance.getEventDistrictPoints(eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEventDistrictPoints");
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
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**EventDistrictPoints**](EventDistrictPoints.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getEventInsights"></a>
# **getEventInsights**
> EventInsights getEventInsights(eventKey, ifNoneMatch)



Gets a set of Event-specific insights for the given Event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      EventInsights result = apiInstance.getEventInsights(eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEventInsights");
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
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**EventInsights**](EventInsights.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getEventMatchTimeseries"></a>
# **getEventMatchTimeseries**
> List&lt;String&gt; getEventMatchTimeseries(eventKey, ifNoneMatch)



Gets an array of Match Keys for the given event key that have timeseries data. Returns an empty array if no matches have timeseries data. *WARNING:* This is *not* official data, and is subject to a significant possibility of error, or missing data. Do not rely on this data for any purpose. In fact, pretend we made it up. *WARNING:* This endpoint and corresponding data models are under *active development* and may change at any time, including in breaking ways.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<String> result = apiInstance.getEventMatchTimeseries(eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEventMatchTimeseries");
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
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getEventMatches"></a>
# **getEventMatches**
> List&lt;Match&gt; getEventMatches(eventKey, ifNoneMatch)



Gets a list of matches for the given event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<Match> result = apiInstance.getEventMatches(eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEventMatches");
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
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**List&lt;Match&gt;**](Match.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getEventMatchesKeys"></a>
# **getEventMatchesKeys**
> List&lt;String&gt; getEventMatchesKeys(eventKey, ifNoneMatch)



Gets a list of match keys for the given event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<String> result = apiInstance.getEventMatchesKeys(eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEventMatchesKeys");
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
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getEventMatchesSimple"></a>
# **getEventMatchesSimple**
> List&lt;MatchSimple&gt; getEventMatchesSimple(eventKey, ifNoneMatch)



Gets a short-form list of matches for the given event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<MatchSimple> result = apiInstance.getEventMatchesSimple(eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEventMatchesSimple");
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
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**List&lt;MatchSimple&gt;**](MatchSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getEventOPRs"></a>
# **getEventOPRs**
> EventOPRs getEventOPRs(eventKey, ifNoneMatch)



Gets a set of Event OPRs (including OPR, DPR, and CCWM) for the given Event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      EventOPRs result = apiInstance.getEventOPRs(eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEventOPRs");
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
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**EventOPRs**](EventOPRs.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getEventPredictions"></a>
# **getEventPredictions**
> Object getEventPredictions(eventKey, ifNoneMatch)



Gets information on TBA-generated predictions for the given Event. Contains year-specific information. *WARNING* This endpoint is currently under development and may change at any time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      Object result = apiInstance.getEventPredictions(eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEventPredictions");
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
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getEventRankings"></a>
# **getEventRankings**
> EventRanking getEventRankings(eventKey, ifNoneMatch)



Gets a list of team rankings for the Event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      EventRanking result = apiInstance.getEventRankings(eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEventRankings");
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
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**EventRanking**](EventRanking.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getEventSimple"></a>
# **getEventSimple**
> EventSimple getEventSimple(eventKey, ifNoneMatch)



Gets a short-form Event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      EventSimple result = apiInstance.getEventSimple(eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEventSimple");
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
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**EventSimple**](EventSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getEventTeams"></a>
# **getEventTeams**
> List&lt;Team&gt; getEventTeams(eventKey, ifNoneMatch)



Gets a list of &#x60;Team&#x60; objects that competed in the given event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<Team> result = apiInstance.getEventTeams(eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEventTeams");
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
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**List&lt;Team&gt;**](Team.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getEventTeamsKeys"></a>
# **getEventTeamsKeys**
> List&lt;String&gt; getEventTeamsKeys(eventKey, ifNoneMatch)



Gets a list of &#x60;Team&#x60; keys that competed in the given event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<String> result = apiInstance.getEventTeamsKeys(eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEventTeamsKeys");
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
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getEventTeamsSimple"></a>
# **getEventTeamsSimple**
> List&lt;TeamSimple&gt; getEventTeamsSimple(eventKey, ifNoneMatch)



Gets a short-form list of &#x60;Team&#x60; objects that competed in the given event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<TeamSimple> result = apiInstance.getEventTeamsSimple(eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEventTeamsSimple");
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
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**List&lt;TeamSimple&gt;**](TeamSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getEventTeamsStatuses"></a>
# **getEventTeamsStatuses**
> Map&lt;String, TeamEventStatus&gt; getEventTeamsStatuses(eventKey, ifNoneMatch)



Gets a key-value list of the event statuses for teams competing at the given event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      Map<String, TeamEventStatus> result = apiInstance.getEventTeamsStatuses(eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEventTeamsStatuses");
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
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**Map&lt;String, TeamEventStatus&gt;**](TeamEventStatus.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getEventsByYear"></a>
# **getEventsByYear**
> List&lt;Event&gt; getEventsByYear(year, ifNoneMatch)



Gets a list of events in the given year.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    Integer year = 56; // Integer | Competition Year (or Season). Must be 4 digits.
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<Event> result = apiInstance.getEventsByYear(year, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEventsByYear");
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
| **year** | **Integer**| Competition Year (or Season). Must be 4 digits. | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**List&lt;Event&gt;**](Event.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getEventsByYearKeys"></a>
# **getEventsByYearKeys**
> List&lt;String&gt; getEventsByYearKeys(year, ifNoneMatch)



Gets a list of event keys in the given year.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    Integer year = 56; // Integer | Competition Year (or Season). Must be 4 digits.
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<String> result = apiInstance.getEventsByYearKeys(year, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEventsByYearKeys");
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
| **year** | **Integer**| Competition Year (or Season). Must be 4 digits. | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getEventsByYearSimple"></a>
# **getEventsByYearSimple**
> List&lt;EventSimple&gt; getEventsByYearSimple(year, ifNoneMatch)



Gets a short-form list of events in the given year.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    Integer year = 56; // Integer | Competition Year (or Season). Must be 4 digits.
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<EventSimple> result = apiInstance.getEventsByYearSimple(year, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEventsByYearSimple");
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
| **year** | **Integer**| Competition Year (or Season). Must be 4 digits. | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**List&lt;EventSimple&gt;**](EventSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getTeamEventAwards_0"></a>
# **getTeamEventAwards_0**
> List&lt;Award&gt; getTeamEventAwards_0(teamKey, eventKey, ifNoneMatch)



Gets a list of awards the given team won at the given event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<Award> result = apiInstance.getTeamEventAwards_0(teamKey, eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getTeamEventAwards_0");
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
| **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | |
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**List&lt;Award&gt;**](Award.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getTeamEventMatchesKeys_0"></a>
# **getTeamEventMatchesKeys_0**
> List&lt;String&gt; getTeamEventMatchesKeys_0(teamKey, eventKey, ifNoneMatch)



Gets a list of match keys for matches for the given team and event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<String> result = apiInstance.getTeamEventMatchesKeys_0(teamKey, eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getTeamEventMatchesKeys_0");
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
| **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | |
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getTeamEventMatchesSimple_0"></a>
# **getTeamEventMatchesSimple_0**
> List&lt;Match&gt; getTeamEventMatchesSimple_0(teamKey, eventKey, ifNoneMatch)



Gets a short-form list of matches for the given team and event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<Match> result = apiInstance.getTeamEventMatchesSimple_0(teamKey, eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getTeamEventMatchesSimple_0");
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
| **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | |
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**List&lt;Match&gt;**](Match.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getTeamEventMatches_0"></a>
# **getTeamEventMatches_0**
> List&lt;Match&gt; getTeamEventMatches_0(teamKey, eventKey, ifNoneMatch)



Gets a list of matches for the given team and event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<Match> result = apiInstance.getTeamEventMatches_0(teamKey, eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getTeamEventMatches_0");
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
| **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | |
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**List&lt;Match&gt;**](Match.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getTeamEventStatus_0"></a>
# **getTeamEventStatus_0**
> TeamEventStatus getTeamEventStatus_0(teamKey, eventKey, ifNoneMatch)



Gets the competition rank and status of the team at the given event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
    String eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      TeamEventStatus result = apiInstance.getTeamEventStatus_0(teamKey, eventKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getTeamEventStatus_0");
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
| **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | |
| **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**TeamEventStatus**](TeamEventStatus.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getTeamEventsByYearKeys_0"></a>
# **getTeamEventsByYearKeys_0**
> List&lt;String&gt; getTeamEventsByYearKeys_0(teamKey, year, ifNoneMatch)



Gets a list of the event keys for events this team has competed at in the given year.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
    Integer year = 56; // Integer | Competition Year (or Season). Must be 4 digits.
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<String> result = apiInstance.getTeamEventsByYearKeys_0(teamKey, year, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getTeamEventsByYearKeys_0");
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
| **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | |
| **year** | **Integer**| Competition Year (or Season). Must be 4 digits. | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getTeamEventsByYearSimple_0"></a>
# **getTeamEventsByYearSimple_0**
> List&lt;EventSimple&gt; getTeamEventsByYearSimple_0(teamKey, year, ifNoneMatch)



Gets a short-form list of events this team has competed at in the given year.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
    Integer year = 56; // Integer | Competition Year (or Season). Must be 4 digits.
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<EventSimple> result = apiInstance.getTeamEventsByYearSimple_0(teamKey, year, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getTeamEventsByYearSimple_0");
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
| **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | |
| **year** | **Integer**| Competition Year (or Season). Must be 4 digits. | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**List&lt;EventSimple&gt;**](EventSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getTeamEventsByYear_0"></a>
# **getTeamEventsByYear_0**
> List&lt;Event&gt; getTeamEventsByYear_0(teamKey, year, ifNoneMatch)



Gets a list of events this team has competed at in the given year.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
    Integer year = 56; // Integer | Competition Year (or Season). Must be 4 digits.
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<Event> result = apiInstance.getTeamEventsByYear_0(teamKey, year, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getTeamEventsByYear_0");
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
| **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | |
| **year** | **Integer**| Competition Year (or Season). Must be 4 digits. | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**List&lt;Event&gt;**](Event.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getTeamEventsKeys_0"></a>
# **getTeamEventsKeys_0**
> List&lt;String&gt; getTeamEventsKeys_0(teamKey, ifNoneMatch)



Gets a list of the event keys for all events this team has competed at.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<String> result = apiInstance.getTeamEventsKeys_0(teamKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getTeamEventsKeys_0");
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
| **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getTeamEventsSimple_0"></a>
# **getTeamEventsSimple_0**
> List&lt;EventSimple&gt; getTeamEventsSimple_0(teamKey, ifNoneMatch)



Gets a short-form list of all events this team has competed at.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<EventSimple> result = apiInstance.getTeamEventsSimple_0(teamKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getTeamEventsSimple_0");
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
| **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**List&lt;EventSimple&gt;**](EventSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getTeamEventsStatusesByYear_1"></a>
# **getTeamEventsStatusesByYear_1**
> Map&lt;String, TeamEventStatus&gt; getTeamEventsStatusesByYear_1(teamKey, year, ifNoneMatch)



Gets a key-value list of the event statuses for events this team has competed at in the given year.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
    Integer year = 56; // Integer | Competition Year (or Season). Must be 4 digits.
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      Map<String, TeamEventStatus> result = apiInstance.getTeamEventsStatusesByYear_1(teamKey, year, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getTeamEventsStatusesByYear_1");
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
| **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | |
| **year** | **Integer**| Competition Year (or Season). Must be 4 digits. | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**Map&lt;String, TeamEventStatus&gt;**](TeamEventStatus.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

<a id="getTeamEvents_0"></a>
# **getTeamEvents_0**
> List&lt;Event&gt; getTeamEvents_0(teamKey, ifNoneMatch)



Gets a list of all events this team has competed at.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.thebluealliance.com/api/v3");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    EventApi apiInstance = new EventApi(defaultClient);
    String teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
    String ifNoneMatch = "ifNoneMatch_example"; // String | Value of the `ETag` header in the most recently cached response by the client.
    try {
      List<Event> result = apiInstance.getTeamEvents_0(teamKey, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getTeamEvents_0");
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
| **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | |
| **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] |

### Return type

[**List&lt;Event&gt;**](Event.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  * Cache-Control - The &#x60;Cache-Control&#x60; header, in particular the &#x60;max-age&#x60; value, contains the number of seconds the result should be considered valid for. During this time subsequent calls should return from the local cache directly. <br>  * ETag - Specifies the version of the most recent response. Used by clients in the &#x60;If-None-Match&#x60; request header. <br>  |
| **304** | Not Modified - Use Local Cached Value |  -  |
| **401** |  |  -  |

