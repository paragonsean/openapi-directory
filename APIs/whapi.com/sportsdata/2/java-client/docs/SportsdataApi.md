# SportsdataApi

All URIs are relative to *https://sandbox.whapi.com/v2/sportsdata*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getClassesForSport**](SportsdataApi.md#getClassesForSport) | **GET** /sports/{sportId}/classes/ | Retrieves a list of classes for a given sport id. |
| [**getCompetition**](SportsdataApi.md#getCompetition) | **GET** /competitions/{competitionId} | Retrieves a specific competition |
| [**getCompetitionsForClass**](SportsdataApi.md#getCompetitionsForClass) | **GET** /classes/{classId}/competitions/ | Retrieves a list of competitions for a given class id. |
| [**getCompetitionsForSport**](SportsdataApi.md#getCompetitionsForSport) | **GET** /sports/{sportId}/competitions/ | Retrieves a list of competitions for a given sport id. |
| [**getEvent**](SportsdataApi.md#getEvent) | **GET** /events/{eventId} | Retrieves a single event by ID. |
| [**getEvents**](SportsdataApi.md#getEvents) | **GET** /events/ | Retrieves a list of events for the provided IDs. |
| [**getEventsForClass**](SportsdataApi.md#getEventsForClass) | **GET** /classes/{classId}/events/ | Retrieves a list of events for a given class id. |
| [**getEventsForCompetition**](SportsdataApi.md#getEventsForCompetition) | **GET** /competitions/{competitionId}/events/ | Retrieves a list of events for a given competition id. |
| [**getMarketGroupsForCompetition**](SportsdataApi.md#getMarketGroupsForCompetition) | **GET** /competitions/{competitionId}/marketgroups/ | Retrieves a list of market groups for a given competition id |
| [**getMarkets**](SportsdataApi.md#getMarkets) | **GET** /events/{eventId}/markets/ | Gets one or more specific markets |
| [**getMarketsByGroupId**](SportsdataApi.md#getMarketsByGroupId) | **GET** /competitions/{competitionId}/marketsByGroupid | Retrieves a list of events/markets/selections where markets within said event match selected sort/groupId |
| [**getSelections**](SportsdataApi.md#getSelections) | **GET** /events/{eventId}/markets/{marketId}/selections/ | Gets one or more selections for a market |
| [**getSports**](SportsdataApi.md#getSports) | **GET** /sports/ | Gets a list of all sports |
| [**getTopBets**](SportsdataApi.md#getTopBets) | **GET** /topbets/ | Retrieves a weighted list of Selections. |


<a id="getClassesForSport"></a>
# **getClassesForSport**
> ClassesWrapper getClassesForSport(apiKey, sportId, isPublished, fields, include, exclude, displayed, channel, status, sort, offset, limit, culture)

Retrieves a list of classes for a given sport id.

Retrieves a list of classes for a given sport id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SportsdataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.whapi.com/v2/sportsdata");

    SportsdataApi apiInstance = new SportsdataApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
    String sportId = "sportId_example"; // String | The sport id to retrieve information for.
    String isPublished = "true"; // String | Specify whether only active entities should be returned, according to the William Hill definition of active
    List<String> fields = Arrays.asList(); // List<String> | Specify an absolute field list to return (Comma-Separated List)
    List<String> include = Arrays.asList(); // List<String> | Specify fields in addition to the default to return (Comma-Separated List)
    List<String> exclude = Arrays.asList(); // List<String> | Specify fields from the default to exclude (Comma-Separated List)
    String displayed = "true"; // String | Specify whether to return displayed entities or not
    String channel = "channel_example"; // String | Specify a channel filter and only results from that channel will be returned
    String status = "status_example"; // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
    String sort = "id,asc"; // String | The field to order the response by, followed by the order. For example: name,desc
    Integer offset = 0; // Integer | Skip over a number of elements by specifying a start value for the query
    Integer limit = 100; // Integer | Specify the number of results to return
    String culture = "culture_example"; // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    try {
      ClassesWrapper result = apiInstance.getClassesForSport(apiKey, sportId, isPublished, fields, include, exclude, displayed, channel, status, sort, offset, limit, culture);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SportsdataApi#getClassesForSport");
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
| **apiKey** | **String**| Your API Key available from your developer portal | |
| **sportId** | **String**| The sport id to retrieve information for. | |
| **isPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to true] |
| **fields** | [**List&lt;String&gt;**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] |
| **exclude** | [**List&lt;String&gt;**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] |
| **displayed** | **String**| Specify whether to return displayed entities or not | [optional] [default to true] |
| **channel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] |
| **status** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] |
| **sort** | **String**| The field to order the response by, followed by the order. For example: name,desc | [optional] [default to id,asc] |
| **offset** | **Integer**| Skip over a number of elements by specifying a start value for the query | [optional] [default to 0] |
| **limit** | **Integer**| Specify the number of results to return | [optional] [default to 100] |
| **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] |

### Return type

[**ClassesWrapper**](ClassesWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Incorrect or Missing Parameter |  -  |
| **404** | No data found for request |  -  |

<a id="getCompetition"></a>
# **getCompetition**
> Competition getCompetition(apiKey, competitionId, fields, include, exclude, culture)

Retrieves a specific competition

Retrieves a specific competition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SportsdataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.whapi.com/v2/sportsdata");

    SportsdataApi apiInstance = new SportsdataApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
    String competitionId = "competitionId_example"; // String | The competition id to retrieve information for.
    List<String> fields = Arrays.asList(); // List<String> | Specify an absolute field list to return (Comma-Separated List)
    List<String> include = Arrays.asList(); // List<String> | Specify fields in addition to the default to return (Comma-Separated List)
    List<String> exclude = Arrays.asList(); // List<String> | Specify fields from the default to exclude (Comma-Separated List)
    String culture = "culture_example"; // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    try {
      Competition result = apiInstance.getCompetition(apiKey, competitionId, fields, include, exclude, culture);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SportsdataApi#getCompetition");
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
| **apiKey** | **String**| Your API Key available from your developer portal | |
| **competitionId** | **String**| The competition id to retrieve information for. | |
| **fields** | [**List&lt;String&gt;**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] |
| **exclude** | [**List&lt;String&gt;**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] |
| **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] |

### Return type

[**Competition**](Competition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Incorrect or Missing Parameter |  -  |
| **404** | No data found for request |  -  |

<a id="getCompetitionsForClass"></a>
# **getCompetitionsForClass**
> CompetitionsWrapper getCompetitionsForClass(apiKey, classId, isPublished, fields, include, exclude, displayed, channel, status, sort, offset, limit, culture)

Retrieves a list of competitions for a given class id.

Retrieves a list of competitions for a given class id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SportsdataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.whapi.com/v2/sportsdata");

    SportsdataApi apiInstance = new SportsdataApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
    String classId = "classId_example"; // String | The class id to retrieve information for.
    String isPublished = "true"; // String | Specify whether only active entities should be returned, according to the William Hill definition of active
    List<String> fields = Arrays.asList(); // List<String> | Specify an absolute field list to return (Comma-Separated List)
    List<String> include = Arrays.asList(); // List<String> | Specify fields in addition to the default to return (Comma-Separated List)
    List<String> exclude = Arrays.asList(); // List<String> | Specify fields from the default to exclude (Comma-Separated List)
    String displayed = "true"; // String | Specify whether to return displayed entities or not
    String channel = "channel_example"; // String | Specify a channel filter and only results from that channel will be returned
    String status = "status_example"; // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
    String sort = "id,asc"; // String | The field to order the response by, followed by the order. For example: name,desc
    Integer offset = 0; // Integer | Skip over a number of elements by specifying a start value for the query
    Integer limit = 100; // Integer | Specify the number of results to return
    String culture = "culture_example"; // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    try {
      CompetitionsWrapper result = apiInstance.getCompetitionsForClass(apiKey, classId, isPublished, fields, include, exclude, displayed, channel, status, sort, offset, limit, culture);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SportsdataApi#getCompetitionsForClass");
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
| **apiKey** | **String**| Your API Key available from your developer portal | |
| **classId** | **String**| The class id to retrieve information for. | |
| **isPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to true] |
| **fields** | [**List&lt;String&gt;**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] |
| **exclude** | [**List&lt;String&gt;**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] |
| **displayed** | **String**| Specify whether to return displayed entities or not | [optional] [default to true] |
| **channel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] |
| **status** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] |
| **sort** | **String**| The field to order the response by, followed by the order. For example: name,desc | [optional] [default to id,asc] |
| **offset** | **Integer**| Skip over a number of elements by specifying a start value for the query | [optional] [default to 0] |
| **limit** | **Integer**| Specify the number of results to return | [optional] [default to 100] |
| **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] |

### Return type

[**CompetitionsWrapper**](CompetitionsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Incorrect or Missing Parameter |  -  |
| **404** | No data found for request |  -  |

<a id="getCompetitionsForSport"></a>
# **getCompetitionsForSport**
> CompetitionsWrapper getCompetitionsForSport(apiKey, sportId, isPublished, fields, include, exclude, displayed, channel, status, sort, offset, limit, culture)

Retrieves a list of competitions for a given sport id.

Retrieves a list of competitions for a given sport id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SportsdataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.whapi.com/v2/sportsdata");

    SportsdataApi apiInstance = new SportsdataApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
    String sportId = "sportId_example"; // String | The sport id to retrieve information for.
    String isPublished = "true"; // String | Specify whether only active entities should be returned, according to the William Hill definition of active
    List<String> fields = Arrays.asList(); // List<String> | Specify an absolute field list to return (Comma-Separated List)
    List<String> include = Arrays.asList(); // List<String> | Specify fields in addition to the default to return (Comma-Separated List)
    List<String> exclude = Arrays.asList(); // List<String> | Specify fields from the default to exclude (Comma-Separated List)
    String displayed = "true"; // String | Specify whether to return displayed entities or not
    String channel = "channel_example"; // String | Specify a channel filter and only results from that channel will be returned
    String status = "status_example"; // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
    String sort = "id,asc"; // String | The field to order the response by, followed by the order. For example: name,desc
    Integer offset = 0; // Integer | Skip over a number of elements by specifying a start value for the query
    Integer limit = 100; // Integer | Specify the number of results to return
    String culture = "culture_example"; // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    try {
      CompetitionsWrapper result = apiInstance.getCompetitionsForSport(apiKey, sportId, isPublished, fields, include, exclude, displayed, channel, status, sort, offset, limit, culture);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SportsdataApi#getCompetitionsForSport");
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
| **apiKey** | **String**| Your API Key available from your developer portal | |
| **sportId** | **String**| The sport id to retrieve information for. | |
| **isPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to true] |
| **fields** | [**List&lt;String&gt;**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] |
| **exclude** | [**List&lt;String&gt;**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] |
| **displayed** | **String**| Specify whether to return displayed entities or not | [optional] [default to true] |
| **channel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] |
| **status** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] |
| **sort** | **String**| The field to order the response by, followed by the order. For example: name,desc | [optional] [default to id,asc] |
| **offset** | **Integer**| Skip over a number of elements by specifying a start value for the query | [optional] [default to 0] |
| **limit** | **Integer**| Specify the number of results to return | [optional] [default to 100] |
| **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] |

### Return type

[**CompetitionsWrapper**](CompetitionsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Incorrect or Missing Parameter |  -  |
| **404** | No data found for request |  -  |

<a id="getEvent"></a>
# **getEvent**
> EventsWrapper getEvent(apiKey, eventId, includeAllDescendants, fields, include, exclude, headlineSummary, marketCount, marketIds, includeEmpty, culture, marketPublished, marketStatus, marketDisplayed, marketChannel, marketSort, marketEW, selectionStatus, selectionChannel, selectionPublished)

Retrieves a single event by ID.

Retrieves a single event by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SportsdataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.whapi.com/v2/sportsdata");

    SportsdataApi apiInstance = new SportsdataApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
    String eventId = "eventId_example"; // String | The event ID to retrieve information for.
    Boolean includeAllDescendants = false; // Boolean | Include every descendant in the below heirarchy
    List<String> fields = Arrays.asList(); // List<String> | Specify an absolute field list to return (Comma-Separated List)
    List<String> include = Arrays.asList(); // List<String> | Specify fields in addition to the default to return (Comma-Separated List)
    List<String> exclude = Arrays.asList(); // List<String> | Specify fields from the default to exclude (Comma-Separated List)
    Boolean headlineSummary = false; // Boolean | Return only headline markets (Markets with the lowest display order) Either 1 InPlay and 1 Pre-Match, or the amount specified in marketCount, if available. Markets and Outcomes will be returned.
    Integer marketCount = 1; // Integer | Specify the number of markets to return when requesting headlineSummary. This count of InPlay and Pre-Match markets will be returned.For example, when specifying 1, 1 In Play and 1 Pre Match market will be returned.
    List<String> marketIds = Arrays.asList(); // List<String> | Comma-seaerated list of market IDs to filter by
    Boolean includeEmpty = true; // Boolean | When declared as false it should exclude markets and events that have no selections / markets
    String culture = "culture_example"; // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    String marketPublished = "true"; // String | Specify whether only active entities should be returned, according to the William Hill definition of active
    String marketStatus = "marketStatus_example"; // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
    String marketDisplayed = "true"; // String | Specify whether to return displayed entities or not
    String marketChannel = "marketChannel_example"; // String | Specify a channel filter and only results from that channel will be returned
    String marketSort = "marketSort_example"; // String | Filter by market sort (e.g. MR (match result) -- (Outright)).
    String marketEW = "marketEW_example"; // String | Specify whether to return markets with each way betting or those without
    String selectionStatus = "selectionStatus_example"; // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
    String selectionChannel = "selectionChannel_example"; // String | Specify a channel filter and only results from that channel will be returned
    String selectionPublished = "true"; // String | Specify whether only active entities should be returned, according to the William Hill definition of active
    try {
      EventsWrapper result = apiInstance.getEvent(apiKey, eventId, includeAllDescendants, fields, include, exclude, headlineSummary, marketCount, marketIds, includeEmpty, culture, marketPublished, marketStatus, marketDisplayed, marketChannel, marketSort, marketEW, selectionStatus, selectionChannel, selectionPublished);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SportsdataApi#getEvent");
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
| **apiKey** | **String**| Your API Key available from your developer portal | |
| **eventId** | **String**| The event ID to retrieve information for. | |
| **includeAllDescendants** | **Boolean**| Include every descendant in the below heirarchy | [optional] [default to false] |
| **fields** | [**List&lt;String&gt;**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] |
| **exclude** | [**List&lt;String&gt;**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] |
| **headlineSummary** | **Boolean**| Return only headline markets (Markets with the lowest display order) Either 1 InPlay and 1 Pre-Match, or the amount specified in marketCount, if available. Markets and Outcomes will be returned. | [optional] [default to false] |
| **marketCount** | **Integer**| Specify the number of markets to return when requesting headlineSummary. This count of InPlay and Pre-Match markets will be returned.For example, when specifying 1, 1 In Play and 1 Pre Match market will be returned. | [optional] [default to 1] |
| **marketIds** | [**List&lt;String&gt;**](String.md)| Comma-seaerated list of market IDs to filter by | [optional] |
| **includeEmpty** | **Boolean**| When declared as false it should exclude markets and events that have no selections / markets | [optional] [default to true] |
| **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] |
| **marketPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to true] |
| **marketStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] |
| **marketDisplayed** | **String**| Specify whether to return displayed entities or not | [optional] [default to true] |
| **marketChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] |
| **marketSort** | **String**| Filter by market sort (e.g. MR (match result) -- (Outright)). | [optional] |
| **marketEW** | **String**| Specify whether to return markets with each way betting or those without | [optional] |
| **selectionStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] |
| **selectionChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] |
| **selectionPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to true] |

### Return type

[**EventsWrapper**](EventsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Incorrect or Missing Parameter |  -  |
| **404** | No data found for request |  -  |

<a id="getEvents"></a>
# **getEvents**
> EventsWrapper getEvents(apiKey, ids, isPublished, includeAllDescendants, fields, include, exclude, channel, settled, includeEmpty, headlineSummary, marketCount, sort, offset, limit, marketIds, culture, marketPublished, marketStatus, marketDisplayed, marketChannel, marketSort, marketEW, selectionStatus, selectionChannel, selectionPublished)

Retrieves a list of events for the provided IDs.

Retrieves a list of events for the provided IDs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SportsdataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.whapi.com/v2/sportsdata");

    SportsdataApi apiInstance = new SportsdataApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
    List<String> ids = Arrays.asList(); // List<String> | A comma-separated list of selectionIds
    String isPublished = "true"; // String | Specify whether only active entities should be returned, according to the William Hill definition of active
    Boolean includeAllDescendants = false; // Boolean | Include every descendant in the below heirarchy
    List<String> fields = Arrays.asList(); // List<String> | Specify an absolute field list to return (Comma-Separated List)
    List<String> include = Arrays.asList(); // List<String> | Specify fields in addition to the default to return (Comma-Separated List)
    List<String> exclude = Arrays.asList(); // List<String> | Specify fields from the default to exclude (Comma-Separated List)
    String channel = "channel_example"; // String | Specify a channel filter and only results from that channel will be returned
    Boolean settled = true; // Boolean | Specify wether only settled entities should be returned
    Boolean includeEmpty = true; // Boolean | When declared as false it should exclude markets and events that have no selections / markets
    Boolean headlineSummary = false; // Boolean | Return only headline markets (Markets with the lowest display order) Either 1 InPlay and 1 Pre-Match, or the amount specified in marketCount, if available. Markets and Outcomes will be returned.
    Integer marketCount = 1; // Integer | Specify the number of markets to return when requesting headlineSummary. This count of InPlay and Pre-Match markets will be returned.For example, when specifying 1, 1 In Play and 1 Pre Match market will be returned.
    String sort = "id,asc"; // String | The field to order the response by, followed by the order. For example: name,desc
    Integer offset = 0; // Integer | Skip over a number of elements by specifying a start value for the query
    Integer limit = 100; // Integer | Specify the number of results to return
    List<String> marketIds = Arrays.asList(); // List<String> | Comma-seaerated list of market IDs to filter by
    String culture = "culture_example"; // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    String marketPublished = "true"; // String | Specify whether only active entities should be returned, according to the William Hill definition of active
    String marketStatus = "marketStatus_example"; // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
    String marketDisplayed = "true"; // String | Specify whether to return displayed entities or not
    String marketChannel = "marketChannel_example"; // String | Specify a channel filter and only results from that channel will be returned
    String marketSort = "marketSort_example"; // String | Filter by market sort (e.g. MR (match result) -- (Outright)).
    String marketEW = "marketEW_example"; // String | Specify whether to return markets with each way betting or those without
    String selectionStatus = "selectionStatus_example"; // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
    String selectionChannel = "selectionChannel_example"; // String | Specify a channel filter and only results from that channel will be returned
    String selectionPublished = "true"; // String | Specify whether only active entities should be returned, according to the William Hill definition of active
    try {
      EventsWrapper result = apiInstance.getEvents(apiKey, ids, isPublished, includeAllDescendants, fields, include, exclude, channel, settled, includeEmpty, headlineSummary, marketCount, sort, offset, limit, marketIds, culture, marketPublished, marketStatus, marketDisplayed, marketChannel, marketSort, marketEW, selectionStatus, selectionChannel, selectionPublished);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SportsdataApi#getEvents");
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
| **apiKey** | **String**| Your API Key available from your developer portal | |
| **ids** | [**List&lt;String&gt;**](String.md)| A comma-separated list of selectionIds | [optional] |
| **isPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to true] |
| **includeAllDescendants** | **Boolean**| Include every descendant in the below heirarchy | [optional] [default to false] |
| **fields** | [**List&lt;String&gt;**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] |
| **exclude** | [**List&lt;String&gt;**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] |
| **channel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] |
| **settled** | **Boolean**| Specify wether only settled entities should be returned | [optional] |
| **includeEmpty** | **Boolean**| When declared as false it should exclude markets and events that have no selections / markets | [optional] [default to true] |
| **headlineSummary** | **Boolean**| Return only headline markets (Markets with the lowest display order) Either 1 InPlay and 1 Pre-Match, or the amount specified in marketCount, if available. Markets and Outcomes will be returned. | [optional] [default to false] |
| **marketCount** | **Integer**| Specify the number of markets to return when requesting headlineSummary. This count of InPlay and Pre-Match markets will be returned.For example, when specifying 1, 1 In Play and 1 Pre Match market will be returned. | [optional] [default to 1] |
| **sort** | **String**| The field to order the response by, followed by the order. For example: name,desc | [optional] [default to id,asc] |
| **offset** | **Integer**| Skip over a number of elements by specifying a start value for the query | [optional] [default to 0] |
| **limit** | **Integer**| Specify the number of results to return | [optional] [default to 100] |
| **marketIds** | [**List&lt;String&gt;**](String.md)| Comma-seaerated list of market IDs to filter by | [optional] |
| **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] |
| **marketPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to true] |
| **marketStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] |
| **marketDisplayed** | **String**| Specify whether to return displayed entities or not | [optional] [default to true] |
| **marketChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] |
| **marketSort** | **String**| Filter by market sort (e.g. MR (match result) -- (Outright)). | [optional] |
| **marketEW** | **String**| Specify whether to return markets with each way betting or those without | [optional] |
| **selectionStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] |
| **selectionChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] |
| **selectionPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to true] |

### Return type

[**EventsWrapper**](EventsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Incorrect or Missing Parameter |  -  |
| **404** | No data found for request |  -  |

<a id="getEventsForClass"></a>
# **getEventsForClass**
> EventsWrapper getEventsForClass(apiKey, classId, isPublished, fields, include, exclude, displayed, channel, settled, includeEmpty, status, sort, offset, limit, headlineSummary, includeAllDescendants, isInPlay, marketCount, date, dateFrom, dateTo, eventSort, culture, marketPublished, marketStatus, marketDisplayed, marketChannel, marketSort, marketEW, selectionStatus, selectionChannel, selectionPublished)

Retrieves a list of events for a given class id.

Retrieves a list of events for a given class id. &#39;includeAllDescendants&#39; parameter should be accompanied with &#39;date&#39; filter or one of &#39;dateFrom&#39; and &#39;dateTo&#39; filters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SportsdataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.whapi.com/v2/sportsdata");

    SportsdataApi apiInstance = new SportsdataApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
    String classId = "classId_example"; // String | The class id to retrieve information for.
    String isPublished = "true"; // String | Specify whether only active entities should be returned, according to the William Hill definition of active
    List<String> fields = Arrays.asList(); // List<String> | Specify an absolute field list to return (Comma-Separated List)
    List<String> include = Arrays.asList(); // List<String> | Specify fields in addition to the default to return (Comma-Separated List)
    List<String> exclude = Arrays.asList(); // List<String> | Specify fields from the default to exclude (Comma-Separated List)
    String displayed = "true"; // String | Specify whether to return displayed entities or not
    String channel = "channel_example"; // String | Specify a channel filter and only results from that channel will be returned
    Boolean settled = true; // Boolean | Specify wether only settled entities should be returned
    Boolean includeEmpty = true; // Boolean | When declared as false it should exclude markets and events that have no selections / markets
    String status = "status_example"; // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
    String sort = "id,asc"; // String | The field to order the response by, followed by the order. For example: name,desc
    Integer offset = 0; // Integer | Skip over a number of elements by specifying a start value for the query
    Integer limit = 100; // Integer | Specify the number of results to return
    Boolean headlineSummary = false; // Boolean | Return only headline markets (Markets with the lowest display order) Either 1 InPlay and 1 Pre-Match, or the amount specified in marketCount, if available. Markets and Outcomes will be returned.
    Boolean includeAllDescendants = false; // Boolean | Include every descendant in the below heirarchy
    Boolean isInPlay = true; // Boolean | Show only events that are in-play
    Integer marketCount = 1; // Integer | Specify the number of markets to return when requesting headlineSummary. This count of InPlay and Pre-Match markets will be returned.For example, when specifying 1, 1 In Play and 1 Pre Match market will be returned.
    String date = "date_example"; // String | Return only events for the specified date (yyyy-MM-dd).
    String dateFrom = "dateFrom_example"; // String | The UTC datetime from the events to be returned. (yyyy-MM-ddTHH:mm:ss)
    String dateTo = "dateTo_example"; // String | The UTC datetime TO the events to be returned. (yyyy-MM-ddTHH:mm:ss)
    String eventSort = "eventSort_example"; // String | Filter event by event sort
    String culture = "culture_example"; // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    String marketPublished = "true"; // String | Specify whether only active entities should be returned, according to the William Hill definition of active
    String marketStatus = "marketStatus_example"; // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
    String marketDisplayed = "true"; // String | Specify whether to return displayed entities or not
    String marketChannel = "marketChannel_example"; // String | Specify a channel filter and only results from that channel will be returned
    String marketSort = "marketSort_example"; // String | Filter by market sort (e.g. MR (match result) -- (Outright)).
    String marketEW = "marketEW_example"; // String | Specify whether to return markets with each way betting or those without
    String selectionStatus = "selectionStatus_example"; // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
    String selectionChannel = "selectionChannel_example"; // String | Specify a channel filter and only results from that channel will be returned
    String selectionPublished = "true"; // String | Specify whether only active entities should be returned, according to the William Hill definition of active
    try {
      EventsWrapper result = apiInstance.getEventsForClass(apiKey, classId, isPublished, fields, include, exclude, displayed, channel, settled, includeEmpty, status, sort, offset, limit, headlineSummary, includeAllDescendants, isInPlay, marketCount, date, dateFrom, dateTo, eventSort, culture, marketPublished, marketStatus, marketDisplayed, marketChannel, marketSort, marketEW, selectionStatus, selectionChannel, selectionPublished);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SportsdataApi#getEventsForClass");
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
| **apiKey** | **String**| Your API Key available from your developer portal | |
| **classId** | **String**| The class id to retrieve information for. | |
| **isPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to true] |
| **fields** | [**List&lt;String&gt;**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] |
| **exclude** | [**List&lt;String&gt;**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] |
| **displayed** | **String**| Specify whether to return displayed entities or not | [optional] [default to true] |
| **channel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] |
| **settled** | **Boolean**| Specify wether only settled entities should be returned | [optional] |
| **includeEmpty** | **Boolean**| When declared as false it should exclude markets and events that have no selections / markets | [optional] [default to true] |
| **status** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] |
| **sort** | **String**| The field to order the response by, followed by the order. For example: name,desc | [optional] [default to id,asc] |
| **offset** | **Integer**| Skip over a number of elements by specifying a start value for the query | [optional] [default to 0] |
| **limit** | **Integer**| Specify the number of results to return | [optional] [default to 100] |
| **headlineSummary** | **Boolean**| Return only headline markets (Markets with the lowest display order) Either 1 InPlay and 1 Pre-Match, or the amount specified in marketCount, if available. Markets and Outcomes will be returned. | [optional] [default to false] |
| **includeAllDescendants** | **Boolean**| Include every descendant in the below heirarchy | [optional] [default to false] |
| **isInPlay** | **Boolean**| Show only events that are in-play | [optional] |
| **marketCount** | **Integer**| Specify the number of markets to return when requesting headlineSummary. This count of InPlay and Pre-Match markets will be returned.For example, when specifying 1, 1 In Play and 1 Pre Match market will be returned. | [optional] [default to 1] |
| **date** | **String**| Return only events for the specified date (yyyy-MM-dd). | [optional] |
| **dateFrom** | **String**| The UTC datetime from the events to be returned. (yyyy-MM-ddTHH:mm:ss) | [optional] |
| **dateTo** | **String**| The UTC datetime TO the events to be returned. (yyyy-MM-ddTHH:mm:ss) | [optional] |
| **eventSort** | **String**| Filter event by event sort | [optional] |
| **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] |
| **marketPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to true] |
| **marketStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] |
| **marketDisplayed** | **String**| Specify whether to return displayed entities or not | [optional] [default to true] |
| **marketChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] |
| **marketSort** | **String**| Filter by market sort (e.g. MR (match result) -- (Outright)). | [optional] |
| **marketEW** | **String**| Specify whether to return markets with each way betting or those without | [optional] |
| **selectionStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] |
| **selectionChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] |
| **selectionPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to true] |

### Return type

[**EventsWrapper**](EventsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Incorrect or Missing Parameter |  -  |
| **404** | No data found for request |  -  |

<a id="getEventsForCompetition"></a>
# **getEventsForCompetition**
> EventsWrapper getEventsForCompetition(apiKey, competitionId, isPublished, fields, include, exclude, displayed, channel, settled, includeEmpty, status, sort, offset, limit, headlineSummary, includeAllDescendants, isInPlay, marketCount, date, dateFrom, dateTo, marketGroupId, eventSort, culture, marketPublished, marketStatus, marketDisplayed, marketChannel, marketSort, marketEW, selectionStatus, selectionChannel, selectionPublished)

Retrieves a list of events for a given competition id.

Retrieves a list of events for a given competition id. &#39;headlineSummary&#39; and includeAllDescendants parameters should be accompanied with &#39;date&#39; filter or one of &#39;dateFrom&#39; and &#39;dateTo&#39; filters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SportsdataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.whapi.com/v2/sportsdata");

    SportsdataApi apiInstance = new SportsdataApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
    String competitionId = "competitionId_example"; // String | The competition id to retrieve information for.
    String isPublished = "true"; // String | Specify whether only active entities should be returned, according to the William Hill definition of active
    List<String> fields = Arrays.asList(); // List<String> | Specify an absolute field list to return (Comma-Separated List)
    List<String> include = Arrays.asList(); // List<String> | Specify fields in addition to the default to return (Comma-Separated List)
    List<String> exclude = Arrays.asList(); // List<String> | Specify fields from the default to exclude (Comma-Separated List)
    String displayed = "true"; // String | Specify whether to return displayed entities or not
    String channel = "channel_example"; // String | Specify a channel filter and only results from that channel will be returned
    Boolean settled = true; // Boolean | Specify wether only settled entities should be returned
    Boolean includeEmpty = true; // Boolean | When declared as false it should exclude markets and events that have no selections / markets
    String status = "status_example"; // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
    String sort = "id,asc"; // String | The field to order the response by, followed by the order. For example: name,desc
    Integer offset = 0; // Integer | Skip over a number of elements by specifying a start value for the query
    Integer limit = 100; // Integer | Specify the number of results to return
    Boolean headlineSummary = false; // Boolean | Return only headline markets (Markets with the lowest display order) Either 1 InPlay and 1 Pre-Match, or the amount specified in marketCount, if available. Markets and Outcomes will be returned.
    Boolean includeAllDescendants = false; // Boolean | Include every descendant in the below heirarchy
    Boolean isInPlay = true; // Boolean | Show only events that are in-play
    Integer marketCount = 1; // Integer | Specify the number of markets to return when requesting headlineSummary. This count of InPlay and Pre-Match markets will be returned.For example, when specifying 1, 1 In Play and 1 Pre Match market will be returned.
    String date = "date_example"; // String | Return only events for the specified date (yyyy-MM-dd).
    String dateFrom = "dateFrom_example"; // String | The UTC datetime from the events to be returned. (yyyy-MM-ddTHH:mm:ss)
    String dateTo = "dateTo_example"; // String | The UTC datetime TO the events to be returned. (yyyy-MM-ddTHH:mm:ss)
    String marketGroupId = "marketGroupId_example"; // String | Filter by marketGroupId (e.g. OB_MG1276585).
    String eventSort = "eventSort_example"; // String | Filter event by event sort
    String culture = "culture_example"; // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    String marketPublished = "true"; // String | Specify whether only active entities should be returned, according to the William Hill definition of active
    String marketStatus = "marketStatus_example"; // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
    String marketDisplayed = "true"; // String | Specify whether to return displayed entities or not
    String marketChannel = "marketChannel_example"; // String | Specify a channel filter and only results from that channel will be returned
    String marketSort = "marketSort_example"; // String | Filter by market sort (e.g. MR (match result) -- (Outright)).
    String marketEW = "marketEW_example"; // String | Specify whether to return markets with each way betting or those without
    String selectionStatus = "selectionStatus_example"; // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
    String selectionChannel = "selectionChannel_example"; // String | Specify a channel filter and only results from that channel will be returned
    String selectionPublished = "true"; // String | Specify whether only active entities should be returned, according to the William Hill definition of active
    try {
      EventsWrapper result = apiInstance.getEventsForCompetition(apiKey, competitionId, isPublished, fields, include, exclude, displayed, channel, settled, includeEmpty, status, sort, offset, limit, headlineSummary, includeAllDescendants, isInPlay, marketCount, date, dateFrom, dateTo, marketGroupId, eventSort, culture, marketPublished, marketStatus, marketDisplayed, marketChannel, marketSort, marketEW, selectionStatus, selectionChannel, selectionPublished);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SportsdataApi#getEventsForCompetition");
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
| **apiKey** | **String**| Your API Key available from your developer portal | |
| **competitionId** | **String**| The competition id to retrieve information for. | |
| **isPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to true] |
| **fields** | [**List&lt;String&gt;**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] |
| **exclude** | [**List&lt;String&gt;**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] |
| **displayed** | **String**| Specify whether to return displayed entities or not | [optional] [default to true] |
| **channel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] |
| **settled** | **Boolean**| Specify wether only settled entities should be returned | [optional] |
| **includeEmpty** | **Boolean**| When declared as false it should exclude markets and events that have no selections / markets | [optional] [default to true] |
| **status** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] |
| **sort** | **String**| The field to order the response by, followed by the order. For example: name,desc | [optional] [default to id,asc] |
| **offset** | **Integer**| Skip over a number of elements by specifying a start value for the query | [optional] [default to 0] |
| **limit** | **Integer**| Specify the number of results to return | [optional] [default to 100] |
| **headlineSummary** | **Boolean**| Return only headline markets (Markets with the lowest display order) Either 1 InPlay and 1 Pre-Match, or the amount specified in marketCount, if available. Markets and Outcomes will be returned. | [optional] [default to false] |
| **includeAllDescendants** | **Boolean**| Include every descendant in the below heirarchy | [optional] [default to false] |
| **isInPlay** | **Boolean**| Show only events that are in-play | [optional] |
| **marketCount** | **Integer**| Specify the number of markets to return when requesting headlineSummary. This count of InPlay and Pre-Match markets will be returned.For example, when specifying 1, 1 In Play and 1 Pre Match market will be returned. | [optional] [default to 1] |
| **date** | **String**| Return only events for the specified date (yyyy-MM-dd). | [optional] |
| **dateFrom** | **String**| The UTC datetime from the events to be returned. (yyyy-MM-ddTHH:mm:ss) | [optional] |
| **dateTo** | **String**| The UTC datetime TO the events to be returned. (yyyy-MM-ddTHH:mm:ss) | [optional] |
| **marketGroupId** | **String**| Filter by marketGroupId (e.g. OB_MG1276585). | [optional] |
| **eventSort** | **String**| Filter event by event sort | [optional] |
| **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] |
| **marketPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to true] |
| **marketStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] |
| **marketDisplayed** | **String**| Specify whether to return displayed entities or not | [optional] [default to true] |
| **marketChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] |
| **marketSort** | **String**| Filter by market sort (e.g. MR (match result) -- (Outright)). | [optional] |
| **marketEW** | **String**| Specify whether to return markets with each way betting or those without | [optional] |
| **selectionStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] |
| **selectionChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] |
| **selectionPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to true] |

### Return type

[**EventsWrapper**](EventsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Incorrect or Missing Parameter |  -  |
| **404** | No data found for request |  -  |

<a id="getMarketGroupsForCompetition"></a>
# **getMarketGroupsForCompetition**
> MarketGroupsWrapper getMarketGroupsForCompetition(apiKey, competitionId, fields, include, exclude, sort, offset, limit, culture, name)

Retrieves a list of market groups for a given competition id

Retrieves a list of market groups for a given competition id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SportsdataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.whapi.com/v2/sportsdata");

    SportsdataApi apiInstance = new SportsdataApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
    String competitionId = "competitionId_example"; // String | The competition id to retrieve information for.
    List<String> fields = Arrays.asList(); // List<String> | Specify an absolute field list to return (Comma-Separated List)
    List<String> include = Arrays.asList(); // List<String> | Specify fields in addition to the default to return (Comma-Separated List)
    List<String> exclude = Arrays.asList(); // List<String> | Specify fields from the default to exclude (Comma-Separated List)
    String sort = "id,asc"; // String | The field to order the response by, followed by the order. For example: name,desc
    Integer offset = 0; // Integer | Skip over a number of elements by specifying a start value for the query
    Integer limit = 100; // Integer | Specify the number of results to return
    String culture = "culture_example"; // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    String name = "name_example"; // String | Filter by market group name
    try {
      MarketGroupsWrapper result = apiInstance.getMarketGroupsForCompetition(apiKey, competitionId, fields, include, exclude, sort, offset, limit, culture, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SportsdataApi#getMarketGroupsForCompetition");
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
| **apiKey** | **String**| Your API Key available from your developer portal | |
| **competitionId** | **String**| The competition id to retrieve information for. | |
| **fields** | [**List&lt;String&gt;**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] |
| **exclude** | [**List&lt;String&gt;**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] |
| **sort** | **String**| The field to order the response by, followed by the order. For example: name,desc | [optional] [default to id,asc] |
| **offset** | **Integer**| Skip over a number of elements by specifying a start value for the query | [optional] [default to 0] |
| **limit** | **Integer**| Specify the number of results to return | [optional] [default to 100] |
| **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] |
| **name** | **String**| Filter by market group name | [optional] |

### Return type

[**MarketGroupsWrapper**](MarketGroupsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Incorrect or Missing Parameter |  -  |
| **404** | No data found for request |  -  |

<a id="getMarkets"></a>
# **getMarkets**
> MarketsWrapper getMarkets(apiKey, eventId, ids, includeAllDescendants, fields, include, exclude, includeEmpty, culture, marketPublished, marketStatus, marketDisplayed, marketChannel, marketSort, marketEW, selectionStatus, selectionChannel, selectionPublished)

Gets one or more specific markets

Retrieves one or more specific markets. Markets with Live at the end are always In-Play markets. However, not ALL In-Play markets have Live at the end of the market name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SportsdataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.whapi.com/v2/sportsdata");

    SportsdataApi apiInstance = new SportsdataApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
    String eventId = "eventId_example"; // String | The event ID to retrieve information for.
    List<String> ids = Arrays.asList(); // List<String> | A comma-separated list of selectionIds
    Boolean includeAllDescendants = false; // Boolean | Include every descendant in the below heirarchy
    List<String> fields = Arrays.asList(); // List<String> | Specify an absolute field list to return (Comma-Separated List)
    List<String> include = Arrays.asList(); // List<String> | Specify fields in addition to the default to return (Comma-Separated List)
    List<String> exclude = Arrays.asList(); // List<String> | Specify fields from the default to exclude (Comma-Separated List)
    Boolean includeEmpty = true; // Boolean | When declared as false it should exclude markets and events that have no selections / markets
    String culture = "culture_example"; // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    String marketPublished = "true"; // String | Specify whether only active entities should be returned, according to the William Hill definition of active
    String marketStatus = "marketStatus_example"; // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
    String marketDisplayed = "true"; // String | Specify whether to return displayed entities or not
    String marketChannel = "marketChannel_example"; // String | Specify a channel filter and only results from that channel will be returned
    String marketSort = "marketSort_example"; // String | Filter by market sort (e.g. MR (match result) -- (Outright)).
    String marketEW = "marketEW_example"; // String | Specify whether to return markets with each way betting or those without
    String selectionStatus = "selectionStatus_example"; // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
    String selectionChannel = "selectionChannel_example"; // String | Specify a channel filter and only results from that channel will be returned
    String selectionPublished = "true"; // String | Specify whether only active entities should be returned, according to the William Hill definition of active
    try {
      MarketsWrapper result = apiInstance.getMarkets(apiKey, eventId, ids, includeAllDescendants, fields, include, exclude, includeEmpty, culture, marketPublished, marketStatus, marketDisplayed, marketChannel, marketSort, marketEW, selectionStatus, selectionChannel, selectionPublished);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SportsdataApi#getMarkets");
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
| **apiKey** | **String**| Your API Key available from your developer portal | |
| **eventId** | **String**| The event ID to retrieve information for. | |
| **ids** | [**List&lt;String&gt;**](String.md)| A comma-separated list of selectionIds | [optional] |
| **includeAllDescendants** | **Boolean**| Include every descendant in the below heirarchy | [optional] [default to false] |
| **fields** | [**List&lt;String&gt;**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] |
| **exclude** | [**List&lt;String&gt;**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] |
| **includeEmpty** | **Boolean**| When declared as false it should exclude markets and events that have no selections / markets | [optional] [default to true] |
| **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] |
| **marketPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to true] |
| **marketStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] |
| **marketDisplayed** | **String**| Specify whether to return displayed entities or not | [optional] [default to true] |
| **marketChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] |
| **marketSort** | **String**| Filter by market sort (e.g. MR (match result) -- (Outright)). | [optional] |
| **marketEW** | **String**| Specify whether to return markets with each way betting or those without | [optional] |
| **selectionStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] |
| **selectionChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] |
| **selectionPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to true] |

### Return type

[**MarketsWrapper**](MarketsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Incorrect or Missing Parameter |  -  |
| **404** | No data found for request |  -  |

<a id="getMarketsByGroupId"></a>
# **getMarketsByGroupId**
> MarketGroupsWrapper getMarketsByGroupId(apiKey, competitionId, marketSort, marketGroupId, fields, include, exclude)

Retrieves a list of events/markets/selections where markets within said event match selected sort/groupId

Retrieves a list of events/markets/selections where markets within said event match selected sort/groupId

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SportsdataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.whapi.com/v2/sportsdata");

    SportsdataApi apiInstance = new SportsdataApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
    String competitionId = "competitionId_example"; // String | The competition id to retrieve information for.
    String marketSort = "marketSort_example"; // String | Filter by market sort (e.g. MR (match result) -- (Outright)).
    String marketGroupId = "marketGroupId_example"; // String | Filter by marketGroupId (e.g. OB_MG1276585).
    List<String> fields = Arrays.asList(); // List<String> | Specify an absolute field list to return (Comma-Separated List)
    List<String> include = Arrays.asList(); // List<String> | Specify fields in addition to the default to return (Comma-Separated List)
    List<String> exclude = Arrays.asList(); // List<String> | Specify fields from the default to exclude (Comma-Separated List)
    try {
      MarketGroupsWrapper result = apiInstance.getMarketsByGroupId(apiKey, competitionId, marketSort, marketGroupId, fields, include, exclude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SportsdataApi#getMarketsByGroupId");
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
| **apiKey** | **String**| Your API Key available from your developer portal | |
| **competitionId** | **String**| The competition id to retrieve information for. | |
| **marketSort** | **String**| Filter by market sort (e.g. MR (match result) -- (Outright)). | |
| **marketGroupId** | **String**| Filter by marketGroupId (e.g. OB_MG1276585). | |
| **fields** | [**List&lt;String&gt;**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] |
| **exclude** | [**List&lt;String&gt;**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] |

### Return type

[**MarketGroupsWrapper**](MarketGroupsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Incorrect or Missing Parameter |  -  |
| **404** | No data found for request |  -  |

<a id="getSelections"></a>
# **getSelections**
> SelectionsWrapper getSelections(apiKey, eventId, marketId, ids, fields, include, exclude, culture, selectionStatus, selectionChannel, selectionPublished)

Gets one or more selections for a market

Retrieves one or more selections for a market

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SportsdataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.whapi.com/v2/sportsdata");

    SportsdataApi apiInstance = new SportsdataApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
    String eventId = "eventId_example"; // String | The event ID to retrieve information for.
    String marketId = "marketId_example"; // String | The market id to retrieve information for
    List<String> ids = Arrays.asList(); // List<String> | A comma-separated list of selectionIds
    List<String> fields = Arrays.asList(); // List<String> | Specify an absolute field list to return (Comma-Separated List)
    List<String> include = Arrays.asList(); // List<String> | Specify fields in addition to the default to return (Comma-Separated List)
    List<String> exclude = Arrays.asList(); // List<String> | Specify fields from the default to exclude (Comma-Separated List)
    String culture = "culture_example"; // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    String selectionStatus = "selectionStatus_example"; // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
    String selectionChannel = "selectionChannel_example"; // String | Specify a channel filter and only results from that channel will be returned
    String selectionPublished = "true"; // String | Specify whether only active entities should be returned, according to the William Hill definition of active
    try {
      SelectionsWrapper result = apiInstance.getSelections(apiKey, eventId, marketId, ids, fields, include, exclude, culture, selectionStatus, selectionChannel, selectionPublished);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SportsdataApi#getSelections");
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
| **apiKey** | **String**| Your API Key available from your developer portal | |
| **eventId** | **String**| The event ID to retrieve information for. | |
| **marketId** | **String**| The market id to retrieve information for | |
| **ids** | [**List&lt;String&gt;**](String.md)| A comma-separated list of selectionIds | [optional] |
| **fields** | [**List&lt;String&gt;**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] |
| **exclude** | [**List&lt;String&gt;**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] |
| **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] |
| **selectionStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] |
| **selectionChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] |
| **selectionPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to true] |

### Return type

[**SelectionsWrapper**](SelectionsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Incorrect or Missing Parameter |  -  |
| **404** | No data found for request |  -  |

<a id="getSports"></a>
# **getSports**
> SportsWrapper getSports(apiKey, sort, offset, isPublished, limit, fields, include, exclude, culture)

Gets a list of all sports

Gets a list of all sports

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SportsdataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.whapi.com/v2/sportsdata");

    SportsdataApi apiInstance = new SportsdataApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
    String sort = "id,asc"; // String | The field to order the response by, followed by the order. For example: name,desc
    Integer offset = 0; // Integer | Skip over a number of elements by specifying a start value for the query
    String isPublished = "true"; // String | Specify whether only active entities should be returned, according to the William Hill definition of active
    Integer limit = 100; // Integer | Specify the number of results to return
    List<String> fields = Arrays.asList(); // List<String> | Specify an absolute field list to return (Comma-Separated List)
    List<String> include = Arrays.asList(); // List<String> | Specify fields in addition to the default to return (Comma-Separated List)
    List<String> exclude = Arrays.asList(); // List<String> | Specify fields from the default to exclude (Comma-Separated List)
    String culture = "culture_example"; // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    try {
      SportsWrapper result = apiInstance.getSports(apiKey, sort, offset, isPublished, limit, fields, include, exclude, culture);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SportsdataApi#getSports");
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
| **apiKey** | **String**| Your API Key available from your developer portal | |
| **sort** | **String**| The field to order the response by, followed by the order. For example: name,desc | [optional] [default to id,asc] |
| **offset** | **Integer**| Skip over a number of elements by specifying a start value for the query | [optional] [default to 0] |
| **isPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to true] |
| **limit** | **Integer**| Specify the number of results to return | [optional] [default to 100] |
| **fields** | [**List&lt;String&gt;**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] |
| **exclude** | [**List&lt;String&gt;**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] |
| **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] |

### Return type

[**SportsWrapper**](SportsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Incorrect or Missing Parameter |  -  |
| **404** | No data found for request |  -  |

<a id="getTopBets"></a>
# **getTopBets**
> TopBetsWrapper getTopBets(apiKey, sportIds, competitionIds, limit, fields, include, exclude, paramTopBetEventId, sortName, culture, locale)

Retrieves a weighted list of Selections.

Retrieves a weighted list of Selections.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SportsdataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.whapi.com/v2/sportsdata");

    SportsdataApi apiInstance = new SportsdataApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
    List<String> sportIds = Arrays.asList(); // List<String> | A comma-separated list of sportsIds for which to retrieve topBets for
    List<String> competitionIds = Arrays.asList(); // List<String> | A comma-separated list of competitionIds for which to retrieve topBets for
    Integer limit = 100; // Integer | Specify the number of results to return
    List<String> fields = Arrays.asList(); // List<String> | Specify an absolute field list to return (Comma-Separated List)
    List<String> include = Arrays.asList(); // List<String> | Specify fields in addition to the default to return (Comma-Separated List)
    List<String> exclude = Arrays.asList(); // List<String> | Specify fields from the default to exclude (Comma-Separated List)
    String paramTopBetEventId = "paramTopBetEventId_example"; // String | The event ID to retrieve top bet information for. Multiple events up to 5 may be used
    String sortName = "sortName_example"; // String | The market sort code used to further filter event results. Please note this can only be used with event id(s).
    String culture = "culture_example"; // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    String locale = "locale_example"; // String | Code used to select a set of top bets settings, default is \"whapi\" which allows events set in far future to be included, setting the value to \"en-GB\" will activate english sportsbook settings, mirroring top bets on the website, which restricts events returned to those taking place in next 36 hours. Acceptable values (not all heve their own settings - if none currently available for that locale - en-GB will be used) are de-DE|whapi|en-GB|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    try {
      TopBetsWrapper result = apiInstance.getTopBets(apiKey, sportIds, competitionIds, limit, fields, include, exclude, paramTopBetEventId, sortName, culture, locale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SportsdataApi#getTopBets");
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
| **apiKey** | **String**| Your API Key available from your developer portal | |
| **sportIds** | [**List&lt;String&gt;**](String.md)| A comma-separated list of sportsIds for which to retrieve topBets for | [optional] |
| **competitionIds** | [**List&lt;String&gt;**](String.md)| A comma-separated list of competitionIds for which to retrieve topBets for | [optional] |
| **limit** | **Integer**| Specify the number of results to return | [optional] [default to 100] |
| **fields** | [**List&lt;String&gt;**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] |
| **exclude** | [**List&lt;String&gt;**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] |
| **paramTopBetEventId** | **String**| The event ID to retrieve top bet information for. Multiple events up to 5 may be used | [optional] |
| **sortName** | **String**| The market sort code used to further filter event results. Please note this can only be used with event id(s). | [optional] |
| **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] |
| **locale** | **String**| Code used to select a set of top bets settings, default is \&quot;whapi\&quot; which allows events set in far future to be included, setting the value to \&quot;en-GB\&quot; will activate english sportsbook settings, mirroring top bets on the website, which restricts events returned to those taking place in next 36 hours. Acceptable values (not all heve their own settings - if none currently available for that locale - en-GB will be used) are de-DE|whapi|en-GB|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] |

### Return type

[**TopBetsWrapper**](TopBetsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **500** | Server Error: Something went wrong |  -  |

