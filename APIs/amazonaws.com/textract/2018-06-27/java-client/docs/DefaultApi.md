# DefaultApi

All URIs are relative to *http://textract.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**analyzeDocument**](DefaultApi.md#analyzeDocument) | **POST** /#X-Amz-Target&#x3D;Textract.AnalyzeDocument |  |
| [**analyzeExpense**](DefaultApi.md#analyzeExpense) | **POST** /#X-Amz-Target&#x3D;Textract.AnalyzeExpense |  |
| [**analyzeID**](DefaultApi.md#analyzeID) | **POST** /#X-Amz-Target&#x3D;Textract.AnalyzeID |  |
| [**detectDocumentText**](DefaultApi.md#detectDocumentText) | **POST** /#X-Amz-Target&#x3D;Textract.DetectDocumentText |  |
| [**getDocumentAnalysis**](DefaultApi.md#getDocumentAnalysis) | **POST** /#X-Amz-Target&#x3D;Textract.GetDocumentAnalysis |  |
| [**getDocumentTextDetection**](DefaultApi.md#getDocumentTextDetection) | **POST** /#X-Amz-Target&#x3D;Textract.GetDocumentTextDetection |  |
| [**getExpenseAnalysis**](DefaultApi.md#getExpenseAnalysis) | **POST** /#X-Amz-Target&#x3D;Textract.GetExpenseAnalysis |  |
| [**getLendingAnalysis**](DefaultApi.md#getLendingAnalysis) | **POST** /#X-Amz-Target&#x3D;Textract.GetLendingAnalysis |  |
| [**getLendingAnalysisSummary**](DefaultApi.md#getLendingAnalysisSummary) | **POST** /#X-Amz-Target&#x3D;Textract.GetLendingAnalysisSummary |  |
| [**startDocumentAnalysis**](DefaultApi.md#startDocumentAnalysis) | **POST** /#X-Amz-Target&#x3D;Textract.StartDocumentAnalysis |  |
| [**startDocumentTextDetection**](DefaultApi.md#startDocumentTextDetection) | **POST** /#X-Amz-Target&#x3D;Textract.StartDocumentTextDetection |  |
| [**startExpenseAnalysis**](DefaultApi.md#startExpenseAnalysis) | **POST** /#X-Amz-Target&#x3D;Textract.StartExpenseAnalysis |  |
| [**startLendingAnalysis**](DefaultApi.md#startLendingAnalysis) | **POST** /#X-Amz-Target&#x3D;Textract.StartLendingAnalysis |  |


<a id="analyzeDocument"></a>
# **analyzeDocument**
> AnalyzeDocumentResponse analyzeDocument(xAmzTarget, analyzeDocumentRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Analyzes an input document for relationships between detected items. &lt;/p&gt; &lt;p&gt;The types of information returned are as follows: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Form data (key-value pairs). The related information is returned in two &lt;a&gt;Block&lt;/a&gt; objects, each of type &lt;code&gt;KEY_VALUE_SET&lt;/code&gt;: a KEY &lt;code&gt;Block&lt;/code&gt; object and a VALUE &lt;code&gt;Block&lt;/code&gt; object. For example, &lt;i&gt;Name: Ana Silva Carolina&lt;/i&gt; contains a key and value. &lt;i&gt;Name:&lt;/i&gt; is the key. &lt;i&gt;Ana Silva Carolina&lt;/i&gt; is the value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Table and table cell data. A TABLE &lt;code&gt;Block&lt;/code&gt; object contains information about a detected table. A CELL &lt;code&gt;Block&lt;/code&gt; object is returned for each cell in a table.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Lines and words of text. A LINE &lt;code&gt;Block&lt;/code&gt; object contains one or more WORD &lt;code&gt;Block&lt;/code&gt; objects. All lines and words that are detected in the document are returned (including text that doesn&#39;t have a relationship with the value of &lt;code&gt;FeatureTypes&lt;/code&gt;). &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Signatures. A SIGNATURE &lt;code&gt;Block&lt;/code&gt; object contains the location information of a signature in a document. If used in conjunction with forms or tables, a signature can be given a Key-Value pairing or be detected in the cell of a table.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Query. A QUERY Block object contains the query text, alias and link to the associated Query results block object.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Query Result. A QUERY_RESULT Block object contains the answer to the query and an ID that connects it to the query asked. This Block also contains a confidence score.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Selection elements such as check boxes and option buttons (radio buttons) can be detected in form data and in tables. A SELECTION_ELEMENT &lt;code&gt;Block&lt;/code&gt; object contains information about a selection element, including the selection status.&lt;/p&gt; &lt;p&gt;You can choose which type of analysis to perform by specifying the &lt;code&gt;FeatureTypes&lt;/code&gt; list. &lt;/p&gt; &lt;p&gt;The output is returned in a list of &lt;code&gt;Block&lt;/code&gt; objects.&lt;/p&gt; &lt;p&gt; &lt;code&gt;AnalyzeDocument&lt;/code&gt; is a synchronous operation. To analyze documents asynchronously, use &lt;a&gt;StartDocumentAnalysis&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html\&quot;&gt;Document Text Analysis&lt;/a&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://textract.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "Textract.AnalyzeDocument"; // String | 
    AnalyzeDocumentRequest analyzeDocumentRequest = new AnalyzeDocumentRequest(); // AnalyzeDocumentRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      AnalyzeDocumentResponse result = apiInstance.analyzeDocument(xAmzTarget, analyzeDocumentRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#analyzeDocument");
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
| **xAmzTarget** | **String**|  | [enum: Textract.AnalyzeDocument] |
| **analyzeDocumentRequest** | [**AnalyzeDocumentRequest**](AnalyzeDocumentRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**AnalyzeDocumentResponse**](AnalyzeDocumentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | InvalidS3ObjectException |  -  |
| **482** | UnsupportedDocumentException |  -  |
| **483** | DocumentTooLargeException |  -  |
| **484** | BadDocumentException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ProvisionedThroughputExceededException |  -  |
| **487** | InternalServerError |  -  |
| **488** | ThrottlingException |  -  |
| **489** | HumanLoopQuotaExceededException |  -  |

<a id="analyzeExpense"></a>
# **analyzeExpense**
> AnalyzeExpenseResponse analyzeExpense(xAmzTarget, analyzeExpenseRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt; &lt;code&gt;AnalyzeExpense&lt;/code&gt; synchronously analyzes an input document for financially related relationships between text.&lt;/p&gt; &lt;p&gt;Information is returned as &lt;code&gt;ExpenseDocuments&lt;/code&gt; and seperated as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LineItemGroups&lt;/code&gt;- A data set containing &lt;code&gt;LineItems&lt;/code&gt; which store information about the lines of text, such as an item purchased and its price on a receipt.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SummaryFields&lt;/code&gt;- Contains all other information a receipt, such as header information or the vendors name.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://textract.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "Textract.AnalyzeExpense"; // String | 
    AnalyzeExpenseRequest analyzeExpenseRequest = new AnalyzeExpenseRequest(); // AnalyzeExpenseRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      AnalyzeExpenseResponse result = apiInstance.analyzeExpense(xAmzTarget, analyzeExpenseRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#analyzeExpense");
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
| **xAmzTarget** | **String**|  | [enum: Textract.AnalyzeExpense] |
| **analyzeExpenseRequest** | [**AnalyzeExpenseRequest**](AnalyzeExpenseRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**AnalyzeExpenseResponse**](AnalyzeExpenseResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | InvalidS3ObjectException |  -  |
| **482** | UnsupportedDocumentException |  -  |
| **483** | DocumentTooLargeException |  -  |
| **484** | BadDocumentException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ProvisionedThroughputExceededException |  -  |
| **487** | InternalServerError |  -  |
| **488** | ThrottlingException |  -  |

<a id="analyzeID"></a>
# **analyzeID**
> AnalyzeIDResponse analyzeID(xAmzTarget, analyzeIDRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Analyzes identity documents for relevant information. This information is extracted and returned as &lt;code&gt;IdentityDocumentFields&lt;/code&gt;, which records both the normalized field and value of the extracted text. Unlike other Amazon Textract operations, &lt;code&gt;AnalyzeID&lt;/code&gt; doesn&#39;t return any Geometry data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://textract.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "Textract.AnalyzeID"; // String | 
    AnalyzeIDRequest analyzeIDRequest = new AnalyzeIDRequest(); // AnalyzeIDRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      AnalyzeIDResponse result = apiInstance.analyzeID(xAmzTarget, analyzeIDRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#analyzeID");
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
| **xAmzTarget** | **String**|  | [enum: Textract.AnalyzeID] |
| **analyzeIDRequest** | [**AnalyzeIDRequest**](AnalyzeIDRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**AnalyzeIDResponse**](AnalyzeIDResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | InvalidS3ObjectException |  -  |
| **482** | UnsupportedDocumentException |  -  |
| **483** | DocumentTooLargeException |  -  |
| **484** | BadDocumentException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ProvisionedThroughputExceededException |  -  |
| **487** | InternalServerError |  -  |
| **488** | ThrottlingException |  -  |

<a id="detectDocumentText"></a>
# **detectDocumentText**
> DetectDocumentTextResponse detectDocumentText(xAmzTarget, detectDocumentTextRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Detects text in the input document. Amazon Textract can detect lines of text and the words that make up a line of text. The input document must be in one of the following image formats: JPEG, PNG, PDF, or TIFF. &lt;code&gt;DetectDocumentText&lt;/code&gt; returns the detected text in an array of &lt;a&gt;Block&lt;/a&gt; objects. &lt;/p&gt; &lt;p&gt;Each document page has as an associated &lt;code&gt;Block&lt;/code&gt; of type PAGE. Each PAGE &lt;code&gt;Block&lt;/code&gt; object is the parent of LINE &lt;code&gt;Block&lt;/code&gt; objects that represent the lines of detected text on a page. A LINE &lt;code&gt;Block&lt;/code&gt; object is a parent for each word that makes up the line. Words are represented by &lt;code&gt;Block&lt;/code&gt; objects of type WORD.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DetectDocumentText&lt;/code&gt; is a synchronous operation. To analyze documents asynchronously, use &lt;a&gt;StartDocumentTextDetection&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html\&quot;&gt;Document Text Detection&lt;/a&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://textract.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "Textract.DetectDocumentText"; // String | 
    DetectDocumentTextRequest detectDocumentTextRequest = new DetectDocumentTextRequest(); // DetectDocumentTextRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DetectDocumentTextResponse result = apiInstance.detectDocumentText(xAmzTarget, detectDocumentTextRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#detectDocumentText");
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
| **xAmzTarget** | **String**|  | [enum: Textract.DetectDocumentText] |
| **detectDocumentTextRequest** | [**DetectDocumentTextRequest**](DetectDocumentTextRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DetectDocumentTextResponse**](DetectDocumentTextResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | InvalidS3ObjectException |  -  |
| **482** | UnsupportedDocumentException |  -  |
| **483** | DocumentTooLargeException |  -  |
| **484** | BadDocumentException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ProvisionedThroughputExceededException |  -  |
| **487** | InternalServerError |  -  |
| **488** | ThrottlingException |  -  |

<a id="getDocumentAnalysis"></a>
# **getDocumentAnalysis**
> GetDocumentAnalysisResponse getDocumentAnalysis(xAmzTarget, getDocumentAnalysisRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets the results for an Amazon Textract asynchronous operation that analyzes text in a document.&lt;/p&gt; &lt;p&gt;You start asynchronous text analysis by calling &lt;a&gt;StartDocumentAnalysis&lt;/a&gt;, which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). When the text analysis operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that&#39;s registered in the initial call to &lt;code&gt;StartDocumentAnalysis&lt;/code&gt;. To get the results of the text-detection operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;code&gt;GetDocumentAnalysis&lt;/code&gt;, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartDocumentAnalysis&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetDocumentAnalysis&lt;/code&gt; returns an array of &lt;a&gt;Block&lt;/a&gt; objects. The following types of information are returned: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Form data (key-value pairs). The related information is returned in two &lt;a&gt;Block&lt;/a&gt; objects, each of type &lt;code&gt;KEY_VALUE_SET&lt;/code&gt;: a KEY &lt;code&gt;Block&lt;/code&gt; object and a VALUE &lt;code&gt;Block&lt;/code&gt; object. For example, &lt;i&gt;Name: Ana Silva Carolina&lt;/i&gt; contains a key and value. &lt;i&gt;Name:&lt;/i&gt; is the key. &lt;i&gt;Ana Silva Carolina&lt;/i&gt; is the value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Table and table cell data. A TABLE &lt;code&gt;Block&lt;/code&gt; object contains information about a detected table. A CELL &lt;code&gt;Block&lt;/code&gt; object is returned for each cell in a table.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Lines and words of text. A LINE &lt;code&gt;Block&lt;/code&gt; object contains one or more WORD &lt;code&gt;Block&lt;/code&gt; objects. All lines and words that are detected in the document are returned (including text that doesn&#39;t have a relationship with the value of the &lt;code&gt;StartDocumentAnalysis&lt;/code&gt; &lt;code&gt;FeatureTypes&lt;/code&gt; input parameter). &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Query. A QUERY Block object contains the query text, alias and link to the associated Query results block object.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Query Results. A QUERY_RESULT Block object contains the answer to the query and an ID that connects it to the query asked. This Block also contains a confidence score.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;While processing a document with queries, look out for &lt;code&gt;INVALID_REQUEST_PARAMETERS&lt;/code&gt; output. This indicates that either the per page query limit has been exceeded or that the operation is trying to query a page in the document which doesn’t exist. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Selection elements such as check boxes and option buttons (radio buttons) can be detected in form data and in tables. A SELECTION_ELEMENT &lt;code&gt;Block&lt;/code&gt; object contains information about a selection element, including the selection status.&lt;/p&gt; &lt;p&gt;Use the &lt;code&gt;MaxResults&lt;/code&gt; parameter to limit the number of blocks that are returned. If there are more results than specified in &lt;code&gt;MaxResults&lt;/code&gt;, the value of &lt;code&gt;NextToken&lt;/code&gt; in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call &lt;code&gt;GetDocumentAnalysis&lt;/code&gt;, and populate the &lt;code&gt;NextToken&lt;/code&gt; request parameter with the token value that&#39;s returned from the previous call to &lt;code&gt;GetDocumentAnalysis&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html\&quot;&gt;Document Text Analysis&lt;/a&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://textract.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "Textract.GetDocumentAnalysis"; // String | 
    GetDocumentAnalysisRequest getDocumentAnalysisRequest = new GetDocumentAnalysisRequest(); // GetDocumentAnalysisRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetDocumentAnalysisResponse result = apiInstance.getDocumentAnalysis(xAmzTarget, getDocumentAnalysisRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDocumentAnalysis");
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
| **xAmzTarget** | **String**|  | [enum: Textract.GetDocumentAnalysis] |
| **getDocumentAnalysisRequest** | [**GetDocumentAnalysisRequest**](GetDocumentAnalysisRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetDocumentAnalysisResponse**](GetDocumentAnalysisResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | AccessDeniedException |  -  |
| **482** | ProvisionedThroughputExceededException |  -  |
| **483** | InvalidJobIdException |  -  |
| **484** | InternalServerError |  -  |
| **485** | ThrottlingException |  -  |
| **486** | InvalidS3ObjectException |  -  |
| **487** | InvalidKMSKeyException |  -  |

<a id="getDocumentTextDetection"></a>
# **getDocumentTextDetection**
> GetDocumentTextDetectionResponse getDocumentTextDetection(xAmzTarget, getDocumentTextDetectionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets the results for an Amazon Textract asynchronous operation that detects text in a document. Amazon Textract can detect lines of text and the words that make up a line of text.&lt;/p&gt; &lt;p&gt;You start asynchronous text detection by calling &lt;a&gt;StartDocumentTextDetection&lt;/a&gt;, which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). When the text detection operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that&#39;s registered in the initial call to &lt;code&gt;StartDocumentTextDetection&lt;/code&gt;. To get the results of the text-detection operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;code&gt;GetDocumentTextDetection&lt;/code&gt;, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartDocumentTextDetection&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetDocumentTextDetection&lt;/code&gt; returns an array of &lt;a&gt;Block&lt;/a&gt; objects. &lt;/p&gt; &lt;p&gt;Each document page has as an associated &lt;code&gt;Block&lt;/code&gt; of type PAGE. Each PAGE &lt;code&gt;Block&lt;/code&gt; object is the parent of LINE &lt;code&gt;Block&lt;/code&gt; objects that represent the lines of detected text on a page. A LINE &lt;code&gt;Block&lt;/code&gt; object is a parent for each word that makes up the line. Words are represented by &lt;code&gt;Block&lt;/code&gt; objects of type WORD.&lt;/p&gt; &lt;p&gt;Use the MaxResults parameter to limit the number of blocks that are returned. If there are more results than specified in &lt;code&gt;MaxResults&lt;/code&gt;, the value of &lt;code&gt;NextToken&lt;/code&gt; in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call &lt;code&gt;GetDocumentTextDetection&lt;/code&gt;, and populate the &lt;code&gt;NextToken&lt;/code&gt; request parameter with the token value that&#39;s returned from the previous call to &lt;code&gt;GetDocumentTextDetection&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html\&quot;&gt;Document Text Detection&lt;/a&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://textract.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "Textract.GetDocumentTextDetection"; // String | 
    GetDocumentTextDetectionRequest getDocumentTextDetectionRequest = new GetDocumentTextDetectionRequest(); // GetDocumentTextDetectionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetDocumentTextDetectionResponse result = apiInstance.getDocumentTextDetection(xAmzTarget, getDocumentTextDetectionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDocumentTextDetection");
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
| **xAmzTarget** | **String**|  | [enum: Textract.GetDocumentTextDetection] |
| **getDocumentTextDetectionRequest** | [**GetDocumentTextDetectionRequest**](GetDocumentTextDetectionRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetDocumentTextDetectionResponse**](GetDocumentTextDetectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | AccessDeniedException |  -  |
| **482** | ProvisionedThroughputExceededException |  -  |
| **483** | InvalidJobIdException |  -  |
| **484** | InternalServerError |  -  |
| **485** | ThrottlingException |  -  |
| **486** | InvalidS3ObjectException |  -  |
| **487** | InvalidKMSKeyException |  -  |

<a id="getExpenseAnalysis"></a>
# **getExpenseAnalysis**
> GetExpenseAnalysisResponse getExpenseAnalysis(xAmzTarget, getExpenseAnalysisRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets the results for an Amazon Textract asynchronous operation that analyzes invoices and receipts. Amazon Textract finds contact information, items purchased, and vendor name, from input invoices and receipts.&lt;/p&gt; &lt;p&gt;You start asynchronous invoice/receipt analysis by calling &lt;a&gt;StartExpenseAnalysis&lt;/a&gt;, which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). Upon completion of the invoice/receipt analysis, Amazon Textract publishes the completion status to the Amazon Simple Notification Service (Amazon SNS) topic. This topic must be registered in the initial call to &lt;code&gt;StartExpenseAnalysis&lt;/code&gt;. To get the results of the invoice/receipt analysis operation, first ensure that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;code&gt;GetExpenseAnalysis&lt;/code&gt;, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartExpenseAnalysis&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Use the MaxResults parameter to limit the number of blocks that are returned. If there are more results than specified in &lt;code&gt;MaxResults&lt;/code&gt;, the value of &lt;code&gt;NextToken&lt;/code&gt; in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call &lt;code&gt;GetExpenseAnalysis&lt;/code&gt;, and populate the &lt;code&gt;NextToken&lt;/code&gt; request parameter with the token value that&#39;s returned from the previous call to &lt;code&gt;GetExpenseAnalysis&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/invoices-receipts.html\&quot;&gt;Analyzing Invoices and Receipts&lt;/a&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://textract.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "Textract.GetExpenseAnalysis"; // String | 
    GetExpenseAnalysisRequest getExpenseAnalysisRequest = new GetExpenseAnalysisRequest(); // GetExpenseAnalysisRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetExpenseAnalysisResponse result = apiInstance.getExpenseAnalysis(xAmzTarget, getExpenseAnalysisRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getExpenseAnalysis");
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
| **xAmzTarget** | **String**|  | [enum: Textract.GetExpenseAnalysis] |
| **getExpenseAnalysisRequest** | [**GetExpenseAnalysisRequest**](GetExpenseAnalysisRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetExpenseAnalysisResponse**](GetExpenseAnalysisResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | AccessDeniedException |  -  |
| **482** | ProvisionedThroughputExceededException |  -  |
| **483** | InvalidJobIdException |  -  |
| **484** | InternalServerError |  -  |
| **485** | ThrottlingException |  -  |
| **486** | InvalidS3ObjectException |  -  |
| **487** | InvalidKMSKeyException |  -  |

<a id="getLendingAnalysis"></a>
# **getLendingAnalysis**
> GetLendingAnalysisResponse getLendingAnalysis(xAmzTarget, getLendingAnalysisRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets the results for an Amazon Textract asynchronous operation that analyzes text in a lending document. &lt;/p&gt; &lt;p&gt;You start asynchronous text analysis by calling &lt;code&gt;StartLendingAnalysis&lt;/code&gt;, which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). When the text analysis operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that&#39;s registered in the initial call to &lt;code&gt;StartLendingAnalysis&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED. If so, call GetLendingAnalysis, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartLendingAnalysis&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://textract.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "Textract.GetLendingAnalysis"; // String | 
    GetLendingAnalysisRequest getLendingAnalysisRequest = new GetLendingAnalysisRequest(); // GetLendingAnalysisRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetLendingAnalysisResponse result = apiInstance.getLendingAnalysis(xAmzTarget, getLendingAnalysisRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getLendingAnalysis");
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
| **xAmzTarget** | **String**|  | [enum: Textract.GetLendingAnalysis] |
| **getLendingAnalysisRequest** | [**GetLendingAnalysisRequest**](GetLendingAnalysisRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetLendingAnalysisResponse**](GetLendingAnalysisResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | AccessDeniedException |  -  |
| **482** | ProvisionedThroughputExceededException |  -  |
| **483** | InvalidJobIdException |  -  |
| **484** | InternalServerError |  -  |
| **485** | ThrottlingException |  -  |
| **486** | InvalidS3ObjectException |  -  |
| **487** | InvalidKMSKeyException |  -  |

<a id="getLendingAnalysisSummary"></a>
# **getLendingAnalysisSummary**
> GetLendingAnalysisSummaryResponse getLendingAnalysisSummary(xAmzTarget, getLendingAnalysisSummaryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets summarized results for the &lt;code&gt;StartLendingAnalysis&lt;/code&gt; operation, which analyzes text in a lending document. The returned summary consists of information about documents grouped together by a common document type. Information like detected signatures, page numbers, and split documents is returned with respect to the type of grouped document. &lt;/p&gt; &lt;p&gt;You start asynchronous text analysis by calling &lt;code&gt;StartLendingAnalysis&lt;/code&gt;, which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). When the text analysis operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that&#39;s registered in the initial call to &lt;code&gt;StartLendingAnalysis&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED. If so, call &lt;code&gt;GetLendingAnalysisSummary&lt;/code&gt;, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartLendingAnalysis&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://textract.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "Textract.GetLendingAnalysisSummary"; // String | 
    GetLendingAnalysisSummaryRequest getLendingAnalysisSummaryRequest = new GetLendingAnalysisSummaryRequest(); // GetLendingAnalysisSummaryRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetLendingAnalysisSummaryResponse result = apiInstance.getLendingAnalysisSummary(xAmzTarget, getLendingAnalysisSummaryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getLendingAnalysisSummary");
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
| **xAmzTarget** | **String**|  | [enum: Textract.GetLendingAnalysisSummary] |
| **getLendingAnalysisSummaryRequest** | [**GetLendingAnalysisSummaryRequest**](GetLendingAnalysisSummaryRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetLendingAnalysisSummaryResponse**](GetLendingAnalysisSummaryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | AccessDeniedException |  -  |
| **482** | ProvisionedThroughputExceededException |  -  |
| **483** | InvalidJobIdException |  -  |
| **484** | InternalServerError |  -  |
| **485** | ThrottlingException |  -  |
| **486** | InvalidS3ObjectException |  -  |
| **487** | InvalidKMSKeyException |  -  |

<a id="startDocumentAnalysis"></a>
# **startDocumentAnalysis**
> StartDocumentAnalysisResponse startDocumentAnalysis(xAmzTarget, startDocumentAnalysisRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Starts the asynchronous analysis of an input document for relationships between detected items such as key-value pairs, tables, and selection elements.&lt;/p&gt; &lt;p&gt; &lt;code&gt;StartDocumentAnalysis&lt;/code&gt; can analyze text in documents that are in JPEG, PNG, TIFF, and PDF format. The documents are stored in an Amazon S3 bucket. Use &lt;a&gt;DocumentLocation&lt;/a&gt; to specify the bucket name and file name of the document. &lt;/p&gt; &lt;p&gt; &lt;code&gt;StartDocumentAnalysis&lt;/code&gt; returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;) that you use to get the results of the operation. When text analysis is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you specify in &lt;code&gt;NotificationChannel&lt;/code&gt;. To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;a&gt;GetDocumentAnalysis&lt;/a&gt;, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartDocumentAnalysis&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html\&quot;&gt;Document Text Analysis&lt;/a&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://textract.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "Textract.StartDocumentAnalysis"; // String | 
    StartDocumentAnalysisRequest startDocumentAnalysisRequest = new StartDocumentAnalysisRequest(); // StartDocumentAnalysisRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartDocumentAnalysisResponse result = apiInstance.startDocumentAnalysis(xAmzTarget, startDocumentAnalysisRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startDocumentAnalysis");
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
| **xAmzTarget** | **String**|  | [enum: Textract.StartDocumentAnalysis] |
| **startDocumentAnalysisRequest** | [**StartDocumentAnalysisRequest**](StartDocumentAnalysisRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartDocumentAnalysisResponse**](StartDocumentAnalysisResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | InvalidS3ObjectException |  -  |
| **482** | InvalidKMSKeyException |  -  |
| **483** | UnsupportedDocumentException |  -  |
| **484** | DocumentTooLargeException |  -  |
| **485** | BadDocumentException |  -  |
| **486** | AccessDeniedException |  -  |
| **487** | ProvisionedThroughputExceededException |  -  |
| **488** | InternalServerError |  -  |
| **489** | IdempotentParameterMismatchException |  -  |
| **490** | ThrottlingException |  -  |
| **491** | LimitExceededException |  -  |

<a id="startDocumentTextDetection"></a>
# **startDocumentTextDetection**
> StartDocumentTextDetectionResponse startDocumentTextDetection(xAmzTarget, startDocumentTextDetectionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Starts the asynchronous detection of text in a document. Amazon Textract can detect lines of text and the words that make up a line of text.&lt;/p&gt; &lt;p&gt; &lt;code&gt;StartDocumentTextDetection&lt;/code&gt; can analyze text in documents that are in JPEG, PNG, TIFF, and PDF format. The documents are stored in an Amazon S3 bucket. Use &lt;a&gt;DocumentLocation&lt;/a&gt; to specify the bucket name and file name of the document. &lt;/p&gt; &lt;p&gt; &lt;code&gt;StartTextDetection&lt;/code&gt; returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;) that you use to get the results of the operation. When text detection is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you specify in &lt;code&gt;NotificationChannel&lt;/code&gt;. To get the results of the text detection operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;a&gt;GetDocumentTextDetection&lt;/a&gt;, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartDocumentTextDetection&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html\&quot;&gt;Document Text Detection&lt;/a&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://textract.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "Textract.StartDocumentTextDetection"; // String | 
    StartDocumentTextDetectionRequest startDocumentTextDetectionRequest = new StartDocumentTextDetectionRequest(); // StartDocumentTextDetectionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartDocumentTextDetectionResponse result = apiInstance.startDocumentTextDetection(xAmzTarget, startDocumentTextDetectionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startDocumentTextDetection");
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
| **xAmzTarget** | **String**|  | [enum: Textract.StartDocumentTextDetection] |
| **startDocumentTextDetectionRequest** | [**StartDocumentTextDetectionRequest**](StartDocumentTextDetectionRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartDocumentTextDetectionResponse**](StartDocumentTextDetectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | InvalidS3ObjectException |  -  |
| **482** | InvalidKMSKeyException |  -  |
| **483** | UnsupportedDocumentException |  -  |
| **484** | DocumentTooLargeException |  -  |
| **485** | BadDocumentException |  -  |
| **486** | AccessDeniedException |  -  |
| **487** | ProvisionedThroughputExceededException |  -  |
| **488** | InternalServerError |  -  |
| **489** | IdempotentParameterMismatchException |  -  |
| **490** | ThrottlingException |  -  |
| **491** | LimitExceededException |  -  |

<a id="startExpenseAnalysis"></a>
# **startExpenseAnalysis**
> StartExpenseAnalysisResponse startExpenseAnalysis(xAmzTarget, startExpenseAnalysisRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Starts the asynchronous analysis of invoices or receipts for data like contact information, items purchased, and vendor names.&lt;/p&gt; &lt;p&gt; &lt;code&gt;StartExpenseAnalysis&lt;/code&gt; can analyze text in documents that are in JPEG, PNG, and PDF format. The documents must be stored in an Amazon S3 bucket. Use the &lt;a&gt;DocumentLocation&lt;/a&gt; parameter to specify the name of your S3 bucket and the name of the document in that bucket. &lt;/p&gt; &lt;p&gt; &lt;code&gt;StartExpenseAnalysis&lt;/code&gt; returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;) that you will provide to &lt;code&gt;GetExpenseAnalysis&lt;/code&gt; to retrieve the results of the operation. When the analysis of the input invoices/receipts is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you provide to the &lt;code&gt;NotificationChannel&lt;/code&gt;. To obtain the results of the invoice and receipt analysis operation, ensure that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;a&gt;GetExpenseAnalysis&lt;/a&gt;, and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) that was returned by your call to &lt;code&gt;StartExpenseAnalysis&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/textract/latest/dg/invoice-receipts.html\&quot;&gt;Analyzing Invoices and Receipts&lt;/a&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://textract.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "Textract.StartExpenseAnalysis"; // String | 
    StartExpenseAnalysisRequest startExpenseAnalysisRequest = new StartExpenseAnalysisRequest(); // StartExpenseAnalysisRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartExpenseAnalysisResponse result = apiInstance.startExpenseAnalysis(xAmzTarget, startExpenseAnalysisRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startExpenseAnalysis");
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
| **xAmzTarget** | **String**|  | [enum: Textract.StartExpenseAnalysis] |
| **startExpenseAnalysisRequest** | [**StartExpenseAnalysisRequest**](StartExpenseAnalysisRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartExpenseAnalysisResponse**](StartExpenseAnalysisResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | InvalidS3ObjectException |  -  |
| **482** | InvalidKMSKeyException |  -  |
| **483** | UnsupportedDocumentException |  -  |
| **484** | DocumentTooLargeException |  -  |
| **485** | BadDocumentException |  -  |
| **486** | AccessDeniedException |  -  |
| **487** | ProvisionedThroughputExceededException |  -  |
| **488** | InternalServerError |  -  |
| **489** | IdempotentParameterMismatchException |  -  |
| **490** | ThrottlingException |  -  |
| **491** | LimitExceededException |  -  |

<a id="startLendingAnalysis"></a>
# **startLendingAnalysis**
> StartLendingAnalysisResponse startLendingAnalysis(xAmzTarget, startLendingAnalysisRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Starts the classification and analysis of an input document. &lt;code&gt;StartLendingAnalysis&lt;/code&gt; initiates the classification and analysis of a packet of lending documents. &lt;code&gt;StartLendingAnalysis&lt;/code&gt; operates on a document file located in an Amazon S3 bucket.&lt;/p&gt; &lt;p&gt; &lt;code&gt;StartLendingAnalysis&lt;/code&gt; can analyze text in documents that are in one of the following formats: JPEG, PNG, TIFF, PDF. Use &lt;code&gt;DocumentLocation&lt;/code&gt; to specify the bucket name and the file name of the document. &lt;/p&gt; &lt;p&gt; &lt;code&gt;StartLendingAnalysis&lt;/code&gt; returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;) that you use to get the results of the operation. When the text analysis is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you specify in &lt;code&gt;NotificationChannel&lt;/code&gt;. To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED. If the status is SUCCEEDED you can call either &lt;code&gt;GetLendingAnalysis&lt;/code&gt; or &lt;code&gt;GetLendingAnalysisSummary&lt;/code&gt; and provide the &lt;code&gt;JobId&lt;/code&gt; to obtain the results of the analysis.&lt;/p&gt; &lt;p&gt;If using &lt;code&gt;OutputConfig&lt;/code&gt; to specify an Amazon S3 bucket, the output will be contained within the specified prefix in a directory labeled with the job-id. In the directory there are 3 sub-directories: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;detailedResponse (contains the GetLendingAnalysis response)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;summaryResponse (for the GetLendingAnalysisSummary response)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;splitDocuments (documents split across logical boundaries)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://textract.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "Textract.StartLendingAnalysis"; // String | 
    StartLendingAnalysisRequest startLendingAnalysisRequest = new StartLendingAnalysisRequest(); // StartLendingAnalysisRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartLendingAnalysisResponse result = apiInstance.startLendingAnalysis(xAmzTarget, startLendingAnalysisRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startLendingAnalysis");
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
| **xAmzTarget** | **String**|  | [enum: Textract.StartLendingAnalysis] |
| **startLendingAnalysisRequest** | [**StartLendingAnalysisRequest**](StartLendingAnalysisRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartLendingAnalysisResponse**](StartLendingAnalysisResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidParameterException |  -  |
| **481** | InvalidS3ObjectException |  -  |
| **482** | InvalidKMSKeyException |  -  |
| **483** | UnsupportedDocumentException |  -  |
| **484** | DocumentTooLargeException |  -  |
| **485** | BadDocumentException |  -  |
| **486** | AccessDeniedException |  -  |
| **487** | ProvisionedThroughputExceededException |  -  |
| **488** | InternalServerError |  -  |
| **489** | IdempotentParameterMismatchException |  -  |
| **490** | ThrottlingException |  -  |
| **491** | LimitExceededException |  -  |

