# DefaultApi

All URIs are relative to *https://support.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addAttachmentsToSet**](DefaultApi.md#addAttachmentsToSet) | **POST** /#X-Amz-Target&#x3D;AWSSupport_20130415.AddAttachmentsToSet |  |
| [**addCommunicationToCase**](DefaultApi.md#addCommunicationToCase) | **POST** /#X-Amz-Target&#x3D;AWSSupport_20130415.AddCommunicationToCase |  |
| [**createCase**](DefaultApi.md#createCase) | **POST** /#X-Amz-Target&#x3D;AWSSupport_20130415.CreateCase |  |
| [**describeAttachment**](DefaultApi.md#describeAttachment) | **POST** /#X-Amz-Target&#x3D;AWSSupport_20130415.DescribeAttachment |  |
| [**describeCases**](DefaultApi.md#describeCases) | **POST** /#X-Amz-Target&#x3D;AWSSupport_20130415.DescribeCases |  |
| [**describeCommunications**](DefaultApi.md#describeCommunications) | **POST** /#X-Amz-Target&#x3D;AWSSupport_20130415.DescribeCommunications |  |
| [**describeCreateCaseOptions**](DefaultApi.md#describeCreateCaseOptions) | **POST** /#X-Amz-Target&#x3D;AWSSupport_20130415.DescribeCreateCaseOptions |  |
| [**describeServices**](DefaultApi.md#describeServices) | **POST** /#X-Amz-Target&#x3D;AWSSupport_20130415.DescribeServices |  |
| [**describeSeverityLevels**](DefaultApi.md#describeSeverityLevels) | **POST** /#X-Amz-Target&#x3D;AWSSupport_20130415.DescribeSeverityLevels |  |
| [**describeSupportedLanguages**](DefaultApi.md#describeSupportedLanguages) | **POST** /#X-Amz-Target&#x3D;AWSSupport_20130415.DescribeSupportedLanguages |  |
| [**describeTrustedAdvisorCheckRefreshStatuses**](DefaultApi.md#describeTrustedAdvisorCheckRefreshStatuses) | **POST** /#X-Amz-Target&#x3D;AWSSupport_20130415.DescribeTrustedAdvisorCheckRefreshStatuses |  |
| [**describeTrustedAdvisorCheckResult**](DefaultApi.md#describeTrustedAdvisorCheckResult) | **POST** /#X-Amz-Target&#x3D;AWSSupport_20130415.DescribeTrustedAdvisorCheckResult |  |
| [**describeTrustedAdvisorCheckSummaries**](DefaultApi.md#describeTrustedAdvisorCheckSummaries) | **POST** /#X-Amz-Target&#x3D;AWSSupport_20130415.DescribeTrustedAdvisorCheckSummaries |  |
| [**describeTrustedAdvisorChecks**](DefaultApi.md#describeTrustedAdvisorChecks) | **POST** /#X-Amz-Target&#x3D;AWSSupport_20130415.DescribeTrustedAdvisorChecks |  |
| [**refreshTrustedAdvisorCheck**](DefaultApi.md#refreshTrustedAdvisorCheck) | **POST** /#X-Amz-Target&#x3D;AWSSupport_20130415.RefreshTrustedAdvisorCheck |  |
| [**resolveCase**](DefaultApi.md#resolveCase) | **POST** /#X-Amz-Target&#x3D;AWSSupport_20130415.ResolveCase |  |


<a id="addAttachmentsToSet"></a>
# **addAttachmentsToSet**
> AddAttachmentsToSetResponse addAttachmentsToSet(xAmzTarget, addAttachmentsToSetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Adds one or more attachments to an attachment set. &lt;/p&gt; &lt;p&gt;An attachment set is a temporary container for attachments that you add to a case or case communication. The set is available for 1 hour after it&#39;s created. The &lt;code&gt;expiryTime&lt;/code&gt; returned in the response is when the set expires. &lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("https://support.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSSupport_20130415.AddAttachmentsToSet"; // String | 
    AddAttachmentsToSetRequest addAttachmentsToSetRequest = new AddAttachmentsToSetRequest(); // AddAttachmentsToSetRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      AddAttachmentsToSetResponse result = apiInstance.addAttachmentsToSet(xAmzTarget, addAttachmentsToSetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addAttachmentsToSet");
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
| **xAmzTarget** | **String**|  | [enum: AWSSupport_20130415.AddAttachmentsToSet] |
| **addAttachmentsToSetRequest** | [**AddAttachmentsToSetRequest**](AddAttachmentsToSetRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**AddAttachmentsToSetResponse**](AddAttachmentsToSetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerError |  -  |
| **481** | AttachmentSetIdNotFound |  -  |
| **482** | AttachmentSetExpired |  -  |
| **483** | AttachmentSetSizeLimitExceeded |  -  |
| **484** | AttachmentLimitExceeded |  -  |

<a id="addCommunicationToCase"></a>
# **addCommunicationToCase**
> AddCommunicationToCaseResponse addCommunicationToCase(xAmzTarget, addCommunicationToCaseRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Adds additional customer communication to an Amazon Web Services Support case. Use the &lt;code&gt;caseId&lt;/code&gt; parameter to identify the case to which to add communication. You can list a set of email addresses to copy on the communication by using the &lt;code&gt;ccEmailAddresses&lt;/code&gt; parameter. The &lt;code&gt;communicationBody&lt;/code&gt; value contains the text of the communication.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("https://support.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSSupport_20130415.AddCommunicationToCase"; // String | 
    AddCommunicationToCaseRequest addCommunicationToCaseRequest = new AddCommunicationToCaseRequest(); // AddCommunicationToCaseRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      AddCommunicationToCaseResponse result = apiInstance.addCommunicationToCase(xAmzTarget, addCommunicationToCaseRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addCommunicationToCase");
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
| **xAmzTarget** | **String**|  | [enum: AWSSupport_20130415.AddCommunicationToCase] |
| **addCommunicationToCaseRequest** | [**AddCommunicationToCaseRequest**](AddCommunicationToCaseRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**AddCommunicationToCaseResponse**](AddCommunicationToCaseResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerError |  -  |
| **481** | CaseIdNotFound |  -  |
| **482** | AttachmentSetIdNotFound |  -  |
| **483** | AttachmentSetExpired |  -  |

<a id="createCase"></a>
# **createCase**
> CreateCaseResponse createCase(xAmzTarget, createCaseRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a case in the Amazon Web Services Support Center. This operation is similar to how you create a case in the Amazon Web Services Support Center &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home#/case/create\&quot;&gt;Create Case&lt;/a&gt; page.&lt;/p&gt; &lt;p&gt;The Amazon Web Services Support API doesn&#39;t support requesting service limit increases. You can submit a service limit increase in the following ways: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Submit a request from the Amazon Web Services Support Center &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home#/case/create\&quot;&gt;Create Case&lt;/a&gt; page.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the Service Quotas &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_RequestServiceQuotaIncrease.html\&quot;&gt;RequestServiceQuotaIncrease&lt;/a&gt; operation.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;A successful &lt;code&gt;CreateCase&lt;/code&gt; request returns an Amazon Web Services Support case number. You can use the &lt;a&gt;DescribeCases&lt;/a&gt; operation and specify the case number to get existing Amazon Web Services Support cases. After you create a case, use the &lt;a&gt;AddCommunicationToCase&lt;/a&gt; operation to add additional communication or attachments to an existing case.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;caseId&lt;/code&gt; is separate from the &lt;code&gt;displayId&lt;/code&gt; that appears in the &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support\&quot;&gt;Amazon Web Services Support Center&lt;/a&gt;. Use the &lt;a&gt;DescribeCases&lt;/a&gt; operation to get the &lt;code&gt;displayId&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("https://support.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSSupport_20130415.CreateCase"; // String | 
    CreateCaseRequest createCaseRequest = new CreateCaseRequest(); // CreateCaseRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateCaseResponse result = apiInstance.createCase(xAmzTarget, createCaseRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createCase");
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
| **xAmzTarget** | **String**|  | [enum: AWSSupport_20130415.CreateCase] |
| **createCaseRequest** | [**CreateCaseRequest**](CreateCaseRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateCaseResponse**](CreateCaseResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerError |  -  |
| **481** | CaseCreationLimitExceeded |  -  |
| **482** | AttachmentSetIdNotFound |  -  |
| **483** | AttachmentSetExpired |  -  |

<a id="describeAttachment"></a>
# **describeAttachment**
> DescribeAttachmentResponse describeAttachment(xAmzTarget, describeAttachmentRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns the attachment that has the specified ID. Attachments can include screenshots, error logs, or other files that describe your issue. Attachment IDs are generated by the case management system when you add an attachment to a case or case communication. Attachment IDs are returned in the &lt;a&gt;AttachmentDetails&lt;/a&gt; objects that are returned by the &lt;a&gt;DescribeCommunications&lt;/a&gt; operation.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("https://support.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSSupport_20130415.DescribeAttachment"; // String | 
    DescribeAttachmentRequest describeAttachmentRequest = new DescribeAttachmentRequest(); // DescribeAttachmentRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeAttachmentResponse result = apiInstance.describeAttachment(xAmzTarget, describeAttachmentRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeAttachment");
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
| **xAmzTarget** | **String**|  | [enum: AWSSupport_20130415.DescribeAttachment] |
| **describeAttachmentRequest** | [**DescribeAttachmentRequest**](DescribeAttachmentRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeAttachmentResponse**](DescribeAttachmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerError |  -  |
| **481** | DescribeAttachmentLimitExceeded |  -  |
| **482** | AttachmentIdNotFound |  -  |

<a id="describeCases"></a>
# **describeCases**
> DescribeCasesResponse describeCases(xAmzTarget, describeCasesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



&lt;p&gt;Returns a list of cases that you specify by passing one or more case IDs. You can use the &lt;code&gt;afterTime&lt;/code&gt; and &lt;code&gt;beforeTime&lt;/code&gt; parameters to filter the cases by date. You can set values for the &lt;code&gt;includeResolvedCases&lt;/code&gt; and &lt;code&gt;includeCommunications&lt;/code&gt; parameters to specify how much information to return.&lt;/p&gt; &lt;p&gt;The response returns the following in JSON format:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;One or more &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/APIReference/API_CaseDetails.html\&quot;&gt;CaseDetails&lt;/a&gt; data types.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;One or more &lt;code&gt;nextToken&lt;/code&gt; values, which specify where to paginate the returned records represented by the &lt;code&gt;CaseDetails&lt;/code&gt; objects.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Case data is available for 12 months after creation. If a case was created more than 12 months ago, a request might return an error.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("https://support.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSSupport_20130415.DescribeCases"; // String | 
    DescribeCasesRequest describeCasesRequest = new DescribeCasesRequest(); // DescribeCasesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      DescribeCasesResponse result = apiInstance.describeCases(xAmzTarget, describeCasesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeCases");
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
| **xAmzTarget** | **String**|  | [enum: AWSSupport_20130415.DescribeCases] |
| **describeCasesRequest** | [**DescribeCasesRequest**](DescribeCasesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**DescribeCasesResponse**](DescribeCasesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerError |  -  |
| **481** | CaseIdNotFound |  -  |

<a id="describeCommunications"></a>
# **describeCommunications**
> DescribeCommunicationsResponse describeCommunications(xAmzTarget, describeCommunicationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



&lt;p&gt;Returns communications and attachments for one or more support cases. Use the &lt;code&gt;afterTime&lt;/code&gt; and &lt;code&gt;beforeTime&lt;/code&gt; parameters to filter by date. You can use the &lt;code&gt;caseId&lt;/code&gt; parameter to restrict the results to a specific case.&lt;/p&gt; &lt;p&gt;Case data is available for 12 months after creation. If a case was created more than 12 months ago, a request for data might cause an error.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;maxResults&lt;/code&gt; and &lt;code&gt;nextToken&lt;/code&gt; parameters to control the pagination of the results. Set &lt;code&gt;maxResults&lt;/code&gt; to the number of cases that you want to display on each page, and use &lt;code&gt;nextToken&lt;/code&gt; to specify the resumption of pagination.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("https://support.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSSupport_20130415.DescribeCommunications"; // String | 
    DescribeCommunicationsRequest describeCommunicationsRequest = new DescribeCommunicationsRequest(); // DescribeCommunicationsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      DescribeCommunicationsResponse result = apiInstance.describeCommunications(xAmzTarget, describeCommunicationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeCommunications");
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
| **xAmzTarget** | **String**|  | [enum: AWSSupport_20130415.DescribeCommunications] |
| **describeCommunicationsRequest** | [**DescribeCommunicationsRequest**](DescribeCommunicationsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**DescribeCommunicationsResponse**](DescribeCommunicationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerError |  -  |
| **481** | CaseIdNotFound |  -  |

<a id="describeCreateCaseOptions"></a>
# **describeCreateCaseOptions**
> DescribeCreateCaseOptionsResponse describeCreateCaseOptions(xAmzTarget, describeCreateCaseOptionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns a list of CreateCaseOption types along with the corresponding supported hours and language availability. You can specify the &lt;code&gt;language&lt;/code&gt; &lt;code&gt;categoryCode&lt;/code&gt;, &lt;code&gt;issueType&lt;/code&gt; and &lt;code&gt;serviceCode&lt;/code&gt; used to retrieve the CreateCaseOptions.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("https://support.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSSupport_20130415.DescribeCreateCaseOptions"; // String | 
    DescribeCreateCaseOptionsRequest describeCreateCaseOptionsRequest = new DescribeCreateCaseOptionsRequest(); // DescribeCreateCaseOptionsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeCreateCaseOptionsResponse result = apiInstance.describeCreateCaseOptions(xAmzTarget, describeCreateCaseOptionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeCreateCaseOptions");
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
| **xAmzTarget** | **String**|  | [enum: AWSSupport_20130415.DescribeCreateCaseOptions] |
| **describeCreateCaseOptionsRequest** | [**DescribeCreateCaseOptionsRequest**](DescribeCreateCaseOptionsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeCreateCaseOptionsResponse**](DescribeCreateCaseOptionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerError |  -  |
| **481** | ThrottlingException |  -  |

<a id="describeServices"></a>
# **describeServices**
> DescribeServicesResponse describeServices(xAmzTarget, describeServicesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns the current list of Amazon Web Services services and a list of service categories for each service. You then use service names and categories in your &lt;a&gt;CreateCase&lt;/a&gt; requests. Each Amazon Web Services service has its own set of categories.&lt;/p&gt; &lt;p&gt;The service codes and category codes correspond to the values that appear in the &lt;b&gt;Service&lt;/b&gt; and &lt;b&gt;Category&lt;/b&gt; lists on the Amazon Web Services Support Center &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home#/case/create\&quot;&gt;Create Case&lt;/a&gt; page. The values in those fields don&#39;t necessarily match the service codes and categories returned by the &lt;code&gt;DescribeServices&lt;/code&gt; operation. Always use the service codes and categories that the &lt;code&gt;DescribeServices&lt;/code&gt; operation returns, so that you have the most recent set of service and category codes.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("https://support.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSSupport_20130415.DescribeServices"; // String | 
    DescribeServicesRequest describeServicesRequest = new DescribeServicesRequest(); // DescribeServicesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeServicesResponse result = apiInstance.describeServices(xAmzTarget, describeServicesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeServices");
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
| **xAmzTarget** | **String**|  | [enum: AWSSupport_20130415.DescribeServices] |
| **describeServicesRequest** | [**DescribeServicesRequest**](DescribeServicesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeServicesResponse**](DescribeServicesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerError |  -  |

<a id="describeSeverityLevels"></a>
# **describeSeverityLevels**
> DescribeSeverityLevelsResponse describeSeverityLevels(xAmzTarget, describeSeverityLevelsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns the list of severity levels that you can assign to a support case. The severity level for a case is also a field in the &lt;a&gt;CaseDetails&lt;/a&gt; data type that you include for a &lt;a&gt;CreateCase&lt;/a&gt; request.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("https://support.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSSupport_20130415.DescribeSeverityLevels"; // String | 
    DescribeSeverityLevelsRequest describeSeverityLevelsRequest = new DescribeSeverityLevelsRequest(); // DescribeSeverityLevelsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeSeverityLevelsResponse result = apiInstance.describeSeverityLevels(xAmzTarget, describeSeverityLevelsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeSeverityLevels");
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
| **xAmzTarget** | **String**|  | [enum: AWSSupport_20130415.DescribeSeverityLevels] |
| **describeSeverityLevelsRequest** | [**DescribeSeverityLevelsRequest**](DescribeSeverityLevelsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeSeverityLevelsResponse**](DescribeSeverityLevelsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerError |  -  |

<a id="describeSupportedLanguages"></a>
# **describeSupportedLanguages**
> DescribeSupportedLanguagesResponse describeSupportedLanguages(xAmzTarget, describeSupportedLanguagesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns a list of supported languages for a specified &lt;code&gt;categoryCode&lt;/code&gt;, &lt;code&gt;issueType&lt;/code&gt; and &lt;code&gt;serviceCode&lt;/code&gt;. The returned supported languages will include a ISO 639-1 code for the &lt;code&gt;language&lt;/code&gt;, and the language display name.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("https://support.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSSupport_20130415.DescribeSupportedLanguages"; // String | 
    DescribeSupportedLanguagesRequest describeSupportedLanguagesRequest = new DescribeSupportedLanguagesRequest(); // DescribeSupportedLanguagesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeSupportedLanguagesResponse result = apiInstance.describeSupportedLanguages(xAmzTarget, describeSupportedLanguagesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeSupportedLanguages");
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
| **xAmzTarget** | **String**|  | [enum: AWSSupport_20130415.DescribeSupportedLanguages] |
| **describeSupportedLanguagesRequest** | [**DescribeSupportedLanguagesRequest**](DescribeSupportedLanguagesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeSupportedLanguagesResponse**](DescribeSupportedLanguagesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerError |  -  |
| **481** | ThrottlingException |  -  |

<a id="describeTrustedAdvisorCheckRefreshStatuses"></a>
# **describeTrustedAdvisorCheckRefreshStatuses**
> DescribeTrustedAdvisorCheckRefreshStatusesResponse describeTrustedAdvisorCheckRefreshStatuses(xAmzTarget, describeTrustedAdvisorCheckRefreshStatusesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns the refresh status of the Trusted Advisor checks that have the specified check IDs. You can get the check IDs by calling the &lt;a&gt;DescribeTrustedAdvisorChecks&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;Some checks are refreshed automatically, and you can&#39;t return their refresh statuses by using the &lt;code&gt;DescribeTrustedAdvisorCheckRefreshStatuses&lt;/code&gt; operation. If you call this operation for these checks, you might see an &lt;code&gt;InvalidParameterValue&lt;/code&gt; error.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; &lt;p&gt;To call the Trusted Advisor operations in the Amazon Web Services Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don&#39;t support the Trusted Advisor operations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint\&quot;&gt;About the Amazon Web Services Support API&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Support User Guide&lt;/i&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("https://support.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSSupport_20130415.DescribeTrustedAdvisorCheckRefreshStatuses"; // String | 
    DescribeTrustedAdvisorCheckRefreshStatusesRequest describeTrustedAdvisorCheckRefreshStatusesRequest = new DescribeTrustedAdvisorCheckRefreshStatusesRequest(); // DescribeTrustedAdvisorCheckRefreshStatusesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeTrustedAdvisorCheckRefreshStatusesResponse result = apiInstance.describeTrustedAdvisorCheckRefreshStatuses(xAmzTarget, describeTrustedAdvisorCheckRefreshStatusesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeTrustedAdvisorCheckRefreshStatuses");
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
| **xAmzTarget** | **String**|  | [enum: AWSSupport_20130415.DescribeTrustedAdvisorCheckRefreshStatuses] |
| **describeTrustedAdvisorCheckRefreshStatusesRequest** | [**DescribeTrustedAdvisorCheckRefreshStatusesRequest**](DescribeTrustedAdvisorCheckRefreshStatusesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeTrustedAdvisorCheckRefreshStatusesResponse**](DescribeTrustedAdvisorCheckRefreshStatusesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerError |  -  |
| **481** | ThrottlingException |  -  |

<a id="describeTrustedAdvisorCheckResult"></a>
# **describeTrustedAdvisorCheckResult**
> DescribeTrustedAdvisorCheckResultResponse describeTrustedAdvisorCheckResult(xAmzTarget, describeTrustedAdvisorCheckResultRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns the results of the Trusted Advisor check that has the specified check ID. You can get the check IDs by calling the &lt;a&gt;DescribeTrustedAdvisorChecks&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;The response contains a &lt;a&gt;TrustedAdvisorCheckResult&lt;/a&gt; object, which contains these three objects:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;TrustedAdvisorCategorySpecificSummary&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;TrustedAdvisorResourceDetail&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;TrustedAdvisorResourcesSummary&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;In addition, the response contains these fields:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;status&lt;/b&gt; - The alert status of the check can be &lt;code&gt;ok&lt;/code&gt; (green), &lt;code&gt;warning&lt;/code&gt; (yellow), &lt;code&gt;error&lt;/code&gt; (red), or &lt;code&gt;not_available&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;timestamp&lt;/b&gt; - The time of the last refresh of the check.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;checkId&lt;/b&gt; - The unique identifier for the check.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; &lt;p&gt;To call the Trusted Advisor operations in the Amazon Web Services Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don&#39;t support the Trusted Advisor operations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint\&quot;&gt;About the Amazon Web Services Support API&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Support User Guide&lt;/i&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("https://support.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSSupport_20130415.DescribeTrustedAdvisorCheckResult"; // String | 
    DescribeTrustedAdvisorCheckResultRequest describeTrustedAdvisorCheckResultRequest = new DescribeTrustedAdvisorCheckResultRequest(); // DescribeTrustedAdvisorCheckResultRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeTrustedAdvisorCheckResultResponse result = apiInstance.describeTrustedAdvisorCheckResult(xAmzTarget, describeTrustedAdvisorCheckResultRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeTrustedAdvisorCheckResult");
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
| **xAmzTarget** | **String**|  | [enum: AWSSupport_20130415.DescribeTrustedAdvisorCheckResult] |
| **describeTrustedAdvisorCheckResultRequest** | [**DescribeTrustedAdvisorCheckResultRequest**](DescribeTrustedAdvisorCheckResultRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeTrustedAdvisorCheckResultResponse**](DescribeTrustedAdvisorCheckResultResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerError |  -  |
| **481** | ThrottlingException |  -  |

<a id="describeTrustedAdvisorCheckSummaries"></a>
# **describeTrustedAdvisorCheckSummaries**
> DescribeTrustedAdvisorCheckSummariesResponse describeTrustedAdvisorCheckSummaries(xAmzTarget, describeTrustedAdvisorCheckSummariesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns the results for the Trusted Advisor check summaries for the check IDs that you specified. You can get the check IDs by calling the &lt;a&gt;DescribeTrustedAdvisorChecks&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;The response contains an array of &lt;a&gt;TrustedAdvisorCheckSummary&lt;/a&gt; objects.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; &lt;p&gt;To call the Trusted Advisor operations in the Amazon Web Services Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don&#39;t support the Trusted Advisor operations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint\&quot;&gt;About the Amazon Web Services Support API&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Support User Guide&lt;/i&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("https://support.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSSupport_20130415.DescribeTrustedAdvisorCheckSummaries"; // String | 
    DescribeTrustedAdvisorCheckSummariesRequest describeTrustedAdvisorCheckSummariesRequest = new DescribeTrustedAdvisorCheckSummariesRequest(); // DescribeTrustedAdvisorCheckSummariesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeTrustedAdvisorCheckSummariesResponse result = apiInstance.describeTrustedAdvisorCheckSummaries(xAmzTarget, describeTrustedAdvisorCheckSummariesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeTrustedAdvisorCheckSummaries");
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
| **xAmzTarget** | **String**|  | [enum: AWSSupport_20130415.DescribeTrustedAdvisorCheckSummaries] |
| **describeTrustedAdvisorCheckSummariesRequest** | [**DescribeTrustedAdvisorCheckSummariesRequest**](DescribeTrustedAdvisorCheckSummariesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeTrustedAdvisorCheckSummariesResponse**](DescribeTrustedAdvisorCheckSummariesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerError |  -  |
| **481** | ThrottlingException |  -  |

<a id="describeTrustedAdvisorChecks"></a>
# **describeTrustedAdvisorChecks**
> DescribeTrustedAdvisorChecksResponse describeTrustedAdvisorChecks(xAmzTarget, describeTrustedAdvisorChecksRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns information about all available Trusted Advisor checks, including the name, ID, category, description, and metadata. You must specify a language code.&lt;/p&gt; &lt;p&gt;The response contains a &lt;a&gt;TrustedAdvisorCheckDescription&lt;/a&gt; object for each check. You must set the Amazon Web Services Region to us-east-1.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The names and descriptions for Trusted Advisor checks are subject to change. We recommend that you specify the check ID in your code to uniquely identify a check.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; &lt;p&gt;To call the Trusted Advisor operations in the Amazon Web Services Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don&#39;t support the Trusted Advisor operations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint\&quot;&gt;About the Amazon Web Services Support API&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Support User Guide&lt;/i&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("https://support.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSSupport_20130415.DescribeTrustedAdvisorChecks"; // String | 
    DescribeTrustedAdvisorChecksRequest describeTrustedAdvisorChecksRequest = new DescribeTrustedAdvisorChecksRequest(); // DescribeTrustedAdvisorChecksRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeTrustedAdvisorChecksResponse result = apiInstance.describeTrustedAdvisorChecks(xAmzTarget, describeTrustedAdvisorChecksRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeTrustedAdvisorChecks");
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
| **xAmzTarget** | **String**|  | [enum: AWSSupport_20130415.DescribeTrustedAdvisorChecks] |
| **describeTrustedAdvisorChecksRequest** | [**DescribeTrustedAdvisorChecksRequest**](DescribeTrustedAdvisorChecksRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeTrustedAdvisorChecksResponse**](DescribeTrustedAdvisorChecksResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerError |  -  |
| **481** | ThrottlingException |  -  |

<a id="refreshTrustedAdvisorCheck"></a>
# **refreshTrustedAdvisorCheck**
> RefreshTrustedAdvisorCheckResponse refreshTrustedAdvisorCheck(xAmzTarget, refreshTrustedAdvisorCheckRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Refreshes the Trusted Advisor check that you specify using the check ID. You can get the check IDs by calling the &lt;a&gt;DescribeTrustedAdvisorChecks&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;Some checks are refreshed automatically. If you call the &lt;code&gt;RefreshTrustedAdvisorCheck&lt;/code&gt; operation to refresh them, you might see the &lt;code&gt;InvalidParameterValue&lt;/code&gt; error.&lt;/p&gt; &lt;p&gt;The response contains a &lt;a&gt;TrustedAdvisorCheckRefreshStatus&lt;/a&gt; object.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; &lt;p&gt;To call the Trusted Advisor operations in the Amazon Web Services Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don&#39;t support the Trusted Advisor operations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint\&quot;&gt;About the Amazon Web Services Support API&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Support User Guide&lt;/i&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("https://support.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSSupport_20130415.RefreshTrustedAdvisorCheck"; // String | 
    RefreshTrustedAdvisorCheckRequest refreshTrustedAdvisorCheckRequest = new RefreshTrustedAdvisorCheckRequest(); // RefreshTrustedAdvisorCheckRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      RefreshTrustedAdvisorCheckResponse result = apiInstance.refreshTrustedAdvisorCheck(xAmzTarget, refreshTrustedAdvisorCheckRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#refreshTrustedAdvisorCheck");
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
| **xAmzTarget** | **String**|  | [enum: AWSSupport_20130415.RefreshTrustedAdvisorCheck] |
| **refreshTrustedAdvisorCheckRequest** | [**RefreshTrustedAdvisorCheckRequest**](RefreshTrustedAdvisorCheckRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**RefreshTrustedAdvisorCheckResponse**](RefreshTrustedAdvisorCheckResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerError |  -  |

<a id="resolveCase"></a>
# **resolveCase**
> ResolveCaseResponse resolveCase(xAmzTarget, resolveCaseRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Resolves a support case. This operation takes a &lt;code&gt;caseId&lt;/code&gt; and returns the initial and final state of the case.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("https://support.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSSupport_20130415.ResolveCase"; // String | 
    ResolveCaseRequest resolveCaseRequest = new ResolveCaseRequest(); // ResolveCaseRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ResolveCaseResponse result = apiInstance.resolveCase(xAmzTarget, resolveCaseRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#resolveCase");
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
| **xAmzTarget** | **String**|  | [enum: AWSSupport_20130415.ResolveCase] |
| **resolveCaseRequest** | [**ResolveCaseRequest**](ResolveCaseRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ResolveCaseResponse**](ResolveCaseResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerError |  -  |
| **481** | CaseIdNotFound |  -  |

