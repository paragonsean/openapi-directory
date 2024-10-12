# SportsDataApi.SportsdataApi

All URIs are relative to *https://sandbox.whapi.com/v2/sportsdata*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getClassesForSport**](SportsdataApi.md#getClassesForSport) | **GET** /sports/{sportId}/classes/ | Retrieves a list of classes for a given sport id.
[**getCompetition**](SportsdataApi.md#getCompetition) | **GET** /competitions/{competitionId} | Retrieves a specific competition
[**getCompetitionsForClass**](SportsdataApi.md#getCompetitionsForClass) | **GET** /classes/{classId}/competitions/ | Retrieves a list of competitions for a given class id.
[**getCompetitionsForSport**](SportsdataApi.md#getCompetitionsForSport) | **GET** /sports/{sportId}/competitions/ | Retrieves a list of competitions for a given sport id.
[**getEvent**](SportsdataApi.md#getEvent) | **GET** /events/{eventId} | Retrieves a single event by ID.
[**getEvents**](SportsdataApi.md#getEvents) | **GET** /events/ | Retrieves a list of events for the provided IDs.
[**getEventsForClass**](SportsdataApi.md#getEventsForClass) | **GET** /classes/{classId}/events/ | Retrieves a list of events for a given class id.
[**getEventsForCompetition**](SportsdataApi.md#getEventsForCompetition) | **GET** /competitions/{competitionId}/events/ | Retrieves a list of events for a given competition id.
[**getMarketGroupsForCompetition**](SportsdataApi.md#getMarketGroupsForCompetition) | **GET** /competitions/{competitionId}/marketgroups/ | Retrieves a list of market groups for a given competition id
[**getMarkets**](SportsdataApi.md#getMarkets) | **GET** /events/{eventId}/markets/ | Gets one or more specific markets
[**getMarketsByGroupId**](SportsdataApi.md#getMarketsByGroupId) | **GET** /competitions/{competitionId}/marketsByGroupid | Retrieves a list of events/markets/selections where markets within said event match selected sort/groupId
[**getSelections**](SportsdataApi.md#getSelections) | **GET** /events/{eventId}/markets/{marketId}/selections/ | Gets one or more selections for a market
[**getSports**](SportsdataApi.md#getSports) | **GET** /sports/ | Gets a list of all sports
[**getTopBets**](SportsdataApi.md#getTopBets) | **GET** /topbets/ | Retrieves a weighted list of Selections.



## getClassesForSport

> ClassesWrapper getClassesForSport(apiKey, sportId, opts)

Retrieves a list of classes for a given sport id.

Retrieves a list of classes for a given sport id.

### Example

```javascript
import SportsDataApi from 'sports_data_api';

let apiInstance = new SportsDataApi.SportsdataApi();
let apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
let sportId = "sportId_example"; // String | The sport id to retrieve information for.
let opts = {
  'isPublished': "'true'", // String | Specify whether only active entities should be returned, according to the William Hill definition of active
  'fields': ["null"], // [String] | Specify an absolute field list to return (Comma-Separated List)
  'include': ["null"], // [String] | Specify fields in addition to the default to return (Comma-Separated List)
  'exclude': ["null"], // [String] | Specify fields from the default to exclude (Comma-Separated List)
  'displayed': "'true'", // String | Specify whether to return displayed entities or not
  'channel': "channel_example", // String | Specify a channel filter and only results from that channel will be returned
  'status': "status_example", // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
  'sort': "'id,asc'", // String | The field to order the response by, followed by the order. For example: name,desc
  'offset': 0, // Number | Skip over a number of elements by specifying a start value for the query
  'limit': 100, // Number | Specify the number of results to return
  'culture': "culture_example" // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
};
apiInstance.getClassesForSport(apiKey, sportId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**| Your API Key available from your developer portal | 
 **sportId** | **String**| The sport id to retrieve information for. | 
 **isPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to &#39;true&#39;]
 **fields** | [**[String]**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] 
 **include** | [**[String]**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] 
 **exclude** | [**[String]**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] 
 **displayed** | **String**| Specify whether to return displayed entities or not | [optional] [default to &#39;true&#39;]
 **channel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] 
 **status** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] 
 **sort** | **String**| The field to order the response by, followed by the order. For example: name,desc | [optional] [default to &#39;id,asc&#39;]
 **offset** | **Number**| Skip over a number of elements by specifying a start value for the query | [optional] [default to 0]
 **limit** | **Number**| Specify the number of results to return | [optional] [default to 100]
 **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] 

### Return type

[**ClassesWrapper**](ClassesWrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCompetition

> Competition getCompetition(apiKey, competitionId, opts)

Retrieves a specific competition

Retrieves a specific competition

### Example

```javascript
import SportsDataApi from 'sports_data_api';

let apiInstance = new SportsDataApi.SportsdataApi();
let apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
let competitionId = "competitionId_example"; // String | The competition id to retrieve information for.
let opts = {
  'fields': ["null"], // [String] | Specify an absolute field list to return (Comma-Separated List)
  'include': ["null"], // [String] | Specify fields in addition to the default to return (Comma-Separated List)
  'exclude': ["null"], // [String] | Specify fields from the default to exclude (Comma-Separated List)
  'culture': "culture_example" // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
};
apiInstance.getCompetition(apiKey, competitionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**| Your API Key available from your developer portal | 
 **competitionId** | **String**| The competition id to retrieve information for. | 
 **fields** | [**[String]**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] 
 **include** | [**[String]**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] 
 **exclude** | [**[String]**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] 
 **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] 

### Return type

[**Competition**](Competition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCompetitionsForClass

> CompetitionsWrapper getCompetitionsForClass(apiKey, classId, opts)

Retrieves a list of competitions for a given class id.

Retrieves a list of competitions for a given class id.

### Example

```javascript
import SportsDataApi from 'sports_data_api';

let apiInstance = new SportsDataApi.SportsdataApi();
let apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
let classId = "classId_example"; // String | The class id to retrieve information for.
let opts = {
  'isPublished': "'true'", // String | Specify whether only active entities should be returned, according to the William Hill definition of active
  'fields': ["null"], // [String] | Specify an absolute field list to return (Comma-Separated List)
  'include': ["null"], // [String] | Specify fields in addition to the default to return (Comma-Separated List)
  'exclude': ["null"], // [String] | Specify fields from the default to exclude (Comma-Separated List)
  'displayed': "'true'", // String | Specify whether to return displayed entities or not
  'channel': "channel_example", // String | Specify a channel filter and only results from that channel will be returned
  'status': "status_example", // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
  'sort': "'id,asc'", // String | The field to order the response by, followed by the order. For example: name,desc
  'offset': 0, // Number | Skip over a number of elements by specifying a start value for the query
  'limit': 100, // Number | Specify the number of results to return
  'culture': "culture_example" // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
};
apiInstance.getCompetitionsForClass(apiKey, classId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**| Your API Key available from your developer portal | 
 **classId** | **String**| The class id to retrieve information for. | 
 **isPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to &#39;true&#39;]
 **fields** | [**[String]**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] 
 **include** | [**[String]**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] 
 **exclude** | [**[String]**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] 
 **displayed** | **String**| Specify whether to return displayed entities or not | [optional] [default to &#39;true&#39;]
 **channel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] 
 **status** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] 
 **sort** | **String**| The field to order the response by, followed by the order. For example: name,desc | [optional] [default to &#39;id,asc&#39;]
 **offset** | **Number**| Skip over a number of elements by specifying a start value for the query | [optional] [default to 0]
 **limit** | **Number**| Specify the number of results to return | [optional] [default to 100]
 **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] 

### Return type

[**CompetitionsWrapper**](CompetitionsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCompetitionsForSport

> CompetitionsWrapper getCompetitionsForSport(apiKey, sportId, opts)

Retrieves a list of competitions for a given sport id.

Retrieves a list of competitions for a given sport id.

### Example

```javascript
import SportsDataApi from 'sports_data_api';

let apiInstance = new SportsDataApi.SportsdataApi();
let apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
let sportId = "sportId_example"; // String | The sport id to retrieve information for.
let opts = {
  'isPublished': "'true'", // String | Specify whether only active entities should be returned, according to the William Hill definition of active
  'fields': ["null"], // [String] | Specify an absolute field list to return (Comma-Separated List)
  'include': ["null"], // [String] | Specify fields in addition to the default to return (Comma-Separated List)
  'exclude': ["null"], // [String] | Specify fields from the default to exclude (Comma-Separated List)
  'displayed': "'true'", // String | Specify whether to return displayed entities or not
  'channel': "channel_example", // String | Specify a channel filter and only results from that channel will be returned
  'status': "status_example", // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
  'sort': "'id,asc'", // String | The field to order the response by, followed by the order. For example: name,desc
  'offset': 0, // Number | Skip over a number of elements by specifying a start value for the query
  'limit': 100, // Number | Specify the number of results to return
  'culture': "culture_example" // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
};
apiInstance.getCompetitionsForSport(apiKey, sportId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**| Your API Key available from your developer portal | 
 **sportId** | **String**| The sport id to retrieve information for. | 
 **isPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to &#39;true&#39;]
 **fields** | [**[String]**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] 
 **include** | [**[String]**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] 
 **exclude** | [**[String]**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] 
 **displayed** | **String**| Specify whether to return displayed entities or not | [optional] [default to &#39;true&#39;]
 **channel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] 
 **status** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] 
 **sort** | **String**| The field to order the response by, followed by the order. For example: name,desc | [optional] [default to &#39;id,asc&#39;]
 **offset** | **Number**| Skip over a number of elements by specifying a start value for the query | [optional] [default to 0]
 **limit** | **Number**| Specify the number of results to return | [optional] [default to 100]
 **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] 

### Return type

[**CompetitionsWrapper**](CompetitionsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEvent

> EventsWrapper getEvent(apiKey, eventId, opts)

Retrieves a single event by ID.

Retrieves a single event by ID.

### Example

```javascript
import SportsDataApi from 'sports_data_api';

let apiInstance = new SportsDataApi.SportsdataApi();
let apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
let eventId = "eventId_example"; // String | The event ID to retrieve information for.
let opts = {
  'includeAllDescendants': false, // Boolean | Include every descendant in the below heirarchy
  'fields': ["null"], // [String] | Specify an absolute field list to return (Comma-Separated List)
  'include': ["null"], // [String] | Specify fields in addition to the default to return (Comma-Separated List)
  'exclude': ["null"], // [String] | Specify fields from the default to exclude (Comma-Separated List)
  'headlineSummary': false, // Boolean | Return only headline markets (Markets with the lowest display order) Either 1 InPlay and 1 Pre-Match, or the amount specified in marketCount, if available. Markets and Outcomes will be returned.
  'marketCount': 1, // Number | Specify the number of markets to return when requesting headlineSummary. This count of InPlay and Pre-Match markets will be returned.For example, when specifying 1, 1 In Play and 1 Pre Match market will be returned.
  'marketIds': ["null"], // [String] | Comma-seaerated list of market IDs to filter by
  'includeEmpty': true, // Boolean | When declared as false it should exclude markets and events that have no selections / markets
  'culture': "culture_example", // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
  'marketPublished': "'true'", // String | Specify whether only active entities should be returned, according to the William Hill definition of active
  'marketStatus': "marketStatus_example", // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
  'marketDisplayed': "'true'", // String | Specify whether to return displayed entities or not
  'marketChannel': "marketChannel_example", // String | Specify a channel filter and only results from that channel will be returned
  'marketSort': "marketSort_example", // String | Filter by market sort (e.g. MR (match result) -- (Outright)).
  'marketEW': "marketEW_example", // String | Specify whether to return markets with each way betting or those without
  'selectionStatus': "selectionStatus_example", // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
  'selectionChannel': "selectionChannel_example", // String | Specify a channel filter and only results from that channel will be returned
  'selectionPublished': "'true'" // String | Specify whether only active entities should be returned, according to the William Hill definition of active
};
apiInstance.getEvent(apiKey, eventId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**| Your API Key available from your developer portal | 
 **eventId** | **String**| The event ID to retrieve information for. | 
 **includeAllDescendants** | **Boolean**| Include every descendant in the below heirarchy | [optional] [default to false]
 **fields** | [**[String]**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] 
 **include** | [**[String]**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] 
 **exclude** | [**[String]**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] 
 **headlineSummary** | **Boolean**| Return only headline markets (Markets with the lowest display order) Either 1 InPlay and 1 Pre-Match, or the amount specified in marketCount, if available. Markets and Outcomes will be returned. | [optional] [default to false]
 **marketCount** | **Number**| Specify the number of markets to return when requesting headlineSummary. This count of InPlay and Pre-Match markets will be returned.For example, when specifying 1, 1 In Play and 1 Pre Match market will be returned. | [optional] [default to 1]
 **marketIds** | [**[String]**](String.md)| Comma-seaerated list of market IDs to filter by | [optional] 
 **includeEmpty** | **Boolean**| When declared as false it should exclude markets and events that have no selections / markets | [optional] [default to true]
 **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] 
 **marketPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to &#39;true&#39;]
 **marketStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] 
 **marketDisplayed** | **String**| Specify whether to return displayed entities or not | [optional] [default to &#39;true&#39;]
 **marketChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] 
 **marketSort** | **String**| Filter by market sort (e.g. MR (match result) -- (Outright)). | [optional] 
 **marketEW** | **String**| Specify whether to return markets with each way betting or those without | [optional] 
 **selectionStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] 
 **selectionChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] 
 **selectionPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to &#39;true&#39;]

### Return type

[**EventsWrapper**](EventsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEvents

> EventsWrapper getEvents(apiKey, opts)

Retrieves a list of events for the provided IDs.

Retrieves a list of events for the provided IDs.

### Example

```javascript
import SportsDataApi from 'sports_data_api';

let apiInstance = new SportsDataApi.SportsdataApi();
let apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
let opts = {
  'ids': ["null"], // [String] | A comma-separated list of selectionIds
  'isPublished': "'true'", // String | Specify whether only active entities should be returned, according to the William Hill definition of active
  'includeAllDescendants': false, // Boolean | Include every descendant in the below heirarchy
  'fields': ["null"], // [String] | Specify an absolute field list to return (Comma-Separated List)
  'include': ["null"], // [String] | Specify fields in addition to the default to return (Comma-Separated List)
  'exclude': ["null"], // [String] | Specify fields from the default to exclude (Comma-Separated List)
  'channel': "channel_example", // String | Specify a channel filter and only results from that channel will be returned
  'settled': true, // Boolean | Specify wether only settled entities should be returned
  'includeEmpty': true, // Boolean | When declared as false it should exclude markets and events that have no selections / markets
  'headlineSummary': false, // Boolean | Return only headline markets (Markets with the lowest display order) Either 1 InPlay and 1 Pre-Match, or the amount specified in marketCount, if available. Markets and Outcomes will be returned.
  'marketCount': 1, // Number | Specify the number of markets to return when requesting headlineSummary. This count of InPlay and Pre-Match markets will be returned.For example, when specifying 1, 1 In Play and 1 Pre Match market will be returned.
  'sort': "'id,asc'", // String | The field to order the response by, followed by the order. For example: name,desc
  'offset': 0, // Number | Skip over a number of elements by specifying a start value for the query
  'limit': 100, // Number | Specify the number of results to return
  'marketIds': ["null"], // [String] | Comma-seaerated list of market IDs to filter by
  'culture': "culture_example", // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
  'marketPublished': "'true'", // String | Specify whether only active entities should be returned, according to the William Hill definition of active
  'marketStatus': "marketStatus_example", // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
  'marketDisplayed': "'true'", // String | Specify whether to return displayed entities or not
  'marketChannel': "marketChannel_example", // String | Specify a channel filter and only results from that channel will be returned
  'marketSort': "marketSort_example", // String | Filter by market sort (e.g. MR (match result) -- (Outright)).
  'marketEW': "marketEW_example", // String | Specify whether to return markets with each way betting or those without
  'selectionStatus': "selectionStatus_example", // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
  'selectionChannel': "selectionChannel_example", // String | Specify a channel filter and only results from that channel will be returned
  'selectionPublished': "'true'" // String | Specify whether only active entities should be returned, according to the William Hill definition of active
};
apiInstance.getEvents(apiKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**| Your API Key available from your developer portal | 
 **ids** | [**[String]**](String.md)| A comma-separated list of selectionIds | [optional] 
 **isPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to &#39;true&#39;]
 **includeAllDescendants** | **Boolean**| Include every descendant in the below heirarchy | [optional] [default to false]
 **fields** | [**[String]**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] 
 **include** | [**[String]**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] 
 **exclude** | [**[String]**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] 
 **channel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] 
 **settled** | **Boolean**| Specify wether only settled entities should be returned | [optional] 
 **includeEmpty** | **Boolean**| When declared as false it should exclude markets and events that have no selections / markets | [optional] [default to true]
 **headlineSummary** | **Boolean**| Return only headline markets (Markets with the lowest display order) Either 1 InPlay and 1 Pre-Match, or the amount specified in marketCount, if available. Markets and Outcomes will be returned. | [optional] [default to false]
 **marketCount** | **Number**| Specify the number of markets to return when requesting headlineSummary. This count of InPlay and Pre-Match markets will be returned.For example, when specifying 1, 1 In Play and 1 Pre Match market will be returned. | [optional] [default to 1]
 **sort** | **String**| The field to order the response by, followed by the order. For example: name,desc | [optional] [default to &#39;id,asc&#39;]
 **offset** | **Number**| Skip over a number of elements by specifying a start value for the query | [optional] [default to 0]
 **limit** | **Number**| Specify the number of results to return | [optional] [default to 100]
 **marketIds** | [**[String]**](String.md)| Comma-seaerated list of market IDs to filter by | [optional] 
 **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] 
 **marketPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to &#39;true&#39;]
 **marketStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] 
 **marketDisplayed** | **String**| Specify whether to return displayed entities or not | [optional] [default to &#39;true&#39;]
 **marketChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] 
 **marketSort** | **String**| Filter by market sort (e.g. MR (match result) -- (Outright)). | [optional] 
 **marketEW** | **String**| Specify whether to return markets with each way betting or those without | [optional] 
 **selectionStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] 
 **selectionChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] 
 **selectionPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to &#39;true&#39;]

### Return type

[**EventsWrapper**](EventsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventsForClass

> EventsWrapper getEventsForClass(apiKey, classId, opts)

Retrieves a list of events for a given class id.

Retrieves a list of events for a given class id. &#39;includeAllDescendants&#39; parameter should be accompanied with &#39;date&#39; filter or one of &#39;dateFrom&#39; and &#39;dateTo&#39; filters.

### Example

```javascript
import SportsDataApi from 'sports_data_api';

let apiInstance = new SportsDataApi.SportsdataApi();
let apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
let classId = "classId_example"; // String | The class id to retrieve information for.
let opts = {
  'isPublished': "'true'", // String | Specify whether only active entities should be returned, according to the William Hill definition of active
  'fields': ["null"], // [String] | Specify an absolute field list to return (Comma-Separated List)
  'include': ["null"], // [String] | Specify fields in addition to the default to return (Comma-Separated List)
  'exclude': ["null"], // [String] | Specify fields from the default to exclude (Comma-Separated List)
  'displayed': "'true'", // String | Specify whether to return displayed entities or not
  'channel': "channel_example", // String | Specify a channel filter and only results from that channel will be returned
  'settled': true, // Boolean | Specify wether only settled entities should be returned
  'includeEmpty': true, // Boolean | When declared as false it should exclude markets and events that have no selections / markets
  'status': "status_example", // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
  'sort': "'id,asc'", // String | The field to order the response by, followed by the order. For example: name,desc
  'offset': 0, // Number | Skip over a number of elements by specifying a start value for the query
  'limit': 100, // Number | Specify the number of results to return
  'headlineSummary': false, // Boolean | Return only headline markets (Markets with the lowest display order) Either 1 InPlay and 1 Pre-Match, or the amount specified in marketCount, if available. Markets and Outcomes will be returned.
  'includeAllDescendants': false, // Boolean | Include every descendant in the below heirarchy
  'isInPlay': true, // Boolean | Show only events that are in-play
  'marketCount': 1, // Number | Specify the number of markets to return when requesting headlineSummary. This count of InPlay and Pre-Match markets will be returned.For example, when specifying 1, 1 In Play and 1 Pre Match market will be returned.
  'date': "date_example", // String | Return only events for the specified date (yyyy-MM-dd).
  'dateFrom': "dateFrom_example", // String | The UTC datetime from the events to be returned. (yyyy-MM-ddTHH:mm:ss)
  'dateTo': "dateTo_example", // String | The UTC datetime TO the events to be returned. (yyyy-MM-ddTHH:mm:ss)
  'eventSort': "eventSort_example", // String | Filter event by event sort
  'culture': "culture_example", // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
  'marketPublished': "'true'", // String | Specify whether only active entities should be returned, according to the William Hill definition of active
  'marketStatus': "marketStatus_example", // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
  'marketDisplayed': "'true'", // String | Specify whether to return displayed entities or not
  'marketChannel': "marketChannel_example", // String | Specify a channel filter and only results from that channel will be returned
  'marketSort': "marketSort_example", // String | Filter by market sort (e.g. MR (match result) -- (Outright)).
  'marketEW': "marketEW_example", // String | Specify whether to return markets with each way betting or those without
  'selectionStatus': "selectionStatus_example", // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
  'selectionChannel': "selectionChannel_example", // String | Specify a channel filter and only results from that channel will be returned
  'selectionPublished': "'true'" // String | Specify whether only active entities should be returned, according to the William Hill definition of active
};
apiInstance.getEventsForClass(apiKey, classId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**| Your API Key available from your developer portal | 
 **classId** | **String**| The class id to retrieve information for. | 
 **isPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to &#39;true&#39;]
 **fields** | [**[String]**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] 
 **include** | [**[String]**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] 
 **exclude** | [**[String]**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] 
 **displayed** | **String**| Specify whether to return displayed entities or not | [optional] [default to &#39;true&#39;]
 **channel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] 
 **settled** | **Boolean**| Specify wether only settled entities should be returned | [optional] 
 **includeEmpty** | **Boolean**| When declared as false it should exclude markets and events that have no selections / markets | [optional] [default to true]
 **status** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] 
 **sort** | **String**| The field to order the response by, followed by the order. For example: name,desc | [optional] [default to &#39;id,asc&#39;]
 **offset** | **Number**| Skip over a number of elements by specifying a start value for the query | [optional] [default to 0]
 **limit** | **Number**| Specify the number of results to return | [optional] [default to 100]
 **headlineSummary** | **Boolean**| Return only headline markets (Markets with the lowest display order) Either 1 InPlay and 1 Pre-Match, or the amount specified in marketCount, if available. Markets and Outcomes will be returned. | [optional] [default to false]
 **includeAllDescendants** | **Boolean**| Include every descendant in the below heirarchy | [optional] [default to false]
 **isInPlay** | **Boolean**| Show only events that are in-play | [optional] 
 **marketCount** | **Number**| Specify the number of markets to return when requesting headlineSummary. This count of InPlay and Pre-Match markets will be returned.For example, when specifying 1, 1 In Play and 1 Pre Match market will be returned. | [optional] [default to 1]
 **date** | **String**| Return only events for the specified date (yyyy-MM-dd). | [optional] 
 **dateFrom** | **String**| The UTC datetime from the events to be returned. (yyyy-MM-ddTHH:mm:ss) | [optional] 
 **dateTo** | **String**| The UTC datetime TO the events to be returned. (yyyy-MM-ddTHH:mm:ss) | [optional] 
 **eventSort** | **String**| Filter event by event sort | [optional] 
 **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] 
 **marketPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to &#39;true&#39;]
 **marketStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] 
 **marketDisplayed** | **String**| Specify whether to return displayed entities or not | [optional] [default to &#39;true&#39;]
 **marketChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] 
 **marketSort** | **String**| Filter by market sort (e.g. MR (match result) -- (Outright)). | [optional] 
 **marketEW** | **String**| Specify whether to return markets with each way betting or those without | [optional] 
 **selectionStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] 
 **selectionChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] 
 **selectionPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to &#39;true&#39;]

### Return type

[**EventsWrapper**](EventsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventsForCompetition

> EventsWrapper getEventsForCompetition(apiKey, competitionId, opts)

Retrieves a list of events for a given competition id.

Retrieves a list of events for a given competition id. &#39;headlineSummary&#39; and includeAllDescendants parameters should be accompanied with &#39;date&#39; filter or one of &#39;dateFrom&#39; and &#39;dateTo&#39; filters.

### Example

```javascript
import SportsDataApi from 'sports_data_api';

let apiInstance = new SportsDataApi.SportsdataApi();
let apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
let competitionId = "competitionId_example"; // String | The competition id to retrieve information for.
let opts = {
  'isPublished': "'true'", // String | Specify whether only active entities should be returned, according to the William Hill definition of active
  'fields': ["null"], // [String] | Specify an absolute field list to return (Comma-Separated List)
  'include': ["null"], // [String] | Specify fields in addition to the default to return (Comma-Separated List)
  'exclude': ["null"], // [String] | Specify fields from the default to exclude (Comma-Separated List)
  'displayed': "'true'", // String | Specify whether to return displayed entities or not
  'channel': "channel_example", // String | Specify a channel filter and only results from that channel will be returned
  'settled': true, // Boolean | Specify wether only settled entities should be returned
  'includeEmpty': true, // Boolean | When declared as false it should exclude markets and events that have no selections / markets
  'status': "status_example", // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
  'sort': "'id,asc'", // String | The field to order the response by, followed by the order. For example: name,desc
  'offset': 0, // Number | Skip over a number of elements by specifying a start value for the query
  'limit': 100, // Number | Specify the number of results to return
  'headlineSummary': false, // Boolean | Return only headline markets (Markets with the lowest display order) Either 1 InPlay and 1 Pre-Match, or the amount specified in marketCount, if available. Markets and Outcomes will be returned.
  'includeAllDescendants': false, // Boolean | Include every descendant in the below heirarchy
  'isInPlay': true, // Boolean | Show only events that are in-play
  'marketCount': 1, // Number | Specify the number of markets to return when requesting headlineSummary. This count of InPlay and Pre-Match markets will be returned.For example, when specifying 1, 1 In Play and 1 Pre Match market will be returned.
  'date': "date_example", // String | Return only events for the specified date (yyyy-MM-dd).
  'dateFrom': "dateFrom_example", // String | The UTC datetime from the events to be returned. (yyyy-MM-ddTHH:mm:ss)
  'dateTo': "dateTo_example", // String | The UTC datetime TO the events to be returned. (yyyy-MM-ddTHH:mm:ss)
  'marketGroupId': "marketGroupId_example", // String | Filter by marketGroupId (e.g. OB_MG1276585).
  'eventSort': "eventSort_example", // String | Filter event by event sort
  'culture': "culture_example", // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
  'marketPublished': "'true'", // String | Specify whether only active entities should be returned, according to the William Hill definition of active
  'marketStatus': "marketStatus_example", // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
  'marketDisplayed': "'true'", // String | Specify whether to return displayed entities or not
  'marketChannel': "marketChannel_example", // String | Specify a channel filter and only results from that channel will be returned
  'marketSort': "marketSort_example", // String | Filter by market sort (e.g. MR (match result) -- (Outright)).
  'marketEW': "marketEW_example", // String | Specify whether to return markets with each way betting or those without
  'selectionStatus': "selectionStatus_example", // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
  'selectionChannel': "selectionChannel_example", // String | Specify a channel filter and only results from that channel will be returned
  'selectionPublished': "'true'" // String | Specify whether only active entities should be returned, according to the William Hill definition of active
};
apiInstance.getEventsForCompetition(apiKey, competitionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**| Your API Key available from your developer portal | 
 **competitionId** | **String**| The competition id to retrieve information for. | 
 **isPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to &#39;true&#39;]
 **fields** | [**[String]**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] 
 **include** | [**[String]**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] 
 **exclude** | [**[String]**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] 
 **displayed** | **String**| Specify whether to return displayed entities or not | [optional] [default to &#39;true&#39;]
 **channel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] 
 **settled** | **Boolean**| Specify wether only settled entities should be returned | [optional] 
 **includeEmpty** | **Boolean**| When declared as false it should exclude markets and events that have no selections / markets | [optional] [default to true]
 **status** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] 
 **sort** | **String**| The field to order the response by, followed by the order. For example: name,desc | [optional] [default to &#39;id,asc&#39;]
 **offset** | **Number**| Skip over a number of elements by specifying a start value for the query | [optional] [default to 0]
 **limit** | **Number**| Specify the number of results to return | [optional] [default to 100]
 **headlineSummary** | **Boolean**| Return only headline markets (Markets with the lowest display order) Either 1 InPlay and 1 Pre-Match, or the amount specified in marketCount, if available. Markets and Outcomes will be returned. | [optional] [default to false]
 **includeAllDescendants** | **Boolean**| Include every descendant in the below heirarchy | [optional] [default to false]
 **isInPlay** | **Boolean**| Show only events that are in-play | [optional] 
 **marketCount** | **Number**| Specify the number of markets to return when requesting headlineSummary. This count of InPlay and Pre-Match markets will be returned.For example, when specifying 1, 1 In Play and 1 Pre Match market will be returned. | [optional] [default to 1]
 **date** | **String**| Return only events for the specified date (yyyy-MM-dd). | [optional] 
 **dateFrom** | **String**| The UTC datetime from the events to be returned. (yyyy-MM-ddTHH:mm:ss) | [optional] 
 **dateTo** | **String**| The UTC datetime TO the events to be returned. (yyyy-MM-ddTHH:mm:ss) | [optional] 
 **marketGroupId** | **String**| Filter by marketGroupId (e.g. OB_MG1276585). | [optional] 
 **eventSort** | **String**| Filter event by event sort | [optional] 
 **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] 
 **marketPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to &#39;true&#39;]
 **marketStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] 
 **marketDisplayed** | **String**| Specify whether to return displayed entities or not | [optional] [default to &#39;true&#39;]
 **marketChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] 
 **marketSort** | **String**| Filter by market sort (e.g. MR (match result) -- (Outright)). | [optional] 
 **marketEW** | **String**| Specify whether to return markets with each way betting or those without | [optional] 
 **selectionStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] 
 **selectionChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] 
 **selectionPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to &#39;true&#39;]

### Return type

[**EventsWrapper**](EventsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMarketGroupsForCompetition

> MarketGroupsWrapper getMarketGroupsForCompetition(apiKey, competitionId, opts)

Retrieves a list of market groups for a given competition id

Retrieves a list of market groups for a given competition id

### Example

```javascript
import SportsDataApi from 'sports_data_api';

let apiInstance = new SportsDataApi.SportsdataApi();
let apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
let competitionId = "competitionId_example"; // String | The competition id to retrieve information for.
let opts = {
  'fields': ["null"], // [String] | Specify an absolute field list to return (Comma-Separated List)
  'include': ["null"], // [String] | Specify fields in addition to the default to return (Comma-Separated List)
  'exclude': ["null"], // [String] | Specify fields from the default to exclude (Comma-Separated List)
  'sort': "'id,asc'", // String | The field to order the response by, followed by the order. For example: name,desc
  'offset': 0, // Number | Skip over a number of elements by specifying a start value for the query
  'limit': 100, // Number | Specify the number of results to return
  'culture': "culture_example", // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
  'name': "name_example" // String | Filter by market group name
};
apiInstance.getMarketGroupsForCompetition(apiKey, competitionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**| Your API Key available from your developer portal | 
 **competitionId** | **String**| The competition id to retrieve information for. | 
 **fields** | [**[String]**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] 
 **include** | [**[String]**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] 
 **exclude** | [**[String]**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] 
 **sort** | **String**| The field to order the response by, followed by the order. For example: name,desc | [optional] [default to &#39;id,asc&#39;]
 **offset** | **Number**| Skip over a number of elements by specifying a start value for the query | [optional] [default to 0]
 **limit** | **Number**| Specify the number of results to return | [optional] [default to 100]
 **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] 
 **name** | **String**| Filter by market group name | [optional] 

### Return type

[**MarketGroupsWrapper**](MarketGroupsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMarkets

> MarketsWrapper getMarkets(apiKey, eventId, opts)

Gets one or more specific markets

Retrieves one or more specific markets. Markets with Live at the end are always In-Play markets. However, not ALL In-Play markets have Live at the end of the market name.

### Example

```javascript
import SportsDataApi from 'sports_data_api';

let apiInstance = new SportsDataApi.SportsdataApi();
let apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
let eventId = "eventId_example"; // String | The event ID to retrieve information for.
let opts = {
  'ids': ["null"], // [String] | A comma-separated list of selectionIds
  'includeAllDescendants': false, // Boolean | Include every descendant in the below heirarchy
  'fields': ["null"], // [String] | Specify an absolute field list to return (Comma-Separated List)
  'include': ["null"], // [String] | Specify fields in addition to the default to return (Comma-Separated List)
  'exclude': ["null"], // [String] | Specify fields from the default to exclude (Comma-Separated List)
  'includeEmpty': true, // Boolean | When declared as false it should exclude markets and events that have no selections / markets
  'culture': "culture_example", // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
  'marketPublished': "'true'", // String | Specify whether only active entities should be returned, according to the William Hill definition of active
  'marketStatus': "marketStatus_example", // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
  'marketDisplayed': "'true'", // String | Specify whether to return displayed entities or not
  'marketChannel': "marketChannel_example", // String | Specify a channel filter and only results from that channel will be returned
  'marketSort': "marketSort_example", // String | Filter by market sort (e.g. MR (match result) -- (Outright)).
  'marketEW': "marketEW_example", // String | Specify whether to return markets with each way betting or those without
  'selectionStatus': "selectionStatus_example", // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
  'selectionChannel': "selectionChannel_example", // String | Specify a channel filter and only results from that channel will be returned
  'selectionPublished': "'true'" // String | Specify whether only active entities should be returned, according to the William Hill definition of active
};
apiInstance.getMarkets(apiKey, eventId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**| Your API Key available from your developer portal | 
 **eventId** | **String**| The event ID to retrieve information for. | 
 **ids** | [**[String]**](String.md)| A comma-separated list of selectionIds | [optional] 
 **includeAllDescendants** | **Boolean**| Include every descendant in the below heirarchy | [optional] [default to false]
 **fields** | [**[String]**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] 
 **include** | [**[String]**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] 
 **exclude** | [**[String]**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] 
 **includeEmpty** | **Boolean**| When declared as false it should exclude markets and events that have no selections / markets | [optional] [default to true]
 **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] 
 **marketPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to &#39;true&#39;]
 **marketStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] 
 **marketDisplayed** | **String**| Specify whether to return displayed entities or not | [optional] [default to &#39;true&#39;]
 **marketChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] 
 **marketSort** | **String**| Filter by market sort (e.g. MR (match result) -- (Outright)). | [optional] 
 **marketEW** | **String**| Specify whether to return markets with each way betting or those without | [optional] 
 **selectionStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] 
 **selectionChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] 
 **selectionPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to &#39;true&#39;]

### Return type

[**MarketsWrapper**](MarketsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMarketsByGroupId

> MarketGroupsWrapper getMarketsByGroupId(apiKey, competitionId, marketSort, marketGroupId, opts)

Retrieves a list of events/markets/selections where markets within said event match selected sort/groupId

Retrieves a list of events/markets/selections where markets within said event match selected sort/groupId

### Example

```javascript
import SportsDataApi from 'sports_data_api';

let apiInstance = new SportsDataApi.SportsdataApi();
let apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
let competitionId = "competitionId_example"; // String | The competition id to retrieve information for.
let marketSort = "marketSort_example"; // String | Filter by market sort (e.g. MR (match result) -- (Outright)).
let marketGroupId = "marketGroupId_example"; // String | Filter by marketGroupId (e.g. OB_MG1276585).
let opts = {
  'fields': ["null"], // [String] | Specify an absolute field list to return (Comma-Separated List)
  'include': ["null"], // [String] | Specify fields in addition to the default to return (Comma-Separated List)
  'exclude': ["null"] // [String] | Specify fields from the default to exclude (Comma-Separated List)
};
apiInstance.getMarketsByGroupId(apiKey, competitionId, marketSort, marketGroupId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**| Your API Key available from your developer portal | 
 **competitionId** | **String**| The competition id to retrieve information for. | 
 **marketSort** | **String**| Filter by market sort (e.g. MR (match result) -- (Outright)). | 
 **marketGroupId** | **String**| Filter by marketGroupId (e.g. OB_MG1276585). | 
 **fields** | [**[String]**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] 
 **include** | [**[String]**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] 
 **exclude** | [**[String]**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] 

### Return type

[**MarketGroupsWrapper**](MarketGroupsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSelections

> SelectionsWrapper getSelections(apiKey, eventId, marketId, opts)

Gets one or more selections for a market

Retrieves one or more selections for a market

### Example

```javascript
import SportsDataApi from 'sports_data_api';

let apiInstance = new SportsDataApi.SportsdataApi();
let apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
let eventId = "eventId_example"; // String | The event ID to retrieve information for.
let marketId = "marketId_example"; // String | The market id to retrieve information for
let opts = {
  'ids': ["null"], // [String] | A comma-separated list of selectionIds
  'fields': ["null"], // [String] | Specify an absolute field list to return (Comma-Separated List)
  'include': ["null"], // [String] | Specify fields in addition to the default to return (Comma-Separated List)
  'exclude': ["null"], // [String] | Specify fields from the default to exclude (Comma-Separated List)
  'culture': "culture_example", // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
  'selectionStatus': "selectionStatus_example", // String | Specify a status to filter results by. This is currently A (active) or S (suspended)
  'selectionChannel': "selectionChannel_example", // String | Specify a channel filter and only results from that channel will be returned
  'selectionPublished': "'true'" // String | Specify whether only active entities should be returned, according to the William Hill definition of active
};
apiInstance.getSelections(apiKey, eventId, marketId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**| Your API Key available from your developer portal | 
 **eventId** | **String**| The event ID to retrieve information for. | 
 **marketId** | **String**| The market id to retrieve information for | 
 **ids** | [**[String]**](String.md)| A comma-separated list of selectionIds | [optional] 
 **fields** | [**[String]**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] 
 **include** | [**[String]**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] 
 **exclude** | [**[String]**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] 
 **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] 
 **selectionStatus** | **String**| Specify a status to filter results by. This is currently A (active) or S (suspended) | [optional] 
 **selectionChannel** | **String**| Specify a channel filter and only results from that channel will be returned | [optional] 
 **selectionPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to &#39;true&#39;]

### Return type

[**SelectionsWrapper**](SelectionsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSports

> SportsWrapper getSports(apiKey, opts)

Gets a list of all sports

Gets a list of all sports

### Example

```javascript
import SportsDataApi from 'sports_data_api';

let apiInstance = new SportsDataApi.SportsdataApi();
let apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
let opts = {
  'sort': "'id,asc'", // String | The field to order the response by, followed by the order. For example: name,desc
  'offset': 0, // Number | Skip over a number of elements by specifying a start value for the query
  'isPublished': "'true'", // String | Specify whether only active entities should be returned, according to the William Hill definition of active
  'limit': 100, // Number | Specify the number of results to return
  'fields': ["null"], // [String] | Specify an absolute field list to return (Comma-Separated List)
  'include': ["null"], // [String] | Specify fields in addition to the default to return (Comma-Separated List)
  'exclude': ["null"], // [String] | Specify fields from the default to exclude (Comma-Separated List)
  'culture': "culture_example" // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
};
apiInstance.getSports(apiKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**| Your API Key available from your developer portal | 
 **sort** | **String**| The field to order the response by, followed by the order. For example: name,desc | [optional] [default to &#39;id,asc&#39;]
 **offset** | **Number**| Skip over a number of elements by specifying a start value for the query | [optional] [default to 0]
 **isPublished** | **String**| Specify whether only active entities should be returned, according to the William Hill definition of active | [optional] [default to &#39;true&#39;]
 **limit** | **Number**| Specify the number of results to return | [optional] [default to 100]
 **fields** | [**[String]**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] 
 **include** | [**[String]**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] 
 **exclude** | [**[String]**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] 
 **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] 

### Return type

[**SportsWrapper**](SportsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTopBets

> TopBetsWrapper getTopBets(apiKey, opts)

Retrieves a weighted list of Selections.

Retrieves a weighted list of Selections.

### Example

```javascript
import SportsDataApi from 'sports_data_api';

let apiInstance = new SportsDataApi.SportsdataApi();
let apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
let opts = {
  'sportIds': ["null"], // [String] | A comma-separated list of sportsIds for which to retrieve topBets for
  'competitionIds': ["null"], // [String] | A comma-separated list of competitionIds for which to retrieve topBets for
  'limit': 100, // Number | Specify the number of results to return
  'fields': ["null"], // [String] | Specify an absolute field list to return (Comma-Separated List)
  'include': ["null"], // [String] | Specify fields in addition to the default to return (Comma-Separated List)
  'exclude': ["null"], // [String] | Specify fields from the default to exclude (Comma-Separated List)
  'paramTopBetEventId': "paramTopBetEventId_example", // String | The event ID to retrieve top bet information for. Multiple events up to 5 may be used
  'sortName': "sortName_example", // String | The market sort code used to further filter event results. Please note this can only be used with event id(s).
  'culture': "culture_example", // String | Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
  'locale': "locale_example" // String | Code used to select a set of top bets settings, default is \"whapi\" which allows events set in far future to be included, setting the value to \"en-GB\" will activate english sportsbook settings, mirroring top bets on the website, which restricts events returned to those taking place in next 36 hours. Acceptable values (not all heve their own settings - if none currently available for that locale - en-GB will be used) are de-DE|whapi|en-GB|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el=GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
};
apiInstance.getTopBets(apiKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**| Your API Key available from your developer portal | 
 **sportIds** | [**[String]**](String.md)| A comma-separated list of sportsIds for which to retrieve topBets for | [optional] 
 **competitionIds** | [**[String]**](String.md)| A comma-separated list of competitionIds for which to retrieve topBets for | [optional] 
 **limit** | **Number**| Specify the number of results to return | [optional] [default to 100]
 **fields** | [**[String]**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] 
 **include** | [**[String]**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] 
 **exclude** | [**[String]**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] 
 **paramTopBetEventId** | **String**| The event ID to retrieve top bet information for. Multiple events up to 5 may be used | [optional] 
 **sortName** | **String**| The market sort code used to further filter event results. Please note this can only be used with event id(s). | [optional] 
 **culture** | **String**| Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] 
 **locale** | **String**| Code used to select a set of top bets settings, default is \&quot;whapi\&quot; which allows events set in far future to be included, setting the value to \&quot;en-GB\&quot; will activate english sportsbook settings, mirroring top bets on the website, which restricts events returned to those taking place in next 36 hours. Acceptable values (not all heve their own settings - if none currently available for that locale - en-GB will be used) are de-DE|whapi|en-GB|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR | [optional] 

### Return type

[**TopBetsWrapper**](TopBetsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

