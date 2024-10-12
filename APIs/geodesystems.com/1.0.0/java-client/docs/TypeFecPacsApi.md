# TypeFecPacsApi

All URIs are relative to *https://geodesystems.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchFecPacs**](TypeFecPacsApi.md#searchFecPacs) | **GET** /repository/search/type/fec_pacs | Search API for &#39;FEC PACs&#39; entry type |


<a id="searchFecPacs"></a>
# **searchFecPacs**
> searchFecPacs(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbFecPacsCommittee, searchDbFecPacsTotalReceipts, searchDbFecPacsBeginningCash, searchDbFecPacsEndingCash, searchDbFecPacsContributionsFromIndividuals, searchDbFecPacsContributionsFromOtherCommittees, searchDbFecPacsTransFromAffiliates, searchDbFecPacsContributionsToOtherCommittee, searchDbFecPacsContributionsFromCandidate, searchDbFecPacsLoansFromCandidate, searchDbFecPacsTotalLoansReceived, searchDbFecPacsTotalDistributions, searchDbFecPacsTransfersToAffiliates, searchDbFecPacsRefundsToIndividuals, searchDbFecPacsRefendsToOthercommittees, searchDbFecPacsCandidateLoanRepayments, searchDbFecPacsLoanRepayments)

Search API for &#39;FEC PACs&#39; entry type

API to search for entries of type FEC PACs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TypeFecPacsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geodesystems.com:443");

    TypeFecPacsApi apiInstance = new TypeFecPacsApi(defaultClient);
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
    String searchDbFecPacsCommittee = "searchDbFecPacsCommittee_example"; // String | Committee
    Double searchDbFecPacsTotalReceipts = 3.4D; // Double | Total Receipts
    Double searchDbFecPacsBeginningCash = 3.4D; // Double | Beginning Cash
    Double searchDbFecPacsEndingCash = 3.4D; // Double | Ending Cash
    Double searchDbFecPacsContributionsFromIndividuals = 3.4D; // Double | Contributions From Individuals
    Double searchDbFecPacsContributionsFromOtherCommittees = 3.4D; // Double | Contributions From Other Committees
    Double searchDbFecPacsTransFromAffiliates = 3.4D; // Double | Trans From Affiliates
    Double searchDbFecPacsContributionsToOtherCommittee = 3.4D; // Double | Contributions To Other Committee
    Double searchDbFecPacsContributionsFromCandidate = 3.4D; // Double | Contributions From Candidate
    Double searchDbFecPacsLoansFromCandidate = 3.4D; // Double | Loans From Candidate
    Double searchDbFecPacsTotalLoansReceived = 3.4D; // Double | Total Loans Received
    Double searchDbFecPacsTotalDistributions = 3.4D; // Double | Total Distributions
    Double searchDbFecPacsTransfersToAffiliates = 3.4D; // Double | Transfers To Affiliates
    Double searchDbFecPacsRefundsToIndividuals = 3.4D; // Double | Refunds To Individuals
    Double searchDbFecPacsRefendsToOthercommittees = 3.4D; // Double | Refends To Othercommittees
    Double searchDbFecPacsCandidateLoanRepayments = 3.4D; // Double | Candidate Loan Repayments
    Double searchDbFecPacsLoanRepayments = 3.4D; // Double | Loan Repayments
    try {
      apiInstance.searchFecPacs(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbFecPacsCommittee, searchDbFecPacsTotalReceipts, searchDbFecPacsBeginningCash, searchDbFecPacsEndingCash, searchDbFecPacsContributionsFromIndividuals, searchDbFecPacsContributionsFromOtherCommittees, searchDbFecPacsTransFromAffiliates, searchDbFecPacsContributionsToOtherCommittee, searchDbFecPacsContributionsFromCandidate, searchDbFecPacsLoansFromCandidate, searchDbFecPacsTotalLoansReceived, searchDbFecPacsTotalDistributions, searchDbFecPacsTransfersToAffiliates, searchDbFecPacsRefundsToIndividuals, searchDbFecPacsRefendsToOthercommittees, searchDbFecPacsCandidateLoanRepayments, searchDbFecPacsLoanRepayments);
    } catch (ApiException e) {
      System.err.println("Exception when calling TypeFecPacsApi#searchFecPacs");
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
| **searchDbFecPacsCommittee** | **String**| Committee | [optional] |
| **searchDbFecPacsTotalReceipts** | **Double**| Total Receipts | [optional] |
| **searchDbFecPacsBeginningCash** | **Double**| Beginning Cash | [optional] |
| **searchDbFecPacsEndingCash** | **Double**| Ending Cash | [optional] |
| **searchDbFecPacsContributionsFromIndividuals** | **Double**| Contributions From Individuals | [optional] |
| **searchDbFecPacsContributionsFromOtherCommittees** | **Double**| Contributions From Other Committees | [optional] |
| **searchDbFecPacsTransFromAffiliates** | **Double**| Trans From Affiliates | [optional] |
| **searchDbFecPacsContributionsToOtherCommittee** | **Double**| Contributions To Other Committee | [optional] |
| **searchDbFecPacsContributionsFromCandidate** | **Double**| Contributions From Candidate | [optional] |
| **searchDbFecPacsLoansFromCandidate** | **Double**| Loans From Candidate | [optional] |
| **searchDbFecPacsTotalLoansReceived** | **Double**| Total Loans Received | [optional] |
| **searchDbFecPacsTotalDistributions** | **Double**| Total Distributions | [optional] |
| **searchDbFecPacsTransfersToAffiliates** | **Double**| Transfers To Affiliates | [optional] |
| **searchDbFecPacsRefundsToIndividuals** | **Double**| Refunds To Individuals | [optional] |
| **searchDbFecPacsRefendsToOthercommittees** | **Double**| Refends To Othercommittees | [optional] |
| **searchDbFecPacsCandidateLoanRepayments** | **Double**| Candidate Loan Repayments | [optional] |
| **searchDbFecPacsLoanRepayments** | **Double**| Loan Repayments | [optional] |

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

