# BrazeEndpoints.NewsFeedApi

All URIs are relative to *https://rest.iad-01.braze.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**newsFeedCardAnalytics_0**](NewsFeedApi.md#newsFeedCardAnalytics_0) | **GET** /feed/data_series | News Feed Card Analytics
[**newsFeedCardsDetails_0**](NewsFeedApi.md#newsFeedCardsDetails_0) | **GET** /feed/details | News Feed Cards Details
[**newsFeedCardsList_0**](NewsFeedApi.md#newsFeedCardsList_0) | **GET** /feed/list | News Feed Cards List



## newsFeedCardAnalytics_0

> newsFeedCardAnalytics_0(opts)

News Feed Card Analytics

This endpoint allows you to retrieve a daily series of engagement stats for a card over time.  ### Components Used - [Card ID](https://www.braze.com/docs/api/identifier_types/) - [News Feed List](https://www.braze.com/docs/api/endpoints/export/news_feed/get_news_feed_cards/)  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) point in time - as ISO 8601 extended when unit is \&quot;hour\&quot; and as ISO 8601 date when unit is \&quot;day\&quot;,             \&quot;clicks\&quot; : (int) ,             \&quot;impressions\&quot; : (int),             \&quot;unique_clicks\&quot; : (int),             \&quot;unique_impressions\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.NewsFeedApi();
let opts = {
  'cardId': "{{card_identifier}}", // String | (Required) String  Card API identifier
  'length': "14", // String | (Required) Integer  Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive
  'unit': "day", // String | (Optional) String  Unit of time between data points - can be \"day\" or \"hour\" (defaults to \"day\")
  'endingAt': "2018-06-28T23:59:59-5:00" // String | (Optional) DateTime (ISO 8601 string)  Date on which the data series should end - defaults to time of the request
};
apiInstance.newsFeedCardAnalytics_0(opts, (error, data, response) => {
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


## newsFeedCardsDetails_0

> newsFeedCardsDetails_0(opts)

News Feed Cards Details

This endpoint allows you to retrieve relevant information on the card, which can be identified by the &#x60;card_id&#x60;.  ### Components Used - [Card ID](https://www.braze.com/docs/api/identifier_types/) - [News Feed List](https://www.braze.com/docs/api/endpoints/export/news_feed/get_news_feed_cards/)   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) The status of the export, returns &#39;success&#39; when completed without errors,     \&quot;created_at\&quot; : (string) Date created as ISO 8601 date,     \&quot;updated_at\&quot; : (string) Date last updated as ISO 8601 date,     \&quot;name\&quot; : (string) Card name,     \&quot;publish_at\&quot; : (string) Date card was published as ISO 8601 date,     \&quot;end_at\&quot; : (string) Date card will stop displaying for users as ISO 8601 date,     \&quot;tags\&quot; : (array) Tag names associated with the card,     \&quot;title\&quot; : (string) Title of the card,     \&quot;image_url\&quot; : (string) Image URL used by this card,     \&quot;extras\&quot; : (dictionary) Dictionary containing key-value pair data attached to this card,     \&quot;description\&quot; : (string) Description text used by this card,     \&quot;archived\&quot;: (boolean) whether this Card is archived,     \&quot;draft\&quot;: (boolean) whether this Card is a draft, } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.NewsFeedApi();
let opts = {
  'cardId': "{{card_identifier}}" // String | (Required) String  Card API identifier 
};
apiInstance.newsFeedCardsDetails_0(opts, (error, data, response) => {
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


## newsFeedCardsList_0

> newsFeedCardsList_0(opts)

News Feed Cards List

This endpoint allows you to export a list of News Feed cards, each of which will include its name and Card API Identifier. The cards are returned in groups of 100 sorted by time of creation (oldest to newest by default).   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;cards\&quot; : [         {             \&quot;id\&quot; : (string) Card API Identifier,             \&quot;type\&quot; : (string) type of the card - NewsItem (classic cards), CaptionedImage, Banner or DevPick (cross-promotional cards),             \&quot;title\&quot; : (string) title of the card,             \&quot;tags\&quot; : (array) tag names associated with the card         },         ...     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.NewsFeedApi();
let opts = {
  'page': "1", // String | (Optional) Integer  The page of cards to return, defaults to 0 (returns the first set of up to 100)
  'includeArchived': "true", // String | (Optional) Boolean  Whether or not to include archived cards, defaults to false
  'sortDirection': "desc" // String | (Optional) String  Pass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest.
};
apiInstance.newsFeedCardsList_0(opts, (error, data, response) => {
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

