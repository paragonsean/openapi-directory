# CandidateApi

All URIs are relative to */v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**candidateCandidateIdGet**](CandidateApi.md#candidateCandidateIdGet) | **GET** /candidate/{candidate_id}/ |  |
| [**candidateCandidateIdHistoryCycleGet**](CandidateApi.md#candidateCandidateIdHistoryCycleGet) | **GET** /candidate/{candidate_id}/history/{cycle}/ |  |
| [**candidateCandidateIdHistoryGet**](CandidateApi.md#candidateCandidateIdHistoryGet) | **GET** /candidate/{candidate_id}/history/ |  |
| [**candidateCandidateIdTotalsGet**](CandidateApi.md#candidateCandidateIdTotalsGet) | **GET** /candidate/{candidate_id}/totals/ |  |
| [**candidatesGet**](CandidateApi.md#candidatesGet) | **GET** /candidates/ |  |
| [**candidatesSearchGet**](CandidateApi.md#candidatesSearchGet) | **GET** /candidates/search/ |  |
| [**candidatesTotalsAggregatesGet**](CandidateApi.md#candidatesTotalsAggregatesGet) | **GET** /candidates/totals/aggregates/ |  |
| [**candidatesTotalsByOfficeByPartyGet**](CandidateApi.md#candidatesTotalsByOfficeByPartyGet) | **GET** /candidates/totals/by_office/by_party/ |  |
| [**candidatesTotalsByOfficeGet**](CandidateApi.md#candidatesTotalsByOfficeGet) | **GET** /candidates/totals/by_office/ |  |
| [**candidatesTotalsGet**](CandidateApi.md#candidatesTotalsGet) | **GET** /candidates/totals/ |  |
| [**committeeCommitteeIdCandidatesGet**](CandidateApi.md#committeeCommitteeIdCandidatesGet) | **GET** /committee/{committee_id}/candidates/ |  |
| [**committeeCommitteeIdCandidatesHistoryCycleGet**](CandidateApi.md#committeeCommitteeIdCandidatesHistoryCycleGet) | **GET** /committee/{committee_id}/candidates/history/{cycle}/ |  |
| [**committeeCommitteeIdCandidatesHistoryGet**](CandidateApi.md#committeeCommitteeIdCandidatesHistoryGet) | **GET** /committee/{committee_id}/candidates/history/ |  |


<a id="candidateCandidateIdGet"></a>
# **candidateCandidateIdGet**
> CandidateDetailPage candidateCandidateIdGet(apiKey, candidateId, incumbentChallenge, cycle, sortNullOnly, federalFundsFlag, sortHideNull, name, perPage, electionYear, office, sort, candidateStatus, district, hasRaisedFunds, party, sortNullsLast, page, state, year)



 This endpoint is useful for finding detailed information about a particular candidate. Use the &#x60;candidate_id&#x60; to find the most recent information about that candidate. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CandidateApi;

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

    CandidateApi apiInstance = new CandidateApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    String candidateId = "candidateId_example"; // String |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
    List<String> incumbentChallenge = Arrays.asList(); // List<String> | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open.
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Boolean federalFundsFlag = true; // Boolean | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates.
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    List<String> name = Arrays.asList(); // List<String> | Name (candidate or committee) to search for. Alias for 'q'.
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    List<Integer> electionYear = Arrays.asList(); // List<Integer> | Year of election
    List<String> office = Arrays.asList(); // List<String> | Federal office candidate runs for: H, S or P
    String sort = "name"; // String | Provide a field to sort by. Use `-` for descending order. 
    List<String> candidateStatus = Arrays.asList(); // List<String> | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate 
    List<String> district = Arrays.asList(); // List<String> | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    Boolean hasRaisedFunds = true; // Boolean | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.)
    List<String> party = Arrays.asList(); // List<String> | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> state = Arrays.asList(); // List<String> | US state or territory where a candidate runs for office
    String year = "year_example"; // String | Retrieve records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year.
    try {
      CandidateDetailPage result = apiInstance.candidateCandidateIdGet(apiKey, candidateId, incumbentChallenge, cycle, sortNullOnly, federalFundsFlag, sortHideNull, name, perPage, electionYear, office, sort, candidateStatus, district, hasRaisedFunds, party, sortNullsLast, page, state, year);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CandidateApi#candidateCandidateIdGet");
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
| **candidateId** | **String**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | |
| **incumbentChallenge** | [**List&lt;String&gt;**](String.md)| One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional] [enum: , I, C, O] |
| **cycle** | [**List&lt;Integer&gt;**](Integer.md)|  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **federalFundsFlag** | **Boolean**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **name** | [**List&lt;String&gt;**](String.md)| Name (candidate or committee) to search for. Alias for &#39;q&#39;. | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **electionYear** | [**List&lt;Integer&gt;**](Integer.md)| Year of election | [optional] |
| **office** | [**List&lt;String&gt;**](String.md)| Federal office candidate runs for: H, S or P | [optional] [enum: , H, S, P] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to name] |
| **candidateStatus** | [**List&lt;String&gt;**](String.md)| One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional] [enum: , C, F, N, P] |
| **district** | [**List&lt;String&gt;**](String.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] |
| **hasRaisedFunds** | **Boolean**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional] |
| **party** | [**List&lt;String&gt;**](String.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **state** | [**List&lt;String&gt;**](String.md)| US state or territory where a candidate runs for office | [optional] |
| **year** | **String**| Retrieve records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. | [optional] |

### Return type

[**CandidateDetailPage**](CandidateDetailPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="candidateCandidateIdHistoryCycleGet"></a>
# **candidateCandidateIdHistoryCycleGet**
> CandidateHistoryPage candidateCandidateIdHistoryCycleGet(apiKey, cycle, candidateId, page, sortHideNull, electionFull, perPage, sortNullOnly, sort, sortNullsLast)



 Find out a candidate&#39;s characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate&#39;s previous races.  This information is organized by &#x60;candidate_id&#x60;, so it won&#39;t help you find a candidate who ran for different offices over time; candidates get a new ID for each office. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CandidateApi;

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

    CandidateApi apiInstance = new CandidateApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    Integer cycle = 56; // Integer |  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag. 
    String candidateId = "candidateId_example"; // String |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Boolean electionFull = true; // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    String sort = "-two_year_period"; // String | Provide a field to sort by. Use `-` for descending order. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    try {
      CandidateHistoryPage result = apiInstance.candidateCandidateIdHistoryCycleGet(apiKey, cycle, candidateId, page, sortHideNull, electionFull, perPage, sortNullOnly, sort, sortNullsLast);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CandidateApi#candidateCandidateIdHistoryCycleGet");
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
| **cycle** | **Integer**|  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | |
| **candidateId** | **String**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -two_year_period] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |

### Return type

[**CandidateHistoryPage**](CandidateHistoryPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="candidateCandidateIdHistoryGet"></a>
# **candidateCandidateIdHistoryGet**
> CandidateHistoryPage candidateCandidateIdHistoryGet(apiKey, candidateId, page, sortHideNull, electionFull, perPage, sortNullOnly, sort, sortNullsLast)



 Find out a candidate&#39;s characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate&#39;s previous races.  This information is organized by &#x60;candidate_id&#x60;, so it won&#39;t help you find a candidate who ran for different offices over time; candidates get a new ID for each office. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CandidateApi;

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

    CandidateApi apiInstance = new CandidateApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    String candidateId = "candidateId_example"; // String |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Boolean electionFull = true; // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    String sort = "-two_year_period"; // String | Provide a field to sort by. Use `-` for descending order. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    try {
      CandidateHistoryPage result = apiInstance.candidateCandidateIdHistoryGet(apiKey, candidateId, page, sortHideNull, electionFull, perPage, sortNullOnly, sort, sortNullsLast);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CandidateApi#candidateCandidateIdHistoryGet");
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
| **candidateId** | **String**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -two_year_period] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |

### Return type

[**CandidateHistoryPage**](CandidateHistoryPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="candidateCandidateIdTotalsGet"></a>
# **candidateCandidateIdTotalsGet**
> CommitteeTotalsPage candidateCandidateIdTotalsGet(apiKey, candidateId, electionFull, cycle, sortNullsLast, page, sortNullOnly, sortHideNull, perPage, sort)



 This endpoint provides information about a committee&#39;s Form 3, Form 3X, or Form 3P financial reports, which are aggregated by two-year period. We refer to two-year periods as a &#x60;cycle&#x60;.  The cycle is named after the even-numbered year and includes the year before it. To obtain totals from 2013 and 2014, you would use 2014. In odd-numbered years, the current cycle is the next year — for example, in 2015, the current cycle is 2016.  For presidential and Senate candidates, multiple two-year cycles exist between elections.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CandidateApi;

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

    CandidateApi apiInstance = new CandidateApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    String candidateId = "candidateId_example"; // String |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
    Boolean electionFull = true; // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String sort = "-cycle"; // String | Provide a field to sort by. Use `-` for descending order. 
    try {
      CommitteeTotalsPage result = apiInstance.candidateCandidateIdTotalsGet(apiKey, candidateId, electionFull, cycle, sortNullsLast, page, sortNullOnly, sortHideNull, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CandidateApi#candidateCandidateIdTotalsGet");
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
| **candidateId** | **String**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | |
| **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] |
| **cycle** | [**List&lt;Integer&gt;**](Integer.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -cycle] |

### Return type

[**CommitteeTotalsPage**](CommitteeTotalsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="candidatesGet"></a>
# **candidatesGet**
> CandidatePage candidatesGet(apiKey, incumbentChallenge, minFirstFileDate, q, cycle, sortNullOnly, federalFundsFlag, sortHideNull, candidateId, name, perPage, electionYear, office, sort, candidateStatus, maxFirstFileDate, district, hasRaisedFunds, party, sortNullsLast, isActiveCandidate, page, state, year)



 Fetch basic information about candidates, and use parameters to filter results to the candidates you&#39;re looking for.  Each result reflects a unique FEC candidate ID. That ID is particular to the candidate for a particular office sought. If a candidate runs for the same office multiple times, the ID stays the same. If the same person runs for another office — for example, a House candidate runs for a Senate office — that candidate will get a unique ID for each office. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CandidateApi;

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

    CandidateApi apiInstance = new CandidateApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    List<String> incumbentChallenge = Arrays.asList(); // List<String> | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open.
    LocalDate minFirstFileDate = LocalDate.now(); // LocalDate | Selects all candidates whose first filing was received by the FEC after this date.
    List<String> q = Arrays.asList(); // List<String> | Name of candidate running for office
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Boolean federalFundsFlag = true; // Boolean | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates.
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    List<String> candidateId = Arrays.asList(); // List<String> |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
    List<String> name = Arrays.asList(); // List<String> | Name (candidate or committee) to search for. Alias for 'q'.
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    List<Integer> electionYear = Arrays.asList(); // List<Integer> | Year of election
    List<String> office = Arrays.asList(); // List<String> | Federal office candidate runs for: H, S or P
    String sort = "name"; // String | Provide a field to sort by. Use `-` for descending order. 
    List<String> candidateStatus = Arrays.asList(); // List<String> | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate 
    LocalDate maxFirstFileDate = LocalDate.now(); // LocalDate | Selects all candidates whose first filing was received by the FEC before this date.
    List<String> district = Arrays.asList(); // List<String> | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    Boolean hasRaisedFunds = true; // Boolean | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.)
    List<String> party = Arrays.asList(); // List<String> | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Boolean isActiveCandidate = true; // Boolean |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned. 
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> state = Arrays.asList(); // List<String> | US state or territory where a candidate runs for office
    String year = "year_example"; // String | Retrieve records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year.
    try {
      CandidatePage result = apiInstance.candidatesGet(apiKey, incumbentChallenge, minFirstFileDate, q, cycle, sortNullOnly, federalFundsFlag, sortHideNull, candidateId, name, perPage, electionYear, office, sort, candidateStatus, maxFirstFileDate, district, hasRaisedFunds, party, sortNullsLast, isActiveCandidate, page, state, year);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CandidateApi#candidatesGet");
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
| **incumbentChallenge** | [**List&lt;String&gt;**](String.md)| One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional] [enum: , I, C, O] |
| **minFirstFileDate** | **LocalDate**| Selects all candidates whose first filing was received by the FEC after this date. | [optional] |
| **q** | [**List&lt;String&gt;**](String.md)| Name of candidate running for office | [optional] |
| **cycle** | [**List&lt;Integer&gt;**](Integer.md)|  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **federalFundsFlag** | **Boolean**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **candidateId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] |
| **name** | [**List&lt;String&gt;**](String.md)| Name (candidate or committee) to search for. Alias for &#39;q&#39;. | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **electionYear** | [**List&lt;Integer&gt;**](Integer.md)| Year of election | [optional] |
| **office** | [**List&lt;String&gt;**](String.md)| Federal office candidate runs for: H, S or P | [optional] [enum: , H, S, P] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to name] |
| **candidateStatus** | [**List&lt;String&gt;**](String.md)| One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional] [enum: , C, F, N, P] |
| **maxFirstFileDate** | **LocalDate**| Selects all candidates whose first filing was received by the FEC before this date. | [optional] |
| **district** | [**List&lt;String&gt;**](String.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] |
| **hasRaisedFunds** | **Boolean**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional] |
| **party** | [**List&lt;String&gt;**](String.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **isActiveCandidate** | **Boolean**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **state** | [**List&lt;String&gt;**](String.md)| US state or territory where a candidate runs for office | [optional] |
| **year** | **String**| Retrieve records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. | [optional] |

### Return type

[**CandidatePage**](CandidatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="candidatesSearchGet"></a>
# **candidatesSearchGet**
> CandidatePage candidatesSearchGet(apiKey, incumbentChallenge, minFirstFileDate, q, cycle, sortNullOnly, federalFundsFlag, sortHideNull, candidateId, name, perPage, electionYear, office, sort, candidateStatus, maxFirstFileDate, district, hasRaisedFunds, party, sortNullsLast, isActiveCandidate, page, state, year)



 Fetch basic information about candidates and their principal committees.  Each result reflects a unique FEC candidate ID. That ID is assigned to the candidate for a particular office sought. If a candidate runs for the same office over time, that ID stays the same. If the same person runs for multiple offices — for example, a House candidate runs for a Senate office — that candidate will get a unique ID for each office.  The candidate endpoints primarily use data from FEC registration [Form 1](https://www.fec.gov/pdf/forms/fecfrm1.pdf) for committee information and [Form 2](https://www.fec.gov/pdf/forms/fecfrm2.pdf) for candidate information. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CandidateApi;

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

    CandidateApi apiInstance = new CandidateApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    List<String> incumbentChallenge = Arrays.asList(); // List<String> | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open.
    LocalDate minFirstFileDate = LocalDate.now(); // LocalDate | Selects all candidates whose first filing was received by the FEC after this date.
    List<String> q = Arrays.asList(); // List<String> | Name of candidate running for office
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Boolean federalFundsFlag = true; // Boolean | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates.
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    List<String> candidateId = Arrays.asList(); // List<String> |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
    List<String> name = Arrays.asList(); // List<String> | Name (candidate or committee) to search for. Alias for 'q'.
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    List<Integer> electionYear = Arrays.asList(); // List<Integer> | Year of election
    List<String> office = Arrays.asList(); // List<String> | Federal office candidate runs for: H, S or P
    String sort = "name"; // String | Provide a field to sort by. Use `-` for descending order. 
    List<String> candidateStatus = Arrays.asList(); // List<String> | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate 
    LocalDate maxFirstFileDate = LocalDate.now(); // LocalDate | Selects all candidates whose first filing was received by the FEC before this date.
    List<String> district = Arrays.asList(); // List<String> | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    Boolean hasRaisedFunds = true; // Boolean | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.)
    List<String> party = Arrays.asList(); // List<String> | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Boolean isActiveCandidate = true; // Boolean |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned. 
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> state = Arrays.asList(); // List<String> | US state or territory where a candidate runs for office
    String year = "year_example"; // String | Retrieve records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year.
    try {
      CandidatePage result = apiInstance.candidatesSearchGet(apiKey, incumbentChallenge, minFirstFileDate, q, cycle, sortNullOnly, federalFundsFlag, sortHideNull, candidateId, name, perPage, electionYear, office, sort, candidateStatus, maxFirstFileDate, district, hasRaisedFunds, party, sortNullsLast, isActiveCandidate, page, state, year);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CandidateApi#candidatesSearchGet");
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
| **incumbentChallenge** | [**List&lt;String&gt;**](String.md)| One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional] [enum: , I, C, O] |
| **minFirstFileDate** | **LocalDate**| Selects all candidates whose first filing was received by the FEC after this date. | [optional] |
| **q** | [**List&lt;String&gt;**](String.md)| Name of candidate running for office | [optional] |
| **cycle** | [**List&lt;Integer&gt;**](Integer.md)|  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **federalFundsFlag** | **Boolean**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **candidateId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] |
| **name** | [**List&lt;String&gt;**](String.md)| Name (candidate or committee) to search for. Alias for &#39;q&#39;. | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **electionYear** | [**List&lt;Integer&gt;**](Integer.md)| Year of election | [optional] |
| **office** | [**List&lt;String&gt;**](String.md)| Federal office candidate runs for: H, S or P | [optional] [enum: , H, S, P] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to name] |
| **candidateStatus** | [**List&lt;String&gt;**](String.md)| One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional] [enum: , C, F, N, P] |
| **maxFirstFileDate** | **LocalDate**| Selects all candidates whose first filing was received by the FEC before this date. | [optional] |
| **district** | [**List&lt;String&gt;**](String.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] |
| **hasRaisedFunds** | **Boolean**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional] |
| **party** | [**List&lt;String&gt;**](String.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **isActiveCandidate** | **Boolean**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **state** | [**List&lt;String&gt;**](String.md)| US state or territory where a candidate runs for office | [optional] |
| **year** | **String**| Retrieve records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. | [optional] |

### Return type

[**CandidatePage**](CandidatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="candidatesTotalsAggregatesGet"></a>
# **candidatesTotalsAggregatesGet**
> CandidateTotalAggregatePage candidatesTotalsAggregatesGet(apiKey, maxElectionCycle, sortNullOnly, sortHideNull, perPage, electionYear, office, sort, minElectionCycle, district, electionFull, party, isActiveCandidate, page, state, sortNullsLast, aggregateBy)



 Candidate total receipts and disbursements aggregated by &#x60;aggregate_by&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CandidateApi;

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

    CandidateApi apiInstance = new CandidateApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    Integer maxElectionCycle = 56; // Integer |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    List<Integer> electionYear = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    String office = ""; // String | Federal office candidate runs for: H, S or P
    List<String> sort = Arrays.asList(); // List<String> |  Provide a field to sort by. Use `-` for descending order. ex: `-case_no` 
    Integer minElectionCycle = 56; // Integer |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year. 
    List<String> district = Arrays.asList(); // List<String> | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    Boolean electionFull = true; // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
    String party = ""; // String | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
    Boolean isActiveCandidate = true; // Boolean |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned. 
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> state = Arrays.asList(); // List<String> | US state or territory where a candidate runs for office
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    String aggregateBy = "office"; // String | Candidate totals aggregate_by (Chose one of dropdown options):         - ' ' grouped by election year         - office grouped by election year, by office         - office-state grouped by election year, by office, by state         - office-state-district grouped by election year, by office, by state, by district         - office-party grouped by election year, by office, by party 
    try {
      CandidateTotalAggregatePage result = apiInstance.candidatesTotalsAggregatesGet(apiKey, maxElectionCycle, sortNullOnly, sortHideNull, perPage, electionYear, office, sort, minElectionCycle, district, electionFull, party, isActiveCandidate, page, state, sortNullsLast, aggregateBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CandidateApi#candidatesTotalsAggregatesGet");
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
| **maxElectionCycle** | **Integer**|  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **electionYear** | [**List&lt;Integer&gt;**](Integer.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] |
| **office** | **String**| Federal office candidate runs for: H, S or P | [optional] [enum: , H, S, P] |
| **sort** | [**List&lt;String&gt;**](String.md)|  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60;  | [optional] |
| **minElectionCycle** | **Integer**|  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | [optional] |
| **district** | [**List&lt;String&gt;**](String.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] |
| **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true] |
| **party** | **String**| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] [enum: , DEM, REP, OTHER] |
| **isActiveCandidate** | **Boolean**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **state** | [**List&lt;String&gt;**](String.md)| US state or territory where a candidate runs for office | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **aggregateBy** | **String**| Candidate totals aggregate_by (Chose one of dropdown options):         - &#39; &#39; grouped by election year         - office grouped by election year, by office         - office-state grouped by election year, by office, by state         - office-state-district grouped by election year, by office, by state, by district         - office-party grouped by election year, by office, by party  | [optional] [enum: office, office-state, office-state-district, office-party] |

### Return type

[**CandidateTotalAggregatePage**](CandidateTotalAggregatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="candidatesTotalsByOfficeByPartyGet"></a>
# **candidatesTotalsByOfficeByPartyGet**
> TotalByOfficeByPartyPage candidatesTotalsByOfficeByPartyGet(apiKey, electionFull, sortNullOnly, page, isActiveCandidate, sortNullsLast, electionYear, sortHideNull, perPage, office, sort)



 Aggregated candidate receipts and disbursements grouped by office by party by cycle. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CandidateApi;

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

    CandidateApi apiInstance = new CandidateApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    Boolean electionFull = true; // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    Boolean isActiveCandidate = true; // Boolean |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    List<Integer> electionYear = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String office = ""; // String | Federal office candidate runs for: H, S or P
    String sort = "sort_example"; // String | Provide a field to sort by. Use `-` for descending order. 
    try {
      TotalByOfficeByPartyPage result = apiInstance.candidatesTotalsByOfficeByPartyGet(apiKey, electionFull, sortNullOnly, page, isActiveCandidate, sortNullsLast, electionYear, sortHideNull, perPage, office, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CandidateApi#candidatesTotalsByOfficeByPartyGet");
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
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **isActiveCandidate** | **Boolean**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **electionYear** | [**List&lt;Integer&gt;**](Integer.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **office** | **String**| Federal office candidate runs for: H, S or P | [optional] [enum: , H, S, P] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] |

### Return type

[**TotalByOfficeByPartyPage**](TotalByOfficeByPartyPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="candidatesTotalsByOfficeGet"></a>
# **candidatesTotalsByOfficeGet**
> TotalByOfficePage candidatesTotalsByOfficeGet(apiKey, maxElectionCycle, electionFull, isActiveCandidate, page, sortNullOnly, sortNullsLast, electionYear, sortHideNull, perPage, office, sort, minElectionCycle)



 Aggregated candidate receipts and disbursements grouped by office by cycle. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CandidateApi;

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

    CandidateApi apiInstance = new CandidateApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    Integer maxElectionCycle = 56; // Integer |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year. 
    Boolean electionFull = true; // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
    Boolean isActiveCandidate = true; // Boolean |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned. 
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    List<Integer> electionYear = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String office = ""; // String | Federal office candidate runs for: H, S or P
    String sort = "sort_example"; // String | Provide a field to sort by. Use `-` for descending order. 
    Integer minElectionCycle = 56; // Integer |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year. 
    try {
      TotalByOfficePage result = apiInstance.candidatesTotalsByOfficeGet(apiKey, maxElectionCycle, electionFull, isActiveCandidate, page, sortNullOnly, sortNullsLast, electionYear, sortHideNull, perPage, office, sort, minElectionCycle);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CandidateApi#candidatesTotalsByOfficeGet");
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
| **maxElectionCycle** | **Integer**|  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | [optional] |
| **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true] |
| **isActiveCandidate** | **Boolean**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **electionYear** | [**List&lt;Integer&gt;**](Integer.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **office** | **String**| Federal office candidate runs for: H, S or P | [optional] [enum: , H, S, P] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] |
| **minElectionCycle** | **Integer**|  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | [optional] |

### Return type

[**TotalByOfficePage**](TotalByOfficePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="candidatesTotalsGet"></a>
# **candidatesTotalsGet**
> CandidateHistoryTotalPage candidatesTotalsGet(apiKey, maxDisbursements, q, cycle, sortNullOnly, maxCashOnHandEndPeriod, maxDebtsOwedByCommittee, minDisbursements, federalFundsFlag, sortHideNull, candidateId, perPage, electionYear, office, sort, district, electionFull, minDebtsOwedByCommittee, maxReceipts, hasRaisedFunds, party, sortNullsLast, isActiveCandidate, page, state, minCashOnHandEndPeriod, minReceipts)



 Aggregated candidate receipts and disbursements grouped by cycle. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CandidateApi;

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

    CandidateApi apiInstance = new CandidateApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    String maxDisbursements = "maxDisbursements_example"; // String | Maximum aggregated disbursements
    List<String> q = Arrays.asList(); // List<String> | Name of candidate running for office
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    String maxCashOnHandEndPeriod = "maxCashOnHandEndPeriod_example"; // String | Maximum cash on hand
    String maxDebtsOwedByCommittee = "maxDebtsOwedByCommittee_example"; // String | Maximum debt
    String minDisbursements = "minDisbursements_example"; // String | Minimum aggregated disbursements
    Boolean federalFundsFlag = true; // Boolean | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates.
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    List<String> candidateId = Arrays.asList(); // List<String> |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    List<Integer> electionYear = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    List<String> office = Arrays.asList(); // List<String> | Federal office candidate runs for: H, S or P
    String sort = "sort_example"; // String | Provide a field to sort by. Use `-` for descending order. 
    List<String> district = Arrays.asList(); // List<String> | District of candidate
    Boolean electionFull = true; // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
    String minDebtsOwedByCommittee = "minDebtsOwedByCommittee_example"; // String | Minimum debt
    String maxReceipts = "maxReceipts_example"; // String | Maximum aggregated receipts
    Boolean hasRaisedFunds = true; // Boolean | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.)
    List<String> party = Arrays.asList(); // List<String> | Three-letter party code
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Boolean isActiveCandidate = true; // Boolean |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned. 
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> state = Arrays.asList(); // List<String> | State of candidate
    String minCashOnHandEndPeriod = "minCashOnHandEndPeriod_example"; // String | Minimum cash on hand
    String minReceipts = "minReceipts_example"; // String | Minimum aggregated receipts
    try {
      CandidateHistoryTotalPage result = apiInstance.candidatesTotalsGet(apiKey, maxDisbursements, q, cycle, sortNullOnly, maxCashOnHandEndPeriod, maxDebtsOwedByCommittee, minDisbursements, federalFundsFlag, sortHideNull, candidateId, perPage, electionYear, office, sort, district, electionFull, minDebtsOwedByCommittee, maxReceipts, hasRaisedFunds, party, sortNullsLast, isActiveCandidate, page, state, minCashOnHandEndPeriod, minReceipts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CandidateApi#candidatesTotalsGet");
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
| **maxDisbursements** | **String**| Maximum aggregated disbursements | [optional] |
| **q** | [**List&lt;String&gt;**](String.md)| Name of candidate running for office | [optional] |
| **cycle** | [**List&lt;Integer&gt;**](Integer.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **maxCashOnHandEndPeriod** | **String**| Maximum cash on hand | [optional] |
| **maxDebtsOwedByCommittee** | **String**| Maximum debt | [optional] |
| **minDisbursements** | **String**| Minimum aggregated disbursements | [optional] |
| **federalFundsFlag** | **Boolean**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **candidateId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **electionYear** | [**List&lt;Integer&gt;**](Integer.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] |
| **office** | [**List&lt;String&gt;**](String.md)| Federal office candidate runs for: H, S or P | [optional] [enum: , H, S, P] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] |
| **district** | [**List&lt;String&gt;**](String.md)| District of candidate | [optional] |
| **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true] |
| **minDebtsOwedByCommittee** | **String**| Minimum debt | [optional] |
| **maxReceipts** | **String**| Maximum aggregated receipts | [optional] |
| **hasRaisedFunds** | **Boolean**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional] |
| **party** | [**List&lt;String&gt;**](String.md)| Three-letter party code | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **isActiveCandidate** | **Boolean**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **state** | [**List&lt;String&gt;**](String.md)| State of candidate | [optional] |
| **minCashOnHandEndPeriod** | **String**| Minimum cash on hand | [optional] |
| **minReceipts** | **String**| Minimum aggregated receipts | [optional] |

### Return type

[**CandidateHistoryTotalPage**](CandidateHistoryTotalPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="committeeCommitteeIdCandidatesGet"></a>
# **committeeCommitteeIdCandidatesGet**
> CandidateDetailPage committeeCommitteeIdCandidatesGet(apiKey, committeeId, incumbentChallenge, cycle, sortNullOnly, federalFundsFlag, sortHideNull, name, perPage, electionYear, office, sort, candidateStatus, district, hasRaisedFunds, party, sortNullsLast, page, state, year)



 This endpoint is useful for finding detailed information about a particular candidate. Use the &#x60;candidate_id&#x60; to find the most recent information about that candidate. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CandidateApi;

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

    CandidateApi apiInstance = new CandidateApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    String committeeId = "committeeId_example"; // String |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    List<String> incumbentChallenge = Arrays.asList(); // List<String> | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open.
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Boolean federalFundsFlag = true; // Boolean | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates.
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    List<String> name = Arrays.asList(); // List<String> | Name (candidate or committee) to search for. Alias for 'q'.
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    List<Integer> electionYear = Arrays.asList(); // List<Integer> | Year of election
    List<String> office = Arrays.asList(); // List<String> | Federal office candidate runs for: H, S or P
    String sort = "name"; // String | Provide a field to sort by. Use `-` for descending order. 
    List<String> candidateStatus = Arrays.asList(); // List<String> | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate 
    List<String> district = Arrays.asList(); // List<String> | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.
    Boolean hasRaisedFunds = true; // Boolean | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.)
    List<String> party = Arrays.asList(); // List<String> | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> state = Arrays.asList(); // List<String> | US state or territory where a candidate runs for office
    String year = "year_example"; // String | Retrieve records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year.
    try {
      CandidateDetailPage result = apiInstance.committeeCommitteeIdCandidatesGet(apiKey, committeeId, incumbentChallenge, cycle, sortNullOnly, federalFundsFlag, sortHideNull, name, perPage, electionYear, office, sort, candidateStatus, district, hasRaisedFunds, party, sortNullsLast, page, state, year);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CandidateApi#committeeCommitteeIdCandidatesGet");
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
| **committeeId** | **String**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | |
| **incumbentChallenge** | [**List&lt;String&gt;**](String.md)| One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional] [enum: , I, C, O] |
| **cycle** | [**List&lt;Integer&gt;**](Integer.md)|  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **federalFundsFlag** | **Boolean**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **name** | [**List&lt;String&gt;**](String.md)| Name (candidate or committee) to search for. Alias for &#39;q&#39;. | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **electionYear** | [**List&lt;Integer&gt;**](Integer.md)| Year of election | [optional] |
| **office** | [**List&lt;String&gt;**](String.md)| Federal office candidate runs for: H, S or P | [optional] [enum: , H, S, P] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to name] |
| **candidateStatus** | [**List&lt;String&gt;**](String.md)| One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional] [enum: , C, F, N, P] |
| **district** | [**List&lt;String&gt;**](String.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] |
| **hasRaisedFunds** | **Boolean**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional] |
| **party** | [**List&lt;String&gt;**](String.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **state** | [**List&lt;String&gt;**](String.md)| US state or territory where a candidate runs for office | [optional] |
| **year** | **String**| Retrieve records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. | [optional] |

### Return type

[**CandidateDetailPage**](CandidateDetailPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="committeeCommitteeIdCandidatesHistoryCycleGet"></a>
# **committeeCommitteeIdCandidatesHistoryCycleGet**
> CandidateHistoryPage committeeCommitteeIdCandidatesHistoryCycleGet(apiKey, committeeId, cycle, page, sortHideNull, electionFull, perPage, sortNullOnly, sort, sortNullsLast)



 Find out a candidate&#39;s characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate&#39;s previous races.  This information is organized by &#x60;candidate_id&#x60;, so it won&#39;t help you find a candidate who ran for different offices over time; candidates get a new ID for each office. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CandidateApi;

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

    CandidateApi apiInstance = new CandidateApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    String committeeId = "committeeId_example"; // String |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    Integer cycle = 56; // Integer |  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag. 
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Boolean electionFull = true; // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    String sort = "-two_year_period"; // String | Provide a field to sort by. Use `-` for descending order. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    try {
      CandidateHistoryPage result = apiInstance.committeeCommitteeIdCandidatesHistoryCycleGet(apiKey, committeeId, cycle, page, sortHideNull, electionFull, perPage, sortNullOnly, sort, sortNullsLast);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CandidateApi#committeeCommitteeIdCandidatesHistoryCycleGet");
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
| **committeeId** | **String**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | |
| **cycle** | **Integer**|  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -two_year_period] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |

### Return type

[**CandidateHistoryPage**](CandidateHistoryPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="committeeCommitteeIdCandidatesHistoryGet"></a>
# **committeeCommitteeIdCandidatesHistoryGet**
> CandidateHistoryPage committeeCommitteeIdCandidatesHistoryGet(apiKey, committeeId, page, sortHideNull, electionFull, perPage, sortNullOnly, sort, sortNullsLast)



 Find out a candidate&#39;s characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate&#39;s previous races.  This information is organized by &#x60;candidate_id&#x60;, so it won&#39;t help you find a candidate who ran for different offices over time; candidates get a new ID for each office. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CandidateApi;

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

    CandidateApi apiInstance = new CandidateApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    String committeeId = "committeeId_example"; // String |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Boolean electionFull = true; // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    String sort = "-two_year_period"; // String | Provide a field to sort by. Use `-` for descending order. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    try {
      CandidateHistoryPage result = apiInstance.committeeCommitteeIdCandidatesHistoryGet(apiKey, committeeId, page, sortHideNull, electionFull, perPage, sortNullOnly, sort, sortNullsLast);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CandidateApi#committeeCommitteeIdCandidatesHistoryGet");
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
| **committeeId** | **String**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -two_year_period] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |

### Return type

[**CandidateHistoryPage**](CandidateHistoryPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

