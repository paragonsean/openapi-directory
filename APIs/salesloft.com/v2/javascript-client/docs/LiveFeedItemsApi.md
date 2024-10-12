# SalesLoftPlatform.LiveFeedItemsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2ThirdPartyLiveFeedItemsPost**](LiveFeedItemsApi.md#v2ThirdPartyLiveFeedItemsPost) | **POST** /v2/third_party_live_feed_items | Create a live feed item



## v2ThirdPartyLiveFeedItemsPost

> [LiveFeedItem] v2ThirdPartyLiveFeedItemsPost(eventOccurredAt, idempotencyKey, message, subjectId, subjectType, userGuid)

Create a live feed item

Creates a live feed item that can be sent to users. May only be used by whitelisted Frontend Integrations. Reference the Salesloft App Directory and Frontend Integrations sections for additional details.

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.LiveFeedItemsApi();
let eventOccurredAt = "eventOccurredAt_example"; // String | Equality filters that are applied to the event_occurred_at field. A single filter can be used by itself or combined with other filters to create a range. ---CUSTOM--- {\\\"keys\\\":[{\\\"description\\\":\\\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\\\",\\\"name\\\":\\\"gt\\\",\\\"type\\\":\\\"iso8601 string\\\"},{\\\"description\\\":\\\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\\\",\\\"name\\\":\\\"gte\\\",\\\"type\\\":\\\"iso8601 string\\\"},{\\\"description\\\":\\\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\\\",\\\"name\\\":\\\"lt\\\",\\\"type\\\":\\\"iso8601 string\\\"},{\\\"description\\\":\\\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\\\",\\\"name\\\":\\\"lte\\\",\\\"type\\\":\\\"iso8601 string\\\"}],\\\"type\\\":\\\"object\\\"} 
let idempotencyKey = "idempotencyKey_example"; // String | Uniquely provided string specific to this event. This should be a value which can't be duplicated between external systems, meaning that an id is not sufficient.
let message = "message_example"; // String | The message that relates to the subject. This message should start with a lower-case past-tense verb and end with a period (e.g. \\\"received a package.\\\"). When live feed items are displayed to users, the subject's name is concatenated with the message and a joining space. Only <a> HTML tags with an \\\"href\\\" attribute are allowed. Other attributes and tags will be stripped.
let subjectId = 56; // Number | The ID of the subject of the live feed item (i.e. the \\\"person\\\" id).
let subjectType = "subjectType_example"; // String | The type of the subject of the live feed item. Currently only \\\"person\\\" is supported.
let userGuid = "userGuid_example"; // String | The guid for the user that this live feed item should be shown to.
apiInstance.v2ThirdPartyLiveFeedItemsPost(eventOccurredAt, idempotencyKey, message, subjectId, subjectType, userGuid, (error, data, response) => {
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
 **eventOccurredAt** | **String**| Equality filters that are applied to the event_occurred_at field. A single filter can be used by itself or combined with other filters to create a range. ---CUSTOM--- {\\\&quot;keys\\\&quot;:[{\\\&quot;description\\\&quot;:\\\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\\\&quot;,\\\&quot;name\\\&quot;:\\\&quot;gt\\\&quot;,\\\&quot;type\\\&quot;:\\\&quot;iso8601 string\\\&quot;},{\\\&quot;description\\\&quot;:\\\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\\\&quot;,\\\&quot;name\\\&quot;:\\\&quot;gte\\\&quot;,\\\&quot;type\\\&quot;:\\\&quot;iso8601 string\\\&quot;},{\\\&quot;description\\\&quot;:\\\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\\\&quot;,\\\&quot;name\\\&quot;:\\\&quot;lt\\\&quot;,\\\&quot;type\\\&quot;:\\\&quot;iso8601 string\\\&quot;},{\\\&quot;description\\\&quot;:\\\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\\\&quot;,\\\&quot;name\\\&quot;:\\\&quot;lte\\\&quot;,\\\&quot;type\\\&quot;:\\\&quot;iso8601 string\\\&quot;}],\\\&quot;type\\\&quot;:\\\&quot;object\\\&quot;}  | 
 **idempotencyKey** | **String**| Uniquely provided string specific to this event. This should be a value which can&#39;t be duplicated between external systems, meaning that an id is not sufficient. | 
 **message** | **String**| The message that relates to the subject. This message should start with a lower-case past-tense verb and end with a period (e.g. \\\&quot;received a package.\\\&quot;). When live feed items are displayed to users, the subject&#39;s name is concatenated with the message and a joining space. Only &lt;a&gt; HTML tags with an \\\&quot;href\\\&quot; attribute are allowed. Other attributes and tags will be stripped. | 
 **subjectId** | **Number**| The ID of the subject of the live feed item (i.e. the \\\&quot;person\\\&quot; id). | 
 **subjectType** | **String**| The type of the subject of the live feed item. Currently only \\\&quot;person\\\&quot; is supported. | 
 **userGuid** | **String**| The guid for the user that this live feed item should be shown to. | 

### Return type

[**[LiveFeedItem]**](LiveFeedItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*

