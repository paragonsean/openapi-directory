# PiWebApi2018Sp1SwaggerSpec.StreamSetApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**streamSetGetChannel**](StreamSetApi.md#streamSetGetChannel) | **GET** /streamsets/{webId}/channel | Opens a channel that will send messages about any value changes for the attributes of an Element, Event Frame, or Attribute.
[**streamSetGetChannelAdHoc**](StreamSetApi.md#streamSetGetChannelAdHoc) | **GET** /streamsets/channel | Opens a channel that will send messages about any value changes for the specified streams.
[**streamSetGetEnd**](StreamSetApi.md#streamSetGetEnd) | **GET** /streamsets/{webId}/end | Returns End of stream values of the attributes for an Element, Event Frame or Attribute
[**streamSetGetEndAdHoc**](StreamSetApi.md#streamSetGetEndAdHoc) | **GET** /streamsets/end | Returns End Of Stream values for attributes of the specified streams
[**streamSetGetInterpolated**](StreamSetApi.md#streamSetGetInterpolated) | **GET** /streamsets/{webId}/interpolated | Returns interpolated values of attributes for an element, event frame or attribute over the specified time range at the specified sampling interval.
[**streamSetGetInterpolatedAdHoc**](StreamSetApi.md#streamSetGetInterpolatedAdHoc) | **GET** /streamsets/interpolated | Returns interpolated values of the specified streams over the specified time range at the specified sampling interval.
[**streamSetGetInterpolatedAtTimes**](StreamSetApi.md#streamSetGetInterpolatedAtTimes) | **GET** /streamsets/{webId}/interpolatedattimes | Returns interpolated values of attributes for an element, event frame or attribute at the specified times.
[**streamSetGetInterpolatedAtTimesAdHoc**](StreamSetApi.md#streamSetGetInterpolatedAtTimesAdHoc) | **GET** /streamsets/interpolatedattimes | Returns interpolated values of the specified streams at the specified times.
[**streamSetGetJoined**](StreamSetApi.md#streamSetGetJoined) | **GET** /streamsets/joined | Returns the base stream&#39;s recorded values and subordinate streams&#39; interpolated values at times matching the recorded values&#39; timestamps.
[**streamSetGetPlot**](StreamSetApi.md#streamSetGetPlot) | **GET** /streamsets/{webId}/plot | Returns values of attributes for an element, event frame or attribute over the specified time range suitable for plotting over the number of intervals (typically represents pixels).
[**streamSetGetPlotAdHoc**](StreamSetApi.md#streamSetGetPlotAdHoc) | **GET** /streamsets/plot | Returns values of attributes for the specified streams over the specified time range suitable for plotting over the number of intervals (typically represents pixels).
[**streamSetGetRecorded**](StreamSetApi.md#streamSetGetRecorded) | **GET** /streamsets/{webId}/recorded | Returns recorded values of the attributes for an element, event frame, or attribute.
[**streamSetGetRecordedAdHoc**](StreamSetApi.md#streamSetGetRecordedAdHoc) | **GET** /streamsets/recorded | Returns recorded values of the specified streams.
[**streamSetGetRecordedAtTime**](StreamSetApi.md#streamSetGetRecordedAtTime) | **GET** /streamsets/{webId}/recordedattime | Returns recorded values of the attributes for an element, event frame, or attribute.
[**streamSetGetRecordedAtTimeAdHoc**](StreamSetApi.md#streamSetGetRecordedAtTimeAdHoc) | **GET** /streamsets/recordedattime | Returns recorded values based on the passed time and retrieval mode.
[**streamSetGetRecordedAtTimes**](StreamSetApi.md#streamSetGetRecordedAtTimes) | **GET** /streamsets/{webId}/recordedattimes | Returns recorded values of attributes for an element, event frame or attribute at the specified times.
[**streamSetGetRecordedAtTimesAdHoc**](StreamSetApi.md#streamSetGetRecordedAtTimesAdHoc) | **GET** /streamsets/recordedattimes | Returns recorded values of the specified streams at the specified times.
[**streamSetGetSummaries**](StreamSetApi.md#streamSetGetSummaries) | **GET** /streamsets/{webId}/summary | Returns summary values of the attributes for an element, event frame or attribute.
[**streamSetGetSummariesAdHoc**](StreamSetApi.md#streamSetGetSummariesAdHoc) | **GET** /streamsets/summary | Returns summary values of the specified streams.
[**streamSetGetValues**](StreamSetApi.md#streamSetGetValues) | **GET** /streamsets/{webId}/value | Returns values of the attributes for an Element, Event Frame or Attribute at the specified time.
[**streamSetGetValuesAdHoc**](StreamSetApi.md#streamSetGetValuesAdHoc) | **GET** /streamsets/value | Returns values of the specified streams.
[**streamSetRegisterStreamSetUpdates**](StreamSetApi.md#streamSetRegisterStreamSetUpdates) | **POST** /streamsets/updates | Register for stream updates
[**streamSetRetrieveStreamSetUpdates**](StreamSetApi.md#streamSetRetrieveStreamSetUpdates) | **GET** /streamsets/updates | Receive stream updates
[**streamSetUpdateValue**](StreamSetApi.md#streamSetUpdateValue) | **POST** /streamsets/{webId}/value | Updates a single value for the specified streams.
[**streamSetUpdateValueAdHoc**](StreamSetApi.md#streamSetUpdateValueAdHoc) | **POST** /streamsets/value | Updates a single value for the specified streams.
[**streamSetUpdateValues**](StreamSetApi.md#streamSetUpdateValues) | **POST** /streamsets/{webId}/recorded | Updates multiple values for the specified streams.
[**streamSetUpdateValuesAdHoc**](StreamSetApi.md#streamSetUpdateValuesAdHoc) | **POST** /streamsets/recorded | Updates multiple values for the specified streams.



## streamSetGetChannel

> streamSetGetChannel(webId, opts)

Opens a channel that will send messages about any value changes for the attributes of an Element, Event Frame, or Attribute.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let webId = "webId_example"; // String | The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes.
let opts = {
  'categoryName': "categoryName_example", // String | Specify that included attributes must have this category. The default is no category filter.
  'heartbeatRate': 56, // Number | Specifies the maximum number of consecutive empty messages that can be elapsed with no new data updates from the PI System, after which the client receives an empty payload. It helps to check if the connection is still alive. Zero/negative values correspond to no heartbeat, and the default value is no heartbeat.
  'includeInitialValues': true, // Boolean | Specified if the channel should send a message with the current values of all the streams after the connection is opened. The default is 'false'.
  'nameFilter': "nameFilter_example", // String | The name query string used for filtering attributes. The default is no filter.
  'searchFullHierarchy': true, // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
  'showExcluded': true, // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
  'showHidden': true, // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
  'templateName': "templateName_example", // String | Specify that included attributes must be members of this template. The default is no template filter.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetGetChannel(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes. | 
 **categoryName** | **String**| Specify that included attributes must have this category. The default is no category filter. | [optional] 
 **heartbeatRate** | **Number**| Specifies the maximum number of consecutive empty messages that can be elapsed with no new data updates from the PI System, after which the client receives an empty payload. It helps to check if the connection is still alive. Zero/negative values correspond to no heartbeat, and the default value is no heartbeat. | [optional] 
 **includeInitialValues** | **Boolean**| Specified if the channel should send a message with the current values of all the streams after the connection is opened. The default is &#39;false&#39;. | [optional] 
 **nameFilter** | **String**| The name query string used for filtering attributes. The default is no filter. | [optional] 
 **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **templateName** | **String**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetGetChannelAdHoc

> streamSetGetChannelAdHoc(webId, opts)

Opens a channel that will send messages about any value changes for the specified streams.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let webId = ["null"]; // [String] | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
let opts = {
  'heartbeatRate': 56, // Number | Specifies the maximum number of consecutive empty messages that can be elapsed with no new data updates from the PI System, after which the client receives an empty payload. It helps to check if the connection is still alive. Zero/negative values correspond to no heartbeat, and the default value is no heartbeat.
  'includeInitialValues': true, // Boolean | Specified if the channel should send a message with the current values of all the streams after the connection is opened. The default is 'false'.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetGetChannelAdHoc(webId, opts, (error, data, response) => {
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
 **webId** | [**[String]**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | 
 **heartbeatRate** | **Number**| Specifies the maximum number of consecutive empty messages that can be elapsed with no new data updates from the PI System, after which the client receives an empty payload. It helps to check if the connection is still alive. Zero/negative values correspond to no heartbeat, and the default value is no heartbeat. | [optional] 
 **includeInitialValues** | **Boolean**| Specified if the channel should send a message with the current values of all the streams after the connection is opened. The default is &#39;false&#39;. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetGetEnd

> ItemsStreamValue streamSetGetEnd(webId, opts)

Returns End of stream values of the attributes for an Element, Event Frame or Attribute

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let webId = "webId_example"; // String | The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes.
let opts = {
  'categoryName': "categoryName_example", // String | Specify that included attributes must have this category. The default is no category filter.
  'nameFilter': "nameFilter_example", // String | The name query string used for filtering attributes. The default is no filter.
  'searchFullHierarchy': true, // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'showExcluded': true, // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
  'showHidden': true, // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. 'Name' is the only supported field by which to sort.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'
  'templateName': "templateName_example", // String | Specify that included attributes must be members of this template. The default is no template filter.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetGetEnd(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes. | 
 **categoryName** | **String**| Specify that included attributes must have this category. The default is no category filter. | [optional] 
 **nameFilter** | **String**| The name query string used for filtering attributes. The default is no filter. | [optional] 
 **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; | [optional] 
 **templateName** | **String**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsStreamValue**](ItemsStreamValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetGetEndAdHoc

> ItemsStreamValues streamSetGetEndAdHoc(webId, opts)

Returns End Of Stream values for attributes of the specified streams

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let webId = ["null"]; // [String] | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. 'Name' is the only supported field by which to sort.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetGetEndAdHoc(webId, opts, (error, data, response) => {
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
 **webId** | [**[String]**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetGetInterpolated

> ItemsStreamValues streamSetGetInterpolated(webId, opts)

Returns interpolated values of attributes for an element, event frame or attribute over the specified time range at the specified sampling interval.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let webId = "webId_example"; // String | The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
let opts = {
  'categoryName': "categoryName_example", // String | Specify that included attributes must have this category. The default is no category filter.
  'endTime': "endTime_example", // String | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
  'filterExpression': "filterExpression_example", // String | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering.
  'includeFilteredValues': true, // Boolean | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.
  'interval': "interval_example", // String | The sampling interval, in AFTimeSpan format.
  'nameFilter': "nameFilter_example", // String | The name query string used for filtering attributes. The default is no filter.
  'searchFullHierarchy': true, // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'showExcluded': true, // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
  'showHidden': true, // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. 'Name' is the only supported field by which to sort.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'.
  'startTime': "startTime_example", // String | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.
  'syncTime': "syncTime_example", // String | An optional start time anchor, in AFTime format. When specified, interpolated data retrieval will use the sync time as the origin for calculating the interval times.
  'syncTimeBoundaryType': "syncTimeBoundaryType_example", // String | An optional string specifying the boundary type to use when applying a syncTime. The allowed values are 'Inside' and 'Outside'. The default is 'Inside'.
  'templateName': "templateName_example", // String | Specify that included attributes must be members of this template. The default is no template filter.
  'timeZone': "timeZone_example", // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetGetInterpolated(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes. | 
 **categoryName** | **String**| Specify that included attributes must have this category. The default is no category filter. | [optional] 
 **endTime** | **String**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **filterExpression** | **String**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. | [optional] 
 **includeFilteredValues** | **Boolean**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] 
 **interval** | **String**| The sampling interval, in AFTimeSpan format. | [optional] 
 **nameFilter** | **String**| The name query string used for filtering attributes. The default is no filter. | [optional] 
 **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] 
 **syncTime** | **String**| An optional start time anchor, in AFTime format. When specified, interpolated data retrieval will use the sync time as the origin for calculating the interval times. | [optional] 
 **syncTimeBoundaryType** | **String**| An optional string specifying the boundary type to use when applying a syncTime. The allowed values are &#39;Inside&#39; and &#39;Outside&#39;. The default is &#39;Inside&#39;. | [optional] 
 **templateName** | **String**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] 
 **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetGetInterpolatedAdHoc

> ItemsStreamValues streamSetGetInterpolatedAdHoc(webId, opts)

Returns interpolated values of the specified streams over the specified time range at the specified sampling interval.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let webId = ["null"]; // [String] | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
let opts = {
  'endTime': "endTime_example", // String | An optional end time. The default is '*'. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
  'filterExpression': "filterExpression_example", // String | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering.
  'includeFilteredValues': true, // Boolean | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.
  'interval': "interval_example", // String | The sampling interval, in AFTimeSpan format.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. 'Name' is the only supported field by which to sort.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'
  'startTime': "startTime_example", // String | An optional start time. The default is '*-1d'.
  'syncTime': "syncTime_example", // String | An optional start time anchor, in AFTime format. When specified, interpolated data retrieval will use the sync time as the origin for calculating the interval times.
  'syncTimeBoundaryType': "syncTimeBoundaryType_example", // String | An optional string specifying the boundary type to use when applying a syncTime. The allowed values are 'Inside' and 'Outside'. The default is 'Inside'.
  'timeZone': "timeZone_example", // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetGetInterpolatedAdHoc(webId, opts, (error, data, response) => {
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
 **webId** | [**[String]**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | 
 **endTime** | **String**| An optional end time. The default is &#39;*&#39;. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **filterExpression** | **String**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. | [optional] 
 **includeFilteredValues** | **Boolean**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] 
 **interval** | **String**| The sampling interval, in AFTimeSpan format. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; | [optional] 
 **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39;. | [optional] 
 **syncTime** | **String**| An optional start time anchor, in AFTime format. When specified, interpolated data retrieval will use the sync time as the origin for calculating the interval times. | [optional] 
 **syncTimeBoundaryType** | **String**| An optional string specifying the boundary type to use when applying a syncTime. The allowed values are &#39;Inside&#39; and &#39;Outside&#39;. The default is &#39;Inside&#39;. | [optional] 
 **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetGetInterpolatedAtTimes

> ItemsStreamValues streamSetGetInterpolatedAtTimes(webId, time, opts)

Returns interpolated values of attributes for an element, event frame or attribute at the specified times.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let webId = "webId_example"; // String | The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
let time = ["null"]; // [String] | The timestamp at which to retrieve a interpolated value. Multiple timestamps may be specified with multiple instances of the parameter.
let opts = {
  'categoryName': "categoryName_example", // String | Specify that included attributes must have this category. The default is no category filter.
  'filterExpression': "filterExpression_example", // String | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering.
  'includeFilteredValues': true, // Boolean | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.
  'nameFilter': "nameFilter_example", // String | The name query string used for filtering attributes. The default is no filter.
  'searchFullHierarchy': true, // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'showExcluded': true, // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
  'showHidden': true, // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'.
  'templateName': "templateName_example", // String | Specify that included attributes must be members of this template. The default is no template filter.
  'timeZone': "timeZone_example", // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetGetInterpolatedAtTimes(webId, time, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes. | 
 **time** | [**[String]**](String.md)| The timestamp at which to retrieve a interpolated value. Multiple timestamps may be specified with multiple instances of the parameter. | 
 **categoryName** | **String**| Specify that included attributes must have this category. The default is no category filter. | [optional] 
 **filterExpression** | **String**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. | [optional] 
 **includeFilteredValues** | **Boolean**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] 
 **nameFilter** | **String**| The name query string used for filtering attributes. The default is no filter. | [optional] 
 **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **templateName** | **String**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] 
 **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetGetInterpolatedAtTimesAdHoc

> ItemsStreamValues streamSetGetInterpolatedAtTimesAdHoc(time, webId, opts)

Returns interpolated values of the specified streams at the specified times.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let time = ["null"]; // [String] | The timestamp at which to retrieve a interpolated value. Multiple timestamps may be specified with multiple instances of the parameter.
let webId = ["null"]; // [String] | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
let opts = {
  'filterExpression': "filterExpression_example", // String | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering.
  'includeFilteredValues': true, // Boolean | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'.
  'timeZone': "timeZone_example", // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetGetInterpolatedAtTimesAdHoc(time, webId, opts, (error, data, response) => {
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
 **time** | [**[String]**](String.md)| The timestamp at which to retrieve a interpolated value. Multiple timestamps may be specified with multiple instances of the parameter. | 
 **webId** | [**[String]**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | 
 **filterExpression** | **String**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. | [optional] 
 **includeFilteredValues** | **Boolean**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetGetJoined

> ItemsStreamValues streamSetGetJoined(baseWebId, subordinateWebId, opts)

Returns the base stream&#39;s recorded values and subordinate streams&#39; interpolated values at times matching the recorded values&#39; timestamps.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream. The first stream in the response is always the X-Axis.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let baseWebId = "baseWebId_example"; // String | The ID of the base stream which is used for retrieving the recorded values.
let subordinateWebId = ["null"]; // [String] | The ID of a stream whose values will be joined on the times with the values of the base stream. Multiple streams may be specified with multiple instances of the parameter.
let opts = {
  'boundaryType': "boundaryType_example", // String | An optional value that determines how the times and values of the returned end points are determined. The default is 'Inside'.
  'endTime': "endTime_example", // String | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
  'filterExpression': "filterExpression_example", // String | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. The default is no filtering.
  'includeFilteredValues': true, // Boolean | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.
  'maxCount': 56, // Number | The maximum number of values to be returned. The default is 1000.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'startTime': "startTime_example", // String | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.
  'timeZone': "timeZone_example", // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either place, the PI Web API server time zone will be used.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetGetJoined(baseWebId, subordinateWebId, opts, (error, data, response) => {
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
 **baseWebId** | **String**| The ID of the base stream which is used for retrieving the recorded values. | 
 **subordinateWebId** | [**[String]**](String.md)| The ID of a stream whose values will be joined on the times with the values of the base stream. Multiple streams may be specified with multiple instances of the parameter. | 
 **boundaryType** | **String**| An optional value that determines how the times and values of the returned end points are determined. The default is &#39;Inside&#39;. | [optional] 
 **endTime** | **String**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **filterExpression** | **String**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. The default is no filtering. | [optional] 
 **includeFilteredValues** | **Boolean**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] 
 **maxCount** | **Number**| The maximum number of values to be returned. The default is 1000. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] 
 **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either place, the PI Web API server time zone will be used. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetGetPlot

> ItemsStreamValues streamSetGetPlot(webId, opts)

Returns values of attributes for an element, event frame or attribute over the specified time range suitable for plotting over the number of intervals (typically represents pixels).

For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state). Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let webId = "webId_example"; // String | The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
let opts = {
  'categoryName': "categoryName_example", // String | Specify that included attributes must have this category. The default is no category filter.
  'endTime': "endTime_example", // String | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
  'intervals': 56, // Number | The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is '24'. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state).
  'nameFilter': "nameFilter_example", // String | The name query string used for filtering attributes. The default is no filter.
  'searchFullHierarchy': true, // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'showExcluded': true, // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
  'showHidden': true, // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. 'Name' is the only supported field by which to sort.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'
  'startTime': "startTime_example", // String | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.
  'templateName': "templateName_example", // String | Specify that included attributes must be members of this template. The default is no template filter.
  'timeZone': "timeZone_example", // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetGetPlot(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes. | 
 **categoryName** | **String**| Specify that included attributes must have this category. The default is no category filter. | [optional] 
 **endTime** | **String**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **intervals** | **Number**| The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is &#39;24&#39;. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state). | [optional] 
 **nameFilter** | **String**| The name query string used for filtering attributes. The default is no filter. | [optional] 
 **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; | [optional] 
 **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] 
 **templateName** | **String**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] 
 **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetGetPlotAdHoc

> ItemsStreamValues streamSetGetPlotAdHoc(webId, opts)

Returns values of attributes for the specified streams over the specified time range suitable for plotting over the number of intervals (typically represents pixels).

For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state). Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let webId = ["null"]; // [String] | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
let opts = {
  'endTime': "endTime_example", // String | An optional end time. The default is '*'. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
  'intervals': 56, // Number | The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is '24'. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state).
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. 'Name' is the only supported field by which to sort.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'
  'startTime': "startTime_example", // String | An optional start time. The default is '*-1d'.
  'timeZone': "timeZone_example", // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetGetPlotAdHoc(webId, opts, (error, data, response) => {
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
 **webId** | [**[String]**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | 
 **endTime** | **String**| An optional end time. The default is &#39;*&#39;. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **intervals** | **Number**| The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is &#39;24&#39;. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state). | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; | [optional] 
 **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39;. | [optional] 
 **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetGetRecorded

> ItemsStreamValues streamSetGetRecorded(webId, opts)

Returns recorded values of the attributes for an element, event frame, or attribute.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let webId = "webId_example"; // String | The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
let opts = {
  'boundaryType': "boundaryType_example", // String | An optional value that determines how the times and values of the returned end points are determined. The default is 'Inside'.
  'categoryName': "categoryName_example", // String | Specify that included attributes must have this category. The default is no category filter.
  'endTime': "endTime_example", // String | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
  'filterExpression': "filterExpression_example", // String | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. The default is no filtering.
  'includeFilteredValues': true, // Boolean | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.
  'maxCount': 56, // Number | The maximum number of values to be returned. The default is 1000.
  'nameFilter': "nameFilter_example", // String | The name query string used for filtering attributes. The default is no filter.
  'searchFullHierarchy': true, // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'showExcluded': true, // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
  'showHidden': true, // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. 'Name' is the only supported field by which to sort.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'
  'startTime': "startTime_example", // String | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.
  'templateName': "templateName_example", // String | Specify that included attributes must be members of this template. The default is no template filter.
  'timeZone': "timeZone_example", // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetGetRecorded(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes. | 
 **boundaryType** | **String**| An optional value that determines how the times and values of the returned end points are determined. The default is &#39;Inside&#39;. | [optional] 
 **categoryName** | **String**| Specify that included attributes must have this category. The default is no category filter. | [optional] 
 **endTime** | **String**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **filterExpression** | **String**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. The default is no filtering. | [optional] 
 **includeFilteredValues** | **Boolean**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] 
 **maxCount** | **Number**| The maximum number of values to be returned. The default is 1000. | [optional] 
 **nameFilter** | **String**| The name query string used for filtering attributes. The default is no filter. | [optional] 
 **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; | [optional] 
 **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] 
 **templateName** | **String**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] 
 **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetGetRecordedAdHoc

> ItemsStreamValues streamSetGetRecordedAdHoc(webId, opts)

Returns recorded values of the specified streams.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let webId = ["null"]; // [String] | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
let opts = {
  'boundaryType': "boundaryType_example", // String | An optional value that determines how the times and values of the returned end points are determined. The default is 'Inside'.
  'endTime': "endTime_example", // String | An optional end time. The default is '*'. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
  'filterExpression': "filterExpression_example", // String | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. The default is no filtering.
  'includeFilteredValues': true, // Boolean | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.
  'maxCount': 56, // Number | The maximum number of values to be returned. The default is 1000.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. 'Name' is the only supported field by which to sort.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'
  'startTime': "startTime_example", // String | An optional start time. The default is '*-1d'.
  'timeZone': "timeZone_example", // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetGetRecordedAdHoc(webId, opts, (error, data, response) => {
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
 **webId** | [**[String]**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | 
 **boundaryType** | **String**| An optional value that determines how the times and values of the returned end points are determined. The default is &#39;Inside&#39;. | [optional] 
 **endTime** | **String**| An optional end time. The default is &#39;*&#39;. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **filterExpression** | **String**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. The default is no filtering. | [optional] 
 **includeFilteredValues** | **Boolean**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] 
 **maxCount** | **Number**| The maximum number of values to be returned. The default is 1000. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; | [optional] 
 **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39;. | [optional] 
 **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetGetRecordedAtTime

> ItemsStreamValue streamSetGetRecordedAtTime(webId, time, opts)

Returns recorded values of the attributes for an element, event frame, or attribute.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let webId = "webId_example"; // String | The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
let time = "time_example"; // String | The timestamp at which the values are desired.
let opts = {
  'categoryName': "categoryName_example", // String | Specify that included attributes must have this category. The default is no category filter.
  'nameFilter': "nameFilter_example", // String | The name query string used for filtering attributes. The default is no filter.
  'retrievalMode': "retrievalMode_example", // String | An optional value that determines the values to return when values don't exist at the exact time specified. The default is 'Auto'.
  'searchFullHierarchy': true, // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'showExcluded': true, // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
  'showHidden': true, // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
  'templateName': "templateName_example", // String | Specify that included attributes must be members of this template. The default is no template filter.
  'timeZone': "timeZone_example", // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetGetRecordedAtTime(webId, time, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes. | 
 **time** | **String**| The timestamp at which the values are desired. | 
 **categoryName** | **String**| Specify that included attributes must have this category. The default is no category filter. | [optional] 
 **nameFilter** | **String**| The name query string used for filtering attributes. The default is no filter. | [optional] 
 **retrievalMode** | **String**| An optional value that determines the values to return when values don&#39;t exist at the exact time specified. The default is &#39;Auto&#39;. | [optional] 
 **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **templateName** | **String**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] 
 **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsStreamValue**](ItemsStreamValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetGetRecordedAtTimeAdHoc

> ItemsStreamValue streamSetGetRecordedAtTimeAdHoc(time, webId, opts)

Returns recorded values based on the passed time and retrieval mode.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let time = "time_example"; // String | The timestamp at which the values are desired.
let webId = ["null"]; // [String] | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
let opts = {
  'retrievalMode': "retrievalMode_example", // String | An optional value that determines the values to return when values don't exist at the exact time specified. The default is 'Auto'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'timeZone': "timeZone_example", // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetGetRecordedAtTimeAdHoc(time, webId, opts, (error, data, response) => {
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
 **time** | **String**| The timestamp at which the values are desired. | 
 **webId** | [**[String]**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | 
 **retrievalMode** | **String**| An optional value that determines the values to return when values don&#39;t exist at the exact time specified. The default is &#39;Auto&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsStreamValue**](ItemsStreamValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetGetRecordedAtTimes

> ItemsStreamValues streamSetGetRecordedAtTimes(webId, time, opts)

Returns recorded values of attributes for an element, event frame or attribute at the specified times.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let webId = "webId_example"; // String | The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
let time = ["null"]; // [String] | The timestamp at which to retrieve a recorded value. Multiple timestamps may be specified with multiple instances of the parameter.
let opts = {
  'categoryName': "categoryName_example", // String | Specify that included attributes must have this category. The default is no category filter.
  'nameFilter': "nameFilter_example", // String | The name query string used for filtering attributes. The default is no filter.
  'retrievalMode': "retrievalMode_example", // String | An optional value that determines the values to return when values don't exist at the exact time specified. The default is 'Auto'.
  'searchFullHierarchy': true, // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'showExcluded': true, // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
  'showHidden': true, // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'.
  'templateName': "templateName_example", // String | Specify that included attributes must be members of this template. The default is no template filter.
  'timeZone': "timeZone_example", // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetGetRecordedAtTimes(webId, time, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes. | 
 **time** | [**[String]**](String.md)| The timestamp at which to retrieve a recorded value. Multiple timestamps may be specified with multiple instances of the parameter. | 
 **categoryName** | **String**| Specify that included attributes must have this category. The default is no category filter. | [optional] 
 **nameFilter** | **String**| The name query string used for filtering attributes. The default is no filter. | [optional] 
 **retrievalMode** | **String**| An optional value that determines the values to return when values don&#39;t exist at the exact time specified. The default is &#39;Auto&#39;. | [optional] 
 **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **templateName** | **String**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] 
 **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetGetRecordedAtTimesAdHoc

> ItemsStreamValues streamSetGetRecordedAtTimesAdHoc(time, webId, opts)

Returns recorded values of the specified streams at the specified times.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let time = ["null"]; // [String] | The timestamp at which to retrieve a recorded value. Multiple timestamps may be specified with multiple instances of the parameter.
let webId = ["null"]; // [String] | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
let opts = {
  'retrievalMode': "retrievalMode_example", // String | An optional value that determines the values to return when values don't exist at the exact time specified. The default is 'Auto'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'.
  'timeZone': "timeZone_example", // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetGetRecordedAtTimesAdHoc(time, webId, opts, (error, data, response) => {
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
 **time** | [**[String]**](String.md)| The timestamp at which to retrieve a recorded value. Multiple timestamps may be specified with multiple instances of the parameter. | 
 **webId** | [**[String]**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | 
 **retrievalMode** | **String**| An optional value that determines the values to return when values don&#39;t exist at the exact time specified. The default is &#39;Auto&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetGetSummaries

> ItemsStreamSummaries streamSetGetSummaries(webId, opts)

Returns summary values of the attributes for an element, event frame or attribute.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let webId = "webId_example"; // String | The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
let opts = {
  'calculationBasis': "calculationBasis_example", // String | Specifies the method of evaluating the data over the time range. The default is 'TimeWeighted'.
  'categoryName': "categoryName_example", // String | Specify that included attributes must have this category. The default is no category filter.
  'endTime': "endTime_example", // String | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
  'filterExpression': "filterExpression_example", // String | A string containing a filter expression. Expression variables are relative to the attribute. Use '.' to reference the containing attribute. The default is no filtering.
  'nameFilter': "nameFilter_example", // String | The name query string used for filtering attributes. The default is no filter.
  'sampleInterval': "sampleInterval_example", // String | A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is 'Interval'.
  'sampleType': "sampleType_example", // String | A flag which specifies one or more summaries to compute for each interval over the time range. The default is 'ExpressionRecordedValues'.
  'searchFullHierarchy': true, // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'showExcluded': true, // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
  'showHidden': true, // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
  'startTime': "startTime_example", // String | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.
  'summaryDuration': "summaryDuration_example", // String | The duration of each summary interval.
  'summaryType': ["null"], // [String] | Specifies the kinds of summaries to produce over the range. The default is 'Total'. Multiple summary types may be specified by using multiple instances of summaryType.
  'templateName': "templateName_example", // String | Specify that included attributes must be members of this template. The default is no template filter.
  'timeType': "timeType_example", // String | Specifies how to calculate the timestamp for each interval. The default is 'Auto'.
  'timeZone': "timeZone_example", // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetGetSummaries(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes. | 
 **calculationBasis** | **String**| Specifies the method of evaluating the data over the time range. The default is &#39;TimeWeighted&#39;. | [optional] 
 **categoryName** | **String**| Specify that included attributes must have this category. The default is no category filter. | [optional] 
 **endTime** | **String**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **filterExpression** | **String**| A string containing a filter expression. Expression variables are relative to the attribute. Use &#39;.&#39; to reference the containing attribute. The default is no filtering. | [optional] 
 **nameFilter** | **String**| The name query string used for filtering attributes. The default is no filter. | [optional] 
 **sampleInterval** | **String**| A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is &#39;Interval&#39;. | [optional] 
 **sampleType** | **String**| A flag which specifies one or more summaries to compute for each interval over the time range. The default is &#39;ExpressionRecordedValues&#39;. | [optional] 
 **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] 
 **summaryDuration** | **String**| The duration of each summary interval. | [optional] 
 **summaryType** | [**[String]**](String.md)| Specifies the kinds of summaries to produce over the range. The default is &#39;Total&#39;. Multiple summary types may be specified by using multiple instances of summaryType. | [optional] 
 **templateName** | **String**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] 
 **timeType** | **String**| Specifies how to calculate the timestamp for each interval. The default is &#39;Auto&#39;. | [optional] 
 **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsStreamSummaries**](ItemsStreamSummaries.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetGetSummariesAdHoc

> ItemsStreamSummaries streamSetGetSummariesAdHoc(webId, opts)

Returns summary values of the specified streams.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let webId = ["null"]; // [String] | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
let opts = {
  'calculationBasis': "calculationBasis_example", // String | Specifies the method of evaluating the data over the time range. The default is 'TimeWeighted'.
  'endTime': "endTime_example", // String | An optional end time. The default is '*'. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
  'filterExpression': "filterExpression_example", // String | A string containing a filter expression. Expression variables are relative to the attribute. Use '.' to reference the containing attribute. The default is no filtering.
  'sampleInterval': "sampleInterval_example", // String | A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is 'Interval'.
  'sampleType': "sampleType_example", // String | A flag which specifies one or more summaries to compute for each interval over the time range. The default is 'ExpressionRecordedValues'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'startTime': "startTime_example", // String | An optional start time. The default is '*-1d'.
  'summaryDuration': "summaryDuration_example", // String | The duration of each summary interval.
  'summaryType': ["null"], // [String] | Specifies the kinds of summaries to produce over the range. The default is 'Total'. Multiple summary types may be specified by using multiple instances of summaryType.
  'timeType': "timeType_example", // String | Specifies how to calculate the timestamp for each interval. The default is 'Auto'.
  'timeZone': "timeZone_example", // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetGetSummariesAdHoc(webId, opts, (error, data, response) => {
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
 **webId** | [**[String]**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | 
 **calculationBasis** | **String**| Specifies the method of evaluating the data over the time range. The default is &#39;TimeWeighted&#39;. | [optional] 
 **endTime** | **String**| An optional end time. The default is &#39;*&#39;. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] 
 **filterExpression** | **String**| A string containing a filter expression. Expression variables are relative to the attribute. Use &#39;.&#39; to reference the containing attribute. The default is no filtering. | [optional] 
 **sampleInterval** | **String**| A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is &#39;Interval&#39;. | [optional] 
 **sampleType** | **String**| A flag which specifies one or more summaries to compute for each interval over the time range. The default is &#39;ExpressionRecordedValues&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39;. | [optional] 
 **summaryDuration** | **String**| The duration of each summary interval. | [optional] 
 **summaryType** | [**[String]**](String.md)| Specifies the kinds of summaries to produce over the range. The default is &#39;Total&#39;. Multiple summary types may be specified by using multiple instances of summaryType. | [optional] 
 **timeType** | **String**| Specifies how to calculate the timestamp for each interval. The default is &#39;Auto&#39;. | [optional] 
 **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsStreamSummaries**](ItemsStreamSummaries.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetGetValues

> ItemsStreamValue streamSetGetValues(webId, opts)

Returns values of the attributes for an Element, Event Frame or Attribute at the specified time.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let webId = "webId_example"; // String | The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes.
let opts = {
  'categoryName': "categoryName_example", // String | Specify that included attributes must have this category. The default is no category filter.
  'nameFilter': "nameFilter_example", // String | The name query string used for filtering attributes. The default is no filter.
  'searchFullHierarchy': true, // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'showExcluded': true, // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
  'showHidden': true, // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. 'Name' is the only supported field by which to sort.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'
  'templateName': "templateName_example", // String | Specify that included attributes must be members of this template. The default is no template filter.
  'time': "time_example", // String | An AF time string, which is used as the time context to get stream values if it is provided. By default, it is not specified, and the default time context of the AF object will be used.
  'timeZone': "timeZone_example", // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetGetValues(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes. | 
 **categoryName** | **String**| Specify that included attributes must have this category. The default is no category filter. | [optional] 
 **nameFilter** | **String**| The name query string used for filtering attributes. The default is no filter. | [optional] 
 **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; | [optional] 
 **templateName** | **String**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] 
 **time** | **String**| An AF time string, which is used as the time context to get stream values if it is provided. By default, it is not specified, and the default time context of the AF object will be used. | [optional] 
 **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsStreamValue**](ItemsStreamValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetGetValuesAdHoc

> ItemsStreamValue streamSetGetValuesAdHoc(webId, opts)

Returns values of the specified streams.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let webId = ["null"]; // [String] | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. 'Name' is the only supported field by which to sort.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'
  'time': "time_example", // String | An AF time string, which is used as the time context to get stream values if it is provided. By default, it is not specified, and the default time context of the AF object will be used.
  'timeZone': "timeZone_example", // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetGetValuesAdHoc(webId, opts, (error, data, response) => {
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
 **webId** | [**[String]**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; | [optional] 
 **time** | **String**| An AF time string, which is used as the time context to get stream values if it is provided. By default, it is not specified, and the default time context of the AF object will be used. | [optional] 
 **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsStreamValue**](ItemsStreamValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetRegisterStreamSetUpdates

> ItemsStreamUpdatesRegister streamSetRegisterStreamSetUpdates(webId, opts)

Register for stream updates

The supplied webIds will register for stream updates. For a 200 response, the returned location header will contain the url for retrieving the next set of stream updates.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let webId = ["null"]; // [String] | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetRegisterStreamSetUpdates(webId, opts, (error, data, response) => {
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
 **webId** | [**[String]**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsStreamUpdatesRegister**](ItemsStreamUpdatesRegister.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetRetrieveStreamSetUpdates

> ItemsStreamUpdatesRetrieve streamSetRetrieveStreamSetUpdates(marker, opts)

Receive stream updates

The supplied markers will identify the set of stream updates to retrieve. For a 200 response, the returned location header will contain the url for retrieving the stream updates.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let marker = ["null"]; // [String] | Identifier of stream source and current position. Multiple markers may be specified with multiple instances of the parameter.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.streamSetRetrieveStreamSetUpdates(marker, opts, (error, data, response) => {
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
 **marker** | [**[String]**](String.md)| Identifier of stream source and current position. Multiple markers may be specified with multiple instances of the parameter. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsStreamUpdatesRetrieve**](ItemsStreamUpdatesRetrieve.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetUpdateValue

> ItemsSubstatus streamSetUpdateValue(webId, values, opts)

Updates a single value for the specified streams.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let webId = "webId_example"; // String | The ID of the parent element, event frame, or attribute. Attributes specified in the body must be descendants of the specified object.
let values = [new PiWebApi2018Sp1SwaggerSpec.StreamValue()]; // [StreamValue] | The values to add or update.
let opts = {
  'bufferOption': "bufferOption_example", // String | The desired AFBufferOption. The default is 'BufferIfPossible'.
  'updateOption': "updateOption_example" // String | The desired AFUpdateOption. The default is 'Replace'.
};
apiInstance.streamSetUpdateValue(webId, values, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the parent element, event frame, or attribute. Attributes specified in the body must be descendants of the specified object. | 
 **values** | [**[StreamValue]**](StreamValue.md)| The values to add or update. | 
 **bufferOption** | **String**| The desired AFBufferOption. The default is &#39;BufferIfPossible&#39;. | [optional] 
 **updateOption** | **String**| The desired AFUpdateOption. The default is &#39;Replace&#39;. | [optional] 

### Return type

[**ItemsSubstatus**](ItemsSubstatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetUpdateValueAdHoc

> ItemsSubstatus streamSetUpdateValueAdHoc(values, opts)

Updates a single value for the specified streams.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let values = [new PiWebApi2018Sp1SwaggerSpec.StreamValue()]; // [StreamValue] | The values to add or update.
let opts = {
  'bufferOption': "bufferOption_example", // String | The desired AFBufferOption. The default is 'BufferIfPossible'.
  'updateOption': "updateOption_example" // String | The desired AFUpdateOption. The default is 'Replace'.
};
apiInstance.streamSetUpdateValueAdHoc(values, opts, (error, data, response) => {
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
 **values** | [**[StreamValue]**](StreamValue.md)| The values to add or update. | 
 **bufferOption** | **String**| The desired AFBufferOption. The default is &#39;BufferIfPossible&#39;. | [optional] 
 **updateOption** | **String**| The desired AFUpdateOption. The default is &#39;Replace&#39;. | [optional] 

### Return type

[**ItemsSubstatus**](ItemsSubstatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetUpdateValues

> ItemsItemsSubstatus streamSetUpdateValues(webId, values, opts)

Updates multiple values for the specified streams.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let webId = "webId_example"; // String | The ID of the parent element, event frame, or attribute. Attributes specified in the body must be descendants of the specified object.
let values = [new PiWebApi2018Sp1SwaggerSpec.StreamValues()]; // [StreamValues] | The values to add or update.
let opts = {
  'bufferOption': "bufferOption_example", // String | The desired AFBufferOption. The default is 'BufferIfPossible'.
  'updateOption': "updateOption_example" // String | The desired AFUpdateOption. The default is 'Replace'.
};
apiInstance.streamSetUpdateValues(webId, values, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the parent element, event frame, or attribute. Attributes specified in the body must be descendants of the specified object. | 
 **values** | [**[StreamValues]**](StreamValues.md)| The values to add or update. | 
 **bufferOption** | **String**| The desired AFBufferOption. The default is &#39;BufferIfPossible&#39;. | [optional] 
 **updateOption** | **String**| The desired AFUpdateOption. The default is &#39;Replace&#39;. | [optional] 

### Return type

[**ItemsItemsSubstatus**](ItemsItemsSubstatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## streamSetUpdateValuesAdHoc

> ItemsItemsSubstatus streamSetUpdateValuesAdHoc(values, opts)

Updates multiple values for the specified streams.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.StreamSetApi();
let values = [new PiWebApi2018Sp1SwaggerSpec.StreamValues()]; // [StreamValues] | The values to add or update.
let opts = {
  'bufferOption': "bufferOption_example", // String | The desired AFBufferOption. The default is 'BufferIfPossible'.
  'updateOption': "updateOption_example" // String | The desired AFUpdateOption. The default is 'Replace'.
};
apiInstance.streamSetUpdateValuesAdHoc(values, opts, (error, data, response) => {
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
 **values** | [**[StreamValues]**](StreamValues.md)| The values to add or update. | 
 **bufferOption** | **String**| The desired AFBufferOption. The default is &#39;BufferIfPossible&#39;. | [optional] 
 **updateOption** | **String**| The desired AFUpdateOption. The default is &#39;Replace&#39;. | [optional] 

### Return type

[**ItemsItemsSubstatus**](ItemsItemsSubstatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json, text/html, application/x-ms-application

