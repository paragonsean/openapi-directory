# TradematicCloudApi.TaskManagerAPIApi

All URIs are relative to *https://api.tradematic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**taskmanagerTasksGet**](TaskManagerAPIApi.md#taskmanagerTasksGet) | **GET** /taskmanager/tasks | Get tasks list
[**taskmanagerTasksPost**](TaskManagerAPIApi.md#taskmanagerTasksPost) | **POST** /taskmanager/tasks | Create a new task
[**taskmanagerTasksTaskidBymonthsGet**](TaskManagerAPIApi.md#taskmanagerTasksTaskidBymonthsGet) | **GET** /taskmanager/tasks/{taskid}/bymonths | Get backtest data for equity chart, grouped by months
[**taskmanagerTasksTaskidByquartersGet**](TaskManagerAPIApi.md#taskmanagerTasksTaskidByquartersGet) | **GET** /taskmanager/tasks/{taskid}/byquarters | Get backtest data for equity chart, grouped by quarters
[**taskmanagerTasksTaskidByyearsGet**](TaskManagerAPIApi.md#taskmanagerTasksTaskidByyearsGet) | **GET** /taskmanager/tasks/{taskid}/byyears | Get backtest data for equity chart, grouped by years
[**taskmanagerTasksTaskidContributionGet**](TaskManagerAPIApi.md#taskmanagerTasksTaskidContributionGet) | **GET** /taskmanager/tasks/{taskid}/contribution | Get backtest symbol contribution data
[**taskmanagerTasksTaskidDrawdownGet**](TaskManagerAPIApi.md#taskmanagerTasksTaskidDrawdownGet) | **GET** /taskmanager/tasks/{taskid}/drawdown | Get data for drawdown chart
[**taskmanagerTasksTaskidEquityGet**](TaskManagerAPIApi.md#taskmanagerTasksTaskidEquityGet) | **GET** /taskmanager/tasks/{taskid}/equity | Get data for equity chart
[**taskmanagerTasksTaskidEquitypctGet**](TaskManagerAPIApi.md#taskmanagerTasksTaskidEquitypctGet) | **GET** /taskmanager/tasks/{taskid}/equitypct | Get data for equity chart (%)
[**taskmanagerTasksTaskidEquitypctsmGet**](TaskManagerAPIApi.md#taskmanagerTasksTaskidEquitypctsmGet) | **GET** /taskmanager/tasks/{taskid}/equitypctsm | Get spared data for equity chart (%)
[**taskmanagerTasksTaskidFolderGet**](TaskManagerAPIApi.md#taskmanagerTasksTaskidFolderGet) | **GET** /taskmanager/tasks/{taskid}/folder | Get task result folder name
[**taskmanagerTasksTaskidGet**](TaskManagerAPIApi.md#taskmanagerTasksTaskidGet) | **GET** /taskmanager/tasks/{taskid} | Get task by ID
[**taskmanagerTasksTaskidPerformanceGet**](TaskManagerAPIApi.md#taskmanagerTasksTaskidPerformanceGet) | **GET** /taskmanager/tasks/{taskid}/performance | Get backtest statistics
[**taskmanagerTasksTaskidResult2Get**](TaskManagerAPIApi.md#taskmanagerTasksTaskidResult2Get) | **GET** /taskmanager/tasks/{taskid}/result2 | Get task result (version 2)
[**taskmanagerTasksTaskidResultGet**](TaskManagerAPIApi.md#taskmanagerTasksTaskidResultGet) | **GET** /taskmanager/tasks/{taskid}/result | Get task result
[**taskmanagerTasksTaskidStatusGet**](TaskManagerAPIApi.md#taskmanagerTasksTaskidStatusGet) | **GET** /taskmanager/tasks/{taskid}/status | Get task status
[**taskmanagerTasksTaskidTradesGet**](TaskManagerAPIApi.md#taskmanagerTasksTaskidTradesGet) | **GET** /taskmanager/tasks/{taskid}/trades | Get backtest trades list



## taskmanagerTasksGet

> [Task] taskmanagerTasksGet()

Get tasks list

Get tasks list

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.TaskManagerAPIApi();
apiInstance.taskmanagerTasksGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Task]**](Task.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskmanagerTasksPost

> TaskmanagerTasksPost202Response taskmanagerTasksPost(body)

Create a new task

Create a new task

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.TaskManagerAPIApi();
let body = new TradematicCloudApi.TaskmanagerTasksPostRequest(); // TaskmanagerTasksPostRequest | 
apiInstance.taskmanagerTasksPost(body, (error, data, response) => {
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
 **body** | [**TaskmanagerTasksPostRequest**](TaskmanagerTasksPostRequest.md)|  | 

### Return type

[**TaskmanagerTasksPost202Response**](TaskmanagerTasksPost202Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskmanagerTasksTaskidBymonthsGet

> [ByMonths] taskmanagerTasksTaskidBymonthsGet(taskid)

Get backtest data for equity chart, grouped by months

Get backtest data for equity chart, grouped by months

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.TaskManagerAPIApi();
let taskid = 789; // Number | 
apiInstance.taskmanagerTasksTaskidBymonthsGet(taskid, (error, data, response) => {
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
 **taskid** | **Number**|  | 

### Return type

[**[ByMonths]**](ByMonths.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskmanagerTasksTaskidByquartersGet

> [ByQuarters] taskmanagerTasksTaskidByquartersGet(taskid)

Get backtest data for equity chart, grouped by quarters

Get backtest data for equity chart, grouped by quarters

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.TaskManagerAPIApi();
let taskid = 789; // Number | 
apiInstance.taskmanagerTasksTaskidByquartersGet(taskid, (error, data, response) => {
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
 **taskid** | **Number**|  | 

### Return type

[**[ByQuarters]**](ByQuarters.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskmanagerTasksTaskidByyearsGet

> [ByYears] taskmanagerTasksTaskidByyearsGet(taskid)

Get backtest data for equity chart, grouped by years

Get backtest data for equity chart, grouped by years

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.TaskManagerAPIApi();
let taskid = 789; // Number | 
apiInstance.taskmanagerTasksTaskidByyearsGet(taskid, (error, data, response) => {
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
 **taskid** | **Number**|  | 

### Return type

[**[ByYears]**](ByYears.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskmanagerTasksTaskidContributionGet

> [Contribution] taskmanagerTasksTaskidContributionGet(taskid)

Get backtest symbol contribution data

Get backtest symbol contribution data

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.TaskManagerAPIApi();
let taskid = 789; // Number | 
apiInstance.taskmanagerTasksTaskidContributionGet(taskid, (error, data, response) => {
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
 **taskid** | **Number**|  | 

### Return type

[**[Contribution]**](Contribution.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskmanagerTasksTaskidDrawdownGet

> [DrawdownItem] taskmanagerTasksTaskidDrawdownGet(taskid)

Get data for drawdown chart

Get data for drawdown chart

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.TaskManagerAPIApi();
let taskid = 789; // Number | 
apiInstance.taskmanagerTasksTaskidDrawdownGet(taskid, (error, data, response) => {
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
 **taskid** | **Number**|  | 

### Return type

[**[DrawdownItem]**](DrawdownItem.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskmanagerTasksTaskidEquityGet

> [EquityItem] taskmanagerTasksTaskidEquityGet(taskid)

Get data for equity chart

Get data for equity chart

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.TaskManagerAPIApi();
let taskid = 789; // Number | 
apiInstance.taskmanagerTasksTaskidEquityGet(taskid, (error, data, response) => {
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
 **taskid** | **Number**|  | 

### Return type

[**[EquityItem]**](EquityItem.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskmanagerTasksTaskidEquitypctGet

> [EquityPctItem] taskmanagerTasksTaskidEquitypctGet(taskid)

Get data for equity chart (%)

Get data for equity chart (%)

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.TaskManagerAPIApi();
let taskid = 789; // Number | 
apiInstance.taskmanagerTasksTaskidEquitypctGet(taskid, (error, data, response) => {
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
 **taskid** | **Number**|  | 

### Return type

[**[EquityPctItem]**](EquityPctItem.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskmanagerTasksTaskidEquitypctsmGet

> [EquityPctSmItem] taskmanagerTasksTaskidEquitypctsmGet(taskid)

Get spared data for equity chart (%)

Get spared data for equity chart (%)

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.TaskManagerAPIApi();
let taskid = 789; // Number | 
apiInstance.taskmanagerTasksTaskidEquitypctsmGet(taskid, (error, data, response) => {
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
 **taskid** | **Number**|  | 

### Return type

[**[EquityPctSmItem]**](EquityPctSmItem.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskmanagerTasksTaskidFolderGet

> TaskmanagerTasksTaskidFolderGet200Response taskmanagerTasksTaskidFolderGet(taskid)

Get task result folder name

Get task result folder name

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.TaskManagerAPIApi();
let taskid = 789; // Number | 
apiInstance.taskmanagerTasksTaskidFolderGet(taskid, (error, data, response) => {
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
 **taskid** | **Number**|  | 

### Return type

[**TaskmanagerTasksTaskidFolderGet200Response**](TaskmanagerTasksTaskidFolderGet200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskmanagerTasksTaskidGet

> Task taskmanagerTasksTaskidGet(taskid)

Get task by ID

Get task by ID

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.TaskManagerAPIApi();
let taskid = 789; // Number | 
apiInstance.taskmanagerTasksTaskidGet(taskid, (error, data, response) => {
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
 **taskid** | **Number**|  | 

### Return type

[**Task**](Task.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskmanagerTasksTaskidPerformanceGet

> TaskmanagerTasksTaskidPerformanceGet200Response taskmanagerTasksTaskidPerformanceGet(taskid)

Get backtest statistics

Get backtest statistics

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.TaskManagerAPIApi();
let taskid = 789; // Number | 
apiInstance.taskmanagerTasksTaskidPerformanceGet(taskid, (error, data, response) => {
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
 **taskid** | **Number**|  | 

### Return type

[**TaskmanagerTasksTaskidPerformanceGet200Response**](TaskmanagerTasksTaskidPerformanceGet200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskmanagerTasksTaskidResult2Get

> TaskmanagerTasksTaskidResult2Get200Response taskmanagerTasksTaskidResult2Get(taskid)

Get task result (version 2)

Get task result (version 2)

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.TaskManagerAPIApi();
let taskid = 789; // Number | 
apiInstance.taskmanagerTasksTaskidResult2Get(taskid, (error, data, response) => {
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
 **taskid** | **Number**|  | 

### Return type

[**TaskmanagerTasksTaskidResult2Get200Response**](TaskmanagerTasksTaskidResult2Get200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskmanagerTasksTaskidResultGet

> TaskmanagerTasksTaskidResultGet200Response taskmanagerTasksTaskidResultGet(taskid)

Get task result

Get task result

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.TaskManagerAPIApi();
let taskid = 789; // Number | 
apiInstance.taskmanagerTasksTaskidResultGet(taskid, (error, data, response) => {
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
 **taskid** | **Number**|  | 

### Return type

[**TaskmanagerTasksTaskidResultGet200Response**](TaskmanagerTasksTaskidResultGet200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskmanagerTasksTaskidStatusGet

> TaskmanagerTasksTaskidStatusGet200Response taskmanagerTasksTaskidStatusGet(taskid)

Get task status

Get task status

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.TaskManagerAPIApi();
let taskid = 789; // Number | 
apiInstance.taskmanagerTasksTaskidStatusGet(taskid, (error, data, response) => {
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
 **taskid** | **Number**|  | 

### Return type

[**TaskmanagerTasksTaskidStatusGet200Response**](TaskmanagerTasksTaskidStatusGet200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskmanagerTasksTaskidTradesGet

> [BacktestTrade] taskmanagerTasksTaskidTradesGet(taskid)

Get backtest trades list

Get backtest trades list

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.TaskManagerAPIApi();
let taskid = 789; // Number | 
apiInstance.taskmanagerTasksTaskidTradesGet(taskid, (error, data, response) => {
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
 **taskid** | **Number**|  | 

### Return type

[**[BacktestTrade]**](BacktestTrade.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

