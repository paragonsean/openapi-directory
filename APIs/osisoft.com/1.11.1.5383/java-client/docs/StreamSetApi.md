# StreamSetApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**streamSetGetChannel**](StreamSetApi.md#streamSetGetChannel) | **GET** /streamsets/{webId}/channel | Opens a channel that will send messages about any value changes for the attributes of an Element, Event Frame, or Attribute. |
| [**streamSetGetChannelAdHoc**](StreamSetApi.md#streamSetGetChannelAdHoc) | **GET** /streamsets/channel | Opens a channel that will send messages about any value changes for the specified streams. |
| [**streamSetGetEnd**](StreamSetApi.md#streamSetGetEnd) | **GET** /streamsets/{webId}/end | Returns End of stream values of the attributes for an Element, Event Frame or Attribute |
| [**streamSetGetEndAdHoc**](StreamSetApi.md#streamSetGetEndAdHoc) | **GET** /streamsets/end | Returns End Of Stream values for attributes of the specified streams |
| [**streamSetGetInterpolated**](StreamSetApi.md#streamSetGetInterpolated) | **GET** /streamsets/{webId}/interpolated | Returns interpolated values of attributes for an element, event frame or attribute over the specified time range at the specified sampling interval. |
| [**streamSetGetInterpolatedAdHoc**](StreamSetApi.md#streamSetGetInterpolatedAdHoc) | **GET** /streamsets/interpolated | Returns interpolated values of the specified streams over the specified time range at the specified sampling interval. |
| [**streamSetGetInterpolatedAtTimes**](StreamSetApi.md#streamSetGetInterpolatedAtTimes) | **GET** /streamsets/{webId}/interpolatedattimes | Returns interpolated values of attributes for an element, event frame or attribute at the specified times. |
| [**streamSetGetInterpolatedAtTimesAdHoc**](StreamSetApi.md#streamSetGetInterpolatedAtTimesAdHoc) | **GET** /streamsets/interpolatedattimes | Returns interpolated values of the specified streams at the specified times. |
| [**streamSetGetJoined**](StreamSetApi.md#streamSetGetJoined) | **GET** /streamsets/joined | Returns the base stream&#39;s recorded values and subordinate streams&#39; interpolated values at times matching the recorded values&#39; timestamps. |
| [**streamSetGetPlot**](StreamSetApi.md#streamSetGetPlot) | **GET** /streamsets/{webId}/plot | Returns values of attributes for an element, event frame or attribute over the specified time range suitable for plotting over the number of intervals (typically represents pixels). |
| [**streamSetGetPlotAdHoc**](StreamSetApi.md#streamSetGetPlotAdHoc) | **GET** /streamsets/plot | Returns values of attributes for the specified streams over the specified time range suitable for plotting over the number of intervals (typically represents pixels). |
| [**streamSetGetRecorded**](StreamSetApi.md#streamSetGetRecorded) | **GET** /streamsets/{webId}/recorded | Returns recorded values of the attributes for an element, event frame, or attribute. |
| [**streamSetGetRecordedAdHoc**](StreamSetApi.md#streamSetGetRecordedAdHoc) | **GET** /streamsets/recorded | Returns recorded values of the specified streams. |
| [**streamSetGetRecordedAtTime**](StreamSetApi.md#streamSetGetRecordedAtTime) | **GET** /streamsets/{webId}/recordedattime | Returns recorded values of the attributes for an element, event frame, or attribute. |
| [**streamSetGetRecordedAtTimeAdHoc**](StreamSetApi.md#streamSetGetRecordedAtTimeAdHoc) | **GET** /streamsets/recordedattime | Returns recorded values based on the passed time and retrieval mode. |
| [**streamSetGetRecordedAtTimes**](StreamSetApi.md#streamSetGetRecordedAtTimes) | **GET** /streamsets/{webId}/recordedattimes | Returns recorded values of attributes for an element, event frame or attribute at the specified times. |
| [**streamSetGetRecordedAtTimesAdHoc**](StreamSetApi.md#streamSetGetRecordedAtTimesAdHoc) | **GET** /streamsets/recordedattimes | Returns recorded values of the specified streams at the specified times. |
| [**streamSetGetSummaries**](StreamSetApi.md#streamSetGetSummaries) | **GET** /streamsets/{webId}/summary | Returns summary values of the attributes for an element, event frame or attribute. |
| [**streamSetGetSummariesAdHoc**](StreamSetApi.md#streamSetGetSummariesAdHoc) | **GET** /streamsets/summary | Returns summary values of the specified streams. |
| [**streamSetGetValues**](StreamSetApi.md#streamSetGetValues) | **GET** /streamsets/{webId}/value | Returns values of the attributes for an Element, Event Frame or Attribute at the specified time. |
| [**streamSetGetValuesAdHoc**](StreamSetApi.md#streamSetGetValuesAdHoc) | **GET** /streamsets/value | Returns values of the specified streams. |
| [**streamSetRegisterStreamSetUpdates**](StreamSetApi.md#streamSetRegisterStreamSetUpdates) | **POST** /streamsets/updates | Register for stream updates |
| [**streamSetRetrieveStreamSetUpdates**](StreamSetApi.md#streamSetRetrieveStreamSetUpdates) | **GET** /streamsets/updates | Receive stream updates |
| [**streamSetUpdateValue**](StreamSetApi.md#streamSetUpdateValue) | **POST** /streamsets/{webId}/value | Updates a single value for the specified streams. |
| [**streamSetUpdateValueAdHoc**](StreamSetApi.md#streamSetUpdateValueAdHoc) | **POST** /streamsets/value | Updates a single value for the specified streams. |
| [**streamSetUpdateValues**](StreamSetApi.md#streamSetUpdateValues) | **POST** /streamsets/{webId}/recorded | Updates multiple values for the specified streams. |
| [**streamSetUpdateValuesAdHoc**](StreamSetApi.md#streamSetUpdateValuesAdHoc) | **POST** /streamsets/recorded | Updates multiple values for the specified streams. |


<a id="streamSetGetChannel"></a>
# **streamSetGetChannel**
> streamSetGetChannel(webId, categoryName, heartbeatRate, includeInitialValues, nameFilter, searchFullHierarchy, showExcluded, showHidden, templateName, webIdType)

Opens a channel that will send messages about any value changes for the attributes of an Element, Event Frame, or Attribute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    String webId = "webId_example"; // String | The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes.
    String categoryName = "categoryName_example"; // String | Specify that included attributes must have this category. The default is no category filter.
    Integer heartbeatRate = 56; // Integer | Specifies the maximum number of consecutive empty messages that can be elapsed with no new data updates from the PI System, after which the client receives an empty payload. It helps to check if the connection is still alive. Zero/negative values correspond to no heartbeat, and the default value is no heartbeat.
    Boolean includeInitialValues = true; // Boolean | Specified if the channel should send a message with the current values of all the streams after the connection is opened. The default is 'false'.
    String nameFilter = "nameFilter_example"; // String | The name query string used for filtering attributes. The default is no filter.
    Boolean searchFullHierarchy = true; // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
    Boolean showExcluded = true; // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
    Boolean showHidden = true; // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
    String templateName = "templateName_example"; // String | Specify that included attributes must be members of this template. The default is no template filter.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.streamSetGetChannel(webId, categoryName, heartbeatRate, includeInitialValues, nameFilter, searchFullHierarchy, showExcluded, showHidden, templateName, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetGetChannel");
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
| **webId** | **String**| The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes. | |
| **categoryName** | **String**| Specify that included attributes must have this category. The default is no category filter. | [optional] |
| **heartbeatRate** | **Integer**| Specifies the maximum number of consecutive empty messages that can be elapsed with no new data updates from the PI System, after which the client receives an empty payload. It helps to check if the connection is still alive. Zero/negative values correspond to no heartbeat, and the default value is no heartbeat. | [optional] |
| **includeInitialValues** | **Boolean**| Specified if the channel should send a message with the current values of all the streams after the connection is opened. The default is &#39;false&#39;. | [optional] |
| **nameFilter** | **String**| The name query string used for filtering attributes. The default is no filter. | [optional] |
| **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] |
| **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] |
| **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] |
| **templateName** | **String**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **101** | Switches to the Web Socket protocol. |  -  |
| **409** | Unsupported operation on the given AF object. |  -  |

<a id="streamSetGetChannelAdHoc"></a>
# **streamSetGetChannelAdHoc**
> streamSetGetChannelAdHoc(webId, heartbeatRate, includeInitialValues, webIdType)

Opens a channel that will send messages about any value changes for the specified streams.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    List<String> webId = Arrays.asList(); // List<String> | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    Integer heartbeatRate = 56; // Integer | Specifies the maximum number of consecutive empty messages that can be elapsed with no new data updates from the PI System, after which the client receives an empty payload. It helps to check if the connection is still alive. Zero/negative values correspond to no heartbeat, and the default value is no heartbeat.
    Boolean includeInitialValues = true; // Boolean | Specified if the channel should send a message with the current values of all the streams after the connection is opened. The default is 'false'.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.streamSetGetChannelAdHoc(webId, heartbeatRate, includeInitialValues, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetGetChannelAdHoc");
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
| **webId** | [**List&lt;String&gt;**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | |
| **heartbeatRate** | **Integer**| Specifies the maximum number of consecutive empty messages that can be elapsed with no new data updates from the PI System, after which the client receives an empty payload. It helps to check if the connection is still alive. Zero/negative values correspond to no heartbeat, and the default value is no heartbeat. | [optional] |
| **includeInitialValues** | **Boolean**| Specified if the channel should send a message with the current values of all the streams after the connection is opened. The default is &#39;false&#39;. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **101** | Switches to the Web Socket protocol. |  -  |

<a id="streamSetGetEnd"></a>
# **streamSetGetEnd**
> ItemsStreamValue streamSetGetEnd(webId, categoryName, nameFilter, searchFullHierarchy, selectedFields, showExcluded, showHidden, sortField, sortOrder, templateName, webIdType)

Returns End of stream values of the attributes for an Element, Event Frame or Attribute

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    String webId = "webId_example"; // String | The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes.
    String categoryName = "categoryName_example"; // String | Specify that included attributes must have this category. The default is no category filter.
    String nameFilter = "nameFilter_example"; // String | The name query string used for filtering attributes. The default is no filter.
    Boolean searchFullHierarchy = true; // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    Boolean showExcluded = true; // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
    Boolean showHidden = true; // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. 'Name' is the only supported field by which to sort.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'
    String templateName = "templateName_example"; // String | Specify that included attributes must be members of this template. The default is no template filter.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsStreamValue result = apiInstance.streamSetGetEnd(webId, categoryName, nameFilter, searchFullHierarchy, selectedFields, showExcluded, showHidden, sortField, sortOrder, templateName, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetGetEnd");
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
| **webId** | **String**| The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes. | |
| **categoryName** | **String**| Specify that included attributes must have this category. The default is no category filter. | [optional] |
| **nameFilter** | **String**| The name query string used for filtering attributes. The default is no filter. | [optional] |
| **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] |
| **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; | [optional] |
| **templateName** | **String**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsStreamValue**](ItemsStreamValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary values of the streams that meet the specified conditions. |  -  |
| **409** | Unsupported operation on the given AF object. |  -  |

<a id="streamSetGetEndAdHoc"></a>
# **streamSetGetEndAdHoc**
> ItemsStreamValues streamSetGetEndAdHoc(webId, selectedFields, sortField, sortOrder, webIdType)

Returns End Of Stream values for attributes of the specified streams

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    List<String> webId = Arrays.asList(); // List<String> | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. 'Name' is the only supported field by which to sort.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsStreamValues result = apiInstance.streamSetGetEndAdHoc(webId, selectedFields, sortField, sortOrder, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetGetEndAdHoc");
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
| **webId** | [**List&lt;String&gt;**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | End of stream values of the streams that meet the specified conditions. |  -  |

<a id="streamSetGetInterpolated"></a>
# **streamSetGetInterpolated**
> ItemsStreamValues streamSetGetInterpolated(webId, categoryName, endTime, filterExpression, includeFilteredValues, interval, nameFilter, searchFullHierarchy, selectedFields, showExcluded, showHidden, sortField, sortOrder, startTime, syncTime, syncTimeBoundaryType, templateName, timeZone, webIdType)

Returns interpolated values of attributes for an element, event frame or attribute over the specified time range at the specified sampling interval.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    String webId = "webId_example"; // String | The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
    String categoryName = "categoryName_example"; // String | Specify that included attributes must have this category. The default is no category filter.
    String endTime = "endTime_example"; // String | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    String filterExpression = "filterExpression_example"; // String | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering.
    Boolean includeFilteredValues = true; // Boolean | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.
    String interval = "interval_example"; // String | The sampling interval, in AFTimeSpan format.
    String nameFilter = "nameFilter_example"; // String | The name query string used for filtering attributes. The default is no filter.
    Boolean searchFullHierarchy = true; // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    Boolean showExcluded = true; // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
    Boolean showHidden = true; // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. 'Name' is the only supported field by which to sort.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'.
    String startTime = "startTime_example"; // String | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.
    String syncTime = "syncTime_example"; // String | An optional start time anchor, in AFTime format. When specified, interpolated data retrieval will use the sync time as the origin for calculating the interval times.
    String syncTimeBoundaryType = "syncTimeBoundaryType_example"; // String | An optional string specifying the boundary type to use when applying a syncTime. The allowed values are 'Inside' and 'Outside'. The default is 'Inside'.
    String templateName = "templateName_example"; // String | Specify that included attributes must be members of this template. The default is no template filter.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsStreamValues result = apiInstance.streamSetGetInterpolated(webId, categoryName, endTime, filterExpression, includeFilteredValues, interval, nameFilter, searchFullHierarchy, selectedFields, showExcluded, showHidden, sortField, sortOrder, startTime, syncTime, syncTimeBoundaryType, templateName, timeZone, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetGetInterpolated");
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
| **webId** | **String**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes. | |
| **categoryName** | **String**| Specify that included attributes must have this category. The default is no category filter. | [optional] |
| **endTime** | **String**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] |
| **filterExpression** | **String**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. | [optional] |
| **includeFilteredValues** | **Boolean**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] |
| **interval** | **String**| The sampling interval, in AFTimeSpan format. | [optional] |
| **nameFilter** | **String**| The name query string used for filtering attributes. The default is no filter. | [optional] |
| **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] |
| **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] |
| **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] |
| **syncTime** | **String**| An optional start time anchor, in AFTime format. When specified, interpolated data retrieval will use the sync time as the origin for calculating the interval times. | [optional] |
| **syncTimeBoundaryType** | **String**| An optional string specifying the boundary type to use when applying a syncTime. The allowed values are &#39;Inside&#39; and &#39;Outside&#39;. The default is &#39;Inside&#39;. | [optional] |
| **templateName** | **String**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Interpolated values of the streams that meet the specified conditions. |  -  |

<a id="streamSetGetInterpolatedAdHoc"></a>
# **streamSetGetInterpolatedAdHoc**
> ItemsStreamValues streamSetGetInterpolatedAdHoc(webId, endTime, filterExpression, includeFilteredValues, interval, selectedFields, sortField, sortOrder, startTime, syncTime, syncTimeBoundaryType, timeZone, webIdType)

Returns interpolated values of the specified streams over the specified time range at the specified sampling interval.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    List<String> webId = Arrays.asList(); // List<String> | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    String endTime = "endTime_example"; // String | An optional end time. The default is '*'. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    String filterExpression = "filterExpression_example"; // String | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering.
    Boolean includeFilteredValues = true; // Boolean | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.
    String interval = "interval_example"; // String | The sampling interval, in AFTimeSpan format.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. 'Name' is the only supported field by which to sort.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'
    String startTime = "startTime_example"; // String | An optional start time. The default is '*-1d'.
    String syncTime = "syncTime_example"; // String | An optional start time anchor, in AFTime format. When specified, interpolated data retrieval will use the sync time as the origin for calculating the interval times.
    String syncTimeBoundaryType = "syncTimeBoundaryType_example"; // String | An optional string specifying the boundary type to use when applying a syncTime. The allowed values are 'Inside' and 'Outside'. The default is 'Inside'.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsStreamValues result = apiInstance.streamSetGetInterpolatedAdHoc(webId, endTime, filterExpression, includeFilteredValues, interval, selectedFields, sortField, sortOrder, startTime, syncTime, syncTimeBoundaryType, timeZone, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetGetInterpolatedAdHoc");
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
| **webId** | [**List&lt;String&gt;**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | |
| **endTime** | **String**| An optional end time. The default is &#39;*&#39;. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] |
| **filterExpression** | **String**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. | [optional] |
| **includeFilteredValues** | **Boolean**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] |
| **interval** | **String**| The sampling interval, in AFTimeSpan format. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; | [optional] |
| **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39;. | [optional] |
| **syncTime** | **String**| An optional start time anchor, in AFTime format. When specified, interpolated data retrieval will use the sync time as the origin for calculating the interval times. | [optional] |
| **syncTimeBoundaryType** | **String**| An optional string specifying the boundary type to use when applying a syncTime. The allowed values are &#39;Inside&#39; and &#39;Outside&#39;. The default is &#39;Inside&#39;. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Interpolated values of the streams that meet the specified conditions. |  -  |

<a id="streamSetGetInterpolatedAtTimes"></a>
# **streamSetGetInterpolatedAtTimes**
> ItemsStreamValues streamSetGetInterpolatedAtTimes(webId, time, categoryName, filterExpression, includeFilteredValues, nameFilter, searchFullHierarchy, selectedFields, showExcluded, showHidden, sortOrder, templateName, timeZone, webIdType)

Returns interpolated values of attributes for an element, event frame or attribute at the specified times.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    String webId = "webId_example"; // String | The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
    List<String> time = Arrays.asList(); // List<String> | The timestamp at which to retrieve a interpolated value. Multiple timestamps may be specified with multiple instances of the parameter.
    String categoryName = "categoryName_example"; // String | Specify that included attributes must have this category. The default is no category filter.
    String filterExpression = "filterExpression_example"; // String | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering.
    Boolean includeFilteredValues = true; // Boolean | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.
    String nameFilter = "nameFilter_example"; // String | The name query string used for filtering attributes. The default is no filter.
    Boolean searchFullHierarchy = true; // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    Boolean showExcluded = true; // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
    Boolean showHidden = true; // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'.
    String templateName = "templateName_example"; // String | Specify that included attributes must be members of this template. The default is no template filter.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsStreamValues result = apiInstance.streamSetGetInterpolatedAtTimes(webId, time, categoryName, filterExpression, includeFilteredValues, nameFilter, searchFullHierarchy, selectedFields, showExcluded, showHidden, sortOrder, templateName, timeZone, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetGetInterpolatedAtTimes");
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
| **webId** | **String**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes. | |
| **time** | [**List&lt;String&gt;**](String.md)| The timestamp at which to retrieve a interpolated value. Multiple timestamps may be specified with multiple instances of the parameter. | |
| **categoryName** | **String**| Specify that included attributes must have this category. The default is no category filter. | [optional] |
| **filterExpression** | **String**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. | [optional] |
| **includeFilteredValues** | **Boolean**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] |
| **nameFilter** | **String**| The name query string used for filtering attributes. The default is no filter. | [optional] |
| **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] |
| **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] |
| **templateName** | **String**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Interpolated values of the streams that meet the specified conditions. |  -  |
| **400** | The request was malformed. |  -  |
| **502** | The request was cancelled. |  -  |

<a id="streamSetGetInterpolatedAtTimesAdHoc"></a>
# **streamSetGetInterpolatedAtTimesAdHoc**
> ItemsStreamValues streamSetGetInterpolatedAtTimesAdHoc(time, webId, filterExpression, includeFilteredValues, selectedFields, sortOrder, timeZone, webIdType)

Returns interpolated values of the specified streams at the specified times.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    List<String> time = Arrays.asList(); // List<String> | The timestamp at which to retrieve a interpolated value. Multiple timestamps may be specified with multiple instances of the parameter.
    List<String> webId = Arrays.asList(); // List<String> | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    String filterExpression = "filterExpression_example"; // String | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering.
    Boolean includeFilteredValues = true; // Boolean | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsStreamValues result = apiInstance.streamSetGetInterpolatedAtTimesAdHoc(time, webId, filterExpression, includeFilteredValues, selectedFields, sortOrder, timeZone, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetGetInterpolatedAtTimesAdHoc");
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
| **time** | [**List&lt;String&gt;**](String.md)| The timestamp at which to retrieve a interpolated value. Multiple timestamps may be specified with multiple instances of the parameter. | |
| **webId** | [**List&lt;String&gt;**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | |
| **filterExpression** | **String**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. | [optional] |
| **includeFilteredValues** | **Boolean**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Interpolated values of the streams that meet the specified conditions. |  -  |
| **400** | The request was malformed. |  -  |
| **502** | The request was cancelled. |  -  |

<a id="streamSetGetJoined"></a>
# **streamSetGetJoined**
> ItemsStreamValues streamSetGetJoined(baseWebId, subordinateWebId, boundaryType, endTime, filterExpression, includeFilteredValues, maxCount, selectedFields, startTime, timeZone, webIdType)

Returns the base stream&#39;s recorded values and subordinate streams&#39; interpolated values at times matching the recorded values&#39; timestamps.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream. The first stream in the response is always the X-Axis.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    String baseWebId = "baseWebId_example"; // String | The ID of the base stream which is used for retrieving the recorded values.
    List<String> subordinateWebId = Arrays.asList(); // List<String> | The ID of a stream whose values will be joined on the times with the values of the base stream. Multiple streams may be specified with multiple instances of the parameter.
    String boundaryType = "boundaryType_example"; // String | An optional value that determines how the times and values of the returned end points are determined. The default is 'Inside'.
    String endTime = "endTime_example"; // String | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    String filterExpression = "filterExpression_example"; // String | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. The default is no filtering.
    Boolean includeFilteredValues = true; // Boolean | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.
    Integer maxCount = 56; // Integer | The maximum number of values to be returned. The default is 1000.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String startTime = "startTime_example"; // String | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either place, the PI Web API server time zone will be used.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsStreamValues result = apiInstance.streamSetGetJoined(baseWebId, subordinateWebId, boundaryType, endTime, filterExpression, includeFilteredValues, maxCount, selectedFields, startTime, timeZone, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetGetJoined");
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
| **baseWebId** | **String**| The ID of the base stream which is used for retrieving the recorded values. | |
| **subordinateWebId** | [**List&lt;String&gt;**](String.md)| The ID of a stream whose values will be joined on the times with the values of the base stream. Multiple streams may be specified with multiple instances of the parameter. | |
| **boundaryType** | **String**| An optional value that determines how the times and values of the returned end points are determined. The default is &#39;Inside&#39;. | [optional] |
| **endTime** | **String**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] |
| **filterExpression** | **String**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. The default is no filtering. | [optional] |
| **includeFilteredValues** | **Boolean**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] |
| **maxCount** | **Integer**| The maximum number of values to be returned. The default is 1000. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either place, the PI Web API server time zone will be used. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recorded values of the streams that meet the specified conditions. |  -  |
| **409** | Unsupported operation on the given AF object. |  -  |

<a id="streamSetGetPlot"></a>
# **streamSetGetPlot**
> ItemsStreamValues streamSetGetPlot(webId, categoryName, endTime, intervals, nameFilter, searchFullHierarchy, selectedFields, showExcluded, showHidden, sortField, sortOrder, startTime, templateName, timeZone, webIdType)

Returns values of attributes for an element, event frame or attribute over the specified time range suitable for plotting over the number of intervals (typically represents pixels).

For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state). Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    String webId = "webId_example"; // String | The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
    String categoryName = "categoryName_example"; // String | Specify that included attributes must have this category. The default is no category filter.
    String endTime = "endTime_example"; // String | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    Integer intervals = 56; // Integer | The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is '24'. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state).
    String nameFilter = "nameFilter_example"; // String | The name query string used for filtering attributes. The default is no filter.
    Boolean searchFullHierarchy = true; // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    Boolean showExcluded = true; // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
    Boolean showHidden = true; // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. 'Name' is the only supported field by which to sort.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'
    String startTime = "startTime_example"; // String | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.
    String templateName = "templateName_example"; // String | Specify that included attributes must be members of this template. The default is no template filter.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsStreamValues result = apiInstance.streamSetGetPlot(webId, categoryName, endTime, intervals, nameFilter, searchFullHierarchy, selectedFields, showExcluded, showHidden, sortField, sortOrder, startTime, templateName, timeZone, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetGetPlot");
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
| **webId** | **String**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes. | |
| **categoryName** | **String**| Specify that included attributes must have this category. The default is no category filter. | [optional] |
| **endTime** | **String**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] |
| **intervals** | **Integer**| The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is &#39;24&#39;. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state). | [optional] |
| **nameFilter** | **String**| The name query string used for filtering attributes. The default is no filter. | [optional] |
| **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] |
| **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; | [optional] |
| **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] |
| **templateName** | **String**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Plot values of the streams that meet the specified conditions. |  -  |
| **409** | Unsupported operation on the given AF object. |  -  |

<a id="streamSetGetPlotAdHoc"></a>
# **streamSetGetPlotAdHoc**
> ItemsStreamValues streamSetGetPlotAdHoc(webId, endTime, intervals, selectedFields, sortField, sortOrder, startTime, timeZone, webIdType)

Returns values of attributes for the specified streams over the specified time range suitable for plotting over the number of intervals (typically represents pixels).

For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state). Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    List<String> webId = Arrays.asList(); // List<String> | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    String endTime = "endTime_example"; // String | An optional end time. The default is '*'. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    Integer intervals = 56; // Integer | The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is '24'. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state).
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. 'Name' is the only supported field by which to sort.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'
    String startTime = "startTime_example"; // String | An optional start time. The default is '*-1d'.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsStreamValues result = apiInstance.streamSetGetPlotAdHoc(webId, endTime, intervals, selectedFields, sortField, sortOrder, startTime, timeZone, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetGetPlotAdHoc");
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
| **webId** | [**List&lt;String&gt;**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | |
| **endTime** | **String**| An optional end time. The default is &#39;*&#39;. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] |
| **intervals** | **Integer**| The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is &#39;24&#39;. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state). | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; | [optional] |
| **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39;. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Plot values of the streams that meet the specified conditions. |  -  |
| **409** | Unsupported operation on the given AF object. |  -  |

<a id="streamSetGetRecorded"></a>
# **streamSetGetRecorded**
> ItemsStreamValues streamSetGetRecorded(webId, boundaryType, categoryName, endTime, filterExpression, includeFilteredValues, maxCount, nameFilter, searchFullHierarchy, selectedFields, showExcluded, showHidden, sortField, sortOrder, startTime, templateName, timeZone, webIdType)

Returns recorded values of the attributes for an element, event frame, or attribute.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    String webId = "webId_example"; // String | The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
    String boundaryType = "boundaryType_example"; // String | An optional value that determines how the times and values of the returned end points are determined. The default is 'Inside'.
    String categoryName = "categoryName_example"; // String | Specify that included attributes must have this category. The default is no category filter.
    String endTime = "endTime_example"; // String | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    String filterExpression = "filterExpression_example"; // String | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. The default is no filtering.
    Boolean includeFilteredValues = true; // Boolean | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.
    Integer maxCount = 56; // Integer | The maximum number of values to be returned. The default is 1000.
    String nameFilter = "nameFilter_example"; // String | The name query string used for filtering attributes. The default is no filter.
    Boolean searchFullHierarchy = true; // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    Boolean showExcluded = true; // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
    Boolean showHidden = true; // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. 'Name' is the only supported field by which to sort.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'
    String startTime = "startTime_example"; // String | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.
    String templateName = "templateName_example"; // String | Specify that included attributes must be members of this template. The default is no template filter.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsStreamValues result = apiInstance.streamSetGetRecorded(webId, boundaryType, categoryName, endTime, filterExpression, includeFilteredValues, maxCount, nameFilter, searchFullHierarchy, selectedFields, showExcluded, showHidden, sortField, sortOrder, startTime, templateName, timeZone, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetGetRecorded");
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
| **webId** | **String**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes. | |
| **boundaryType** | **String**| An optional value that determines how the times and values of the returned end points are determined. The default is &#39;Inside&#39;. | [optional] |
| **categoryName** | **String**| Specify that included attributes must have this category. The default is no category filter. | [optional] |
| **endTime** | **String**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] |
| **filterExpression** | **String**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. The default is no filtering. | [optional] |
| **includeFilteredValues** | **Boolean**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] |
| **maxCount** | **Integer**| The maximum number of values to be returned. The default is 1000. | [optional] |
| **nameFilter** | **String**| The name query string used for filtering attributes. The default is no filter. | [optional] |
| **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] |
| **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; | [optional] |
| **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] |
| **templateName** | **String**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recorded values of the streams that meet the specified conditions. |  -  |
| **409** | Unsupported operation on the given AF object. |  -  |

<a id="streamSetGetRecordedAdHoc"></a>
# **streamSetGetRecordedAdHoc**
> ItemsStreamValues streamSetGetRecordedAdHoc(webId, boundaryType, endTime, filterExpression, includeFilteredValues, maxCount, selectedFields, sortField, sortOrder, startTime, timeZone, webIdType)

Returns recorded values of the specified streams.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    List<String> webId = Arrays.asList(); // List<String> | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    String boundaryType = "boundaryType_example"; // String | An optional value that determines how the times and values of the returned end points are determined. The default is 'Inside'.
    String endTime = "endTime_example"; // String | An optional end time. The default is '*'. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    String filterExpression = "filterExpression_example"; // String | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. The default is no filtering.
    Boolean includeFilteredValues = true; // Boolean | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.
    Integer maxCount = 56; // Integer | The maximum number of values to be returned. The default is 1000.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. 'Name' is the only supported field by which to sort.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'
    String startTime = "startTime_example"; // String | An optional start time. The default is '*-1d'.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsStreamValues result = apiInstance.streamSetGetRecordedAdHoc(webId, boundaryType, endTime, filterExpression, includeFilteredValues, maxCount, selectedFields, sortField, sortOrder, startTime, timeZone, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetGetRecordedAdHoc");
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
| **webId** | [**List&lt;String&gt;**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | |
| **boundaryType** | **String**| An optional value that determines how the times and values of the returned end points are determined. The default is &#39;Inside&#39;. | [optional] |
| **endTime** | **String**| An optional end time. The default is &#39;*&#39;. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] |
| **filterExpression** | **String**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. The default is no filtering. | [optional] |
| **includeFilteredValues** | **Boolean**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] |
| **maxCount** | **Integer**| The maximum number of values to be returned. The default is 1000. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; | [optional] |
| **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39;. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recorded values of the streams that meet the specified conditions. |  -  |
| **409** | Unsupported operation on the given AF object. |  -  |

<a id="streamSetGetRecordedAtTime"></a>
# **streamSetGetRecordedAtTime**
> ItemsStreamValue streamSetGetRecordedAtTime(webId, time, categoryName, nameFilter, retrievalMode, searchFullHierarchy, selectedFields, showExcluded, showHidden, templateName, timeZone, webIdType)

Returns recorded values of the attributes for an element, event frame, or attribute.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    String webId = "webId_example"; // String | The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
    String time = "time_example"; // String | The timestamp at which the values are desired.
    String categoryName = "categoryName_example"; // String | Specify that included attributes must have this category. The default is no category filter.
    String nameFilter = "nameFilter_example"; // String | The name query string used for filtering attributes. The default is no filter.
    String retrievalMode = "retrievalMode_example"; // String | An optional value that determines the values to return when values don't exist at the exact time specified. The default is 'Auto'.
    Boolean searchFullHierarchy = true; // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    Boolean showExcluded = true; // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
    Boolean showHidden = true; // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
    String templateName = "templateName_example"; // String | Specify that included attributes must be members of this template. The default is no template filter.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsStreamValue result = apiInstance.streamSetGetRecordedAtTime(webId, time, categoryName, nameFilter, retrievalMode, searchFullHierarchy, selectedFields, showExcluded, showHidden, templateName, timeZone, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetGetRecordedAtTime");
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
| **webId** | **String**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes. | |
| **time** | **String**| The timestamp at which the values are desired. | |
| **categoryName** | **String**| Specify that included attributes must have this category. The default is no category filter. | [optional] |
| **nameFilter** | **String**| The name query string used for filtering attributes. The default is no filter. | [optional] |
| **retrievalMode** | **String**| An optional value that determines the values to return when values don&#39;t exist at the exact time specified. The default is &#39;Auto&#39;. | [optional] |
| **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] |
| **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] |
| **templateName** | **String**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsStreamValue**](ItemsStreamValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recorded values of the streams that meet the specified conditions. |  -  |
| **409** | Unsupported operation on the given AF object. |  -  |

<a id="streamSetGetRecordedAtTimeAdHoc"></a>
# **streamSetGetRecordedAtTimeAdHoc**
> ItemsStreamValue streamSetGetRecordedAtTimeAdHoc(time, webId, retrievalMode, selectedFields, timeZone, webIdType)

Returns recorded values based on the passed time and retrieval mode.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    String time = "time_example"; // String | The timestamp at which the values are desired.
    List<String> webId = Arrays.asList(); // List<String> | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    String retrievalMode = "retrievalMode_example"; // String | An optional value that determines the values to return when values don't exist at the exact time specified. The default is 'Auto'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsStreamValue result = apiInstance.streamSetGetRecordedAtTimeAdHoc(time, webId, retrievalMode, selectedFields, timeZone, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetGetRecordedAtTimeAdHoc");
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
| **time** | **String**| The timestamp at which the values are desired. | |
| **webId** | [**List&lt;String&gt;**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | |
| **retrievalMode** | **String**| An optional value that determines the values to return when values don&#39;t exist at the exact time specified. The default is &#39;Auto&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsStreamValue**](ItemsStreamValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recorded values of the streams that meet the specified conditions. |  -  |
| **409** | Unsupported operation on the given AF object. |  -  |

<a id="streamSetGetRecordedAtTimes"></a>
# **streamSetGetRecordedAtTimes**
> ItemsStreamValues streamSetGetRecordedAtTimes(webId, time, categoryName, nameFilter, retrievalMode, searchFullHierarchy, selectedFields, showExcluded, showHidden, sortOrder, templateName, timeZone, webIdType)

Returns recorded values of attributes for an element, event frame or attribute at the specified times.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    String webId = "webId_example"; // String | The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
    List<String> time = Arrays.asList(); // List<String> | The timestamp at which to retrieve a recorded value. Multiple timestamps may be specified with multiple instances of the parameter.
    String categoryName = "categoryName_example"; // String | Specify that included attributes must have this category. The default is no category filter.
    String nameFilter = "nameFilter_example"; // String | The name query string used for filtering attributes. The default is no filter.
    String retrievalMode = "retrievalMode_example"; // String | An optional value that determines the values to return when values don't exist at the exact time specified. The default is 'Auto'.
    Boolean searchFullHierarchy = true; // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    Boolean showExcluded = true; // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
    Boolean showHidden = true; // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'.
    String templateName = "templateName_example"; // String | Specify that included attributes must be members of this template. The default is no template filter.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsStreamValues result = apiInstance.streamSetGetRecordedAtTimes(webId, time, categoryName, nameFilter, retrievalMode, searchFullHierarchy, selectedFields, showExcluded, showHidden, sortOrder, templateName, timeZone, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetGetRecordedAtTimes");
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
| **webId** | **String**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes. | |
| **time** | [**List&lt;String&gt;**](String.md)| The timestamp at which to retrieve a recorded value. Multiple timestamps may be specified with multiple instances of the parameter. | |
| **categoryName** | **String**| Specify that included attributes must have this category. The default is no category filter. | [optional] |
| **nameFilter** | **String**| The name query string used for filtering attributes. The default is no filter. | [optional] |
| **retrievalMode** | **String**| An optional value that determines the values to return when values don&#39;t exist at the exact time specified. The default is &#39;Auto&#39;. | [optional] |
| **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] |
| **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] |
| **templateName** | **String**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recorded values of the streams that meet the specified conditions. |  -  |
| **400** | The request was malformed. |  -  |
| **502** | The request was cancelled. |  -  |

<a id="streamSetGetRecordedAtTimesAdHoc"></a>
# **streamSetGetRecordedAtTimesAdHoc**
> ItemsStreamValues streamSetGetRecordedAtTimesAdHoc(time, webId, retrievalMode, selectedFields, sortOrder, timeZone, webIdType)

Returns recorded values of the specified streams at the specified times.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    List<String> time = Arrays.asList(); // List<String> | The timestamp at which to retrieve a recorded value. Multiple timestamps may be specified with multiple instances of the parameter.
    List<String> webId = Arrays.asList(); // List<String> | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    String retrievalMode = "retrievalMode_example"; // String | An optional value that determines the values to return when values don't exist at the exact time specified. The default is 'Auto'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsStreamValues result = apiInstance.streamSetGetRecordedAtTimesAdHoc(time, webId, retrievalMode, selectedFields, sortOrder, timeZone, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetGetRecordedAtTimesAdHoc");
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
| **time** | [**List&lt;String&gt;**](String.md)| The timestamp at which to retrieve a recorded value. Multiple timestamps may be specified with multiple instances of the parameter. | |
| **webId** | [**List&lt;String&gt;**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | |
| **retrievalMode** | **String**| An optional value that determines the values to return when values don&#39;t exist at the exact time specified. The default is &#39;Auto&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsStreamValues**](ItemsStreamValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recorded values of the streams that meet the specified conditions. |  -  |
| **400** | The request was malformed. |  -  |
| **502** | The request was cancelled. |  -  |

<a id="streamSetGetSummaries"></a>
# **streamSetGetSummaries**
> ItemsStreamSummaries streamSetGetSummaries(webId, calculationBasis, categoryName, endTime, filterExpression, nameFilter, sampleInterval, sampleType, searchFullHierarchy, selectedFields, showExcluded, showHidden, startTime, summaryDuration, summaryType, templateName, timeType, timeZone, webIdType)

Returns summary values of the attributes for an element, event frame or attribute.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    String webId = "webId_example"; // String | The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
    String calculationBasis = "calculationBasis_example"; // String | Specifies the method of evaluating the data over the time range. The default is 'TimeWeighted'.
    String categoryName = "categoryName_example"; // String | Specify that included attributes must have this category. The default is no category filter.
    String endTime = "endTime_example"; // String | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    String filterExpression = "filterExpression_example"; // String | A string containing a filter expression. Expression variables are relative to the attribute. Use '.' to reference the containing attribute. The default is no filtering.
    String nameFilter = "nameFilter_example"; // String | The name query string used for filtering attributes. The default is no filter.
    String sampleInterval = "sampleInterval_example"; // String | A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is 'Interval'.
    String sampleType = "sampleType_example"; // String | A flag which specifies one or more summaries to compute for each interval over the time range. The default is 'ExpressionRecordedValues'.
    Boolean searchFullHierarchy = true; // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    Boolean showExcluded = true; // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
    Boolean showHidden = true; // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
    String startTime = "startTime_example"; // String | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.
    String summaryDuration = "summaryDuration_example"; // String | The duration of each summary interval.
    List<String> summaryType = Arrays.asList(); // List<String> | Specifies the kinds of summaries to produce over the range. The default is 'Total'. Multiple summary types may be specified by using multiple instances of summaryType.
    String templateName = "templateName_example"; // String | Specify that included attributes must be members of this template. The default is no template filter.
    String timeType = "timeType_example"; // String | Specifies how to calculate the timestamp for each interval. The default is 'Auto'.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsStreamSummaries result = apiInstance.streamSetGetSummaries(webId, calculationBasis, categoryName, endTime, filterExpression, nameFilter, sampleInterval, sampleType, searchFullHierarchy, selectedFields, showExcluded, showHidden, startTime, summaryDuration, summaryType, templateName, timeType, timeZone, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetGetSummaries");
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
| **webId** | **String**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes. | |
| **calculationBasis** | **String**| Specifies the method of evaluating the data over the time range. The default is &#39;TimeWeighted&#39;. | [optional] |
| **categoryName** | **String**| Specify that included attributes must have this category. The default is no category filter. | [optional] |
| **endTime** | **String**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] |
| **filterExpression** | **String**| A string containing a filter expression. Expression variables are relative to the attribute. Use &#39;.&#39; to reference the containing attribute. The default is no filtering. | [optional] |
| **nameFilter** | **String**| The name query string used for filtering attributes. The default is no filter. | [optional] |
| **sampleInterval** | **String**| A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is &#39;Interval&#39;. | [optional] |
| **sampleType** | **String**| A flag which specifies one or more summaries to compute for each interval over the time range. The default is &#39;ExpressionRecordedValues&#39;. | [optional] |
| **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] |
| **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] |
| **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] |
| **summaryDuration** | **String**| The duration of each summary interval. | [optional] |
| **summaryType** | [**List&lt;String&gt;**](String.md)| Specifies the kinds of summaries to produce over the range. The default is &#39;Total&#39;. Multiple summary types may be specified by using multiple instances of summaryType. | [optional] |
| **templateName** | **String**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] |
| **timeType** | **String**| Specifies how to calculate the timestamp for each interval. The default is &#39;Auto&#39;. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsStreamSummaries**](ItemsStreamSummaries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary values of the streams that meet the specified conditions. |  -  |
| **409** | Unsupported operation on the given AF object. |  -  |

<a id="streamSetGetSummariesAdHoc"></a>
# **streamSetGetSummariesAdHoc**
> ItemsStreamSummaries streamSetGetSummariesAdHoc(webId, calculationBasis, endTime, filterExpression, sampleInterval, sampleType, selectedFields, startTime, summaryDuration, summaryType, timeType, timeZone, webIdType)

Returns summary values of the specified streams.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    List<String> webId = Arrays.asList(); // List<String> | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    String calculationBasis = "calculationBasis_example"; // String | Specifies the method of evaluating the data over the time range. The default is 'TimeWeighted'.
    String endTime = "endTime_example"; // String | An optional end time. The default is '*'. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    String filterExpression = "filterExpression_example"; // String | A string containing a filter expression. Expression variables are relative to the attribute. Use '.' to reference the containing attribute. The default is no filtering.
    String sampleInterval = "sampleInterval_example"; // String | A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is 'Interval'.
    String sampleType = "sampleType_example"; // String | A flag which specifies one or more summaries to compute for each interval over the time range. The default is 'ExpressionRecordedValues'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String startTime = "startTime_example"; // String | An optional start time. The default is '*-1d'.
    String summaryDuration = "summaryDuration_example"; // String | The duration of each summary interval.
    List<String> summaryType = Arrays.asList(); // List<String> | Specifies the kinds of summaries to produce over the range. The default is 'Total'. Multiple summary types may be specified by using multiple instances of summaryType.
    String timeType = "timeType_example"; // String | Specifies how to calculate the timestamp for each interval. The default is 'Auto'.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsStreamSummaries result = apiInstance.streamSetGetSummariesAdHoc(webId, calculationBasis, endTime, filterExpression, sampleInterval, sampleType, selectedFields, startTime, summaryDuration, summaryType, timeType, timeZone, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetGetSummariesAdHoc");
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
| **webId** | [**List&lt;String&gt;**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | |
| **calculationBasis** | **String**| Specifies the method of evaluating the data over the time range. The default is &#39;TimeWeighted&#39;. | [optional] |
| **endTime** | **String**| An optional end time. The default is &#39;*&#39;. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] |
| **filterExpression** | **String**| A string containing a filter expression. Expression variables are relative to the attribute. Use &#39;.&#39; to reference the containing attribute. The default is no filtering. | [optional] |
| **sampleInterval** | **String**| A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is &#39;Interval&#39;. | [optional] |
| **sampleType** | **String**| A flag which specifies one or more summaries to compute for each interval over the time range. The default is &#39;ExpressionRecordedValues&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39;. | [optional] |
| **summaryDuration** | **String**| The duration of each summary interval. | [optional] |
| **summaryType** | [**List&lt;String&gt;**](String.md)| Specifies the kinds of summaries to produce over the range. The default is &#39;Total&#39;. Multiple summary types may be specified by using multiple instances of summaryType. | [optional] |
| **timeType** | **String**| Specifies how to calculate the timestamp for each interval. The default is &#39;Auto&#39;. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsStreamSummaries**](ItemsStreamSummaries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary values of the streams that meet the specified conditions. |  -  |
| **409** | Unsupported operation on the given AF object. |  -  |

<a id="streamSetGetValues"></a>
# **streamSetGetValues**
> ItemsStreamValue streamSetGetValues(webId, categoryName, nameFilter, searchFullHierarchy, selectedFields, showExcluded, showHidden, sortField, sortOrder, templateName, time, timeZone, webIdType)

Returns values of the attributes for an Element, Event Frame or Attribute at the specified time.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    String webId = "webId_example"; // String | The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes.
    String categoryName = "categoryName_example"; // String | Specify that included attributes must have this category. The default is no category filter.
    String nameFilter = "nameFilter_example"; // String | The name query string used for filtering attributes. The default is no filter.
    Boolean searchFullHierarchy = true; // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    Boolean showExcluded = true; // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
    Boolean showHidden = true; // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. 'Name' is the only supported field by which to sort.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'
    String templateName = "templateName_example"; // String | Specify that included attributes must be members of this template. The default is no template filter.
    String time = "time_example"; // String | An AF time string, which is used as the time context to get stream values if it is provided. By default, it is not specified, and the default time context of the AF object will be used.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsStreamValue result = apiInstance.streamSetGetValues(webId, categoryName, nameFilter, searchFullHierarchy, selectedFields, showExcluded, showHidden, sortField, sortOrder, templateName, time, timeZone, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetGetValues");
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
| **webId** | **String**| The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes. | |
| **categoryName** | **String**| Specify that included attributes must have this category. The default is no category filter. | [optional] |
| **nameFilter** | **String**| The name query string used for filtering attributes. The default is no filter. | [optional] |
| **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] |
| **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; | [optional] |
| **templateName** | **String**| Specify that included attributes must be members of this template. The default is no template filter. | [optional] |
| **time** | **String**| An AF time string, which is used as the time context to get stream values if it is provided. By default, it is not specified, and the default time context of the AF object will be used. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsStreamValue**](ItemsStreamValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary values of the streams that meet the specified conditions. |  -  |
| **409** | Unsupported operation on the given AF object. |  -  |

<a id="streamSetGetValuesAdHoc"></a>
# **streamSetGetValuesAdHoc**
> ItemsStreamValue streamSetGetValuesAdHoc(webId, selectedFields, sortField, sortOrder, time, timeZone, webIdType)

Returns values of the specified streams.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    List<String> webId = Arrays.asList(); // List<String> | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String sortField = "sortField_example"; // String | The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. 'Name' is the only supported field by which to sort.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'
    String time = "time_example"; // String | An AF time string, which is used as the time context to get stream values if it is provided. By default, it is not specified, and the default time context of the AF object will be used.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsStreamValue result = apiInstance.streamSetGetValuesAdHoc(webId, selectedFields, sortField, sortOrder, time, timeZone, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetGetValuesAdHoc");
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
| **webId** | [**List&lt;String&gt;**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **sortField** | **String**| The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; | [optional] |
| **time** | **String**| An AF time string, which is used as the time context to get stream values if it is provided. By default, it is not specified, and the default time context of the AF object will be used. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsStreamValue**](ItemsStreamValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary values of the streams that meet the specified conditions. |  -  |
| **409** | Unsupported operation on the given AF object. |  -  |

<a id="streamSetRegisterStreamSetUpdates"></a>
# **streamSetRegisterStreamSetUpdates**
> ItemsStreamUpdatesRegister streamSetRegisterStreamSetUpdates(webId, selectedFields, webIdType)

Register for stream updates

The supplied webIds will register for stream updates. For a 200 response, the returned location header will contain the url for retrieving the next set of stream updates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    List<String> webId = Arrays.asList(); // List<String> | The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsStreamUpdatesRegister result = apiInstance.streamSetRegisterStreamSetUpdates(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetRegisterStreamSetUpdates");
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
| **webId** | [**List&lt;String&gt;**](String.md)| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsStreamUpdatesRegister**](ItemsStreamUpdatesRegister.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Registration |  -  |
| **400** | Any webID supplied is invalid |  -  |
| **409** | Any webID supplied is a static attribute |  -  |

<a id="streamSetRetrieveStreamSetUpdates"></a>
# **streamSetRetrieveStreamSetUpdates**
> ItemsStreamUpdatesRetrieve streamSetRetrieveStreamSetUpdates(marker, selectedFields, webIdType)

Receive stream updates

The supplied markers will identify the set of stream updates to retrieve. For a 200 response, the returned location header will contain the url for retrieving the stream updates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    List<String> marker = Arrays.asList(); // List<String> | Identifier of stream source and current position. Multiple markers may be specified with multiple instances of the parameter.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      ItemsStreamUpdatesRetrieve result = apiInstance.streamSetRetrieveStreamSetUpdates(marker, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetRetrieveStreamSetUpdates");
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
| **marker** | [**List&lt;String&gt;**](String.md)| Identifier of stream source and current position. Multiple markers may be specified with multiple instances of the parameter. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**ItemsStreamUpdatesRetrieve**](ItemsStreamUpdatesRetrieve.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The stream updates have been successfully retrieved |  -  |

<a id="streamSetUpdateValue"></a>
# **streamSetUpdateValue**
> ItemsSubstatus streamSetUpdateValue(webId, values, bufferOption, updateOption)

Updates a single value for the specified streams.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the parent element, event frame, or attribute. Attributes specified in the body must be descendants of the specified object.
    List<StreamValue> values = Arrays.asList(); // List<StreamValue> | The values to add or update.
    String bufferOption = "bufferOption_example"; // String | The desired AFBufferOption. The default is 'BufferIfPossible'.
    String updateOption = "updateOption_example"; // String | The desired AFUpdateOption. The default is 'Replace'.
    try {
      ItemsSubstatus result = apiInstance.streamSetUpdateValue(webId, values, bufferOption, updateOption);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetUpdateValue");
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
| **webId** | **String**| The ID of the parent element, event frame, or attribute. Attributes specified in the body must be descendants of the specified object. | |
| **values** | [**List&lt;StreamValue&gt;**](StreamValue.md)| The values to add or update. | |
| **bufferOption** | **String**| The desired AFBufferOption. The default is &#39;BufferIfPossible&#39;. | [optional] |
| **updateOption** | **String**| The desired AFUpdateOption. The default is &#39;Replace&#39;. | [optional] |

### Return type

[**ItemsSubstatus**](ItemsSubstatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All updates executed successfully. |  -  |
| **207** | The operation was a partial success. The response body contains substatuses and errors in the same order as the supplied values. |  -  |
| **409** | Unsupported operation on the given AF object. |  -  |

<a id="streamSetUpdateValueAdHoc"></a>
# **streamSetUpdateValueAdHoc**
> ItemsSubstatus streamSetUpdateValueAdHoc(values, bufferOption, updateOption)

Updates a single value for the specified streams.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    List<StreamValue> values = Arrays.asList(); // List<StreamValue> | The values to add or update.
    String bufferOption = "bufferOption_example"; // String | The desired AFBufferOption. The default is 'BufferIfPossible'.
    String updateOption = "updateOption_example"; // String | The desired AFUpdateOption. The default is 'Replace'.
    try {
      ItemsSubstatus result = apiInstance.streamSetUpdateValueAdHoc(values, bufferOption, updateOption);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetUpdateValueAdHoc");
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
| **values** | [**List&lt;StreamValue&gt;**](StreamValue.md)| The values to add or update. | |
| **bufferOption** | **String**| The desired AFBufferOption. The default is &#39;BufferIfPossible&#39;. | [optional] |
| **updateOption** | **String**| The desired AFUpdateOption. The default is &#39;Replace&#39;. | [optional] |

### Return type

[**ItemsSubstatus**](ItemsSubstatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All updates executed successfully. |  -  |
| **207** | The operation was a partial success. The response body contains substatuses and errors in the same order as the supplied values. |  -  |
| **409** | Unsupported operation on the given AF object. |  -  |

<a id="streamSetUpdateValues"></a>
# **streamSetUpdateValues**
> ItemsItemsSubstatus streamSetUpdateValues(webId, values, bufferOption, updateOption)

Updates multiple values for the specified streams.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the parent element, event frame, or attribute. Attributes specified in the body must be descendants of the specified object.
    List<StreamValues> values = Arrays.asList(); // List<StreamValues> | The values to add or update.
    String bufferOption = "bufferOption_example"; // String | The desired AFBufferOption. The default is 'BufferIfPossible'.
    String updateOption = "updateOption_example"; // String | The desired AFUpdateOption. The default is 'Replace'.
    try {
      ItemsItemsSubstatus result = apiInstance.streamSetUpdateValues(webId, values, bufferOption, updateOption);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetUpdateValues");
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
| **webId** | **String**| The ID of the parent element, event frame, or attribute. Attributes specified in the body must be descendants of the specified object. | |
| **values** | [**List&lt;StreamValues&gt;**](StreamValues.md)| The values to add or update. | |
| **bufferOption** | **String**| The desired AFBufferOption. The default is &#39;BufferIfPossible&#39;. | [optional] |
| **updateOption** | **String**| The desired AFUpdateOption. The default is &#39;Replace&#39;. | [optional] |

### Return type

[**ItemsItemsSubstatus**](ItemsItemsSubstatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All updates executed successfully. |  -  |
| **207** | The operation was a partial success. The response body contains substatuses and errors in the same order as the supplied values. |  -  |
| **409** | Unsupported operation on the given AF object. |  -  |

<a id="streamSetUpdateValuesAdHoc"></a>
# **streamSetUpdateValuesAdHoc**
> ItemsItemsSubstatus streamSetUpdateValuesAdHoc(values, bufferOption, updateOption)

Updates multiple values for the specified streams.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamSetApi apiInstance = new StreamSetApi(defaultClient);
    List<StreamValues> values = Arrays.asList(); // List<StreamValues> | The values to add or update.
    String bufferOption = "bufferOption_example"; // String | The desired AFBufferOption. The default is 'BufferIfPossible'.
    String updateOption = "updateOption_example"; // String | The desired AFUpdateOption. The default is 'Replace'.
    try {
      ItemsItemsSubstatus result = apiInstance.streamSetUpdateValuesAdHoc(values, bufferOption, updateOption);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSetApi#streamSetUpdateValuesAdHoc");
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
| **values** | [**List&lt;StreamValues&gt;**](StreamValues.md)| The values to add or update. | |
| **bufferOption** | **String**| The desired AFBufferOption. The default is &#39;BufferIfPossible&#39;. | [optional] |
| **updateOption** | **String**| The desired AFUpdateOption. The default is &#39;Replace&#39;. | [optional] |

### Return type

[**ItemsItemsSubstatus**](ItemsItemsSubstatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All updates executed successfully. |  -  |
| **207** | The operation was a partial success. The response body contains substatuses and errors in the same order as the supplied values. |  -  |
| **409** | Unsupported operation on the given AF object. |  -  |

