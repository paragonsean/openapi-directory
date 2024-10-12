# NflV3RotoBallerPremiumNews.DefaultApi

All URIs are relative to *http://azure-api.sportsdata.io/v3/nfl/news-rotoballer*

Method | HTTP request | Description
------------- | ------------- | -------------
[**premiumNews**](DefaultApi.md#premiumNews) | **GET** /{format}/RotoBallerPremiumNews | Premium News
[**premiumNewsByDate**](DefaultApi.md#premiumNewsByDate) | **GET** /{format}/RotoBallerPremiumNewsByDate/{date} | Premium News by Date
[**premiumNewsByPlayer**](DefaultApi.md#premiumNewsByPlayer) | **GET** /{format}/RotoBallerPremiumNewsByPlayerID/{playerid} | Premium News by Player
[**premiumNewsByTeam**](DefaultApi.md#premiumNewsByTeam) | **GET** /{format}/RotoBallerPremiumNewsByTeam/{team} | Premium News by Team



## premiumNews

> [News] premiumNews(format)

Premium News

### Example

```javascript
import NflV3RotoBallerPremiumNews from 'nfl_v3_roto_baller_premium_news';
let defaultClient = NflV3RotoBallerPremiumNews.ApiClient.instance;
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

let apiInstance = new NflV3RotoBallerPremiumNews.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
apiInstance.premiumNews(format, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;xml&#39;]

### Return type

[**[News]**](News.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## premiumNewsByDate

> [News] premiumNewsByDate(format, date)

Premium News by Date

### Example

```javascript
import NflV3RotoBallerPremiumNews from 'nfl_v3_roto_baller_premium_news';
let defaultClient = NflV3RotoBallerPremiumNews.ApiClient.instance;
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

let apiInstance = new NflV3RotoBallerPremiumNews.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the news. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.
apiInstance.premiumNewsByDate(format, date, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;xml&#39;]
 **date** | **String**| The date of the news. &lt;br&gt;Examples: &lt;code&gt;2017-JUL-31&lt;/code&gt;, &lt;code&gt;2017-SEP-01&lt;/code&gt;. | 

### Return type

[**[News]**](News.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## premiumNewsByPlayer

> [News] premiumNewsByPlayer(format, playerid)

Premium News by Player

### Example

```javascript
import NflV3RotoBallerPremiumNews from 'nfl_v3_roto_baller_premium_news';
let defaultClient = NflV3RotoBallerPremiumNews.ApiClient.instance;
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

let apiInstance = new NflV3RotoBallerPremiumNews.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let playerid = "playerid_example"; // String | Unique FantasyData Player ID. Example:<code>10000507</code>.
apiInstance.premiumNewsByPlayer(format, playerid, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;xml&#39;]
 **playerid** | **String**| Unique FantasyData Player ID. Example:&lt;code&gt;10000507&lt;/code&gt;. | 

### Return type

[**[News]**](News.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## premiumNewsByTeam

> [News] premiumNewsByTeam(format, team)

Premium News by Team

### Example

```javascript
import NflV3RotoBallerPremiumNews from 'nfl_v3_roto_baller_premium_news';
let defaultClient = NflV3RotoBallerPremiumNews.ApiClient.instance;
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

let apiInstance = new NflV3RotoBallerPremiumNews.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let team = "team_example"; // String | Abbreviation of the team. Example: <code>WAS</code>.
apiInstance.premiumNewsByTeam(format, team, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to &#39;xml&#39;]
 **team** | **String**| Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;. | 

### Return type

[**[News]**](News.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

