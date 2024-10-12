# IndependentExpendituresApi

All URIs are relative to */v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**schedulesScheduleEByCandidateGet**](IndependentExpendituresApi.md#schedulesScheduleEByCandidateGet) | **GET** /schedules/schedule_e/by_candidate/ |  |
| [**schedulesScheduleEEfileGet**](IndependentExpendituresApi.md#schedulesScheduleEEfileGet) | **GET** /schedules/schedule_e/efile/ |  |
| [**schedulesScheduleEGet**](IndependentExpendituresApi.md#schedulesScheduleEGet) | **GET** /schedules/schedule_e/ |  |
| [**schedulesScheduleETotalsByCandidateGet**](IndependentExpendituresApi.md#schedulesScheduleETotalsByCandidateGet) | **GET** /schedules/schedule_e/totals/by_candidate/ |  |


<a id="schedulesScheduleEByCandidateGet"></a>
# **schedulesScheduleEByCandidateGet**
> ScheduleEByCandidatePage schedulesScheduleEByCandidateGet(apiKey, district, supportOppose, electionFull, cycle, sortNullOnly, page, state, committeeId, sortNullsLast, sortHideNull, candidateId, perPage, office, sort)



 Schedule E receipts aggregated by recipient candidate. To avoid double counting, memoed items are not included. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndependentExpendituresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");
    
    // Configure API key authorization: ApiKeyHeaderAuth
    ApiKeyAuth ApiKeyHeaderAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyHeaderAuth");
    ApiKeyHeaderAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyHeaderAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: ApiKeyQueryAuth
    ApiKeyAuth ApiKeyQueryAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyQueryAuth");
    ApiKeyQueryAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyQueryAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    IndependentExpendituresApi apiInstance = new IndependentExpendituresApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    String district = "district_example"; // String | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    String supportOppose = "S"; // String | Support or opposition
    Boolean electionFull = true; // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    String state = "state_example"; // String | US state or territory where a candidate runs for office
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    List<String> candidateId = Arrays.asList(); // List<String> |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String office = "house"; // String | Federal office candidate runs for: H, S or P
    String sort = "sort_example"; // String | Provide a field to sort by. Use `-` for descending order. 
    try {
      ScheduleEByCandidatePage result = apiInstance.schedulesScheduleEByCandidateGet(apiKey, district, supportOppose, electionFull, cycle, sortNullOnly, page, state, committeeId, sortNullsLast, sortHideNull, candidateId, perPage, office, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndependentExpendituresApi#schedulesScheduleEByCandidateGet");
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
| **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY] |
| **district** | **String**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] |
| **supportOppose** | **String**| Support or opposition | [optional] [enum: S, O] |
| **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true] |
| **cycle** | [**List&lt;Integer&gt;**](Integer.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **state** | **String**| US state or territory where a candidate runs for office | [optional] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **candidateId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **office** | **String**| Federal office candidate runs for: H, S or P | [optional] [enum: house, senate, president] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] |

### Return type

[**ScheduleEByCandidatePage**](ScheduleEByCandidatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleEEfileGet"></a>
# **schedulesScheduleEEfileGet**
> ScheduleEEfilePage schedulesScheduleEEfileGet(apiKey, maxExpenditureAmount, supportOpposeIndicator, minExpenditureDate, filingForm, maxExpenditureDate, maxFiledDate, isNotice, sortNullOnly, sortHideNull, payeeName, candidateId, perPage, candidateOfficeDistrict, sort, minExpenditureAmount, spenderName, minDisseminationDate, candidateOfficeState, sortNullsLast, page, committeeId, candidateSearch, imageNumber, candidateParty, minFiledDate, maxDisseminationDate, mostRecent, candidateOffice)



 Efiling endpoints provide real-time campaign finance data received from electronic filers. Efiling endpoints only contain the most recent four months of data and don&#39;t contain the processed and coded data that you can find on other endpoints. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndependentExpendituresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");
    
    // Configure API key authorization: ApiKeyHeaderAuth
    ApiKeyAuth ApiKeyHeaderAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyHeaderAuth");
    ApiKeyHeaderAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyHeaderAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: ApiKeyQueryAuth
    ApiKeyAuth ApiKeyQueryAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyQueryAuth");
    ApiKeyQueryAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyQueryAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    IndependentExpendituresApi apiInstance = new IndependentExpendituresApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    Integer maxExpenditureAmount = 56; // Integer | Selects all items expended by this committee less than this amount
    List<String> supportOpposeIndicator = Arrays.asList(); // List<String> | Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs.
    LocalDate minExpenditureDate = LocalDate.now(); // LocalDate | Selects all items expended by this committee after this date
    List<String> filingForm = Arrays.asList(); // List<String> | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information 
    LocalDate maxExpenditureDate = LocalDate.now(); // LocalDate | Selects all items expended by this committee before this date
    LocalDate maxFiledDate = LocalDate.now(); // LocalDate | Timestamp of electronic or paper record that FEC received
    Boolean isNotice = true; // Boolean |  Record filed as 24- or 48-hour notice. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    List<String> payeeName = Arrays.asList(); // List<String> |  Name of the entity that received the payment. 
    List<String> candidateId = Arrays.asList(); // List<String> |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    List<String> candidateOfficeDistrict = Arrays.asList(); // List<String> | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    String sort = "-expenditure_date"; // String | Provide a field to sort by. Use `-` for descending order. 
    Integer minExpenditureAmount = 56; // Integer | Selects all items expended by this committee greater than this amount
    List<String> spenderName = Arrays.asList(); // List<String> | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records.
    LocalDate minDisseminationDate = LocalDate.now(); // LocalDate | Selects all items distributed by this committee after this date
    List<String> candidateOfficeState = Arrays.asList(); // List<String> | US state or territory where a candidate runs for office
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    List<String> candidateSearch = Arrays.asList(); // List<String> |  Search for candidates by candiate id or candidate first or last name 
    List<String> imageNumber = Arrays.asList(); // List<String> |  An unique identifier for each page where the electronic or paper filing is reported. 
    List<String> candidateParty = Arrays.asList(); // List<String> | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
    LocalDate minFiledDate = LocalDate.now(); // LocalDate | Timestamp of electronic or paper record that FEC received
    LocalDate maxDisseminationDate = LocalDate.now(); // LocalDate | Selects all items distributed by this committee before this date
    Boolean mostRecent = true; // Boolean |  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (`null`) is always included. 
    String candidateOffice = ""; // String | Federal office candidate runs for: H, S or P
    try {
      ScheduleEEfilePage result = apiInstance.schedulesScheduleEEfileGet(apiKey, maxExpenditureAmount, supportOpposeIndicator, minExpenditureDate, filingForm, maxExpenditureDate, maxFiledDate, isNotice, sortNullOnly, sortHideNull, payeeName, candidateId, perPage, candidateOfficeDistrict, sort, minExpenditureAmount, spenderName, minDisseminationDate, candidateOfficeState, sortNullsLast, page, committeeId, candidateSearch, imageNumber, candidateParty, minFiledDate, maxDisseminationDate, mostRecent, candidateOffice);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndependentExpendituresApi#schedulesScheduleEEfileGet");
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
| **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY] |
| **maxExpenditureAmount** | **Integer**| Selects all items expended by this committee less than this amount | [optional] |
| **supportOpposeIndicator** | [**List&lt;String&gt;**](String.md)| Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs. | [optional] [enum: S, O] |
| **minExpenditureDate** | **LocalDate**| Selects all items expended by this committee after this date | [optional] |
| **filingForm** | [**List&lt;String&gt;**](String.md)| The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional] |
| **maxExpenditureDate** | **LocalDate**| Selects all items expended by this committee before this date | [optional] |
| **maxFiledDate** | **LocalDate**| Timestamp of electronic or paper record that FEC received | [optional] |
| **isNotice** | **Boolean**|  Record filed as 24- or 48-hour notice.  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **payeeName** | [**List&lt;String&gt;**](String.md)|  Name of the entity that received the payment.  | [optional] |
| **candidateId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **candidateOfficeDistrict** | [**List&lt;String&gt;**](String.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -expenditure_date] |
| **minExpenditureAmount** | **Integer**| Selects all items expended by this committee greater than this amount | [optional] |
| **spenderName** | [**List&lt;String&gt;**](String.md)| The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] |
| **minDisseminationDate** | **LocalDate**| Selects all items distributed by this committee after this date | [optional] |
| **candidateOfficeState** | [**List&lt;String&gt;**](String.md)| US state or territory where a candidate runs for office | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **candidateSearch** | [**List&lt;String&gt;**](String.md)|  Search for candidates by candiate id or candidate first or last name  | [optional] |
| **imageNumber** | [**List&lt;String&gt;**](String.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] |
| **candidateParty** | [**List&lt;String&gt;**](String.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] |
| **minFiledDate** | **LocalDate**| Timestamp of electronic or paper record that FEC received | [optional] |
| **maxDisseminationDate** | **LocalDate**| Selects all items distributed by this committee before this date | [optional] |
| **mostRecent** | **Boolean**|  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (&#x60;null&#x60;) is always included.  | [optional] |
| **candidateOffice** | **String**| Federal office candidate runs for: H, S or P | [optional] [enum: , H, S, P] |

### Return type

[**ScheduleEEfilePage**](ScheduleEEfilePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleEGet"></a>
# **schedulesScheduleEGet**
> ScheduleEPage schedulesScheduleEGet(apiKey, lastExpenditureDate, maxImageNumber, isNotice, payeeName, minAmount, candidateId, sortHideNull, lastOfficeTotalYtd, sort, minFilingDate, qSpender, minDisseminationDate, candidateOfficeState, sortNullsLast, lastExpenditureAmount, imageNumber, maxDate, maxDisseminationDate, minDate, filingForm, supportOpposeIndicator, minImageNumber, cycle, maxFilingDate, sortNullOnly, lastSupportOpposeIndicator, lastIndex, perPage, candidateOfficeDistrict, lineNumber, committeeId, candidateParty, maxAmount, mostRecent, candidateOffice)



 Schedule E covers the line item expenditures for independent expenditures. For example, if a super PAC bought ads on TV to oppose a federal candidate, each ad purchase would be recorded here with the expenditure amount, name and id of the candidate, and whether the ad supported or opposed the candidate.  An independent expenditure is an expenditure for a communication \&quot;expressly advocating the election or defeat of a clearly identified candidate that is not made in cooperation, consultation, or concert with, or at the request or suggestion of, a candidate, a candidate’s authorized committee, or their agents, or a political party or its agents.\&quot;  Aggregates by candidate do not include 24 and 48 hour reports. This ensures we don&#39;t double count expenditures and the totals are more accurate. You can still find the information from 24 and 48 hour reports in &#x60;/schedule/schedule_e/&#x60;.  Due to the large quantity of Schedule E filings, this endpoint is not paginated by page number. Instead, you can request the next page of results by adding the values in the &#x60;last_indexes&#x60; object from &#x60;pagination&#x60; to the URL of your last request. For example, when sorting by &#x60;expenditure_amount&#x60;, you might receive a page of results with the following pagination information:  &#x60;&#x60;&#x60;  \&quot;pagination\&quot;: {     \&quot;count\&quot;: 152623,     \&quot;last_indexes\&quot;: {       \&quot;last_index\&quot;: \&quot;3023037\&quot;,       \&quot;last_expenditure_amount\&quot;: -17348.5     },     \&quot;per_page\&quot;: 20,     \&quot;pages\&quot;: 7632   } } &#x60;&#x60;&#x60;  To fetch the next page of sorted results, append &#x60;last_index&#x3D;3023037&#x60; and &#x60;last_expenditure_amount&#x3D;&#x60; to the URL.  We strongly advise paging through these results by using the sort indices (defaults to sort by disbursement date, e.g. &#x60;last_disbursement_date&#x60;), otherwise some resources may be unintentionally filtered out.  This resource uses keyset pagination to improve query performance and these indices are required to properly page through this large dataset.  Note: because the Schedule E data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndependentExpendituresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");
    
    // Configure API key authorization: ApiKeyHeaderAuth
    ApiKeyAuth ApiKeyHeaderAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyHeaderAuth");
    ApiKeyHeaderAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyHeaderAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: ApiKeyQueryAuth
    ApiKeyAuth ApiKeyQueryAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyQueryAuth");
    ApiKeyQueryAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyQueryAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    IndependentExpendituresApi apiInstance = new IndependentExpendituresApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    LocalDate lastExpenditureDate = LocalDate.now(); // LocalDate |  When sorting by `expenditure_date`, this is populated with the `expenditure_date` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page. 
    String maxImageNumber = "maxImageNumber_example"; // String | Maxium image number of the page where the schedule item is reported
    List<Boolean> isNotice = Arrays.asList(); // List<Boolean> |  Record filed as 24- or 48-hour notice. 
    List<String> payeeName = Arrays.asList(); // List<String> |  Name of the entity that received the payment. 
    String minAmount = "minAmount_example"; // String | Filter for all amounts greater than a value.
    List<String> candidateId = Arrays.asList(); // List<String> |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Float lastOfficeTotalYtd = 3.4F; // Float |  When sorting by `office_total_ytd`, this is populated with the `office_total_ytd` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page.' 
    String sort = "-expenditure_date"; // String | Provide a field to sort by. Use `-` for descending order. 
    LocalDate minFilingDate = LocalDate.now(); // LocalDate |  Selects all filings received after this date 
    List<String> qSpender = Arrays.asList(); // List<String> |  Keyword search for spender name or ID 
    LocalDate minDisseminationDate = LocalDate.now(); // LocalDate | Selects all items distributed by this committee after this date
    List<String> candidateOfficeState = Arrays.asList(); // List<String> | US state or territory
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Float lastExpenditureAmount = 3.4F; // Float |  When sorting by `expenditure_amount`, this is populated with the `expenditure_amount` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page. 
    List<String> imageNumber = Arrays.asList(); // List<String> |  An unique identifier for each page where the electronic or paper filing is reported. 
    LocalDate maxDate = LocalDate.now(); // LocalDate | Maximum date
    LocalDate maxDisseminationDate = LocalDate.now(); // LocalDate | Selects all items distributed by this committee before this date
    LocalDate minDate = LocalDate.now(); // LocalDate | Minimum date
    List<String> filingForm = Arrays.asList(); // List<String> | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information 
    List<String> supportOpposeIndicator = Arrays.asList(); // List<String> | Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs.
    String minImageNumber = "minImageNumber_example"; // String | Minium image number of the page where the schedule item is reported
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    LocalDate maxFilingDate = LocalDate.now(); // LocalDate |  Selects all filings received before this date 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    String lastSupportOpposeIndicator = "lastSupportOpposeIndicator_example"; // String |  When sorting by `support_oppose_indicator`, this is populated with the `support_oppose_indicator` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page.' 
    Integer lastIndex = 56; // Integer | Index of last result from previous page
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    List<String> candidateOfficeDistrict = Arrays.asList(); // List<String> | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    String lineNumber = "lineNumber_example"; // String | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    List<String> candidateParty = Arrays.asList(); // List<String> | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
    String maxAmount = "maxAmount_example"; // String | Filter for all amounts less than a value.
    Boolean mostRecent = true; // Boolean |  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (`null`) is always included. 
    List<String> candidateOffice = Arrays.asList(); // List<String> | Federal office candidate runs for: H, S or P
    try {
      ScheduleEPage result = apiInstance.schedulesScheduleEGet(apiKey, lastExpenditureDate, maxImageNumber, isNotice, payeeName, minAmount, candidateId, sortHideNull, lastOfficeTotalYtd, sort, minFilingDate, qSpender, minDisseminationDate, candidateOfficeState, sortNullsLast, lastExpenditureAmount, imageNumber, maxDate, maxDisseminationDate, minDate, filingForm, supportOpposeIndicator, minImageNumber, cycle, maxFilingDate, sortNullOnly, lastSupportOpposeIndicator, lastIndex, perPage, candidateOfficeDistrict, lineNumber, committeeId, candidateParty, maxAmount, mostRecent, candidateOffice);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndependentExpendituresApi#schedulesScheduleEGet");
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
| **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY] |
| **lastExpenditureDate** | **LocalDate**|  When sorting by &#x60;expenditure_date&#x60;, this is populated with the &#x60;expenditure_date&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.  | [optional] |
| **maxImageNumber** | **String**| Maxium image number of the page where the schedule item is reported | [optional] |
| **isNotice** | [**List&lt;Boolean&gt;**](Boolean.md)|  Record filed as 24- or 48-hour notice.  | [optional] |
| **payeeName** | [**List&lt;String&gt;**](String.md)|  Name of the entity that received the payment.  | [optional] |
| **minAmount** | **String**| Filter for all amounts greater than a value. | [optional] |
| **candidateId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **lastOfficeTotalYtd** | **Float**|  When sorting by &#x60;office_total_ytd&#x60;, this is populated with the &#x60;office_total_ytd&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.&#39;  | [optional] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -expenditure_date] |
| **minFilingDate** | **LocalDate**|  Selects all filings received after this date  | [optional] |
| **qSpender** | [**List&lt;String&gt;**](String.md)|  Keyword search for spender name or ID  | [optional] |
| **minDisseminationDate** | **LocalDate**| Selects all items distributed by this committee after this date | [optional] |
| **candidateOfficeState** | [**List&lt;String&gt;**](String.md)| US state or territory | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **lastExpenditureAmount** | **Float**|  When sorting by &#x60;expenditure_amount&#x60;, this is populated with the &#x60;expenditure_amount&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.  | [optional] |
| **imageNumber** | [**List&lt;String&gt;**](String.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] |
| **maxDate** | **LocalDate**| Maximum date | [optional] |
| **maxDisseminationDate** | **LocalDate**| Selects all items distributed by this committee before this date | [optional] |
| **minDate** | **LocalDate**| Minimum date | [optional] |
| **filingForm** | [**List&lt;String&gt;**](String.md)| The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional] |
| **supportOpposeIndicator** | [**List&lt;String&gt;**](String.md)| Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs. | [optional] [enum: S, O] |
| **minImageNumber** | **String**| Minium image number of the page where the schedule item is reported | [optional] |
| **cycle** | [**List&lt;Integer&gt;**](Integer.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] |
| **maxFilingDate** | **LocalDate**|  Selects all filings received before this date  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **lastSupportOpposeIndicator** | **String**|  When sorting by &#x60;support_oppose_indicator&#x60;, this is populated with the &#x60;support_oppose_indicator&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.&#39;  | [optional] |
| **lastIndex** | **Integer**| Index of last result from previous page | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **candidateOfficeDistrict** | [**List&lt;String&gt;**](String.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] |
| **lineNumber** | **String**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **candidateParty** | [**List&lt;String&gt;**](String.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] |
| **maxAmount** | **String**| Filter for all amounts less than a value. | [optional] |
| **mostRecent** | **Boolean**|  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (&#x60;null&#x60;) is always included.  | [optional] |
| **candidateOffice** | [**List&lt;String&gt;**](String.md)| Federal office candidate runs for: H, S or P | [optional] [enum: , H, S, P] |

### Return type

[**ScheduleEPage**](ScheduleEPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleETotalsByCandidateGet"></a>
# **schedulesScheduleETotalsByCandidateGet**
> IETotalsByCandidatePage schedulesScheduleETotalsByCandidateGet(apiKey, electionFull, cycle, sortNullsLast, page, sortNullOnly, sortHideNull, candidateId, perPage, sort)



 Total independent expenditure on supported or opposed candidates by cycle or candidate election year. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndependentExpendituresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");
    
    // Configure API key authorization: ApiKeyHeaderAuth
    ApiKeyAuth ApiKeyHeaderAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyHeaderAuth");
    ApiKeyHeaderAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyHeaderAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: ApiKeyQueryAuth
    ApiKeyAuth ApiKeyQueryAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyQueryAuth");
    ApiKeyQueryAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyQueryAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    IndependentExpendituresApi apiInstance = new IndependentExpendituresApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    Boolean electionFull = true; // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    List<String> candidateId = Arrays.asList(); // List<String> |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String sort = "sort_example"; // String | Provide a field to sort by. Use `-` for descending order. 
    try {
      IETotalsByCandidatePage result = apiInstance.schedulesScheduleETotalsByCandidateGet(apiKey, electionFull, cycle, sortNullsLast, page, sortNullOnly, sortHideNull, candidateId, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndependentExpendituresApi#schedulesScheduleETotalsByCandidateGet");
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
| **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY] |
| **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true] |
| **cycle** | [**List&lt;Integer&gt;**](Integer.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **candidateId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] |

### Return type

[**IETotalsByCandidatePage**](IETotalsByCandidatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

