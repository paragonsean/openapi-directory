# DriveBcsOpen511Api.ResourcesApi

All URIs are relative to *http://api.open511.gov.bc.ca*

Method | HTTP request | Description
------------- | ------------- | -------------
[**areasGet**](ResourcesApi.md#areasGet) | **GET** /areas | Lists the geographical areas (e.g. districts) that can be used to filter events.
[**eventsGet**](ResourcesApi.md#eventsGet) | **GET** /events | Lists road events
[**jurisdictionGet**](ResourcesApi.md#jurisdictionGet) | **GET** /jurisdiction | Lists the jurisdictions publishing data through this Open511 API implementation
[**jurisdictiongeographyGet**](ResourcesApi.md#jurisdictiongeographyGet) | **GET** /jurisdictiongeography | Provides the geographical boundaries for all the jurisdictions.



## areasGet

> areasGet(opts)

Lists the geographical areas (e.g. districts) that can be used to filter events.

### Example

```javascript
import DriveBcsOpen511Api from 'drive_bcs_open511_api';

let apiInstance = new DriveBcsOpen511Api.ResourcesApi();
let opts = {
  'format': "'json'" // String | The format of the response
};
apiInstance.areasGet(opts, (error, data, response) => {
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
 **format** | **String**| The format of the response | [optional] [default to &#39;json&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## eventsGet

> eventsGet(opts)

Lists road events

The events resource provides information about road events (e.g. accidents, construction, special events). The response is a list of event elements matching the filtering parameters if any are provided. 

### Example

```javascript
import DriveBcsOpen511Api from 'drive_bcs_open511_api';

let apiInstance = new DriveBcsOpen511Api.ResourcesApi();
let opts = {
  'format': "'json'", // String | The format of the response
  'status': "'ALL'", // String | Limits the response to events having a given status.
  'severity': "'MAJOR'", // String | Limits the response to events tagged with one of the listed severity values. The possible values are: [MINOR, MODERATE, MAJOR].  Multiple values may be listed, and should be separated by a comma. The default is to return events of any severity.
  'jurisdiction': "'drivebc.ca'", // String | Limits the response to events reported by a given jurisdiction. The value given must be specified as the ID of a jurisdiction returned by the /jurisdiction resource. The default is to return events from all jurisdictions.
  'eventType': "'INCIDENT'", // String | Limits the response to events tagged with one of the listed event types.  The possible values include: [CONSTRUCTION, INCIDENT, SPECIAL_EVENT, WEATHER_CONDITION].  Multiple values may be listed, and should be separated by a comma. The default is to return events of all types.
  'created': "'>2015-09-01T12:00:00Z'", // String | Limits the response to events based on the date and time that the event was created (first recorded). The date/time must be specified in ISO 8601 format, and may be prefixed by one of the following operators [<, <=, >, >=] to indicate 'before', 'before or equal to', 'after' or 'after or equal to' respectively.  For example, >2013-12-01T12:00:00Z requests all events create after Dec. 1, 2015 at 12pm (noon) Coordinated Universal Time.  The default is to return events with any creation time.
  'updated': "'>2015-09-01T12:00:00Z'", // String | Limits the response to events based on the date and time that the event was last updated. The date/time must be specified in ISO 8601 format, and may be prefixed by one of the following operators [<, <=, >, >=] to indicate 'before', 'before or equal to', 'after' or 'after or equal to' respectively.  For example, >2013-12-01T12:00:00Z requests all events updated after Dec. 1, 2015 at 12pm (noon) Coordinated Universal Time. The default is to return events with any update time
  'roadName': "'Highway 99'", // String | Limits the response to events on a given road as specified by the road name.  An example of a valid road name is 'Highway 1'. The default is to return events on all roads.
  'areaId': "'drivebc.ca/1'", // String | Limits the response to events within one of the specified areas.  An area must be specified as the ID of an item returned by the /areas resource. For example: an area_id of 'drivebc.ca/1' limits events to those within the Lower Mainland District.  The default is to return events in all areas.
  'bbox': "'-130,48,-116,60'" // String | Limits the response to events that fall within the specified geographical bounding box.  The bbox format must be '[min longitude],[min latitude],[max longitude],[max latitude]' with WGS84 coordinates.  For example: -123.45,48.99,-122.45,49.49.  The default is to return events in all geographical locations.
};
apiInstance.eventsGet(opts, (error, data, response) => {
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
 **format** | **String**| The format of the response | [optional] [default to &#39;json&#39;]
 **status** | **String**| Limits the response to events having a given status. | [optional] [default to &#39;ALL&#39;]
 **severity** | **String**| Limits the response to events tagged with one of the listed severity values. The possible values are: [MINOR, MODERATE, MAJOR].  Multiple values may be listed, and should be separated by a comma. The default is to return events of any severity. | [optional] [default to &#39;MAJOR&#39;]
 **jurisdiction** | **String**| Limits the response to events reported by a given jurisdiction. The value given must be specified as the ID of a jurisdiction returned by the /jurisdiction resource. The default is to return events from all jurisdictions. | [optional] [default to &#39;drivebc.ca&#39;]
 **eventType** | **String**| Limits the response to events tagged with one of the listed event types.  The possible values include: [CONSTRUCTION, INCIDENT, SPECIAL_EVENT, WEATHER_CONDITION].  Multiple values may be listed, and should be separated by a comma. The default is to return events of all types. | [optional] [default to &#39;INCIDENT&#39;]
 **created** | **String**| Limits the response to events based on the date and time that the event was created (first recorded). The date/time must be specified in ISO 8601 format, and may be prefixed by one of the following operators [&lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;] to indicate &#39;before&#39;, &#39;before or equal to&#39;, &#39;after&#39; or &#39;after or equal to&#39; respectively.  For example, &gt;2013-12-01T12:00:00Z requests all events create after Dec. 1, 2015 at 12pm (noon) Coordinated Universal Time.  The default is to return events with any creation time. | [optional] [default to &#39;&gt;2015-09-01T12:00:00Z&#39;]
 **updated** | **String**| Limits the response to events based on the date and time that the event was last updated. The date/time must be specified in ISO 8601 format, and may be prefixed by one of the following operators [&lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;] to indicate &#39;before&#39;, &#39;before or equal to&#39;, &#39;after&#39; or &#39;after or equal to&#39; respectively.  For example, &gt;2013-12-01T12:00:00Z requests all events updated after Dec. 1, 2015 at 12pm (noon) Coordinated Universal Time. The default is to return events with any update time | [optional] [default to &#39;&gt;2015-09-01T12:00:00Z&#39;]
 **roadName** | **String**| Limits the response to events on a given road as specified by the road name.  An example of a valid road name is &#39;Highway 1&#39;. The default is to return events on all roads. | [optional] [default to &#39;Highway 99&#39;]
 **areaId** | **String**| Limits the response to events within one of the specified areas.  An area must be specified as the ID of an item returned by the /areas resource. For example: an area_id of &#39;drivebc.ca/1&#39; limits events to those within the Lower Mainland District.  The default is to return events in all areas. | [optional] [default to &#39;drivebc.ca/1&#39;]
 **bbox** | **String**| Limits the response to events that fall within the specified geographical bounding box.  The bbox format must be &#39;[min longitude],[min latitude],[max longitude],[max latitude]&#39; with WGS84 coordinates.  For example: -123.45,48.99,-122.45,49.49.  The default is to return events in all geographical locations. | [optional] [default to &#39;-130,48,-116,60&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## jurisdictionGet

> jurisdictionGet(opts)

Lists the jurisdictions publishing data through this Open511 API implementation

### Example

```javascript
import DriveBcsOpen511Api from 'drive_bcs_open511_api';

let apiInstance = new DriveBcsOpen511Api.ResourcesApi();
let opts = {
  'format': "'json'" // String | The format of the response
};
apiInstance.jurisdictionGet(opts, (error, data, response) => {
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
 **format** | **String**| The format of the response | [optional] [default to &#39;json&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## jurisdictiongeographyGet

> jurisdictiongeographyGet(opts)

Provides the geographical boundaries for all the jurisdictions.

### Example

```javascript
import DriveBcsOpen511Api from 'drive_bcs_open511_api';

let apiInstance = new DriveBcsOpen511Api.ResourcesApi();
let opts = {
  'format': "'json'" // String | The format of the response
};
apiInstance.jurisdictiongeographyGet(opts, (error, data, response) => {
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
 **format** | **String**| The format of the response | [optional] [default to &#39;json&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

