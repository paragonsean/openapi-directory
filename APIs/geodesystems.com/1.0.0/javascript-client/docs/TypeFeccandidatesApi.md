# GeodesystemsCom443.TypeFeccandidatesApi

All URIs are relative to *https://geodesystems.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchFeccandidates**](TypeFeccandidatesApi.md#searchFeccandidates) | **GET** /repository/search/type/feccandidates | Search API for &#39;Candidates&#39; entry type



## searchFeccandidates

> searchFeccandidates(opts)

Search API for &#39;Candidates&#39; entry type

API to search for entries of type Candidates

### Example

```javascript
import GeodesystemsCom443 from 'geodesystems_com443';

let apiInstance = new GeodesystemsCom443.TypeFeccandidatesApi();
let opts = {
  'text': "text_example", // String | Search text
  'name': "name_example", // String | Search name
  'description': "description_example", // String | Search description
  'fromdate': new Date("2013-10-20T19:20:30+01:00"), // Date | From date
  'todate': new Date("2013-10-20T19:20:30+01:00"), // Date | To date
  'createdateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Archive create date from
  'createdateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Archive create date to
  'changedateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Archive change date from
  'changedateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Archive change date to
  'group': "group_example", // String | Parent entry
  'filesuffix': "filesuffix_example", // String | File suffix
  'maxlatitude': 3.4, // Number | Northern bounds of search
  'minlongitude': 3.4, // Number | Western bounds of search
  'minlatitude': 3.4, // Number | Southern bounds of search
  'maxlongitude': 3.4, // Number | Eastern bounds of search
  'max': 56, // Number | Max number of results
  'skip': 56, // Number | Number to skip
  'searchDbFeccandidatesName': "searchDbFeccandidatesName_example", // String | Name
  'searchDbFeccandidatesParty': "searchDbFeccandidatesParty_example", // String | Party
  'searchDbFeccandidatesState': "searchDbFeccandidatesState_example", // String | State
  'searchDbFeccandidatesDistrict': "searchDbFeccandidatesDistrict_example", // String | District
  'searchDbFeccandidatesGender': "searchDbFeccandidatesGender_example", // String | Gender
  'searchDbFeccandidatesBeginningCash': 3.4, // Number | Beginning Cash
  'searchDbFeccandidatesEndingCash': 3.4, // Number | Ending Cash
  'searchDbFeccandidatesTotalReceipts': 3.4, // Number | Total Receipts
  'searchDbFeccandidatesTotalIndivualContributions': 3.4, // Number | Total Indivual Contributions
  'searchDbFeccandidatesTransfersFromCommittees': 3.4, // Number | Transfers From Committees
  'searchDbFeccandidatesTransfersToCommittees': 3.4, // Number | Transfers To Committees
  'searchDbFeccandidatesTotalDisbursements': 3.4, // Number | Total Disbursements
  'searchDbFeccandidatesContributionsFromCandidate': 3.4, // Number | Contributions From Candidate
  'searchDbFeccandidatesLoansFromCandidates': 3.4, // Number | Loans From Candidates
  'searchDbFeccandidatesOtherLoans': 3.4, // Number | Other Loans
  'searchDbFeccandidatesCandidateLoanRepayments': 3.4, // Number | Candidate Loan Repayments
  'searchDbFeccandidatesOtherLoanRepayments': 3.4, // Number | Other Loan Repayments
  'searchDbFeccandidatesDebtsOwedBy': 3.4, // Number | Debts Owed By
  'searchDbFeccandidatesContributionsFromOtherCommittees': 3.4, // Number | Contributions From Other Committees
  'searchDbFeccandidatesContributionsFromPartyCommittees': 3.4, // Number | Contributions From Party Committees
  'searchDbFeccandidatesCoverageEndDate': "searchDbFeccandidatesCoverageEndDate_example", // String | Coverage End Date
  'searchDbFeccandidatesIndividualRefunds': 3.4, // Number | Individual Refunds
  'searchDbFeccandidatesCommitteeRefunds': 3.4 // Number | Committee Refunds
};
apiInstance.searchFeccandidates(opts, (error, data, response) => {
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
 **text** | **String**| Search text | [optional] 
 **name** | **String**| Search name | [optional] 
 **description** | **String**| Search description | [optional] 
 **fromdate** | **Date**| From date | [optional] 
 **todate** | **Date**| To date | [optional] 
 **createdateFrom** | **Date**| Archive create date from | [optional] 
 **createdateTo** | **Date**| Archive create date to | [optional] 
 **changedateFrom** | **Date**| Archive change date from | [optional] 
 **changedateTo** | **Date**| Archive change date to | [optional] 
 **group** | **String**| Parent entry | [optional] 
 **filesuffix** | **String**| File suffix | [optional] 
 **maxlatitude** | **Number**| Northern bounds of search | [optional] 
 **minlongitude** | **Number**| Western bounds of search | [optional] 
 **minlatitude** | **Number**| Southern bounds of search | [optional] 
 **maxlongitude** | **Number**| Eastern bounds of search | [optional] 
 **max** | **Number**| Max number of results | [optional] 
 **skip** | **Number**| Number to skip | [optional] 
 **searchDbFeccandidatesName** | **String**| Name | [optional] 
 **searchDbFeccandidatesParty** | **String**| Party | [optional] 
 **searchDbFeccandidatesState** | **String**| State | [optional] 
 **searchDbFeccandidatesDistrict** | **String**| District | [optional] 
 **searchDbFeccandidatesGender** | **String**| Gender | [optional] 
 **searchDbFeccandidatesBeginningCash** | **Number**| Beginning Cash | [optional] 
 **searchDbFeccandidatesEndingCash** | **Number**| Ending Cash | [optional] 
 **searchDbFeccandidatesTotalReceipts** | **Number**| Total Receipts | [optional] 
 **searchDbFeccandidatesTotalIndivualContributions** | **Number**| Total Indivual Contributions | [optional] 
 **searchDbFeccandidatesTransfersFromCommittees** | **Number**| Transfers From Committees | [optional] 
 **searchDbFeccandidatesTransfersToCommittees** | **Number**| Transfers To Committees | [optional] 
 **searchDbFeccandidatesTotalDisbursements** | **Number**| Total Disbursements | [optional] 
 **searchDbFeccandidatesContributionsFromCandidate** | **Number**| Contributions From Candidate | [optional] 
 **searchDbFeccandidatesLoansFromCandidates** | **Number**| Loans From Candidates | [optional] 
 **searchDbFeccandidatesOtherLoans** | **Number**| Other Loans | [optional] 
 **searchDbFeccandidatesCandidateLoanRepayments** | **Number**| Candidate Loan Repayments | [optional] 
 **searchDbFeccandidatesOtherLoanRepayments** | **Number**| Other Loan Repayments | [optional] 
 **searchDbFeccandidatesDebtsOwedBy** | **Number**| Debts Owed By | [optional] 
 **searchDbFeccandidatesContributionsFromOtherCommittees** | **Number**| Contributions From Other Committees | [optional] 
 **searchDbFeccandidatesContributionsFromPartyCommittees** | **Number**| Contributions From Party Committees | [optional] 
 **searchDbFeccandidatesCoverageEndDate** | **String**| Coverage End Date | [optional] 
 **searchDbFeccandidatesIndividualRefunds** | **Number**| Individual Refunds | [optional] 
 **searchDbFeccandidatesCommitteeRefunds** | **Number**| Committee Refunds | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

