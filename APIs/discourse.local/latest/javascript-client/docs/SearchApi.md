# DiscourseApiDocumentation.SearchApi

All URIs are relative to *http://discourse.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **GET** /search.json | Search for a term



## search

> Search200Response search(opts)

Search for a term

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.SearchApi();
let opts = {
  'q': "api @blake #support tags:api after:2021-06-04 in:unseen in:open order:latest_topic", // String | The query string needs to be url encoded and is made up of the following options: - Search term. This is just a string. Usually it would be the first item in the query. - `@<username>`: Use the `@` followed by the username to specify posts by this user. - `#<category>`: Use the `#` followed by the category slug to search within this category. - `tags:`: `api,solved` or for posts that have all the specified tags `api+solved`. - `before:`: `yyyy-mm-dd` - `after:`: `yyyy-mm-dd` - `order:`: `latest`, `likes`, `views`, `latest_topic` - `assigned:`: username (without `@`) - `in:`: `title`, `likes`, `personal`, `messages`, `seen`, `unseen`, `posted`, `created`, `watching`, `tracking`, `bookmarks`, `assigned`, `unassigned`, `first`, `pinned`, `wiki` - `with:`: `images` - `status:`: `open`, `closed`, `public`, `archived`, `noreplies`, `single_user`, `solved`, `unsolved` - `group:`: group_name or group_id - `group_messages:`: group_name or group_id - `min_posts:`: 1 - `max_posts:`: 10 - `min_views:`: 1 - `max_views:`: 10  If you are using cURL you can use the `-G` and the `--data-urlencode` flags to encode the query:  ``` curl -i -sS -X GET -G \"http://localhost:4200/search.json\" \\ --data-urlencode 'q=wordpress @scossar #fun after:2020-01-01' ``` 
  'page': 1 // Number | 
};
apiInstance.search(opts, (error, data, response) => {
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
 **q** | **String**| The query string needs to be url encoded and is made up of the following options: - Search term. This is just a string. Usually it would be the first item in the query. - &#x60;@&lt;username&gt;&#x60;: Use the &#x60;@&#x60; followed by the username to specify posts by this user. - &#x60;#&lt;category&gt;&#x60;: Use the &#x60;#&#x60; followed by the category slug to search within this category. - &#x60;tags:&#x60;: &#x60;api,solved&#x60; or for posts that have all the specified tags &#x60;api+solved&#x60;. - &#x60;before:&#x60;: &#x60;yyyy-mm-dd&#x60; - &#x60;after:&#x60;: &#x60;yyyy-mm-dd&#x60; - &#x60;order:&#x60;: &#x60;latest&#x60;, &#x60;likes&#x60;, &#x60;views&#x60;, &#x60;latest_topic&#x60; - &#x60;assigned:&#x60;: username (without &#x60;@&#x60;) - &#x60;in:&#x60;: &#x60;title&#x60;, &#x60;likes&#x60;, &#x60;personal&#x60;, &#x60;messages&#x60;, &#x60;seen&#x60;, &#x60;unseen&#x60;, &#x60;posted&#x60;, &#x60;created&#x60;, &#x60;watching&#x60;, &#x60;tracking&#x60;, &#x60;bookmarks&#x60;, &#x60;assigned&#x60;, &#x60;unassigned&#x60;, &#x60;first&#x60;, &#x60;pinned&#x60;, &#x60;wiki&#x60; - &#x60;with:&#x60;: &#x60;images&#x60; - &#x60;status:&#x60;: &#x60;open&#x60;, &#x60;closed&#x60;, &#x60;public&#x60;, &#x60;archived&#x60;, &#x60;noreplies&#x60;, &#x60;single_user&#x60;, &#x60;solved&#x60;, &#x60;unsolved&#x60; - &#x60;group:&#x60;: group_name or group_id - &#x60;group_messages:&#x60;: group_name or group_id - &#x60;min_posts:&#x60;: 1 - &#x60;max_posts:&#x60;: 10 - &#x60;min_views:&#x60;: 1 - &#x60;max_views:&#x60;: 10  If you are using cURL you can use the &#x60;-G&#x60; and the &#x60;--data-urlencode&#x60; flags to encode the query:  &#x60;&#x60;&#x60; curl -i -sS -X GET -G \&quot;http://localhost:4200/search.json\&quot; \\ --data-urlencode &#39;q&#x3D;wordpress @scossar #fun after:2020-01-01&#39; &#x60;&#x60;&#x60;  | [optional] 
 **page** | **Number**|  | [optional] 

### Return type

[**Search200Response**](Search200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

