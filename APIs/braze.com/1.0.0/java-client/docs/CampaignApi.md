# CampaignApi

All URIs are relative to *https://rest.iad-01.braze.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**campaignAnalytics_0**](CampaignApi.md#campaignAnalytics_0) | **GET** /campaigns/data_series | Campaign Analytics |
| [**campaignDetails_0**](CampaignApi.md#campaignDetails_0) | **GET** /campaigns/details | Campaign Details |
| [**campaignList_0**](CampaignApi.md#campaignList_0) | **GET** /campaigns/list | Campaign List |
| [**sendAnalytics_0**](CampaignApi.md#sendAnalytics_0) | **GET** /sends/data_series | Send Analytics |


<a id="campaignAnalytics_0"></a>
# **campaignAnalytics_0**
> campaignAnalytics_0(campaignId, length, endingAt)

Campaign Analytics

This endpoint allows you to retrieve a daily series of various stats for a campaign over time. Data returned includes how many messages were sent, opened, clicked, converted, etc., broken down by message channel.   ### Components Used -[Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)   ### Responses  #### Multi-Channel Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;messages\&quot; : {                 \&quot;ios_push\&quot; : [                     {                       \&quot;variation_name\&quot;: \&quot;iOS_Push\&quot;,                       \&quot;sent\&quot; : (int),                       \&quot;direct_opens\&quot; : (int),                       \&quot;total_opens\&quot; : (int),                       \&quot;bounces\&quot; : (int),                       \&quot;body_clicks\&quot; : (int)                       \&quot;revenue\&quot;: 0,                       \&quot;unique_recipients\&quot;: 1,                       \&quot;conversions\&quot;: 0,                       \&quot;conversions_by_send_time\&quot;: 0,                       \&quot;conversions1\&quot;: 0,                       \&quot;conversions1_by_send_time\&quot;: 0,                       \&quot;conversions2\&quot;: 0,                       \&quot;conversions2_by_send_time\&quot;: 0,                       \&quot;conversions3\&quot;: 0,                       \&quot;conversions3_by_send_time\&quot;: 0,                       \&quot;carousel_slide_[NUM]_[TITLE]_click\&quot;: (optional, int),                       \&quot;notif_button_[NUM]_[TITLE]_click\&quot;: (optional, int)                     }                 ],                 \&quot;android_push\&quot; : [                     {                       \&quot;sent\&quot; : (int),                       \&quot;direct_opens\&quot; : (int),                       \&quot;total_opens\&quot; : (int),                       \&quot;bounces\&quot; : (int),                       \&quot;body_clicks\&quot; : (int)                     }                 ],                 \&quot;webhook\&quot;: [                     {                       \&quot;sent\&quot;: (int),                       \&quot;errors\&quot;: (int)                     }                 ],                 \&quot;email\&quot; : [                     {                       \&quot;sent\&quot;: (int),                       \&quot;opens\&quot;: (int),                       \&quot;unique_opens\&quot;: (int),                       \&quot;clicks\&quot;: (int),                       \&quot;unique_clicks\&quot;: (int),                       \&quot;unsubscribes\&quot;: (int),                       \&quot;bounces\&quot;: (int),                       \&quot;delivered\&quot;: (int),                       \&quot;reported_spam\&quot;: (int)                     }                 ],                 \&quot;sms\&quot; : [                   {                     \&quot;sent\&quot;: (int),                     \&quot;delivered\&quot;: (int),                     \&quot;undelivered\&quot;: (int),                     \&quot;delivery_failed\&quot;: (int)                   }                 ]               },            \&quot;conversions_by_send_time\&quot;: (optional, int),            \&quot;conversions1_by_send_time\&quot;: (optional, int),            \&quot;conversions2_by_send_time\&quot;: (optional, int),            \&quot;conversions3_by_send_time\&quot;: (optional, int),            \&quot;conversions\&quot;: (int),            \&quot;conversions1\&quot;: (optional, int),            \&quot;conversions2\&quot;: (optional, int),            \&quot;conversions3\&quot;: (optional, int),            \&quot;unique_recipients\&quot;: (int),            \&quot;revenue\&quot;: (optional, float)         },         ...     ],     ... } &#x60;&#x60;&#x60;  #### Multivariate Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;conversions\&quot; : (int),             \&quot;revenue\&quot;: (float),             \&quot;conversions_by_send_time\&quot;: (int),             \&quot;messages\&quot; : {                \&quot;trigger_in_app_message\&quot;: [{           \&quot;variation_name\&quot;: (optional, string),           \&quot;impressions\&quot;: (int),           \&quot;clicks\&quot;: (int),           \&quot;first_button_clicks\&quot;: (int),           \&quot;second_button_clicks\&quot;: (int),           \&quot;revenue\&quot;: (optional, float),,           \&quot;unique_recipients\&quot;: (int),           \&quot;conversions\&quot;: (optional, int),           \&quot;conversions_by_send_time\&quot;: (optional, int),           \&quot;conversions1\&quot;: (optional, int),           \&quot;conversions1_by_send_time\&quot;: (optional, int),           \&quot;conversions2\&quot;: (optional, int),           \&quot;conversions2_by_send_time\&quot;: (optional, int),           \&quot;conversions3\&quot;: (optional, int),           \&quot;conversions3_by_send_time\&quot;: (optional, int)          }, {           \&quot;variation_name\&quot;: (optional, string),           \&quot;impressions\&quot;: (int),           \&quot;clicks\&quot;: (int),           \&quot;first_button_clicks\&quot;: (int),           \&quot;second_button_clicks\&quot;: (int),           \&quot;revenue\&quot;: (optional, float),,           \&quot;unique_recipients\&quot;: (int),           \&quot;conversions\&quot;: (optional, int),           \&quot;conversions_by_send_time\&quot;: (optional, int),           \&quot;conversions1\&quot;: (optional, int),           \&quot;conversions1_by_send_time\&quot;: (optional, int),           \&quot;conversions2\&quot;: (optional, int),           \&quot;conversions2_by_send_time\&quot;: (optional, int),           \&quot;conversions3\&quot;: (optional, int).           \&quot;conversions3_by_send_time\&quot;: (optional, int)          }, {           \&quot;variation_name\&quot;: (optional, string),           \&quot;revenue\&quot;: (optional, float),,           \&quot;unique_recipients\&quot;: (int),           \&quot;conversions\&quot;: (optional, int),           \&quot;conversions_by_send_time\&quot;: (optional, int),           \&quot;conversions1\&quot;: (optional, int),           \&quot;conversions1_by_send_time\&quot;: (optional, int),           \&quot;conversions2\&quot;: (optional, int),           \&quot;conversions2_by_send_time\&quot;: (optional, int),           \&quot;conversions3\&quot;: (optional, int),           \&quot;conversions3_by_send_time\&quot;: (optional, int),           \&quot;enrolled\&quot;: (optional, int)          }]         },         \&quot;conversions_by_send_time\&quot;: (optional, int),         \&quot;conversions1_by_send_time\&quot;: (optional, int),         \&quot;conversions2_by_send_time\&quot;: (optional, int),         \&quot;conversions3_by_send_time\&quot;: (optional, int),         \&quot;conversions\&quot;: (optional, int,         \&quot;conversions1\&quot;: (optional, int),         \&quot;conversions2\&quot;: (optional, int),         \&quot;conversions3\&quot;: (optional, int),         \&quot;unique_recipients\&quot;: (int),         \&quot;revenue\&quot;: (optional, float)          }],          ... } &#x60;&#x60;&#x60;  Possible message types are &#x60;email&#x60;, &#x60;in_app_message&#x60;, &#x60;webhook&#x60;, &#x60;android_push&#x60;, &#x60;apple_push&#x60;, &#x60;kindle_push&#x60;, &#x60;web_push&#x60;, &#x60;windows_phone8_push&#x60;, and &#x60;windows_universal_push&#x60;. All push message types will have the same statistics shown for &#x60;android_push&#x60; above.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.iad-01.braze.com");

    CampaignApi apiInstance = new CampaignApi(defaultClient);
    String campaignId = "{{campaign_identifier}}"; // String | (Required) String  Campaign API identifier
    String length = "7"; // String | (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
    String endingAt = "2020-06-28T23:59:59-5:00"; // String | (Optional) DateTime (ISO 8601 string)  Date on which the data series should end - defaults to time of the request
    try {
      apiInstance.campaignAnalytics_0(campaignId, length, endingAt);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignApi#campaignAnalytics_0");
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
| **campaignId** | **String**| (Required) String  Campaign API identifier | [optional] |
| **length** | **String**| (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive | [optional] |
| **endingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Date on which the data series should end - defaults to time of the request | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="campaignDetails_0"></a>
# **campaignDetails_0**
> campaignDetails_0(campaignId)

Campaign Details

This endpoint allows you to retrieve relevant information on a specified campaign, which can be identified by the &#x60;campaign_id&#x60;.   &gt; The campaign_id for API campaigns can be found on the Developer Console page and the campaign details page within your dashboard or you can use the Campaign List Endpoint.  ### Components Used - [Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)   ### Campaign Details Endpoint API Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;created_at\&quot; : (string) date created as ISO 8601 date,     \&quot;updated_at\&quot; : (string) date last updated as ISO 8601 date,     \&quot;archived\&quot;: (boolean) whether this Campaign is archived,     \&quot;draft\&quot;: (boolean) whether this Campaign is a draft,     \&quot;name\&quot; : (string) campaign name,     \&quot;description\&quot; : (string) campaign description,     \&quot;schedule_type\&quot; : (string) type of scheduling action,     \&quot;channels\&quot; : (array) list of channels to send via,     \&quot;first_sent\&quot; : (string) date and hour of first sent as ISO 8601 date,     \&quot;last_sent\&quot; : (string) date and hour of last sent as ISO 8601 date,     \&quot;tags\&quot; : (array) tag names associated with the campaign,     \&quot;messages\&quot;: {         \&quot;message_variation_id\&quot;: (string) { // &lt;&#x3D;This is the actual id             \&quot;channel\&quot;: (string) channel type of the message (as in, \&quot;email\&quot;, \&quot;ios_push\&quot;, \&quot;webhook\&quot;, \&quot;content_card\&quot;, \&quot;in-app_message\&quot;, \&quot;sms\&quot;),             \&quot;name\&quot;: (string) name of the message in the Dashboard (eg., \&quot;Variation 1\&quot;)             ... channel-specific fields for this message, see below ...         }     },     \&quot;conversion_behaviors\&quot;: (array) conversion event behaviors assigned to the campaign (see below) } &#x60;&#x60;&#x60;  #### Messages  The &#x60;messages&#x60; response will contain information about each message. Example message responses for channels are below:  ##### Push Channels  &#x60;&#x60;&#x60;json {     \&quot;channel\&quot;: (string) description of the channel, such as \&quot;ios_push\&quot; or \&quot;android_push\&quot;     \&quot;alert\&quot;: (string) alert body text,     \&quot;extras\&quot;: (hash) any key value pairs provided } &#x60;&#x60;&#x60;  ##### Email Channel  &#x60;&#x60;&#x60;json {     \&quot;channel\&quot;: \&quot;email\&quot;,     \&quot;subject\&quot;: (string) subject,     \&quot;body\&quot;: (string) HTML body,     \&quot;from\&quot;: (string) from address and display name,     \&quot;reply_to\&quot;: (string) reply-to for message, if different than \&quot;from\&quot; address,     \&quot;title\&quot;: (string) name of the email,     \&quot;extras\&quot;: (hash) any key value pairs provided } &#x60;&#x60;&#x60;  ##### Content Card Channel  &#x60;&#x60;&#x60;json {     \&quot;channel\&quot;: \&quot;content_cards\&quot;,     \&quot;name\&quot;: (string) name of variant,     \&quot;extras\&quot;: (hash) any key value pairs provided; only present if at least one key-value pair has been set } &#x60;&#x60;&#x60;  ##### Webhook Channel  &#x60;&#x60;&#x60;json {     \&quot;channel\&quot;: \&quot;webhook\&quot;,     \&quot;url\&quot;: (string) url for webhook,     \&quot;body\&quot;: (string) payload body,     \&quot;type\&quot;: (string) body content type,     \&quot;headers\&quot;: (hash) specified request headers,     \&quot;method\&quot;: (string) HTTP method (e.g., \&quot;POST\&quot; or \&quot;GET\&quot;), } &#x60;&#x60;&#x60;  ##### SMS Channel  &#x60;&#x60;&#x60;json {   \&quot;channel\&quot;: \&quot;sms\&quot;,   \&quot;body\&quot;: (string) payload body,   \&quot;from\&quot;: (string) list of numbers associated with the subscription group,   \&quot;subscription_group_id\&quot;: (string) API id of the subscription group targeted in the SMS message } &#x60;&#x60;&#x60;  ##### Control Messages  &#x60;&#x60;&#x60;json {     \&quot;channel\&quot;: (string) description of the channel that the control is for,     \&quot;type\&quot;: \&quot;control\&quot; } &#x60;&#x60;&#x60;  #### Conversion Behaviors  The &#x60;conversion_behaviors&#x60; array will contain information about each conversion event behavior set for the campaign. These behaviors are in order as set by the campaign. For example, Conversion Event A will be the first item in the array, Conversion Event B will be second, etc. Example conversion event behavior responses for are below:  ##### Clicks Email  &#x60;&#x60;&#x60;json {     \&quot;type\&quot;: \&quot;Clicks Email\&quot;,     \&quot;window\&quot;: (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours } &#x60;&#x60;&#x60;  ##### Opens Email  &#x60;&#x60;&#x60;json {     \&quot;type\&quot;: \&quot;Opens Email\&quot;,     \&quot;window\&quot;: (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours } &#x60;&#x60;&#x60;  ##### Makes Purchase (any purchase)  &#x60;&#x60;&#x60;json {     \&quot;type\&quot;: \&quot;Makes Any Purchase\&quot;,     \&quot;window\&quot;: (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours } &#x60;&#x60;&#x60;  ##### Makes Purchase (specific product)  &#x60;&#x60;&#x60;json {     \&quot;type\&quot;: \&quot;Makes Specific Purchase\&quot;,     \&quot;window\&quot;: (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,     \&quot;product\&quot;: (string) name of the product, i.e. - \&quot;Feline Body Armor\&quot; } &#x60;&#x60;&#x60;  ##### Performs Custom Event  &#x60;&#x60;&#x60;json {     \&quot;type\&quot;: \&quot;Performs Custom Event\&quot;,     \&quot;window\&quot;: (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,     \&quot;custom_event_name\&quot;: (string) name of the event, i.e. - \&quot;Used Feline Body Armor\&quot; } &#x60;&#x60;&#x60;  ##### Upgrades App  &#x60;&#x60;&#x60;json {     \&quot;type\&quot;: \&quot;Upgrades App\&quot;,     \&quot;window\&quot;: (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,     \&quot;app_ids\&quot;: (array|null) array of app ids, i.e. - [\&quot;12345\&quot;, \&quot;67890\&quot;], or &#x60;null&#x60; if \&quot;Track sessions for any app\&quot; is selected in the UI } &#x60;&#x60;&#x60;  ##### Uses App  &#x60;&#x60;&#x60;json {     \&quot;type\&quot;: \&quot;Starts Session\&quot;,     \&quot;window\&quot;: (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,     \&quot;app_ids\&quot;: (array|null) array of app ids, i.e. - [\&quot;12345\&quot;, \&quot;67890\&quot;], or &#x60;null&#x60; if \&quot;Track sessions for any app\&quot; is selected in the UI } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.iad-01.braze.com");

    CampaignApi apiInstance = new CampaignApi(defaultClient);
    String campaignId = "{{campaign_identifier}}"; // String | (Required) String  Campaign API identifier
    try {
      apiInstance.campaignDetails_0(campaignId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignApi#campaignDetails_0");
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
| **campaignId** | **String**| (Required) String  Campaign API identifier | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="campaignList_0"></a>
# **campaignList_0**
> campaignList_0(page, includeArchived, sortDirection, lastEditTimeGt)

Campaign List

This endpoint allows you to export a list of campaigns, each of which will include its name, Campaign API Identifier, whether it is an API Campaign, and Tags associated with the campaign. The campaigns are returned in groups of 100 sorted by time of creation (oldest to newest by default).  ## Campaign List Endpoint API Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;campaigns\&quot; : [         {             \&quot;id\&quot; : (string) Campaign API Identifier,             \&quot;last_edited\&quot;: (ISO 8601 string) the last edited time for the message              \&quot;name\&quot; : (string) campaign name,             \&quot;is_api_campaign\&quot; : (boolean) whether the campaign is an API Campaign,             \&quot;tags\&quot; : (array) tag names associated with the campaign         },         ...     ] } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.iad-01.braze.com");

    CampaignApi apiInstance = new CampaignApi(defaultClient);
    String page = "0"; // String | (Optional) Integer  The page of campaigns to return, defaults to 0 (returns the first set of up to 100)
    String includeArchived = "false"; // String | (Optional) Boolean  Whether or not to include archived campaigns, defaults to false
    String sortDirection = "desc"; // String | (Optional) String  Pass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest.
    String lastEditTimeGt = "2020-06-28T23:59:59-5:00"; // String | (Optional) DateTime (ISO 8601 string)  Filters the results and only returns campaigns that were edited greater than the time provided till now. 
    try {
      apiInstance.campaignList_0(page, includeArchived, sortDirection, lastEditTimeGt);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignApi#campaignList_0");
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
| **page** | **String**| (Optional) Integer  The page of campaigns to return, defaults to 0 (returns the first set of up to 100) | [optional] |
| **includeArchived** | **String**| (Optional) Boolean  Whether or not to include archived campaigns, defaults to false | [optional] |
| **sortDirection** | **String**| (Optional) String  Pass in the value &#x60;desc&#x60; to sort by creation time from newest to oldest. Pass in &#x60;asc&#x60; to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest. | [optional] |
| **lastEditTimeGt** | **String**| (Optional) DateTime (ISO 8601 string)  Filters the results and only returns campaigns that were edited greater than the time provided till now.  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="sendAnalytics_0"></a>
# **sendAnalytics_0**
> sendAnalytics_0(campaignId, sendId, length, endingAt)

Send Analytics

This endpoint allows you to retrieve a daily series of various stats for a tracked &#x60;send_id&#x60;. Braze stores send analytics for 14 days after the send.  Campaign conversions will be attributed towards the most recent send id that a given user has received from the campaign.  &gt; The &#x60;send_id&#x60; is only generated for API campaign sends targeting segments, connected audiences or broadcasts. When relevant, the &#x60;send_id&#x60; is included in response for the &#x60;messages/send&#x60;, &#x60;messages/schedule&#x60;, &#x60;campaign/trigger/send&#x60; and &#x60;campaign/trigger/schedule&#x60; endpoints.  ### Components Used - [Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)  ### Send Analytics Endpoint API Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {             \&quot;variation_name\&quot;: (string) variation name,             \&quot;sent\&quot;: (int) the number of sends,             \&quot;delivered\&quot;: (int) the number of messages successfully delivered,             \&quot;undelivered\&quot;: (int) the number of undelivered,             \&quot;delivery_failed\&quot;: (int) the number of rejected,             \&quot;direct_opens\&quot;: (int) the number of direct opens,             \&quot;total_opens\&quot;: (int) the number of total opens,             \&quot;bounces\&quot;: (int) the number of bounces,             \&quot;body_clicks\&quot;: (int) the number of body clicks,             \&quot;revenue\&quot;: (float) the number of dollars of revenue (USD),             \&quot;unique_recipients\&quot;: (int) the number of unique recipients,             \&quot;conversions\&quot;: (int) the number of conversions,             \&quot;conversions_by_send_time\&quot;: (int) the number of conversions,             \&quot;conversions1\&quot;: (int, optional) the number of conversions for the second conversion event,             \&quot;conversions1_by_send_time\&quot;: (int, optional) the number of conversions for the second conversion event by send time,             \&quot;conversions2\&quot;: (int, optional) the number of conversions for the third conversion event,             \&quot;conversions2_by_send_time\&quot;: (int, optional) the number of conversions for the third conversion event by send time,             \&quot;conversions3\&quot;: (int, optional) the number of conversions for the fourth conversion event,             \&quot;conversions3_by_send_time\&quot;: (int, optional) the number of conversions for the fourth conversion event by send time           }         ]       },       \&quot;conversions_by_send_time\&quot;: 0,       \&quot;conversions1_by_send_time\&quot;: 0,       \&quot;conversions2_by_send_time\&quot;: 0,       \&quot;conversions3_by_send_time\&quot;: 0,       \&quot;conversions\&quot;: 0,       \&quot;conversions1\&quot;: 0,       \&quot;conversions2\&quot;: 0,       \&quot;conversions3\&quot;: 0,       \&quot;unique_recipients\&quot;: 1,       \&quot;revenue\&quot;: 0     }   ],   \&quot;message\&quot;: \&quot;success\&quot; } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.iad-01.braze.com");

    CampaignApi apiInstance = new CampaignApi(defaultClient);
    String campaignId = "{{campaign_identifier}}"; // String | (Required) String  Campaign API identifier.
    String sendId = "{{send_identifier}}"; // String | (Required) String  Send API identifier.
    String length = "30"; // String | (Required) Integer  Maximum number of days before `ending_at` to include in the returned series. Must be between 1 and 100 inclusive.
    String endingAt = "2014-12-10T23:59:59-05:00"; // String | (Optional) Datetime ISO 8601 string  Date on which the data series should end. Defaults to time of the request.
    try {
      apiInstance.sendAnalytics_0(campaignId, sendId, length, endingAt);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignApi#sendAnalytics_0");
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
| **campaignId** | **String**| (Required) String  Campaign API identifier. | [optional] |
| **sendId** | **String**| (Required) String  Send API identifier. | [optional] |
| **length** | **String**| (Required) Integer  Maximum number of days before &#x60;ending_at&#x60; to include in the returned series. Must be between 1 and 100 inclusive. | [optional] |
| **endingAt** | **String**| (Optional) Datetime ISO 8601 string  Date on which the data series should end. Defaults to time of the request. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

