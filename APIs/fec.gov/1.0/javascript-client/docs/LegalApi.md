# OpenFec.LegalApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**legalSearchGet**](LegalApi.md#legalSearchGet) | **GET** /legal/search/ | 



## legalSearchGet

> LegalSearchGetDefaultResponse legalSearchGet(apiKey, opts)



 Search legal documents by document type, or across all document types using keywords, parameter values and ranges. 

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

let apiInstance = new OpenFec.LegalApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'caseStatutoryCitation': ["null"], // [String] |  Statutory citations 
  'afMinRtbDate': new Date("2013-10-20"), // Date |  The earliest Reason to Believe date 
  'afReportYear': "afReportYear_example", // String |  Admin fine report year 
  'q': "q_example", // String |  Text to search legal documents for 
  'fromHit': 56, // Number |  Get results starting from this index 
  'aoRequestorType': [null], // [Number] |  Code of the advisory opinion requestor type. 
  'caseMaxCloseDate': new Date("2013-10-20"), // Date |  The latest date closed of case 
  'aoIsPending': true, // Boolean |  AO is pending 
  'afFdFineAmount': 56, // Number |  Final Determination fine amount 
  'caseMinOpenDate': new Date("2013-10-20"), // Date |  The earliest date opened of case 
  'aoMinIssueDate': new Date("2013-10-20"), // Date |  Earliest issue date of advisory opinion 
  'sort': "sort_example", // String |  Provide a field to sort by. Use `-` for descending order. ex: `-case_no` 
  'aoCitationRequireAll': true, // Boolean |  Require all citations to be in document (default behavior is any) 
  'caseDocCategoryId': ["null"], // [String] |  Select one or more case_doc_category_id to filter by corresponding CASE_DOCUMENT_CATEGORY:         - 1 - Conciliation and Settlement Agreements         - 2 - Complaint, Responses, Designation of Counsel and Extensions of Time         - 3 - General Counsel Reports, Briefs, Notifications and Responses         - 4 - Certifications         - 5 - Civil Penalties, Disgorgements, Other Payments and Letters of Compliance         - 6 - Statement of Reasons          - 1001 - ADR Settlement Agreements         - 1002 - Complaint, Responses, Designation of Counsel and Extensions of Time         - 1003 - ADR Memoranda, Notifications and Responses         - 1004 - Certifications         - 1005 - Civil Penalties, Disgorgements, Other Payments and Letters of Compliance         - 1006 - Statement of Reasons          - 2001 - Administrative Fine Case 
  'aoStatus': "aoStatus_example", // String |  Status of AO (pending, withdrawn, or final) 
  'afMaxRtbDate': new Date("2013-10-20"), // Date |  The latest Reason to Believe date 
  'afRtbFineAmount': 56, // Number |  Reason to Believe fine amount 
  'caseRespondents': "caseRespondents_example", // String |  Cases respondents 
  'aoEntityName': ["null"], // [String] |  Name of commenter or representative 
  'aoRequestor': "aoRequestor_example", // String |  The requestor of the advisory opinion 
  'aoCategory': ["null"], // [String] |  Category of the document 
  'aoRegulatoryCitation': ["null"], // [String] |  Regulatory citations 
  'caseRegulatoryCitation': ["null"], // [String] |  Regulatory citations 
  'caseCitationRequireAll': true, // Boolean |  Require all citations to be in document (default behavior is any) 
  'caseDispositions': ["null"], // [String] |  Cases dispositions 
  'aoName': ["null"], // [String] |  Force advisory opinion name 
  'afMaxFdDate': new Date("2013-10-20"), // Date |  The latest Final Determination date 
  'aoMaxRequestDate': new Date("2013-10-20"), // Date |  Latest request date of advisory opinion 
  'murType': "murType_example", // String |  Type of MUR : current or archived 
  'hitsReturned': 56, // Number |  Number of results to return (max 10) 
  'caseElectionCycles': 56, // Number |  Cases election cycles 
  'caseMinCloseDate': new Date("2013-10-20"), // Date |  The earliest date closed of case 
  'aoMaxIssueDate': new Date("2013-10-20"), // Date |  Latest issue date of advisory opinion 
  'afCommitteeId': "afCommitteeId_example", // String |  Admin fine committee ID 
  'afMinFdDate': new Date("2013-10-20"), // Date |  The earliest Final Determination date 
  'caseMaxOpenDate': new Date("2013-10-20"), // Date |  The latest date opened of case 
  'aoMinRequestDate': new Date("2013-10-20"), // Date |  Earliest request date of advisory opinion 
  'aoNo': ["null"], // [String] |  Force advisory opinion number 
  'type': "type_example", // String |  Choose a legal document type 
  'caseNo': ["null"], // [String] |  Enforcement matter case number 
  'aoStatutoryCitation': ["null"], // [String] |  Statutory citations 
  'afName': ["null"] // [String] |  Admin fine committee name 
};
apiInstance.legalSearchGet(apiKey, opts, (error, data, response) => {
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
 **caseStatutoryCitation** | [**[String]**](String.md)|  Statutory citations  | [optional] 
 **afMinRtbDate** | **Date**|  The earliest Reason to Believe date  | [optional] 
 **afReportYear** | **String**|  Admin fine report year  | [optional] 
 **q** | **String**|  Text to search legal documents for  | [optional] 
 **fromHit** | **Number**|  Get results starting from this index  | [optional] 
 **aoRequestorType** | [**[Number]**](Number.md)|  Code of the advisory opinion requestor type.  | [optional] 
 **caseMaxCloseDate** | **Date**|  The latest date closed of case  | [optional] 
 **aoIsPending** | **Boolean**|  AO is pending  | [optional] 
 **afFdFineAmount** | **Number**|  Final Determination fine amount  | [optional] 
 **caseMinOpenDate** | **Date**|  The earliest date opened of case  | [optional] 
 **aoMinIssueDate** | **Date**|  Earliest issue date of advisory opinion  | [optional] 
 **sort** | **String**|  Provide a field to sort by. Use &#x60;-&#x60; for descending order. ex: &#x60;-case_no&#x60;  | [optional] 
 **aoCitationRequireAll** | **Boolean**|  Require all citations to be in document (default behavior is any)  | [optional] 
 **caseDocCategoryId** | [**[String]**](String.md)|  Select one or more case_doc_category_id to filter by corresponding CASE_DOCUMENT_CATEGORY:         - 1 - Conciliation and Settlement Agreements         - 2 - Complaint, Responses, Designation of Counsel and Extensions of Time         - 3 - General Counsel Reports, Briefs, Notifications and Responses         - 4 - Certifications         - 5 - Civil Penalties, Disgorgements, Other Payments and Letters of Compliance         - 6 - Statement of Reasons          - 1001 - ADR Settlement Agreements         - 1002 - Complaint, Responses, Designation of Counsel and Extensions of Time         - 1003 - ADR Memoranda, Notifications and Responses         - 1004 - Certifications         - 1005 - Civil Penalties, Disgorgements, Other Payments and Letters of Compliance         - 1006 - Statement of Reasons          - 2001 - Administrative Fine Case  | [optional] 
 **aoStatus** | **String**|  Status of AO (pending, withdrawn, or final)  | [optional] 
 **afMaxRtbDate** | **Date**|  The latest Reason to Believe date  | [optional] 
 **afRtbFineAmount** | **Number**|  Reason to Believe fine amount  | [optional] 
 **caseRespondents** | **String**|  Cases respondents  | [optional] 
 **aoEntityName** | [**[String]**](String.md)|  Name of commenter or representative  | [optional] 
 **aoRequestor** | **String**|  The requestor of the advisory opinion  | [optional] 
 **aoCategory** | [**[String]**](String.md)|  Category of the document  | [optional] 
 **aoRegulatoryCitation** | [**[String]**](String.md)|  Regulatory citations  | [optional] 
 **caseRegulatoryCitation** | [**[String]**](String.md)|  Regulatory citations  | [optional] 
 **caseCitationRequireAll** | **Boolean**|  Require all citations to be in document (default behavior is any)  | [optional] 
 **caseDispositions** | [**[String]**](String.md)|  Cases dispositions  | [optional] 
 **aoName** | [**[String]**](String.md)|  Force advisory opinion name  | [optional] 
 **afMaxFdDate** | **Date**|  The latest Final Determination date  | [optional] 
 **aoMaxRequestDate** | **Date**|  Latest request date of advisory opinion  | [optional] 
 **murType** | **String**|  Type of MUR : current or archived  | [optional] 
 **hitsReturned** | **Number**|  Number of results to return (max 10)  | [optional] 
 **caseElectionCycles** | **Number**|  Cases election cycles  | [optional] 
 **caseMinCloseDate** | **Date**|  The earliest date closed of case  | [optional] 
 **aoMaxIssueDate** | **Date**|  Latest issue date of advisory opinion  | [optional] 
 **afCommitteeId** | **String**|  Admin fine committee ID  | [optional] 
 **afMinFdDate** | **Date**|  The earliest Final Determination date  | [optional] 
 **caseMaxOpenDate** | **Date**|  The latest date opened of case  | [optional] 
 **aoMinRequestDate** | **Date**|  Earliest request date of advisory opinion  | [optional] 
 **aoNo** | [**[String]**](String.md)|  Force advisory opinion number  | [optional] 
 **type** | **String**|  Choose a legal document type  | [optional] 
 **caseNo** | [**[String]**](String.md)|  Enforcement matter case number  | [optional] 
 **aoStatutoryCitation** | [**[String]**](String.md)|  Statutory citations  | [optional] 
 **afName** | [**[String]**](String.md)|  Admin fine committee name  | [optional] 

### Return type

[**LegalSearchGetDefaultResponse**](LegalSearchGetDefaultResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

