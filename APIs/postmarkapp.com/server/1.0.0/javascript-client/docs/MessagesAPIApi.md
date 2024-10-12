# PostmarkApi.MessagesAPIApi

All URIs are relative to *http://api.postmarkapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bypassRulesForInboundMessage**](MessagesAPIApi.md#bypassRulesForInboundMessage) | **PUT** /messages/inbound/{messageid}/bypass | Bypass rules for a blocked inbound message
[**getClicksForSingleOutboundMessage**](MessagesAPIApi.md#getClicksForSingleOutboundMessage) | **GET** /messages/outbound/clicks/{messageid} | Retrieve Message Clicks
[**getInboundMessageDetails**](MessagesAPIApi.md#getInboundMessageDetails) | **GET** /messages/inbound/{messageid}/details | Inbound message details
[**getOpensForSingleOutboundMessage**](MessagesAPIApi.md#getOpensForSingleOutboundMessage) | **GET** /messages/outbound/opens/{messageid} | Retrieve Message Opens
[**getOutboundMessageDetails**](MessagesAPIApi.md#getOutboundMessageDetails) | **GET** /messages/outbound/{messageid}/details | Outbound message details
[**getOutboundMessageDump**](MessagesAPIApi.md#getOutboundMessageDump) | **GET** /messages/outbound/{messageid}/dump | Outbound message dump
[**retryInboundMessageProcessing**](MessagesAPIApi.md#retryInboundMessageProcessing) | **PUT** /messages/inbound/{messageid}/retry | Retry a failed inbound message for processing
[**searchClicksForOutboundMessages**](MessagesAPIApi.md#searchClicksForOutboundMessages) | **GET** /messages/outbound/clicks | Clicks for a all messages
[**searchInboundMessages**](MessagesAPIApi.md#searchInboundMessages) | **GET** /messages/inbound | Inbound message search
[**searchOpensForOutboundMessages**](MessagesAPIApi.md#searchOpensForOutboundMessages) | **GET** /messages/outbound/opens | Opens for all messages
[**searchOutboundMessages**](MessagesAPIApi.md#searchOutboundMessages) | **GET** /messages/outbound | Outbound message search



## bypassRulesForInboundMessage

> StandardPostmarkResponse bypassRulesForInboundMessage(xPostmarkServerToken, messageid)

Bypass rules for a blocked inbound message

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.MessagesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let messageid = "messageid_example"; // String | The ID of the message which should bypass inbound rules.
apiInstance.bypassRulesForInboundMessage(xPostmarkServerToken, messageid, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **messageid** | **String**| The ID of the message which should bypass inbound rules. | 

### Return type

[**StandardPostmarkResponse**](StandardPostmarkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClicksForSingleOutboundMessage

> MessageClickSearchResponse getClicksForSingleOutboundMessage(xPostmarkServerToken, messageid, count, offset)

Retrieve Message Clicks

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.MessagesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let messageid = "messageid_example"; // String | The ID of the Outbound Message for which click statistics should be retrieved.
let count = 1; // Number | Number of message clicks to return per request. Max 500.
let offset = 0; // Number | Number of messages to skip.
apiInstance.getClicksForSingleOutboundMessage(xPostmarkServerToken, messageid, count, offset, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **messageid** | **String**| The ID of the Outbound Message for which click statistics should be retrieved. | 
 **count** | **Number**| Number of message clicks to return per request. Max 500. | [default to 1]
 **offset** | **Number**| Number of messages to skip. | [default to 0]

### Return type

[**MessageClickSearchResponse**](MessageClickSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInboundMessageDetails

> InboundMessageFullDetailsResponse getInboundMessageDetails(xPostmarkServerToken, messageid)

Inbound message details

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.MessagesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let messageid = "messageid_example"; // String | The ID of the message for which to details will be retrieved.
apiInstance.getInboundMessageDetails(xPostmarkServerToken, messageid, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **messageid** | **String**| The ID of the message for which to details will be retrieved. | 

### Return type

[**InboundMessageFullDetailsResponse**](InboundMessageFullDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOpensForSingleOutboundMessage

> MessageOpenSearchResponse getOpensForSingleOutboundMessage(xPostmarkServerToken, messageid, count, offset)

Retrieve Message Opens

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.MessagesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let messageid = "messageid_example"; // String | The ID of the Outbound Message for which open statistics should be retrieved.
let count = 1; // Number | Number of message opens to return per request. Max 500.
let offset = 0; // Number | Number of messages to skip.
apiInstance.getOpensForSingleOutboundMessage(xPostmarkServerToken, messageid, count, offset, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **messageid** | **String**| The ID of the Outbound Message for which open statistics should be retrieved. | 
 **count** | **Number**| Number of message opens to return per request. Max 500. | [default to 1]
 **offset** | **Number**| Number of messages to skip. | [default to 0]

### Return type

[**MessageOpenSearchResponse**](MessageOpenSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOutboundMessageDetails

> OutboundMessageDetailsResponse getOutboundMessageDetails(xPostmarkServerToken, messageid)

Outbound message details

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.MessagesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let messageid = "messageid_example"; // String | The ID of the message for which to retrieve details.
apiInstance.getOutboundMessageDetails(xPostmarkServerToken, messageid, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **messageid** | **String**| The ID of the message for which to retrieve details. | 

### Return type

[**OutboundMessageDetailsResponse**](OutboundMessageDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOutboundMessageDump

> OutboundMessageDumpResponse getOutboundMessageDump(xPostmarkServerToken, messageid)

Outbound message dump

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.MessagesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let messageid = "messageid_example"; // String | The ID of the message for which to retrieve a dump.
apiInstance.getOutboundMessageDump(xPostmarkServerToken, messageid, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **messageid** | **String**| The ID of the message for which to retrieve a dump. | 

### Return type

[**OutboundMessageDumpResponse**](OutboundMessageDumpResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retryInboundMessageProcessing

> StandardPostmarkResponse retryInboundMessageProcessing(xPostmarkServerToken, messageid)

Retry a failed inbound message for processing

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.MessagesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let messageid = "messageid_example"; // String | The ID of the inbound message on which we should retry processing.
apiInstance.retryInboundMessageProcessing(xPostmarkServerToken, messageid, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **messageid** | **String**| The ID of the inbound message on which we should retry processing. | 

### Return type

[**StandardPostmarkResponse**](StandardPostmarkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchClicksForOutboundMessages

> MessageClickSearchResponse searchClicksForOutboundMessages(xPostmarkServerToken, count, offset, opts)

Clicks for a all messages

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.MessagesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let count = 56; // Number | Number of message clicks to return per request. Max 500.
let offset = 56; // Number | Number of messages to skip
let opts = {
  'recipient': "recipient_example", // String | Filter by To, Cc, Bcc
  'tag': "tag_example", // String | Filter by tag
  'clientName': "clientName_example", // String | Filter by client name, i.e. Outlook, Gmail
  'clientCompany': "clientCompany_example", // String | Filter by company, i.e. Microsoft, Apple, Google
  'clientFamily': "clientFamily_example", // String | Filter by client family, i.e. OS X, Chrome
  'osName': "osName_example", // String | Filter by full OS name and specific version, i.e. OS X 10.9 Mavericks, Windows 7
  'osFamily': "osFamily_example", // String | Filter by kind of OS used without specific version, i.e. OS X, Windows
  'osCompany': "osCompany_example", // String | Filter by company which produced the OS, i.e. Apple Computer, Inc., Microsoft Corporation
  'platform': "platform_example", // String | Filter by platform, i.e. webmail, desktop, mobile
  'country': "country_example", // String | Filter by country messages were opened in, i.e. Denmark, Russia
  'region': "region_example", // String | Filter by full name of region messages were opened in, i.e. Moscow, New York
  'city': "city_example" // String | Filter by full name of region messages were opened in, i.e. Moscow, New York
};
apiInstance.searchClicksForOutboundMessages(xPostmarkServerToken, count, offset, opts, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **count** | **Number**| Number of message clicks to return per request. Max 500. | 
 **offset** | **Number**| Number of messages to skip | 
 **recipient** | **String**| Filter by To, Cc, Bcc | [optional] 
 **tag** | **String**| Filter by tag | [optional] 
 **clientName** | **String**| Filter by client name, i.e. Outlook, Gmail | [optional] 
 **clientCompany** | **String**| Filter by company, i.e. Microsoft, Apple, Google | [optional] 
 **clientFamily** | **String**| Filter by client family, i.e. OS X, Chrome | [optional] 
 **osName** | **String**| Filter by full OS name and specific version, i.e. OS X 10.9 Mavericks, Windows 7 | [optional] 
 **osFamily** | **String**| Filter by kind of OS used without specific version, i.e. OS X, Windows | [optional] 
 **osCompany** | **String**| Filter by company which produced the OS, i.e. Apple Computer, Inc., Microsoft Corporation | [optional] 
 **platform** | **String**| Filter by platform, i.e. webmail, desktop, mobile | [optional] 
 **country** | **String**| Filter by country messages were opened in, i.e. Denmark, Russia | [optional] 
 **region** | **String**| Filter by full name of region messages were opened in, i.e. Moscow, New York | [optional] 
 **city** | **String**| Filter by full name of region messages were opened in, i.e. Moscow, New York | [optional] 

### Return type

[**MessageClickSearchResponse**](MessageClickSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchInboundMessages

> InboundSearchResponse searchInboundMessages(xPostmarkServerToken, count, offset, opts)

Inbound message search

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.MessagesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let count = 56; // Number | Number of messages to return per request. Max 500.
let offset = 56; // Number | Number of messages to skip
let opts = {
  'recipient': "recipient_example", // String | Filter by the user who was receiving the email
  'fromemail': "fromemail_example", // String | Filter by the sender email address
  'subject': "subject_example", // String | Filter by email subject
  'mailboxhash': "mailboxhash_example", // String | Filter by mailboxhash
  'tag': "tag_example", // String | Filter by tag
  'status': "status_example", // String | Filter by status (`blocked`, `processed`, `queued`, `failed`, `scheduled`)
  'todate': new Date("2013-10-20"), // Date | Filter messages up to the date specified. e.g. `2014-02-01`
  'fromdate': new Date("2013-10-20") // Date | Filter messages starting from the date specified. e.g. `2014-02-01`
};
apiInstance.searchInboundMessages(xPostmarkServerToken, count, offset, opts, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **count** | **Number**| Number of messages to return per request. Max 500. | 
 **offset** | **Number**| Number of messages to skip | 
 **recipient** | **String**| Filter by the user who was receiving the email | [optional] 
 **fromemail** | **String**| Filter by the sender email address | [optional] 
 **subject** | **String**| Filter by email subject | [optional] 
 **mailboxhash** | **String**| Filter by mailboxhash | [optional] 
 **tag** | **String**| Filter by tag | [optional] 
 **status** | **String**| Filter by status (&#x60;blocked&#x60;, &#x60;processed&#x60;, &#x60;queued&#x60;, &#x60;failed&#x60;, &#x60;scheduled&#x60;) | [optional] 
 **todate** | **Date**| Filter messages up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 
 **fromdate** | **Date**| Filter messages starting from the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**InboundSearchResponse**](InboundSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchOpensForOutboundMessages

> MessageOpenSearchResponse searchOpensForOutboundMessages(xPostmarkServerToken, count, offset, opts)

Opens for all messages

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.MessagesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let count = 56; // Number | Number of message opens to return per request. Max 500.
let offset = 56; // Number | Number of messages to skip
let opts = {
  'recipient': "recipient_example", // String | Filter by To, Cc, Bcc
  'tag': "tag_example", // String | Filter by tag
  'clientName': "clientName_example", // String | Filter by client name, i.e. Outlook, Gmail
  'clientCompany': "clientCompany_example", // String | Filter by company, i.e. Microsoft, Apple, Google
  'clientFamily': "clientFamily_example", // String | Filter by client family, i.e. OS X, Chrome
  'osName': "osName_example", // String | Filter by full OS name and specific version, i.e. OS X 10.9 Mavericks, Windows 7
  'osFamily': "osFamily_example", // String | Filter by kind of OS used without specific version, i.e. OS X, Windows
  'osCompany': "osCompany_example", // String | Filter by company which produced the OS, i.e. Apple Computer, Inc., Microsoft Corporation
  'platform': "platform_example", // String | Filter by platform, i.e. webmail, desktop, mobile
  'country': "country_example", // String | Filter by country messages were opened in, i.e. Denmark, Russia
  'region': "region_example", // String | Filter by full name of region messages were opened in, i.e. Moscow, New York
  'city': "city_example" // String | Filter by full name of region messages were opened in, i.e. Moscow, New York
};
apiInstance.searchOpensForOutboundMessages(xPostmarkServerToken, count, offset, opts, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **count** | **Number**| Number of message opens to return per request. Max 500. | 
 **offset** | **Number**| Number of messages to skip | 
 **recipient** | **String**| Filter by To, Cc, Bcc | [optional] 
 **tag** | **String**| Filter by tag | [optional] 
 **clientName** | **String**| Filter by client name, i.e. Outlook, Gmail | [optional] 
 **clientCompany** | **String**| Filter by company, i.e. Microsoft, Apple, Google | [optional] 
 **clientFamily** | **String**| Filter by client family, i.e. OS X, Chrome | [optional] 
 **osName** | **String**| Filter by full OS name and specific version, i.e. OS X 10.9 Mavericks, Windows 7 | [optional] 
 **osFamily** | **String**| Filter by kind of OS used without specific version, i.e. OS X, Windows | [optional] 
 **osCompany** | **String**| Filter by company which produced the OS, i.e. Apple Computer, Inc., Microsoft Corporation | [optional] 
 **platform** | **String**| Filter by platform, i.e. webmail, desktop, mobile | [optional] 
 **country** | **String**| Filter by country messages were opened in, i.e. Denmark, Russia | [optional] 
 **region** | **String**| Filter by full name of region messages were opened in, i.e. Moscow, New York | [optional] 
 **city** | **String**| Filter by full name of region messages were opened in, i.e. Moscow, New York | [optional] 

### Return type

[**MessageOpenSearchResponse**](MessageOpenSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchOutboundMessages

> OutboundSearchResponse searchOutboundMessages(xPostmarkServerToken, count, offset, opts)

Outbound message search

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.MessagesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let count = 56; // Number | Number of messages to return per request. Max 500.
let offset = 56; // Number | Number of messages to skip
let opts = {
  'recipient': "recipient_example", // String | Filter by the user who was receiving the email
  'fromemail': "fromemail_example", // String | Filter by the sender email address
  'tag': "tag_example", // String | Filter by tag
  'status': "status_example", // String | Filter by status (`queued` or `sent`)
  'todate': new Date("2013-10-20"), // Date | Filter messages up to the date specified. e.g. `2014-02-01`
  'fromdate': new Date("2013-10-20") // Date | Filter messages starting from the date specified. e.g. `2014-02-01`
};
apiInstance.searchOutboundMessages(xPostmarkServerToken, count, offset, opts, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **count** | **Number**| Number of messages to return per request. Max 500. | 
 **offset** | **Number**| Number of messages to skip | 
 **recipient** | **String**| Filter by the user who was receiving the email | [optional] 
 **fromemail** | **String**| Filter by the sender email address | [optional] 
 **tag** | **String**| Filter by tag | [optional] 
 **status** | **String**| Filter by status (&#x60;queued&#x60; or &#x60;sent&#x60;) | [optional] 
 **todate** | **Date**| Filter messages up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 
 **fromdate** | **Date**| Filter messages starting from the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**OutboundSearchResponse**](OutboundSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

