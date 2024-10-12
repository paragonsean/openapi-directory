# Incidents.DefaultApi

All URIs are relative to *http://api.wmata.com/Incidents.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call54763641281d830c946a3d75**](DefaultApi.md#call54763641281d830c946a3d75) | **GET** /json/BusIncidents | JSON - Bus Incidents
[**call54763641281d830c946a3d76**](DefaultApi.md#call54763641281d830c946a3d76) | **GET** /json/ElevatorIncidents | JSON - Elevator/Escalator Outages
[**call54763641281d830c946a3d77**](DefaultApi.md#call54763641281d830c946a3d77) | **GET** /json/Incidents | JSON - Rail Incidents
[**call54763641281d830c946a3d78**](DefaultApi.md#call54763641281d830c946a3d78) | **GET** /BusIncidents | XML - Bus Incidents
[**call54763641281d830c946a3d79**](DefaultApi.md#call54763641281d830c946a3d79) | **GET** /ElevatorIncidents | XML - Elevator/Escalator Outages
[**call54763641281d830c946a3d7a**](DefaultApi.md#call54763641281d830c946a3d7a) | **GET** /Incidents | XML - Rail Incidents



## call54763641281d830c946a3d75

> call54763641281d830c946a3d75(opts)

JSON - Bus Incidents

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;    &lt;p&gt;Returns a set of reported bus incidents/delays for a given Route. Omit the  Route to return all reported items.&lt;/p&gt;    &lt;p&gt;Note that the Route parameter accepts only base route names and no  variations, i.e.: use 10A instead of 10Av1 and 10Av2.&lt;/p&gt;    &lt;p&gt;Bus incidents/delays are refreshed once every 20 to 30 seconds approximately.&lt;/p&gt;    &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;    &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt;  &lt;thead&gt;  &lt;tr&gt;  &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;    &lt;th&gt;Description&lt;/th&gt;  &lt;/tr&gt;  &lt;/thead&gt;    &lt;tbody&gt;  &lt;tr&gt;  &lt;td&gt;BusIncidents&lt;/td&gt;    &lt;td&gt;  Array containing bus incident information (&lt;a href&#x3D;  \&quot;#BusIncident\&quot;&gt;BusIncident&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;BusIncident\&quot; name&#x3D;\&quot;BusIncident\&quot;&gt;BusIncident  Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;DateUpdated&lt;/td&gt;    &lt;td&gt;Date and time (Eastern Standard Time) of last update. Will be  in YYYY-MM-DDTHH:mm:ss format (e.g.: 2014-10-28T08:13:03).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Description&lt;/td&gt;    &lt;td&gt;Free-text description of the delay or incident.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;IncidentID&lt;/td&gt;    &lt;td&gt;Unique identifier for an incident.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;IncidentType&lt;/td&gt;    &lt;td&gt;Free-text description of the incident type. Usually  &lt;span class&#x3D;\&quot;text-info\&quot;&gt;Delay&lt;/span&gt; or &lt;span class&#x3D;  \&quot;text-info\&quot;&gt;Alert&lt;/span&gt; but is subject to change at any time.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;RoutesAffected&lt;/td&gt;    &lt;td&gt;Array containing routes affected. Routes listed are usually  identical to base route names (i.e.: not 10Av1 or 10Av2, but 10A),  but &lt;em&gt;may&lt;/em&gt; differ from what our bus methods return.&lt;/td&gt;  &lt;/tr&gt;  &lt;/tbody&gt;  &lt;/table&gt;

### Example

```javascript
import Incidents from 'incidents';
let defaultClient = Incidents.ApiClient.instance;
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

let apiInstance = new Incidents.DefaultApi();
let opts = {
  'route': "route_example" // String | Base bus route; variations are not recognized (i.e.: C2 instead of C2v1, C2v2, etc.).
};
apiInstance.call54763641281d830c946a3d75(opts, (error, data, response) => {
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
 **route** | **String**| Base bus route; variations are not recognized (i.e.: C2 instead of C2v1, C2v2, etc.). | [optional] 

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## call54763641281d830c946a3d76

> call54763641281d830c946a3d76(opts)

JSON - Elevator/Escalator Outages

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;  &lt;p&gt;Returns a list of &lt;em&gt;reported&lt;/em&gt; elevator and escalator outages at a given station. Omit the StationCode parameter to return all reported outages.&lt;/p&gt;  &lt;p&gt;Note that for stations with multiple platforms and therefore StationCodes (e.g.: Metro Center, L&#39;Enfant Plaza, etc.), a distinct call is required for each StationCode.&lt;/p&gt;  &lt;p&gt;Elevator and escalator outages are refreshed once every 20 to 30 seconds approximately.&lt;/p&gt;  &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;  &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt; &lt;thead&gt; &lt;tr&gt; &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;  &lt;th&gt;Description&lt;/th&gt; &lt;/tr&gt; &lt;/thead&gt;  &lt;tbody&gt; &lt;tr&gt; &lt;td&gt;ElevatorIncidents&lt;/td&gt;  &lt;td&gt; Array containing elevator/escalator outage information (&lt;a href&#x3D;\&quot;#ElevatorIncident\&quot;&gt;ElevatorIncident&lt;/a&gt;). &lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td colspan&#x3D;\&quot;2\&quot;&gt; &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt; &lt;a id&#x3D;\&quot;ElevatorIncident\&quot; name&#x3D; \&quot;ElevatorIncident\&quot;&gt;ElevatorIncident Elements&lt;/a&gt; &lt;/div&gt; &lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;DateOutOfServ&lt;/td&gt;  &lt;td&gt;Date and time (Eastern Standard Time) unit was reported out of service. Will be in YYYY-MM-DDTHH:mm:ss format (e.g.: 2014-10-27T15:17:00).&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;DateUpdated&lt;/td&gt;  &lt;td&gt;Date and time (Eastern Standard Time) outage details was last updated. Will be in YYYY-MM-DDTHH:mm:ss format (e.g.: 2014-10-27T15:17:00).&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;DisplayOrder&lt;/td&gt;  &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt;&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;EstimatedReturnToService&lt;/td&gt;  &lt;td&gt;Estimated date and time (Eastern Standard Time) by when unit is expected to return to normal service. May be NULL, otherwise will be in YYYY-MM-DDTHH:mm:ss format (e.g.: 2014-10-27T23:59:59).&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;LocationDescription&lt;/td&gt;  &lt;td&gt;Free-text description of the unit location within a station (e.g.: &lt;span class&#x3D;\&quot;text-info\&quot;&gt;Escalator between mezzanine and platform&lt;/span&gt;).&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;StationCode&lt;/td&gt;  &lt;td&gt;Unit&#39;s station code. Use this value in other rail-related APIs to retrieve data about a station.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;StationName&lt;/td&gt;  &lt;td&gt;Full station name, may include entrance information (e.g.: &lt;span class&#x3D;\&quot;text-info\&quot;&gt;Metro Center, G and 11th St Entrance&lt;/span&gt;).&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;SymptomCode&lt;/td&gt;  &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt;&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;SymptomDescription&lt;/td&gt;  &lt;td&gt;Description for why the unit is out of service or otherwise in reduced operation.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;TimeOutOfService&lt;/td&gt;  &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt; Use the time portion of the DateOutOfServ element.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;UnitName&lt;/td&gt;  &lt;td&gt;Unique identifier for unit, by type (a single elevator and escalator may have the same UnitName, but no two elevators or two escalators will have the same UnitName).&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;UnitStatus&lt;/td&gt;  &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt; If listed here, the unit is inoperational or otherwise impaired.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;UnitType&lt;/td&gt;  &lt;td&gt;Type of unit. Will be &lt;span class&#x3D;\&quot;text-info\&quot;&gt;ELEVATOR&lt;/span&gt; or &lt;span class&#x3D;\&quot;text-info\&quot;&gt;ESCALATOR&lt;/span&gt;.&lt;/td&gt; &lt;/tr&gt; &lt;/tbody&gt; &lt;/table&gt;

### Example

```javascript
import Incidents from 'incidents';
let defaultClient = Incidents.ApiClient.instance;
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

let apiInstance = new Incidents.DefaultApi();
let opts = {
  'stationCode': "stationCode_example" // String | Station code.  Use the Station List method to return a list of all station codes.
};
apiInstance.call54763641281d830c946a3d76(opts, (error, data, response) => {
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
 **stationCode** | **String**| Station code.  Use the Station List method to return a list of all station codes. | [optional] 

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## call54763641281d830c946a3d77

> call54763641281d830c946a3d77()

JSON - Rail Incidents

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;    &lt;p&gt;Returns reported rail incidents (significant disruptions and delays to  normal service). The data is identical to WMATA&#39;s &lt;a href&#x3D;  \&quot;http://www.metroalerts.info/rss.aspx?rs\&quot;&gt;Metrorail Service Status  feed&lt;/a&gt;.&lt;/p&gt;    &lt;p&gt;Rail incidents are refreshed once every 20 to 30 seconds approximately.&lt;/p&gt;    &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;    &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt;  &lt;thead&gt;  &lt;tr&gt;  &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;    &lt;th&gt;Description&lt;/th&gt;  &lt;/tr&gt;  &lt;/thead&gt;    &lt;tbody&gt;  &lt;tr&gt;  &lt;td&gt;Incidents&lt;/td&gt;    &lt;td&gt;  Array containing rail disruption information (&lt;a href&#x3D;  \&quot;#Incident\&quot;&gt;Incident&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;Incident\&quot; name&#x3D;\&quot;Incident\&quot;&gt;Incident Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;DateUpdated&lt;/td&gt;    &lt;td&gt;Date and time (Eastern Standard Time) of last update. Will be  in YYYY-MM-DDTHH:mm:SS format (e.g.: 2010-07-29T14:21:28).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;DelaySeverity&lt;/td&gt;    &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt;&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Description&lt;/td&gt;    &lt;td&gt;Free-text description of the incident.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;EmergencyText&lt;/td&gt;    &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt;&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;EndLocationFullName&lt;/td&gt;    &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt;&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;IncidentID&lt;/td&gt;    &lt;td&gt;Unique identifier for an incident.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;IncidentType&lt;/td&gt;    &lt;td&gt;Free-text description of the incident type. Usually Delay or  Alert but is subject to change at any time.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;LinesAffected&lt;/td&gt;    &lt;td&gt;Semi-colon and space separated list of line codes (e.g.:  &lt;span class&#x3D;\&quot;text-info\&quot;&gt;RD;&lt;/span&gt; or &lt;span class&#x3D;\&quot;text-info\&quot;&gt;BL;  OR;&lt;/span&gt; or &lt;span class&#x3D;\&quot;text-info\&quot;&gt;BL; OR; RD;&lt;/span&gt;). We do  plan to update this to return something more reasonable like an  array, but until then, use code similar to the following:&lt;br&gt;  &lt;br&gt;  &lt;code&gt;\&quot;RD; GR; BL;\&quot;.split(/;[\\s]?/).filter(function(fn) { return fn  !&#x3D;&#x3D; &#39;&#39;; })&lt;/code&gt;&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;PassengerDelay&lt;/td&gt;    &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt;&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;  StartLocationFullName&lt;/td&gt;    &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt;&lt;/td&gt;  &lt;/tr&gt;  &lt;/tbody&gt;  &lt;/table&gt;

### Example

```javascript
import Incidents from 'incidents';
let defaultClient = Incidents.ApiClient.instance;
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

let apiInstance = new Incidents.DefaultApi();
apiInstance.call54763641281d830c946a3d77((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## call54763641281d830c946a3d78

> call54763641281d830c946a3d78(opts)

XML - Bus Incidents

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;    &lt;p&gt;Returns a set of reported bus incidents/delays for a given Route. Omit the  Route to return all reported items.&lt;/p&gt;    &lt;p&gt;Note that the Route parameter accepts only base route names and no  variations, i.e.: use 10A instead of 10Av1 and 10Av2.&lt;/p&gt;    &lt;p&gt;Bus incidents/delays are refreshed once every 20 to 30 seconds approximately.&lt;/p&gt;    &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;    &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt;  &lt;thead&gt;  &lt;tr&gt;  &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;    &lt;th&gt;Description&lt;/th&gt;  &lt;/tr&gt;  &lt;/thead&gt;    &lt;tbody&gt;  &lt;tr&gt;  &lt;td&gt;BusIncidents&lt;/td&gt;    &lt;td&gt;  Array containing bus incident information (&lt;a href&#x3D;  \&quot;#BusIncident\&quot;&gt;BusIncident&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;BusIncident\&quot; name&#x3D;\&quot;BusIncident\&quot;&gt;BusIncident  Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;DateUpdated&lt;/td&gt;    &lt;td&gt;Date and time (Eastern Standard Time) of last update. Will be  in YYYY-MM-DDTHH:mm:ss format (e.g.: 2014-10-28T08:13:03).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Description&lt;/td&gt;    &lt;td&gt;Free-text description of the delay or incident.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;IncidentID&lt;/td&gt;    &lt;td&gt;Unique identifier for an incident.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;IncidentType&lt;/td&gt;    &lt;td&gt;Free-text description of the incident type. Usually  &lt;span class&#x3D;\&quot;text-info\&quot;&gt;Delay&lt;/span&gt; or &lt;span class&#x3D;  \&quot;text-info\&quot;&gt;Alert&lt;/span&gt; but is subject to change at any time.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;RoutesAffected&lt;/td&gt;    &lt;td&gt;Array containing routes affected. Routes listed are usually  identical to base route names (i.e.: not 10Av1 or 10Av2, but 10A),  but &lt;em&gt;may&lt;/em&gt; differ from what our bus methods return.&lt;/td&gt;  &lt;/tr&gt;  &lt;/tbody&gt;  &lt;/table&gt;

### Example

```javascript
import Incidents from 'incidents';
let defaultClient = Incidents.ApiClient.instance;
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

let apiInstance = new Incidents.DefaultApi();
let opts = {
  'route': "route_example" // String | Bus route.  Use full route code, i.e.: C2 instead of C2v1, C2v2, etc.
};
apiInstance.call54763641281d830c946a3d78(opts, (error, data, response) => {
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
 **route** | **String**| Bus route.  Use full route code, i.e.: C2 instead of C2v1, C2v2, etc. | [optional] 

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml


## call54763641281d830c946a3d79

> call54763641281d830c946a3d79(opts)

XML - Elevator/Escalator Outages

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;  &lt;p&gt;Returns a list of &lt;em&gt;reported&lt;/em&gt; elevator and escalator outages at a given station. Omit the StationCode parameter to return all reported outages.&lt;/p&gt;  &lt;p&gt;Note that for stations with multiple platforms and therefore StationCodes (e.g.: Metro Center, L&#39;Enfant Plaza, etc.), a distinct call is required for each StationCode.&lt;/p&gt;  &lt;p&gt;Elevator and escalator outages are refreshed once every 20 to 30 seconds approximately.&lt;/p&gt;  &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;  &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt; &lt;thead&gt; &lt;tr&gt; &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;  &lt;th&gt;Description&lt;/th&gt; &lt;/tr&gt; &lt;/thead&gt;  &lt;tbody&gt; &lt;tr&gt; &lt;td&gt;ElevatorIncidents&lt;/td&gt;  &lt;td&gt; Array containing elevator/escalator outage information (&lt;a href&#x3D;\&quot;#ElevatorIncident\&quot;&gt;ElevatorIncident&lt;/a&gt;). &lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td colspan&#x3D;\&quot;2\&quot;&gt; &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt; &lt;a id&#x3D;\&quot;ElevatorIncident\&quot; name&#x3D; \&quot;ElevatorIncident\&quot;&gt;ElevatorIncident Elements&lt;/a&gt; &lt;/div&gt; &lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;DateOutOfServ&lt;/td&gt;  &lt;td&gt;Date and time (Eastern Standard Time) unit was reported out of service. Will be in YYYY-MM-DDTHH:mm:ss format (e.g.: 2014-10-27T15:17:00).&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;DateUpdated&lt;/td&gt;  &lt;td&gt;Date and time (Eastern Standard Time) outage details was last updated. Will be in YYYY-MM-DDTHH:mm:ss format (e.g.: 2014-10-27T15:17:00).&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;DisplayOrder&lt;/td&gt;  &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt;&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;EstimatedReturnToService&lt;/td&gt;  &lt;td&gt;Estimated date and time (Eastern Standard Time) by when unit is expected to return to normal service. May be NULL, otherwise will be in YYYY-MM-DDTHH:mm:ss format (e.g.: 2014-10-27T23:59:59).&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;LocationDescription&lt;/td&gt;  &lt;td&gt;Free-text description of the unit location within a station (e.g.: &lt;span class&#x3D;\&quot;text-info\&quot;&gt;Escalator between mezzanine and platform&lt;/span&gt;).&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;StationCode&lt;/td&gt;  &lt;td&gt;Unit&#39;s station code. Use this value in other rail-related APIs to retrieve data about a station.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;StationName&lt;/td&gt;  &lt;td&gt;Full station name, may include entrance information (e.g.: &lt;span class&#x3D;\&quot;text-info\&quot;&gt;Metro Center, G and 11th St Entrance&lt;/span&gt;).&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;SymptomCode&lt;/td&gt;  &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt;&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;SymptomDescription&lt;/td&gt;  &lt;td&gt;Description for why the unit is out of service or otherwise in reduced operation.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;TimeOutOfService&lt;/td&gt;  &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt; Use the time portion of the DateOutOfServ element.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;UnitName&lt;/td&gt;  &lt;td&gt;Unique identifier for unit, by type (a single elevator and escalator may have the same UnitName, but no two elevators or two escalators will have the same UnitName).&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;UnitStatus&lt;/td&gt;  &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt; If listed here, the unit is inoperational or otherwise impaired.&lt;/td&gt; &lt;/tr&gt;  &lt;tr&gt; &lt;td&gt;UnitType&lt;/td&gt;  &lt;td&gt;Type of unit. Will be &lt;span class&#x3D;\&quot;text-info\&quot;&gt;ELEVATOR&lt;/span&gt; or &lt;span class&#x3D;\&quot;text-info\&quot;&gt;ESCALATOR&lt;/span&gt;.&lt;/td&gt; &lt;/tr&gt; &lt;/tbody&gt; &lt;/table&gt;

### Example

```javascript
import Incidents from 'incidents';
let defaultClient = Incidents.ApiClient.instance;
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

let apiInstance = new Incidents.DefaultApi();
let opts = {
  'stationCode': "stationCode_example" // String | Two-letter station code.  Use the Station List method to return a list of all station codes.
};
apiInstance.call54763641281d830c946a3d79(opts, (error, data, response) => {
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
 **stationCode** | **String**| Two-letter station code.  Use the Station List method to return a list of all station codes. | [optional] 

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml


## call54763641281d830c946a3d7a

> call54763641281d830c946a3d7a()

XML - Rail Incidents

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;    &lt;p&gt;Returns reported rail incidents (significant disruptions and delays to  normal service). The data is identical to WMATA&#39;s &lt;a href&#x3D;  \&quot;http://www.metroalerts.info/rss.aspx?rs\&quot;&gt;Metrorail Service Status  feed&lt;/a&gt;.&lt;/p&gt;    &lt;p&gt;Rail incidents are refreshed once every 20 to 30 seconds approximately.&lt;/p&gt;    &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;    &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt;  &lt;thead&gt;  &lt;tr&gt;  &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;    &lt;th&gt;Description&lt;/th&gt;  &lt;/tr&gt;  &lt;/thead&gt;    &lt;tbody&gt;  &lt;tr&gt;  &lt;td&gt;Incidents&lt;/td&gt;    &lt;td&gt;  Array containing rail disruption information (&lt;a href&#x3D;  \&quot;#Incident\&quot;&gt;Incident&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;Incident\&quot; name&#x3D;\&quot;Incident\&quot;&gt;Incident Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;DateUpdated&lt;/td&gt;    &lt;td&gt;Date and time (Eastern Standard Time) of last update. Will be  in YYYY-MM-DDTHH:mm:SS format (e.g.: 2010-07-29T14:21:28).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;DelaySeverity&lt;/td&gt;    &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt;&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Description&lt;/td&gt;    &lt;td&gt;Free-text description of the incident.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;EmergencyText&lt;/td&gt;    &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt;&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;EndLocationFullName&lt;/td&gt;    &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt;&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;IncidentID&lt;/td&gt;    &lt;td&gt;Unique identifier for an incident.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;IncidentType&lt;/td&gt;    &lt;td&gt;Free-text description of the incident type. Usually Delay or  Alert but is subject to change at any time.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;LinesAffected&lt;/td&gt;    &lt;td&gt;Semi-colon and space separated list of line codes (e.g.:  &lt;span class&#x3D;\&quot;text-info\&quot;&gt;RD;&lt;/span&gt; or &lt;span class&#x3D;\&quot;text-info\&quot;&gt;BL;  OR;&lt;/span&gt; or &lt;span class&#x3D;\&quot;text-info\&quot;&gt;BL; OR; RD;&lt;/span&gt;). We do  plan to update this to return something more reasonable like an  array, but until then, use code similar to the following:&lt;br&gt;  &lt;br&gt;  &lt;code&gt;\&quot;RD; GR; BL;\&quot;.split(/;[\\s]?/).filter(function(fn) { return fn  !&#x3D;&#x3D; &#39;&#39;; })&lt;/code&gt;&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;PassengerDelay&lt;/td&gt;    &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt;&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td style&#x3D;\&quot;text-decoration: line-through\&quot;&gt;  StartLocationFullName&lt;/td&gt;    &lt;td&gt;&lt;span class&#x3D;\&quot;text-danger\&quot;&gt;Deprecated.&lt;/span&gt;&lt;/td&gt;  &lt;/tr&gt;  &lt;/tbody&gt;  &lt;/table&gt;

### Example

```javascript
import Incidents from 'incidents';
let defaultClient = Incidents.ApiClient.instance;
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

let apiInstance = new Incidents.DefaultApi();
apiInstance.call54763641281d830c946a3d7a((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml

