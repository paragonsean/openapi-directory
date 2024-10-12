# OpenFec.FinancialApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**committeeCommitteeIdReportsGet**](FinancialApi.md#committeeCommitteeIdReportsGet) | **GET** /committee/{committee_id}/reports/ | 
[**committeeCommitteeIdTotalsGet**](FinancialApi.md#committeeCommitteeIdTotalsGet) | **GET** /committee/{committee_id}/totals/ | 
[**electionsGet**](FinancialApi.md#electionsGet) | **GET** /elections/ | 
[**electionsSearchGet**](FinancialApi.md#electionsSearchGet) | **GET** /elections/search/ | 
[**electionsSummaryGet**](FinancialApi.md#electionsSummaryGet) | **GET** /elections/summary/ | 
[**reportsEntityTypeGet**](FinancialApi.md#reportsEntityTypeGet) | **GET** /reports/{entity_type}/ | 
[**totalsByEntityGet**](FinancialApi.md#totalsByEntityGet) | **GET** /totals/by_entity/ | 
[**totalsEntityTypeGet**](FinancialApi.md#totalsEntityTypeGet) | **GET** /totals/{entity_type}/ | 
[**totalsInauguralCommitteesByContributorGet**](FinancialApi.md#totalsInauguralCommitteesByContributorGet) | **GET** /totals/inaugural_committees/by_contributor/ | 



## committeeCommitteeIdReportsGet

> CommitteeReportsPage committeeCommitteeIdReportsGet(apiKey, committeeId, opts)



 Each report represents the summary information from Form 3, Form 3X and Form 3P. These reports have key statistics that illuminate the financial status of a given committee. Things like cash on hand, debts owed by committee, total receipts, and total disbursements are especially helpful for understanding a committee&#39;s financial dealings.  By default, this endpoint includes both amended and final versions of each report. To restrict to only the final versions of each report, use &#x60;is_amended&#x3D;false&#x60;; to retrieve only reports that have been amended, use &#x60;is_amended&#x3D;true&#x60;.  Several different reporting structures exist, depending on the type of organization that submits financial information. To see an example of these reporting requirements, look at the summary and detailed summary pages of Form 3, Form 3X, and Form 3P.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users. 

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

let apiInstance = new OpenFec.FinancialApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let committeeId = "committeeId_example"; // String |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
let opts = {
  'minPartyCoordinatedExpenditures': "minPartyCoordinatedExpenditures_example", // String |  Filter for all amounts greater than a value. 
  'isAmended': true, // Boolean |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment. 
  'maxPartyCoordinatedExpenditures': "maxPartyCoordinatedExpenditures_example", // String |  Filter for all amounts less than a value. 
  'maxCashOnHandEndPeriodAmount': "maxCashOnHandEndPeriodAmount_example", // String |  Filter for all amounts less than a value. 
  'maxDisbursementsAmount': "maxDisbursementsAmount_example", // String |  Filter for all amounts less than a value. 
  'maxDebtsOwedExpenditures': "maxDebtsOwedExpenditures_example", // String |  Filter for all amounts less than a value. 
  'minReceiptsAmount': "minReceiptsAmount_example", // String |  Filter for all amounts greater than a value. 
  'cycle': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'minDebtsOwedAmount': "minDebtsOwedAmount_example", // String |  Filter for all amounts greater than a value. 
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'candidateId': "candidateId_example", // String |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
  'minIndependentExpenditures': "minIndependentExpenditures_example", // String |  Filter for all amounts greater than a value. 
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': ["null"], // [String] |  Provide a field to sort by. Use `-` for descending order. ex: `-case_no` 
  'maxReceiptsAmount': "maxReceiptsAmount_example", // String |  Filter for all amounts less than a value. 
  'reportType': ["null"], // [String] | Report type; prefix with \"-\" to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND 
  'maxTotalContributions': "maxTotalContributions_example", // String |  Filter for all amounts less than a value. 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'year': [null], // [Number] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date. 
  'maxIndependentExpenditures': "maxIndependentExpenditures_example", // String |  Filter for all amounts less than a value. 
  'type': ["null"], // [String] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
  'minCashOnHandEndPeriodAmount': "minCashOnHandEndPeriodAmount_example", // String |  Filter for all amounts greater than a value. 
  'minDisbursementsAmount': "minDisbursementsAmount_example", // String |  Filter for all amounts greater than a value. 
  'minTotalContributions': "minTotalContributions_example", // String |  Filter for all amounts greater than a value. 
  'beginningImageNumber': ["null"] // [String] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document. 
};
apiInstance.committeeCommitteeIdReportsGet(apiKey, committeeId, opts, (error, data, response) => {
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
 **minPartyCoordinatedExpenditures** | **String**|  Filter for all amounts greater than a value.  | [optional] 
 **isAmended** | **Boolean**|  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  | [optional] 
 **maxPartyCoordinatedExpenditures** | **String**|  Filter for all amounts less than a value.  | [optional] 
 **maxCashOnHandEndPeriodAmount** | **String**|  Filter for all amounts less than a value.  | [optional] 
 **maxDisbursementsAmount** | **String**|  Filter for all amounts less than a value.  | [optional] 
 **maxDebtsOwedExpenditures** | **String**|  Filter for all amounts less than a value.  | [optional] 
 **minReceiptsAmount** | **String**|  Filter for all amounts greater than a value.  | [optional] 
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **minDebtsOwedAmount** | **String**|  Filter for all amounts greater than a value.  | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **candidateId** | **String**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
 **minIndependentExpenditures** | **String**|  Filter for all amounts greater than a value.  | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | [**[String]**](String.md)|  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60;  | [optional] 
 **maxReceiptsAmount** | **String**|  Filter for all amounts less than a value.  | [optional] 
 **reportType** | [**[String]**](String.md)| Report type; prefix with \&quot;-\&quot; to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  | [optional] 
 **maxTotalContributions** | **String**|  Filter for all amounts less than a value.  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **year** | [**[Number]**](Number.md)|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] 
 **maxIndependentExpenditures** | **String**|  Filter for all amounts less than a value.  | [optional] 
 **type** | [**[String]**](String.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **minCashOnHandEndPeriodAmount** | **String**|  Filter for all amounts greater than a value.  | [optional] 
 **minDisbursementsAmount** | **String**|  Filter for all amounts greater than a value.  | [optional] 
 **minTotalContributions** | **String**|  Filter for all amounts greater than a value.  | [optional] 
 **beginningImageNumber** | [**[String]**](String.md)|  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  | [optional] 

### Return type

[**CommitteeReportsPage**](CommitteeReportsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## committeeCommitteeIdTotalsGet

> CommitteeTotalsPage committeeCommitteeIdTotalsGet(apiKey, committeeId, opts)



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

let apiInstance = new OpenFec.FinancialApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let committeeId = "committeeId_example"; // String |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
let opts = {
  'page': 1, // Number | For paginating through results, starting at page 1
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'sort': "'-cycle'", // String | Provide a field to sort by. Use `-` for descending order. 
  'cycle': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullOnly': false // Boolean | Toggle that filters out all rows having sort column that is non-null
};
apiInstance.committeeCommitteeIdTotalsGet(apiKey, committeeId, opts, (error, data, response) => {
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
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-cycle&#39;]
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]

### Return type

[**CommitteeTotalsPage**](CommitteeTotalsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## electionsGet

> ElectionPage electionsGet(apiKey, cycle, office, opts)



 Look at the top-level financial information for all candidates running for the same office.  Choose a 2-year cycle, and &#x60;house&#x60;, &#x60;senate&#x60; or &#x60;presidential&#x60;.  If you are looking for a Senate seat, you will need to select the state using a two-letter abbreviation.  House races require state and a two-digit district number.  Since this endpoint reflects financial information, it will only have candidates once they file financial reporting forms. Query the &#x60;/candidates&#x60; endpoint to retrieve an-up-to-date list of all the candidates that filed to run for a particular seat. 

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

let apiInstance = new OpenFec.FinancialApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let cycle = 56; // Number |  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag. 
let office = "office_example"; // String | Federal office candidate runs for: H, S or P
let opts = {
  'district': "district_example", // String | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
  'electionFull': true, // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'page': 1, // Number | For paginating through results, starting at page 1
  'state': "state_example", // String | US state or territory where a candidate runs for office
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': "'-total_receipts'" // String | Provide a field to sort by. Use `-` for descending order. 
};
apiInstance.electionsGet(apiKey, cycle, office, opts, (error, data, response) => {
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
 **office** | **String**| Federal office candidate runs for: H, S or P | 
 **district** | **String**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **state** | **String**| US state or territory where a candidate runs for office | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-total_receipts&#39;]

### Return type

[**ElectionPage**](ElectionPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## electionsSearchGet

> ElectionsListPage electionsSearchGet(apiKey, opts)



 List elections by cycle, office, state, and district. 

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

let apiInstance = new OpenFec.FinancialApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'zip': [null], // [Number] | Zip code
  'district': ["null"], // [String] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
  'cycle': [null], // [Number] |  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'state': ["null"], // [String] | US state or territory where a candidate runs for office
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'office': ["null"], // [String] | 
  'sort': ["null"] // [String] |  Provide a field to sort by. Use `-` for descending order. ex: `-case_no` 
};
apiInstance.electionsSearchGet(apiKey, opts, (error, data, response) => {
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
 **zip** | [**[Number]**](Number.md)| Zip code | [optional] 
 **district** | [**[String]**](String.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **cycle** | [**[Number]**](Number.md)|  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **state** | [**[String]**](String.md)| US state or territory where a candidate runs for office | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **office** | [**[String]**](String.md)|  | [optional] 
 **sort** | [**[String]**](String.md)|  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60;  | [optional] 

### Return type

[**ElectionsListPage**](ElectionsListPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## electionsSummaryGet

> ElectionSummary electionsSummaryGet(apiKey, office, cycle, opts)



 List elections by cycle, office, state, and district. 

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

let apiInstance = new OpenFec.FinancialApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let office = "office_example"; // String | Federal office candidate runs for: H, S or P
let cycle = 56; // Number |  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag. 
let opts = {
  'state': "state_example", // String | US state or territory where a candidate runs for office
  'district': "district_example", // String | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
  'electionFull': true // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
};
apiInstance.electionsSummaryGet(apiKey, office, cycle, opts, (error, data, response) => {
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
 **office** | **String**| Federal office candidate runs for: H, S or P | 
 **cycle** | **Number**|  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | 
 **state** | **String**| US state or territory where a candidate runs for office | [optional] 
 **district** | **String**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]

### Return type

[**ElectionSummary**](ElectionSummary.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsEntityTypeGet

> CommitteeReportsPage reportsEntityTypeGet(apiKey, entityType, opts)



 Each report represents the summary information from Form 3, Form 3X and Form 3P. These reports have key statistics that illuminate the financial status of a given committee. Things like cash on hand, debts owed by committee, total receipts, and total disbursements are especially helpful for understanding a committee&#39;s financial dealings.  By default, this endpoint includes both amended and final versions of each report. To restrict to only the final versions of each report, use &#x60;is_amended&#x3D;false&#x60;; to retrieve only reports that have been amended, use &#x60;is_amended&#x3D;true&#x60;.  Several different reporting structures exist, depending on the type of organization that submits financial information. To see an example of these reporting requirements, look at the summary and detailed summary pages of Form 3, Form 3X, and Form 3P.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users. 

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

let apiInstance = new OpenFec.FinancialApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let entityType = "entityType_example"; // String | Committee groupings based on FEC filing form.                 Choose one of: `presidential`, `pac-party`, `house-senate`, or `ie-only`
let opts = {
  'maxPartyCoordinatedExpenditures': "maxPartyCoordinatedExpenditures_example", // String |  Filter for all amounts less than a value. 
  'maxDebtsOwedExpenditures': "maxDebtsOwedExpenditures_example", // String |  Filter for all amounts less than a value. 
  'minReceiptsAmount': "minReceiptsAmount_example", // String |  Filter for all amounts greater than a value. 
  'minDebtsOwedAmount': "minDebtsOwedAmount_example", // String |  Filter for all amounts greater than a value. 
  'maxReceiptDate': new Date("2013-10-20"), // Date |  Selects all items received by FEC before this date(MM/DD/YYYY or YYYY-MM-DD) 
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'candidateId': "candidateId_example", // String |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
  'sort': ["null"], // [String] |  Provide a field to sort by. Use `-` for descending order. ex: `-case_no` 
  'qSpender': ["null"], // [String] |  Keyword search for spender name or ID 
  'maxReceiptsAmount': "maxReceiptsAmount_example", // String |  Filter for all amounts less than a value. 
  'filerType': "filerType_example", // String | The method used to file with the FEC, either electronic or on paper.
  'reportType': ["null"], // [String] | Report type; prefix with \"-\" to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND 
  'maxTotalContributions': "maxTotalContributions_example", // String |  Filter for all amounts less than a value. 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'maxIndependentExpenditures': "maxIndependentExpenditures_example", // String |  Filter for all amounts less than a value. 
  'minTotalContributions': "minTotalContributions_example", // String |  Filter for all amounts greater than a value. 
  'minPartyCoordinatedExpenditures': "minPartyCoordinatedExpenditures_example", // String |  Filter for all amounts greater than a value. 
  'beginningImageNumber': ["null"], // [String] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document. 
  'minReceiptDate': new Date("2013-10-20"), // Date |  Selects all items received by FEC after this date(MM/DD/YYYY or YYYY-MM-DD) 
  'isAmended': true, // Boolean |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment. 
  'maxDisbursementsAmount': "maxDisbursementsAmount_example", // String |  Filter for all amounts less than a value. 
  'maxCashOnHandEndPeriodAmount': "maxCashOnHandEndPeriodAmount_example", // String |  Filter for all amounts less than a value. 
  'amendmentIndicator': ["null"], // [String] | Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment. 
  'cycle': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'minIndependentExpenditures': "minIndependentExpenditures_example", // String |  Filter for all amounts greater than a value. 
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'qFiler': ["null"], // [String] |  Keyword search for filer name or ID 
  'committeeType': ["null"], // [String] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
  'page': 1, // Number | For paginating through results, starting at page 1
  'year': [null], // [Number] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date. 
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'minCashOnHandEndPeriodAmount': "minCashOnHandEndPeriodAmount_example", // String |  Filter for all amounts greater than a value. 
  'minDisbursementsAmount': "minDisbursementsAmount_example", // String |  Filter for all amounts greater than a value. 
  'mostRecent': true // Boolean |  Report is either new or is the most-recently filed amendment 
};
apiInstance.reportsEntityTypeGet(apiKey, entityType, opts, (error, data, response) => {
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
 **entityType** | **String**| Committee groupings based on FEC filing form.                 Choose one of: &#x60;presidential&#x60;, &#x60;pac-party&#x60;, &#x60;house-senate&#x60;, or &#x60;ie-only&#x60; | 
 **maxPartyCoordinatedExpenditures** | **String**|  Filter for all amounts less than a value.  | [optional] 
 **maxDebtsOwedExpenditures** | **String**|  Filter for all amounts less than a value.  | [optional] 
 **minReceiptsAmount** | **String**|  Filter for all amounts greater than a value.  | [optional] 
 **minDebtsOwedAmount** | **String**|  Filter for all amounts greater than a value.  | [optional] 
 **maxReceiptDate** | **Date**|  Selects all items received by FEC before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **candidateId** | **String**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
 **sort** | [**[String]**](String.md)|  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60;  | [optional] 
 **qSpender** | [**[String]**](String.md)|  Keyword search for spender name or ID  | [optional] 
 **maxReceiptsAmount** | **String**|  Filter for all amounts less than a value.  | [optional] 
 **filerType** | **String**| The method used to file with the FEC, either electronic or on paper. | [optional] 
 **reportType** | [**[String]**](String.md)| Report type; prefix with \&quot;-\&quot; to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  | [optional] 
 **maxTotalContributions** | **String**|  Filter for all amounts less than a value.  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **maxIndependentExpenditures** | **String**|  Filter for all amounts less than a value.  | [optional] 
 **minTotalContributions** | **String**|  Filter for all amounts greater than a value.  | [optional] 
 **minPartyCoordinatedExpenditures** | **String**|  Filter for all amounts greater than a value.  | [optional] 
 **beginningImageNumber** | [**[String]**](String.md)|  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  | [optional] 
 **minReceiptDate** | **Date**|  Selects all items received by FEC after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **isAmended** | **Boolean**|  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  | [optional] 
 **maxDisbursementsAmount** | **String**|  Filter for all amounts less than a value.  | [optional] 
 **maxCashOnHandEndPeriodAmount** | **String**|  Filter for all amounts less than a value.  | [optional] 
 **amendmentIndicator** | [**[String]**](String.md)| Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  | [optional] 
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **minIndependentExpenditures** | **String**|  Filter for all amounts greater than a value.  | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **qFiler** | [**[String]**](String.md)|  Keyword search for filer name or ID  | [optional] 
 **committeeType** | [**[String]**](String.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **year** | [**[Number]**](Number.md)|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] 
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **minCashOnHandEndPeriodAmount** | **String**|  Filter for all amounts greater than a value.  | [optional] 
 **minDisbursementsAmount** | **String**|  Filter for all amounts greater than a value.  | [optional] 
 **mostRecent** | **Boolean**|  Report is either new or is the most-recently filed amendment  | [optional] 

### Return type

[**CommitteeReportsPage**](CommitteeReportsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## totalsByEntityGet

> EntityReceiptDisbursementTotalsPage totalsByEntityGet(apiKey, cycle, opts)



 Provides cumulative receipt totals by entity type, over a two year cycle. Totals are adjusted to avoid double counting.  This is [the sql](https://github.com/fecgov/openFEC/blob/develop/data/migrations/V41__large_aggregates.sql) that creates these calculations. 

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

let apiInstance = new OpenFec.FinancialApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let cycle = 56; // Number |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
let opts = {
  'page': 1, // Number | For paginating through results, starting at page 1
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'sort': "'end_date'", // String | Provide a field to sort by. Use `-` for descending order. 
  'sortNullsLast': false // Boolean | Toggle that sorts null values last
};
apiInstance.totalsByEntityGet(apiKey, cycle, opts, (error, data, response) => {
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
 **cycle** | **Number**|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | 
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;end_date&#39;]
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]

### Return type

[**EntityReceiptDisbursementTotalsPage**](EntityReceiptDisbursementTotalsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## totalsEntityTypeGet

> CommitteeTotalsPage totalsEntityTypeGet(apiKey, entityType, opts)



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

let apiInstance = new OpenFec.FinancialApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let entityType = "entityType_example"; // String | Committee groupings based on FEC filing form.                 Choose one of: `presidential`, `pac`, `party`, `pac-party`,                 `house-senate`, or `ie-only`
let opts = {
  'treasurerName': ["null"], // [String] | Name of the Committee's treasurer. If multiple treasurers for the committee, the most recent treasurer will be shown.
  'maxDisbursements': "maxDisbursements_example", // String |  Filter for all amounts less than a value. 
  'committeeState': ["null"], // [String] | US state or territory
  'cycle': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'sponsorCandidateId': ["null"], // [String] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. This is a filter for Leadership PAC sponsor. 
  'minDisbursements': "minDisbursements_example", // String |  Filter for all amounts greater than a value. 
  'minLastCashOnHandEndPeriod': "minLastCashOnHandEndPeriod_example", // String |  Filter for all amounts greater than a value. 
  'maxLastCashOnHandEndPeriod': "maxLastCashOnHandEndPeriod_example", // String |  Filter for all amounts less than a value. 
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'filingFrequency': ["null"], // [String] | The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived 
  'sort': "'-cycle'", // String | Provide a field to sort by. Use `-` for descending order. 
  'maxLastDebtsOwedByCommittee': "maxLastDebtsOwedByCommittee_example", // String |  Filter for all amounts less than a value. 
  'minFirstF1Date': new Date("2013-10-20"), // Date | Filter for committees whose first Form 1 was received on or after this date.
  'committeeDesignation': ["null"], // [String] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC 
  'maxReceipts': "maxReceipts_example", // String |  Filter for all amounts less than a value. 
  'committeeType': ["null"], // [String] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'minLastDebtsOwedByCommittee': "minLastDebtsOwedByCommittee_example", // String |  Filter for all amounts greater than a value. 
  'maxFirstF1Date': new Date("2013-10-20"), // Date | Filter for committees whose first Form 1 was received on or before this date.
  'organizationType': ["null"], // [String] | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock 
  'minReceipts': "minReceipts_example" // String |  Filter for all amounts greater than a value. 
};
apiInstance.totalsEntityTypeGet(apiKey, entityType, opts, (error, data, response) => {
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
 **entityType** | **String**| Committee groupings based on FEC filing form.                 Choose one of: &#x60;presidential&#x60;, &#x60;pac&#x60;, &#x60;party&#x60;, &#x60;pac-party&#x60;,                 &#x60;house-senate&#x60;, or &#x60;ie-only&#x60; | 
 **treasurerName** | [**[String]**](String.md)| Name of the Committee&#39;s treasurer. If multiple treasurers for the committee, the most recent treasurer will be shown. | [optional] 
 **maxDisbursements** | **String**|  Filter for all amounts less than a value.  | [optional] 
 **committeeState** | [**[String]**](String.md)| US state or territory | [optional] 
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sponsorCandidateId** | [**[String]**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. This is a filter for Leadership PAC sponsor.  | [optional] 
 **minDisbursements** | **String**|  Filter for all amounts greater than a value.  | [optional] 
 **minLastCashOnHandEndPeriod** | **String**|  Filter for all amounts greater than a value.  | [optional] 
 **maxLastCashOnHandEndPeriod** | **String**|  Filter for all amounts less than a value.  | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **filingFrequency** | [**[String]**](String.md)| The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  | [optional] 
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-cycle&#39;]
 **maxLastDebtsOwedByCommittee** | **String**|  Filter for all amounts less than a value.  | [optional] 
 **minFirstF1Date** | **Date**| Filter for committees whose first Form 1 was received on or after this date. | [optional] 
 **committeeDesignation** | [**[String]**](String.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **maxReceipts** | **String**|  Filter for all amounts less than a value.  | [optional] 
 **committeeType** | [**[String]**](String.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **minLastDebtsOwedByCommittee** | **String**|  Filter for all amounts greater than a value.  | [optional] 
 **maxFirstF1Date** | **Date**| Filter for committees whose first Form 1 was received on or before this date. | [optional] 
 **organizationType** | [**[String]**](String.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
 **minReceipts** | **String**|  Filter for all amounts greater than a value.  | [optional] 

### Return type

[**CommitteeTotalsPage**](CommitteeTotalsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## totalsInauguralCommitteesByContributorGet

> InauguralDonationsPage totalsInauguralCommitteesByContributorGet(apiKey, opts)



 This endpoint provides information about an inaugural committee&#39;s Form 13 report of donations accepted. The data is aggregated by the contributor and the two-year period. We refer to two-year periods as a &#x60;cycle&#x60;.  

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

let apiInstance = new OpenFec.FinancialApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'cycle': [null], // [Number] |  A two year election cycle that the committee was active- (after original registration date but before expiration date in Form 1s) The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'contributorName': ["null"], // [String] | Name of contributor
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': ["null"] // [String] |  Provide a field to sort by. Use `-` for descending order. ex: `-case_no` 
};
apiInstance.totalsInauguralCommitteesByContributorGet(apiKey, opts, (error, data, response) => {
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
 **cycle** | [**[Number]**](Number.md)|  A two year election cycle that the committee was active- (after original registration date but before expiration date in Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **contributorName** | [**[String]**](String.md)| Name of contributor | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | [**[String]**](String.md)|  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60;  | [optional] 

### Return type

[**InauguralDonationsPage**](InauguralDonationsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

