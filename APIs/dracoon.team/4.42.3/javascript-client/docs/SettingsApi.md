# DracoonApi.SettingsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAndPreserveKeyPair**](SettingsApi.md#createAndPreserveKeyPair) | **POST** /v4/settings/keypairs | Create system rescue key pair and preserve copy of old private key
[**createWebhook**](SettingsApi.md#createWebhook) | **POST** /v4/settings/webhooks | Create webhook
[**removeSystemRescueKeyPair**](SettingsApi.md#removeSystemRescueKeyPair) | **DELETE** /v4/settings/keypair | Remove system rescue key pair
[**removeWebhook**](SettingsApi.md#removeWebhook) | **DELETE** /v4/settings/webhooks/{webhook_id} | Remove webhook
[**requestAllSystemRescueKeyPairs**](SettingsApi.md#requestAllSystemRescueKeyPairs) | **GET** /v4/settings/keypairs | Request all system rescue key pairs
[**requestListOfEventTypesForConfigManager**](SettingsApi.md#requestListOfEventTypesForConfigManager) | **GET** /v4/settings/webhooks/event_types | Request list of event types
[**requestListOfWebhooks**](SettingsApi.md#requestListOfWebhooks) | **GET** /v4/settings/webhooks | Request list of webhooks
[**requestNotificationChannels**](SettingsApi.md#requestNotificationChannels) | **GET** /v4/settings/notifications/channels | Request list of notification channels
[**requestSettings**](SettingsApi.md#requestSettings) | **GET** /v4/settings | Request customer settings
[**requestSystemRescueKeyPair**](SettingsApi.md#requestSystemRescueKeyPair) | **GET** /v4/settings/keypair | Request system rescue key pair
[**requestWebhook**](SettingsApi.md#requestWebhook) | **GET** /v4/settings/webhooks/{webhook_id} | Request webhook
[**resetWebhookLifetime**](SettingsApi.md#resetWebhookLifetime) | **POST** /v4/settings/webhooks/{webhook_id}/reset_lifetime | Reset webhook lifetime
[**setSettings**](SettingsApi.md#setSettings) | **PUT** /v4/settings | Set customer settings
[**setSystemRescueKeyPair**](SettingsApi.md#setSystemRescueKeyPair) | **POST** /v4/settings/keypair | Activate client-side encryption for customer
[**toggleNotificationChannels**](SettingsApi.md#toggleNotificationChannels) | **PUT** /v4/settings/notifications/channels | Toggle notification channels
[**updateWebhook**](SettingsApi.md#updateWebhook) | **PUT** /v4/settings/webhooks/{webhook_id} | Update webhook



## createAndPreserveKeyPair

> createAndPreserveKeyPair(createKeyPairRequest, opts)

Create system rescue key pair and preserve copy of old private key

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Create system rescue key pair and preserve copy of old private key.  ### Precondition: * Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; * Existence of own key pair  ### Postcondition: System rescue key pair is created.   Copy of old private key is preserved.  ### Further Information: You can submit your old private key, encrypted with your current password.   This allows migrating file keys encrypted with your old key pair to the new one. 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SettingsApi();
let createKeyPairRequest = new DracoonApi.CreateKeyPairRequest(); // CreateKeyPairRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.createAndPreserveKeyPair(createKeyPairRequest, opts, (error, data, response) => {
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
 **createKeyPairRequest** | [**CreateKeyPairRequest**](CreateKeyPairRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createWebhook

> Webhook createWebhook(createWebhookRequest, opts)

Create webhook

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Create a new webhook for the customer scope.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; required.  ### Postcondition: Webhook is created for given event types.  ### Further Information: URL must begin with the &#x60;HTTPS&#x60; scheme.   Webhook names are limited to 150 characters.  ### Available event types: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Name | Description | Scope | | :--- | :--- | :--- | | **&#x60;user.created&#x60;** | Triggered when a new user is created | Customer Admin Webhook | | **&#x60;user.deleted&#x60;** | Triggered when a user is deleted | Customer Admin Webhook | | **&#x60;user.locked&#x60;** | Triggered when a user gets locked | Customer Admin Webhook | |  |  |  | | **&#x60;webhook.expiring&#x60;** | Triggered 30/20/10/1 days before a webhook expires |  Customer Admin Webhook | |  |  |  | | **&#x60;downloadshare.created&#x60;** | Triggered when a new download share is created in affected room | Node Webhook | | **&#x60;downloadshare.deleted&#x60;** | Triggered when a download share is deleted in affected room | Node Webhook | | **&#x60;downloadshare.used&#x60;** | Triggered when a download share is utilized in affected room | Node Webhook | | **&#x60;uploadshare.created&#x60;** | Triggered when a new upload share is created in affected room | Node Webhook | | **&#x60;uploadshare.deleted&#x60;** | Triggered when a upload share is deleted in affected room | Node Webhook | | **&#x60;uploadshare.used&#x60;** | Triggered when a new file is uploaded via the upload share in affected room | Node Webhook | | **&#x60;file.created&#x60;** | Triggered when a new file is uploaded in affected room | Node Webhook | | **&#x60;folder.created&#x60;** | Triggered when a new folder is created in affected room | Node Webhook | | **&#x60;room.created&#x60;** | Triggered when a new room is created (in affected room) | Node Webhook | | **&#x60;file.deleted&#x60;** | Triggered when a file is deleted in affected room | Node Webhook | | **&#x60;folder.deleted&#x60;** | Triggered when a folder is deleted in affected room | Node Webhook | | **&#x60;room.deleted&#x60;** | Triggered when a room is deleted in affected room | Node Webhook |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SettingsApi();
let createWebhookRequest = new DracoonApi.CreateWebhookRequest(); // CreateWebhookRequest | 
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.createWebhook(createWebhookRequest, opts, (error, data, response) => {
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
 **createWebhookRequest** | [**CreateWebhookRequest**](CreateWebhookRequest.md)|  | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeSystemRescueKeyPair

> removeSystemRescueKeyPair(opts)

Remove system rescue key pair

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Remove the system rescue key pair.  ### Precondition: * Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; * Existence of own key pair  ### Postcondition: Key pair is removed (cf. further information below).  ### Further Information: Please set a new system rescue key pair first and re-encrypt file keys with it.   If no version is set, deleted key pair with lowest preference value.   Although, &#x60;version&#x60; **SHOULD** be set. 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SettingsApi();
let opts = {
  'version': "version_example", // String | Version (NEW)
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.removeSystemRescueKeyPair(opts, (error, data, response) => {
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
 **version** | **String**| Version (NEW) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeWebhook

> removeWebhook(webhookId, opts)

Remove webhook

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Delete a webhook for the customer scope.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; required.  ### Postcondition: Webhook is deleted.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SettingsApi();
let webhookId = 789; // Number | Webhook ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.removeWebhook(webhookId, opts, (error, data, response) => {
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
 **webhookId** | **Number**| Webhook ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestAllSystemRescueKeyPairs

> [UserKeyPairContainer] requestAllSystemRescueKeyPairs(opts)

Request all system rescue key pairs

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Retrieve all system rescue key pairs to allow migrating system-rescue-key-encrypted file keys.  ### Precondition: * Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; * Existence of own key pair  ### Postcondition: List of key pairs is returned.  ### Further Information: In the case of an algorithm migration of a system rescue key, one should create the new key pair before deleting the old one.   This allows re-encrypting file keys with the new key pair, using the old one.    This API allows to retrieve both key pairs, in contrast to &#x60;GET /settings/keypair&#x60;, which only delivers the preferred one. 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SettingsApi();
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestAllSystemRescueKeyPairs(opts, (error, data, response) => {
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
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**[UserKeyPairContainer]**](UserKeyPairContainer.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestListOfEventTypesForConfigManager

> EventTypeList requestListOfEventTypesForConfigManager(opts)

Request list of event types

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Get a list of available (for &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt;) event types.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; required.  ### Postcondition: List of available event types is returned.  ### Further Information: None. 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SettingsApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestListOfEventTypesForConfigManager(opts, (error, data, response) => {
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
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**EventTypeList**](EventTypeList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestListOfWebhooks

> WebhookList requestListOfWebhooks(opts)

Request list of webhooks

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Get a list of webhooks for the customer scope.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; required.  ### Postcondition: List of webhooks is returned.  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;name:cn:goo|createdAt:ge:2015-01-01&#x60;   Get webhooks where name contains &#x60;goo&#x60; **AND** webhook creation date is **&gt;&#x3D;** &#x60;2015-01-01&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | **&#x60;id&#x60;** | Webhook id filter | &#x60;eq&#x60; | Webhook id equals value.&lt;br&gt;Multiple values are allowed and will be connected via logical disjunction (**OR**). |&#x60;positive number&#x60;| | **&#x60;name&#x60;** | Webhook type name| &#x60;cn, eq&#x60; | Webhook name contains / equals value. | &#x60;search String&#x60; | | **&#x60;isEnabled&#x60;** | Webhook isEnabled filter | &#x60;eq&#x60; |  | &#x60;true or false&#x60; | | **&#x60;createdAt&#x60;** | Creation date filter | &#x60;ge, le&#x60; | Creation date is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;createdAt:ge:2016-12-31&#x60;&amp;#124;&#x60;createdAt:le:2018-01-01&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; | | **&#x60;updatedAt&#x60;** | Last modification date filter | &#x60;ge, le&#x60; | Last modification date is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;updatedAt:ge:2016-12-31&#x60;&amp;#124;&#x60;updatedAt:le:2018-01-01&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; | | **&#x60;expiration&#x60;** | Expiration date filter | &#x60;ge, le, eq&#x60; | Expiration date is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;expiration:ge:2016-12-31&#x60;&amp;#124;&#x60;expiration:le:2018-01-01&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; | | **&#x60;lastFailStatus&#x60;** | Failure status filter | &#x60;eq&#x60; | Last HTTP status code. Set when a webhook is auto-disabled due to repeated delivery failures |&#x60;positive number&#x60;|  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;name:desc|isEnabled:asc&#x60;   Sort by &#x60;name&#x60; descending and &#x60;isEnabled&#x60; ascending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | **&#x60;id&#x60;** | Webhook id | | **&#x60;name&#x60;** | Webhook name | | **&#x60;isEnabled&#x60;** | Webhook isEnabled | | **&#x60;createdAt&#x60;** | Creation date | | **&#x60;updatedAt&#x60;** | Last modification date | | **&#x60;expiration&#x60;** | Expiration date |  &lt;/details&gt; 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SettingsApi();
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'offset': 56, // Number | Range offset
  'limit': 56, // Number | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
  'filter': "filter_example", // String | Filter string
  'sort': "sort_example", // String | Sort string
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestListOfWebhooks(opts, (error, data, response) => {
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
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **offset** | **Number**| Range offset | [optional] 
 **limit** | **Number**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] 
 **filter** | **String**| Filter string | [optional] 
 **sort** | **String**| Sort string | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**WebhookList**](WebhookList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestNotificationChannels

> NotificationChannelList requestNotificationChannels(opts)

Request list of notification channels

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description:   Retrieve a list of configured notification channels.  ### Precondition: Right _\&quot;change config\&quot;_ required.  ### Postcondition: List of notification channels is returned.  ### Further Information: None. 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SettingsApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestNotificationChannels(opts, (error, data, response) => {
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
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**NotificationChannelList**](NotificationChannelList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestSettings

> CustomerSettingsResponse requestSettings(opts)

Request customer settings

### Description:   Retrieve customer related settings.   ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read config&lt;/span&gt; required.  ### Postcondition: List of available settings is returned.  ### Further Information: None.  ### Configurable customer settings: &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description                                                                                                                                                           | Value | | :--- |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------| :--- | | &#x60;homeRoomParentName&#x60; | Name of the container in which all user&#39;s home rooms are located.&lt;br&gt;&#x60;null&#x60; if &#x60;homeRoomsActive&#x60; is &#x60;false&#x60;.                                                          | &#x60;String&#x60; | | &#x60;homeRoomQuota&#x60; | Refers to the quota of each single user&#39;s home room.&lt;br&gt;&#x60;0&#x60; represents no quota.&lt;br&gt;&#x60;null&#x60; if &#x60;homeRoomsActive&#x60; is &#x60;false&#x60;.                                           | &#x60;positive Long&#x60; | | &#x60;homeRoomsActive&#x60; | If set to &#x60;true&#x60;, every user with an Active Directory account or OpenID Connect account gets a personal homeroom.&lt;br&gt;Once activated, this **CANNOT** be deactivated. | &#x60;true or false&#x60; |   &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SettingsApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestSettings(opts, (error, data, response) => {
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
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**CustomerSettingsResponse**](CustomerSettingsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestSystemRescueKeyPair

> UserKeyPairContainer requestSystemRescueKeyPair(opts)

Request system rescue key pair

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Retrieve the system rescue key pair.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt;  ### Postcondition: Key pair is returned.  ### Further Information: If more than one key pair exists the one with highest preference value is returned. 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SettingsApi();
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'version': "version_example", // String | Version (NEW)
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestSystemRescueKeyPair(opts, (error, data, response) => {
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
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **version** | **String**| Version (NEW) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**UserKeyPairContainer**](UserKeyPairContainer.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestWebhook

> Webhook requestWebhook(webhookId, opts)

Request webhook

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Get a specific webhook for the customer scope.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; required.  ### Postcondition: Webhook is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SettingsApi();
let webhookId = 789; // Number | Webhook ID
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestWebhook(webhookId, opts, (error, data, response) => {
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
 **webhookId** | **Number**| Webhook ID | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resetWebhookLifetime

> Webhook resetWebhookLifetime(webhookId, opts)

Reset webhook lifetime

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Reset the lifetime of a webhook for the customer scope.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; required.  ### Postcondition: Lifetime of the webhook is reset.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SettingsApi();
let webhookId = 789; // Number | Webhook ID
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.resetWebhookLifetime(webhookId, opts, (error, data, response) => {
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
 **webhookId** | **Number**| Webhook ID | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setSettings

> CustomerSettingsResponse setSettings(customerSettingsRequest, opts)

Set customer settings

### Description:   Set customer related settings.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; required.  ### Postcondition: Provided settings are updated.  ### Further Information: None.  ### Configurable customer settings &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description                                                                                                                                                          | Value | | :--- |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------| :--- | | &#x60;homeRoomParentName&#x60; | Name of the container in which all user&#39;s home rooms are located.&lt;br&gt;&#x60;null&#x60; if &#x60;homeRoomsActive&#x60; is &#x60;false&#x60;.                                                         | &#x60;String&#x60; | | &#x60;homeRoomQuota&#x60; | Refers to the quota of each single user&#39;s home room.&lt;br&gt;&#x60;0&#x60; represents no quota.&lt;br&gt;&#x60;null&#x60; if &#x60;homeRoomsActive&#x60; is &#x60;false&#x60;.                                          | &#x60;positive Long&#x60; | | &#x60;homeRoomsActive&#x60; | If set to &#x60;true&#x60;, every user with an Active Directory account or OpenID Connect account gets a personal homeroom.&lt;br&gt;Once activated, this **CANNOT** be deactivated. | &#x60;true or false&#x60; |  &lt;/details&gt;  ### Node naming convention: * Node (room, folder, file) names are limited to **150** characters. * Illegal names:   &#x60;&#39;CON&#39;, &#39;PRN&#39;, &#39;AUX&#39;, &#39;NUL&#39;, &#39;COM1&#39;, &#39;COM2&#39;, &#39;COM3&#39;, &#39;COM4&#39;, &#39;COM5&#39;, &#39;COM6&#39;, &#39;COM7&#39;, &#39;COM8&#39;, &#39;COM9&#39;, &#39;LPT1&#39;, &#39;LPT2&#39;, &#39;LPT3&#39;, &#39;LPT4&#39;, &#39;LPT5&#39;, &#39;LPT6&#39;, &#39;LPT7&#39;, &#39;LPT8&#39;, &#39;LPT9&#39;, (and any of those with an extension)&#x60; * Illegal characters in names:   &#x60;&#39;\\\\&#39;, &#39;&lt;&#39;,&#39;&gt;&#39;, &#39;:&#39;, &#39;\\\&quot;&#39;, &#39;|&#39;, &#39;?&#39;, &#39;*&#39;, &#39;/&#39;, leading &#39;-&#39;, trailing &#39;.&#39; &#x60; 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SettingsApi();
let customerSettingsRequest = new DracoonApi.CustomerSettingsRequest(); // CustomerSettingsRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.setSettings(customerSettingsRequest, opts, (error, data, response) => {
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
 **customerSettingsRequest** | [**CustomerSettingsRequest**](CustomerSettingsRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**CustomerSettingsResponse**](CustomerSettingsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setSystemRescueKeyPair

> setSystemRescueKeyPair(userKeyPairContainer, opts)

Activate client-side encryption for customer

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Set the system rescue key pair and activate client-side encryption for according customer.  ### Precondition: * Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; * Existence of own key pair  ### Postcondition: System rescue key pair is set and client-side encryption is enabled.  ### Further Information: Sets the ability for this customer to encrypt rooms.   Once enabled on customer level, it **CANNOT** be unset.   On activation, a customer rescue key pair **MUST** be set. 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SettingsApi();
let userKeyPairContainer = new DracoonApi.UserKeyPairContainer(); // UserKeyPairContainer | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.setSystemRescueKeyPair(userKeyPairContainer, opts, (error, data, response) => {
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
 **userKeyPairContainer** | [**UserKeyPairContainer**](UserKeyPairContainer.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## toggleNotificationChannels

> NotificationChannelList toggleNotificationChannels(notificationChannelActivationRequest, opts)

Toggle notification channels

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description:   Toggle configured notification channels.  ### Precondition: Right _\&quot;change config\&quot;_ required.  ### Postcondition: Channel status is switched.  ### Further Information: None. 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SettingsApi();
let notificationChannelActivationRequest = new DracoonApi.NotificationChannelActivationRequest(); // NotificationChannelActivationRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.toggleNotificationChannels(notificationChannelActivationRequest, opts, (error, data, response) => {
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
 **notificationChannelActivationRequest** | [**NotificationChannelActivationRequest**](NotificationChannelActivationRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**NotificationChannelList**](NotificationChannelList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateWebhook

> Webhook updateWebhook(webhookId, updateWebhookRequest, opts)

Update webhook

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Update an existing webhook for the customer scope.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; required.  ### Postcondition: Webhook is updated.  ### Further Information: URL must begin with the &#x60;HTTPS&#x60; scheme. Webhook names are limited to 150 characters. Webhook event types can not be changed from Customer Admin Webhook types to Node Webhook types and vice versa    ### Available event types: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Name | Description | Scope | | :--- | :--- | :--- | | **&#x60;user.created&#x60;** | Triggered when a new user is created | Customer Admin Webhook | | **&#x60;user.deleted&#x60;** | Triggered when a user is deleted | Customer Admin Webhook | | **&#x60;user.locked&#x60;** | Triggered when a user gets locked | Customer Admin Webhook | |  |  |  | | **&#x60;webhook.expiring&#x60;** | Triggered 30/20/10/1 days before a webhook expires |  Customer Admin Webhook | |  |  |  | | **&#x60;downloadshare.created&#x60;** | Triggered when a new download share is created in affected room | Node Webhook | | **&#x60;downloadshare.deleted&#x60;** | Triggered when a download share is deleted in affected room | Node Webhook | | **&#x60;downloadshare.used&#x60;** | Triggered when a download share is utilized in affected room | Node Webhook | | **&#x60;uploadshare.created&#x60;** | Triggered when a new upload share is created in affected room | Node Webhook | | **&#x60;uploadshare.deleted&#x60;** | Triggered when a upload share is deleted in affected room | Node Webhook | | **&#x60;uploadshare.used&#x60;** | Triggered when a new file is uploaded via the upload share in affected room | Node Webhook | | **&#x60;file.created&#x60;** | Triggered when a new file is uploaded in affected room | Node Webhook | | **&#x60;folder.created&#x60;** | Triggered when a new folder is created in affected room | Node Webhook | | **&#x60;room.created&#x60;** | Triggered when a new room is created (in affected room) | Node Webhook | | **&#x60;file.deleted&#x60;** | Triggered when a file is deleted in affected room | Node Webhook | | **&#x60;folder.deleted&#x60;** | Triggered when a folder is deleted in affected room | Node Webhook | | **&#x60;room.deleted&#x60;** | Triggered when a room is deleted in affected room | Node Webhook |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SettingsApi();
let webhookId = 789; // Number | Webhook ID
let updateWebhookRequest = new DracoonApi.UpdateWebhookRequest(); // UpdateWebhookRequest | 
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateWebhook(webhookId, updateWebhookRequest, opts, (error, data, response) => {
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
 **webhookId** | **Number**| Webhook ID | 
 **updateWebhookRequest** | [**UpdateWebhookRequest**](UpdateWebhookRequest.md)|  | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

