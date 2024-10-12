# TypeFeccandidatesApi

All URIs are relative to *https://geodesystems.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchFeccandidates**](TypeFeccandidatesApi.md#searchFeccandidates) | **GET** /repository/search/type/feccandidates | Search API for &#39;Candidates&#39; entry type |


<a id="searchFeccandidates"></a>
# **searchFeccandidates**
> searchFeccandidates(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbFeccandidatesName, searchDbFeccandidatesParty, searchDbFeccandidatesState, searchDbFeccandidatesDistrict, searchDbFeccandidatesGender, searchDbFeccandidatesBeginningCash, searchDbFeccandidatesEndingCash, searchDbFeccandidatesTotalReceipts, searchDbFeccandidatesTotalIndivualContributions, searchDbFeccandidatesTransfersFromCommittees, searchDbFeccandidatesTransfersToCommittees, searchDbFeccandidatesTotalDisbursements, searchDbFeccandidatesContributionsFromCandidate, searchDbFeccandidatesLoansFromCandidates, searchDbFeccandidatesOtherLoans, searchDbFeccandidatesCandidateLoanRepayments, searchDbFeccandidatesOtherLoanRepayments, searchDbFeccandidatesDebtsOwedBy, searchDbFeccandidatesContributionsFromOtherCommittees, searchDbFeccandidatesContributionsFromPartyCommittees, searchDbFeccandidatesCoverageEndDate, searchDbFeccandidatesIndividualRefunds, searchDbFeccandidatesCommitteeRefunds)

Search API for &#39;Candidates&#39; entry type

API to search for entries of type Candidates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TypeFeccandidatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geodesystems.com:443");

    TypeFeccandidatesApi apiInstance = new TypeFeccandidatesApi(defaultClient);
    String text = "text_example"; // String | Search text
    String name = "name_example"; // String | Search name
    String description = "description_example"; // String | Search description
    OffsetDateTime fromdate = OffsetDateTime.now(); // OffsetDateTime | From date
    OffsetDateTime todate = OffsetDateTime.now(); // OffsetDateTime | To date
    OffsetDateTime createdateFrom = OffsetDateTime.now(); // OffsetDateTime | Archive create date from
    OffsetDateTime createdateTo = OffsetDateTime.now(); // OffsetDateTime | Archive create date to
    OffsetDateTime changedateFrom = OffsetDateTime.now(); // OffsetDateTime | Archive change date from
    OffsetDateTime changedateTo = OffsetDateTime.now(); // OffsetDateTime | Archive change date to
    String group = "group_example"; // String | Parent entry
    String filesuffix = "filesuffix_example"; // String | File suffix
    Float maxlatitude = 3.4F; // Float | Northern bounds of search
    Float minlongitude = 3.4F; // Float | Western bounds of search
    Float minlatitude = 3.4F; // Float | Southern bounds of search
    Float maxlongitude = 3.4F; // Float | Eastern bounds of search
    Integer max = 56; // Integer | Max number of results
    Integer skip = 56; // Integer | Number to skip
    String searchDbFeccandidatesName = "searchDbFeccandidatesName_example"; // String | Name
    String searchDbFeccandidatesParty = "searchDbFeccandidatesParty_example"; // String | Party
    String searchDbFeccandidatesState = "searchDbFeccandidatesState_example"; // String | State
    String searchDbFeccandidatesDistrict = "searchDbFeccandidatesDistrict_example"; // String | District
    String searchDbFeccandidatesGender = "searchDbFeccandidatesGender_example"; // String | Gender
    Double searchDbFeccandidatesBeginningCash = 3.4D; // Double | Beginning Cash
    Double searchDbFeccandidatesEndingCash = 3.4D; // Double | Ending Cash
    Double searchDbFeccandidatesTotalReceipts = 3.4D; // Double | Total Receipts
    Double searchDbFeccandidatesTotalIndivualContributions = 3.4D; // Double | Total Indivual Contributions
    Double searchDbFeccandidatesTransfersFromCommittees = 3.4D; // Double | Transfers From Committees
    Double searchDbFeccandidatesTransfersToCommittees = 3.4D; // Double | Transfers To Committees
    Double searchDbFeccandidatesTotalDisbursements = 3.4D; // Double | Total Disbursements
    Double searchDbFeccandidatesContributionsFromCandidate = 3.4D; // Double | Contributions From Candidate
    Double searchDbFeccandidatesLoansFromCandidates = 3.4D; // Double | Loans From Candidates
    Double searchDbFeccandidatesOtherLoans = 3.4D; // Double | Other Loans
    Double searchDbFeccandidatesCandidateLoanRepayments = 3.4D; // Double | Candidate Loan Repayments
    Double searchDbFeccandidatesOtherLoanRepayments = 3.4D; // Double | Other Loan Repayments
    Double searchDbFeccandidatesDebtsOwedBy = 3.4D; // Double | Debts Owed By
    Double searchDbFeccandidatesContributionsFromOtherCommittees = 3.4D; // Double | Contributions From Other Committees
    Double searchDbFeccandidatesContributionsFromPartyCommittees = 3.4D; // Double | Contributions From Party Committees
    String searchDbFeccandidatesCoverageEndDate = "searchDbFeccandidatesCoverageEndDate_example"; // String | Coverage End Date
    Double searchDbFeccandidatesIndividualRefunds = 3.4D; // Double | Individual Refunds
    Double searchDbFeccandidatesCommitteeRefunds = 3.4D; // Double | Committee Refunds
    try {
      apiInstance.searchFeccandidates(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbFeccandidatesName, searchDbFeccandidatesParty, searchDbFeccandidatesState, searchDbFeccandidatesDistrict, searchDbFeccandidatesGender, searchDbFeccandidatesBeginningCash, searchDbFeccandidatesEndingCash, searchDbFeccandidatesTotalReceipts, searchDbFeccandidatesTotalIndivualContributions, searchDbFeccandidatesTransfersFromCommittees, searchDbFeccandidatesTransfersToCommittees, searchDbFeccandidatesTotalDisbursements, searchDbFeccandidatesContributionsFromCandidate, searchDbFeccandidatesLoansFromCandidates, searchDbFeccandidatesOtherLoans, searchDbFeccandidatesCandidateLoanRepayments, searchDbFeccandidatesOtherLoanRepayments, searchDbFeccandidatesDebtsOwedBy, searchDbFeccandidatesContributionsFromOtherCommittees, searchDbFeccandidatesContributionsFromPartyCommittees, searchDbFeccandidatesCoverageEndDate, searchDbFeccandidatesIndividualRefunds, searchDbFeccandidatesCommitteeRefunds);
    } catch (ApiException e) {
      System.err.println("Exception when calling TypeFeccandidatesApi#searchFeccandidates");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **text** | **String**| Search text | [optional] |
| **name** | **String**| Search name | [optional] |
| **description** | **String**| Search description | [optional] |
| **fromdate** | **OffsetDateTime**| From date | [optional] |
| **todate** | **OffsetDateTime**| To date | [optional] |
| **createdateFrom** | **OffsetDateTime**| Archive create date from | [optional] |
| **createdateTo** | **OffsetDateTime**| Archive create date to | [optional] |
| **changedateFrom** | **OffsetDateTime**| Archive change date from | [optional] |
| **changedateTo** | **OffsetDateTime**| Archive change date to | [optional] |
| **group** | **String**| Parent entry | [optional] |
| **filesuffix** | **String**| File suffix | [optional] |
| **maxlatitude** | **Float**| Northern bounds of search | [optional] |
| **minlongitude** | **Float**| Western bounds of search | [optional] |
| **minlatitude** | **Float**| Southern bounds of search | [optional] |
| **maxlongitude** | **Float**| Eastern bounds of search | [optional] |
| **max** | **Integer**| Max number of results | [optional] |
| **skip** | **Integer**| Number to skip | [optional] |
| **searchDbFeccandidatesName** | **String**| Name | [optional] |
| **searchDbFeccandidatesParty** | **String**| Party | [optional] |
| **searchDbFeccandidatesState** | **String**| State | [optional] |
| **searchDbFeccandidatesDistrict** | **String**| District | [optional] |
| **searchDbFeccandidatesGender** | **String**| Gender | [optional] |
| **searchDbFeccandidatesBeginningCash** | **Double**| Beginning Cash | [optional] |
| **searchDbFeccandidatesEndingCash** | **Double**| Ending Cash | [optional] |
| **searchDbFeccandidatesTotalReceipts** | **Double**| Total Receipts | [optional] |
| **searchDbFeccandidatesTotalIndivualContributions** | **Double**| Total Indivual Contributions | [optional] |
| **searchDbFeccandidatesTransfersFromCommittees** | **Double**| Transfers From Committees | [optional] |
| **searchDbFeccandidatesTransfersToCommittees** | **Double**| Transfers To Committees | [optional] |
| **searchDbFeccandidatesTotalDisbursements** | **Double**| Total Disbursements | [optional] |
| **searchDbFeccandidatesContributionsFromCandidate** | **Double**| Contributions From Candidate | [optional] |
| **searchDbFeccandidatesLoansFromCandidates** | **Double**| Loans From Candidates | [optional] |
| **searchDbFeccandidatesOtherLoans** | **Double**| Other Loans | [optional] |
| **searchDbFeccandidatesCandidateLoanRepayments** | **Double**| Candidate Loan Repayments | [optional] |
| **searchDbFeccandidatesOtherLoanRepayments** | **Double**| Other Loan Repayments | [optional] |
| **searchDbFeccandidatesDebtsOwedBy** | **Double**| Debts Owed By | [optional] |
| **searchDbFeccandidatesContributionsFromOtherCommittees** | **Double**| Contributions From Other Committees | [optional] |
| **searchDbFeccandidatesContributionsFromPartyCommittees** | **Double**| Contributions From Party Committees | [optional] |
| **searchDbFeccandidatesCoverageEndDate** | **String**| Coverage End Date | [optional] |
| **searchDbFeccandidatesIndividualRefunds** | **Double**| Individual Refunds | [optional] |
| **searchDbFeccandidatesCommitteeRefunds** | **Double**| Committee Refunds | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

