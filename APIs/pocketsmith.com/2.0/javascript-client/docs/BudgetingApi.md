# PocketSmith.BudgetingApi

All URIs are relative to *https://api.pocketsmith.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersIdBudgetGet**](BudgetingApi.md#usersIdBudgetGet) | **GET** /users/{id}/budget | List budget for user
[**usersIdBudgetSummaryGet**](BudgetingApi.md#usersIdBudgetSummaryGet) | **GET** /users/{id}/budget_summary | Get budget summary for user
[**usersIdForecastCacheDelete**](BudgetingApi.md#usersIdForecastCacheDelete) | **DELETE** /users/{id}/forecast_cache | Delete forecast cache for user
[**usersIdTrendAnalysisGet**](BudgetingApi.md#usersIdTrendAnalysisGet) | **GET** /users/{id}/trend_analysis | Get trend analysis for user



## usersIdBudgetGet

> [BudgetAnalysisPackage] usersIdBudgetGet(id, opts)

List budget for user

Lists the user&#39;s budget, consisting of one or more budget analysis packages, one per category. Akin to the list on the Budget page in PocketSmith.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.BudgetingApi();
let id = 42; // Number | The unique identifier of the account.
let opts = {
  'rollUp': true // Boolean | Whether parent categories should have their children rolled up into them. When used, the children will still appear in the collection on their own, but their actual and forecast figures will be rolled up to the root parent.
};
apiInstance.usersIdBudgetGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the account. | 
 **rollUp** | **Boolean**| Whether parent categories should have their children rolled up into them. When used, the children will still appear in the collection on their own, but their actual and forecast figures will be rolled up to the root parent. | [optional] 

### Return type

[**[BudgetAnalysisPackage]**](BudgetAnalysisPackage.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdBudgetSummaryGet

> [BudgetAnalysisPackage] usersIdBudgetSummaryGet(id, period, interval, startDate, endDate)

Get budget summary for user

Get the user&#39;s budget summary, containing an expense and income analysis for all categories (excluding transfer categories) for the given period and date range. Akin to the overall budget shown on the Budget page in PocketSmith.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.BudgetingApi();
let id = 42; // Number | The unique identifier of the user.
let period = "weeks"; // String | The period to analyse in, one of `weeks`, `months` or `years`. Also supported is `event`, although event period analysis is only possible when the budget events gathered align, so in this case where all categories are analysed together, it's highly unlikely that event period analysis will be possible.
let interval = 2; // Number | The period interval, e.g. if the interval is 2 and the period is weeks, the budget will be analysed fortnightly.
let startDate = "2016-11-01"; // String | The date to start analysing the budget from. This will be bumped out to make full periods as necessary.
let endDate = "2016-11-30"; // String | The date to stop analysing the budget from. This will be bumped out to make full periods as necessary.
apiInstance.usersIdBudgetSummaryGet(id, period, interval, startDate, endDate, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the user. | 
 **period** | **String**| The period to analyse in, one of &#x60;weeks&#x60;, &#x60;months&#x60; or &#x60;years&#x60;. Also supported is &#x60;event&#x60;, although event period analysis is only possible when the budget events gathered align, so in this case where all categories are analysed together, it&#39;s highly unlikely that event period analysis will be possible. | 
 **interval** | **Number**| The period interval, e.g. if the interval is 2 and the period is weeks, the budget will be analysed fortnightly. | 
 **startDate** | **String**| The date to start analysing the budget from. This will be bumped out to make full periods as necessary. | 
 **endDate** | **String**| The date to stop analysing the budget from. This will be bumped out to make full periods as necessary. | 

### Return type

[**[BudgetAnalysisPackage]**](BudgetAnalysisPackage.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdForecastCacheDelete

> usersIdForecastCacheDelete(id)

Delete forecast cache for user

Delete the user&#39;s cached forecast by recalculating the forecast.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.BudgetingApi();
let id = 42; // Number | The unique identifier of the user.
apiInstance.usersIdForecastCacheDelete(id, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the user. | 

### Return type

null (empty response body)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdTrendAnalysisGet

> [BudgetAnalysisPackage] usersIdTrendAnalysisGet(id, period, interval, startDate, endDate, categories, scenarios)

Get trend analysis for user

Get an income and/or expense budget analysis for the given date range and period across any number of categories and scenarios. Akin to the Trends page in PocketSmith.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.BudgetingApi();
let id = 42; // Number | The unique identifier of the user.
let period = "weeks"; // String | The period to analyse in, one of `weeks`, `months` or `years`. Also supported is `event`, although event period analysis is only possible when the budget events gathered align, so in this case where all categories are analysed together, it's highly unlikely that event period analysis will be possible.
let interval = true; // Number | The period interval, e.g. if the interval is 2 and the period is weeks, the budget will be analysed fortnightly.
let startDate = "2016-11-01"; // String | The date to start analysing the budget from. This will be bumped out to make full periods as necessary.
let endDate = "2016-11-30"; // String | The date to stop analysing the budget from. This will be bumped out to make full periods as necessary.
let categories = "42,49"; // String | A comma-separated list of category IDs to analyse.
let scenarios = "11,29"; // String | A comma-separated list of scenario IDs to analyse. You're likely going to want to include all a user's scenarios here, unless you have reason to only analyse for a subset of scenarios. Regardless of what scenarios are analysed, all actuals (transactions) across all accounts will be included.
apiInstance.usersIdTrendAnalysisGet(id, period, interval, startDate, endDate, categories, scenarios, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the user. | 
 **period** | **String**| The period to analyse in, one of &#x60;weeks&#x60;, &#x60;months&#x60; or &#x60;years&#x60;. Also supported is &#x60;event&#x60;, although event period analysis is only possible when the budget events gathered align, so in this case where all categories are analysed together, it&#39;s highly unlikely that event period analysis will be possible. | 
 **interval** | **Number**| The period interval, e.g. if the interval is 2 and the period is weeks, the budget will be analysed fortnightly. | 
 **startDate** | **String**| The date to start analysing the budget from. This will be bumped out to make full periods as necessary. | 
 **endDate** | **String**| The date to stop analysing the budget from. This will be bumped out to make full periods as necessary. | 
 **categories** | **String**| A comma-separated list of category IDs to analyse. | 
 **scenarios** | **String**| A comma-separated list of scenario IDs to analyse. You&#39;re likely going to want to include all a user&#39;s scenarios here, unless you have reason to only analyse for a subset of scenarios. Regardless of what scenarios are analysed, all actuals (transactions) across all accounts will be included. | 

### Return type

[**[BudgetAnalysisPackage]**](BudgetAnalysisPackage.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

