# OpenFec.FilingsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**candidateCandidateIdFilingsGet**](FilingsApi.md#candidateCandidateIdFilingsGet) | **GET** /candidate/{candidate_id}/filings/ | 
[**committeeCommitteeIdFilingsGet**](FilingsApi.md#committeeCommitteeIdFilingsGet) | **GET** /committee/{committee_id}/filings/ | 
[**filingsGet**](FilingsApi.md#filingsGet) | **GET** /filings/ | 
[**operationsLogGet**](FilingsApi.md#operationsLogGet) | **GET** /operations-log/ | 



## candidateCandidateIdFilingsGet

> FilingsPage candidateCandidateIdFilingsGet(apiKey, candidateId, opts)



 All official records and reports filed by or delivered to the FEC.  Note: because the filings data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned. 

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

let apiInstance = new OpenFec.FilingsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let candidateId = "candidateId_example"; // String |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
let opts = {
  'isAmended': true, // Boolean |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment. 
  'minReceiptDate': new Date("2013-10-20"), // Date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD) 
  'formCategory': ["null"], // [String] |  The forms filed are categorized based on the nature of the filing:     - REPORT F3, F3X, F3P, F3L, F4, F5, F7, F13     - NOTICE F5, F24, F6, F9, F10, F11     - STATEMENT F1, F2     - OTHER F1M, F8, F99, F12, FRQ 
  'requestType': ["null"], // [String] |  Requests for additional information (RFAIs) sent to filers. The request type is based on the type of document filed:     - 1 Statement of Organization     - 2 Report of Receipts and Expenditures (Form 3 and 3X)     - 3 Second Notice - Reports     - 4 Request for Additional Information     - 5 Informational - Reports     - 6 Second Notice - Statement of Organization     - 7 Failure to File     - 8 From Public Disclosure     - 9 From Multi Candidate Status 
  'primaryGeneralIndicator': ["null"], // [String] |  Primary, general or special election indicator. 
  'cycle': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'maxReceiptDate': new Date("2013-10-20"), // Date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD) 
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'fileNumber': [null], // [Number] | Filing ID number
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'office': ["null"], // [String] | Federal office candidate runs for: H, S or P
  'sort': ["null"], // [String] |  Provide a field to sort by. Use `-` for descending order. ex: `-case_no` 
  'qFiler': ["null"], // [String] |  Keyword search for filer name or ID 
  'district': ["null"], // [String] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
  'filerType': "filerType_example", // String | The method used to file with the FEC, either electronic or on paper.
  'mostRecent': true, // Boolean |  Report is either new or is the most-recently filed amendment 
  'reportType': ["null"], // [String] | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE) 
  'committeeType': "committeeType_example", // String | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
  'party': ["null"], // [String] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
  'formType': ["null"], // [String] | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'state': ["null"], // [String] | US state or territory where a candidate runs for office
  'reportYear': [null], // [Number] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date. 
  'amendmentIndicator': ["null"], // [String] | Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment. 
  'documentType': ["null"], // [String] |  The type of document for documents other than reports:     - 2 24 Hour Contribution Notice     - 4 48 Hour Contribution Notice     - A Debt Settlement Statement     - B Acknowledgment of Receipt of Debt Settlement Statement     - C RFAI: Debt Settlement First Notice     - D Commission Debt Settlement Review     - E Commission Response TO Debt Settlement Request     - F Administrative Termination     - G Debt Settlement Plan Amendment     - H Disavowal Notice     - I Disavowal Response     - J Conduit Report     - K Termination Approval     - L Repeat Non-Filer Notice     - M Filing Frequency Change Notice     - N Paper Amendment to Electronic Report     - O Acknowledgment of Filing Frequency Change     - S RFAI: Debt Settlement Second     - T Miscellaneous Report TO FEC     - V Repeat Violation Notice (441A OR 441B)     - P Notice of Paper Filing     - R F3L Filing Frequency Change Notice     - Q Acknowledgment of F3L Filing Frequency Change     - U Unregistered Committee Notice 
  'beginningImageNumber': ["null"] // [String] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document. 
};
apiInstance.candidateCandidateIdFilingsGet(apiKey, candidateId, opts, (error, data, response) => {
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
 **isAmended** | **Boolean**|  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  | [optional] 
 **minReceiptDate** | **Date**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **formCategory** | [**[String]**](String.md)|  The forms filed are categorized based on the nature of the filing:     - REPORT F3, F3X, F3P, F3L, F4, F5, F7, F13     - NOTICE F5, F24, F6, F9, F10, F11     - STATEMENT F1, F2     - OTHER F1M, F8, F99, F12, FRQ  | [optional] 
 **requestType** | [**[String]**](String.md)|  Requests for additional information (RFAIs) sent to filers. The request type is based on the type of document filed:     - 1 Statement of Organization     - 2 Report of Receipts and Expenditures (Form 3 and 3X)     - 3 Second Notice - Reports     - 4 Request for Additional Information     - 5 Informational - Reports     - 6 Second Notice - Statement of Organization     - 7 Failure to File     - 8 From Public Disclosure     - 9 From Multi Candidate Status  | [optional] 
 **primaryGeneralIndicator** | [**[String]**](String.md)|  Primary, general or special election indicator.  | [optional] 
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **maxReceiptDate** | **Date**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **fileNumber** | [**[Number]**](Number.md)| Filing ID number | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **office** | [**[String]**](String.md)| Federal office candidate runs for: H, S or P | [optional] 
 **sort** | [**[String]**](String.md)|  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60;  | [optional] 
 **qFiler** | [**[String]**](String.md)|  Keyword search for filer name or ID  | [optional] 
 **district** | [**[String]**](String.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **filerType** | **String**| The method used to file with the FEC, either electronic or on paper. | [optional] 
 **mostRecent** | **Boolean**|  Report is either new or is the most-recently filed amendment  | [optional] 
 **reportType** | [**[String]**](String.md)| Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional] 
 **committeeType** | **String**| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **party** | [**[String]**](String.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
 **formType** | [**[String]**](String.md)| The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **state** | [**[String]**](String.md)| US state or territory where a candidate runs for office | [optional] 
 **reportYear** | [**[Number]**](Number.md)|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] 
 **amendmentIndicator** | [**[String]**](String.md)| Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  | [optional] 
 **documentType** | [**[String]**](String.md)|  The type of document for documents other than reports:     - 2 24 Hour Contribution Notice     - 4 48 Hour Contribution Notice     - A Debt Settlement Statement     - B Acknowledgment of Receipt of Debt Settlement Statement     - C RFAI: Debt Settlement First Notice     - D Commission Debt Settlement Review     - E Commission Response TO Debt Settlement Request     - F Administrative Termination     - G Debt Settlement Plan Amendment     - H Disavowal Notice     - I Disavowal Response     - J Conduit Report     - K Termination Approval     - L Repeat Non-Filer Notice     - M Filing Frequency Change Notice     - N Paper Amendment to Electronic Report     - O Acknowledgment of Filing Frequency Change     - S RFAI: Debt Settlement Second     - T Miscellaneous Report TO FEC     - V Repeat Violation Notice (441A OR 441B)     - P Notice of Paper Filing     - R F3L Filing Frequency Change Notice     - Q Acknowledgment of F3L Filing Frequency Change     - U Unregistered Committee Notice  | [optional] 
 **beginningImageNumber** | [**[String]**](String.md)|  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  | [optional] 

### Return type

[**FilingsPage**](FilingsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## committeeCommitteeIdFilingsGet

> FilingsPage committeeCommitteeIdFilingsGet(apiKey, committeeId, opts)



 All official records and reports filed by or delivered to the FEC.  Note: because the filings data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned. 

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

let apiInstance = new OpenFec.FilingsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let committeeId = "committeeId_example"; // String |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
let opts = {
  'isAmended': true, // Boolean |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment. 
  'minReceiptDate': new Date("2013-10-20"), // Date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD) 
  'formCategory': ["null"], // [String] |  The forms filed are categorized based on the nature of the filing:     - REPORT F3, F3X, F3P, F3L, F4, F5, F7, F13     - NOTICE F5, F24, F6, F9, F10, F11     - STATEMENT F1, F2     - OTHER F1M, F8, F99, F12, FRQ 
  'requestType': ["null"], // [String] |  Requests for additional information (RFAIs) sent to filers. The request type is based on the type of document filed:     - 1 Statement of Organization     - 2 Report of Receipts and Expenditures (Form 3 and 3X)     - 3 Second Notice - Reports     - 4 Request for Additional Information     - 5 Informational - Reports     - 6 Second Notice - Statement of Organization     - 7 Failure to File     - 8 From Public Disclosure     - 9 From Multi Candidate Status 
  'primaryGeneralIndicator': ["null"], // [String] |  Primary, general or special election indicator. 
  'cycle': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'maxReceiptDate': new Date("2013-10-20"), // Date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD) 
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'fileNumber': [null], // [Number] | Filing ID number
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'office': ["null"], // [String] | Federal office candidate runs for: H, S or P
  'sort': ["null"], // [String] |  Provide a field to sort by. Use `-` for descending order. ex: `-case_no` 
  'qFiler': ["null"], // [String] |  Keyword search for filer name or ID 
  'district': ["null"], // [String] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
  'filerType': "filerType_example", // String | The method used to file with the FEC, either electronic or on paper.
  'mostRecent': true, // Boolean |  Report is either new or is the most-recently filed amendment 
  'reportType': ["null"], // [String] | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE) 
  'committeeType': "committeeType_example", // String | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
  'party': ["null"], // [String] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
  'formType': ["null"], // [String] | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'state': ["null"], // [String] | US state or territory where a candidate runs for office
  'reportYear': [null], // [Number] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date. 
  'amendmentIndicator': ["null"], // [String] | Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment. 
  'documentType': ["null"], // [String] |  The type of document for documents other than reports:     - 2 24 Hour Contribution Notice     - 4 48 Hour Contribution Notice     - A Debt Settlement Statement     - B Acknowledgment of Receipt of Debt Settlement Statement     - C RFAI: Debt Settlement First Notice     - D Commission Debt Settlement Review     - E Commission Response TO Debt Settlement Request     - F Administrative Termination     - G Debt Settlement Plan Amendment     - H Disavowal Notice     - I Disavowal Response     - J Conduit Report     - K Termination Approval     - L Repeat Non-Filer Notice     - M Filing Frequency Change Notice     - N Paper Amendment to Electronic Report     - O Acknowledgment of Filing Frequency Change     - S RFAI: Debt Settlement Second     - T Miscellaneous Report TO FEC     - V Repeat Violation Notice (441A OR 441B)     - P Notice of Paper Filing     - R F3L Filing Frequency Change Notice     - Q Acknowledgment of F3L Filing Frequency Change     - U Unregistered Committee Notice 
  'beginningImageNumber': ["null"] // [String] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document. 
};
apiInstance.committeeCommitteeIdFilingsGet(apiKey, committeeId, opts, (error, data, response) => {
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
 **isAmended** | **Boolean**|  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  | [optional] 
 **minReceiptDate** | **Date**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **formCategory** | [**[String]**](String.md)|  The forms filed are categorized based on the nature of the filing:     - REPORT F3, F3X, F3P, F3L, F4, F5, F7, F13     - NOTICE F5, F24, F6, F9, F10, F11     - STATEMENT F1, F2     - OTHER F1M, F8, F99, F12, FRQ  | [optional] 
 **requestType** | [**[String]**](String.md)|  Requests for additional information (RFAIs) sent to filers. The request type is based on the type of document filed:     - 1 Statement of Organization     - 2 Report of Receipts and Expenditures (Form 3 and 3X)     - 3 Second Notice - Reports     - 4 Request for Additional Information     - 5 Informational - Reports     - 6 Second Notice - Statement of Organization     - 7 Failure to File     - 8 From Public Disclosure     - 9 From Multi Candidate Status  | [optional] 
 **primaryGeneralIndicator** | [**[String]**](String.md)|  Primary, general or special election indicator.  | [optional] 
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **maxReceiptDate** | **Date**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **fileNumber** | [**[Number]**](Number.md)| Filing ID number | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **office** | [**[String]**](String.md)| Federal office candidate runs for: H, S or P | [optional] 
 **sort** | [**[String]**](String.md)|  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60;  | [optional] 
 **qFiler** | [**[String]**](String.md)|  Keyword search for filer name or ID  | [optional] 
 **district** | [**[String]**](String.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **filerType** | **String**| The method used to file with the FEC, either electronic or on paper. | [optional] 
 **mostRecent** | **Boolean**|  Report is either new or is the most-recently filed amendment  | [optional] 
 **reportType** | [**[String]**](String.md)| Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional] 
 **committeeType** | **String**| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **party** | [**[String]**](String.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
 **formType** | [**[String]**](String.md)| The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **state** | [**[String]**](String.md)| US state or territory where a candidate runs for office | [optional] 
 **reportYear** | [**[Number]**](Number.md)|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] 
 **amendmentIndicator** | [**[String]**](String.md)| Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  | [optional] 
 **documentType** | [**[String]**](String.md)|  The type of document for documents other than reports:     - 2 24 Hour Contribution Notice     - 4 48 Hour Contribution Notice     - A Debt Settlement Statement     - B Acknowledgment of Receipt of Debt Settlement Statement     - C RFAI: Debt Settlement First Notice     - D Commission Debt Settlement Review     - E Commission Response TO Debt Settlement Request     - F Administrative Termination     - G Debt Settlement Plan Amendment     - H Disavowal Notice     - I Disavowal Response     - J Conduit Report     - K Termination Approval     - L Repeat Non-Filer Notice     - M Filing Frequency Change Notice     - N Paper Amendment to Electronic Report     - O Acknowledgment of Filing Frequency Change     - S RFAI: Debt Settlement Second     - T Miscellaneous Report TO FEC     - V Repeat Violation Notice (441A OR 441B)     - P Notice of Paper Filing     - R F3L Filing Frequency Change Notice     - Q Acknowledgment of F3L Filing Frequency Change     - U Unregistered Committee Notice  | [optional] 
 **beginningImageNumber** | [**[String]**](String.md)|  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  | [optional] 

### Return type

[**FilingsPage**](FilingsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## filingsGet

> FilingsPage filingsGet(apiKey, opts)



 All official records and reports filed by or delivered to the FEC.  Note: because the filings data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned. 

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

let apiInstance = new OpenFec.FilingsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'isAmended': true, // Boolean |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment. 
  'minReceiptDate': new Date("2013-10-20"), // Date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD) 
  'formCategory': ["null"], // [String] |  The forms filed are categorized based on the nature of the filing:     - REPORT F3, F3X, F3P, F3L, F4, F5, F7, F13     - NOTICE F5, F24, F6, F9, F10, F11     - STATEMENT F1, F2     - OTHER F1M, F8, F99, F12, FRQ 
  'requestType': ["null"], // [String] |  Requests for additional information (RFAIs) sent to filers. The request type is based on the type of document filed:     - 1 Statement of Organization     - 2 Report of Receipts and Expenditures (Form 3 and 3X)     - 3 Second Notice - Reports     - 4 Request for Additional Information     - 5 Informational - Reports     - 6 Second Notice - Statement of Organization     - 7 Failure to File     - 8 From Public Disclosure     - 9 From Multi Candidate Status 
  'primaryGeneralIndicator': ["null"], // [String] |  Primary, general or special election indicator. 
  'cycle': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'maxReceiptDate': new Date("2013-10-20"), // Date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD) 
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'candidateId': ["null"], // [String] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
  'fileNumber': [null], // [Number] | Filing ID number
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'office': ["null"], // [String] | Federal office candidate runs for: H, S or P
  'sort': ["null"], // [String] |  Provide a field to sort by. Use `-` for descending order. ex: `-case_no` 
  'qFiler': ["null"], // [String] |  Keyword search for filer name or ID 
  'district': ["null"], // [String] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
  'filerType': "filerType_example", // String | The method used to file with the FEC, either electronic or on paper.
  'mostRecent': true, // Boolean |  Report is either new or is the most-recently filed amendment 
  'reportType': ["null"], // [String] | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE) 
  'committeeType': "committeeType_example", // String | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
  'party': ["null"], // [String] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
  'formType': ["null"], // [String] | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'state': ["null"], // [String] | US state or territory where a candidate runs for office
  'reportYear': [null], // [Number] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date. 
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'amendmentIndicator': ["null"], // [String] | Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment. 
  'documentType': ["null"], // [String] |  The type of document for documents other than reports:     - 2 24 Hour Contribution Notice     - 4 48 Hour Contribution Notice     - A Debt Settlement Statement     - B Acknowledgment of Receipt of Debt Settlement Statement     - C RFAI: Debt Settlement First Notice     - D Commission Debt Settlement Review     - E Commission Response TO Debt Settlement Request     - F Administrative Termination     - G Debt Settlement Plan Amendment     - H Disavowal Notice     - I Disavowal Response     - J Conduit Report     - K Termination Approval     - L Repeat Non-Filer Notice     - M Filing Frequency Change Notice     - N Paper Amendment to Electronic Report     - O Acknowledgment of Filing Frequency Change     - S RFAI: Debt Settlement Second     - T Miscellaneous Report TO FEC     - V Repeat Violation Notice (441A OR 441B)     - P Notice of Paper Filing     - R F3L Filing Frequency Change Notice     - Q Acknowledgment of F3L Filing Frequency Change     - U Unregistered Committee Notice 
  'beginningImageNumber': ["null"] // [String] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document. 
};
apiInstance.filingsGet(apiKey, opts, (error, data, response) => {
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
 **isAmended** | **Boolean**|  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  | [optional] 
 **minReceiptDate** | **Date**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **formCategory** | [**[String]**](String.md)|  The forms filed are categorized based on the nature of the filing:     - REPORT F3, F3X, F3P, F3L, F4, F5, F7, F13     - NOTICE F5, F24, F6, F9, F10, F11     - STATEMENT F1, F2     - OTHER F1M, F8, F99, F12, FRQ  | [optional] 
 **requestType** | [**[String]**](String.md)|  Requests for additional information (RFAIs) sent to filers. The request type is based on the type of document filed:     - 1 Statement of Organization     - 2 Report of Receipts and Expenditures (Form 3 and 3X)     - 3 Second Notice - Reports     - 4 Request for Additional Information     - 5 Informational - Reports     - 6 Second Notice - Statement of Organization     - 7 Failure to File     - 8 From Public Disclosure     - 9 From Multi Candidate Status  | [optional] 
 **primaryGeneralIndicator** | [**[String]**](String.md)|  Primary, general or special election indicator.  | [optional] 
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **maxReceiptDate** | **Date**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **candidateId** | [**[String]**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
 **fileNumber** | [**[Number]**](Number.md)| Filing ID number | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **office** | [**[String]**](String.md)| Federal office candidate runs for: H, S or P | [optional] 
 **sort** | [**[String]**](String.md)|  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60;  | [optional] 
 **qFiler** | [**[String]**](String.md)|  Keyword search for filer name or ID  | [optional] 
 **district** | [**[String]**](String.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **filerType** | **String**| The method used to file with the FEC, either electronic or on paper. | [optional] 
 **mostRecent** | **Boolean**|  Report is either new or is the most-recently filed amendment  | [optional] 
 **reportType** | [**[String]**](String.md)| Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional] 
 **committeeType** | **String**| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **party** | [**[String]**](String.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
 **formType** | [**[String]**](String.md)| The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **state** | [**[String]**](String.md)| US state or territory where a candidate runs for office | [optional] 
 **reportYear** | [**[Number]**](Number.md)|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] 
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **amendmentIndicator** | [**[String]**](String.md)| Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  | [optional] 
 **documentType** | [**[String]**](String.md)|  The type of document for documents other than reports:     - 2 24 Hour Contribution Notice     - 4 48 Hour Contribution Notice     - A Debt Settlement Statement     - B Acknowledgment of Receipt of Debt Settlement Statement     - C RFAI: Debt Settlement First Notice     - D Commission Debt Settlement Review     - E Commission Response TO Debt Settlement Request     - F Administrative Termination     - G Debt Settlement Plan Amendment     - H Disavowal Notice     - I Disavowal Response     - J Conduit Report     - K Termination Approval     - L Repeat Non-Filer Notice     - M Filing Frequency Change Notice     - N Paper Amendment to Electronic Report     - O Acknowledgment of Filing Frequency Change     - S RFAI: Debt Settlement Second     - T Miscellaneous Report TO FEC     - V Repeat Violation Notice (441A OR 441B)     - P Notice of Paper Filing     - R F3L Filing Frequency Change Notice     - Q Acknowledgment of F3L Filing Frequency Change     - U Unregistered Committee Notice  | [optional] 
 **beginningImageNumber** | [**[String]**](String.md)|  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  | [optional] 

### Return type

[**FilingsPage**](FilingsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## operationsLogGet

> OperationsLogPage operationsLogGet(apiKey, opts)



 The Operations log contains details of each report loaded into the database. It is primarily used as status check to determine when all of the data processes, from initial entry through review are complete. 

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

let apiInstance = new OpenFec.FilingsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'minReceiptDate': new Date("2013-10-20"), // Date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD) 
  'candidateCommitteeId': ["null"], // [String] |  A unique identifier of the registered filer. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'maxReceiptDate': new Date("2013-10-20"), // Date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD) 
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'maxTransactionDataCompleteDate': new Date("2013-10-20"), // Date |  Select all filings processed completely before this date(MM/DD/YYYY or YYYY-MM-DD) 
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': ["null"], // [String] |  Provide a field to sort by. Use `-` for descending order. ex: `-case_no` 
  'reportType': ["null"], // [String] | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE) 
  'minTransactionDataCompleteDate': new Date("2013-10-20"), // Date |  Select all filings processed completely after this date(MM/DD/YYYY or YYYY-MM-DD) 
  'formType': ["null"], // [String] | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'maxCoverageEndDate': new Date("2013-10-20"), // Date |  Ending date of the reporting period before this date(MM/DD/YYYY or YYYY-MM-DD) 
  'page': 1, // Number | For paginating through results, starting at page 1
  'reportYear': [null], // [Number] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date. 
  'statusNum': ["null"], // [String] |  Status of the transactional report.     -0- Transaction is entered            into the system.           But not verified.     -1- Transaction is verified. 
  'amendmentIndicator': ["null"], // [String] | Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment. 
  'beginningImageNumber': ["null"], // [String] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document. 
  'minCoverageEndDate': new Date("2013-10-20") // Date |  Ending date of the reporting period after this date(MM/DD/YYYY or YYYY-MM-DD) 
};
apiInstance.operationsLogGet(apiKey, opts, (error, data, response) => {
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
 **minReceiptDate** | **Date**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **candidateCommitteeId** | [**[String]**](String.md)|  A unique identifier of the registered filer.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **maxReceiptDate** | **Date**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **maxTransactionDataCompleteDate** | **Date**|  Select all filings processed completely before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | [**[String]**](String.md)|  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60;  | [optional] 
 **reportType** | [**[String]**](String.md)| Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional] 
 **minTransactionDataCompleteDate** | **Date**|  Select all filings processed completely after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **formType** | [**[String]**](String.md)| The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **maxCoverageEndDate** | **Date**|  Ending date of the reporting period before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **reportYear** | [**[Number]**](Number.md)|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] 
 **statusNum** | [**[String]**](String.md)|  Status of the transactional report.     -0- Transaction is entered            into the system.           But not verified.     -1- Transaction is verified.  | [optional] 
 **amendmentIndicator** | [**[String]**](String.md)| Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  | [optional] 
 **beginningImageNumber** | [**[String]**](String.md)|  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  | [optional] 
 **minCoverageEndDate** | **Date**|  Ending date of the reporting period after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 

### Return type

[**OperationsLogPage**](OperationsLogPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

