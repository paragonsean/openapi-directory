# AmazonTextract.DefaultApi

All URIs are relative to *http://textract.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyzeDocument**](DefaultApi.md#analyzeDocument) | **POST** /#X-Amz-Target&#x3D;Textract.AnalyzeDocument | 
[**analyzeExpense**](DefaultApi.md#analyzeExpense) | **POST** /#X-Amz-Target&#x3D;Textract.AnalyzeExpense | 
[**analyzeID**](DefaultApi.md#analyzeID) | **POST** /#X-Amz-Target&#x3D;Textract.AnalyzeID | 
[**detectDocumentText**](DefaultApi.md#detectDocumentText) | **POST** /#X-Amz-Target&#x3D;Textract.DetectDocumentText | 
[**getDocumentAnalysis**](DefaultApi.md#getDocumentAnalysis) | **POST** /#X-Amz-Target&#x3D;Textract.GetDocumentAnalysis | 
[**getDocumentTextDetection**](DefaultApi.md#getDocumentTextDetection) | **POST** /#X-Amz-Target&#x3D;Textract.GetDocumentTextDetection | 
[**getExpenseAnalysis**](DefaultApi.md#getExpenseAnalysis) | **POST** /#X-Amz-Target&#x3D;Textract.GetExpenseAnalysis | 
[**getLendingAnalysis**](DefaultApi.md#getLendingAnalysis) | **POST** /#X-Amz-Target&#x3D;Textract.GetLendingAnalysis | 
[**getLendingAnalysisSummary**](DefaultApi.md#getLendingAnalysisSummary) | **POST** /#X-Amz-Target&#x3D;Textract.GetLendingAnalysisSummary | 
[**startDocumentAnalysis**](DefaultApi.md#startDocumentAnalysis) | **POST** /#X-Amz-Target&#x3D;Textract.StartDocumentAnalysis | 
[**startDocumentTextDetection**](DefaultApi.md#startDocumentTextDetection) | **POST** /#X-Amz-Target&#x3D;Textract.StartDocumentTextDetection | 
[**startExpenseAnalysis**](DefaultApi.md#startExpenseAnalysis) | **POST** /#X-Amz-Target&#x3D;Textract.StartExpenseAnalysis | 
[**startLendingAnalysis**](DefaultApi.md#startLendingAnalysis) | **POST** /#X-Amz-Target&#x3D;Textract.StartLendingAnalysis | 



## analyzeDocument

> AnalyzeDocumentResponse analyzeDocument(xAmzTarget, analyzeDocumentRequest, opts)



&lt;p&gt;Analyzes an input document for relationships between detected items. &lt;/p&gt; &lt;p&gt;The types of information returned are as follows: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Form data (key-value pairs). The related information is returned in two &lt;a&gt;Block&lt;/a&gt; objects, each of type &lt;code&gt;KEY_VALUE_SET&lt;/code&gt;: a KEY &lt;code&gt;Block&lt;/code&gt; object and a VALUE &lt;code&gt;Block&lt;/code&gt; object. For example, &lt;i&gt;Name: Ana Silva Carolina&lt;/i&gt; contains a key and value. &lt;i&gt;Name:&lt;/i&gt; is the key. &lt;i&gt;Ana Silva Carolina&lt;/i&gt; is the value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Table and table cell data. A TABLE &lt;code&gt;Block&lt;/code&gt; object contains information about a detected table. A CELL &lt;code&gt;Block&lt;/code&gt; object is returned for each cell in a table.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Lines and words of text. A LINE &lt;code&gt;Block&lt;/code&gt; object contains one or more WORD &lt;code&gt;Block&lt;/code&gt; objects. All lines and words that are detected in the document are returned (including text that doesn&#39;t have a relationship with the value of &lt;code&gt;FeatureTypes&lt;/code&gt;). &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Signatures. A SIGNATURE &lt;code&gt;Block&lt;/code&gt; object contains the location information of a signature in a document. If used in conjunction with forms or tables, a signature can be given a Key-Value pairing or be detected in the cell of a table.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Query. A QUERY Block object contains the query text, alias and link to the associated Query results block object.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Query Result. A QUERY_RESULT Block object contains the answer to the query and an ID that connects it to the query asked. This Block also contains a confidence score.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Selection elements such as check boxes and option buttons (radio buttons) can be detected in form data and in tables. A SELECTION_ELEMENT &lt;code&gt;Block&lt;/code&gt; object contains information about a selection element, including the selection status.&lt;/p&gt; &lt;p&gt;You can choose which type of analysis to perform by specifying the &lt;code&gt;FeatureTypes&lt;/code&gt; list. &lt;/p&gt; &lt;p&gt;The output is returned in a list of &lt;code&gt;Block&lt;/code&gt; objects.&lt;/p&gt; &lt;p&gt; &lt;code&gt;AnalyzeDocument&lt;/code&gt; is a synchronous operation. To analyze documents asynchronously, use &lt;a&gt;StartDocumentAnalysis&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html\&quot;&gt;Document Text Analysis&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonTextract from 'amazon_textract';
let defaultClient = AmazonTextract.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTextract.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let analyzeDocumentRequest = new AmazonTextract.AnalyzeDocumentRequest(); // AnalyzeDocumentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.analyzeDocument(xAmzTarget, analyzeDocumentRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **analyzeDocumentRequest** | [**AnalyzeDocumentRequest**](AnalyzeDocumentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AnalyzeDocumentResponse**](AnalyzeDocumentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## analyzeExpense

> AnalyzeExpenseResponse analyzeExpense(xAmzTarget, analyzeExpenseRequest, opts)



&lt;p&gt; &lt;code&gt;AnalyzeExpense&lt;/code&gt; synchronously analyzes an input document for financially related relationships between text.&lt;/p&gt; &lt;p&gt;Information is returned as &lt;code&gt;ExpenseDocuments&lt;/code&gt; and seperated as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LineItemGroups&lt;/code&gt;- A data set containing &lt;code&gt;LineItems&lt;/code&gt; which store information about the lines of text, such as an item purchased and its price on a receipt.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SummaryFields&lt;/code&gt;- Contains all other information a receipt, such as header information or the vendors name.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonTextract from 'amazon_textract';
let defaultClient = AmazonTextract.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTextract.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let analyzeExpenseRequest = new AmazonTextract.AnalyzeExpenseRequest(); // AnalyzeExpenseRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.analyzeExpense(xAmzTarget, analyzeExpenseRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **analyzeExpenseRequest** | [**AnalyzeExpenseRequest**](AnalyzeExpenseRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AnalyzeExpenseResponse**](AnalyzeExpenseResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## analyzeID

> AnalyzeIDResponse analyzeID(xAmzTarget, analyzeIDRequest, opts)



Analyzes identity documents for relevant information. This information is extracted and returned as &lt;code&gt;IdentityDocumentFields&lt;/code&gt;, which records both the normalized field and value of the extracted text. Unlike other Amazon Textract operations, &lt;code&gt;AnalyzeID&lt;/code&gt; doesn&#39;t return any Geometry data.

### Example

```javascript
import AmazonTextract from 'amazon_textract';
let defaultClient = AmazonTextract.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTextract.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let analyzeIDRequest = new AmazonTextract.AnalyzeIDRequest(); // AnalyzeIDRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.analyzeID(xAmzTarget, analyzeIDRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **analyzeIDRequest** | [**AnalyzeIDRequest**](AnalyzeIDRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AnalyzeIDResponse**](AnalyzeIDResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## detectDocumentText

> DetectDocumentTextResponse detectDocumentText(xAmzTarget, detectDocumentTextRequest, opts)



&lt;p&gt;Detects text in the input document. Amazon Textract can detect lines of text and the words that make up a line of text. The input document must be in one of the following image formats: JPEG, PNG, PDF, or TIFF. &lt;code&gt;DetectDocumentText&lt;/code&gt; returns the detected text in an array of &lt;a&gt;Block&lt;/a&gt; objects. &lt;/p&gt; &lt;p&gt;Each document page has as an associated &lt;code&gt;Block&lt;/code&gt; of type PAGE. Each PAGE &lt;code&gt;Block&lt;/code&gt; object is the parent of LINE &lt;code&gt;Block&lt;/code&gt; objects that represent the lines of detected text on a page. A LINE &lt;code&gt;Block&lt;/code&gt; object is a parent for each word that makes up the line. Words are represented by &lt;code&gt;Block&lt;/code&gt; objects of type WORD.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DetectDocumentText&lt;/code&gt; is a synchronous operation. To analyze documents asynchronously, use &lt;a&gt;StartDocumentTextDetection&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html\&quot;&gt;Document Text Detection&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonTextract from 'amazon_textract';
let defaultClient = AmazonTextract.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTextract.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let detectDocumentTextRequest = new AmazonTextract.DetectDocumentTextRequest(); // DetectDocumentTextRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.detectDocumentText(xAmzTarget, detectDocumentTextRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **detectDocumentTextRequest** | [**DetectDocumentTextRequest**](DetectDocumentTextRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DetectDocumentTextResponse**](DetectDocumentTextResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getDocumentAnalysis

> GetDocumentAnalysisResponse getDocumentAnalysis(xAmzTarget, getDocumentAnalysisRequest, opts)



&lt;p&gt;Gets the results for an Amazon Textract asynchronous operation that analyzes text in a document.&lt;/p&gt; &lt;p&gt;You start asynchronous text analysis by calling &lt;a&gt;StartDocumentAnalysis&lt;/a&gt;, which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). When the text analysis operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that&#39;s registered in the initial call to &lt;code&gt;StartDocumentAnalysis&lt;/code&gt;. To get the results of the text-detection operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;code&gt;GetDocumentAnalysis&lt;/code&gt;, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartDocumentAnalysis&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetDocumentAnalysis&lt;/code&gt; returns an array of &lt;a&gt;Block&lt;/a&gt; objects. The following types of information are returned: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Form data (key-value pairs). The related information is returned in two &lt;a&gt;Block&lt;/a&gt; objects, each of type &lt;code&gt;KEY_VALUE_SET&lt;/code&gt;: a KEY &lt;code&gt;Block&lt;/code&gt; object and a VALUE &lt;code&gt;Block&lt;/code&gt; object. For example, &lt;i&gt;Name: Ana Silva Carolina&lt;/i&gt; contains a key and value. &lt;i&gt;Name:&lt;/i&gt; is the key. &lt;i&gt;Ana Silva Carolina&lt;/i&gt; is the value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Table and table cell data. A TABLE &lt;code&gt;Block&lt;/code&gt; object contains information about a detected table. A CELL &lt;code&gt;Block&lt;/code&gt; object is returned for each cell in a table.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Lines and words of text. A LINE &lt;code&gt;Block&lt;/code&gt; object contains one or more WORD &lt;code&gt;Block&lt;/code&gt; objects. All lines and words that are detected in the document are returned (including text that doesn&#39;t have a relationship with the value of the &lt;code&gt;StartDocumentAnalysis&lt;/code&gt; &lt;code&gt;FeatureTypes&lt;/code&gt; input parameter). &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Query. A QUERY Block object contains the query text, alias and link to the associated Query results block object.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Query Results. A QUERY_RESULT Block object contains the answer to the query and an ID that connects it to the query asked. This Block also contains a confidence score.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;While processing a document with queries, look out for &lt;code&gt;INVALID_REQUEST_PARAMETERS&lt;/code&gt; output. This indicates that either the per page query limit has been exceeded or that the operation is trying to query a page in the document which doesn’t exist. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Selection elements such as check boxes and option buttons (radio buttons) can be detected in form data and in tables. A SELECTION_ELEMENT &lt;code&gt;Block&lt;/code&gt; object contains information about a selection element, including the selection status.&lt;/p&gt; &lt;p&gt;Use the &lt;code&gt;MaxResults&lt;/code&gt; parameter to limit the number of blocks that are returned. If there are more results than specified in &lt;code&gt;MaxResults&lt;/code&gt;, the value of &lt;code&gt;NextToken&lt;/code&gt; in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call &lt;code&gt;GetDocumentAnalysis&lt;/code&gt;, and populate the &lt;code&gt;NextToken&lt;/code&gt; request parameter with the token value that&#39;s returned from the previous call to &lt;code&gt;GetDocumentAnalysis&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html\&quot;&gt;Document Text Analysis&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonTextract from 'amazon_textract';
let defaultClient = AmazonTextract.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTextract.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getDocumentAnalysisRequest = new AmazonTextract.GetDocumentAnalysisRequest(); // GetDocumentAnalysisRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDocumentAnalysis(xAmzTarget, getDocumentAnalysisRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **getDocumentAnalysisRequest** | [**GetDocumentAnalysisRequest**](GetDocumentAnalysisRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDocumentAnalysisResponse**](GetDocumentAnalysisResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getDocumentTextDetection

> GetDocumentTextDetectionResponse getDocumentTextDetection(xAmzTarget, getDocumentTextDetectionRequest, opts)



&lt;p&gt;Gets the results for an Amazon Textract asynchronous operation that detects text in a document. Amazon Textract can detect lines of text and the words that make up a line of text.&lt;/p&gt; &lt;p&gt;You start asynchronous text detection by calling &lt;a&gt;StartDocumentTextDetection&lt;/a&gt;, which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). When the text detection operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that&#39;s registered in the initial call to &lt;code&gt;StartDocumentTextDetection&lt;/code&gt;. To get the results of the text-detection operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;code&gt;GetDocumentTextDetection&lt;/code&gt;, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartDocumentTextDetection&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetDocumentTextDetection&lt;/code&gt; returns an array of &lt;a&gt;Block&lt;/a&gt; objects. &lt;/p&gt; &lt;p&gt;Each document page has as an associated &lt;code&gt;Block&lt;/code&gt; of type PAGE. Each PAGE &lt;code&gt;Block&lt;/code&gt; object is the parent of LINE &lt;code&gt;Block&lt;/code&gt; objects that represent the lines of detected text on a page. A LINE &lt;code&gt;Block&lt;/code&gt; object is a parent for each word that makes up the line. Words are represented by &lt;code&gt;Block&lt;/code&gt; objects of type WORD.&lt;/p&gt; &lt;p&gt;Use the MaxResults parameter to limit the number of blocks that are returned. If there are more results than specified in &lt;code&gt;MaxResults&lt;/code&gt;, the value of &lt;code&gt;NextToken&lt;/code&gt; in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call &lt;code&gt;GetDocumentTextDetection&lt;/code&gt;, and populate the &lt;code&gt;NextToken&lt;/code&gt; request parameter with the token value that&#39;s returned from the previous call to &lt;code&gt;GetDocumentTextDetection&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html\&quot;&gt;Document Text Detection&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonTextract from 'amazon_textract';
let defaultClient = AmazonTextract.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTextract.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getDocumentTextDetectionRequest = new AmazonTextract.GetDocumentTextDetectionRequest(); // GetDocumentTextDetectionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDocumentTextDetection(xAmzTarget, getDocumentTextDetectionRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **getDocumentTextDetectionRequest** | [**GetDocumentTextDetectionRequest**](GetDocumentTextDetectionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDocumentTextDetectionResponse**](GetDocumentTextDetectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getExpenseAnalysis

> GetExpenseAnalysisResponse getExpenseAnalysis(xAmzTarget, getExpenseAnalysisRequest, opts)



&lt;p&gt;Gets the results for an Amazon Textract asynchronous operation that analyzes invoices and receipts. Amazon Textract finds contact information, items purchased, and vendor name, from input invoices and receipts.&lt;/p&gt; &lt;p&gt;You start asynchronous invoice/receipt analysis by calling &lt;a&gt;StartExpenseAnalysis&lt;/a&gt;, which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). Upon completion of the invoice/receipt analysis, Amazon Textract publishes the completion status to the Amazon Simple Notification Service (Amazon SNS) topic. This topic must be registered in the initial call to &lt;code&gt;StartExpenseAnalysis&lt;/code&gt;. To get the results of the invoice/receipt analysis operation, first ensure that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;code&gt;GetExpenseAnalysis&lt;/code&gt;, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartExpenseAnalysis&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Use the MaxResults parameter to limit the number of blocks that are returned. If there are more results than specified in &lt;code&gt;MaxResults&lt;/code&gt;, the value of &lt;code&gt;NextToken&lt;/code&gt; in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call &lt;code&gt;GetExpenseAnalysis&lt;/code&gt;, and populate the &lt;code&gt;NextToken&lt;/code&gt; request parameter with the token value that&#39;s returned from the previous call to &lt;code&gt;GetExpenseAnalysis&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/invoices-receipts.html\&quot;&gt;Analyzing Invoices and Receipts&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonTextract from 'amazon_textract';
let defaultClient = AmazonTextract.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTextract.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getExpenseAnalysisRequest = new AmazonTextract.GetExpenseAnalysisRequest(); // GetExpenseAnalysisRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getExpenseAnalysis(xAmzTarget, getExpenseAnalysisRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **getExpenseAnalysisRequest** | [**GetExpenseAnalysisRequest**](GetExpenseAnalysisRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetExpenseAnalysisResponse**](GetExpenseAnalysisResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getLendingAnalysis

> GetLendingAnalysisResponse getLendingAnalysis(xAmzTarget, getLendingAnalysisRequest, opts)



&lt;p&gt;Gets the results for an Amazon Textract asynchronous operation that analyzes text in a lending document. &lt;/p&gt; &lt;p&gt;You start asynchronous text analysis by calling &lt;code&gt;StartLendingAnalysis&lt;/code&gt;, which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). When the text analysis operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that&#39;s registered in the initial call to &lt;code&gt;StartLendingAnalysis&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED. If so, call GetLendingAnalysis, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartLendingAnalysis&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonTextract from 'amazon_textract';
let defaultClient = AmazonTextract.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTextract.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getLendingAnalysisRequest = new AmazonTextract.GetLendingAnalysisRequest(); // GetLendingAnalysisRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getLendingAnalysis(xAmzTarget, getLendingAnalysisRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **getLendingAnalysisRequest** | [**GetLendingAnalysisRequest**](GetLendingAnalysisRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetLendingAnalysisResponse**](GetLendingAnalysisResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getLendingAnalysisSummary

> GetLendingAnalysisSummaryResponse getLendingAnalysisSummary(xAmzTarget, getLendingAnalysisSummaryRequest, opts)



&lt;p&gt;Gets summarized results for the &lt;code&gt;StartLendingAnalysis&lt;/code&gt; operation, which analyzes text in a lending document. The returned summary consists of information about documents grouped together by a common document type. Information like detected signatures, page numbers, and split documents is returned with respect to the type of grouped document. &lt;/p&gt; &lt;p&gt;You start asynchronous text analysis by calling &lt;code&gt;StartLendingAnalysis&lt;/code&gt;, which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). When the text analysis operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that&#39;s registered in the initial call to &lt;code&gt;StartLendingAnalysis&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED. If so, call &lt;code&gt;GetLendingAnalysisSummary&lt;/code&gt;, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartLendingAnalysis&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonTextract from 'amazon_textract';
let defaultClient = AmazonTextract.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTextract.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getLendingAnalysisSummaryRequest = new AmazonTextract.GetLendingAnalysisSummaryRequest(); // GetLendingAnalysisSummaryRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getLendingAnalysisSummary(xAmzTarget, getLendingAnalysisSummaryRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **getLendingAnalysisSummaryRequest** | [**GetLendingAnalysisSummaryRequest**](GetLendingAnalysisSummaryRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetLendingAnalysisSummaryResponse**](GetLendingAnalysisSummaryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startDocumentAnalysis

> StartDocumentAnalysisResponse startDocumentAnalysis(xAmzTarget, startDocumentAnalysisRequest, opts)



&lt;p&gt;Starts the asynchronous analysis of an input document for relationships between detected items such as key-value pairs, tables, and selection elements.&lt;/p&gt; &lt;p&gt; &lt;code&gt;StartDocumentAnalysis&lt;/code&gt; can analyze text in documents that are in JPEG, PNG, TIFF, and PDF format. The documents are stored in an Amazon S3 bucket. Use &lt;a&gt;DocumentLocation&lt;/a&gt; to specify the bucket name and file name of the document. &lt;/p&gt; &lt;p&gt; &lt;code&gt;StartDocumentAnalysis&lt;/code&gt; returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;) that you use to get the results of the operation. When text analysis is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you specify in &lt;code&gt;NotificationChannel&lt;/code&gt;. To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;a&gt;GetDocumentAnalysis&lt;/a&gt;, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartDocumentAnalysis&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html\&quot;&gt;Document Text Analysis&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonTextract from 'amazon_textract';
let defaultClient = AmazonTextract.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTextract.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startDocumentAnalysisRequest = new AmazonTextract.StartDocumentAnalysisRequest(); // StartDocumentAnalysisRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startDocumentAnalysis(xAmzTarget, startDocumentAnalysisRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **startDocumentAnalysisRequest** | [**StartDocumentAnalysisRequest**](StartDocumentAnalysisRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartDocumentAnalysisResponse**](StartDocumentAnalysisResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startDocumentTextDetection

> StartDocumentTextDetectionResponse startDocumentTextDetection(xAmzTarget, startDocumentTextDetectionRequest, opts)



&lt;p&gt;Starts the asynchronous detection of text in a document. Amazon Textract can detect lines of text and the words that make up a line of text.&lt;/p&gt; &lt;p&gt; &lt;code&gt;StartDocumentTextDetection&lt;/code&gt; can analyze text in documents that are in JPEG, PNG, TIFF, and PDF format. The documents are stored in an Amazon S3 bucket. Use &lt;a&gt;DocumentLocation&lt;/a&gt; to specify the bucket name and file name of the document. &lt;/p&gt; &lt;p&gt; &lt;code&gt;StartTextDetection&lt;/code&gt; returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;) that you use to get the results of the operation. When text detection is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you specify in &lt;code&gt;NotificationChannel&lt;/code&gt;. To get the results of the text detection operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;a&gt;GetDocumentTextDetection&lt;/a&gt;, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartDocumentTextDetection&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html\&quot;&gt;Document Text Detection&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonTextract from 'amazon_textract';
let defaultClient = AmazonTextract.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTextract.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startDocumentTextDetectionRequest = new AmazonTextract.StartDocumentTextDetectionRequest(); // StartDocumentTextDetectionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startDocumentTextDetection(xAmzTarget, startDocumentTextDetectionRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **startDocumentTextDetectionRequest** | [**StartDocumentTextDetectionRequest**](StartDocumentTextDetectionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartDocumentTextDetectionResponse**](StartDocumentTextDetectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startExpenseAnalysis

> StartExpenseAnalysisResponse startExpenseAnalysis(xAmzTarget, startExpenseAnalysisRequest, opts)



&lt;p&gt;Starts the asynchronous analysis of invoices or receipts for data like contact information, items purchased, and vendor names.&lt;/p&gt; &lt;p&gt; &lt;code&gt;StartExpenseAnalysis&lt;/code&gt; can analyze text in documents that are in JPEG, PNG, and PDF format. The documents must be stored in an Amazon S3 bucket. Use the &lt;a&gt;DocumentLocation&lt;/a&gt; parameter to specify the name of your S3 bucket and the name of the document in that bucket. &lt;/p&gt; &lt;p&gt; &lt;code&gt;StartExpenseAnalysis&lt;/code&gt; returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;) that you will provide to &lt;code&gt;GetExpenseAnalysis&lt;/code&gt; to retrieve the results of the operation. When the analysis of the input invoices/receipts is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you provide to the &lt;code&gt;NotificationChannel&lt;/code&gt;. To obtain the results of the invoice and receipt analysis operation, ensure that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;a&gt;GetExpenseAnalysis&lt;/a&gt;, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) that was returned by your call to &lt;code&gt;StartExpenseAnalysis&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/invoice-receipts.html\&quot;&gt;Analyzing Invoices and Receipts&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonTextract from 'amazon_textract';
let defaultClient = AmazonTextract.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTextract.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startExpenseAnalysisRequest = new AmazonTextract.StartExpenseAnalysisRequest(); // StartExpenseAnalysisRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startExpenseAnalysis(xAmzTarget, startExpenseAnalysisRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **startExpenseAnalysisRequest** | [**StartExpenseAnalysisRequest**](StartExpenseAnalysisRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartExpenseAnalysisResponse**](StartExpenseAnalysisResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startLendingAnalysis

> StartLendingAnalysisResponse startLendingAnalysis(xAmzTarget, startLendingAnalysisRequest, opts)



&lt;p&gt;Starts the classification and analysis of an input document. &lt;code&gt;StartLendingAnalysis&lt;/code&gt; initiates the classification and analysis of a packet of lending documents. &lt;code&gt;StartLendingAnalysis&lt;/code&gt; operates on a document file located in an Amazon S3 bucket.&lt;/p&gt; &lt;p&gt; &lt;code&gt;StartLendingAnalysis&lt;/code&gt; can analyze text in documents that are in one of the following formats: JPEG, PNG, TIFF, PDF. Use &lt;code&gt;DocumentLocation&lt;/code&gt; to specify the bucket name and the file name of the document. &lt;/p&gt; &lt;p&gt; &lt;code&gt;StartLendingAnalysis&lt;/code&gt; returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;) that you use to get the results of the operation. When the text analysis is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you specify in &lt;code&gt;NotificationChannel&lt;/code&gt;. To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED. If the status is SUCCEEDED you can call either &lt;code&gt;GetLendingAnalysis&lt;/code&gt; or &lt;code&gt;GetLendingAnalysisSummary&lt;/code&gt; and provide the &lt;code&gt;JobId&lt;/code&gt; to obtain the results of the analysis.&lt;/p&gt; &lt;p&gt;If using &lt;code&gt;OutputConfig&lt;/code&gt; to specify an Amazon S3 bucket, the output will be contained within the specified prefix in a directory labeled with the job-id. In the directory there are 3 sub-directories: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;detailedResponse (contains the GetLendingAnalysis response)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;summaryResponse (for the GetLendingAnalysisSummary response)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;splitDocuments (documents split across logical boundaries)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonTextract from 'amazon_textract';
let defaultClient = AmazonTextract.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTextract.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startLendingAnalysisRequest = new AmazonTextract.StartLendingAnalysisRequest(); // StartLendingAnalysisRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startLendingAnalysis(xAmzTarget, startLendingAnalysisRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **startLendingAnalysisRequest** | [**StartLendingAnalysisRequest**](StartLendingAnalysisRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartLendingAnalysisResponse**](StartLendingAnalysisResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

