# TextsApi

All URIs are relative to *https://api.callfire.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addTextBroadcastBatch**](TextsApi.md#addTextBroadcastBatch) | **POST** /texts/broadcasts/{id}/batches | Add batches to a text broadcast |
| [**addTextBroadcastRecipients**](TextsApi.md#addTextBroadcastRecipients) | **POST** /texts/broadcasts/{id}/recipients | Add recipients to a text broadcast |
| [**archiveTextBroadcast**](TextsApi.md#archiveTextBroadcast) | **POST** /texts/broadcasts/{id}/archive | Archive text broadcast |
| [**createTextAutoReply**](TextsApi.md#createTextAutoReply) | **POST** /texts/auto-replys | Create an auto reply |
| [**createTextBroadcast**](TextsApi.md#createTextBroadcast) | **POST** /texts/broadcasts | Create a text broadcast |
| [**deleteTextAutoReply**](TextsApi.md#deleteTextAutoReply) | **DELETE** /texts/auto-replys/{id} | Delete an auto reply |
| [**findTextAutoReplys**](TextsApi.md#findTextAutoReplys) | **GET** /texts/auto-replys | Find auto replies |
| [**findTextBroadcasts**](TextsApi.md#findTextBroadcasts) | **GET** /texts/broadcasts | Find text broadcasts |
| [**findTexts**](TextsApi.md#findTexts) | **GET** /texts | Find texts |
| [**getText**](TextsApi.md#getText) | **GET** /texts/{id} | Find a specific text |
| [**getTextAutoReply**](TextsApi.md#getTextAutoReply) | **GET** /texts/auto-replys/{id} | Find a specific auto reply |
| [**getTextBroadcast**](TextsApi.md#getTextBroadcast) | **GET** /texts/broadcasts/{id} | Find a specific text broadcast |
| [**getTextBroadcastBatches**](TextsApi.md#getTextBroadcastBatches) | **GET** /texts/broadcasts/{id}/batches | Find batches in a text broadcast |
| [**getTextBroadcastStats**](TextsApi.md#getTextBroadcastStats) | **GET** /texts/broadcasts/{id}/stats | Get statistics on text broadcast |
| [**getTextBroadcastTexts**](TextsApi.md#getTextBroadcastTexts) | **GET** /texts/broadcasts/{id}/texts | Find texts in a text broadcast |
| [**sendTexts**](TextsApi.md#sendTexts) | **POST** /texts | Send texts |
| [**startTextBroadcast**](TextsApi.md#startTextBroadcast) | **POST** /texts/broadcasts/{id}/start | Start text broadcast |
| [**stopTextBroadcast**](TextsApi.md#stopTextBroadcast) | **POST** /texts/broadcasts/{id}/stop | Stop text broadcast |
| [**toggleTextBroadcastRecipientsStatus**](TextsApi.md#toggleTextBroadcastRecipientsStatus) | **POST** /texts/broadcasts/{id}/toggleRecipientsStatus | Disable/enable undialed recipients in broadcast |
| [**updateTextBroadcast**](TextsApi.md#updateTextBroadcast) | **PUT** /texts/broadcasts/{id} | Update a text broadcast |


<a id="addTextBroadcastBatch"></a>
# **addTextBroadcastBatch**
> ResourceId addTextBroadcastBatch(id, strictValidation, batchRequest)

Add batches to a text broadcast

Allows adding an extra batches to an already created text broadcast campaign. The batches which being  added pass the CallFire validation process (unlike in the recipients version of this API). That is why using of a scrubDuplicates flag remove duplicates from your batch. Batches may be added as a contact list id, a list of contact ids, or a list of numbers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TextsApi apiInstance = new TextsApi(defaultClient);
    Long id = 56L; // Long | An id of a text broadcast
    Boolean strictValidation = true; // Boolean | Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation = true and one of numbers didn't pass validation
    BatchRequest batchRequest = new BatchRequest(); // BatchRequest | A request object
    try {
      ResourceId result = apiInstance.addTextBroadcastBatch(id, strictValidation, batchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextsApi#addTextBroadcastBatch");
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
| **id** | **Long**| An id of a text broadcast | |
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

<a id="addTextBroadcastRecipients"></a>
# **addTextBroadcastRecipients**
> TextList addTextBroadcastRecipients(id, fields, strictValidation, textRecipient)

Add recipients to a text broadcast

Use this API to add recipients to a text broadcast which is already created. Post a list of Recipient objects to be immediately added to the text broadcast campaign. These contacts will not go through validation process, and will be acted upon as they are added. Recipients may be added as a list of contact ids, or list of numbers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TextsApi apiInstance = new TextsApi(defaultClient);
    Long id = 56L; // Long | An id of a text broadcast
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    Boolean strictValidation = true; // Boolean | Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation = true and one of numbers didn't pass validation
    List<TextRecipient> textRecipient = Arrays.asList(); // List<TextRecipient> | A list of the TextRecipient objects
    try {
      TextList result = apiInstance.addTextBroadcastRecipients(id, fields, strictValidation, textRecipient);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextsApi#addTextBroadcastRecipients");
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
| **id** | **Long**| An id of a text broadcast | |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |
| **strictValidation** | **Boolean**| Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation | [optional] |
| **textRecipient** | [**List&lt;TextRecipient&gt;**](TextRecipient.md)| A list of the TextRecipient objects | [optional] |

### Return type

[**TextList**](TextList.md)

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

<a id="archiveTextBroadcast"></a>
# **archiveTextBroadcast**
> archiveTextBroadcast(id)

Archive text broadcast

Archives a text broadcast (and hides it in the search results)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TextsApi apiInstance = new TextsApi(defaultClient);
    Long id = 56L; // Long | An id of a text broadcast to archive
    try {
      apiInstance.archiveTextBroadcast(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextsApi#archiveTextBroadcast");
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
| **id** | **Long**| An id of a text broadcast to archive | |

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

<a id="createTextAutoReply"></a>
# **createTextAutoReply**
> ResourceId createTextAutoReply(textAutoReply)

Create an auto reply

CallFire gives you possibility to set up auto reply messages for your numbers and keywords. You can set a general auto reply for anyone who texts your number, keyword, and/or include a text to match, so that the auto reply would be sent only to those who text the matched text

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TextsApi apiInstance = new TextsApi(defaultClient);
    TextAutoReply textAutoReply = new TextAutoReply(); // TextAutoReply | TextAutoReply object, keyword or number should be specified with response message and text to match if needed
    try {
      ResourceId result = apiInstance.createTextAutoReply(textAutoReply);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextsApi#createTextAutoReply");
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
| **textAutoReply** | [**TextAutoReply**](TextAutoReply.md)| TextAutoReply object, keyword or number should be specified with response message and text to match if needed | [optional] |

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

<a id="createTextBroadcast"></a>
# **createTextBroadcast**
> ResourceId createTextBroadcast(start, strictValidation, textBroadcast)

Create a text broadcast

Creates a text broadcast campaign using the Text Broadcast API. Send a TextBroadcast object in the message body to detail a text broadcast campaign. A campaign can be created without contacts and with bare minimum configuration, but contacts have to be added further on to use the campaign. It supports scheduling, retry logic, pattern-based messages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TextsApi apiInstance = new TextsApi(defaultClient);
    Boolean start = true; // Boolean | If true then starts the campaign immediately (not required).
    Boolean strictValidation = true; // Boolean | Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation = true and one of numbers didn't pass validation
    TextBroadcast textBroadcast = new TextBroadcast(); // TextBroadcast | A TextBroadcast object
    try {
      ResourceId result = apiInstance.createTextBroadcast(start, strictValidation, textBroadcast);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextsApi#createTextBroadcast");
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
| **start** | **Boolean**| If true then starts the campaign immediately (not required). | [optional] |
| **strictValidation** | **Boolean**| Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation | [optional] |
| **textBroadcast** | [**TextBroadcast**](TextBroadcast.md)| A TextBroadcast object | [optional] |

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

<a id="deleteTextAutoReply"></a>
# **deleteTextAutoReply**
> deleteTextAutoReply(id)

Delete an auto reply

Deletes a text auto reply and removes the configuration. Can not delete a TextAutoReply which is currently active for a campaign

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TextsApi apiInstance = new TextsApi(defaultClient);
    Long id = 56L; // Long | An id of a text auto reply
    try {
      apiInstance.deleteTextAutoReply(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextsApi#deleteTextAutoReply");
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
| **id** | **Long**| An id of a text auto reply | |

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

<a id="findTextAutoReplys"></a>
# **findTextAutoReplys**
> TextAutoReplyPage findTextAutoReplys(fields, limit, offset, number)

Find auto replies

Find all text autoreplies created by user. Returns a paged list of TextAutoReply

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TextsApi apiInstance = new TextsApi(defaultClient);
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    Integer limit = 100; // Integer | To set the maximum number of records to return in a paged list response. The default is 100
    Integer offset = 0; // Integer | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    String number = "number_example"; // String | Phone number in E.164 format (11-digit) which contains a TextAutoReply. Example: 12132000384. If number is empty then operator returns all autoreplies configured for the user's account
    try {
      TextAutoReplyPage result = apiInstance.findTextAutoReplys(fields, limit, offset, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextsApi#findTextAutoReplys");
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
| **number** | **String**| Phone number in E.164 format (11-digit) which contains a TextAutoReply. Example: 12132000384. If number is empty then operator returns all autoreplies configured for the user&#39;s account | [optional] |

### Return type

[**TextAutoReplyPage**](TextAutoReplyPage.md)

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

<a id="findTextBroadcasts"></a>
# **findTextBroadcasts**
> TextBroadcastPage findTextBroadcasts(name, label, running, scheduled, intervalBegin, intervalEnd, limit, offset, fields)

Find text broadcasts

Searches for all text broadcasts created by user. Can query on label, name, and the current running status of the campaign. Returns a paged list of text broadcasts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TextsApi apiInstance = new TextsApi(defaultClient);
    String name = "name_example"; // String | A name of text broadcast
    String label = "label_example"; // String | A label of a text broadcast
    Boolean running = true; // Boolean | Returns broadcasts only in running state.
    Boolean scheduled = true; // Boolean | Specify whether the campaigns should be scheduled or not
    Long intervalBegin = 56L; // Long | Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
    Long intervalEnd = 56L; // Long | End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
    Integer limit = 10; // Integer | To set the maximum number of records to return in a paged list response. The default is 100
    Integer offset = 0; // Integer | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      TextBroadcastPage result = apiInstance.findTextBroadcasts(name, label, running, scheduled, intervalBegin, intervalEnd, limit, offset, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextsApi#findTextBroadcasts");
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
| **name** | **String**| A name of text broadcast | [optional] |
| **label** | **String**| A label of a text broadcast | [optional] |
| **running** | **Boolean**| Returns broadcasts only in running state. | [optional] |
| **scheduled** | **Boolean**| Specify whether the campaigns should be scheduled or not | [optional] |
| **intervalBegin** | **Long**| Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] |
| **intervalEnd** | **Long**| End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] |
| **limit** | **Integer**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 10] |
| **offset** | **Integer**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0] |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**TextBroadcastPage**](TextBroadcastPage.md)

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

<a id="findTexts"></a>
# **findTexts**
> TextPage findTexts(id, campaignId, batchId, fromNumber, toNumber, label, states, results, inbound, intervalBegin, intervalEnd, limit, offset, fields)

Find texts

Searches for texts sent or received by user. Use \&quot;campaignId&#x3D;0\&quot; parameter to query for all texts sent through the POST /texts API. See [call states and results](https://developers.callfire.com/results-responses-errors.html)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TextsApi apiInstance = new TextsApi(defaultClient);
    List<Long> id = Arrays.asList(); // List<Long> | List of Text ids to search for, if ids specified other query params ignored
    Long campaignId = 56L; // Long | An id of a campaign, queries for texts inside a particular campaign. Specify null to list texts of all campaigns or 0 for a default campaign
    Long batchId = 56L; // Long | An Id of a contact batch, queries for texts which are used in the particular contact batch
    String fromNumber = "fromNumber_example"; // String | A phone number in E.164 format (11-digit). Example: 12132000384, 67076
    String toNumber = "toNumber_example"; // String | A phone number in E.164 format (11-digit). Example: 12132000384, 67076
    String label = "label_example"; // String | A label of a text message
    String states = "states_example"; // String | Expected text statuses in comma separated string, available values: READY, SELECTED, CALLBACK, FINISHED, DISABLED, DNC, DUP, INVALID, TIMEOUT, PERIOD_LIMIT. See [call states and results](https://developers.callfire.com/results-responses-errors.html)
    String results = "results_example"; // String | Expected text results in comma separated string, available values: SENT, RECEIVED, DNT, TOO_BIG, INTERNAL_ERROR, CARRIER_ERROR, CARRIER_TEMP_ERROR, UNDIALED. See [call states and results](https://developers.callfire.com/results-responses-errors.html)
    Boolean inbound = true; // Boolean | Specify true for inbound or false for outbounds. Do not specify this parameter if you need to get both inbound and outbound texts listed in response
    Long intervalBegin = 56L; // Long | Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000
    Long intervalEnd = 56L; // Long | End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000
    Integer limit = 10; // Integer | To set the maximum number of records to return in a paged list response. The default is 100
    Integer offset = 0; // Integer | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      TextPage result = apiInstance.findTexts(id, campaignId, batchId, fromNumber, toNumber, label, states, results, inbound, intervalBegin, intervalEnd, limit, offset, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextsApi#findTexts");
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
| **id** | [**List&lt;Long&gt;**](Long.md)| List of Text ids to search for, if ids specified other query params ignored | [optional] |
| **campaignId** | **Long**| An id of a campaign, queries for texts inside a particular campaign. Specify null to list texts of all campaigns or 0 for a default campaign | [optional] |
| **batchId** | **Long**| An Id of a contact batch, queries for texts which are used in the particular contact batch | [optional] |
| **fromNumber** | **String**| A phone number in E.164 format (11-digit). Example: 12132000384, 67076 | [optional] |
| **toNumber** | **String**| A phone number in E.164 format (11-digit). Example: 12132000384, 67076 | [optional] |
| **label** | **String**| A label of a text message | [optional] |
| **states** | **String**| Expected text statuses in comma separated string, available values: READY, SELECTED, CALLBACK, FINISHED, DISABLED, DNC, DUP, INVALID, TIMEOUT, PERIOD_LIMIT. See [call states and results](https://developers.callfire.com/results-responses-errors.html) | [optional] |
| **results** | **String**| Expected text results in comma separated string, available values: SENT, RECEIVED, DNT, TOO_BIG, INTERNAL_ERROR, CARRIER_ERROR, CARRIER_TEMP_ERROR, UNDIALED. See [call states and results](https://developers.callfire.com/results-responses-errors.html) | [optional] |
| **inbound** | **Boolean**| Specify true for inbound or false for outbounds. Do not specify this parameter if you need to get both inbound and outbound texts listed in response | [optional] |
| **intervalBegin** | **Long**| Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 | [optional] |
| **intervalEnd** | **Long**| End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 | [optional] |
| **limit** | **Integer**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 10] |
| **offset** | **Integer**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0] |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**TextPage**](TextPage.md)

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

<a id="getText"></a>
# **getText**
> Text getText(id, fields)

Find a specific text

Returns a single Text instance for a given text id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TextsApi apiInstance = new TextsApi(defaultClient);
    Long id = 56L; // Long | An id of a text
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      Text result = apiInstance.getText(id, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextsApi#getText");
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
| **id** | **Long**| An id of a text | |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**Text**](Text.md)

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

<a id="getTextAutoReply"></a>
# **getTextAutoReply**
> TextAutoReply getTextAutoReply(id, fields)

Find a specific auto reply

Returns a single TextAutoReply instance for a given text auto reply id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TextsApi apiInstance = new TextsApi(defaultClient);
    Long id = 56L; // Long | An id of a text auto reply
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      TextAutoReply result = apiInstance.getTextAutoReply(id, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextsApi#getTextAutoReply");
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
| **id** | **Long**| An id of a text auto reply | |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**TextAutoReply**](TextAutoReply.md)

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

<a id="getTextBroadcast"></a>
# **getTextBroadcast**
> TextBroadcast getTextBroadcast(id, fields)

Find a specific text broadcast

Returns a single TextBroadcast instance for a given text broadcast id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TextsApi apiInstance = new TextsApi(defaultClient);
    Long id = 56L; // Long | An id of a text broadcast
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      TextBroadcast result = apiInstance.getTextBroadcast(id, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextsApi#getTextBroadcast");
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
| **id** | **Long**| An id of a text broadcast | |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**TextBroadcast**](TextBroadcast.md)

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

<a id="getTextBroadcastBatches"></a>
# **getTextBroadcastBatches**
> BatchPage getTextBroadcastBatches(id, fields, limit, offset)

Find batches in a text broadcast

This endpoint will enable the user to page through all of the batches for a particular text broadcast campaign

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TextsApi apiInstance = new TextsApi(defaultClient);
    Long id = 56L; // Long | An id of a text broadcast
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    Integer limit = 100; // Integer | To set the maximum number of records to return in a paged list response. The default is 100
    Integer offset = 0; // Integer | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    try {
      BatchPage result = apiInstance.getTextBroadcastBatches(id, fields, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextsApi#getTextBroadcastBatches");
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
| **id** | **Long**| An id of a text broadcast | |
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

<a id="getTextBroadcastStats"></a>
# **getTextBroadcastStats**
> TextBroadcastStatsDto getTextBroadcastStats(id, fields, begin, end)

Get statistics on text broadcast

Returns the broadcast statistics. Example: total number of the sent/received actions, total cost, number of remaining outbound actions, error count, etc

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TextsApi apiInstance = new TextsApi(defaultClient);
    Long id = 56L; // Long | An id of a text broadcast
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    Long begin = 56L; // Long | Start of a search find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
    Long end = 56L; // Long | End of a search time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
    try {
      TextBroadcastStatsDto result = apiInstance.getTextBroadcastStats(id, fields, begin, end);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextsApi#getTextBroadcastStats");
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
| **id** | **Long**| An id of a text broadcast | |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |
| **begin** | **Long**| Start of a search find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] |
| **end** | **Long**| End of a search time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] |

### Return type

[**TextBroadcastStatsDto**](TextBroadcastStatsDto.md)

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

<a id="getTextBroadcastTexts"></a>
# **getTextBroadcastTexts**
> TextPage getTextBroadcastTexts(id, batchId, fields, limit, offset)

Find texts in a text broadcast

This endpoint will enable the user to page through all of the texts for a particular text broadcast campaign

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TextsApi apiInstance = new TextsApi(defaultClient);
    Long id = 56L; // Long | An id of a text broadcast
    Long batchId = 56L; // Long | ~
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    Integer limit = 100; // Integer | To set the maximum number of records to return in a paged list response. The default is 100
    Integer offset = 0; // Integer | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    try {
      TextPage result = apiInstance.getTextBroadcastTexts(id, batchId, fields, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextsApi#getTextBroadcastTexts");
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
| **id** | **Long**| An id of a text broadcast | |
| **batchId** | **Long**| ~ | [optional] |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |
| **limit** | **Integer**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100] |
| **offset** | **Integer**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0] |

### Return type

[**TextPage**](TextPage.md)

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

<a id="sendTexts"></a>
# **sendTexts**
> TextList sendTexts(fields, campaignId, defaultMessage, strictValidation, textRecipient)

Send texts

Use the /texts API to send individual texts quickly. By default all texts are going out from CallFire&#39;s dedicated short code. Example: 67076, 818818 etc

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TextsApi apiInstance = new TextsApi(defaultClient);
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    Long campaignId = 56L; // Long | Specifies a campaignId to send texts through a previously created campaign
    String defaultMessage = "defaultMessage_example"; // String | Text message can be overridden by TextRecipient.message field. If multiple recipients have the same text message to a different recipients it is better to specify a single default message and do not duplicate it in each recipient.
    Boolean strictValidation = true; // Boolean | Turns on strict validation for recipients
    List<TextRecipient> textRecipient = Arrays.asList(); // List<TextRecipient> | List of TextRecipient objects. By recipient we mean either phone number or contact with user-defined attributes added to action. Text messaging supports media files, provide a list of ids of media files for recipient to attach media to the message.
    try {
      TextList result = apiInstance.sendTexts(fields, campaignId, defaultMessage, strictValidation, textRecipient);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextsApi#sendTexts");
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
| **campaignId** | **Long**| Specifies a campaignId to send texts through a previously created campaign | [optional] |
| **defaultMessage** | **String**| Text message can be overridden by TextRecipient.message field. If multiple recipients have the same text message to a different recipients it is better to specify a single default message and do not duplicate it in each recipient. | [optional] |
| **strictValidation** | **Boolean**| Turns on strict validation for recipients | [optional] |
| **textRecipient** | [**List&lt;TextRecipient&gt;**](TextRecipient.md)| List of TextRecipient objects. By recipient we mean either phone number or contact with user-defined attributes added to action. Text messaging supports media files, provide a list of ids of media files for recipient to attach media to the message. | [optional] |

### Return type

[**TextList**](TextList.md)

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

<a id="startTextBroadcast"></a>
# **startTextBroadcast**
> startTextBroadcast(id)

Start text broadcast

Starts a text broadcast

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TextsApi apiInstance = new TextsApi(defaultClient);
    Long id = 56L; // Long | An id of a text broadcast to start
    try {
      apiInstance.startTextBroadcast(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextsApi#startTextBroadcast");
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
| **id** | **Long**| An id of a text broadcast to start | |

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

<a id="stopTextBroadcast"></a>
# **stopTextBroadcast**
> stopTextBroadcast(id)

Stop text broadcast

Stops a text broadcast

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TextsApi apiInstance = new TextsApi(defaultClient);
    Long id = 56L; // Long | An Id of a text broadcast. To stop the broadcast
    try {
      apiInstance.stopTextBroadcast(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextsApi#stopTextBroadcast");
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
| **id** | **Long**| An Id of a text broadcast. To stop the broadcast | |

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

<a id="toggleTextBroadcastRecipientsStatus"></a>
# **toggleTextBroadcastRecipientsStatus**
> toggleTextBroadcastRecipientsStatus(id, enable, recipient)

Disable/enable undialed recipients in broadcast

This operation lets the user to disable/enable undialed contacts in created broadcast

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TextsApi apiInstance = new TextsApi(defaultClient);
    Long id = 56L; // Long | An id of a text broadcast
    Boolean enable = false; // Boolean | Flag which indicate what to do with texts (true will enable texts in DISABLED status and vice versa)
    List<Recipient> recipient = Arrays.asList(); // List<Recipient> | List of Recipient objects. By recipient we mean either phone number or contact id.
    try {
      apiInstance.toggleTextBroadcastRecipientsStatus(id, enable, recipient);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextsApi#toggleTextBroadcastRecipientsStatus");
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
| **id** | **Long**| An id of a text broadcast | |
| **enable** | **Boolean**| Flag which indicate what to do with texts (true will enable texts in DISABLED status and vice versa) | [optional] [default to false] |
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

<a id="updateTextBroadcast"></a>
# **updateTextBroadcast**
> TextBroadcastCreateResponse updateTextBroadcast(id, strictValidation, textBroadcast)

Update a text broadcast

Allows modifying the configuration of existing text broadcast campaign. See TextBroadcast for more information on what can/can&#39;t be updated on this API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TextsApi apiInstance = new TextsApi(defaultClient);
    Long id = 56L; // Long | An id of a text broadcast
    Boolean strictValidation = true; // Boolean | Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation = true and one of numbers didn't pass validation
    TextBroadcast textBroadcast = new TextBroadcast(); // TextBroadcast | A TextBroadcast object
    try {
      TextBroadcastCreateResponse result = apiInstance.updateTextBroadcast(id, strictValidation, textBroadcast);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextsApi#updateTextBroadcast");
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
| **id** | **Long**| An id of a text broadcast | |
| **strictValidation** | **Boolean**| Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation | [optional] |
| **textBroadcast** | [**TextBroadcast**](TextBroadcast.md)| A TextBroadcast object | [optional] |

### Return type

[**TextBroadcastCreateResponse**](TextBroadcastCreateResponse.md)

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

