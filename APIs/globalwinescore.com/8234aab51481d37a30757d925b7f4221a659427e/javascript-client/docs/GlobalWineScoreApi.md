# GlobalWineScoreApiDocumentation.GlobalWineScoreApi

All URIs are relative to *https://api.globalwinescore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**globalwinescoresLatestGet**](GlobalWineScoreApi.md#globalwinescoresLatestGet) | **GET** /globalwinescores/latest/ | List all latest GWS
[**listHistoricalGWS**](GlobalWineScoreApi.md#listHistoricalGWS) | **GET** /globalwinescores/ | List all historical GWS



## globalwinescoresLatestGet

> globalwinescoresLatestGet(opts)

List all latest GWS

Returns the latest GWS available per wine/vintage.

### Example

```javascript
import GlobalWineScoreApiDocumentation from 'global_wine_score_api_documentation';
let defaultClient = GlobalWineScoreApiDocumentation.ApiClient.instance;
// Configure API key authorization: TokenAuthentication
let TokenAuthentication = defaultClient.authentications['TokenAuthentication'];
TokenAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new GlobalWineScoreApiDocumentation.GlobalWineScoreApi();
let opts = {
  'authorization': "Token <YOUR-API-TOKEN>", // String | 
  'wineId': [null], // [Number] | The exact `id` of the wine. Can be used multiple times (e.g `?wine_id=114959&wine_id=114952`) <br/> If you need to find the `wine_id` for your wines, use our <a href=\"https://api.globalwinescore.com/search/\" target=\"_blank\">search page</a> 
  'vintage': "2000", // String | The vintage you want to search against.
  'color': "color_example", // String | The lowercase color of the wine.
  'isPrimeurs': false, // Boolean | Only show the <a href=\"See https://en.wikipedia.org/wiki/En_primeur\">en primeur</a> GlobalWineScores 
  'lwin': "1014033", // String | L-WIN wine identifier (See definition <a href=\"https://www.liv-ex.com/lwin/\" target=\"_blank\">here</a>) 
  'lwin11': "10140332000", // String | L-WIN wine/vintage identifier (See definition <a href=\"https://www.liv-ex.com/lwin/\" target=\"_blank\">here</a>) 
  'limit': 100, // Number | Number of results to return per page.
  'offset': 100, // Number | The initial index from which to return the results.
  'ordering': "'-date'" // String | Which field to use when ordering the results.
};
apiInstance.globalwinescoresLatestGet(opts, (error, data, response) => {
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
 **authorization** | **String**|  | [optional] 
 **wineId** | [**[Number]**](Number.md)| The exact &#x60;id&#x60; of the wine. Can be used multiple times (e.g &#x60;?wine_id&#x3D;114959&amp;wine_id&#x3D;114952&#x60;) &lt;br/&gt; If you need to find the &#x60;wine_id&#x60; for your wines, use our &lt;a href&#x3D;\&quot;https://api.globalwinescore.com/search/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;search page&lt;/a&gt;  | [optional] 
 **vintage** | **String**| The vintage you want to search against. | [optional] 
 **color** | **String**| The lowercase color of the wine. | [optional] 
 **isPrimeurs** | **Boolean**| Only show the &lt;a href&#x3D;\&quot;See https://en.wikipedia.org/wiki/En_primeur\&quot;&gt;en primeur&lt;/a&gt; GlobalWineScores  | [optional] [default to false]
 **lwin** | **String**| L-WIN wine identifier (See definition &lt;a href&#x3D;\&quot;https://www.liv-ex.com/lwin/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;)  | [optional] 
 **lwin11** | **String**| L-WIN wine/vintage identifier (See definition &lt;a href&#x3D;\&quot;https://www.liv-ex.com/lwin/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;)  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] [default to 100]
 **offset** | **Number**| The initial index from which to return the results. | [optional] 
 **ordering** | **String**| Which field to use when ordering the results. | [optional] [default to &#39;-date&#39;]

### Return type

null (empty response body)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listHistoricalGWS

> listHistoricalGWS(opts)

List all historical GWS

Returns all available GWS

### Example

```javascript
import GlobalWineScoreApiDocumentation from 'global_wine_score_api_documentation';
let defaultClient = GlobalWineScoreApiDocumentation.ApiClient.instance;
// Configure API key authorization: TokenAuthentication
let TokenAuthentication = defaultClient.authentications['TokenAuthentication'];
TokenAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new GlobalWineScoreApiDocumentation.GlobalWineScoreApi();
let opts = {
  'authorization': "Token <YOUR-API-TOKEN>", // String | 
  'wineId': [null], // [Number] | The exact `id` of the wine. Can be used multiple times (e.g `?wine_id=114959&wine_id=114952`) <br/> If you need to find the `wine_id` for your wines, use our <a href=\"https://api.globalwinescore.com/search/\" target=\"_blank\">search page</a> 
  'vintage': "2000", // String | The vintage you want to search against.
  'color': "color_example", // String | The lowercase color of the wine.
  'isPrimeurs': false, // Boolean | Only show the <a href=\"See https://en.wikipedia.org/wiki/En_primeur\">en primeur</a> GlobalWineScores 
  'lwin': "1014033", // String | L-WIN wine identifier (See definition <a href=\"https://www.liv-ex.com/lwin/\" target=\"_blank\">here</a>) 
  'lwin11': "10140332000", // String | L-WIN wine/vintage identifier (See definition <a href=\"https://www.liv-ex.com/lwin/\" target=\"_blank\">here</a>) 
  'limit': 100, // Number | Number of results to return per page.
  'offset': 100, // Number | The initial index from which to return the results.
  'ordering': "'-date'" // String | Which field to use when ordering the results.
};
apiInstance.listHistoricalGWS(opts, (error, data, response) => {
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
 **authorization** | **String**|  | [optional] 
 **wineId** | [**[Number]**](Number.md)| The exact &#x60;id&#x60; of the wine. Can be used multiple times (e.g &#x60;?wine_id&#x3D;114959&amp;wine_id&#x3D;114952&#x60;) &lt;br/&gt; If you need to find the &#x60;wine_id&#x60; for your wines, use our &lt;a href&#x3D;\&quot;https://api.globalwinescore.com/search/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;search page&lt;/a&gt;  | [optional] 
 **vintage** | **String**| The vintage you want to search against. | [optional] 
 **color** | **String**| The lowercase color of the wine. | [optional] 
 **isPrimeurs** | **Boolean**| Only show the &lt;a href&#x3D;\&quot;See https://en.wikipedia.org/wiki/En_primeur\&quot;&gt;en primeur&lt;/a&gt; GlobalWineScores  | [optional] [default to false]
 **lwin** | **String**| L-WIN wine identifier (See definition &lt;a href&#x3D;\&quot;https://www.liv-ex.com/lwin/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;)  | [optional] 
 **lwin11** | **String**| L-WIN wine/vintage identifier (See definition &lt;a href&#x3D;\&quot;https://www.liv-ex.com/lwin/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;)  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] [default to 100]
 **offset** | **Number**| The initial index from which to return the results. | [optional] 
 **ordering** | **String**| Which field to use when ordering the results. | [optional] [default to &#39;-date&#39;]

### Return type

null (empty response body)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

