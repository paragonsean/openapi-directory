# OpenFec.CandidateApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**candidateCandidateIdGet**](CandidateApi.md#candidateCandidateIdGet) | **GET** /candidate/{candidate_id}/ | 
[**candidateCandidateIdHistoryCycleGet**](CandidateApi.md#candidateCandidateIdHistoryCycleGet) | **GET** /candidate/{candidate_id}/history/{cycle}/ | 
[**candidateCandidateIdHistoryGet**](CandidateApi.md#candidateCandidateIdHistoryGet) | **GET** /candidate/{candidate_id}/history/ | 
[**candidateCandidateIdTotalsGet**](CandidateApi.md#candidateCandidateIdTotalsGet) | **GET** /candidate/{candidate_id}/totals/ | 
[**candidatesGet**](CandidateApi.md#candidatesGet) | **GET** /candidates/ | 
[**candidatesSearchGet**](CandidateApi.md#candidatesSearchGet) | **GET** /candidates/search/ | 
[**candidatesTotalsAggregatesGet**](CandidateApi.md#candidatesTotalsAggregatesGet) | **GET** /candidates/totals/aggregates/ | 
[**candidatesTotalsByOfficeByPartyGet**](CandidateApi.md#candidatesTotalsByOfficeByPartyGet) | **GET** /candidates/totals/by_office/by_party/ | 
[**candidatesTotalsByOfficeGet**](CandidateApi.md#candidatesTotalsByOfficeGet) | **GET** /candidates/totals/by_office/ | 
[**candidatesTotalsGet**](CandidateApi.md#candidatesTotalsGet) | **GET** /candidates/totals/ | 
[**committeeCommitteeIdCandidatesGet**](CandidateApi.md#committeeCommitteeIdCandidatesGet) | **GET** /committee/{committee_id}/candidates/ | 
[**committeeCommitteeIdCandidatesHistoryCycleGet**](CandidateApi.md#committeeCommitteeIdCandidatesHistoryCycleGet) | **GET** /committee/{committee_id}/candidates/history/{cycle}/ | 
[**committeeCommitteeIdCandidatesHistoryGet**](CandidateApi.md#committeeCommitteeIdCandidatesHistoryGet) | **GET** /committee/{committee_id}/candidates/history/ | 



## candidateCandidateIdGet

> CandidateDetailPage candidateCandidateIdGet(apiKey, candidateId, opts)



 This endpoint is useful for finding detailed information about a particular candidate. Use the &#x60;candidate_id&#x60; to find the most recent information about that candidate. 

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

let apiInstance = new OpenFec.CandidateApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let candidateId = "candidateId_example"; // String |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
let opts = {
  'incumbentChallenge': ["null"], // [String] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open.
  'cycle': [null], // [Number] |  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'federalFundsFlag': true, // Boolean | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates.
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'name': ["null"], // [String] | Name (candidate or committee) to search for. Alias for 'q'.
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'electionYear': [null], // [Number] | Year of election
  'office': ["null"], // [String] | Federal office candidate runs for: H, S or P
  'sort': "'name'", // String | Provide a field to sort by. Use `-` for descending order. 
  'candidateStatus': ["null"], // [String] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate 
  'district': ["null"], // [String] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
  'hasRaisedFunds': true, // Boolean | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.)
  'party': ["null"], // [String] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'state': ["null"], // [String] | US state or territory where a candidate runs for office
  'year': "year_example" // String | Retrieve records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year.
};
apiInstance.candidateCandidateIdGet(apiKey, candidateId, opts, (error, data, response) => {
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
 **candidateId** | **String**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | 
 **incumbentChallenge** | [**[String]**](String.md)| One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional] 
 **cycle** | [**[Number]**](Number.md)|  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **federalFundsFlag** | **Boolean**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **name** | [**[String]**](String.md)| Name (candidate or committee) to search for. Alias for &#39;q&#39;. | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **electionYear** | [**[Number]**](Number.md)| Year of election | [optional] 
 **office** | [**[String]**](String.md)| Federal office candidate runs for: H, S or P | [optional] 
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;name&#39;]
 **candidateStatus** | [**[String]**](String.md)| One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional] 
 **district** | [**[String]**](String.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **hasRaisedFunds** | **Boolean**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional] 
 **party** | [**[String]**](String.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **state** | [**[String]**](String.md)| US state or territory where a candidate runs for office | [optional] 
 **year** | **String**| Retrieve records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. | [optional] 

### Return type

[**CandidateDetailPage**](CandidateDetailPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## candidateCandidateIdHistoryCycleGet

> CandidateHistoryPage candidateCandidateIdHistoryCycleGet(apiKey, cycle, candidateId, opts)



 Find out a candidate&#39;s characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate&#39;s previous races.  This information is organized by &#x60;candidate_id&#x60;, so it won&#39;t help you find a candidate who ran for different offices over time; candidates get a new ID for each office. 

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

let apiInstance = new OpenFec.CandidateApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let cycle = 56; // Number |  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag. 
let candidateId = "candidateId_example"; // String |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
let opts = {
  'page': 1, // Number | For paginating through results, starting at page 1
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'electionFull': true, // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'sort': "'-two_year_period'", // String | Provide a field to sort by. Use `-` for descending order. 
  'sortNullsLast': false // Boolean | Toggle that sorts null values last
};
apiInstance.candidateCandidateIdHistoryCycleGet(apiKey, cycle, candidateId, opts, (error, data, response) => {
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
 **cycle** | **Number**|  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | 
 **candidateId** | **String**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | 
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-two_year_period&#39;]
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]

### Return type

[**CandidateHistoryPage**](CandidateHistoryPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## candidateCandidateIdHistoryGet

> CandidateHistoryPage candidateCandidateIdHistoryGet(apiKey, candidateId, opts)



 Find out a candidate&#39;s characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate&#39;s previous races.  This information is organized by &#x60;candidate_id&#x60;, so it won&#39;t help you find a candidate who ran for different offices over time; candidates get a new ID for each office. 

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

let apiInstance = new OpenFec.CandidateApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let candidateId = "candidateId_example"; // String |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
let opts = {
  'page': 1, // Number | For paginating through results, starting at page 1
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'electionFull': true, // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'sort': "'-two_year_period'", // String | Provide a field to sort by. Use `-` for descending order. 
  'sortNullsLast': false // Boolean | Toggle that sorts null values last
};
apiInstance.candidateCandidateIdHistoryGet(apiKey, candidateId, opts, (error, data, response) => {
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
 **candidateId** | **String**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | 
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-two_year_period&#39;]
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]

### Return type

[**CandidateHistoryPage**](CandidateHistoryPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## candidateCandidateIdTotalsGet

> CommitteeTotalsPage candidateCandidateIdTotalsGet(apiKey, candidateId, opts)



 This endpoint provides information about a committee&#39;s Form 3, Form 3X, or Form 3P financial reports, which are aggregated by two-year period. We refer to two-year periods as a &#x60;cycle&#x60;.  The cycle is named after the even-numbered year and includes the year before it. To obtain totals from 2013 and 2014, you would use 2014. In odd-numbered years, the current cycle is the next year — for example, in 2015, the current cycle is 2016.  For presidential and Senate candidates, multiple two-year cycles exist between elections.  

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

let apiInstance = new OpenFec.CandidateApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let candidateId = "candidateId_example"; // String |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
let opts = {
  'electionFull': true, // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
  'cycle': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': "'-cycle'" // String | Provide a field to sort by. Use `-` for descending order. 
};
apiInstance.candidateCandidateIdTotalsGet(apiKey, candidateId, opts, (error, data, response) => {
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
 **candidateId** | **String**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | 
 **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] 
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-cycle&#39;]

### Return type

[**CommitteeTotalsPage**](CommitteeTotalsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## candidatesGet

> CandidatePage candidatesGet(apiKey, opts)



 Fetch basic information about candidates, and use parameters to filter results to the candidates you&#39;re looking for.  Each result reflects a unique FEC candidate ID. That ID is particular to the candidate for a particular office sought. If a candidate runs for the same office multiple times, the ID stays the same. If the same person runs for another office — for example, a House candidate runs for a Senate office — that candidate will get a unique ID for each office. 

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

let apiInstance = new OpenFec.CandidateApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'incumbentChallenge': ["null"], // [String] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open.
  'minFirstFileDate': new Date("2013-10-20"), // Date | Selects all candidates whose first filing was received by the FEC after this date.
  'q': ["null"], // [String] | Name of candidate running for office
  'cycle': [null], // [Number] |  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'federalFundsFlag': true, // Boolean | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates.
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'candidateId': ["null"], // [String] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
  'name': ["null"], // [String] | Name (candidate or committee) to search for. Alias for 'q'.
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'electionYear': [null], // [Number] | Year of election
  'office': ["null"], // [String] | Federal office candidate runs for: H, S or P
  'sort': "'name'", // String | Provide a field to sort by. Use `-` for descending order. 
  'candidateStatus': ["null"], // [String] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate 
  'maxFirstFileDate': new Date("2013-10-20"), // Date | Selects all candidates whose first filing was received by the FEC before this date.
  'district': ["null"], // [String] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
  'hasRaisedFunds': true, // Boolean | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.)
  'party': ["null"], // [String] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'isActiveCandidate': true, // Boolean |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned. 
  'page': 1, // Number | For paginating through results, starting at page 1
  'state': ["null"], // [String] | US state or territory where a candidate runs for office
  'year': "year_example" // String | Retrieve records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year.
};
apiInstance.candidatesGet(apiKey, opts, (error, data, response) => {
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
 **incumbentChallenge** | [**[String]**](String.md)| One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional] 
 **minFirstFileDate** | **Date**| Selects all candidates whose first filing was received by the FEC after this date. | [optional] 
 **q** | [**[String]**](String.md)| Name of candidate running for office | [optional] 
 **cycle** | [**[Number]**](Number.md)|  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **federalFundsFlag** | **Boolean**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **candidateId** | [**[String]**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
 **name** | [**[String]**](String.md)| Name (candidate or committee) to search for. Alias for &#39;q&#39;. | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **electionYear** | [**[Number]**](Number.md)| Year of election | [optional] 
 **office** | [**[String]**](String.md)| Federal office candidate runs for: H, S or P | [optional] 
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;name&#39;]
 **candidateStatus** | [**[String]**](String.md)| One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional] 
 **maxFirstFileDate** | **Date**| Selects all candidates whose first filing was received by the FEC before this date. | [optional] 
 **district** | [**[String]**](String.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **hasRaisedFunds** | **Boolean**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional] 
 **party** | [**[String]**](String.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **isActiveCandidate** | **Boolean**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional] 
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **state** | [**[String]**](String.md)| US state or territory where a candidate runs for office | [optional] 
 **year** | **String**| Retrieve records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. | [optional] 

### Return type

[**CandidatePage**](CandidatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## candidatesSearchGet

> CandidatePage candidatesSearchGet(apiKey, opts)



 Fetch basic information about candidates and their principal committees.  Each result reflects a unique FEC candidate ID. That ID is assigned to the candidate for a particular office sought. If a candidate runs for the same office over time, that ID stays the same. If the same person runs for multiple offices — for example, a House candidate runs for a Senate office — that candidate will get a unique ID for each office.  The candidate endpoints primarily use data from FEC registration [Form 1](https://www.fec.gov/pdf/forms/fecfrm1.pdf) for committee information and [Form 2](https://www.fec.gov/pdf/forms/fecfrm2.pdf) for candidate information. 

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

let apiInstance = new OpenFec.CandidateApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'incumbentChallenge': ["null"], // [String] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open.
  'minFirstFileDate': new Date("2013-10-20"), // Date | Selects all candidates whose first filing was received by the FEC after this date.
  'q': ["null"], // [String] | Name of candidate running for office
  'cycle': [null], // [Number] |  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'federalFundsFlag': true, // Boolean | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates.
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'candidateId': ["null"], // [String] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
  'name': ["null"], // [String] | Name (candidate or committee) to search for. Alias for 'q'.
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'electionYear': [null], // [Number] | Year of election
  'office': ["null"], // [String] | Federal office candidate runs for: H, S or P
  'sort': "'name'", // String | Provide a field to sort by. Use `-` for descending order. 
  'candidateStatus': ["null"], // [String] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate 
  'maxFirstFileDate': new Date("2013-10-20"), // Date | Selects all candidates whose first filing was received by the FEC before this date.
  'district': ["null"], // [String] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
  'hasRaisedFunds': true, // Boolean | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.)
  'party': ["null"], // [String] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'isActiveCandidate': true, // Boolean |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned. 
  'page': 1, // Number | For paginating through results, starting at page 1
  'state': ["null"], // [String] | US state or territory where a candidate runs for office
  'year': "year_example" // String | Retrieve records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year.
};
apiInstance.candidatesSearchGet(apiKey, opts, (error, data, response) => {
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
 **incumbentChallenge** | [**[String]**](String.md)| One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional] 
 **minFirstFileDate** | **Date**| Selects all candidates whose first filing was received by the FEC after this date. | [optional] 
 **q** | [**[String]**](String.md)| Name of candidate running for office | [optional] 
 **cycle** | [**[Number]**](Number.md)|  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **federalFundsFlag** | **Boolean**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **candidateId** | [**[String]**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
 **name** | [**[String]**](String.md)| Name (candidate or committee) to search for. Alias for &#39;q&#39;. | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **electionYear** | [**[Number]**](Number.md)| Year of election | [optional] 
 **office** | [**[String]**](String.md)| Federal office candidate runs for: H, S or P | [optional] 
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;name&#39;]
 **candidateStatus** | [**[String]**](String.md)| One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional] 
 **maxFirstFileDate** | **Date**| Selects all candidates whose first filing was received by the FEC before this date. | [optional] 
 **district** | [**[String]**](String.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **hasRaisedFunds** | **Boolean**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional] 
 **party** | [**[String]**](String.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **isActiveCandidate** | **Boolean**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional] 
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **state** | [**[String]**](String.md)| US state or territory where a candidate runs for office | [optional] 
 **year** | **String**| Retrieve records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. | [optional] 

### Return type

[**CandidatePage**](CandidatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## candidatesTotalsAggregatesGet

> CandidateTotalAggregatePage candidatesTotalsAggregatesGet(apiKey, opts)



 Candidate total receipts and disbursements aggregated by &#x60;aggregate_by&#x60;. 

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

let apiInstance = new OpenFec.CandidateApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'maxElectionCycle': 56, // Number |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'electionYear': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'office': "office_example", // String | Federal office candidate runs for: H, S or P
  'sort': ["null"], // [String] |  Provide a field to sort by. Use `-` for descending order. ex: `-case_no` 
  'minElectionCycle': 56, // Number |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year. 
  'district': ["null"], // [String] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
  'electionFull': true, // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
  'party': "party_example", // String | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
  'isActiveCandidate': true, // Boolean |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned. 
  'page': 1, // Number | For paginating through results, starting at page 1
  'state': ["null"], // [String] | US state or territory where a candidate runs for office
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'aggregateBy': "aggregateBy_example" // String | Candidate totals aggregate_by (Chose one of dropdown options):         - ' ' grouped by election year         - office grouped by election year, by office         - office-state grouped by election year, by office, by state         - office-state-district grouped by election year, by office, by state, by district         - office-party grouped by election year, by office, by party 
};
apiInstance.candidatesTotalsAggregatesGet(apiKey, opts, (error, data, response) => {
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
 **maxElectionCycle** | **Number**|  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **electionYear** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **office** | **String**| Federal office candidate runs for: H, S or P | [optional] 
 **sort** | [**[String]**](String.md)|  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60;  | [optional] 
 **minElectionCycle** | **Number**|  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **district** | [**[String]**](String.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **party** | **String**| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
 **isActiveCandidate** | **Boolean**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional] 
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **state** | [**[String]**](String.md)| US state or territory where a candidate runs for office | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **aggregateBy** | **String**| Candidate totals aggregate_by (Chose one of dropdown options):         - &#39; &#39; grouped by election year         - office grouped by election year, by office         - office-state grouped by election year, by office, by state         - office-state-district grouped by election year, by office, by state, by district         - office-party grouped by election year, by office, by party  | [optional] 

### Return type

[**CandidateTotalAggregatePage**](CandidateTotalAggregatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## candidatesTotalsByOfficeByPartyGet

> TotalByOfficeByPartyPage candidatesTotalsByOfficeByPartyGet(apiKey, opts)



 Aggregated candidate receipts and disbursements grouped by office by party by cycle. 

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

let apiInstance = new OpenFec.CandidateApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'electionFull': true, // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'page': 1, // Number | For paginating through results, starting at page 1
  'isActiveCandidate': true, // Boolean |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned. 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'electionYear': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'office': "office_example", // String | Federal office candidate runs for: H, S or P
  'sort': "sort_example" // String | Provide a field to sort by. Use `-` for descending order. 
};
apiInstance.candidatesTotalsByOfficeByPartyGet(apiKey, opts, (error, data, response) => {
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
 **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **isActiveCandidate** | **Boolean**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **electionYear** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **office** | **String**| Federal office candidate runs for: H, S or P | [optional] 
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 

### Return type

[**TotalByOfficeByPartyPage**](TotalByOfficeByPartyPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## candidatesTotalsByOfficeGet

> TotalByOfficePage candidatesTotalsByOfficeGet(apiKey, opts)



 Aggregated candidate receipts and disbursements grouped by office by cycle. 

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

let apiInstance = new OpenFec.CandidateApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'maxElectionCycle': 56, // Number |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year. 
  'electionFull': true, // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
  'isActiveCandidate': true, // Boolean |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned. 
  'page': 1, // Number | For paginating through results, starting at page 1
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'electionYear': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'office': "office_example", // String | Federal office candidate runs for: H, S or P
  'sort': "sort_example", // String | Provide a field to sort by. Use `-` for descending order. 
  'minElectionCycle': 56 // Number |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year. 
};
apiInstance.candidatesTotalsByOfficeGet(apiKey, opts, (error, data, response) => {
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
 **maxElectionCycle** | **Number**|  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **isActiveCandidate** | **Boolean**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional] 
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **electionYear** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **office** | **String**| Federal office candidate runs for: H, S or P | [optional] 
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 
 **minElectionCycle** | **Number**|  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | [optional] 

### Return type

[**TotalByOfficePage**](TotalByOfficePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## candidatesTotalsGet

> CandidateHistoryTotalPage candidatesTotalsGet(apiKey, opts)



 Aggregated candidate receipts and disbursements grouped by cycle. 

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

let apiInstance = new OpenFec.CandidateApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'maxDisbursements': "maxDisbursements_example", // String | Maximum aggregated disbursements
  'q': ["null"], // [String] | Name of candidate running for office
  'cycle': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'maxCashOnHandEndPeriod': "maxCashOnHandEndPeriod_example", // String | Maximum cash on hand
  'maxDebtsOwedByCommittee': "maxDebtsOwedByCommittee_example", // String | Maximum debt
  'minDisbursements': "minDisbursements_example", // String | Minimum aggregated disbursements
  'federalFundsFlag': true, // Boolean | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates.
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'candidateId': ["null"], // [String] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'electionYear': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'office': ["null"], // [String] | Federal office candidate runs for: H, S or P
  'sort': "sort_example", // String | Provide a field to sort by. Use `-` for descending order. 
  'district': ["null"], // [String] | District of candidate
  'electionFull': true, // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
  'minDebtsOwedByCommittee': "minDebtsOwedByCommittee_example", // String | Minimum debt
  'maxReceipts': "maxReceipts_example", // String | Maximum aggregated receipts
  'hasRaisedFunds': true, // Boolean | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.)
  'party': ["null"], // [String] | Three-letter party code
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'isActiveCandidate': true, // Boolean |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned. 
  'page': 1, // Number | For paginating through results, starting at page 1
  'state': ["null"], // [String] | State of candidate
  'minCashOnHandEndPeriod': "minCashOnHandEndPeriod_example", // String | Minimum cash on hand
  'minReceipts': "minReceipts_example" // String | Minimum aggregated receipts
};
apiInstance.candidatesTotalsGet(apiKey, opts, (error, data, response) => {
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
 **maxDisbursements** | **String**| Maximum aggregated disbursements | [optional] 
 **q** | [**[String]**](String.md)| Name of candidate running for office | [optional] 
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **maxCashOnHandEndPeriod** | **String**| Maximum cash on hand | [optional] 
 **maxDebtsOwedByCommittee** | **String**| Maximum debt | [optional] 
 **minDisbursements** | **String**| Minimum aggregated disbursements | [optional] 
 **federalFundsFlag** | **Boolean**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **candidateId** | [**[String]**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **electionYear** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **office** | [**[String]**](String.md)| Federal office candidate runs for: H, S or P | [optional] 
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 
 **district** | [**[String]**](String.md)| District of candidate | [optional] 
 **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **minDebtsOwedByCommittee** | **String**| Minimum debt | [optional] 
 **maxReceipts** | **String**| Maximum aggregated receipts | [optional] 
 **hasRaisedFunds** | **Boolean**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional] 
 **party** | [**[String]**](String.md)| Three-letter party code | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **isActiveCandidate** | **Boolean**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional] 
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **state** | [**[String]**](String.md)| State of candidate | [optional] 
 **minCashOnHandEndPeriod** | **String**| Minimum cash on hand | [optional] 
 **minReceipts** | **String**| Minimum aggregated receipts | [optional] 

### Return type

[**CandidateHistoryTotalPage**](CandidateHistoryTotalPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## committeeCommitteeIdCandidatesGet

> CandidateDetailPage committeeCommitteeIdCandidatesGet(apiKey, committeeId, opts)



 This endpoint is useful for finding detailed information about a particular candidate. Use the &#x60;candidate_id&#x60; to find the most recent information about that candidate. 

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

let apiInstance = new OpenFec.CandidateApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let committeeId = "committeeId_example"; // String |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
let opts = {
  'incumbentChallenge': ["null"], // [String] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open.
  'cycle': [null], // [Number] |  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'federalFundsFlag': true, // Boolean | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates.
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'name': ["null"], // [String] | Name (candidate or committee) to search for. Alias for 'q'.
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'electionYear': [null], // [Number] | Year of election
  'office': ["null"], // [String] | Federal office candidate runs for: H, S or P
  'sort': "'name'", // String | Provide a field to sort by. Use `-` for descending order. 
  'candidateStatus': ["null"], // [String] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate 
  'district': ["null"], // [String] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
  'hasRaisedFunds': true, // Boolean | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.)
  'party': ["null"], // [String] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'state': ["null"], // [String] | US state or territory where a candidate runs for office
  'year': "year_example" // String | Retrieve records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year.
};
apiInstance.committeeCommitteeIdCandidatesGet(apiKey, committeeId, opts, (error, data, response) => {
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
 **committeeId** | **String**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | 
 **incumbentChallenge** | [**[String]**](String.md)| One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional] 
 **cycle** | [**[Number]**](Number.md)|  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **federalFundsFlag** | **Boolean**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **name** | [**[String]**](String.md)| Name (candidate or committee) to search for. Alias for &#39;q&#39;. | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **electionYear** | [**[Number]**](Number.md)| Year of election | [optional] 
 **office** | [**[String]**](String.md)| Federal office candidate runs for: H, S or P | [optional] 
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;name&#39;]
 **candidateStatus** | [**[String]**](String.md)| One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional] 
 **district** | [**[String]**](String.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **hasRaisedFunds** | **Boolean**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional] 
 **party** | [**[String]**](String.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **state** | [**[String]**](String.md)| US state or territory where a candidate runs for office | [optional] 
 **year** | **String**| Retrieve records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. | [optional] 

### Return type

[**CandidateDetailPage**](CandidateDetailPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## committeeCommitteeIdCandidatesHistoryCycleGet

> CandidateHistoryPage committeeCommitteeIdCandidatesHistoryCycleGet(apiKey, committeeId, cycle, opts)



 Find out a candidate&#39;s characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate&#39;s previous races.  This information is organized by &#x60;candidate_id&#x60;, so it won&#39;t help you find a candidate who ran for different offices over time; candidates get a new ID for each office. 

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

let apiInstance = new OpenFec.CandidateApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let committeeId = "committeeId_example"; // String |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
let cycle = 56; // Number |  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag. 
let opts = {
  'page': 1, // Number | For paginating through results, starting at page 1
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'electionFull': true, // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'sort': "'-two_year_period'", // String | Provide a field to sort by. Use `-` for descending order. 
  'sortNullsLast': false // Boolean | Toggle that sorts null values last
};
apiInstance.committeeCommitteeIdCandidatesHistoryCycleGet(apiKey, committeeId, cycle, opts, (error, data, response) => {
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
 **committeeId** | **String**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | 
 **cycle** | **Number**|  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | 
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-two_year_period&#39;]
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]

### Return type

[**CandidateHistoryPage**](CandidateHistoryPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## committeeCommitteeIdCandidatesHistoryGet

> CandidateHistoryPage committeeCommitteeIdCandidatesHistoryGet(apiKey, committeeId, opts)



 Find out a candidate&#39;s characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate&#39;s previous races.  This information is organized by &#x60;candidate_id&#x60;, so it won&#39;t help you find a candidate who ran for different offices over time; candidates get a new ID for each office. 

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

let apiInstance = new OpenFec.CandidateApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let committeeId = "committeeId_example"; // String |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
let opts = {
  'page': 1, // Number | For paginating through results, starting at page 1
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'electionFull': true, // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'sort': "'-two_year_period'", // String | Provide a field to sort by. Use `-` for descending order. 
  'sortNullsLast': false // Boolean | Toggle that sorts null values last
};
apiInstance.committeeCommitteeIdCandidatesHistoryGet(apiKey, committeeId, opts, (error, data, response) => {
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
 **committeeId** | **String**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | 
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-two_year_period&#39;]
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]

### Return type

[**CandidateHistoryPage**](CandidateHistoryPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

