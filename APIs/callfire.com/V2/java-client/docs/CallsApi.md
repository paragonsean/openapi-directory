# CallsApi

All URIs are relative to *https://api.callfire.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addCallBroadcastBatch**](CallsApi.md#addCallBroadcastBatch) | **POST** /calls/broadcasts/{id}/batches | Add batches to a call broadcast |
| [**addCallBroadcastRecipients**](CallsApi.md#addCallBroadcastRecipients) | **POST** /calls/broadcasts/{id}/recipients | Add recipients to a call broadcast |
| [**archiveVoiceBroadcast**](CallsApi.md#archiveVoiceBroadcast) | **POST** /calls/broadcasts/{id}/archive | Archive voice broadcast |
| [**createCallBroadcast**](CallsApi.md#createCallBroadcast) | **POST** /calls/broadcasts | Create a call broadcast |
| [**findCallBroadcasts**](CallsApi.md#findCallBroadcasts) | **GET** /calls/broadcasts | Find call broadcasts |
| [**findCalls**](CallsApi.md#findCalls) | **GET** /calls | Find calls |
| [**getCall**](CallsApi.md#getCall) | **GET** /calls/{id} | Find a specific call |
| [**getCallBroadcast**](CallsApi.md#getCallBroadcast) | **GET** /calls/broadcasts/{id} | Find a specific call broadcast |
| [**getCallBroadcastBatches**](CallsApi.md#getCallBroadcastBatches) | **GET** /calls/broadcasts/{id}/batches | Find batches in a call broadcast |
| [**getCallBroadcastCalls**](CallsApi.md#getCallBroadcastCalls) | **GET** /calls/broadcasts/{id}/calls | Find calls in a call broadcast |
| [**getCallBroadcastStats**](CallsApi.md#getCallBroadcastStats) | **GET** /calls/broadcasts/{id}/stats | Get statistics on call broadcast |
| [**getCallRecording**](CallsApi.md#getCallRecording) | **GET** /calls/recordings/{id} | Get call recording by id |
| [**getCallRecordingByName**](CallsApi.md#getCallRecordingByName) | **GET** /calls/{id}/recordings/{name} | Get call recording by name |
| [**getCallRecordingMp3**](CallsApi.md#getCallRecordingMp3) | **GET** /calls/recordings/{id}.mp3 | Get call recording in mp3 format |
| [**getCallRecordingMp3ByName**](CallsApi.md#getCallRecordingMp3ByName) | **GET** /calls/{id}/recordings/{name}.mp3 | Get call mp3 recording by name |
| [**getCallRecordings**](CallsApi.md#getCallRecordings) | **GET** /calls/{id}/recordings | Get call recordings for a call |
| [**sendCalls**](CallsApi.md#sendCalls) | **POST** /calls | Send calls |
| [**startVoiceBroadcast**](CallsApi.md#startVoiceBroadcast) | **POST** /calls/broadcasts/{id}/start | Start voice broadcast |
| [**stopVoiceBroadcast**](CallsApi.md#stopVoiceBroadcast) | **POST** /calls/broadcasts/{id}/stop | Stop voice broadcast |
| [**toggleCallBroadcastRecipientsStatus**](CallsApi.md#toggleCallBroadcastRecipientsStatus) | **POST** /calls/broadcasts/{id}/toggleRecipientsStatus | Disable/enable undialed recipients in broadcast |
| [**updateCallBroadcast**](CallsApi.md#updateCallBroadcast) | **PUT** /calls/broadcasts/{id} | Update a call broadcast |


<a id="addCallBroadcastBatch"></a>
# **addCallBroadcastBatch**
> ResourceId addCallBroadcastBatch(id, strictValidation, batchRequest)

Add batches to a call broadcast

The &#39;add batch&#39; API allows user to add additional batches to an already created voice broadcast campaign. The added batch will go through the CallFire validation process, unlike in the recipients version of this API. That is why you can use the scrubDuplicates flag to remove duplicates from your batch. Batches may be added as a contact list id, a list of contact ids, or a list of numbers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallsApi apiInstance = new CallsApi(defaultClient);
    Long id = 56L; // Long | An id of a call broadcast
    Boolean strictValidation = true; // Boolean | Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation = true and one of numbers didn't pass validation
    BatchRequest batchRequest = new BatchRequest(); // BatchRequest | A request object
    try {
      ResourceId result = apiInstance.addCallBroadcastBatch(id, strictValidation, batchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#addCallBroadcastBatch");
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
| **id** | **Long**| An id of a call broadcast | |
| **strictValidation** | **Boolean**| Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation | [optional] |
| **batchRequest** | [**BatchRequest**](BatchRequest.md)| A request object | [optional] |

### Return type

[**ResourceId**](ResourceId.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="addCallBroadcastRecipients"></a>
# **addCallBroadcastRecipients**
> CallList addCallBroadcastRecipients(id, fields, strictValidation, recipient)

Add recipients to a call broadcast

Use this API to add the recipients to an existing voice broadcast. Post a list of Recipient objects to be added to the voice broadcast campaign. These contacts will not go through validation process, and will be acted upon as they are added. Recipients may be added as a list of contact ids, or list of numbers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallsApi apiInstance = new CallsApi(defaultClient);
    Long id = 56L; // Long | An id of a call broadcast
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    Boolean strictValidation = true; // Boolean | Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation = true and one of numbers didn't pass validation
    List<Recipient> recipient = Arrays.asList(); // List<Recipient> | A list of CallRecipient objects
    try {
      CallList result = apiInstance.addCallBroadcastRecipients(id, fields, strictValidation, recipient);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#addCallBroadcastRecipients");
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
| **id** | **Long**| An id of a call broadcast | |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |
| **strictValidation** | **Boolean**| Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation | [optional] |
| **recipient** | [**List&lt;Recipient&gt;**](Recipient.md)| A list of CallRecipient objects | [optional] |

### Return type

[**CallList**](CallList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="archiveVoiceBroadcast"></a>
# **archiveVoiceBroadcast**
> archiveVoiceBroadcast(id)

Archive voice broadcast

Archives a voice broadcast (voice broadcast will be hidden in search results)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallsApi apiInstance = new CallsApi(defaultClient);
    Long id = 56L; // Long | An id of a voice broadcast to archive
    try {
      apiInstance.archiveVoiceBroadcast(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#archiveVoiceBroadcast");
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
| **id** | **Long**| An id of a voice broadcast to archive | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="createCallBroadcast"></a>
# **createCallBroadcast**
> ResourceId createCallBroadcast(start, strictValidation, callBroadcast)

Create a call broadcast

Creates a call broadcast campaign using the Call Broadcast API. Send a CallBroadcast in the message body to add details in a voice broadcast campaign. The campaign can be created without contacts and bare minimum configuration, but contacts will have to be added further on to use the campaign

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallsApi apiInstance = new CallsApi(defaultClient);
    Boolean start = true; // Boolean | Specify whether to immediately start this campaign (not required)
    Boolean strictValidation = true; // Boolean | Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation = true and one of numbers didn't pass validation
    CallBroadcast callBroadcast = new CallBroadcast(); // CallBroadcast | A CallBroadcast object
    try {
      ResourceId result = apiInstance.createCallBroadcast(start, strictValidation, callBroadcast);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#createCallBroadcast");
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
| **start** | **Boolean**| Specify whether to immediately start this campaign (not required) | [optional] |
| **strictValidation** | **Boolean**| Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation | [optional] |
| **callBroadcast** | [**CallBroadcast**](CallBroadcast.md)| A CallBroadcast object | [optional] |

### Return type

[**ResourceId**](ResourceId.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="findCallBroadcasts"></a>
# **findCallBroadcasts**
> CallBroadcastPage findCallBroadcasts(fields, limit, offset, label, name, running, scheduled, intervalBegin, intervalEnd)

Find call broadcasts

Searches for all voice broadcasts created by user. Can query on label, name, and the current running status of the campaign. Returns a paged list of voice broadcasts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallsApi apiInstance = new CallsApi(defaultClient);
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    Integer limit = 10; // Integer | To set the maximum number of records to return in a paged list response. The default is 100
    Integer offset = 0; // Integer | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    String label = "label_example"; // String | A label of a voice broadcast
    String name = "name_example"; // String | A name of voice broadcast
    Boolean running = true; // Boolean | Specify whether the campaigns should be running or not
    Boolean scheduled = true; // Boolean | Specify whether the campaigns should be scheduled or not
    Long intervalBegin = 56L; // Long | Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
    Long intervalEnd = 56L; // Long | End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
    try {
      CallBroadcastPage result = apiInstance.findCallBroadcasts(fields, limit, offset, label, name, running, scheduled, intervalBegin, intervalEnd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#findCallBroadcasts");
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
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |
| **limit** | **Integer**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 10] |
| **offset** | **Integer**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0] |
| **label** | **String**| A label of a voice broadcast | [optional] |
| **name** | **String**| A name of voice broadcast | [optional] |
| **running** | **Boolean**| Specify whether the campaigns should be running or not | [optional] |
| **scheduled** | **Boolean**| Specify whether the campaigns should be scheduled or not | [optional] |
| **intervalBegin** | **Long**| Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] |
| **intervalEnd** | **Long**| End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] |

### Return type

[**CallBroadcastPage**](CallBroadcastPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="findCalls"></a>
# **findCalls**
> CallPage findCalls(fields, limit, offset, id, campaignId, batchId, fromNumber, toNumber, label, states, results, inbound, intervalBegin, intervalEnd)

Find calls

To search for all calls sent or received by the user. Use \&quot;id&#x3D;0\&quot; for the campaignId parameter to query for all calls sent through the POST /calls API. See [call states and results](https://developers.callfire.com/results-responses-errors.html)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallsApi apiInstance = new CallsApi(defaultClient);
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    Integer limit = 100; // Integer | To set the maximum number of records to return in a paged list response. The default is 100
    Integer offset = 0; // Integer | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    List<Long> id = Arrays.asList(); // List<Long> | Lists the Call ids to search for. If calls ids are specified then other query parameters can be ignored
    Long campaignId = 56L; // Long | An id of a campaign, queries for calls included to a particular campaign. Specify null for all campaigns and 0 for default campaign
    Long batchId = 56L; // Long | An id of a contact batch, queries for calls of a particular contact batch
    String fromNumber = "fromNumber_example"; // String | Phone number in E.164 format (11-digit) that call was from. Example: 12132000384
    String toNumber = "toNumber_example"; // String | Phone number in E.164 format (11-digit) that call was sent to. Example: 12132000384
    String label = "label_example"; // String | A label for a specific call
    String states = "states_example"; // String | Searches for all calls which correspond to statuses listed in a comma separated string. Available values: READY, SELECTED, CALLBACK, FINISHED, DISABLED, DNC, DUP, INVALID, TIMEOUT, PERIOD_LIMIT. See [call states and results](https://developers.callfire.com/results-responses-errors.html)
    String results = "results_example"; // String | Searches for all calls with statuses listed in a comma separated string. Available values: SENT, RECEIVED, DNT, TOO_BIG, INTERNAL_ERROR, CARRIER_ERROR, CARRIER_TEMP_ERROR, UNDIALED. See [call states and results](https://developers.callfire.com/results-responses-errors.html)
    Boolean inbound = true; // Boolean | Filters inbound calls for \"true\" value and outbound calls for \"false\" value
    Long intervalBegin = 56L; // Long | Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
    Long intervalEnd = 56L; // Long | End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
    try {
      CallPage result = apiInstance.findCalls(fields, limit, offset, id, campaignId, batchId, fromNumber, toNumber, label, states, results, inbound, intervalBegin, intervalEnd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#findCalls");
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
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |
| **limit** | **Integer**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100] |
| **offset** | **Integer**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0] |
| **id** | [**List&lt;Long&gt;**](Long.md)| Lists the Call ids to search for. If calls ids are specified then other query parameters can be ignored | [optional] |
| **campaignId** | **Long**| An id of a campaign, queries for calls included to a particular campaign. Specify null for all campaigns and 0 for default campaign | [optional] |
| **batchId** | **Long**| An id of a contact batch, queries for calls of a particular contact batch | [optional] |
| **fromNumber** | **String**| Phone number in E.164 format (11-digit) that call was from. Example: 12132000384 | [optional] |
| **toNumber** | **String**| Phone number in E.164 format (11-digit) that call was sent to. Example: 12132000384 | [optional] |
| **label** | **String**| A label for a specific call | [optional] |
| **states** | **String**| Searches for all calls which correspond to statuses listed in a comma separated string. Available values: READY, SELECTED, CALLBACK, FINISHED, DISABLED, DNC, DUP, INVALID, TIMEOUT, PERIOD_LIMIT. See [call states and results](https://developers.callfire.com/results-responses-errors.html) | [optional] |
| **results** | **String**| Searches for all calls with statuses listed in a comma separated string. Available values: SENT, RECEIVED, DNT, TOO_BIG, INTERNAL_ERROR, CARRIER_ERROR, CARRIER_TEMP_ERROR, UNDIALED. See [call states and results](https://developers.callfire.com/results-responses-errors.html) | [optional] |
| **inbound** | **Boolean**| Filters inbound calls for \&quot;true\&quot; value and outbound calls for \&quot;false\&quot; value | [optional] |
| **intervalBegin** | **Long**| Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] |
| **intervalEnd** | **Long**| End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] |

### Return type

[**CallPage**](CallPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCall"></a>
# **getCall**
> Call getCall(id, fields)

Find a specific call

Returns a single Call instance for a given call id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallsApi apiInstance = new CallsApi(defaultClient);
    Long id = 56L; // Long | An id of a call
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      Call result = apiInstance.getCall(id, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#getCall");
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
| **id** | **Long**| An id of a call | |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**Call**](Call.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCallBroadcast"></a>
# **getCallBroadcast**
> CallBroadcast getCallBroadcast(id, fields)

Find a specific call broadcast

Returns a single CallBroadcast instance for a given call broadcast campaign id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallsApi apiInstance = new CallsApi(defaultClient);
    Long id = 56L; // Long | An id of a CallBroadcast
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      CallBroadcast result = apiInstance.getCallBroadcast(id, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#getCallBroadcast");
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
| **id** | **Long**| An id of a CallBroadcast | |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**CallBroadcast**](CallBroadcast.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCallBroadcastBatches"></a>
# **getCallBroadcastBatches**
> BatchPage getCallBroadcastBatches(id, fields, limit, offset)

Find batches in a call broadcast

This endpoint will enable the user to page through all of the batches for a particular voice broadcast campaign

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallsApi apiInstance = new CallsApi(defaultClient);
    Long id = 56L; // Long | An id of a call broadcast
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    Integer limit = 100; // Integer | To set the maximum number of records to return in a paged list response. The default is 100
    Integer offset = 0; // Integer | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    try {
      BatchPage result = apiInstance.getCallBroadcastBatches(id, fields, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#getCallBroadcastBatches");
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
| **id** | **Long**| An id of a call broadcast | |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |
| **limit** | **Integer**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100] |
| **offset** | **Integer**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0] |

### Return type

[**BatchPage**](BatchPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCallBroadcastCalls"></a>
# **getCallBroadcastCalls**
> CallPage getCallBroadcastCalls(id, batchId, fields, limit, offset)

Find calls in a call broadcast

This endpoint will enable the user to page through all calls for a particular call broadcast campaign

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallsApi apiInstance = new CallsApi(defaultClient);
    Long id = 56L; // Long | An Id of a call broadcast
    Long batchId = 56L; // Long | An id of a particular batch associated with broadcast
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    Integer limit = 100; // Integer | To set the maximum number of records to return in a paged list response. The default is 100
    Integer offset = 0; // Integer | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    try {
      CallPage result = apiInstance.getCallBroadcastCalls(id, batchId, fields, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#getCallBroadcastCalls");
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
| **id** | **Long**| An Id of a call broadcast | |
| **batchId** | **Long**| An id of a particular batch associated with broadcast | [optional] |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |
| **limit** | **Integer**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100] |
| **offset** | **Integer**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0] |

### Return type

[**CallPage**](CallPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCallBroadcastStats"></a>
# **getCallBroadcastStats**
> CallBroadcastStats getCallBroadcastStats(id, fields, begin, end)

Get statistics on call broadcast

Returns broadcast statistics like total number of sent/received actions, total cost, number of remaining outbound actions, error count, etc

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallsApi apiInstance = new CallsApi(defaultClient);
    Long id = 56L; // Long | An id of a call broadcast
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    Long begin = 56L; // Long | Start of the search time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
    Long end = 56L; // Long | End of the search time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
    try {
      CallBroadcastStats result = apiInstance.getCallBroadcastStats(id, fields, begin, end);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#getCallBroadcastStats");
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
| **id** | **Long**| An id of a call broadcast | |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |
| **begin** | **Long**| Start of the search time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] |
| **end** | **Long**| End of the search time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] |

### Return type

[**CallBroadcastStats**](CallBroadcastStats.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCallRecording"></a>
# **getCallRecording**
> CallRecording getCallRecording(id, fields)

Get call recording by id

Returns metadata of recording of a particular call. Metadata contains a link to a MP3 recording

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallsApi apiInstance = new CallsApi(defaultClient);
    Long id = 56L; // Long | ~
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      CallRecording result = apiInstance.getCallRecording(id, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#getCallRecording");
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
| **id** | **Long**| ~ | |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**CallRecording**](CallRecording.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCallRecordingByName"></a>
# **getCallRecordingByName**
> CallRecording getCallRecordingByName(id, name, fields)

Get call recording by name

Returns recording metadata of particular call. Metadata contains link to a MP3 recording

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallsApi apiInstance = new CallsApi(defaultClient);
    Long id = 56L; // Long | An id of a call
    String name = "name_example"; // String | A name of a recording
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      CallRecording result = apiInstance.getCallRecordingByName(id, name, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#getCallRecordingByName");
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
| **id** | **Long**| An id of a call | |
| **name** | **String**| A name of a recording | |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**CallRecording**](CallRecording.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCallRecordingMp3"></a>
# **getCallRecordingMp3**
> Object getCallRecordingMp3(id)

Get call recording in mp3 format

Returns an MP3 recording of particular call, response contains binary data, content type is &#39;audio/mpeg&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallsApi apiInstance = new CallsApi(defaultClient);
    Long id = 56L; // Long | An id of a call
    try {
      Object result = apiInstance.getCallRecordingMp3(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#getCallRecordingMp3");
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
| **id** | **Long**| An id of a call | |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCallRecordingMp3ByName"></a>
# **getCallRecordingMp3ByName**
> Object getCallRecordingMp3ByName(id, name)

Get call mp3 recording by name

Returns a MP3 recording of a particular call, response contains binary data, content type is &#39;audio/mpeg&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallsApi apiInstance = new CallsApi(defaultClient);
    Long id = 56L; // Long | An id of a call
    String name = "name_example"; // String | A name of a recording
    try {
      Object result = apiInstance.getCallRecordingMp3ByName(id, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#getCallRecordingMp3ByName");
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
| **id** | **Long**| An id of a call | |
| **name** | **String**| A name of a recording | |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: audio/mpeg

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCallRecordings"></a>
# **getCallRecordings**
> CallRecordingList getCallRecordings(id, fields)

Get call recordings for a call

Returns a list of recordings metadata of particular call. Metadata contains link to a MP3 recording

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallsApi apiInstance = new CallsApi(defaultClient);
    Long id = 56L; // Long | An id of a call
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      CallRecordingList result = apiInstance.getCallRecordings(id, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#getCallRecordings");
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
| **id** | **Long**| An id of a call | |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**CallRecordingList**](CallRecordingList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="sendCalls"></a>
# **sendCalls**
> CallList sendCalls(fields, campaignId, defaultLiveMessage, defaultMachineMessage, defaultLiveMessageSoundId, defaultMachineMessageSoundId, defaultVoice, strictValidation, callRecipient)

Send calls

Use the /calls API to send individual calls quickly. A verified Caller ID and sufficient credits are required to make a call. CallRecipient represents a single recipient identified by phone number or contact id in CallFire system. You can attach user-defined attributes to a Call action via CallRecipient.attributes property, attributes are available in Call action response

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallsApi apiInstance = new CallsApi(defaultClient);
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    Long campaignId = 56L; // Long | Specifies a campaignId to send calls quickly on a previously created campaign
    String defaultLiveMessage = "defaultLiveMessage_example"; // String | Text to be turned into a sound, this text will be played when the phone is answered. Parameter can be overridden for any particular CallRecipient
    String defaultMachineMessage = "defaultMachineMessage_example"; // String | Text to be turned into a sound, this text will be played when answering machine is detected. Parameter can be overridden for any particular CallRecipient
    Long defaultLiveMessageSoundId = 56L; // Long | Id of sound file to play if phone is answered. Parameter can be overridden for any particular CallRecipient
    Long defaultMachineMessageSoundId = 56L; // Long | An id of a sound file to play if answering machine is detected. Parameter can be overridden for any particular CallRecipient
    String defaultVoice = "MALE1"; // String | The voice set by default for all text-to-speech messages defined in CallRecipient objects or as default *Message properties
    Boolean strictValidation = true; // Boolean | Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation = true and one of numbers didn't pass validation
    List<CallRecipient> callRecipient = Arrays.asList(); // List<CallRecipient> | An array of CallRecipient objects.  Limitations: 1. Max number of CallRecipient objects is 10 
    try {
      CallList result = apiInstance.sendCalls(fields, campaignId, defaultLiveMessage, defaultMachineMessage, defaultLiveMessageSoundId, defaultMachineMessageSoundId, defaultVoice, strictValidation, callRecipient);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#sendCalls");
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
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |
| **campaignId** | **Long**| Specifies a campaignId to send calls quickly on a previously created campaign | [optional] |
| **defaultLiveMessage** | **String**| Text to be turned into a sound, this text will be played when the phone is answered. Parameter can be overridden for any particular CallRecipient | [optional] |
| **defaultMachineMessage** | **String**| Text to be turned into a sound, this text will be played when answering machine is detected. Parameter can be overridden for any particular CallRecipient | [optional] |
| **defaultLiveMessageSoundId** | **Long**| Id of sound file to play if phone is answered. Parameter can be overridden for any particular CallRecipient | [optional] |
| **defaultMachineMessageSoundId** | **Long**| An id of a sound file to play if answering machine is detected. Parameter can be overridden for any particular CallRecipient | [optional] |
| **defaultVoice** | **String**| The voice set by default for all text-to-speech messages defined in CallRecipient objects or as default *Message properties | [optional] [enum: MALE1, FEMALE1, FEMALE2, SPANISH1, FRENCHCANADIAN1] |
| **strictValidation** | **Boolean**| Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation | [optional] |
| **callRecipient** | [**List&lt;CallRecipient&gt;**](CallRecipient.md)| An array of CallRecipient objects.  Limitations: 1. Max number of CallRecipient objects is 10  | [optional] |

### Return type

[**CallList**](CallList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="startVoiceBroadcast"></a>
# **startVoiceBroadcast**
> startVoiceBroadcast(id)

Start voice broadcast

Start a voice broadcast

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallsApi apiInstance = new CallsApi(defaultClient);
    Long id = 56L; // Long | An id of voice broadcast to start
    try {
      apiInstance.startVoiceBroadcast(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#startVoiceBroadcast");
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
| **id** | **Long**| An id of voice broadcast to start | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="stopVoiceBroadcast"></a>
# **stopVoiceBroadcast**
> stopVoiceBroadcast(id)

Stop voice broadcast

Stop a voice broadcast

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallsApi apiInstance = new CallsApi(defaultClient);
    Long id = 56L; // Long | An id of voice broadcast to stop
    try {
      apiInstance.stopVoiceBroadcast(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#stopVoiceBroadcast");
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
| **id** | **Long**| An id of voice broadcast to stop | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="toggleCallBroadcastRecipientsStatus"></a>
# **toggleCallBroadcastRecipientsStatus**
> toggleCallBroadcastRecipientsStatus(id, enable, recipient)

Disable/enable undialed recipients in broadcast

This operation lets the user to disable/enable undialed recipients in created broadcast

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallsApi apiInstance = new CallsApi(defaultClient);
    Long id = 56L; // Long | An id of a voice broadcast
    Boolean enable = false; // Boolean | Flag which indicate what to do with calls (true will enable call in DISABLED status and vice versa)
    List<Recipient> recipient = Arrays.asList(); // List<Recipient> | List of Recipient objects. By recipient we mean either phone number or contact id.
    try {
      apiInstance.toggleCallBroadcastRecipientsStatus(id, enable, recipient);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#toggleCallBroadcastRecipientsStatus");
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
| **id** | **Long**| An id of a voice broadcast | |
| **enable** | **Boolean**| Flag which indicate what to do with calls (true will enable call in DISABLED status and vice versa) | [optional] [default to false] |
| **recipient** | [**List&lt;Recipient&gt;**](Recipient.md)| List of Recipient objects. By recipient we mean either phone number or contact id. | [optional] |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="updateCallBroadcast"></a>
# **updateCallBroadcast**
> updateCallBroadcast(id, strictValidation, callBroadcast)

Update a call broadcast

This operation lets the user modify the configuration of a voice broadcast campaign after call broadcast campaign is created. See CallBroadcast for more information on what can/can&#39;t be updated on this API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallsApi apiInstance = new CallsApi(defaultClient);
    Long id = 56L; // Long | An id of a voice broadcast
    Boolean strictValidation = true; // Boolean | Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation = true and one of numbers didn't pass validation
    CallBroadcast callBroadcast = new CallBroadcast(); // CallBroadcast | A CallBroadcast object
    try {
      apiInstance.updateCallBroadcast(id, strictValidation, callBroadcast);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#updateCallBroadcast");
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
| **id** | **Long**| An id of a voice broadcast | |
| **strictValidation** | **Boolean**| Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation | [optional] |
| **callBroadcast** | [**CallBroadcast**](CallBroadcast.md)| A CallBroadcast object | [optional] |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

