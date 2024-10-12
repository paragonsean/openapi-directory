# OpenFec.ReceiptsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedulesScheduleAByEmployerGet**](ReceiptsApi.md#schedulesScheduleAByEmployerGet) | **GET** /schedules/schedule_a/by_employer/ | 
[**schedulesScheduleAByOccupationGet**](ReceiptsApi.md#schedulesScheduleAByOccupationGet) | **GET** /schedules/schedule_a/by_occupation/ | 
[**schedulesScheduleABySizeByCandidateGet**](ReceiptsApi.md#schedulesScheduleABySizeByCandidateGet) | **GET** /schedules/schedule_a/by_size/by_candidate/ | 
[**schedulesScheduleABySizeGet**](ReceiptsApi.md#schedulesScheduleABySizeGet) | **GET** /schedules/schedule_a/by_size/ | 
[**schedulesScheduleAByStateByCandidateGet**](ReceiptsApi.md#schedulesScheduleAByStateByCandidateGet) | **GET** /schedules/schedule_a/by_state/by_candidate/ | 
[**schedulesScheduleAByStateByCandidateTotalsGet**](ReceiptsApi.md#schedulesScheduleAByStateByCandidateTotalsGet) | **GET** /schedules/schedule_a/by_state/by_candidate/totals/ | 
[**schedulesScheduleAByStateGet**](ReceiptsApi.md#schedulesScheduleAByStateGet) | **GET** /schedules/schedule_a/by_state/ | 
[**schedulesScheduleAByStateTotalsGet**](ReceiptsApi.md#schedulesScheduleAByStateTotalsGet) | **GET** /schedules/schedule_a/by_state/totals/ | 
[**schedulesScheduleAByZipGet**](ReceiptsApi.md#schedulesScheduleAByZipGet) | **GET** /schedules/schedule_a/by_zip/ | 
[**schedulesScheduleAEfileGet**](ReceiptsApi.md#schedulesScheduleAEfileGet) | **GET** /schedules/schedule_a/efile/ | 
[**schedulesScheduleAGet**](ReceiptsApi.md#schedulesScheduleAGet) | **GET** /schedules/schedule_a/ | 
[**schedulesScheduleASubIdGet**](ReceiptsApi.md#schedulesScheduleASubIdGet) | **GET** /schedules/schedule_a/{sub_id}/ | 



## schedulesScheduleAByEmployerGet

> ScheduleAByEmployerPage schedulesScheduleAByEmployerGet(apiKey, opts)



 This endpoint provides itemized individual contributions received by a committee, aggregated by the contributor’s employer name. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included. 

### Example

```javascript
import OpenFec from 'open_fec';
let defaultClient = OpenFec.ApiClient.instance;
// Configure API key authorization: ApiKeyHeaderAuth
let ApiKeyHeaderAuth = defaultClient.authentications['ApiKeyHeaderAuth'];
ApiKeyHeaderAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyHeaderAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyQueryAuth
let ApiKeyQueryAuth = defaultClient.authentications['ApiKeyQueryAuth'];
ApiKeyQueryAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyQueryAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new OpenFec.ReceiptsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'cycle': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'employer': ["null"], // [String] | Employer of contributor as reported on the committee's filing
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': "sort_example" // String | Provide a field to sort by. Use `-` for descending order. 
};
apiInstance.schedulesScheduleAByEmployerGet(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **employer** | [**[String]**](String.md)| Employer of contributor as reported on the committee&#39;s filing | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 

### Return type

[**ScheduleAByEmployerPage**](ScheduleAByEmployerPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesScheduleAByOccupationGet

> ScheduleAByOccupationPage schedulesScheduleAByOccupationGet(apiKey, opts)



 This endpoint provides itemized individual contributions received by a committee, aggregated by the contributor’s occupation. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included. 

### Example

```javascript
import OpenFec from 'open_fec';
let defaultClient = OpenFec.ApiClient.instance;
// Configure API key authorization: ApiKeyHeaderAuth
let ApiKeyHeaderAuth = defaultClient.authentications['ApiKeyHeaderAuth'];
ApiKeyHeaderAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyHeaderAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyQueryAuth
let ApiKeyQueryAuth = defaultClient.authentications['ApiKeyQueryAuth'];
ApiKeyQueryAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyQueryAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new OpenFec.ReceiptsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'cycle': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'occupation': ["null"], // [String] | Occupation of contributor as reported on the committee's filing
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': "sort_example" // String | Provide a field to sort by. Use `-` for descending order. 
};
apiInstance.schedulesScheduleAByOccupationGet(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **occupation** | [**[String]**](String.md)| Occupation of contributor as reported on the committee&#39;s filing | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 

### Return type

[**ScheduleAByOccupationPage**](ScheduleAByOccupationPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesScheduleABySizeByCandidateGet

> ScheduleABySizeCandidatePage schedulesScheduleABySizeByCandidateGet(apiKey, cycle, candidateId, opts)



 This endpoint provides itemized individual contributions received by a committee, aggregated by size of contribution and candidate. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included. 

### Example

```javascript
import OpenFec from 'open_fec';
let defaultClient = OpenFec.ApiClient.instance;
// Configure API key authorization: ApiKeyHeaderAuth
let ApiKeyHeaderAuth = defaultClient.authentications['ApiKeyHeaderAuth'];
ApiKeyHeaderAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyHeaderAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyQueryAuth
let ApiKeyQueryAuth = defaultClient.authentications['ApiKeyQueryAuth'];
ApiKeyQueryAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyQueryAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new OpenFec.ReceiptsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let cycle = [null]; // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
let candidateId = ["null"]; // [String] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
let opts = {
  'electionFull': true, // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': "sort_example" // String | Provide a field to sort by. Use `-` for descending order. 
};
apiInstance.schedulesScheduleABySizeByCandidateGet(apiKey, cycle, candidateId, opts, (error, data, response) => {
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
 **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | 
 **candidateId** | [**[String]**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | 
 **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 

### Return type

[**ScheduleABySizeCandidatePage**](ScheduleABySizeCandidatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesScheduleABySizeGet

> ScheduleABySizePage schedulesScheduleABySizeGet(apiKey, opts)



 This endpoint provides individual contributions received by a committee, aggregated by size:  &#x60;&#x60;&#x60;  - $200 and under  - $200.01 - $499.99  - $500 - $999.99  - $1000 - $1999.99  - $2000 + &#x60;&#x60;&#x60;  The $200.00 and under category includes contributions of $200 or less combined with unitemized individual contributions. 

### Example

```javascript
import OpenFec from 'open_fec';
let defaultClient = OpenFec.ApiClient.instance;
// Configure API key authorization: ApiKeyHeaderAuth
let ApiKeyHeaderAuth = defaultClient.authentications['ApiKeyHeaderAuth'];
ApiKeyHeaderAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyHeaderAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyQueryAuth
let ApiKeyQueryAuth = defaultClient.authentications['ApiKeyQueryAuth'];
ApiKeyQueryAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyQueryAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new OpenFec.ReceiptsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'cycle': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'size': [null], // [Number] |  The total all contributions in the following ranges: ```   -0    $200 and under   -200  $200.01 - $499.99   -500  $500 - $999.99   -1000 $1000 - $1999.99   -2000 $2000 + ``` Unitemized contributions are included in the `0` category. 
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': "sort_example" // String | Provide a field to sort by. Use `-` for descending order. 
};
apiInstance.schedulesScheduleABySizeGet(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **size** | [**[Number]**](Number.md)|  The total all contributions in the following ranges: &#x60;&#x60;&#x60;   -0    $200 and under   -200  $200.01 - $499.99   -500  $500 - $999.99   -1000 $1000 - $1999.99   -2000 $2000 + &#x60;&#x60;&#x60; Unitemized contributions are included in the &#x60;0&#x60; category.  | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 

### Return type

[**ScheduleABySizePage**](ScheduleABySizePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesScheduleAByStateByCandidateGet

> ScheduleAByStateCandidatePage schedulesScheduleAByStateByCandidateGet(apiKey, cycle, candidateId, opts)



 This endpoint provides itemized individual contributions received by a committee, aggregated by contributor’s state and candidate. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included. 

### Example

```javascript
import OpenFec from 'open_fec';
let defaultClient = OpenFec.ApiClient.instance;
// Configure API key authorization: ApiKeyHeaderAuth
let ApiKeyHeaderAuth = defaultClient.authentications['ApiKeyHeaderAuth'];
ApiKeyHeaderAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyHeaderAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyQueryAuth
let ApiKeyQueryAuth = defaultClient.authentications['ApiKeyQueryAuth'];
ApiKeyQueryAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyQueryAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new OpenFec.ReceiptsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let cycle = [null]; // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
let candidateId = ["null"]; // [String] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
let opts = {
  'electionFull': true, // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': "sort_example" // String | Provide a field to sort by. Use `-` for descending order. 
};
apiInstance.schedulesScheduleAByStateByCandidateGet(apiKey, cycle, candidateId, opts, (error, data, response) => {
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
 **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | 
 **candidateId** | [**[String]**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | 
 **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 

### Return type

[**ScheduleAByStateCandidatePage**](ScheduleAByStateCandidatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesScheduleAByStateByCandidateTotalsGet

> ScheduleAByStateCandidatePage schedulesScheduleAByStateByCandidateTotalsGet(apiKey, cycle, candidateId, opts)



 Itemized individual contributions aggregated by contributor’s state, candidate, committee type and cycle. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included.  

### Example

```javascript
import OpenFec from 'open_fec';
let defaultClient = OpenFec.ApiClient.instance;
// Configure API key authorization: ApiKeyHeaderAuth
let ApiKeyHeaderAuth = defaultClient.authentications['ApiKeyHeaderAuth'];
ApiKeyHeaderAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyHeaderAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyQueryAuth
let ApiKeyQueryAuth = defaultClient.authentications['ApiKeyQueryAuth'];
ApiKeyQueryAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyQueryAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new OpenFec.ReceiptsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let cycle = [null]; // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
let candidateId = ["null"]; // [String] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
let opts = {
  'electionFull': true, // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': "sort_example" // String | Provide a field to sort by. Use `-` for descending order. 
};
apiInstance.schedulesScheduleAByStateByCandidateTotalsGet(apiKey, cycle, candidateId, opts, (error, data, response) => {
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
 **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | 
 **candidateId** | [**[String]**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | 
 **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 

### Return type

[**ScheduleAByStateCandidatePage**](ScheduleAByStateCandidatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesScheduleAByStateGet

> ScheduleAByStatePage schedulesScheduleAByStateGet(apiKey, opts)



 This endpoint provides itemized individual contributions received by a committee, aggregated by the contributor’s state. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included. 

### Example

```javascript
import OpenFec from 'open_fec';
let defaultClient = OpenFec.ApiClient.instance;
// Configure API key authorization: ApiKeyHeaderAuth
let ApiKeyHeaderAuth = defaultClient.authentications['ApiKeyHeaderAuth'];
ApiKeyHeaderAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyHeaderAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyQueryAuth
let ApiKeyQueryAuth = defaultClient.authentications['ApiKeyQueryAuth'];
ApiKeyQueryAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyQueryAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new OpenFec.ReceiptsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'hideNull': false, // Boolean | Exclude values with missing state
  'cycle': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'page': 1, // Number | For paginating through results, starting at page 1
  'state': ["null"], // [String] | State of contributor
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': "'-total'" // String | Provide a field to sort by. Use `-` for descending order. 
};
apiInstance.schedulesScheduleAByStateGet(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **hideNull** | **Boolean**| Exclude values with missing state | [optional] [default to false]
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **state** | [**[String]**](String.md)| State of contributor | [optional] 
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-total&#39;]

### Return type

[**ScheduleAByStatePage**](ScheduleAByStatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesScheduleAByStateTotalsGet

> ScheduleAByStateRecipientTotalsPage schedulesScheduleAByStateTotalsGet(apiKey, opts)



 This endpoint provides itemized individual contributions received by a committee, aggregated by contributor’s state, committee type and cycle. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included. 

### Example

```javascript
import OpenFec from 'open_fec';
let defaultClient = OpenFec.ApiClient.instance;
// Configure API key authorization: ApiKeyHeaderAuth
let ApiKeyHeaderAuth = defaultClient.authentications['ApiKeyHeaderAuth'];
ApiKeyHeaderAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyHeaderAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyQueryAuth
let ApiKeyQueryAuth = defaultClient.authentications['ApiKeyQueryAuth'];
ApiKeyQueryAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyQueryAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new OpenFec.ReceiptsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'committeeType': ["null"], // [String] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account         - all All Committee Types         - all_candidates All Candidate Committee Types (H, S, P)         - all_pacs All PAC Committee Types (N, O, Q, V, W) 
  'cycle': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'page': 1, // Number | For paginating through results, starting at page 1
  'state': ["null"], // [String] | US state or territory
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': "'cycle'" // String | Provide a field to sort by. Use `-` for descending order. 
};
apiInstance.schedulesScheduleAByStateTotalsGet(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **committeeType** | [**[String]**](String.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account         - all All Committee Types         - all_candidates All Candidate Committee Types (H, S, P)         - all_pacs All PAC Committee Types (N, O, Q, V, W)  | [optional] 
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **state** | [**[String]**](String.md)| US state or territory | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;cycle&#39;]

### Return type

[**ScheduleAByStateRecipientTotalsPage**](ScheduleAByStateRecipientTotalsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesScheduleAByZipGet

> ScheduleAByZipPage schedulesScheduleAByZipGet(apiKey, opts)



 This endpoint provides itemized individual contributions received by a committee, aggregated by the contributor’s ZIP code. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included. 

### Example

```javascript
import OpenFec from 'open_fec';
let defaultClient = OpenFec.ApiClient.instance;
// Configure API key authorization: ApiKeyHeaderAuth
let ApiKeyHeaderAuth = defaultClient.authentications['ApiKeyHeaderAuth'];
ApiKeyHeaderAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyHeaderAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyQueryAuth
let ApiKeyQueryAuth = defaultClient.authentications['ApiKeyQueryAuth'];
ApiKeyQueryAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyQueryAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new OpenFec.ReceiptsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'zip': ["null"], // [String] | Zip code of contributor
  'cycle': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'page': 1, // Number | For paginating through results, starting at page 1
  'state': ["null"], // [String] | State of contributor
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': "sort_example" // String | Provide a field to sort by. Use `-` for descending order. 
};
apiInstance.schedulesScheduleAByZipGet(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **zip** | [**[String]**](String.md)| Zip code of contributor | [optional] 
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **state** | [**[String]**](String.md)| State of contributor | [optional] 
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 

### Return type

[**ScheduleAByZipPage**](ScheduleAByZipPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesScheduleAEfileGet

> ScheduleAEfilePage schedulesScheduleAEfileGet(apiKey, opts)



 Efiling endpoints provide real-time campaign finance data received from electronic filers. Efiling endpoints only contain the most recent four months of data and don&#39;t contain the processed and coded data that you can find on other endpoints. 

### Example

```javascript
import OpenFec from 'open_fec';
let defaultClient = OpenFec.ApiClient.instance;
// Configure API key authorization: ApiKeyHeaderAuth
let ApiKeyHeaderAuth = defaultClient.authentications['ApiKeyHeaderAuth'];
ApiKeyHeaderAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyHeaderAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyQueryAuth
let ApiKeyQueryAuth = defaultClient.authentications['ApiKeyQueryAuth'];
ApiKeyQueryAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyQueryAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new OpenFec.ReceiptsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'minDate': new Date("2013-10-20"), // Date | Minimum date
  'maxImageNumber': "maxImageNumber_example", // String | Maxium image number of the page where the schedule item is reported
  'contributorEmployer': ["null"], // [String] | Employer of contributor, filers need to make an effort to gather this information
  'minImageNumber': "minImageNumber_example", // String | Minium image number of the page where the schedule item is reported
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'contributorName': ["null"], // [String] | Name of contributor
  'minAmount': "minAmount_example", // String | Filter for all amounts greater than a value.
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'contributorState': ["null"], // [String] | State of contributor
  'sort': "'-contribution_receipt_date'", // String | Provide a field to sort by. Use `-` for descending order. 
  'lineNumber': "lineNumber_example", // String | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.
  'contributorOccupation': ["null"], // [String] | Occupation of contributor, filers need to make an effort to gather this information
  'contributorCity': ["null"], // [String] | City of contributor
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'imageNumber': ["null"], // [String] |  An unique identifier for each page where the electronic or paper filing is reported. 
  'maxDate': new Date("2013-10-20"), // Date | Maximum date
  'maxAmount': "maxAmount_example" // String | Filter for all amounts less than a value.
};
apiInstance.schedulesScheduleAEfileGet(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **minDate** | **Date**| Minimum date | [optional] 
 **maxImageNumber** | **String**| Maxium image number of the page where the schedule item is reported | [optional] 
 **contributorEmployer** | [**[String]**](String.md)| Employer of contributor, filers need to make an effort to gather this information | [optional] 
 **minImageNumber** | **String**| Minium image number of the page where the schedule item is reported | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **contributorName** | [**[String]**](String.md)| Name of contributor | [optional] 
 **minAmount** | **String**| Filter for all amounts greater than a value. | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **contributorState** | [**[String]**](String.md)| State of contributor | [optional] 
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-contribution_receipt_date&#39;]
 **lineNumber** | **String**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional] 
 **contributorOccupation** | [**[String]**](String.md)| Occupation of contributor, filers need to make an effort to gather this information | [optional] 
 **contributorCity** | [**[String]**](String.md)| City of contributor | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **imageNumber** | [**[String]**](String.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **maxDate** | **Date**| Maximum date | [optional] 
 **maxAmount** | **String**| Filter for all amounts less than a value. | [optional] 

### Return type

[**ScheduleAEfilePage**](ScheduleAEfilePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesScheduleAGet

> ScheduleAPage schedulesScheduleAGet(apiKey, opts)



 This description is for both ​&#x60;/schedules​/schedule_a​/&#x60; and ​ &#x60;/schedules​/schedule_a​/{sub_id}​/&#x60;.  This endpoint provides itemized receipts. Schedule A records describe itemized receipts, including contributions from individuals. If you are interested in contributions from an individual, use the &#x60;/schedules/schedule_a/&#x60; endpoint. For a more complete description of all Schedule A records visit [About receipts data](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/about-receipts-data/). If you are interested in our \&quot;is_individual\&quot; methodology visit our [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology/).  ​The &#x60;/schedules​/schedule_a​/&#x60; endpoint is not paginated by page number. This endpoint uses keyset pagination to improve query performance and these indices are required to properly page through this large dataset. To request the next page, you should append the values found in the &#x60;last_indexes&#x60; object from pagination to the URL of your last request as additional parameters.  For example, when sorting by &#x60;contribution_receipt_date&#x60;, you might receive a page of results with the two scenarios of following pagination information:  case #1: &#x60;&#x60;&#x60; pagination: {     pages: 2152643,     per_page: 20,     count: 43052850,     last_indexes: {         last_index: \&quot;230880619\&quot;,         last_contribution_receipt_date: \&quot;2014-01-01\&quot;     } } &#x60;&#x60;&#x60; &lt;br/&gt; case #2 (results which include contribution_receipt_date &#x3D; NULL):  &#x60;&#x60;&#x60; pagination: {     pages: 2152644,     per_page: 20,     count: 43052850,     last_indexes: {         last_index: \&quot;230880639\&quot;,         sort_null_only: True     } } &#x60;&#x60;&#x60; To fetch the next page of sorted results, append &#x60;last_index&#x3D;230880619&#x60; and &#x60;last_contribution_receipt_date&#x3D;2014-01-01&#x60; to the URL and when reaching &#x60;contribution_receipt_date&#x3D;NULL&#x60;, append &#x60;last_index&#x3D;230880639&#x60; and &#x60;sort_null_only&#x3D;True&#x60;. We strongly advise paging through these results using sort indices. The default sort is acending by &#x60;contribution_receipt_date&#x60; (&#x60;deprecated&#x60;, will be descending). If you do not page using sort indices, some transactions may be unintentionally filtered out.  Calls to ​&#x60;/schedules​/schedule_a​/&#x60; may return many records. For large result sets, the record counts found in the pagination object are approximate; you will need to page through the records until no records are returned.  To avoid throwing the \&quot;out of range\&quot; exception on the last page, one recommandation is to use total count and &#x60;per_page&#x60; to control the traverse loop of results.  ​The &#x60;/schedules​/schedule_a​/{sub_id}​/&#x60; endpoint returns a single transaction, but it does include a pagination object class. Please ignore the information in that object class.  

### Example

```javascript
import OpenFec from 'open_fec';
let defaultClient = OpenFec.ApiClient.instance;
// Configure API key authorization: ApiKeyHeaderAuth
let ApiKeyHeaderAuth = defaultClient.authentications['ApiKeyHeaderAuth'];
ApiKeyHeaderAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyHeaderAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyQueryAuth
let ApiKeyQueryAuth = defaultClient.authentications['ApiKeyQueryAuth'];
ApiKeyQueryAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyQueryAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new OpenFec.ReceiptsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'isIndividual': true, // Boolean | Restrict to non-earmarked individual contributions where memo code is true. Filtering individuals is useful to make sure contributions are not double reported and in creating breakdowns of the amount of money coming from individuals.
  'minDate': new Date("2013-10-20"), // Date | Minimum date
  'maxImageNumber': "maxImageNumber_example", // String | Maxium image number of the page where the schedule item is reported
  'minImageNumber': "minImageNumber_example", // String | Minium image number of the page where the schedule item is reported
  'contributorType': ["null"], // [String] | Filters individual or committee contributions based on line number
  'contributorId': ["null"], // [String] | The FEC identifier should be represented here if the contributor is registered with the FEC.
  'recipientCommitteeOrgType': ["null"], // [String] | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock 
  'contributorEmployer': ["null"], // [String] | Employer of contributor, filers need to make an effort to gather this information
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'lastIndex': 56, // Number | Index of last result from previous page
  'contributorName': ["null"], // [String] | Name of contributor
  'minAmount': "minAmount_example", // String | Filter for all amounts greater than a value.
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'recipientCommitteeDesignation': ["null"], // [String] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC 
  'maxLoadDate': new Date("2013-10-20"), // Date | Maximum load date
  'recipientCommitteeType': ["null"], // [String] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
  'sort': "'-contribution_receipt_date'", // String | Provide a field to sort by. Use `-` for descending order. 
  'lastContributionReceiptDate': new Date("2013-10-20"), // Date | When sorting by `contribution_receipt_date`, this is populated with the         `contribution_receipt_date` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page.
  'lastContributionReceiptAmount': 3.4, // Number | When sorting by `contribution_receipt_amount`, this is populated with the         `contribution_receipt_amount` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page.
  'lineNumber': "lineNumber_example", // String | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.
  'contributorState': ["null"], // [String] | State of contributor
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'twoYearTransactionPeriod': [null], // [Number] |  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle. 
  'contributorZip': ["null"], // [String] | Zip code of contributor
  'minLoadDate': new Date("2013-10-20"), // Date | Minimum load date
  'contributorOccupation': ["null"], // [String] | Occupation of contributor, filers need to make an effort to gather this information
  'contributorCity': ["null"], // [String] | City of contributor
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'imageNumber': ["null"], // [String] |  An unique identifier for each page where the electronic or paper filing is reported. 
  'maxDate': new Date("2013-10-20"), // Date | Maximum date
  'maxAmount': "maxAmount_example" // String | Filter for all amounts less than a value.
};
apiInstance.schedulesScheduleAGet(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **isIndividual** | **Boolean**| Restrict to non-earmarked individual contributions where memo code is true. Filtering individuals is useful to make sure contributions are not double reported and in creating breakdowns of the amount of money coming from individuals. | [optional] 
 **minDate** | **Date**| Minimum date | [optional] 
 **maxImageNumber** | **String**| Maxium image number of the page where the schedule item is reported | [optional] 
 **minImageNumber** | **String**| Minium image number of the page where the schedule item is reported | [optional] 
 **contributorType** | [**[String]**](String.md)| Filters individual or committee contributions based on line number | [optional] 
 **contributorId** | [**[String]**](String.md)| The FEC identifier should be represented here if the contributor is registered with the FEC. | [optional] 
 **recipientCommitteeOrgType** | [**[String]**](String.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
 **contributorEmployer** | [**[String]**](String.md)| Employer of contributor, filers need to make an effort to gather this information | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **lastIndex** | **Number**| Index of last result from previous page | [optional] 
 **contributorName** | [**[String]**](String.md)| Name of contributor | [optional] 
 **minAmount** | **String**| Filter for all amounts greater than a value. | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **recipientCommitteeDesignation** | [**[String]**](String.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **maxLoadDate** | **Date**| Maximum load date | [optional] 
 **recipientCommitteeType** | [**[String]**](String.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-contribution_receipt_date&#39;]
 **lastContributionReceiptDate** | **Date**| When sorting by &#x60;contribution_receipt_date&#x60;, this is populated with the         &#x60;contribution_receipt_date&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **lastContributionReceiptAmount** | **Number**| When sorting by &#x60;contribution_receipt_amount&#x60;, this is populated with the         &#x60;contribution_receipt_amount&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **lineNumber** | **String**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional] 
 **contributorState** | [**[String]**](String.md)| State of contributor | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **twoYearTransactionPeriod** | [**[Number]**](Number.md)|  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  | [optional] 
 **contributorZip** | [**[String]**](String.md)| Zip code of contributor | [optional] 
 **minLoadDate** | **Date**| Minimum load date | [optional] 
 **contributorOccupation** | [**[String]**](String.md)| Occupation of contributor, filers need to make an effort to gather this information | [optional] 
 **contributorCity** | [**[String]**](String.md)| City of contributor | [optional] 
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **imageNumber** | [**[String]**](String.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **maxDate** | **Date**| Maximum date | [optional] 
 **maxAmount** | **String**| Filter for all amounts less than a value. | [optional] 

### Return type

[**ScheduleAPage**](ScheduleAPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesScheduleASubIdGet

> ScheduleAPage schedulesScheduleASubIdGet(apiKey, subId, opts)



 This description is for both ​&#x60;/schedules​/schedule_a​/&#x60; and ​ &#x60;/schedules​/schedule_a​/{sub_id}​/&#x60;.  This endpoint provides itemized receipts. Schedule A records describe itemized receipts, including contributions from individuals. If you are interested in contributions from an individual, use the &#x60;/schedules/schedule_a/&#x60; endpoint. For a more complete description of all Schedule A records visit [About receipts data](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/about-receipts-data/). If you are interested in our \&quot;is_individual\&quot; methodology visit our [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology/).  ​The &#x60;/schedules​/schedule_a​/&#x60; endpoint is not paginated by page number. This endpoint uses keyset pagination to improve query performance and these indices are required to properly page through this large dataset. To request the next page, you should append the values found in the &#x60;last_indexes&#x60; object from pagination to the URL of your last request as additional parameters.  For example, when sorting by &#x60;contribution_receipt_date&#x60;, you might receive a page of results with the two scenarios of following pagination information:  case #1: &#x60;&#x60;&#x60; pagination: {     pages: 2152643,     per_page: 20,     count: 43052850,     last_indexes: {         last_index: \&quot;230880619\&quot;,         last_contribution_receipt_date: \&quot;2014-01-01\&quot;     } } &#x60;&#x60;&#x60; &lt;br/&gt; case #2 (results which include contribution_receipt_date &#x3D; NULL):  &#x60;&#x60;&#x60; pagination: {     pages: 2152644,     per_page: 20,     count: 43052850,     last_indexes: {         last_index: \&quot;230880639\&quot;,         sort_null_only: True     } } &#x60;&#x60;&#x60; To fetch the next page of sorted results, append &#x60;last_index&#x3D;230880619&#x60; and &#x60;last_contribution_receipt_date&#x3D;2014-01-01&#x60; to the URL and when reaching &#x60;contribution_receipt_date&#x3D;NULL&#x60;, append &#x60;last_index&#x3D;230880639&#x60; and &#x60;sort_null_only&#x3D;True&#x60;. We strongly advise paging through these results using sort indices. The default sort is acending by &#x60;contribution_receipt_date&#x60; (&#x60;deprecated&#x60;, will be descending). If you do not page using sort indices, some transactions may be unintentionally filtered out.  Calls to ​&#x60;/schedules​/schedule_a​/&#x60; may return many records. For large result sets, the record counts found in the pagination object are approximate; you will need to page through the records until no records are returned.  To avoid throwing the \&quot;out of range\&quot; exception on the last page, one recommandation is to use total count and &#x60;per_page&#x60; to control the traverse loop of results.  ​The &#x60;/schedules​/schedule_a​/{sub_id}​/&#x60; endpoint returns a single transaction, but it does include a pagination object class. Please ignore the information in that object class.  

### Example

```javascript
import OpenFec from 'open_fec';
let defaultClient = OpenFec.ApiClient.instance;
// Configure API key authorization: ApiKeyHeaderAuth
let ApiKeyHeaderAuth = defaultClient.authentications['ApiKeyHeaderAuth'];
ApiKeyHeaderAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyHeaderAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyQueryAuth
let ApiKeyQueryAuth = defaultClient.authentications['ApiKeyQueryAuth'];
ApiKeyQueryAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyQueryAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new OpenFec.ReceiptsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let subId = "subId_example"; // String | 
let opts = {
  'isIndividual': true, // Boolean | Restrict to non-earmarked individual contributions where memo code is true. Filtering individuals is useful to make sure contributions are not double reported and in creating breakdowns of the amount of money coming from individuals.
  'minDate': new Date("2013-10-20"), // Date | Minimum date
  'maxImageNumber': "maxImageNumber_example", // String | Maxium image number of the page where the schedule item is reported
  'minImageNumber': "minImageNumber_example", // String | Minium image number of the page where the schedule item is reported
  'contributorType': ["null"], // [String] | Filters individual or committee contributions based on line number
  'contributorId': ["null"], // [String] | The FEC identifier should be represented here if the contributor is registered with the FEC.
  'recipientCommitteeOrgType': ["null"], // [String] | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock 
  'contributorEmployer': ["null"], // [String] | Employer of contributor, filers need to make an effort to gather this information
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'lastIndex': 56, // Number | Index of last result from previous page
  'contributorName': ["null"], // [String] | Name of contributor
  'minAmount': "minAmount_example", // String | Filter for all amounts greater than a value.
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'recipientCommitteeDesignation': ["null"], // [String] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC 
  'maxLoadDate': new Date("2013-10-20"), // Date | Maximum load date
  'recipientCommitteeType': ["null"], // [String] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
  'sort': "'-contribution_receipt_date'", // String | Provide a field to sort by. Use `-` for descending order. 
  'lastContributionReceiptDate': new Date("2013-10-20"), // Date | When sorting by `contribution_receipt_date`, this is populated with the         `contribution_receipt_date` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page.
  'lastContributionReceiptAmount': 3.4, // Number | When sorting by `contribution_receipt_amount`, this is populated with the         `contribution_receipt_amount` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page.
  'lineNumber': "lineNumber_example", // String | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.
  'contributorState': ["null"], // [String] | State of contributor
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'twoYearTransactionPeriod': [null], // [Number] |  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle. 
  'contributorZip': ["null"], // [String] | Zip code of contributor
  'minLoadDate': new Date("2013-10-20"), // Date | Minimum load date
  'contributorOccupation': ["null"], // [String] | Occupation of contributor, filers need to make an effort to gather this information
  'contributorCity': ["null"], // [String] | City of contributor
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'imageNumber': ["null"], // [String] |  An unique identifier for each page where the electronic or paper filing is reported. 
  'maxDate': new Date("2013-10-20"), // Date | Maximum date
  'maxAmount': "maxAmount_example" // String | Filter for all amounts less than a value.
};
apiInstance.schedulesScheduleASubIdGet(apiKey, subId, opts, (error, data, response) => {
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
 **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **subId** | **String**|  | 
 **isIndividual** | **Boolean**| Restrict to non-earmarked individual contributions where memo code is true. Filtering individuals is useful to make sure contributions are not double reported and in creating breakdowns of the amount of money coming from individuals. | [optional] 
 **minDate** | **Date**| Minimum date | [optional] 
 **maxImageNumber** | **String**| Maxium image number of the page where the schedule item is reported | [optional] 
 **minImageNumber** | **String**| Minium image number of the page where the schedule item is reported | [optional] 
 **contributorType** | [**[String]**](String.md)| Filters individual or committee contributions based on line number | [optional] 
 **contributorId** | [**[String]**](String.md)| The FEC identifier should be represented here if the contributor is registered with the FEC. | [optional] 
 **recipientCommitteeOrgType** | [**[String]**](String.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
 **contributorEmployer** | [**[String]**](String.md)| Employer of contributor, filers need to make an effort to gather this information | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **lastIndex** | **Number**| Index of last result from previous page | [optional] 
 **contributorName** | [**[String]**](String.md)| Name of contributor | [optional] 
 **minAmount** | **String**| Filter for all amounts greater than a value. | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **recipientCommitteeDesignation** | [**[String]**](String.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **maxLoadDate** | **Date**| Maximum load date | [optional] 
 **recipientCommitteeType** | [**[String]**](String.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-contribution_receipt_date&#39;]
 **lastContributionReceiptDate** | **Date**| When sorting by &#x60;contribution_receipt_date&#x60;, this is populated with the         &#x60;contribution_receipt_date&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **lastContributionReceiptAmount** | **Number**| When sorting by &#x60;contribution_receipt_amount&#x60;, this is populated with the         &#x60;contribution_receipt_amount&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **lineNumber** | **String**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional] 
 **contributorState** | [**[String]**](String.md)| State of contributor | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **twoYearTransactionPeriod** | [**[Number]**](Number.md)|  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  | [optional] 
 **contributorZip** | [**[String]**](String.md)| Zip code of contributor | [optional] 
 **minLoadDate** | **Date**| Minimum load date | [optional] 
 **contributorOccupation** | [**[String]**](String.md)| Occupation of contributor, filers need to make an effort to gather this information | [optional] 
 **contributorCity** | [**[String]**](String.md)| City of contributor | [optional] 
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **imageNumber** | [**[String]**](String.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **maxDate** | **Date**| Maximum date | [optional] 
 **maxAmount** | **String**| Filter for all amounts less than a value. | [optional] 

### Return type

[**ScheduleAPage**](ScheduleAPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

