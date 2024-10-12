# OpenFec.IndependentExpendituresApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedulesScheduleEByCandidateGet**](IndependentExpendituresApi.md#schedulesScheduleEByCandidateGet) | **GET** /schedules/schedule_e/by_candidate/ | 
[**schedulesScheduleEEfileGet**](IndependentExpendituresApi.md#schedulesScheduleEEfileGet) | **GET** /schedules/schedule_e/efile/ | 
[**schedulesScheduleEGet**](IndependentExpendituresApi.md#schedulesScheduleEGet) | **GET** /schedules/schedule_e/ | 
[**schedulesScheduleETotalsByCandidateGet**](IndependentExpendituresApi.md#schedulesScheduleETotalsByCandidateGet) | **GET** /schedules/schedule_e/totals/by_candidate/ | 



## schedulesScheduleEByCandidateGet

> ScheduleEByCandidatePage schedulesScheduleEByCandidateGet(apiKey, opts)



 Schedule E receipts aggregated by recipient candidate. To avoid double counting, memoed items are not included. 

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

let apiInstance = new OpenFec.IndependentExpendituresApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'district': "district_example", // String | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
  'supportOppose': "supportOppose_example", // String | Support or opposition
  'electionFull': true, // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
  'cycle': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'page': 1, // Number | For paginating through results, starting at page 1
  'state': "state_example", // String | US state or territory where a candidate runs for office
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'candidateId': ["null"], // [String] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'office': "office_example", // String | Federal office candidate runs for: H, S or P
  'sort': "sort_example" // String | Provide a field to sort by. Use `-` for descending order. 
};
apiInstance.schedulesScheduleEByCandidateGet(apiKey, opts, (error, data, response) => {
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
 **district** | **String**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **supportOppose** | **String**| Support or opposition | [optional] 
 **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **state** | **String**| US state or territory where a candidate runs for office | [optional] 
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **candidateId** | [**[String]**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **office** | **String**| Federal office candidate runs for: H, S or P | [optional] 
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 

### Return type

[**ScheduleEByCandidatePage**](ScheduleEByCandidatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesScheduleEEfileGet

> ScheduleEEfilePage schedulesScheduleEEfileGet(apiKey, opts)



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

let apiInstance = new OpenFec.IndependentExpendituresApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'maxExpenditureAmount': 56, // Number | Selects all items expended by this committee less than this amount
  'supportOpposeIndicator': ["null"], // [String] | Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs.
  'minExpenditureDate': new Date("2013-10-20"), // Date | Selects all items expended by this committee after this date
  'filingForm': ["null"], // [String] | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information 
  'maxExpenditureDate': new Date("2013-10-20"), // Date | Selects all items expended by this committee before this date
  'maxFiledDate': new Date("2013-10-20"), // Date | Timestamp of electronic or paper record that FEC received
  'isNotice': true, // Boolean |  Record filed as 24- or 48-hour notice. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'payeeName': ["null"], // [String] |  Name of the entity that received the payment. 
  'candidateId': ["null"], // [String] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'candidateOfficeDistrict': ["null"], // [String] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
  'sort': "'-expenditure_date'", // String | Provide a field to sort by. Use `-` for descending order. 
  'minExpenditureAmount': 56, // Number | Selects all items expended by this committee greater than this amount
  'spenderName': ["null"], // [String] | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records.
  'minDisseminationDate': new Date("2013-10-20"), // Date | Selects all items distributed by this committee after this date
  'candidateOfficeState': ["null"], // [String] | US state or territory where a candidate runs for office
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'candidateSearch': ["null"], // [String] |  Search for candidates by candiate id or candidate first or last name 
  'imageNumber': ["null"], // [String] |  An unique identifier for each page where the electronic or paper filing is reported. 
  'candidateParty': ["null"], // [String] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
  'minFiledDate': new Date("2013-10-20"), // Date | Timestamp of electronic or paper record that FEC received
  'maxDisseminationDate': new Date("2013-10-20"), // Date | Selects all items distributed by this committee before this date
  'mostRecent': true, // Boolean |  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (`null`) is always included. 
  'candidateOffice': "candidateOffice_example" // String | Federal office candidate runs for: H, S or P
};
apiInstance.schedulesScheduleEEfileGet(apiKey, opts, (error, data, response) => {
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
 **maxExpenditureAmount** | **Number**| Selects all items expended by this committee less than this amount | [optional] 
 **supportOpposeIndicator** | [**[String]**](String.md)| Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs. | [optional] 
 **minExpenditureDate** | **Date**| Selects all items expended by this committee after this date | [optional] 
 **filingForm** | [**[String]**](String.md)| The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional] 
 **maxExpenditureDate** | **Date**| Selects all items expended by this committee before this date | [optional] 
 **maxFiledDate** | **Date**| Timestamp of electronic or paper record that FEC received | [optional] 
 **isNotice** | **Boolean**|  Record filed as 24- or 48-hour notice.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **payeeName** | [**[String]**](String.md)|  Name of the entity that received the payment.  | [optional] 
 **candidateId** | [**[String]**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **candidateOfficeDistrict** | [**[String]**](String.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-expenditure_date&#39;]
 **minExpenditureAmount** | **Number**| Selects all items expended by this committee greater than this amount | [optional] 
 **spenderName** | [**[String]**](String.md)| The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
 **minDisseminationDate** | **Date**| Selects all items distributed by this committee after this date | [optional] 
 **candidateOfficeState** | [**[String]**](String.md)| US state or territory where a candidate runs for office | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **candidateSearch** | [**[String]**](String.md)|  Search for candidates by candiate id or candidate first or last name  | [optional] 
 **imageNumber** | [**[String]**](String.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **candidateParty** | [**[String]**](String.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
 **minFiledDate** | **Date**| Timestamp of electronic or paper record that FEC received | [optional] 
 **maxDisseminationDate** | **Date**| Selects all items distributed by this committee before this date | [optional] 
 **mostRecent** | **Boolean**|  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (&#x60;null&#x60;) is always included.  | [optional] 
 **candidateOffice** | **String**| Federal office candidate runs for: H, S or P | [optional] 

### Return type

[**ScheduleEEfilePage**](ScheduleEEfilePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesScheduleEGet

> ScheduleEPage schedulesScheduleEGet(apiKey, opts)



 Schedule E covers the line item expenditures for independent expenditures. For example, if a super PAC bought ads on TV to oppose a federal candidate, each ad purchase would be recorded here with the expenditure amount, name and id of the candidate, and whether the ad supported or opposed the candidate.  An independent expenditure is an expenditure for a communication \&quot;expressly advocating the election or defeat of a clearly identified candidate that is not made in cooperation, consultation, or concert with, or at the request or suggestion of, a candidate, a candidate’s authorized committee, or their agents, or a political party or its agents.\&quot;  Aggregates by candidate do not include 24 and 48 hour reports. This ensures we don&#39;t double count expenditures and the totals are more accurate. You can still find the information from 24 and 48 hour reports in &#x60;/schedule/schedule_e/&#x60;.  Due to the large quantity of Schedule E filings, this endpoint is not paginated by page number. Instead, you can request the next page of results by adding the values in the &#x60;last_indexes&#x60; object from &#x60;pagination&#x60; to the URL of your last request. For example, when sorting by &#x60;expenditure_amount&#x60;, you might receive a page of results with the following pagination information:  &#x60;&#x60;&#x60;  \&quot;pagination\&quot;: {     \&quot;count\&quot;: 152623,     \&quot;last_indexes\&quot;: {       \&quot;last_index\&quot;: \&quot;3023037\&quot;,       \&quot;last_expenditure_amount\&quot;: -17348.5     },     \&quot;per_page\&quot;: 20,     \&quot;pages\&quot;: 7632   } } &#x60;&#x60;&#x60;  To fetch the next page of sorted results, append &#x60;last_index&#x3D;3023037&#x60; and &#x60;last_expenditure_amount&#x3D;&#x60; to the URL.  We strongly advise paging through these results by using the sort indices (defaults to sort by disbursement date, e.g. &#x60;last_disbursement_date&#x60;), otherwise some resources may be unintentionally filtered out.  This resource uses keyset pagination to improve query performance and these indices are required to properly page through this large dataset.  Note: because the Schedule E data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned. 

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

let apiInstance = new OpenFec.IndependentExpendituresApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'lastExpenditureDate': new Date("2013-10-20"), // Date |  When sorting by `expenditure_date`, this is populated with the `expenditure_date` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page. 
  'maxImageNumber': "maxImageNumber_example", // String | Maxium image number of the page where the schedule item is reported
  'isNotice': [null], // [Boolean] |  Record filed as 24- or 48-hour notice. 
  'payeeName': ["null"], // [String] |  Name of the entity that received the payment. 
  'minAmount': "minAmount_example", // String | Filter for all amounts greater than a value.
  'candidateId': ["null"], // [String] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'lastOfficeTotalYtd': 3.4, // Number |  When sorting by `office_total_ytd`, this is populated with the `office_total_ytd` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page.' 
  'sort': "'-expenditure_date'", // String | Provide a field to sort by. Use `-` for descending order. 
  'minFilingDate': new Date("2013-10-20"), // Date |  Selects all filings received after this date 
  'qSpender': ["null"], // [String] |  Keyword search for spender name or ID 
  'minDisseminationDate': new Date("2013-10-20"), // Date | Selects all items distributed by this committee after this date
  'candidateOfficeState': ["null"], // [String] | US state or territory
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'lastExpenditureAmount': 3.4, // Number |  When sorting by `expenditure_amount`, this is populated with the `expenditure_amount` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page. 
  'imageNumber': ["null"], // [String] |  An unique identifier for each page where the electronic or paper filing is reported. 
  'maxDate': new Date("2013-10-20"), // Date | Maximum date
  'maxDisseminationDate': new Date("2013-10-20"), // Date | Selects all items distributed by this committee before this date
  'minDate': new Date("2013-10-20"), // Date | Minimum date
  'filingForm': ["null"], // [String] | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information 
  'supportOpposeIndicator': ["null"], // [String] | Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs.
  'minImageNumber': "minImageNumber_example", // String | Minium image number of the page where the schedule item is reported
  'cycle': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'maxFilingDate': new Date("2013-10-20"), // Date |  Selects all filings received before this date 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'lastSupportOpposeIndicator': "lastSupportOpposeIndicator_example", // String |  When sorting by `support_oppose_indicator`, this is populated with the `support_oppose_indicator` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page.' 
  'lastIndex': 56, // Number | Index of last result from previous page
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'candidateOfficeDistrict': ["null"], // [String] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
  'lineNumber': "lineNumber_example", // String | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'candidateParty': ["null"], // [String] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
  'maxAmount': "maxAmount_example", // String | Filter for all amounts less than a value.
  'mostRecent': true, // Boolean |  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (`null`) is always included. 
  'candidateOffice': ["null"] // [String] | Federal office candidate runs for: H, S or P
};
apiInstance.schedulesScheduleEGet(apiKey, opts, (error, data, response) => {
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
 **lastExpenditureDate** | **Date**|  When sorting by &#x60;expenditure_date&#x60;, this is populated with the &#x60;expenditure_date&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.  | [optional] 
 **maxImageNumber** | **String**| Maxium image number of the page where the schedule item is reported | [optional] 
 **isNotice** | [**[Boolean]**](Boolean.md)|  Record filed as 24- or 48-hour notice.  | [optional] 
 **payeeName** | [**[String]**](String.md)|  Name of the entity that received the payment.  | [optional] 
 **minAmount** | **String**| Filter for all amounts greater than a value. | [optional] 
 **candidateId** | [**[String]**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **lastOfficeTotalYtd** | **Number**|  When sorting by &#x60;office_total_ytd&#x60;, this is populated with the &#x60;office_total_ytd&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.&#39;  | [optional] 
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-expenditure_date&#39;]
 **minFilingDate** | **Date**|  Selects all filings received after this date  | [optional] 
 **qSpender** | [**[String]**](String.md)|  Keyword search for spender name or ID  | [optional] 
 **minDisseminationDate** | **Date**| Selects all items distributed by this committee after this date | [optional] 
 **candidateOfficeState** | [**[String]**](String.md)| US state or territory | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **lastExpenditureAmount** | **Number**|  When sorting by &#x60;expenditure_amount&#x60;, this is populated with the &#x60;expenditure_amount&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.  | [optional] 
 **imageNumber** | [**[String]**](String.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **maxDate** | **Date**| Maximum date | [optional] 
 **maxDisseminationDate** | **Date**| Selects all items distributed by this committee before this date | [optional] 
 **minDate** | **Date**| Minimum date | [optional] 
 **filingForm** | [**[String]**](String.md)| The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional] 
 **supportOpposeIndicator** | [**[String]**](String.md)| Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs. | [optional] 
 **minImageNumber** | **String**| Minium image number of the page where the schedule item is reported | [optional] 
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **maxFilingDate** | **Date**|  Selects all filings received before this date  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **lastSupportOpposeIndicator** | **String**|  When sorting by &#x60;support_oppose_indicator&#x60;, this is populated with the &#x60;support_oppose_indicator&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.&#39;  | [optional] 
 **lastIndex** | **Number**| Index of last result from previous page | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **candidateOfficeDistrict** | [**[String]**](String.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **lineNumber** | **String**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional] 
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **candidateParty** | [**[String]**](String.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
 **maxAmount** | **String**| Filter for all amounts less than a value. | [optional] 
 **mostRecent** | **Boolean**|  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (&#x60;null&#x60;) is always included.  | [optional] 
 **candidateOffice** | [**[String]**](String.md)| Federal office candidate runs for: H, S or P | [optional] 

### Return type

[**ScheduleEPage**](ScheduleEPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesScheduleETotalsByCandidateGet

> IETotalsByCandidatePage schedulesScheduleETotalsByCandidateGet(apiKey, opts)



 Total independent expenditure on supported or opposed candidates by cycle or candidate election year. 

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

let apiInstance = new OpenFec.IndependentExpendituresApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'electionFull': true, // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
  'cycle': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'candidateId': ["null"], // [String] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': "sort_example" // String | Provide a field to sort by. Use `-` for descending order. 
};
apiInstance.schedulesScheduleETotalsByCandidateGet(apiKey, opts, (error, data, response) => {
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
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **candidateId** | [**[String]**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 

### Return type

[**IETotalsByCandidatePage**](IETotalsByCandidatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

