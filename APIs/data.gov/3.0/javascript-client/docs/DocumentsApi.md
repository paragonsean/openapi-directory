# RegulationsGov.DocumentsApi

All URIs are relative to *https://api.data.gov/regulations/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**document**](DocumentsApi.md#document) | **GET** /document.{response_format} | Returns Document information
[**documents**](DocumentsApi.md#documents) | **GET** /documents.{response_format} | Search for Documents



## document

> document(responseFormat, opts)

Returns Document information

### Example

```javascript
import RegulationsGov from 'regulations_gov';
let defaultClient = RegulationsGov.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new RegulationsGov.DocumentsApi();
let responseFormat = "'json'"; // String | Format
let opts = {
  'documentId': "'EPA-HQ-OAR-2011-0028-0108'", // String | FDMS Document ID
  'federalRegisterNumber': "federalRegisterNumber_example" // String | Federal Register Document Number
};
apiInstance.document(responseFormat, opts, (error, data, response) => {
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
 **responseFormat** | **String**| Format | [default to &#39;json&#39;]
 **documentId** | **String**| FDMS Document ID | [optional] [default to &#39;EPA-HQ-OAR-2011-0028-0108&#39;]
 **federalRegisterNumber** | **String**| Federal Register Document Number | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## documents

> documents(responseFormat, opts)

Search for Documents

This API allows users to build a query based on any of the parameters below.  If you have trouble building queries, you may wish to try them through the &lt;a href&#x3D;\&quot;http://www.regulations.gov/#!advancedSearch\&quot;&gt;Advanced Search&lt;/a&gt; page on the Regulations.gov website.

### Example

```javascript
import RegulationsGov from 'regulations_gov';
let defaultClient = RegulationsGov.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new RegulationsGov.DocumentsApi();
let responseFormat = "'json'"; // String | Format
let opts = {
  'countsOnly': 56, // Number | Counts Only: <ul><li>1 (will return only the document count for a search query)</li><li>0 (will return documents as well)</li></ul>
  'encoded': 56, // Number | Encoded: <ul><li>1 (will accept Regulations.gov style encoded parameters)</li><li>0 (will not accept such encoded parameters)</li></ul>
  's': "s_example", // String | Keyword(s)
  'dct': "dct_example", // String | Document Type: <ul><li>N: Notice</li><li>PR: Proposed Rule</li><li>FR: Rule</li><li>O: Other</li><li>SR: Supporting & Related Material</li><li>PS: Public Submission</li></ul>
  'dktid': "dktid_example", // String | Valid Docket ID (ex. SEC-2012-0044)
  'dkt': "dkt_example", // String | Docket Type: <ul><li>R: Rulemaking</li><li>N: Nonrulemaking</li></ul><p>A Docket Type is either Rulemaking or Nonrulemaking. A Rulemaking docket includes the type of regulation that establishes a rule. While a Non-Rulemaking docket does not include a rule.</p>
  'cp': "cp_example", // String | Comment Period: <ul><li>O: Open</li><li>C: Closed</li></ul>
  'a': "a_example", // String | Federal Agency: List of accepted Federal Agency values. This field allows multiple values. Ex. a=FMCSA%252BEPA%252BFDA
  'rpp': "rpp_example", // String | Results Per Page 10, 25, 100, 500, 1,000.  Results per page may not exceed 1,000.
  'po': 56, // Number | Enter the page offset (always starts with 0). This is used in conjunction with results per page to provide large data sets. For example, if a search produces 82 results and the result per page is set to 25, this will generate 4 pages. 3 pages will have 25 results and the last page will have 7 results. Page offset values for each page will be: <pre>Page 1: po=0 Page 2: po=25 Page 3: po=50 Page 4: po=75</pre> The total number of pages is [total results/results per page] and page offset for page X is [X-1 * results per page]
  'cs': 56, // Number | Comment Period Closing Soon: <ul><li>0 (closing today)</li><li>3 (closing within 3 days)</li><li>15 (closing within 15 days)</li><li>30 (closing within 30 days)</li><li>90 (closing within 90 days)</li></ul>
  'np': 56, // Number | Newly Posted: <ul><li>0 (posted today)</li><li>3 (posted within last 3 days)</li><li>15 (posted within last 15 days)</li><li>30 (posted within last 30 days)</li><li>90 (posted within last 90 days)</li></ul>  For periods of time beyond 90-days, please use a date range with the Posted Date parameter.
  'cmsd': new Date("2013-10-20"), // Date | Comment Period Start Date: Enter a date in the form of MM/DD/YY. Note: If the Comment Period End Date is also provided, then ensure the Comment Period Start date is earlier.
  'cmd': new Date("2013-10-20"), // Date | Comment Period End Date: Enter a date in the form of MM/DD/YY. Note: If the Comment Period Start Date is also provided, then ensure the Comment Period End date is after.<br/>* Comment Period Start and End Dates are mutually exclusive with the 'closing soon' parameter. If both are provided, 'closing soon' will be ignored.
  'crd': new Date("2013-10-20"), // Date | Creation Date: Enter a date in the form of MM/DD/YY. Accepts a single date or a date range. Ex. <code>crd=11/06/13-03/06/14</code>
  'rd': new Date("2013-10-20"), // Date | Received Date: Enter a date in the form of MM/DD/YY. Accepts a single date or a date range. Ex. <code>rd=11/06/13-03/06/14</code>
  'pd': new Date("2013-10-20"), // Date | Posted Date: Enter a date in the form of MM/DD/YY. Accepts a single date or a date range. Ex. <code>pd=11/06/13-03/06/14</code>
  'cat': "cat_example", // String | Document Category: <ul><li>AD (Aerospace and Transportation)</li> <li>AEP (Agriculture, Environment, and Public Lands)</li> <li>BFS (Banking and Financial)</li> <li>CT (Commerce and International)</li> <li>LES (Defense, Law Enforcement, and Security)</li> <li>EELS (Education, Labor, Presidential, and Government Services)</li> <li>EUMM (Energy, Natural Resources, and Utilities)</li> <li>HCFP (Food Safety, Health, and Pharmaceutical)</li> <li>PRE (Housing, Development, and Real Estate)</li> <li>ITT (Technology and Telecommunications)</li></ul>
  'sb': "sb_example", // String | Sort By: <ul><li>docketId (Docket ID)</li><li>docId (Document ID)</li><li>title (Title)</li><li>postedDate (Posted Date)</li><li>agency (Agency)</li><li>documentType (Document Type)</li><li>submitterName (Submitter Name)</li><li>organization (Organization)</li></ul> Sort Order is REQUIRED if this parameter is included.
  'so': "so_example", // String | Sort Order: <ul><li>ASC: Ascending</li><li>DESC: Descending</li></ul>
  'dktst': "dktst_example", // String | Docket Subtype: Only one docket subtype at a time may be selected. One or more agency values must be part of the request. Only values valid for the selected agency will be returned.
  'dktst2': "dktst2_example", // String | Docket Sub-subtype: Only one docket sub-subtype at a time may be selected. One or more agency values must be part of the request. Only values valid for the selected agency will be returned.
  'docst': "docst_example" // String | Document Subtype: Single or multiple document subtypes may be included.  Multiple values should be passed as follows: <code>docst=%20Certificate+of+Service%252BCorrespondence</code>
};
apiInstance.documents(responseFormat, opts, (error, data, response) => {
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
 **responseFormat** | **String**| Format | [default to &#39;json&#39;]
 **countsOnly** | **Number**| Counts Only: &lt;ul&gt;&lt;li&gt;1 (will return only the document count for a search query)&lt;/li&gt;&lt;li&gt;0 (will return documents as well)&lt;/li&gt;&lt;/ul&gt; | [optional] 
 **encoded** | **Number**| Encoded: &lt;ul&gt;&lt;li&gt;1 (will accept Regulations.gov style encoded parameters)&lt;/li&gt;&lt;li&gt;0 (will not accept such encoded parameters)&lt;/li&gt;&lt;/ul&gt; | [optional] 
 **s** | **String**| Keyword(s) | [optional] 
 **dct** | **String**| Document Type: &lt;ul&gt;&lt;li&gt;N: Notice&lt;/li&gt;&lt;li&gt;PR: Proposed Rule&lt;/li&gt;&lt;li&gt;FR: Rule&lt;/li&gt;&lt;li&gt;O: Other&lt;/li&gt;&lt;li&gt;SR: Supporting &amp; Related Material&lt;/li&gt;&lt;li&gt;PS: Public Submission&lt;/li&gt;&lt;/ul&gt; | [optional] 
 **dktid** | **String**| Valid Docket ID (ex. SEC-2012-0044) | [optional] 
 **dkt** | **String**| Docket Type: &lt;ul&gt;&lt;li&gt;R: Rulemaking&lt;/li&gt;&lt;li&gt;N: Nonrulemaking&lt;/li&gt;&lt;/ul&gt;&lt;p&gt;A Docket Type is either Rulemaking or Nonrulemaking. A Rulemaking docket includes the type of regulation that establishes a rule. While a Non-Rulemaking docket does not include a rule.&lt;/p&gt; | [optional] 
 **cp** | **String**| Comment Period: &lt;ul&gt;&lt;li&gt;O: Open&lt;/li&gt;&lt;li&gt;C: Closed&lt;/li&gt;&lt;/ul&gt; | [optional] 
 **a** | **String**| Federal Agency: List of accepted Federal Agency values. This field allows multiple values. Ex. a&#x3D;FMCSA%252BEPA%252BFDA | [optional] 
 **rpp** | **String**| Results Per Page 10, 25, 100, 500, 1,000.  Results per page may not exceed 1,000. | [optional] 
 **po** | **Number**| Enter the page offset (always starts with 0). This is used in conjunction with results per page to provide large data sets. For example, if a search produces 82 results and the result per page is set to 25, this will generate 4 pages. 3 pages will have 25 results and the last page will have 7 results. Page offset values for each page will be: &lt;pre&gt;Page 1: po&#x3D;0 Page 2: po&#x3D;25 Page 3: po&#x3D;50 Page 4: po&#x3D;75&lt;/pre&gt; The total number of pages is [total results/results per page] and page offset for page X is [X-1 * results per page] | [optional] 
 **cs** | **Number**| Comment Period Closing Soon: &lt;ul&gt;&lt;li&gt;0 (closing today)&lt;/li&gt;&lt;li&gt;3 (closing within 3 days)&lt;/li&gt;&lt;li&gt;15 (closing within 15 days)&lt;/li&gt;&lt;li&gt;30 (closing within 30 days)&lt;/li&gt;&lt;li&gt;90 (closing within 90 days)&lt;/li&gt;&lt;/ul&gt; | [optional] 
 **np** | **Number**| Newly Posted: &lt;ul&gt;&lt;li&gt;0 (posted today)&lt;/li&gt;&lt;li&gt;3 (posted within last 3 days)&lt;/li&gt;&lt;li&gt;15 (posted within last 15 days)&lt;/li&gt;&lt;li&gt;30 (posted within last 30 days)&lt;/li&gt;&lt;li&gt;90 (posted within last 90 days)&lt;/li&gt;&lt;/ul&gt;  For periods of time beyond 90-days, please use a date range with the Posted Date parameter. | [optional] 
 **cmsd** | **Date**| Comment Period Start Date: Enter a date in the form of MM/DD/YY. Note: If the Comment Period End Date is also provided, then ensure the Comment Period Start date is earlier. | [optional] 
 **cmd** | **Date**| Comment Period End Date: Enter a date in the form of MM/DD/YY. Note: If the Comment Period Start Date is also provided, then ensure the Comment Period End date is after.&lt;br/&gt;* Comment Period Start and End Dates are mutually exclusive with the &#39;closing soon&#39; parameter. If both are provided, &#39;closing soon&#39; will be ignored. | [optional] 
 **crd** | **Date**| Creation Date: Enter a date in the form of MM/DD/YY. Accepts a single date or a date range. Ex. &lt;code&gt;crd&#x3D;11/06/13-03/06/14&lt;/code&gt; | [optional] 
 **rd** | **Date**| Received Date: Enter a date in the form of MM/DD/YY. Accepts a single date or a date range. Ex. &lt;code&gt;rd&#x3D;11/06/13-03/06/14&lt;/code&gt; | [optional] 
 **pd** | **Date**| Posted Date: Enter a date in the form of MM/DD/YY. Accepts a single date or a date range. Ex. &lt;code&gt;pd&#x3D;11/06/13-03/06/14&lt;/code&gt; | [optional] 
 **cat** | **String**| Document Category: &lt;ul&gt;&lt;li&gt;AD (Aerospace and Transportation)&lt;/li&gt; &lt;li&gt;AEP (Agriculture, Environment, and Public Lands)&lt;/li&gt; &lt;li&gt;BFS (Banking and Financial)&lt;/li&gt; &lt;li&gt;CT (Commerce and International)&lt;/li&gt; &lt;li&gt;LES (Defense, Law Enforcement, and Security)&lt;/li&gt; &lt;li&gt;EELS (Education, Labor, Presidential, and Government Services)&lt;/li&gt; &lt;li&gt;EUMM (Energy, Natural Resources, and Utilities)&lt;/li&gt; &lt;li&gt;HCFP (Food Safety, Health, and Pharmaceutical)&lt;/li&gt; &lt;li&gt;PRE (Housing, Development, and Real Estate)&lt;/li&gt; &lt;li&gt;ITT (Technology and Telecommunications)&lt;/li&gt;&lt;/ul&gt; | [optional] 
 **sb** | **String**| Sort By: &lt;ul&gt;&lt;li&gt;docketId (Docket ID)&lt;/li&gt;&lt;li&gt;docId (Document ID)&lt;/li&gt;&lt;li&gt;title (Title)&lt;/li&gt;&lt;li&gt;postedDate (Posted Date)&lt;/li&gt;&lt;li&gt;agency (Agency)&lt;/li&gt;&lt;li&gt;documentType (Document Type)&lt;/li&gt;&lt;li&gt;submitterName (Submitter Name)&lt;/li&gt;&lt;li&gt;organization (Organization)&lt;/li&gt;&lt;/ul&gt; Sort Order is REQUIRED if this parameter is included. | [optional] 
 **so** | **String**| Sort Order: &lt;ul&gt;&lt;li&gt;ASC: Ascending&lt;/li&gt;&lt;li&gt;DESC: Descending&lt;/li&gt;&lt;/ul&gt; | [optional] 
 **dktst** | **String**| Docket Subtype: Only one docket subtype at a time may be selected. One or more agency values must be part of the request. Only values valid for the selected agency will be returned. | [optional] 
 **dktst2** | **String**| Docket Sub-subtype: Only one docket sub-subtype at a time may be selected. One or more agency values must be part of the request. Only values valid for the selected agency will be returned. | [optional] 
 **docst** | **String**| Document Subtype: Single or multiple document subtypes may be included.  Multiple values should be passed as follows: &lt;code&gt;docst&#x3D;%20Certificate+of+Service%252BCorrespondence&lt;/code&gt; | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

