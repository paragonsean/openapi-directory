# MoonByAiWeiweiOlafurEliasson.MarksApi

All URIs are relative to *http://moonmoonmoonmoon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**marksHashtags**](MarksApi.md#marksHashtags) | **GET** /api/hashtags | Fetches popular hashtags or marks tagged with specified hashtag
[**marksIndex**](MarksApi.md#marksIndex) | **GET** /api/marks | Fetches marks



## marksHashtags

> marksHashtags(opts)

Fetches popular hashtags or marks tagged with specified hashtag

Search for specified tag (no pound sign necessary). If &lt;b&gt;tag&lt;/b&gt; is empty, the 50 most popular hashtags will be returned.

### Example

```javascript
import MoonByAiWeiweiOlafurEliasson from 'moon_by_ai_weiwei__olafur_eliasson';

let apiInstance = new MoonByAiWeiweiOlafurEliasson.MarksApi();
let opts = {
  'tag': "tag_example" // String | Hashtag to search for
};
apiInstance.marksHashtags(opts, (error, data, response) => {
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
 **tag** | **String**| Hashtag to search for | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## marksIndex

> marksIndex(opts)

Fetches marks

The main method for querying the marks database. You may use the following options:         &lt;ol style&#x3D;&#39;list-style-type: lower-roman;&#39;&gt;         &lt;li&gt;No parameters to retrieve all marks in descending chronological order (use &lt;b&gt;before&lt;/b&gt; for pagination)&lt;/li&gt;         &lt;li&gt;&lt;b&gt;popular&lt;/b&gt; (and optionally &lt;b&gt;last_popular_id&lt;/b&gt;) to retrieve all popular marks&lt;/li&gt;         &lt;li&gt;&lt;b&gt;featured&lt;/b&gt; to retrieve all featured marks&lt;/li&gt;         &lt;li&gt;&lt;b&gt;x &amp; y&lt;/b&gt; to retrieve mark at specific coordinate&lt;/li&gt;         &lt;li&gt;&lt;b&gt;user&lt;/b&gt; to retrieve all marks created by the specified user&lt;/li&gt;         &lt;li&gt;&lt;b&gt;collection&lt;/b&gt; to retrieve all marks collected by the specified user&lt;/li&gt;         &lt;/ol&gt;

### Example

```javascript
import MoonByAiWeiweiOlafurEliasson from 'moon_by_ai_weiwei__olafur_eliasson';

let apiInstance = new MoonByAiWeiweiOlafurEliasson.MarksApi();
let opts = {
  'before': "before_example", // String | Before ID (pagination purposes)
  'popular': true, // Boolean | Popular marks
  'lastPopularId': "lastPopularId_example", // String | Last popular ID (for pagination purposes)
  'featured': true, // Boolean | Featured marks
  'x': 56, // Number | X coordinate
  'y': 56, // Number | Y coordinate
  'user': "user_example", // String | Created by user ID
  'collection': "collection_example" // String | Collection ID
};
apiInstance.marksIndex(opts, (error, data, response) => {
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
 **before** | **String**| Before ID (pagination purposes) | [optional] 
 **popular** | **Boolean**| Popular marks | [optional] 
 **lastPopularId** | **String**| Last popular ID (for pagination purposes) | [optional] 
 **featured** | **Boolean**| Featured marks | [optional] 
 **x** | **Number**| X coordinate | [optional] 
 **y** | **Number**| Y coordinate | [optional] 
 **user** | **String**| Created by user ID | [optional] 
 **collection** | **String**| Collection ID | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

