# LoLV3Projections.DefaultApi

All URIs are relative to *http://azure-api.sportsdata.io/v3/lol/projections*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dfsSlatesByDate**](DefaultApi.md#dfsSlatesByDate) | **GET** /{format}/DfsSlatesByDate/{date} | Dfs Slates By Date
[**projectedPlayerGameStatsByDate**](DefaultApi.md#projectedPlayerGameStatsByDate) | **GET** /{format}/PlayerGameProjectionStatsByDate/{date} | Projected Player Game Stats by Date
[**projectedPlayerGameStatsByPlayer**](DefaultApi.md#projectedPlayerGameStatsByPlayer) | **GET** /{format}/PlayerGameProjectionStatsByPlayer/{date}/{playerid} | Projected Player Game Stats by Player



## dfsSlatesByDate

> [DfsSlate] dfsSlatesByDate(format, date)

Dfs Slates By Date

### Example

```javascript
import LoLV3Projections from 'lo_l_v3_projections';
let defaultClient = LoLV3Projections.ApiClient.instance;
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

let apiInstance = new LoLV3Projections.DefaultApi();
let format = "format_example"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
apiInstance.dfsSlatesByDate(format, date, (error, data, response) => {
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
 **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **date** | **String**| The date of the game(s). &lt;br&gt;Examples: &lt;code&gt;2017-02-27&lt;/code&gt;, &lt;code&gt;2017-09-01&lt;/code&gt;. | 

### Return type

[**[DfsSlate]**](DfsSlate.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectedPlayerGameStatsByDate

> [PlayerGameProjection] projectedPlayerGameStatsByDate(format, date)

Projected Player Game Stats by Date

Projected Player Game Stats by Date

### Example

```javascript
import LoLV3Projections from 'lo_l_v3_projections';
let defaultClient = LoLV3Projections.ApiClient.instance;
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

let apiInstance = new LoLV3Projections.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Example: <code>2019-01-20</code>
apiInstance.projectedPlayerGameStatsByDate(format, date, (error, data, response) => {
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
 **date** | **String**| The date of the game(s). &lt;br&gt;Example: &lt;code&gt;2019-01-20&lt;/code&gt; | 

### Return type

[**[PlayerGameProjection]**](PlayerGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectedPlayerGameStatsByPlayer

> [PlayerGameProjection] projectedPlayerGameStatsByPlayer(format, date, playerid)

Projected Player Game Stats by Player

Projected Player Game Stats by Date

### Example

```javascript
import LoLV3Projections from 'lo_l_v3_projections';
let defaultClient = LoLV3Projections.ApiClient.instance;
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

let apiInstance = new LoLV3Projections.DefaultApi();
let format = "'xml'"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
let date = "date_example"; // String | The date of the game(s). <br>Example: <code>2019-01-20</code>
let playerid = "playerid_example"; // String | Unique FantasyData Player ID. Example:<code>100001500</code>.
apiInstance.projectedPlayerGameStatsByPlayer(format, date, playerid, (error, data, response) => {
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
 **date** | **String**| The date of the game(s). &lt;br&gt;Example: &lt;code&gt;2019-01-20&lt;/code&gt; | 
 **playerid** | **String**| Unique FantasyData Player ID. Example:&lt;code&gt;100001500&lt;/code&gt;. | 

### Return type

[**[PlayerGameProjection]**](PlayerGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

