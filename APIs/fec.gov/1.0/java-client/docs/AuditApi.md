# AuditApi

All URIs are relative to */v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**auditCaseGet**](AuditApi.md#auditCaseGet) | **GET** /audit-case/ |  |
| [**auditCategoryGet**](AuditApi.md#auditCategoryGet) | **GET** /audit-category/ |  |
| [**auditPrimaryCategoryGet**](AuditApi.md#auditPrimaryCategoryGet) | **GET** /audit-primary-category/ |  |
| [**namesAuditCandidatesGet**](AuditApi.md#namesAuditCandidatesGet) | **GET** /names/audit_candidates/ |  |
| [**namesAuditCommitteesGet**](AuditApi.md#namesAuditCommitteesGet) | **GET** /names/audit_committees/ |  |


<a id="auditCaseGet"></a>
# **auditCaseGet**
> AuditCasePage auditCaseGet(apiKey, maxElectionCycle, q, subCategoryId, cycle, sortNullOnly, auditCaseId, sortHideNull, candidateId, qq, perPage, sort, minElectionCycle, auditId, committeeDesignation, committeeType, sortNullsLast, page, committeeId, primaryCategoryId)



 This endpoint contains Final Audit Reports approved by the Commission since inception. The search can be based on information about the audited committee (Name, FEC ID Number, Type,  Election Cycle) or the issues covered in the report. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuditApi;

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

    AuditApi apiInstance = new AuditApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    Integer maxElectionCycle = 56; // Integer |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year. 
    List<String> q = Arrays.asList(); // List<String> | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records.
    String subCategoryId = "all"; // String |  The finding id of an audit. Finding are a category of broader issues. Each category has an unique ID. 
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    List<String> auditCaseId = Arrays.asList(); // List<String> |  Primary/foreign key for audit tables 
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    List<String> candidateId = Arrays.asList(); // List<String> |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
    List<String> qq = Arrays.asList(); // List<String> | Name of candidate running for office
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    List<String> sort = Arrays.asList(); // List<String> |  Provide a field to sort by. Use `-` for descending order. ex: `-case_no` 
    Integer minElectionCycle = 56; // Integer |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year. 
    List<Integer> auditId = Arrays.asList(); // List<Integer> |  The audit issue. Each subcategory has an unique ID 
    String committeeDesignation = "committeeDesignation_example"; // String | Type of committee:         - H or S - Congressional         - P - Presidential         - X or Y or Z - Party         - N or Q - PAC         - I - Independent expenditure         - O - Super PAC  
    List<String> committeeType = Arrays.asList(); // List<String> | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    String primaryCategoryId = "all"; // String |  Audit category ID (table PK) 
    try {
      AuditCasePage result = apiInstance.auditCaseGet(apiKey, maxElectionCycle, q, subCategoryId, cycle, sortNullOnly, auditCaseId, sortHideNull, candidateId, qq, perPage, sort, minElectionCycle, auditId, committeeDesignation, committeeType, sortNullsLast, page, committeeId, primaryCategoryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditApi#auditCaseGet");
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
| **q** | [**List&lt;String&gt;**](String.md)| The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] |
| **subCategoryId** | **String**|  The finding id of an audit. Finding are a category of broader issues. Each category has an unique ID.  | [optional] [default to all] |
| **cycle** | [**List&lt;Integer&gt;**](Integer.md)|  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **auditCaseId** | [**List&lt;String&gt;**](String.md)|  Primary/foreign key for audit tables  | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **candidateId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] |
| **qq** | [**List&lt;String&gt;**](String.md)| Name of candidate running for office | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sort** | [**List&lt;String&gt;**](String.md)|  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60;  | [optional] |
| **minElectionCycle** | **Integer**|  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | [optional] |
| **auditId** | [**List&lt;Integer&gt;**](Integer.md)|  The audit issue. Each subcategory has an unique ID  | [optional] |
| **committeeDesignation** | **String**| Type of committee:         - H or S - Congressional         - P - Presidential         - X or Y or Z - Party         - N or Q - PAC         - I - Independent expenditure         - O - Super PAC   | [optional] |
| **committeeType** | [**List&lt;String&gt;**](String.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **primaryCategoryId** | **String**|  Audit category ID (table PK)  | [optional] [default to all] |

### Return type

[**AuditCasePage**](AuditCasePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="auditCategoryGet"></a>
# **auditCategoryGet**
> AuditCategoryPage auditCategoryGet(apiKey, sortNullsLast, page, sortNullOnly, sortHideNull, perPage, primaryCategoryId, sort, primaryCategoryName)



 This lists the options for the categories and subcategories available in the /audit-search/ endpoint. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuditApi;

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

    AuditApi apiInstance = new AuditApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    List<String> primaryCategoryId = Arrays.asList(); // List<String> |  Audit category ID (table PK) 
    String sort = "primary_category_name"; // String | Provide a field to sort by. Use `-` for descending order. 
    List<String> primaryCategoryName = Arrays.asList(); // List<String> | Primary Audit Category     - No Findings or Issues/Not a Committee     - Net Outstanding Campaign/Convention Expenditures/Obligations     - Payments/Disgorgements     - Allocation Issues     - Prohibited Contributions     - Disclosure     - Recordkeeping     - Repayment to US Treasury     - Other     - Misstatement of Financial Activity     - Excessive Contributions     - Failure to File Reports/Schedules/Notices     - Loans     - Referred Findings Not Listed 
    try {
      AuditCategoryPage result = apiInstance.auditCategoryGet(apiKey, sortNullsLast, page, sortNullOnly, sortHideNull, perPage, primaryCategoryId, sort, primaryCategoryName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditApi#auditCategoryGet");
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
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **primaryCategoryId** | [**List&lt;String&gt;**](String.md)|  Audit category ID (table PK)  | [optional] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to primary_category_name] |
| **primaryCategoryName** | [**List&lt;String&gt;**](String.md)| Primary Audit Category     - No Findings or Issues/Not a Committee     - Net Outstanding Campaign/Convention Expenditures/Obligations     - Payments/Disgorgements     - Allocation Issues     - Prohibited Contributions     - Disclosure     - Recordkeeping     - Repayment to US Treasury     - Other     - Misstatement of Financial Activity     - Excessive Contributions     - Failure to File Reports/Schedules/Notices     - Loans     - Referred Findings Not Listed  | [optional] |

### Return type

[**AuditCategoryPage**](AuditCategoryPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="auditPrimaryCategoryGet"></a>
# **auditPrimaryCategoryGet**
> AuditPrimaryCategoryPage auditPrimaryCategoryGet(apiKey, sortNullsLast, page, sortNullOnly, sortHideNull, perPage, primaryCategoryId, sort, primaryCategoryName)



 This lists the options for the primary categories available in the /audit-search/ endpoint. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuditApi;

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

    AuditApi apiInstance = new AuditApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    List<String> primaryCategoryId = Arrays.asList(); // List<String> |  Audit category ID (table PK) 
    String sort = "primary_category_name"; // String | Provide a field to sort by. Use `-` for descending order. 
    List<String> primaryCategoryName = Arrays.asList(); // List<String> | Primary Audit Category     - No Findings or Issues/Not a Committee     - Net Outstanding Campaign/Convention Expenditures/Obligations     - Payments/Disgorgements     - Allocation Issues     - Prohibited Contributions     - Disclosure     - Recordkeeping     - Repayment to US Treasury     - Other     - Misstatement of Financial Activity     - Excessive Contributions     - Failure to File Reports/Schedules/Notices     - Loans     - Referred Findings Not Listed 
    try {
      AuditPrimaryCategoryPage result = apiInstance.auditPrimaryCategoryGet(apiKey, sortNullsLast, page, sortNullOnly, sortHideNull, perPage, primaryCategoryId, sort, primaryCategoryName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditApi#auditPrimaryCategoryGet");
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
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **primaryCategoryId** | [**List&lt;String&gt;**](String.md)|  Audit category ID (table PK)  | [optional] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to primary_category_name] |
| **primaryCategoryName** | [**List&lt;String&gt;**](String.md)| Primary Audit Category     - No Findings or Issues/Not a Committee     - Net Outstanding Campaign/Convention Expenditures/Obligations     - Payments/Disgorgements     - Allocation Issues     - Prohibited Contributions     - Disclosure     - Recordkeeping     - Repayment to US Treasury     - Other     - Misstatement of Financial Activity     - Excessive Contributions     - Failure to File Reports/Schedules/Notices     - Loans     - Referred Findings Not Listed  | [optional] |

### Return type

[**AuditPrimaryCategoryPage**](AuditPrimaryCategoryPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="namesAuditCandidatesGet"></a>
# **namesAuditCandidatesGet**
> AuditCandidateSearchList namesAuditCandidatesGet(apiKey, q)



 Search for candidates or committees by name. If you&#39;re looking for information on a particular person or group, using a name to find the &#x60;candidate_id&#x60; or &#x60;committee_id&#x60; on this endpoint can be a helpful first step. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuditApi;

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

    AuditApi apiInstance = new AuditApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    List<String> q = Arrays.asList(); // List<String> | Name (candidate or committee) to search for
    try {
      AuditCandidateSearchList result = apiInstance.namesAuditCandidatesGet(apiKey, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditApi#namesAuditCandidatesGet");
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
| **q** | [**List&lt;String&gt;**](String.md)| Name (candidate or committee) to search for | |

### Return type

[**AuditCandidateSearchList**](AuditCandidateSearchList.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="namesAuditCommitteesGet"></a>
# **namesAuditCommitteesGet**
> AuditCommitteeSearchList namesAuditCommitteesGet(apiKey, q)



 Search for candidates or committees by name. If you&#39;re looking for information on a particular person or group, using a name to find the &#x60;candidate_id&#x60; or &#x60;committee_id&#x60; on this endpoint can be a helpful first step. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuditApi;

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

    AuditApi apiInstance = new AuditApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    List<String> q = Arrays.asList(); // List<String> | Name (candidate or committee) to search for
    try {
      AuditCommitteeSearchList result = apiInstance.namesAuditCommitteesGet(apiKey, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditApi#namesAuditCommitteesGet");
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
| **q** | [**List&lt;String&gt;**](String.md)| Name (candidate or committee) to search for | |

### Return type

[**AuditCommitteeSearchList**](AuditCommitteeSearchList.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

