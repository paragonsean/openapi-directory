# LegalApi

All URIs are relative to */v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**legalSearchGet**](LegalApi.md#legalSearchGet) | **GET** /legal/search/ |  |


<a id="legalSearchGet"></a>
# **legalSearchGet**
> LegalSearchGetDefaultResponse legalSearchGet(apiKey, caseStatutoryCitation, afMinRtbDate, afReportYear, q, fromHit, aoRequestorType, caseMaxCloseDate, aoIsPending, afFdFineAmount, caseMinOpenDate, aoMinIssueDate, sort, aoCitationRequireAll, caseDocCategoryId, aoStatus, afMaxRtbDate, afRtbFineAmount, caseRespondents, aoEntityName, aoRequestor, aoCategory, aoRegulatoryCitation, caseRegulatoryCitation, caseCitationRequireAll, caseDispositions, aoName, afMaxFdDate, aoMaxRequestDate, murType, hitsReturned, caseElectionCycles, caseMinCloseDate, aoMaxIssueDate, afCommitteeId, afMinFdDate, caseMaxOpenDate, aoMinRequestDate, aoNo, type, caseNo, aoStatutoryCitation, afName)



 Search legal documents by document type, or across all document types using keywords, parameter values and ranges. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegalApi;

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

    LegalApi apiInstance = new LegalApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    List<String> caseStatutoryCitation = Arrays.asList(); // List<String> |  Statutory citations 
    LocalDate afMinRtbDate = LocalDate.now(); // LocalDate |  The earliest Reason to Believe date 
    String afReportYear = "afReportYear_example"; // String |  Admin fine report year 
    String q = "q_example"; // String |  Text to search legal documents for 
    Integer fromHit = 56; // Integer |  Get results starting from this index 
    List<Integer> aoRequestorType = Arrays.asList(); // List<Integer> |  Code of the advisory opinion requestor type. 
    LocalDate caseMaxCloseDate = LocalDate.now(); // LocalDate |  The latest date closed of case 
    Boolean aoIsPending = true; // Boolean |  AO is pending 
    Integer afFdFineAmount = 56; // Integer |  Final Determination fine amount 
    LocalDate caseMinOpenDate = LocalDate.now(); // LocalDate |  The earliest date opened of case 
    LocalDate aoMinIssueDate = LocalDate.now(); // LocalDate |  Earliest issue date of advisory opinion 
    String sort = "sort_example"; // String |  Provide a field to sort by. Use `-` for descending order. ex: `-case_no` 
    Boolean aoCitationRequireAll = true; // Boolean |  Require all citations to be in document (default behavior is any) 
    List<String> caseDocCategoryId = Arrays.asList(); // List<String> |  Select one or more case_doc_category_id to filter by corresponding CASE_DOCUMENT_CATEGORY:         - 1 - Conciliation and Settlement Agreements         - 2 - Complaint, Responses, Designation of Counsel and Extensions of Time         - 3 - General Counsel Reports, Briefs, Notifications and Responses         - 4 - Certifications         - 5 - Civil Penalties, Disgorgements, Other Payments and Letters of Compliance         - 6 - Statement of Reasons          - 1001 - ADR Settlement Agreements         - 1002 - Complaint, Responses, Designation of Counsel and Extensions of Time         - 1003 - ADR Memoranda, Notifications and Responses         - 1004 - Certifications         - 1005 - Civil Penalties, Disgorgements, Other Payments and Letters of Compliance         - 1006 - Statement of Reasons          - 2001 - Administrative Fine Case 
    String aoStatus = "aoStatus_example"; // String |  Status of AO (pending, withdrawn, or final) 
    LocalDate afMaxRtbDate = LocalDate.now(); // LocalDate |  The latest Reason to Believe date 
    Integer afRtbFineAmount = 56; // Integer |  Reason to Believe fine amount 
    String caseRespondents = "caseRespondents_example"; // String |  Cases respondents 
    List<String> aoEntityName = Arrays.asList(); // List<String> |  Name of commenter or representative 
    String aoRequestor = "aoRequestor_example"; // String |  The requestor of the advisory opinion 
    List<String> aoCategory = Arrays.asList(); // List<String> |  Category of the document 
    List<String> aoRegulatoryCitation = Arrays.asList(); // List<String> |  Regulatory citations 
    List<String> caseRegulatoryCitation = Arrays.asList(); // List<String> |  Regulatory citations 
    Boolean caseCitationRequireAll = true; // Boolean |  Require all citations to be in document (default behavior is any) 
    List<String> caseDispositions = Arrays.asList(); // List<String> |  Cases dispositions 
    List<String> aoName = Arrays.asList(); // List<String> |  Force advisory opinion name 
    LocalDate afMaxFdDate = LocalDate.now(); // LocalDate |  The latest Final Determination date 
    LocalDate aoMaxRequestDate = LocalDate.now(); // LocalDate |  Latest request date of advisory opinion 
    String murType = "archived"; // String |  Type of MUR : current or archived 
    Integer hitsReturned = 56; // Integer |  Number of results to return (max 10) 
    Integer caseElectionCycles = 56; // Integer |  Cases election cycles 
    LocalDate caseMinCloseDate = LocalDate.now(); // LocalDate |  The earliest date closed of case 
    LocalDate aoMaxIssueDate = LocalDate.now(); // LocalDate |  Latest issue date of advisory opinion 
    String afCommitteeId = "afCommitteeId_example"; // String |  Admin fine committee ID 
    LocalDate afMinFdDate = LocalDate.now(); // LocalDate |  The earliest Final Determination date 
    LocalDate caseMaxOpenDate = LocalDate.now(); // LocalDate |  The latest date opened of case 
    LocalDate aoMinRequestDate = LocalDate.now(); // LocalDate |  Earliest request date of advisory opinion 
    List<String> aoNo = Arrays.asList(); // List<String> |  Force advisory opinion number 
    String type = "admin_fines"; // String |  Choose a legal document type 
    List<String> caseNo = Arrays.asList(); // List<String> |  Enforcement matter case number 
    List<String> aoStatutoryCitation = Arrays.asList(); // List<String> |  Statutory citations 
    List<String> afName = Arrays.asList(); // List<String> |  Admin fine committee name 
    try {
      LegalSearchGetDefaultResponse result = apiInstance.legalSearchGet(apiKey, caseStatutoryCitation, afMinRtbDate, afReportYear, q, fromHit, aoRequestorType, caseMaxCloseDate, aoIsPending, afFdFineAmount, caseMinOpenDate, aoMinIssueDate, sort, aoCitationRequireAll, caseDocCategoryId, aoStatus, afMaxRtbDate, afRtbFineAmount, caseRespondents, aoEntityName, aoRequestor, aoCategory, aoRegulatoryCitation, caseRegulatoryCitation, caseCitationRequireAll, caseDispositions, aoName, afMaxFdDate, aoMaxRequestDate, murType, hitsReturned, caseElectionCycles, caseMinCloseDate, aoMaxIssueDate, afCommitteeId, afMinFdDate, caseMaxOpenDate, aoMinRequestDate, aoNo, type, caseNo, aoStatutoryCitation, afName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegalApi#legalSearchGet");
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
| **caseStatutoryCitation** | [**List&lt;String&gt;**](String.md)|  Statutory citations  | [optional] |
| **afMinRtbDate** | **LocalDate**|  The earliest Reason to Believe date  | [optional] |
| **afReportYear** | **String**|  Admin fine report year  | [optional] |
| **q** | **String**|  Text to search legal documents for  | [optional] |
| **fromHit** | **Integer**|  Get results starting from this index  | [optional] |
| **aoRequestorType** | [**List&lt;Integer&gt;**](Integer.md)|  Code of the advisory opinion requestor type.  | [optional] [enum: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16] |
| **caseMaxCloseDate** | **LocalDate**|  The latest date closed of case  | [optional] |
| **aoIsPending** | **Boolean**|  AO is pending  | [optional] |
| **afFdFineAmount** | **Integer**|  Final Determination fine amount  | [optional] |
| **caseMinOpenDate** | **LocalDate**|  The earliest date opened of case  | [optional] |
| **aoMinIssueDate** | **LocalDate**|  Earliest issue date of advisory opinion  | [optional] |
| **sort** | **String**|  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60;  | [optional] |
| **aoCitationRequireAll** | **Boolean**|  Require all citations to be in document (default behavior is any)  | [optional] |
| **caseDocCategoryId** | [**List&lt;String&gt;**](String.md)|  Select one or more case_doc_category_id to filter by corresponding CASE_DOCUMENT_CATEGORY:         - 1 - Conciliation and Settlement Agreements         - 2 - Complaint, Responses, Designation of Counsel and Extensions of Time         - 3 - General Counsel Reports, Briefs, Notifications and Responses         - 4 - Certifications         - 5 - Civil Penalties, Disgorgements, Other Payments and Letters of Compliance         - 6 - Statement of Reasons          - 1001 - ADR Settlement Agreements         - 1002 - Complaint, Responses, Designation of Counsel and Extensions of Time         - 1003 - ADR Memoranda, Notifications and Responses         - 1004 - Certifications         - 1005 - Civil Penalties, Disgorgements, Other Payments and Letters of Compliance         - 1006 - Statement of Reasons          - 2001 - Administrative Fine Case  | [optional] [enum: 1, 2, 3, 4, 5, 6, 1001, 1002, 1003, 1004, 1005, 1006, 2001] |
| **aoStatus** | **String**|  Status of AO (pending, withdrawn, or final)  | [optional] |
| **afMaxRtbDate** | **LocalDate**|  The latest Reason to Believe date  | [optional] |
| **afRtbFineAmount** | **Integer**|  Reason to Believe fine amount  | [optional] |
| **caseRespondents** | **String**|  Cases respondents  | [optional] |
| **aoEntityName** | [**List&lt;String&gt;**](String.md)|  Name of commenter or representative  | [optional] |
| **aoRequestor** | **String**|  The requestor of the advisory opinion  | [optional] |
| **aoCategory** | [**List&lt;String&gt;**](String.md)|  Category of the document  | [optional] [enum: F, V, D, R, W, C, S] |
| **aoRegulatoryCitation** | [**List&lt;String&gt;**](String.md)|  Regulatory citations  | [optional] |
| **caseRegulatoryCitation** | [**List&lt;String&gt;**](String.md)|  Regulatory citations  | [optional] |
| **caseCitationRequireAll** | **Boolean**|  Require all citations to be in document (default behavior is any)  | [optional] |
| **caseDispositions** | [**List&lt;String&gt;**](String.md)|  Cases dispositions  | [optional] |
| **aoName** | [**List&lt;String&gt;**](String.md)|  Force advisory opinion name  | [optional] |
| **afMaxFdDate** | **LocalDate**|  The latest Final Determination date  | [optional] |
| **aoMaxRequestDate** | **LocalDate**|  Latest request date of advisory opinion  | [optional] |
| **murType** | **String**|  Type of MUR : current or archived  | [optional] [enum: archived, current] |
| **hitsReturned** | **Integer**|  Number of results to return (max 10)  | [optional] |
| **caseElectionCycles** | **Integer**|  Cases election cycles  | [optional] |
| **caseMinCloseDate** | **LocalDate**|  The earliest date closed of case  | [optional] |
| **aoMaxIssueDate** | **LocalDate**|  Latest issue date of advisory opinion  | [optional] |
| **afCommitteeId** | **String**|  Admin fine committee ID  | [optional] |
| **afMinFdDate** | **LocalDate**|  The earliest Final Determination date  | [optional] |
| **caseMaxOpenDate** | **LocalDate**|  The latest date opened of case  | [optional] |
| **aoMinRequestDate** | **LocalDate**|  Earliest request date of advisory opinion  | [optional] |
| **aoNo** | [**List&lt;String&gt;**](String.md)|  Force advisory opinion number  | [optional] |
| **type** | **String**|  Choose a legal document type  | [optional] [enum: admin_fines, adrs, advisory_opinions, murs, regulations, statutes] |
| **caseNo** | [**List&lt;String&gt;**](String.md)|  Enforcement matter case number  | [optional] |
| **aoStatutoryCitation** | [**List&lt;String&gt;**](String.md)|  Statutory citations  | [optional] |
| **afName** | [**List&lt;String&gt;**](String.md)|  Admin fine committee name  | [optional] |

### Return type

[**LegalSearchGetDefaultResponse**](LegalSearchGetDefaultResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Legal search results |  -  |

