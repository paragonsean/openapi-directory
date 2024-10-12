# RealTimeRailPredictions.DefaultApi

All URIs are relative to *http://api.wmata.com/StationPrediction.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call547636a6f918230da855363f**](DefaultApi.md#call547636a6f918230da855363f) | **GET** /json/GetPrediction/{StationCodes} | JSON - Next Trains
[**call547636a6f918230da8553640**](DefaultApi.md#call547636a6f918230da8553640) | **GET** /GetPrediction/{StationCodes} | XML - Next Trains



## call547636a6f918230da855363f

> call547636a6f918230da855363f(stationCodes)

JSON - Next Trains

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;    &lt;p&gt;Returns next train arrival information for one or more stations. Will return  an empty set of results when no predictions are available. Use &lt;span class&#x3D;  \&quot;text-info\&quot;&gt;All&lt;/span&gt; for the StationCodes parameter to return predictions for  all stations.&lt;/p&gt;    &lt;p&gt;For terminal stations (e.g.: Greenbelt, Shady Grove, etc.), predictions may  be displayed twice.&lt;/p&gt;    &lt;p&gt;Some stations have two platforms (e.g.: Gallery Place, Fort Totten, L&#39;Enfant  Plaza, and Metro Center). To retrieve complete predictions for these stations,  be sure to pass in both StationCodes.&lt;/p&gt;    &lt;p&gt;For trains with no passengers, the DestinationName will be &lt;span class&#x3D;  \&quot;text-info\&quot;&gt;No Passenger&lt;/span&gt;.&lt;/p&gt;    &lt;p&gt;Next train arrival information is refreshed once every 20 to 30 seconds approximately.&lt;/p&gt;    &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;    &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt;  &lt;thead&gt;  &lt;tr&gt;  &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;    &lt;th&gt;Description&lt;/th&gt;  &lt;/tr&gt;  &lt;/thead&gt;    &lt;tbody&gt;  &lt;tr&gt;  &lt;td&gt;Trains&lt;/td&gt;    &lt;td&gt;  Array containing train prediction information (&lt;a href&#x3D;  \&quot;#AIMPredictionTrainInfo\&quot;&gt;AIMPredictionTrainInfo&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;AIMPredictionTrainInfo\&quot; name&#x3D;  \&quot;AIMPredictionTrainInfo\&quot;&gt;AIMPredictionTrainInfo  Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Car&lt;/td&gt;    &lt;td&gt;Number of cars on a train, usually 6 or 8, but might also  return &lt;span class&#x3D;\&quot;text-info\&quot;&gt;-&lt;/span&gt; or NULL.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Destination&lt;/td&gt;    &lt;td&gt;Abbreviated version of the final destination for a train. This  is similar to what is displayed on the signs at stations.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;DestinationCode&lt;/td&gt;    &lt;td&gt;Destination station code. Can be NULL. Use this value in other  rail-related APIs to retrieve data about a station.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;DestinationName&lt;/td&gt;    &lt;td&gt;When DestinationCode is populated, this is the full name of the  destination station, as shown on the WMATA website.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Group&lt;/td&gt;    &lt;td&gt;Denotes the track this train is on, but does not necessarily  equate to Track 1 or Track 2. With the exception of terminal  stations, predictions at the same station with different Group  values refer to trains on different tracks.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Line&lt;/td&gt;    &lt;td&gt;Two-letter abbreviation for the line (e.g.: RD, BL, YL, OR, GR,  or SV). May also be blank or &lt;span class&#x3D;\&quot;text-info\&quot;&gt;No&lt;/span&gt; for  trains with no passengers.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;LocationCode&lt;/td&gt;    &lt;td&gt;Station code for where the train is arriving. Useful when  passing in &lt;span class&#x3D;\&quot;text-info\&quot;&gt;All&lt;/span&gt; as the StationCodes  parameter. Use this value in other rail-related APIs to retrieve  data about a station.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;LocationName&lt;/td&gt;    &lt;td&gt;Full name of the station where the train is arriving. Useful  when passing in &lt;span class&#x3D;\&quot;text-info\&quot;&gt;All&lt;/span&gt; as the  StationCodes parameter.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Min&lt;/td&gt;    &lt;td&gt;Minutes until arrival. Can be a numeric value, &lt;span class&#x3D;  \&quot;text-info\&quot;&gt;ARR&lt;/span&gt; (arriving), &lt;span class&#x3D;  \&quot;text-info\&quot;&gt;BRD&lt;/span&gt; (boarding), &lt;span class&#x3D;  \&quot;text-info\&quot;&gt;---&lt;/span&gt;, or empty.&lt;/td&gt;  &lt;/tr&gt;  &lt;/tbody&gt;  &lt;/table&gt;  &lt;hr&gt;

### Example

```javascript
import RealTimeRailPredictions from 'real_time_rail_predictions';
let defaultClient = RealTimeRailPredictions.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new RealTimeRailPredictions.DefaultApi();
let stationCodes = "'B03'"; // String | Comma-separated list of station codes.  For all predictions, use \"All\".
apiInstance.call547636a6f918230da855363f(stationCodes, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stationCodes** | **String**| Comma-separated list of station codes.  For all predictions, use \&quot;All\&quot;. | [default to &#39;B03&#39;]

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## call547636a6f918230da8553640

> call547636a6f918230da8553640(stationCodes)

XML - Next Trains

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;    &lt;p&gt;Returns next train arrival information for one or more stations. Will return  an empty set of results when no predictions are available. Use &lt;span class&#x3D;  \&quot;text-info\&quot;&gt;All&lt;/span&gt; for the StationCodes parameter to return predictions for  all stations.&lt;/p&gt;    &lt;p&gt;For terminal stations (e.g.: Greenbelt, Shady Grove, etc.), predictions may  be displayed twice.&lt;/p&gt;    &lt;p&gt;Some stations have two platforms (e.g.: Gallery Place, Fort Totten, L&#39;Enfant  Plaza, and Metro Center). To retrieve complete predictions for these stations,  be sure to pass in both StationCodes.&lt;/p&gt;    &lt;p&gt;For trains with no passengers, the DestinationName will be &lt;span class&#x3D;  \&quot;text-info\&quot;&gt;No Passenger&lt;/span&gt;.&lt;/p&gt;    &lt;p&gt;Next train arrival information is refreshed once every 20 to 30 seconds approximately.&lt;/p&gt;    &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;    &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt;  &lt;thead&gt;  &lt;tr&gt;  &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;    &lt;th&gt;Description&lt;/th&gt;  &lt;/tr&gt;  &lt;/thead&gt;    &lt;tbody&gt;  &lt;tr&gt;  &lt;td&gt;Trains&lt;/td&gt;    &lt;td&gt;  Array containing train prediction information (&lt;a href&#x3D;  \&quot;#AIMPredictionTrainInfo\&quot;&gt;AIMPredictionTrainInfo&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;AIMPredictionTrainInfo\&quot; name&#x3D;  \&quot;AIMPredictionTrainInfo\&quot;&gt;AIMPredictionTrainInfo  Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Car&lt;/td&gt;    &lt;td&gt;Number of cars on a train, usually 6 or 8, but might also  return &lt;span class&#x3D;\&quot;text-info\&quot;&gt;-&lt;/span&gt; or NULL.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Destination&lt;/td&gt;    &lt;td&gt;Abbreviated version of the final destination for a train. This  is similar to what is displayed on the signs at stations.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;DestinationCode&lt;/td&gt;    &lt;td&gt;Destination station code. Can be NULL. Use this value in other  rail-related APIs to retrieve data about a station.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;DestinationName&lt;/td&gt;    &lt;td&gt;When DestinationCode is populated, this is the full name of the  destination station, as shown on the WMATA website.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Group&lt;/td&gt;    &lt;td&gt;Denotes the track this train is on, but does not necessarily  equate to Track 1 or Track 2. With the exception of terminal  stations, predictions at the same station with different Group  values refer to trains on different tracks.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Line&lt;/td&gt;    &lt;td&gt;Two-letter abbreviation for the line (e.g.: RD, BL, YL, OR, GR,  or SV). May also be blank or &lt;span class&#x3D;\&quot;text-info\&quot;&gt;No&lt;/span&gt; for  trains with no passengers.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;LocationCode&lt;/td&gt;    &lt;td&gt;Station code for where the train is arriving. Useful when  passing in &lt;span class&#x3D;\&quot;text-info\&quot;&gt;All&lt;/span&gt; as the StationCodes  parameter. Use this value in other rail-related APIs to retrieve  data about a station.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;LocationName&lt;/td&gt;    &lt;td&gt;Full name of the station where the train is arriving. Useful  when passing in &lt;span class&#x3D;\&quot;text-info\&quot;&gt;All&lt;/span&gt; as the  StationCodes parameter.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Min&lt;/td&gt;    &lt;td&gt;Minutes until arrival. Can be a numeric value, &lt;span class&#x3D;  \&quot;text-info\&quot;&gt;ARR&lt;/span&gt; (arriving), &lt;span class&#x3D;  \&quot;text-info\&quot;&gt;BRD&lt;/span&gt; (boarding), &lt;span class&#x3D;  \&quot;text-info\&quot;&gt;---&lt;/span&gt;, or empty.&lt;/td&gt;  &lt;/tr&gt;  &lt;/tbody&gt;  &lt;/table&gt;  &lt;hr&gt;

### Example

```javascript
import RealTimeRailPredictions from 'real_time_rail_predictions';
let defaultClient = RealTimeRailPredictions.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new RealTimeRailPredictions.DefaultApi();
let stationCodes = "'B03'"; // String | Comma-separated list of station codes.  For all predictions, use \"All\".
apiInstance.call547636a6f918230da8553640(stationCodes, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stationCodes** | **String**| Comma-separated list of station codes.  For all predictions, use \&quot;All\&quot;. | [default to &#39;B03&#39;]

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml

