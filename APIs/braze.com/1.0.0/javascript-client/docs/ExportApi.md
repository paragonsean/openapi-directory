# BrazeEndpoints.ExportApi

All URIs are relative to *https://rest.iad-01.braze.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appSessionsByTime**](ExportApi.md#appSessionsByTime) | **GET** /sessions/data_series | App Sessions by Time
[**campaignAnalytics**](ExportApi.md#campaignAnalytics) | **GET** /campaigns/data_series | Campaign Analytics
[**campaignDetails**](ExportApi.md#campaignDetails) | **GET** /campaigns/details | Campaign Details
[**campaignList**](ExportApi.md#campaignList) | **GET** /campaigns/list | Campaign List
[**canvasDataAnalyticsSummary**](ExportApi.md#canvasDataAnalyticsSummary) | **GET** /canvas/data_summary | Canvas Data Analytics Summary
[**canvasDataSeriesAnalytics**](ExportApi.md#canvasDataSeriesAnalytics) | **GET** /canvas/data_series | Canvas Data Series Analytics
[**canvasDetails**](ExportApi.md#canvasDetails) | **GET** /canvas/details | Canvas Details
[**canvasList**](ExportApi.md#canvasList) | **GET** /canvas/list | Canvas List
[**customEventsAnalytics**](ExportApi.md#customEventsAnalytics) | **GET** /events/data_series | Custom Events Analytics
[**customEventsList**](ExportApi.md#customEventsList) | **GET** /events/list | Custom Events List
[**dailyActiveUsersByDate**](ExportApi.md#dailyActiveUsersByDate) | **GET** /kpi/dau/data_series | Daily Active Users by Date
[**dailyNewUsersByDate**](ExportApi.md#dailyNewUsersByDate) | **GET** /kpi/new_users/data_series | Daily New Users by Date
[**kpIsForDailyAppUninstallsByDate**](ExportApi.md#kpIsForDailyAppUninstallsByDate) | **GET** /kpi/uninstalls/data_series | KPIs for Daily App Uninstalls by Date
[**monthlyActiveUsersForLast30Days**](ExportApi.md#monthlyActiveUsersForLast30Days) | **GET** /kpi/mau/data_series | Monthly Active Users for Last 30 Days
[**newsFeedCardAnalytics**](ExportApi.md#newsFeedCardAnalytics) | **GET** /feed/data_series | News Feed Card Analytics
[**newsFeedCardsDetails**](ExportApi.md#newsFeedCardsDetails) | **GET** /feed/details | News Feed Cards Details
[**newsFeedCardsList**](ExportApi.md#newsFeedCardsList) | **GET** /feed/list | News Feed Cards List
[**segmentAnalytics**](ExportApi.md#segmentAnalytics) | **GET** /segments/data_series | Segment Analytics
[**segmentDetails**](ExportApi.md#segmentDetails) | **GET** /segments/details | Segment Details
[**segmentList**](ExportApi.md#segmentList) | **GET** /segments/list | Segment List
[**sendAnalytics**](ExportApi.md#sendAnalytics) | **GET** /sends/data_series | Send Analytics



## appSessionsByTime

> appSessionsByTime(opts)

App Sessions by Time

This endpoint allows you to retrieve a series of the number of sessions for your app over a designated time period.  ### Components Used - [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) point in time - as ISO 8601 extended when unit is \&quot;hour\&quot; and as ISO 8601 date when unit is \&quot;day\&quot;,             \&quot;sessions\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.ExportApi();
let opts = {
  'length': "14", // String | (Required) Integer  Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive.
  'unit': "day", // String | (Optional) String  Unit of time between data points - can be \"day\" or \"hour\" (defaults to \"day\"). 
  'endingAt': "2018-06-28T23:59:59-5:00", // String | (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request.
  'appId': "{{app_identifier}}", // String | (Optional) String  App API identifier retrieved from the Developer Console to limit analytics to a specific app.
  'segmentId': "{{segment_identifier}}" // String | (Optional) String  Segment API identifier indicating the analytics enabled segment for which sessions should be returned.
};
apiInstance.appSessionsByTime(opts, (error, data, response) => {
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
 **length** | **String**| (Required) Integer  Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive. | [optional] 
 **unit** | **String**| (Optional) String  Unit of time between data points - can be \&quot;day\&quot; or \&quot;hour\&quot; (defaults to \&quot;day\&quot;).  | [optional] 
 **endingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request. | [optional] 
 **appId** | **String**| (Optional) String  App API identifier retrieved from the Developer Console to limit analytics to a specific app. | [optional] 
 **segmentId** | **String**| (Optional) String  Segment API identifier indicating the analytics enabled segment for which sessions should be returned. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## campaignAnalytics

> campaignAnalytics(opts)

Campaign Analytics

This endpoint allows you to retrieve a daily series of various stats for a campaign over time. Data returned includes how many messages were sent, opened, clicked, converted, etc., broken down by message channel.   ### Components Used -[Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)   ### Responses  #### Multi-Channel Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;messages\&quot; : {                 \&quot;ios_push\&quot; : [                     {                       \&quot;variation_name\&quot;: \&quot;iOS_Push\&quot;,                       \&quot;sent\&quot; : (int),                       \&quot;direct_opens\&quot; : (int),                       \&quot;total_opens\&quot; : (int),                       \&quot;bounces\&quot; : (int),                       \&quot;body_clicks\&quot; : (int)                       \&quot;revenue\&quot;: 0,                       \&quot;unique_recipients\&quot;: 1,                       \&quot;conversions\&quot;: 0,                       \&quot;conversions_by_send_time\&quot;: 0,                       \&quot;conversions1\&quot;: 0,                       \&quot;conversions1_by_send_time\&quot;: 0,                       \&quot;conversions2\&quot;: 0,                       \&quot;conversions2_by_send_time\&quot;: 0,                       \&quot;conversions3\&quot;: 0,                       \&quot;conversions3_by_send_time\&quot;: 0,                       \&quot;carousel_slide_[NUM]_[TITLE]_click\&quot;: (optional, int),                       \&quot;notif_button_[NUM]_[TITLE]_click\&quot;: (optional, int)                     }                 ],                 \&quot;android_push\&quot; : [                     {                       \&quot;sent\&quot; : (int),                       \&quot;direct_opens\&quot; : (int),                       \&quot;total_opens\&quot; : (int),                       \&quot;bounces\&quot; : (int),                       \&quot;body_clicks\&quot; : (int)                     }                 ],                 \&quot;webhook\&quot;: [                     {                       \&quot;sent\&quot;: (int),                       \&quot;errors\&quot;: (int)                     }                 ],                 \&quot;email\&quot; : [                     {                       \&quot;sent\&quot;: (int),                       \&quot;opens\&quot;: (int),                       \&quot;unique_opens\&quot;: (int),                       \&quot;clicks\&quot;: (int),                       \&quot;unique_clicks\&quot;: (int),                       \&quot;unsubscribes\&quot;: (int),                       \&quot;bounces\&quot;: (int),                       \&quot;delivered\&quot;: (int),                       \&quot;reported_spam\&quot;: (int)                     }                 ],                 \&quot;sms\&quot; : [                   {                     \&quot;sent\&quot;: (int),                     \&quot;delivered\&quot;: (int),                     \&quot;undelivered\&quot;: (int),                     \&quot;delivery_failed\&quot;: (int)                   }                 ]               },            \&quot;conversions_by_send_time\&quot;: (optional, int),            \&quot;conversions1_by_send_time\&quot;: (optional, int),            \&quot;conversions2_by_send_time\&quot;: (optional, int),            \&quot;conversions3_by_send_time\&quot;: (optional, int),            \&quot;conversions\&quot;: (int),            \&quot;conversions1\&quot;: (optional, int),            \&quot;conversions2\&quot;: (optional, int),            \&quot;conversions3\&quot;: (optional, int),            \&quot;unique_recipients\&quot;: (int),            \&quot;revenue\&quot;: (optional, float)         },         ...     ],     ... } &#x60;&#x60;&#x60;  #### Multivariate Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;conversions\&quot; : (int),             \&quot;revenue\&quot;: (float),             \&quot;conversions_by_send_time\&quot;: (int),             \&quot;messages\&quot; : {                \&quot;trigger_in_app_message\&quot;: [{           \&quot;variation_name\&quot;: (optional, string),           \&quot;impressions\&quot;: (int),           \&quot;clicks\&quot;: (int),           \&quot;first_button_clicks\&quot;: (int),           \&quot;second_button_clicks\&quot;: (int),           \&quot;revenue\&quot;: (optional, float),,           \&quot;unique_recipients\&quot;: (int),           \&quot;conversions\&quot;: (optional, int),           \&quot;conversions_by_send_time\&quot;: (optional, int),           \&quot;conversions1\&quot;: (optional, int),           \&quot;conversions1_by_send_time\&quot;: (optional, int),           \&quot;conversions2\&quot;: (optional, int),           \&quot;conversions2_by_send_time\&quot;: (optional, int),           \&quot;conversions3\&quot;: (optional, int),           \&quot;conversions3_by_send_time\&quot;: (optional, int)          }, {           \&quot;variation_name\&quot;: (optional, string),           \&quot;impressions\&quot;: (int),           \&quot;clicks\&quot;: (int),           \&quot;first_button_clicks\&quot;: (int),           \&quot;second_button_clicks\&quot;: (int),           \&quot;revenue\&quot;: (optional, float),,           \&quot;unique_recipients\&quot;: (int),           \&quot;conversions\&quot;: (optional, int),           \&quot;conversions_by_send_time\&quot;: (optional, int),           \&quot;conversions1\&quot;: (optional, int),           \&quot;conversions1_by_send_time\&quot;: (optional, int),           \&quot;conversions2\&quot;: (optional, int),           \&quot;conversions2_by_send_time\&quot;: (optional, int),           \&quot;conversions3\&quot;: (optional, int).           \&quot;conversions3_by_send_time\&quot;: (optional, int)          }, {           \&quot;variation_name\&quot;: (optional, string),           \&quot;revenue\&quot;: (optional, float),,           \&quot;unique_recipients\&quot;: (int),           \&quot;conversions\&quot;: (optional, int),           \&quot;conversions_by_send_time\&quot;: (optional, int),           \&quot;conversions1\&quot;: (optional, int),           \&quot;conversions1_by_send_time\&quot;: (optional, int),           \&quot;conversions2\&quot;: (optional, int),           \&quot;conversions2_by_send_time\&quot;: (optional, int),           \&quot;conversions3\&quot;: (optional, int),           \&quot;conversions3_by_send_time\&quot;: (optional, int),           \&quot;enrolled\&quot;: (optional, int)          }]         },         \&quot;conversions_by_send_time\&quot;: (optional, int),         \&quot;conversions1_by_send_time\&quot;: (optional, int),         \&quot;conversions2_by_send_time\&quot;: (optional, int),         \&quot;conversions3_by_send_time\&quot;: (optional, int),         \&quot;conversions\&quot;: (optional, int,         \&quot;conversions1\&quot;: (optional, int),         \&quot;conversions2\&quot;: (optional, int),         \&quot;conversions3\&quot;: (optional, int),         \&quot;unique_recipients\&quot;: (int),         \&quot;revenue\&quot;: (optional, float)          }],          ... } &#x60;&#x60;&#x60;  Possible message types are &#x60;email&#x60;, &#x60;in_app_message&#x60;, &#x60;webhook&#x60;, &#x60;android_push&#x60;, &#x60;apple_push&#x60;, &#x60;kindle_push&#x60;, &#x60;web_push&#x60;, &#x60;windows_phone8_push&#x60;, and &#x60;windows_universal_push&#x60;. All push message types will have the same statistics shown for &#x60;android_push&#x60; above.

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.ExportApi();
let opts = {
  'campaignId': "{{campaign_identifier}}", // String | (Required) String  Campaign API identifier
  'length': "7", // String | (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
  'endingAt': "2020-06-28T23:59:59-5:00" // String | (Optional) DateTime (ISO 8601 string)  Date on which the data series should end - defaults to time of the request
};
apiInstance.campaignAnalytics(opts, (error, data, response) => {
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
 **campaignId** | **String**| (Required) String  Campaign API identifier | [optional] 
 **length** | **String**| (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive | [optional] 
 **endingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Date on which the data series should end - defaults to time of the request | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## campaignDetails

> campaignDetails(opts)

Campaign Details

This endpoint allows you to retrieve relevant information on a specified campaign, which can be identified by the &#x60;campaign_id&#x60;.   &gt; The campaign_id for API campaigns can be found on the Developer Console page and the campaign details page within your dashboard or you can use the Campaign List Endpoint.  ### Components Used - [Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)   ### Campaign Details Endpoint API Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;created_at\&quot; : (string) date created as ISO 8601 date,     \&quot;updated_at\&quot; : (string) date last updated as ISO 8601 date,     \&quot;archived\&quot;: (boolean) whether this Campaign is archived,     \&quot;draft\&quot;: (boolean) whether this Campaign is a draft,     \&quot;name\&quot; : (string) campaign name,     \&quot;description\&quot; : (string) campaign description,     \&quot;schedule_type\&quot; : (string) type of scheduling action,     \&quot;channels\&quot; : (array) list of channels to send via,     \&quot;first_sent\&quot; : (string) date and hour of first sent as ISO 8601 date,     \&quot;last_sent\&quot; : (string) date and hour of last sent as ISO 8601 date,     \&quot;tags\&quot; : (array) tag names associated with the campaign,     \&quot;messages\&quot;: {         \&quot;message_variation_id\&quot;: (string) { // &lt;&#x3D;This is the actual id             \&quot;channel\&quot;: (string) channel type of the message (as in, \&quot;email\&quot;, \&quot;ios_push\&quot;, \&quot;webhook\&quot;, \&quot;content_card\&quot;, \&quot;in-app_message\&quot;, \&quot;sms\&quot;),             \&quot;name\&quot;: (string) name of the message in the Dashboard (eg., \&quot;Variation 1\&quot;)             ... channel-specific fields for this message, see below ...         }     },     \&quot;conversion_behaviors\&quot;: (array) conversion event behaviors assigned to the campaign (see below) } &#x60;&#x60;&#x60;  #### Messages  The &#x60;messages&#x60; response will contain information about each message. Example message responses for channels are below:  ##### Push Channels  &#x60;&#x60;&#x60;json {     \&quot;channel\&quot;: (string) description of the channel, such as \&quot;ios_push\&quot; or \&quot;android_push\&quot;     \&quot;alert\&quot;: (string) alert body text,     \&quot;extras\&quot;: (hash) any key value pairs provided } &#x60;&#x60;&#x60;  ##### Email Channel  &#x60;&#x60;&#x60;json {     \&quot;channel\&quot;: \&quot;email\&quot;,     \&quot;subject\&quot;: (string) subject,     \&quot;body\&quot;: (string) HTML body,     \&quot;from\&quot;: (string) from address and display name,     \&quot;reply_to\&quot;: (string) reply-to for message, if different than \&quot;from\&quot; address,     \&quot;title\&quot;: (string) name of the email,     \&quot;extras\&quot;: (hash) any key value pairs provided } &#x60;&#x60;&#x60;  ##### Content Card Channel  &#x60;&#x60;&#x60;json {     \&quot;channel\&quot;: \&quot;content_cards\&quot;,     \&quot;name\&quot;: (string) name of variant,     \&quot;extras\&quot;: (hash) any key value pairs provided; only present if at least one key-value pair has been set } &#x60;&#x60;&#x60;  ##### Webhook Channel  &#x60;&#x60;&#x60;json {     \&quot;channel\&quot;: \&quot;webhook\&quot;,     \&quot;url\&quot;: (string) url for webhook,     \&quot;body\&quot;: (string) payload body,     \&quot;type\&quot;: (string) body content type,     \&quot;headers\&quot;: (hash) specified request headers,     \&quot;method\&quot;: (string) HTTP method (e.g., \&quot;POST\&quot; or \&quot;GET\&quot;), } &#x60;&#x60;&#x60;  ##### SMS Channel  &#x60;&#x60;&#x60;json {   \&quot;channel\&quot;: \&quot;sms\&quot;,   \&quot;body\&quot;: (string) payload body,   \&quot;from\&quot;: (string) list of numbers associated with the subscription group,   \&quot;subscription_group_id\&quot;: (string) API id of the subscription group targeted in the SMS message } &#x60;&#x60;&#x60;  ##### Control Messages  &#x60;&#x60;&#x60;json {     \&quot;channel\&quot;: (string) description of the channel that the control is for,     \&quot;type\&quot;: \&quot;control\&quot; } &#x60;&#x60;&#x60;  #### Conversion Behaviors  The &#x60;conversion_behaviors&#x60; array will contain information about each conversion event behavior set for the campaign. These behaviors are in order as set by the campaign. For example, Conversion Event A will be the first item in the array, Conversion Event B will be second, etc. Example conversion event behavior responses for are below:  ##### Clicks Email  &#x60;&#x60;&#x60;json {     \&quot;type\&quot;: \&quot;Clicks Email\&quot;,     \&quot;window\&quot;: (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours } &#x60;&#x60;&#x60;  ##### Opens Email  &#x60;&#x60;&#x60;json {     \&quot;type\&quot;: \&quot;Opens Email\&quot;,     \&quot;window\&quot;: (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours } &#x60;&#x60;&#x60;  ##### Makes Purchase (any purchase)  &#x60;&#x60;&#x60;json {     \&quot;type\&quot;: \&quot;Makes Any Purchase\&quot;,     \&quot;window\&quot;: (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours } &#x60;&#x60;&#x60;  ##### Makes Purchase (specific product)  &#x60;&#x60;&#x60;json {     \&quot;type\&quot;: \&quot;Makes Specific Purchase\&quot;,     \&quot;window\&quot;: (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,     \&quot;product\&quot;: (string) name of the product, i.e. - \&quot;Feline Body Armor\&quot; } &#x60;&#x60;&#x60;  ##### Performs Custom Event  &#x60;&#x60;&#x60;json {     \&quot;type\&quot;: \&quot;Performs Custom Event\&quot;,     \&quot;window\&quot;: (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,     \&quot;custom_event_name\&quot;: (string) name of the event, i.e. - \&quot;Used Feline Body Armor\&quot; } &#x60;&#x60;&#x60;  ##### Upgrades App  &#x60;&#x60;&#x60;json {     \&quot;type\&quot;: \&quot;Upgrades App\&quot;,     \&quot;window\&quot;: (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,     \&quot;app_ids\&quot;: (array|null) array of app ids, i.e. - [\&quot;12345\&quot;, \&quot;67890\&quot;], or &#x60;null&#x60; if \&quot;Track sessions for any app\&quot; is selected in the UI } &#x60;&#x60;&#x60;  ##### Uses App  &#x60;&#x60;&#x60;json {     \&quot;type\&quot;: \&quot;Starts Session\&quot;,     \&quot;window\&quot;: (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,     \&quot;app_ids\&quot;: (array|null) array of app ids, i.e. - [\&quot;12345\&quot;, \&quot;67890\&quot;], or &#x60;null&#x60; if \&quot;Track sessions for any app\&quot; is selected in the UI } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.ExportApi();
let opts = {
  'campaignId': "{{campaign_identifier}}" // String | (Required) String  Campaign API identifier
};
apiInstance.campaignDetails(opts, (error, data, response) => {
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
 **campaignId** | **String**| (Required) String  Campaign API identifier | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## campaignList

> campaignList(opts)

Campaign List

This endpoint allows you to export a list of campaigns, each of which will include its name, Campaign API Identifier, whether it is an API Campaign, and Tags associated with the campaign. The campaigns are returned in groups of 100 sorted by time of creation (oldest to newest by default).  ## Campaign List Endpoint API Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;campaigns\&quot; : [         {             \&quot;id\&quot; : (string) Campaign API Identifier,             \&quot;last_edited\&quot;: (ISO 8601 string) the last edited time for the message              \&quot;name\&quot; : (string) campaign name,             \&quot;is_api_campaign\&quot; : (boolean) whether the campaign is an API Campaign,             \&quot;tags\&quot; : (array) tag names associated with the campaign         },         ...     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.ExportApi();
let opts = {
  'page': "0", // String | (Optional) Integer  The page of campaigns to return, defaults to 0 (returns the first set of up to 100)
  'includeArchived': "false", // String | (Optional) Boolean  Whether or not to include archived campaigns, defaults to false
  'sortDirection': "desc", // String | (Optional) String  Pass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest.
  'lastEditTimeGt': "2020-06-28T23:59:59-5:00" // String | (Optional) DateTime (ISO 8601 string)  Filters the results and only returns campaigns that were edited greater than the time provided till now. 
};
apiInstance.campaignList(opts, (error, data, response) => {
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
 **page** | **String**| (Optional) Integer  The page of campaigns to return, defaults to 0 (returns the first set of up to 100) | [optional] 
 **includeArchived** | **String**| (Optional) Boolean  Whether or not to include archived campaigns, defaults to false | [optional] 
 **sortDirection** | **String**| (Optional) String  Pass in the value &#x60;desc&#x60; to sort by creation time from newest to oldest. Pass in &#x60;asc&#x60; to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest. | [optional] 
 **lastEditTimeGt** | **String**| (Optional) DateTime (ISO 8601 string)  Filters the results and only returns campaigns that were edited greater than the time provided till now.  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## canvasDataAnalyticsSummary

> canvasDataAnalyticsSummary(opts)

Canvas Data Analytics Summary

This endpoint allows you to export rollups of time series data for a Canvas, providing a concise summary of a Canvas&#39; results.  ### Components Used - [Canvas Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   \&quot;data\&quot;: {     \&quot;name\&quot;: (string) Canvas name,     \&quot;total_stats\&quot;: {       \&quot;revenue\&quot;: (float),       \&quot;conversions\&quot;: (int),       \&quot;conversions_by_entry_time\&quot;: (int),       \&quot;entries\&quot;: (int)     },     \&quot;variant_stats\&quot;: (optional) {       \&quot;00000000-0000-0000-0000-0000000000000\&quot;: (API identifier for variant) {         \&quot;name\&quot;: (string) name of variant,         \&quot;revenue\&quot;: (float),         \&quot;conversions\&quot;: (int),         \&quot;entries\&quot;: (int)       },       ... (more variants)     },     \&quot;step_stats\&quot;: (optional) {       \&quot;00000000-0000-0000-0000-0000000000000\&quot;: (API identifier for step) {         \&quot;name\&quot;: (string) name of step,         \&quot;revenue\&quot;: (float),         \&quot;conversions\&quot;: (int),         \&quot;conversions_by_entry_time\&quot;: (int),         \&quot;messages\&quot;: {           \&quot;android_push\&quot;: (name of channel) [             {               \&quot;sent\&quot;: (int),               \&quot;opens\&quot;: (int),               \&quot;influenced_opens\&quot;: (int),               \&quot;bounces\&quot;: (int)               ... (more stats for channel)             }           ],           ... (more channels)         }       },       ... (more steps)     }   },   \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.ExportApi();
let opts = {
  'canvasId': "{{canvas_id}}", // String | (Required) String   Canvas API identifier
  'endingAt': "2018-05-30T23:59:59-5:00", // String | (Required) DateTime (ISO 8601 string)  Date on which the data export should end - defaults to time of the request
  'startingAt': "2018-05-28T23:59:59-5:00", // String | (Optional) DateTime (ISO 8601 string)  Date on which the data export should begin (either length or starting_at required)
  'length': "5", // String | (Optional) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 14 inclusive (either length or starting_at required)
  'includeVariantBreakdown': "true", // String | (Optional) Boolean  Whether or not to include variant stats (defaults to false)
  'includeStepBreakdown': "true", // String | (Optional) Boolean  Whether or not to include step stats (defaults to false)
  'includeDeletedStepData': "true" // String | (Optional) Boolean  Whether or not to include step stats for deleted steps (defaults to false)
};
apiInstance.canvasDataAnalyticsSummary(opts, (error, data, response) => {
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
 **canvasId** | **String**| (Required) String   Canvas API identifier | [optional] 
 **endingAt** | **String**| (Required) DateTime (ISO 8601 string)  Date on which the data export should end - defaults to time of the request | [optional] 
 **startingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Date on which the data export should begin (either length or starting_at required) | [optional] 
 **length** | **String**| (Optional) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 14 inclusive (either length or starting_at required) | [optional] 
 **includeVariantBreakdown** | **String**| (Optional) Boolean  Whether or not to include variant stats (defaults to false) | [optional] 
 **includeStepBreakdown** | **String**| (Optional) Boolean  Whether or not to include step stats (defaults to false) | [optional] 
 **includeDeletedStepData** | **String**| (Optional) Boolean  Whether or not to include step stats for deleted steps (defaults to false) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## canvasDataSeriesAnalytics

> canvasDataSeriesAnalytics(opts)

Canvas Data Series Analytics

This endpoint allows you to export time series data for a Canvas.  ### Components Used - [Canvas Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   \&quot;data\&quot;: {     \&quot;name\&quot;: (string) Canvas name,     \&quot;stats\&quot;: [       {         \&quot;time\&quot;: (string) date as ISO 8601 date,         \&quot;total_stats\&quot;: {           \&quot;revenue\&quot;: (float),           \&quot;conversions\&quot;: (int),           \&quot;conversions_by_entry_time\&quot;: (int),           \&quot;entries\&quot;: (int)         },         \&quot;variant_stats\&quot;: (optional) {           \&quot;00000000-0000-0000-0000-0000000000000\&quot;: (API identifier for variant) {             \&quot;name\&quot;: (string) name of variant,             \&quot;revenue\&quot;: (int),             \&quot;conversions\&quot;: (int),             \&quot;conversions_by_entry_time\&quot;: (int),             \&quot;entries\&quot;: (int)           },           ... (more variants)         },         \&quot;step_stats\&quot;: (optional) {           \&quot;00000000-0000-0000-0000-0000000000000\&quot;: (API identifier for step) {             \&quot;name\&quot;: (string) name of step,             \&quot;revenue\&quot;: (float),             \&quot;conversions\&quot;: (int),             \&quot;conversions_by_entry_time\&quot;: (int),             \&quot;messages\&quot;: {               \&quot;email\&quot;: [                 {                   \&quot;sent\&quot;: (int),                   \&quot;opens\&quot;: (int),                   \&quot;unique_opens\&quot;: (int),                   \&quot;clicks\&quot;: (int),                   ... (more stats)                 }               ],               ... (more channels)             }           },           ... (more steps)         }       },       ... (more stats by time)     ]   },   \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.ExportApi();
let opts = {
  'canvasId': "{{canvas_id}}", // String | (Required) String  Canvas API Identifier
  'endingAt': "2018-05-30T23:59:59-5:00", // String | (Required) DateTime (ISO 8601 string)  Date on which the data export should end - defaults to time of the request
  'startingAt': "2018-05-28T23:59:59-5:00", // String | (Optional) DateTime (ISO 8601 string)   Date on which the data export should begin (either length or starting_at are required)
  'length': "10", // String | (Optional) DateTime (ISO 8601 string)  Max number of days before ending_at to include in the returned series - must be between 1 and 14 inclusive (either length or starting_at required)
  'includeVariantBreakdown': "true", // String | (Optional) Boolean  Whether or not to include variant stats (defaults to false)
  'includeStepBreakdown': "true", // String | (Optional) Boolean  Whether or not to include step stats (defaults to false)
  'includeDeletedStepData': "true" // String | (Optional) Boolean  Whether or not to include step stats for deleted steps (defaults to false)
};
apiInstance.canvasDataSeriesAnalytics(opts, (error, data, response) => {
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
 **canvasId** | **String**| (Required) String  Canvas API Identifier | [optional] 
 **endingAt** | **String**| (Required) DateTime (ISO 8601 string)  Date on which the data export should end - defaults to time of the request | [optional] 
 **startingAt** | **String**| (Optional) DateTime (ISO 8601 string)   Date on which the data export should begin (either length or starting_at are required) | [optional] 
 **length** | **String**| (Optional) DateTime (ISO 8601 string)  Max number of days before ending_at to include in the returned series - must be between 1 and 14 inclusive (either length or starting_at required) | [optional] 
 **includeVariantBreakdown** | **String**| (Optional) Boolean  Whether or not to include variant stats (defaults to false) | [optional] 
 **includeStepBreakdown** | **String**| (Optional) Boolean  Whether or not to include step stats (defaults to false) | [optional] 
 **includeDeletedStepData** | **String**| (Optional) Boolean  Whether or not to include step stats for deleted steps (defaults to false) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## canvasDetails

> canvasDetails(opts)

Canvas Details

This endpoint allows you to export metadata about a Canvas, such as its name, when it was created, its current status, and more.  ### Components Used - [Canvas Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   \&quot;created_at\&quot;: (string) date created as ISO 8601 date,   \&quot;updated_at\&quot;: (string) date updated as ISO 8601 date,   \&quot;name\&quot;: (string) Canvas name,   \&quot;description\&quot;: (string) Canvas description,   \&quot;archived\&quot;: (boolean) whether this Canvas is archived,   \&quot;draft\&quot;: (boolean) whether this Canvas is a draft,   \&quot;schedule_type\&quot;: (string) type of scheduling action,   \&quot;first_entry\&quot;: (string) date of first entry as ISO 8601 date,   \&quot;last_entry\&quot;: (string) date of last entry as ISO 8601 date,   \&quot;channels\&quot;: (array of strings) step channels used with Canvas,   \&quot;variants\&quot;: [     {       \&quot;name\&quot;: (string) name of variant,       \&quot;id\&quot;: (string) API identifier of the variant,       \&quot;first_step_ids\&quot;: (array of strings) API identifiers for first steps in variant,       \&quot;first_step_id\&quot;: (string) API identifier of first step in variant (deprecated in November 2017, only included if the variant has only one first step)     },     ... (more variations)   ],   \&quot;tags\&quot;: (array of strings) tag names associated with the Canvas,   \&quot;steps\&quot;: [     {       \&quot;name\&quot;: (string) name of step,       \&quot;id\&quot;: (string) API identifier of the step,       \&quot;next_step_ids\&quot;: (array of strings) API identifiers of steps following step,       \&quot;channels\&quot;: (array of strings) channels used in step,       \&quot;messages\&quot;: {           \&quot;message_variation_id\&quot;: (string) {  // &lt;&#x3D;This is the actual id               \&quot;channel\&quot;: (string) channel type of the message (eg., \&quot;email\&quot;),               ... channel-specific fields for this message, see Campaign Details Endpoint API Response for example message responses ...           }       }     },     ... (more steps)   ],   \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.ExportApi();
let opts = {
  'canvasId': "{{canvas_identifier}}" // String | (Required) String  Canvas API Identifier 
};
apiInstance.canvasDetails(opts, (error, data, response) => {
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
 **canvasId** | **String**| (Required) String  Canvas API Identifier  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## canvasList

> canvasList(opts)

Canvas List

This endpoint allows you to export a list of Canvases, including the name, Canvas API Identifier and associated Tags. The Canvases are returned in groups of 100 sorted by time of creation (oldest to newest by default).  &gt; Archived Canvases will not be included in the API response unless the &#x60;include_archived&#x60; field is specified. Canvases that are stopped but not archived, however, will be returned by default.   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   \&quot;canvases\&quot; : [    {     \&quot;id\&quot; : (string) Canvas API Identifier,     \&quot;last_edited\&quot;: (ISO 8601 string) the last edited time for the message,     \&quot;name\&quot; : (string) Canvas name,     \&quot;tags\&quot; : (array) tag names associated with the Canvas,    },     ... (more Canvases)   ],   \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.ExportApi();
let opts = {
  'page': "1", // String | (Optional) Integer  The page of Canvases to return, defaults to `0` (returns the first set of up to 100)
  'includeArchived': "false", // String | (Optional) Boolean  Whether or not to include archived Canvases, defaults to `false`.
  'sortDirection': "desc", // String | (Optional) String  Pass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest.
  'lastEditTimeGt': "2020-06-28T23:59:59-5:00" // String | (Optional) DateTime (ISO 8601 string)  Filters the results and only returns Canvases that were edited greater than the time provided till now.
};
apiInstance.canvasList(opts, (error, data, response) => {
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
 **page** | **String**| (Optional) Integer  The page of Canvases to return, defaults to &#x60;0&#x60; (returns the first set of up to 100) | [optional] 
 **includeArchived** | **String**| (Optional) Boolean  Whether or not to include archived Canvases, defaults to &#x60;false&#x60;. | [optional] 
 **sortDirection** | **String**| (Optional) String  Pass in the value &#x60;desc&#x60; to sort by creation time from newest to oldest. Pass in &#x60;asc&#x60; to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest. | [optional] 
 **lastEditTimeGt** | **String**| (Optional) DateTime (ISO 8601 string)  Filters the results and only returns Canvases that were edited greater than the time provided till now. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## customEventsAnalytics

> customEventsAnalytics(opts)

Custom Events Analytics

This endpoint allows you to retrieve a series of the number of occurrences of a custom event in your app over a designated time period.  ### Components Used -[Segment Identifier](https://www.braze.com/docs/api/identifier_types/)   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) point in time - as ISO 8601 extended when unit is \&quot;hour\&quot; and as ISO 8601 date when unit is \&quot;day\&quot;,             \&quot;count\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;  ### Fatal Error Response Codes The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.  | Error Code       | Reason / Cause                                                   | | ---------------- | ---------------------------------------------------------------- | | 400 Bad Request  | Bad Syntax                                                       | | 401 Unauthorized | Unknown or missing REST API Key                                  | | 429 Rate Limited | Over rate limit                                                  | | 5XX              | Internal server error, you should retry with exponential backoff |

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.ExportApi();
let opts = {
  'event': "event_name", // String | (Required) String  The name of the custom event for which to return analytics 
  'length': "24", // String | (Required) Integer  Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive
  'unit': "hour", // String | (Optional) String  Unit of time between data points - can be \"day\" or \"hour\" (defaults to \"day\")
  'endingAt': "2014-12-10T23:59:59-05:00", // String | (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
  'appId': "{{app_identifier}}", // String | (Optional) String  App API identifier retrieved from the Developer Console to limit analytics to a specific app
  'segmentId': "{{segment_identifier}}" // String | (Optional) String  Segment API identifier indicating the analytics enabled segment for which event analytics should be returned
};
apiInstance.customEventsAnalytics(opts, (error, data, response) => {
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
 **event** | **String**| (Required) String  The name of the custom event for which to return analytics  | [optional] 
 **length** | **String**| (Required) Integer  Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive | [optional] 
 **unit** | **String**| (Optional) String  Unit of time between data points - can be \&quot;day\&quot; or \&quot;hour\&quot; (defaults to \&quot;day\&quot;) | [optional] 
 **endingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request | [optional] 
 **appId** | **String**| (Optional) String  App API identifier retrieved from the Developer Console to limit analytics to a specific app | [optional] 
 **segmentId** | **String**| (Optional) String  Segment API identifier indicating the analytics enabled segment for which event analytics should be returned | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## customEventsList

> customEventsList(opts)

Custom Events List

This endpoint allows you to export a list of custom events that have been recorded for your app. The event names are returned in groups of 250, sorted alphabetically.   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;events\&quot; : [         \&quot;Event A\&quot;,         \&quot;Event B\&quot;,         \&quot;Event C\&quot;,         ...     ] } &#x60;&#x60;&#x60;  ### Fatal Error Response Codes  The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.  | Error Code       | Reason / Cause                                                   | | ---------------- | ---------------------------------------------------------------- | | 400 Bad Request  | Bad Syntax                                                       | | 401 Unauthorized | Unknown or missing REST API Key                                  | | 429 Rate Limited | Over rate limit                                                  | | 5XX              | Internal server error, you should retry with exponential backoff |

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.ExportApi();
let opts = {
  'page': "3" // String | (Optional) Integer  The page of event names to return, defaults to 0 (returns the first set of up to 250)
};
apiInstance.customEventsList(opts, (error, data, response) => {
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
 **page** | **String**| (Optional) Integer  The page of event names to return, defaults to 0 (returns the first set of up to 250) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## dailyActiveUsersByDate

> dailyActiveUsersByDate(opts)

Daily Active Users by Date

This endpoint allows you to retrieve a daily series of the total number of unique active users on each date.   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;dau\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.ExportApi();
let opts = {
  'length': "10", // String | (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
  'endingAt': "2018-06-28T23:59:59-5:00", // String | (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
  'appId': "{{app_identifier}}" // String | (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned
};
apiInstance.dailyActiveUsersByDate(opts, (error, data, response) => {
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
 **length** | **String**| (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive | [optional] 
 **endingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request | [optional] 
 **appId** | **String**| (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## dailyNewUsersByDate

> dailyNewUsersByDate(opts)

Daily New Users by Date

This endpoint allows you to retrieve a daily series of the total number of new users on each date.   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;new_users\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.ExportApi();
let opts = {
  'length': "14", // String | (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
  'endingAt': "2018-06-28T23:59:59-5:00", // String | (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
  'appId': "{{app_identifier}}" // String | (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned
};
apiInstance.dailyNewUsersByDate(opts, (error, data, response) => {
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
 **length** | **String**| (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive | [optional] 
 **endingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request | [optional] 
 **appId** | **String**| (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## kpIsForDailyAppUninstallsByDate

> kpIsForDailyAppUninstallsByDate(opts)

KPIs for Daily App Uninstalls by Date

This endpoint allows you to retrieve a daily series of the total number of uninstalls on each date.  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;uninstalls\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.ExportApi();
let opts = {
  'length': "14", // String | (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
  'endingAt': "2018-06-28T23:59:59-5:00", // String | (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
  'appId': "{{app_identifier}}" // String | (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned
};
apiInstance.kpIsForDailyAppUninstallsByDate(opts, (error, data, response) => {
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
 **length** | **String**| (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive | [optional] 
 **endingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request | [optional] 
 **appId** | **String**| (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## monthlyActiveUsersForLast30Days

> monthlyActiveUsersForLast30Days(opts)

Monthly Active Users for Last 30 Days

This endpoint allows you to retrieve a daily series of the total number of unique active users over a 30-day rolling window.  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;mau\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.ExportApi();
let opts = {
  'length': "7", // String | (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
  'endingAt': "2018-06-28T23:59:59-05:00", // String | (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
  'appId': "{{app_identifier}}" // String | (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned
};
apiInstance.monthlyActiveUsersForLast30Days(opts, (error, data, response) => {
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
 **length** | **String**| (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive | [optional] 
 **endingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request | [optional] 
 **appId** | **String**| (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## newsFeedCardAnalytics

> newsFeedCardAnalytics(opts)

News Feed Card Analytics

This endpoint allows you to retrieve a daily series of engagement stats for a card over time.  ### Components Used - [Card ID](https://www.braze.com/docs/api/identifier_types/) - [News Feed List](https://www.braze.com/docs/api/endpoints/export/news_feed/get_news_feed_cards/)  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) point in time - as ISO 8601 extended when unit is \&quot;hour\&quot; and as ISO 8601 date when unit is \&quot;day\&quot;,             \&quot;clicks\&quot; : (int) ,             \&quot;impressions\&quot; : (int),             \&quot;unique_clicks\&quot; : (int),             \&quot;unique_impressions\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.ExportApi();
let opts = {
  'cardId': "{{card_identifier}}", // String | (Required) String  Card API identifier
  'length': "14", // String | (Required) Integer  Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive
  'unit': "day", // String | (Optional) String  Unit of time between data points - can be \"day\" or \"hour\" (defaults to \"day\")
  'endingAt': "2018-06-28T23:59:59-5:00" // String | (Optional) DateTime (ISO 8601 string)  Date on which the data series should end - defaults to time of the request
};
apiInstance.newsFeedCardAnalytics(opts, (error, data, response) => {
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
 **cardId** | **String**| (Required) String  Card API identifier | [optional] 
 **length** | **String**| (Required) Integer  Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive | [optional] 
 **unit** | **String**| (Optional) String  Unit of time between data points - can be \&quot;day\&quot; or \&quot;hour\&quot; (defaults to \&quot;day\&quot;) | [optional] 
 **endingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Date on which the data series should end - defaults to time of the request | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## newsFeedCardsDetails

> newsFeedCardsDetails(opts)

News Feed Cards Details

This endpoint allows you to retrieve relevant information on the card, which can be identified by the &#x60;card_id&#x60;.  ### Components Used - [Card ID](https://www.braze.com/docs/api/identifier_types/) - [News Feed List](https://www.braze.com/docs/api/endpoints/export/news_feed/get_news_feed_cards/)   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) The status of the export, returns &#39;success&#39; when completed without errors,     \&quot;created_at\&quot; : (string) Date created as ISO 8601 date,     \&quot;updated_at\&quot; : (string) Date last updated as ISO 8601 date,     \&quot;name\&quot; : (string) Card name,     \&quot;publish_at\&quot; : (string) Date card was published as ISO 8601 date,     \&quot;end_at\&quot; : (string) Date card will stop displaying for users as ISO 8601 date,     \&quot;tags\&quot; : (array) Tag names associated with the card,     \&quot;title\&quot; : (string) Title of the card,     \&quot;image_url\&quot; : (string) Image URL used by this card,     \&quot;extras\&quot; : (dictionary) Dictionary containing key-value pair data attached to this card,     \&quot;description\&quot; : (string) Description text used by this card,     \&quot;archived\&quot;: (boolean) whether this Card is archived,     \&quot;draft\&quot;: (boolean) whether this Card is a draft, } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.ExportApi();
let opts = {
  'cardId': "{{card_identifier}}" // String | (Required) String  Card API identifier 
};
apiInstance.newsFeedCardsDetails(opts, (error, data, response) => {
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
 **cardId** | **String**| (Required) String  Card API identifier  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## newsFeedCardsList

> newsFeedCardsList(opts)

News Feed Cards List

This endpoint allows you to export a list of News Feed cards, each of which will include its name and Card API Identifier. The cards are returned in groups of 100 sorted by time of creation (oldest to newest by default).   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;cards\&quot; : [         {             \&quot;id\&quot; : (string) Card API Identifier,             \&quot;type\&quot; : (string) type of the card - NewsItem (classic cards), CaptionedImage, Banner or DevPick (cross-promotional cards),             \&quot;title\&quot; : (string) title of the card,             \&quot;tags\&quot; : (array) tag names associated with the card         },         ...     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.ExportApi();
let opts = {
  'page': "1", // String | (Optional) Integer  The page of cards to return, defaults to 0 (returns the first set of up to 100)
  'includeArchived': "true", // String | (Optional) Boolean  Whether or not to include archived cards, defaults to false
  'sortDirection': "desc" // String | (Optional) String  Pass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest.
};
apiInstance.newsFeedCardsList(opts, (error, data, response) => {
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
 **page** | **String**| (Optional) Integer  The page of cards to return, defaults to 0 (returns the first set of up to 100) | [optional] 
 **includeArchived** | **String**| (Optional) Boolean  Whether or not to include archived cards, defaults to false | [optional] 
 **sortDirection** | **String**| (Optional) String  Pass in the value &#x60;desc&#x60; to sort by creation time from newest to oldest. Pass in &#x60;asc&#x60; to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## segmentAnalytics

> segmentAnalytics(opts)

Segment Analytics

This endpoint allows you to retrieve a daily series of the size of a segment over time for a segment.  ### Request Components - [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;size\&quot; : (int) size of the segment on that date         },         ...     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.ExportApi();
let opts = {
  'segmentId': "{{segment_identifier}}", // String | (Required) String  Segment API identifier.
  'length': "14", // String | (Required) Integer  Max number of days before `ending_at` to include in the returned series - must be between 1 and 100 inclusive.
  'endingAt': "2018-06-27T23:59:59-5:00" // String | (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request.
};
apiInstance.segmentAnalytics(opts, (error, data, response) => {
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
 **segmentId** | **String**| (Required) String  Segment API identifier. | [optional] 
 **length** | **String**| (Required) Integer  Max number of days before &#x60;ending_at&#x60; to include in the returned series - must be between 1 and 100 inclusive. | [optional] 
 **endingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## segmentDetails

> segmentDetails(opts)

Segment Details

This endpoint allows you to retrieve relevant information on the segment, which can be identified by the &#x60;segment_id&#x60;.  ### Request Components - [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {       \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,       \&quot;created_at\&quot; : (string) date created as ISO 8601 date,       \&quot;updated_at\&quot; : (string) date last updated as ISO 8601 date,       \&quot;name\&quot; : (string) segment name,       \&quot;description\&quot; : (string) human-readable description of filters,       \&quot;text_description\&quot; : (string) segment description,        \&quot;tags\&quot; : (array) tag names associated with the segment } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.ExportApi();
let opts = {
  'segmentId': "{{segment_identifier}}" // String | (Required) String  Segment API identifier
};
apiInstance.segmentDetails(opts, (error, data, response) => {
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
 **segmentId** | **String**| (Required) String  Segment API identifier | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## segmentList

> segmentList(opts)

Segment List

This endpoint allows you to export a list of segments, each of which will include its name, Segment API Identifier, and whether it has analytics tracking enabled. The segments are returned in groups of 100 sorted by time of creation (oldest to newest by default). Archived segments are not included.  ### Request Components - [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;segments\&quot; : [         {             \&quot;id\&quot; : (string) Segment API Identifier,             \&quot;name\&quot; : (string) segment name,             \&quot;analytics_tracking_enabled\&quot; : (boolean) whether the segment has analytics tracking enabled,             \&quot;tags\&quot; : (array) tag names associated with the segment         },         ...     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.ExportApi();
let opts = {
  'page': "1", // String | (Optional) Integer  The page of segments to return, defaults to 0 (returns the first set of up to 100)
  'sortDirection': "desc" // String | (Optional) String  Pass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If `sort_direction` is not included, the default order is oldest to newest.
};
apiInstance.segmentList(opts, (error, data, response) => {
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
 **page** | **String**| (Optional) Integer  The page of segments to return, defaults to 0 (returns the first set of up to 100) | [optional] 
 **sortDirection** | **String**| (Optional) String  Pass in the value &#x60;desc&#x60; to sort by creation time from newest to oldest. Pass in &#x60;asc&#x60; to sort from oldest to newest. If &#x60;sort_direction&#x60; is not included, the default order is oldest to newest. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## sendAnalytics

> sendAnalytics(opts)

Send Analytics

This endpoint allows you to retrieve a daily series of various stats for a tracked &#x60;send_id&#x60;. Braze stores send analytics for 14 days after the send.  Campaign conversions will be attributed towards the most recent send id that a given user has received from the campaign.  &gt; The &#x60;send_id&#x60; is only generated for API campaign sends targeting segments, connected audiences or broadcasts. When relevant, the &#x60;send_id&#x60; is included in response for the &#x60;messages/send&#x60;, &#x60;messages/schedule&#x60;, &#x60;campaign/trigger/send&#x60; and &#x60;campaign/trigger/schedule&#x60; endpoints.  ### Components Used - [Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)  ### Send Analytics Endpoint API Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {             \&quot;variation_name\&quot;: (string) variation name,             \&quot;sent\&quot;: (int) the number of sends,             \&quot;delivered\&quot;: (int) the number of messages successfully delivered,             \&quot;undelivered\&quot;: (int) the number of undelivered,             \&quot;delivery_failed\&quot;: (int) the number of rejected,             \&quot;direct_opens\&quot;: (int) the number of direct opens,             \&quot;total_opens\&quot;: (int) the number of total opens,             \&quot;bounces\&quot;: (int) the number of bounces,             \&quot;body_clicks\&quot;: (int) the number of body clicks,             \&quot;revenue\&quot;: (float) the number of dollars of revenue (USD),             \&quot;unique_recipients\&quot;: (int) the number of unique recipients,             \&quot;conversions\&quot;: (int) the number of conversions,             \&quot;conversions_by_send_time\&quot;: (int) the number of conversions,             \&quot;conversions1\&quot;: (int, optional) the number of conversions for the second conversion event,             \&quot;conversions1_by_send_time\&quot;: (int, optional) the number of conversions for the second conversion event by send time,             \&quot;conversions2\&quot;: (int, optional) the number of conversions for the third conversion event,             \&quot;conversions2_by_send_time\&quot;: (int, optional) the number of conversions for the third conversion event by send time,             \&quot;conversions3\&quot;: (int, optional) the number of conversions for the fourth conversion event,             \&quot;conversions3_by_send_time\&quot;: (int, optional) the number of conversions for the fourth conversion event by send time           }         ]       },       \&quot;conversions_by_send_time\&quot;: 0,       \&quot;conversions1_by_send_time\&quot;: 0,       \&quot;conversions2_by_send_time\&quot;: 0,       \&quot;conversions3_by_send_time\&quot;: 0,       \&quot;conversions\&quot;: 0,       \&quot;conversions1\&quot;: 0,       \&quot;conversions2\&quot;: 0,       \&quot;conversions3\&quot;: 0,       \&quot;unique_recipients\&quot;: 1,       \&quot;revenue\&quot;: 0     }   ],   \&quot;message\&quot;: \&quot;success\&quot; } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.ExportApi();
let opts = {
  'campaignId': "{{campaign_identifier}}", // String | (Required) String  Campaign API identifier.
  'sendId': "{{send_identifier}}", // String | (Required) String  Send API identifier.
  'length': "30", // String | (Required) Integer  Maximum number of days before `ending_at` to include in the returned series. Must be between 1 and 100 inclusive.
  'endingAt': "2014-12-10T23:59:59-05:00" // String | (Optional) Datetime ISO 8601 string  Date on which the data series should end. Defaults to time of the request.
};
apiInstance.sendAnalytics(opts, (error, data, response) => {
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
 **campaignId** | **String**| (Required) String  Campaign API identifier. | [optional] 
 **sendId** | **String**| (Required) String  Send API identifier. | [optional] 
 **length** | **String**| (Required) Integer  Maximum number of days before &#x60;ending_at&#x60; to include in the returned series. Must be between 1 and 100 inclusive. | [optional] 
 **endingAt** | **String**| (Optional) Datetime ISO 8601 string  Date on which the data series should end. Defaults to time of the request. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

