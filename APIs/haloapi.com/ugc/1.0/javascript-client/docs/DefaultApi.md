# Ugc.DefaultApi

All URIs are relative to *https://www.haloapi.com/ugc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call58acde292109180bdcacc40c**](DefaultApi.md#call58acde292109180bdcacc40c) | **GET** /h5/players/{player}/gamevariants/{variant} | Halo 5 - Player Game Variant
[**call58acde292109180bdcacc40d**](DefaultApi.md#call58acde292109180bdcacc40d) | **GET** /h5/players/{player}/gamevariants | Halo 5 - Player Game Variants
[**call58acde292109180bdcacc40e**](DefaultApi.md#call58acde292109180bdcacc40e) | **GET** /h5/players/{player}/mapvariants/{variant} | Halo 5 - Player Map Variant
[**call58acde292109180bdcacc40f**](DefaultApi.md#call58acde292109180bdcacc40f) | **GET** /h5/players/{player}/mapvariants | Halo 5 - Player Map Variants



## call58acde292109180bdcacc40c

> call58acde292109180bdcacc40c(player, variant)

Halo 5 - Player Game Variant

&lt;p&gt;Retrieves Metadata about a Player-created Game Variant.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Get Game Variant\&quot; to \&quot;Halo 5 - Player Game Variant\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;August 5, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

### Example

```javascript
import Ugc from 'ugc';
let defaultClient = Ugc.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new Ugc.DefaultApi();
let player = "player_example"; // String | The Gamertag of the Player that owns the Game Variant.
let variant = "variant_example"; // String | The ID for the Game Variant.
apiInstance.call58acde292109180bdcacc40c(player, variant, (error, data, response) => {
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
 **player** | **String**| The Gamertag of the Player that owns the Game Variant. | 
 **variant** | **String**| The ID for the Game Variant. | 

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## call58acde292109180bdcacc40d

> call58acde292109180bdcacc40d(player, opts)

Halo 5 - Player Game Variants

&lt;p&gt;Retrieves a list of Game Variants created by a Player.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;List Game Variants\&quot; to \&quot;Halo 5 - Player Game Variants\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;August 5, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

### Example

```javascript
import Ugc from 'ugc';
let defaultClient = Ugc.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new Ugc.DefaultApi();
let player = "player_example"; // String | The Gamertag of the Player that owns the listed Game Variants.
let opts = {
  'start': 3.4, // Number | When specified, this indicates the starting index (0-based) for which the list of results will begin at.
  'count': 3.4, // Number | When specified, this indicates the maximum quantity of items the caller would like returned in the response.
  'sort': 3.4, // Number | When specified, this indicates what field should be used to sort the results as the primary sort order. When omitted, \"modified\" (descending) is the assumed primary sort order. Allowed sort fields are: name, description, accessibility, created, modified, bookmarkCount.
  'order': 3.4 // Number | When specified, this indicates the ordering that will be applied. When omitted, \"desc\" is assumed. Allowed order values are: asc, desc.
};
apiInstance.call58acde292109180bdcacc40d(player, opts, (error, data, response) => {
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
 **player** | **String**| The Gamertag of the Player that owns the listed Game Variants. | 
 **start** | **Number**| When specified, this indicates the starting index (0-based) for which the list of results will begin at. | [optional] 
 **count** | **Number**| When specified, this indicates the maximum quantity of items the caller would like returned in the response. | [optional] 
 **sort** | **Number**| When specified, this indicates what field should be used to sort the results as the primary sort order. When omitted, \&quot;modified\&quot; (descending) is the assumed primary sort order. Allowed sort fields are: name, description, accessibility, created, modified, bookmarkCount. | [optional] 
 **order** | **Number**| When specified, this indicates the ordering that will be applied. When omitted, \&quot;desc\&quot; is assumed. Allowed order values are: asc, desc. | [optional] 

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## call58acde292109180bdcacc40e

> call58acde292109180bdcacc40e(player, variant)

Halo 5 - Player Map Variant

&lt;p&gt;Retrieves Metadata about a Player-created Map Variant.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Get Map Variant\&quot; to \&quot;Halo 5 - Player Map Variant\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;August 5, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

### Example

```javascript
import Ugc from 'ugc';
let defaultClient = Ugc.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new Ugc.DefaultApi();
let player = "player_example"; // String | The Gamertag of the Player that owns the Map Variant.
let variant = "variant_example"; // String | The ID for the Map Variant.
apiInstance.call58acde292109180bdcacc40e(player, variant, (error, data, response) => {
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
 **player** | **String**| The Gamertag of the Player that owns the Map Variant. | 
 **variant** | **String**| The ID for the Map Variant. | 

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## call58acde292109180bdcacc40f

> call58acde292109180bdcacc40f(player, opts)

Halo 5 - Player Map Variants

&lt;p&gt;Retrieves a list Map Variants created by a Player.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;List Map Variants\&quot; to \&quot;Halo 5 - Player Map Variants\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;August 5, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

### Example

```javascript
import Ugc from 'ugc';
let defaultClient = Ugc.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new Ugc.DefaultApi();
let player = "player_example"; // String | The Gamertag of the Player that owns the listed Map Variants.
let opts = {
  'start': 3.4, // Number | When specified, this indicates the starting index (0-based) for which the list of results will begin at.
  'count': 3.4, // Number | When specified, this indicates the maximum quantity of items the caller would like returned in the response.
  'sort': 3.4, // Number | When specified, this indicates what field should be used to sort the results as the primary sort order. When omitted, \"modified\" (descending) is the assumed primary sort order. Allowed sort fields are: name, description, accessibility, created, modified, bookmarkCount.
  'order': 3.4 // Number | When specified, this indicates the ordering that will be applied. When omitted, \"desc\" is assumed. Allowed order values are: asc, desc.
};
apiInstance.call58acde292109180bdcacc40f(player, opts, (error, data, response) => {
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
 **player** | **String**| The Gamertag of the Player that owns the listed Map Variants. | 
 **start** | **Number**| When specified, this indicates the starting index (0-based) for which the list of results will begin at. | [optional] 
 **count** | **Number**| When specified, this indicates the maximum quantity of items the caller would like returned in the response. | [optional] 
 **sort** | **Number**| When specified, this indicates what field should be used to sort the results as the primary sort order. When omitted, \&quot;modified\&quot; (descending) is the assumed primary sort order. Allowed sort fields are: name, description, accessibility, created, modified, bookmarkCount. | [optional] 
 **order** | **Number**| When specified, this indicates the ordering that will be applied. When omitted, \&quot;desc\&quot; is assumed. Allowed order values are: asc, desc. | [optional] 

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

