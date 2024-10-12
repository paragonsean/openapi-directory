# DocumentsApi

All URIs are relative to *https://api.data.gov/regulations/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**document**](DocumentsApi.md#document) | **GET** /document.{response_format} | Returns Document information |
| [**documents**](DocumentsApi.md#documents) | **GET** /documents.{response_format} | Search for Documents |


<a id="document"></a>
# **document**
> document(responseFormat, documentId, federalRegisterNumber)

Returns Document information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.data.gov/regulations/v3");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String responseFormat = "json"; // String | Format
    String documentId = "EPA-HQ-OAR-2011-0028-0108"; // String | FDMS Document ID
    String federalRegisterNumber = "federalRegisterNumber_example"; // String | Federal Register Document Number
    try {
      apiInstance.document(responseFormat, documentId, federalRegisterNumber);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#document");
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
| **responseFormat** | **String**| Format | [default to json] [enum: json, xml] |
| **documentId** | **String**| FDMS Document ID | [optional] [default to EPA-HQ-OAR-2011-0028-0108] |
| **federalRegisterNumber** | **String**| Federal Register Document Number | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **400** | Bad request. The document is only available for comment via Regulations.gov. |  -  |
| **404** | File not found. |  -  |

<a id="documents"></a>
# **documents**
> documents(responseFormat, countsOnly, encoded, s, dct, dktid, dkt, cp, a, rpp, po, cs, np, cmsd, cmd, crd, rd, pd, cat, sb, so, dktst, dktst2, docst)

Search for Documents

This API allows users to build a query based on any of the parameters below.  If you have trouble building queries, you may wish to try them through the &lt;a href&#x3D;\&quot;http://www.regulations.gov/#!advancedSearch\&quot;&gt;Advanced Search&lt;/a&gt; page on the Regulations.gov website.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.data.gov/regulations/v3");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String responseFormat = "json"; // String | Format
    Integer countsOnly = 0; // Integer | Counts Only: <ul><li>1 (will return only the document count for a search query)</li><li>0 (will return documents as well)</li></ul>
    Integer encoded = 0; // Integer | Encoded: <ul><li>1 (will accept Regulations.gov style encoded parameters)</li><li>0 (will not accept such encoded parameters)</li></ul>
    String s = "s_example"; // String | Keyword(s)
    String dct = "N"; // String | Document Type: <ul><li>N: Notice</li><li>PR: Proposed Rule</li><li>FR: Rule</li><li>O: Other</li><li>SR: Supporting & Related Material</li><li>PS: Public Submission</li></ul>
    String dktid = "dktid_example"; // String | Valid Docket ID (ex. SEC-2012-0044)
    String dkt = "N"; // String | Docket Type: <ul><li>R: Rulemaking</li><li>N: Nonrulemaking</li></ul><p>A Docket Type is either Rulemaking or Nonrulemaking. A Rulemaking docket includes the type of regulation that establishes a rule. While a Non-Rulemaking docket does not include a rule.</p>
    String cp = "O"; // String | Comment Period: <ul><li>O: Open</li><li>C: Closed</li></ul>
    String a = "a_example"; // String | Federal Agency: List of accepted Federal Agency values. This field allows multiple values. Ex. a=FMCSA%252BEPA%252BFDA
    String rpp = "10"; // String | Results Per Page 10, 25, 100, 500, 1,000.  Results per page may not exceed 1,000.
    Integer po = 56; // Integer | Enter the page offset (always starts with 0). This is used in conjunction with results per page to provide large data sets. For example, if a search produces 82 results and the result per page is set to 25, this will generate 4 pages. 3 pages will have 25 results and the last page will have 7 results. Page offset values for each page will be: <pre>Page 1: po=0 Page 2: po=25 Page 3: po=50 Page 4: po=75</pre> The total number of pages is [total results/results per page] and page offset for page X is [X-1 * results per page]
    Integer cs = 0; // Integer | Comment Period Closing Soon: <ul><li>0 (closing today)</li><li>3 (closing within 3 days)</li><li>15 (closing within 15 days)</li><li>30 (closing within 30 days)</li><li>90 (closing within 90 days)</li></ul>
    Integer np = 0; // Integer | Newly Posted: <ul><li>0 (posted today)</li><li>3 (posted within last 3 days)</li><li>15 (posted within last 15 days)</li><li>30 (posted within last 30 days)</li><li>90 (posted within last 90 days)</li></ul>  For periods of time beyond 90-days, please use a date range with the Posted Date parameter.
    LocalDate cmsd = LocalDate.now(); // LocalDate | Comment Period Start Date: Enter a date in the form of MM/DD/YY. Note: If the Comment Period End Date is also provided, then ensure the Comment Period Start date is earlier.
    LocalDate cmd = LocalDate.now(); // LocalDate | Comment Period End Date: Enter a date in the form of MM/DD/YY. Note: If the Comment Period Start Date is also provided, then ensure the Comment Period End date is after.<br/>* Comment Period Start and End Dates are mutually exclusive with the 'closing soon' parameter. If both are provided, 'closing soon' will be ignored.
    LocalDate crd = LocalDate.now(); // LocalDate | Creation Date: Enter a date in the form of MM/DD/YY. Accepts a single date or a date range. Ex. <code>crd=11/06/13-03/06/14</code>
    LocalDate rd = LocalDate.now(); // LocalDate | Received Date: Enter a date in the form of MM/DD/YY. Accepts a single date or a date range. Ex. <code>rd=11/06/13-03/06/14</code>
    LocalDate pd = LocalDate.now(); // LocalDate | Posted Date: Enter a date in the form of MM/DD/YY. Accepts a single date or a date range. Ex. <code>pd=11/06/13-03/06/14</code>
    String cat = "AD"; // String | Document Category: <ul><li>AD (Aerospace and Transportation)</li> <li>AEP (Agriculture, Environment, and Public Lands)</li> <li>BFS (Banking and Financial)</li> <li>CT (Commerce and International)</li> <li>LES (Defense, Law Enforcement, and Security)</li> <li>EELS (Education, Labor, Presidential, and Government Services)</li> <li>EUMM (Energy, Natural Resources, and Utilities)</li> <li>HCFP (Food Safety, Health, and Pharmaceutical)</li> <li>PRE (Housing, Development, and Real Estate)</li> <li>ITT (Technology and Telecommunications)</li></ul>
    String sb = "docketId"; // String | Sort By: <ul><li>docketId (Docket ID)</li><li>docId (Document ID)</li><li>title (Title)</li><li>postedDate (Posted Date)</li><li>agency (Agency)</li><li>documentType (Document Type)</li><li>submitterName (Submitter Name)</li><li>organization (Organization)</li></ul> Sort Order is REQUIRED if this parameter is included.
    String so = "ASC"; // String | Sort Order: <ul><li>ASC: Ascending</li><li>DESC: Descending</li></ul>
    String dktst = "dktst_example"; // String | Docket Subtype: Only one docket subtype at a time may be selected. One or more agency values must be part of the request. Only values valid for the selected agency will be returned.
    String dktst2 = "dktst2_example"; // String | Docket Sub-subtype: Only one docket sub-subtype at a time may be selected. One or more agency values must be part of the request. Only values valid for the selected agency will be returned.
    String docst = "docst_example"; // String | Document Subtype: Single or multiple document subtypes may be included.  Multiple values should be passed as follows: <code>docst=%20Certificate+of+Service%252BCorrespondence</code>
    try {
      apiInstance.documents(responseFormat, countsOnly, encoded, s, dct, dktid, dkt, cp, a, rpp, po, cs, np, cmsd, cmd, crd, rd, pd, cat, sb, so, dktst, dktst2, docst);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#documents");
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
| **responseFormat** | **String**| Format | [default to json] [enum: json, xml] |
| **countsOnly** | **Integer**| Counts Only: &lt;ul&gt;&lt;li&gt;1 (will return only the document count for a search query)&lt;/li&gt;&lt;li&gt;0 (will return documents as well)&lt;/li&gt;&lt;/ul&gt; | [optional] [enum: 0, 1] |
| **encoded** | **Integer**| Encoded: &lt;ul&gt;&lt;li&gt;1 (will accept Regulations.gov style encoded parameters)&lt;/li&gt;&lt;li&gt;0 (will not accept such encoded parameters)&lt;/li&gt;&lt;/ul&gt; | [optional] [enum: 0, 1] |
| **s** | **String**| Keyword(s) | [optional] |
| **dct** | **String**| Document Type: &lt;ul&gt;&lt;li&gt;N: Notice&lt;/li&gt;&lt;li&gt;PR: Proposed Rule&lt;/li&gt;&lt;li&gt;FR: Rule&lt;/li&gt;&lt;li&gt;O: Other&lt;/li&gt;&lt;li&gt;SR: Supporting &amp; Related Material&lt;/li&gt;&lt;li&gt;PS: Public Submission&lt;/li&gt;&lt;/ul&gt; | [optional] [enum: N, PR, FR, O, SR, PS] |
| **dktid** | **String**| Valid Docket ID (ex. SEC-2012-0044) | [optional] |
| **dkt** | **String**| Docket Type: &lt;ul&gt;&lt;li&gt;R: Rulemaking&lt;/li&gt;&lt;li&gt;N: Nonrulemaking&lt;/li&gt;&lt;/ul&gt;&lt;p&gt;A Docket Type is either Rulemaking or Nonrulemaking. A Rulemaking docket includes the type of regulation that establishes a rule. While a Non-Rulemaking docket does not include a rule.&lt;/p&gt; | [optional] [enum: N, R] |
| **cp** | **String**| Comment Period: &lt;ul&gt;&lt;li&gt;O: Open&lt;/li&gt;&lt;li&gt;C: Closed&lt;/li&gt;&lt;/ul&gt; | [optional] [enum: O, C] |
| **a** | **String**| Federal Agency: List of accepted Federal Agency values. This field allows multiple values. Ex. a&#x3D;FMCSA%252BEPA%252BFDA | [optional] |
| **rpp** | **String**| Results Per Page 10, 25, 100, 500, 1,000.  Results per page may not exceed 1,000. | [optional] [enum: 10, 25, 100, 500, 1000] |
| **po** | **Integer**| Enter the page offset (always starts with 0). This is used in conjunction with results per page to provide large data sets. For example, if a search produces 82 results and the result per page is set to 25, this will generate 4 pages. 3 pages will have 25 results and the last page will have 7 results. Page offset values for each page will be: &lt;pre&gt;Page 1: po&#x3D;0 Page 2: po&#x3D;25 Page 3: po&#x3D;50 Page 4: po&#x3D;75&lt;/pre&gt; The total number of pages is [total results/results per page] and page offset for page X is [X-1 * results per page] | [optional] |
| **cs** | **Integer**| Comment Period Closing Soon: &lt;ul&gt;&lt;li&gt;0 (closing today)&lt;/li&gt;&lt;li&gt;3 (closing within 3 days)&lt;/li&gt;&lt;li&gt;15 (closing within 15 days)&lt;/li&gt;&lt;li&gt;30 (closing within 30 days)&lt;/li&gt;&lt;li&gt;90 (closing within 90 days)&lt;/li&gt;&lt;/ul&gt; | [optional] [enum: 0, 3, 15, 30, 90] |
| **np** | **Integer**| Newly Posted: &lt;ul&gt;&lt;li&gt;0 (posted today)&lt;/li&gt;&lt;li&gt;3 (posted within last 3 days)&lt;/li&gt;&lt;li&gt;15 (posted within last 15 days)&lt;/li&gt;&lt;li&gt;30 (posted within last 30 days)&lt;/li&gt;&lt;li&gt;90 (posted within last 90 days)&lt;/li&gt;&lt;/ul&gt;  For periods of time beyond 90-days, please use a date range with the Posted Date parameter. | [optional] [enum: 0, 3, 15, 30, 90] |
| **cmsd** | **LocalDate**| Comment Period Start Date: Enter a date in the form of MM/DD/YY. Note: If the Comment Period End Date is also provided, then ensure the Comment Period Start date is earlier. | [optional] |
| **cmd** | **LocalDate**| Comment Period End Date: Enter a date in the form of MM/DD/YY. Note: If the Comment Period Start Date is also provided, then ensure the Comment Period End date is after.&lt;br/&gt;* Comment Period Start and End Dates are mutually exclusive with the &#39;closing soon&#39; parameter. If both are provided, &#39;closing soon&#39; will be ignored. | [optional] |
| **crd** | **LocalDate**| Creation Date: Enter a date in the form of MM/DD/YY. Accepts a single date or a date range. Ex. &lt;code&gt;crd&#x3D;11/06/13-03/06/14&lt;/code&gt; | [optional] |
| **rd** | **LocalDate**| Received Date: Enter a date in the form of MM/DD/YY. Accepts a single date or a date range. Ex. &lt;code&gt;rd&#x3D;11/06/13-03/06/14&lt;/code&gt; | [optional] |
| **pd** | **LocalDate**| Posted Date: Enter a date in the form of MM/DD/YY. Accepts a single date or a date range. Ex. &lt;code&gt;pd&#x3D;11/06/13-03/06/14&lt;/code&gt; | [optional] |
| **cat** | **String**| Document Category: &lt;ul&gt;&lt;li&gt;AD (Aerospace and Transportation)&lt;/li&gt; &lt;li&gt;AEP (Agriculture, Environment, and Public Lands)&lt;/li&gt; &lt;li&gt;BFS (Banking and Financial)&lt;/li&gt; &lt;li&gt;CT (Commerce and International)&lt;/li&gt; &lt;li&gt;LES (Defense, Law Enforcement, and Security)&lt;/li&gt; &lt;li&gt;EELS (Education, Labor, Presidential, and Government Services)&lt;/li&gt; &lt;li&gt;EUMM (Energy, Natural Resources, and Utilities)&lt;/li&gt; &lt;li&gt;HCFP (Food Safety, Health, and Pharmaceutical)&lt;/li&gt; &lt;li&gt;PRE (Housing, Development, and Real Estate)&lt;/li&gt; &lt;li&gt;ITT (Technology and Telecommunications)&lt;/li&gt;&lt;/ul&gt; | [optional] [enum: AD, AEP, BFS, CT, LES, EELS, EUMM, HCFP, PRE, ITT] |
| **sb** | **String**| Sort By: &lt;ul&gt;&lt;li&gt;docketId (Docket ID)&lt;/li&gt;&lt;li&gt;docId (Document ID)&lt;/li&gt;&lt;li&gt;title (Title)&lt;/li&gt;&lt;li&gt;postedDate (Posted Date)&lt;/li&gt;&lt;li&gt;agency (Agency)&lt;/li&gt;&lt;li&gt;documentType (Document Type)&lt;/li&gt;&lt;li&gt;submitterName (Submitter Name)&lt;/li&gt;&lt;li&gt;organization (Organization)&lt;/li&gt;&lt;/ul&gt; Sort Order is REQUIRED if this parameter is included. | [optional] [enum: docketId, docId, title, postedDate, agency, documentType, submitterName, organization] |
| **so** | **String**| Sort Order: &lt;ul&gt;&lt;li&gt;ASC: Ascending&lt;/li&gt;&lt;li&gt;DESC: Descending&lt;/li&gt;&lt;/ul&gt; | [optional] [enum: ASC, DESC] |
| **dktst** | **String**| Docket Subtype: Only one docket subtype at a time may be selected. One or more agency values must be part of the request. Only values valid for the selected agency will be returned. | [optional] |
| **dktst2** | **String**| Docket Sub-subtype: Only one docket sub-subtype at a time may be selected. One or more agency values must be part of the request. Only values valid for the selected agency will be returned. | [optional] |
| **docst** | **String**| Document Subtype: Single or multiple document subtypes may be included.  Multiple values should be passed as follows: &lt;code&gt;docst&#x3D;%20Certificate+of+Service%252BCorrespondence&lt;/code&gt; | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **400** | Bad request. The document is only available for comment via Regulations.gov. |  -  |
| **404** | File not found. |  -  |

