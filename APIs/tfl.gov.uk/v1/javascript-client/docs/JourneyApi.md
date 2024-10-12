# TransportForLondonUnifiedApi.JourneyApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**journeyJourneyResults**](JourneyApi.md#journeyJourneyResults) | **GET** /Journey/JourneyResults/{from}/to/{to} | Perform a Journey Planner search from the parameters specified in simple types
[**journeyMeta**](JourneyApi.md#journeyMeta) | **GET** /Journey/Meta/Modes | Gets a list of all of the available journey planner modes



## journeyJourneyResults

> TflApiPresentationEntitiesJourneyPlannerItineraryResult journeyJourneyResults(from, to, opts)

Perform a Journey Planner search from the parameters specified in simple types

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.JourneyApi();
let from = "from_example"; // String | Origin of the journey. Can be WGS84 coordinates expressed as \"lat,long\", a UK postcode, a Naptan (StopPoint) id, an ICS StopId, or a free-text string (will cause disambiguation unless it exactly matches a point of interest name).
let to = "to_example"; // String | Destination of the journey. Can be WGS84 coordinates expressed as \"lat,long\", a UK postcode, a Naptan (StopPoint) id, an ICS StopId, or a free-text string (will cause disambiguation unless it exactly matches a point of interest name).
let opts = {
  'via': "via_example", // String | Travel through point on the journey. Can be WGS84 coordinates expressed as \"lat,long\", a UK postcode, a Naptan (StopPoint) id, an ICS StopId, or a free-text string (will cause disambiguation unless it exactly matches a point of interest name).
  'nationalSearch': true, // Boolean | Does the journey cover stops outside London? eg. \"nationalSearch=true\"
  'date': "date_example", // String | The date must be in yyyyMMdd format
  'time': "time_example", // String | The time must be in HHmm format
  'timeIs': "timeIs_example", // String | Does the time given relate to arrival or leaving time? Possible options: \"departing\" | \"arriving\"
  'journeyPreference': "journeyPreference_example", // String | The journey preference eg possible options: \"leastinterchange\" | \"leasttime\" | \"leastwalking\"
  'mode': ["null"], // [String] | The mode must be a comma separated list of modes. eg possible options: \"public-bus,overground,train,tube,coach,dlr,cablecar,tram,river,walking,cycle\"
  'accessibilityPreference': ["null"], // [String] | The accessibility preference must be a comma separated list eg. \"noSolidStairs,noEscalators,noElevators,stepFreeToVehicle,stepFreeToPlatform\"
  'fromName': "fromName_example", // String | An optional name to associate with the origin of the journey in the results.
  'toName': "toName_example", // String | An optional name to associate with the destination of the journey in the results.
  'viaName': "viaName_example", // String | An optional name to associate with the via point of the journey in the results.
  'maxTransferMinutes': "maxTransferMinutes_example", // String | The max walking time in minutes for transfer eg. \"120\"
  'maxWalkingMinutes': "maxWalkingMinutes_example", // String | The max walking time in minutes for journeys eg. \"120\"
  'walkingSpeed': "walkingSpeed_example", // String | The walking speed. eg possible options: \"slow\" | \"average\" | \"fast\".
  'cyclePreference': "cyclePreference_example", // String | The cycle preference. eg possible options: \"allTheWay\" | \"leaveAtStation\" | \"takeOnTransport\" | \"cycleHire\"
  'adjustment': "adjustment_example", // String | Time adjustment command. eg possible options: \"TripFirst\" | \"TripLast\"
  'bikeProficiency': ["null"], // [String] | A comma separated list of cycling proficiency levels. eg possible options: \"easy,moderate,fast\"
  'alternativeCycle': true, // Boolean | Option to determine whether to return alternative cycling journey
  'alternativeWalking': true, // Boolean | Option to determine whether to return alternative walking journey
  'applyHtmlMarkup': true, // Boolean | Flag to determine whether certain text (e.g. walking instructions) should be output with HTML tags or not.
  'useMultiModalCall': true, // Boolean | A boolean to indicate whether or not to return 3 public transport journeys, a bus journey, a cycle hire journey, a personal cycle journey and a walking journey
  'walkingOptimization': true, // Boolean | A boolean to indicate whether to optimize journeys using walking
  'taxiOnlyTrip': true, // Boolean | A boolean to indicate whether to return one or more taxi journeys. Note, setting this to true will override \"useMultiModalCall\".
  'routeBetweenEntrances': true, // Boolean | A boolean to indicate whether public transport routes should include directions between platforms and station entrances.
  'useRealTimeLiveArrivals': true, // Boolean | A boolean to indicate if we want to receive real time live arrivals data where available.
  'calcOneDirection': true // Boolean | A boolean to make Journey Planner calculate journeys in one temporal direction only. In other words, only calculate journeys after the 'depart' time, or before the 'arrive' time. By default, the Journey Planner engine (EFA) calculates journeys in both temporal directions.
};
apiInstance.journeyJourneyResults(from, to, opts, (error, data, response) => {
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
 **from** | **String**| Origin of the journey. Can be WGS84 coordinates expressed as \&quot;lat,long\&quot;, a UK postcode, a Naptan (StopPoint) id, an ICS StopId, or a free-text string (will cause disambiguation unless it exactly matches a point of interest name). | 
 **to** | **String**| Destination of the journey. Can be WGS84 coordinates expressed as \&quot;lat,long\&quot;, a UK postcode, a Naptan (StopPoint) id, an ICS StopId, or a free-text string (will cause disambiguation unless it exactly matches a point of interest name). | 
 **via** | **String**| Travel through point on the journey. Can be WGS84 coordinates expressed as \&quot;lat,long\&quot;, a UK postcode, a Naptan (StopPoint) id, an ICS StopId, or a free-text string (will cause disambiguation unless it exactly matches a point of interest name). | [optional] 
 **nationalSearch** | **Boolean**| Does the journey cover stops outside London? eg. \&quot;nationalSearch&#x3D;true\&quot; | [optional] 
 **date** | **String**| The date must be in yyyyMMdd format | [optional] 
 **time** | **String**| The time must be in HHmm format | [optional] 
 **timeIs** | **String**| Does the time given relate to arrival or leaving time? Possible options: \&quot;departing\&quot; | \&quot;arriving\&quot; | [optional] 
 **journeyPreference** | **String**| The journey preference eg possible options: \&quot;leastinterchange\&quot; | \&quot;leasttime\&quot; | \&quot;leastwalking\&quot; | [optional] 
 **mode** | [**[String]**](String.md)| The mode must be a comma separated list of modes. eg possible options: \&quot;public-bus,overground,train,tube,coach,dlr,cablecar,tram,river,walking,cycle\&quot; | [optional] 
 **accessibilityPreference** | [**[String]**](String.md)| The accessibility preference must be a comma separated list eg. \&quot;noSolidStairs,noEscalators,noElevators,stepFreeToVehicle,stepFreeToPlatform\&quot; | [optional] 
 **fromName** | **String**| An optional name to associate with the origin of the journey in the results. | [optional] 
 **toName** | **String**| An optional name to associate with the destination of the journey in the results. | [optional] 
 **viaName** | **String**| An optional name to associate with the via point of the journey in the results. | [optional] 
 **maxTransferMinutes** | **String**| The max walking time in minutes for transfer eg. \&quot;120\&quot; | [optional] 
 **maxWalkingMinutes** | **String**| The max walking time in minutes for journeys eg. \&quot;120\&quot; | [optional] 
 **walkingSpeed** | **String**| The walking speed. eg possible options: \&quot;slow\&quot; | \&quot;average\&quot; | \&quot;fast\&quot;. | [optional] 
 **cyclePreference** | **String**| The cycle preference. eg possible options: \&quot;allTheWay\&quot; | \&quot;leaveAtStation\&quot; | \&quot;takeOnTransport\&quot; | \&quot;cycleHire\&quot; | [optional] 
 **adjustment** | **String**| Time adjustment command. eg possible options: \&quot;TripFirst\&quot; | \&quot;TripLast\&quot; | [optional] 
 **bikeProficiency** | [**[String]**](String.md)| A comma separated list of cycling proficiency levels. eg possible options: \&quot;easy,moderate,fast\&quot; | [optional] 
 **alternativeCycle** | **Boolean**| Option to determine whether to return alternative cycling journey | [optional] 
 **alternativeWalking** | **Boolean**| Option to determine whether to return alternative walking journey | [optional] 
 **applyHtmlMarkup** | **Boolean**| Flag to determine whether certain text (e.g. walking instructions) should be output with HTML tags or not. | [optional] 
 **useMultiModalCall** | **Boolean**| A boolean to indicate whether or not to return 3 public transport journeys, a bus journey, a cycle hire journey, a personal cycle journey and a walking journey | [optional] 
 **walkingOptimization** | **Boolean**| A boolean to indicate whether to optimize journeys using walking | [optional] 
 **taxiOnlyTrip** | **Boolean**| A boolean to indicate whether to return one or more taxi journeys. Note, setting this to true will override \&quot;useMultiModalCall\&quot;. | [optional] 
 **routeBetweenEntrances** | **Boolean**| A boolean to indicate whether public transport routes should include directions between platforms and station entrances. | [optional] 
 **useRealTimeLiveArrivals** | **Boolean**| A boolean to indicate if we want to receive real time live arrivals data where available. | [optional] 
 **calcOneDirection** | **Boolean**| A boolean to make Journey Planner calculate journeys in one temporal direction only. In other words, only calculate journeys after the &#39;depart&#39; time, or before the &#39;arrive&#39; time. By default, the Journey Planner engine (EFA) calculates journeys in both temporal directions. | [optional] 

### Return type

[**TflApiPresentationEntitiesJourneyPlannerItineraryResult**](TflApiPresentationEntitiesJourneyPlannerItineraryResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## journeyMeta

> [TflApiPresentationEntitiesMode] journeyMeta()

Gets a list of all of the available journey planner modes

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.JourneyApi();
apiInstance.journeyMeta((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[TflApiPresentationEntitiesMode]**](TflApiPresentationEntitiesMode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

