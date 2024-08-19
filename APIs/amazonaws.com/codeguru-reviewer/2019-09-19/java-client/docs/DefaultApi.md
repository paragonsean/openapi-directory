# DefaultApi

All URIs are relative to *http://codeguru-reviewer.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**associateRepository**](DefaultApi.md#associateRepository) | **POST** /associations |  |
| [**createCodeReview**](DefaultApi.md#createCodeReview) | **POST** /codereviews |  |
| [**describeCodeReview**](DefaultApi.md#describeCodeReview) | **GET** /codereviews/{CodeReviewArn} |  |
| [**describeRecommendationFeedback**](DefaultApi.md#describeRecommendationFeedback) | **GET** /feedback/{CodeReviewArn}#RecommendationId |  |
| [**describeRepositoryAssociation**](DefaultApi.md#describeRepositoryAssociation) | **GET** /associations/{AssociationArn} |  |
| [**disassociateRepository**](DefaultApi.md#disassociateRepository) | **DELETE** /associations/{AssociationArn} |  |
| [**listCodeReviews**](DefaultApi.md#listCodeReviews) | **GET** /codereviews#Type |  |
| [**listRecommendationFeedback**](DefaultApi.md#listRecommendationFeedback) | **GET** /feedback/{CodeReviewArn}/RecommendationFeedback |  |
| [**listRecommendations**](DefaultApi.md#listRecommendations) | **GET** /codereviews/{CodeReviewArn}/Recommendations |  |
| [**listRepositoryAssociations**](DefaultApi.md#listRepositoryAssociations) | **GET** /associations |  |
| [**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} |  |
| [**putRecommendationFeedback**](DefaultApi.md#putRecommendationFeedback) | **PUT** /feedback |  |
| [**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} |  |
| [**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys |  |


<a id="associateRepository"></a>
# **associateRepository**
> AssociateRepositoryResponse associateRepository(associateRepositoryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Use to associate an Amazon Web Services CodeCommit repository or a repository managed by Amazon Web Services CodeStar Connections with Amazon CodeGuru Reviewer. When you associate a repository, CodeGuru Reviewer reviews source code changes in the repository&#39;s pull requests and provides automatic recommendations. You can view recommendations using the CodeGuru Reviewer console. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/recommendations.html\&quot;&gt;Recommendations in Amazon CodeGuru Reviewer&lt;/a&gt; in the &lt;i&gt;Amazon CodeGuru Reviewer User Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;If you associate a CodeCommit or S3 repository, it must be in the same Amazon Web Services Region and Amazon Web Services account where its CodeGuru Reviewer code reviews are configured.&lt;/p&gt; &lt;p&gt;Bitbucket and GitHub Enterprise Server repositories are managed by Amazon Web Services CodeStar Connections to connect to CodeGuru Reviewer. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/getting-started-associate-repository.html\&quot;&gt;Associate a repository&lt;/a&gt; in the &lt;i&gt;Amazon CodeGuru Reviewer User Guide.&lt;/i&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;You cannot use the CodeGuru Reviewer SDK or the Amazon Web Services CLI to associate a GitHub repository with Amazon CodeGuru Reviewer. To associate a GitHub repository, use the console. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/getting-started-with-guru.html\&quot;&gt;Getting started with CodeGuru Reviewer&lt;/a&gt; in the &lt;i&gt;CodeGuru Reviewer User Guide.&lt;/i&gt; &lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("http://codeguru-reviewer.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    AssociateRepositoryRequest associateRepositoryRequest = new AssociateRepositoryRequest(); // AssociateRepositoryRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      AssociateRepositoryResponse result = apiInstance.associateRepository(associateRepositoryRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#associateRepository");
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
| **associateRepositoryRequest** | [**AssociateRepositoryRequest**](AssociateRepositoryRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**AssociateRepositoryResponse**](AssociateRepositoryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ValidationException |  -  |
| **482** | AccessDeniedException |  -  |
| **483** | ConflictException |  -  |
| **484** | ThrottlingException |  -  |

<a id="createCodeReview"></a>
# **createCodeReview**
> CreateCodeReviewResponse createCodeReview(createCodeReviewRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Use to create a code review with a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReviewType.html\&quot;&gt;CodeReviewType&lt;/a&gt; of &lt;code&gt;RepositoryAnalysis&lt;/code&gt;. This type of code review analyzes all code under a specified branch in an associated repository. &lt;code&gt;PullRequest&lt;/code&gt; code reviews are automatically triggered by a pull request.

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
    defaultClient.setBasePath("http://codeguru-reviewer.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateCodeReviewRequest createCodeReviewRequest = new CreateCodeReviewRequest(); // CreateCodeReviewRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateCodeReviewResponse result = apiInstance.createCodeReview(createCodeReviewRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createCodeReview");
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
| **createCodeReviewRequest** | [**CreateCodeReviewRequest**](CreateCodeReviewRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateCodeReviewResponse**](CreateCodeReviewResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ValidationException |  -  |
| **483** | ConflictException |  -  |
| **484** | AccessDeniedException |  -  |
| **485** | ThrottlingException |  -  |

<a id="describeCodeReview"></a>
# **describeCodeReview**
> DescribeCodeReviewResponse describeCodeReview(codeReviewArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Returns the metadata associated with the code review along with its status.

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
    defaultClient.setBasePath("http://codeguru-reviewer.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String codeReviewArn = "codeReviewArn_example"; // String | The Amazon Resource Name (ARN) of the <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html\">CodeReview</a> object. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeCodeReviewResponse result = apiInstance.describeCodeReview(codeReviewArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeCodeReview");
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
| **codeReviewArn** | **String**| The Amazon Resource Name (ARN) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html\&quot;&gt;CodeReview&lt;/a&gt; object.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeCodeReviewResponse**](DescribeCodeReviewResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ValidationException |  -  |
| **483** | AccessDeniedException |  -  |
| **484** | ThrottlingException |  -  |

<a id="describeRecommendationFeedback"></a>
# **describeRecommendationFeedback**
> DescribeRecommendationFeedbackResponse describeRecommendationFeedback(codeReviewArn, recommendationId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, userId)



Describes the customer feedback for a CodeGuru Reviewer recommendation.

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
    defaultClient.setBasePath("http://codeguru-reviewer.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String codeReviewArn = "codeReviewArn_example"; // String | The Amazon Resource Name (ARN) of the <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html\">CodeReview</a> object. 
    String recommendationId = "recommendationId_example"; // String | The recommendation ID that can be used to track the provided recommendations and then to collect the feedback.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String userId = "userId_example"; // String | <p>Optional parameter to describe the feedback for a given user. If this is not supplied, it defaults to the user making the request.</p> <p> The <code>UserId</code> is an IAM principal that can be specified as an Amazon Web Services account ID or an Amazon Resource Name (ARN). For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying\"> Specifying a Principal</a> in the <i>Amazon Web Services Identity and Access Management User Guide</i>.</p>
    try {
      DescribeRecommendationFeedbackResponse result = apiInstance.describeRecommendationFeedback(codeReviewArn, recommendationId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeRecommendationFeedback");
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
| **codeReviewArn** | **String**| The Amazon Resource Name (ARN) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html\&quot;&gt;CodeReview&lt;/a&gt; object.  | |
| **recommendationId** | **String**| The recommendation ID that can be used to track the provided recommendations and then to collect the feedback. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **userId** | **String**| &lt;p&gt;Optional parameter to describe the feedback for a given user. If this is not supplied, it defaults to the user making the request.&lt;/p&gt; &lt;p&gt; The &lt;code&gt;UserId&lt;/code&gt; is an IAM principal that can be specified as an Amazon Web Services account ID or an Amazon Resource Name (ARN). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying\&quot;&gt; Specifying a Principal&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Identity and Access Management User Guide&lt;/i&gt;.&lt;/p&gt; | [optional] |

### Return type

[**DescribeRecommendationFeedbackResponse**](DescribeRecommendationFeedbackResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ValidationException |  -  |
| **483** | AccessDeniedException |  -  |
| **484** | ThrottlingException |  -  |

<a id="describeRepositoryAssociation"></a>
# **describeRepositoryAssociation**
> DescribeRepositoryAssociationResponse describeRepositoryAssociation(associationArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html\&quot;&gt;RepositoryAssociation&lt;/a&gt; object that contains information about the requested repository association.

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
    defaultClient.setBasePath("http://codeguru-reviewer.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String associationArn = "associationArn_example"; // String | The Amazon Resource Name (ARN) of the <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html\">RepositoryAssociation</a> object. You can retrieve this ARN by calling <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html\">ListRepositoryAssociations</a>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeRepositoryAssociationResponse result = apiInstance.describeRepositoryAssociation(associationArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeRepositoryAssociation");
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
| **associationArn** | **String**| The Amazon Resource Name (ARN) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html\&quot;&gt;RepositoryAssociation&lt;/a&gt; object. You can retrieve this ARN by calling &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html\&quot;&gt;ListRepositoryAssociations&lt;/a&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeRepositoryAssociationResponse**](DescribeRepositoryAssociationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ValidationException |  -  |
| **483** | AccessDeniedException |  -  |
| **484** | ThrottlingException |  -  |

<a id="disassociateRepository"></a>
# **disassociateRepository**
> DisassociateRepositoryResponse disassociateRepository(associationArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Removes the association between Amazon CodeGuru Reviewer and a repository.

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
    defaultClient.setBasePath("http://codeguru-reviewer.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String associationArn = "associationArn_example"; // String | The Amazon Resource Name (ARN) of the <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html\">RepositoryAssociation</a> object. You can retrieve this ARN by calling <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html\">ListRepositoryAssociations</a>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DisassociateRepositoryResponse result = apiInstance.disassociateRepository(associationArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#disassociateRepository");
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
| **associationArn** | **String**| The Amazon Resource Name (ARN) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html\&quot;&gt;RepositoryAssociation&lt;/a&gt; object. You can retrieve this ARN by calling &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html\&quot;&gt;ListRepositoryAssociations&lt;/a&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DisassociateRepositoryResponse**](DisassociateRepositoryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ValidationException |  -  |
| **483** | AccessDeniedException |  -  |
| **484** | ConflictException |  -  |
| **485** | ThrottlingException |  -  |

<a id="listCodeReviews"></a>
# **listCodeReviews**
> ListCodeReviewsResponse listCodeReviews(type, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, providerTypes, states, repositoryNames, maxResults, nextToken)



Lists all the code reviews that the customer has created in the past 90 days.

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
    defaultClient.setBasePath("http://codeguru-reviewer.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String type = "PullRequest"; // String | The type of code reviews to list in the response.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    List<ProviderType> providerTypes = Arrays.asList(); // List<ProviderType> | List of provider types for filtering that needs to be applied before displaying the result. For example, <code>providerTypes=[GitHub]</code> lists code reviews from GitHub.
    List<JobState> states = Arrays.asList(); // List<JobState> | <p>List of states for filtering that needs to be applied before displaying the result. For example, <code>states=[Pending]</code> lists code reviews in the Pending state.</p> <p>The valid code review states are:</p> <ul> <li> <p> <code>Completed</code>: The code review is complete.</p> </li> <li> <p> <code>Pending</code>: The code review started and has not completed or failed.</p> </li> <li> <p> <code>Failed</code>: The code review failed.</p> </li> <li> <p> <code>Deleting</code>: The code review is being deleted.</p> </li> </ul>
    List<String> repositoryNames = Arrays.asList(); // List<String> | List of repository names for filtering that needs to be applied before displaying the result.
    Integer maxResults = 56; // Integer | The maximum number of results that are returned per call. The default is 100.
    String nextToken = "nextToken_example"; // String | If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
    try {
      ListCodeReviewsResponse result = apiInstance.listCodeReviews(type, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, providerTypes, states, repositoryNames, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listCodeReviews");
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
| **type** | **String**| The type of code reviews to list in the response. | [enum: PullRequest, RepositoryAnalysis] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **providerTypes** | [**List&lt;ProviderType&gt;**](ProviderType.md)| List of provider types for filtering that needs to be applied before displaying the result. For example, &lt;code&gt;providerTypes&#x3D;[GitHub]&lt;/code&gt; lists code reviews from GitHub. | [optional] |
| **states** | [**List&lt;JobState&gt;**](JobState.md)| &lt;p&gt;List of states for filtering that needs to be applied before displaying the result. For example, &lt;code&gt;states&#x3D;[Pending]&lt;/code&gt; lists code reviews in the Pending state.&lt;/p&gt; &lt;p&gt;The valid code review states are:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Completed&lt;/code&gt;: The code review is complete.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Pending&lt;/code&gt;: The code review started and has not completed or failed.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Failed&lt;/code&gt;: The code review failed.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Deleting&lt;/code&gt;: The code review is being deleted.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] |
| **repositoryNames** | [**List&lt;String&gt;**](String.md)| List of repository names for filtering that needs to be applied before displaying the result. | [optional] |
| **maxResults** | **Integer**| The maximum number of results that are returned per call. The default is 100. | [optional] |
| **nextToken** | **String**| If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. | [optional] |

### Return type

[**ListCodeReviewsResponse**](ListCodeReviewsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ValidationException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | AccessDeniedException |  -  |

<a id="listRecommendationFeedback"></a>
# **listRecommendationFeedback**
> ListRecommendationFeedbackResponse listRecommendationFeedback(codeReviewArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, userIds, recommendationIds)



Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RecommendationFeedbackSummary.html\&quot;&gt;RecommendationFeedbackSummary&lt;/a&gt; objects that contain customer recommendation feedback for all CodeGuru Reviewer users.

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
    defaultClient.setBasePath("http://codeguru-reviewer.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String codeReviewArn = "codeReviewArn_example"; // String | The Amazon Resource Name (ARN) of the <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html\">CodeReview</a> object. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
    Integer maxResults = 56; // Integer | The maximum number of results that are returned per call. The default is 100.
    List<String> userIds = Arrays.asList(); // List<String> | <p>An Amazon Web Services user's account ID or Amazon Resource Name (ARN). Use this ID to query the recommendation feedback for a code review from that user.</p> <p> The <code>UserId</code> is an IAM principal that can be specified as an Amazon Web Services account ID or an Amazon Resource Name (ARN). For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying\"> Specifying a Principal</a> in the <i>Amazon Web Services Identity and Access Management User Guide</i>.</p>
    List<String> recommendationIds = Arrays.asList(); // List<String> | Used to query the recommendation feedback for a given recommendation.
    try {
      ListRecommendationFeedbackResponse result = apiInstance.listRecommendationFeedback(codeReviewArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, userIds, recommendationIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listRecommendationFeedback");
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
| **codeReviewArn** | **String**| The Amazon Resource Name (ARN) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html\&quot;&gt;CodeReview&lt;/a&gt; object.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. | [optional] |
| **maxResults** | **Integer**| The maximum number of results that are returned per call. The default is 100. | [optional] |
| **userIds** | [**List&lt;String&gt;**](String.md)| &lt;p&gt;An Amazon Web Services user&#39;s account ID or Amazon Resource Name (ARN). Use this ID to query the recommendation feedback for a code review from that user.&lt;/p&gt; &lt;p&gt; The &lt;code&gt;UserId&lt;/code&gt; is an IAM principal that can be specified as an Amazon Web Services account ID or an Amazon Resource Name (ARN). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying\&quot;&gt; Specifying a Principal&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Identity and Access Management User Guide&lt;/i&gt;.&lt;/p&gt; | [optional] |
| **recommendationIds** | [**List&lt;String&gt;**](String.md)| Used to query the recommendation feedback for a given recommendation. | [optional] |

### Return type

[**ListRecommendationFeedbackResponse**](ListRecommendationFeedbackResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ValidationException |  -  |
| **483** | AccessDeniedException |  -  |
| **484** | ThrottlingException |  -  |

<a id="listRecommendations"></a>
# **listRecommendations**
> ListRecommendationsResponse listRecommendations(codeReviewArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults)



Returns the list of all recommendations for a completed code review.

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
    defaultClient.setBasePath("http://codeguru-reviewer.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String codeReviewArn = "codeReviewArn_example"; // String | The Amazon Resource Name (ARN) of the <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html\">CodeReview</a> object. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | Pagination token.
    Integer maxResults = 56; // Integer | The maximum number of results that are returned per call. The default is 100.
    try {
      ListRecommendationsResponse result = apiInstance.listRecommendations(codeReviewArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listRecommendations");
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
| **codeReviewArn** | **String**| The Amazon Resource Name (ARN) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html\&quot;&gt;CodeReview&lt;/a&gt; object.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| Pagination token. | [optional] |
| **maxResults** | **Integer**| The maximum number of results that are returned per call. The default is 100. | [optional] |

### Return type

[**ListRecommendationsResponse**](ListRecommendationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ValidationException |  -  |
| **483** | AccessDeniedException |  -  |
| **484** | ThrottlingException |  -  |

<a id="listRepositoryAssociations"></a>
# **listRepositoryAssociations**
> ListRepositoryAssociationsResponse listRepositoryAssociations(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, providerType, state, name, owner, maxResults, nextToken)



Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html\&quot;&gt;RepositoryAssociationSummary&lt;/a&gt; objects that contain summary information about a repository association. You can filter the returned list by &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html#reviewer-Type-RepositoryAssociationSummary-ProviderType\&quot;&gt;ProviderType&lt;/a&gt;, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html#reviewer-Type-RepositoryAssociationSummary-Name\&quot;&gt;Name&lt;/a&gt;, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html#reviewer-Type-RepositoryAssociationSummary-State\&quot;&gt;State&lt;/a&gt;, and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html#reviewer-Type-RepositoryAssociationSummary-Owner\&quot;&gt;Owner&lt;/a&gt;.

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
    defaultClient.setBasePath("http://codeguru-reviewer.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    List<ProviderType> providerType = Arrays.asList(); // List<ProviderType> | List of provider types to use as a filter.
    List<RepositoryAssociationState> state = Arrays.asList(); // List<RepositoryAssociationState> | <p>List of repository association states to use as a filter.</p> <p>The valid repository association states are:</p> <ul> <li> <p> <b>Associated</b>: The repository association is complete.</p> </li> <li> <p> <b>Associating</b>: CodeGuru Reviewer is:</p> <ul> <li> <p>Setting up pull request notifications. This is required for pull requests to trigger a CodeGuru Reviewer review.</p> <note> <p>If your repository <code>ProviderType</code> is <code>GitHub</code>, <code>GitHub Enterprise Server</code>, or <code>Bitbucket</code>, CodeGuru Reviewer creates webhooks in your repository to trigger CodeGuru Reviewer reviews. If you delete these webhooks, reviews of code in your repository cannot be triggered.</p> </note> </li> <li> <p>Setting up source code access. This is required for CodeGuru Reviewer to securely clone code in your repository.</p> </li> </ul> </li> <li> <p> <b>Failed</b>: The repository failed to associate or disassociate.</p> </li> <li> <p> <b>Disassociating</b>: CodeGuru Reviewer is removing the repository's pull request notifications and source code access.</p> </li> <li> <p> <b>Disassociated</b>: CodeGuru Reviewer successfully disassociated the repository. You can create a new association with this repository if you want to review source code in it later. You can control access to code reviews created in anassociated repository with tags after it has been disassociated. For more information, see <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/auth-and-access-control-using-tags.html\">Using tags to control access to associated repositories</a> in the <i>Amazon CodeGuru Reviewer User Guide</i>.</p> </li> </ul>
    List<String> name = Arrays.asList(); // List<String> | List of repository names to use as a filter.
    List<String> owner = Arrays.asList(); // List<String> | List of owners to use as a filter. For Amazon Web Services CodeCommit, it is the name of the CodeCommit account that was used to associate the repository. For other repository source providers, such as Bitbucket and GitHub Enterprise Server, this is name of the account that was used to associate the repository. 
    Integer maxResults = 56; // Integer | The maximum number of repository association results returned by <code>ListRepositoryAssociations</code> in paginated output. When this parameter is used, <code>ListRepositoryAssociations</code> only returns <code>maxResults</code> results in a single page with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListRepositoryAssociations</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter is not used, <code>ListRepositoryAssociations</code> returns up to 100 results and a <code>nextToken</code> value if applicable. 
    String nextToken = "nextToken_example"; // String | <p>The <code>nextToken</code> value returned from a previous paginated <code>ListRepositoryAssociations</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. </p> <note> <p>Treat this token as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
    try {
      ListRepositoryAssociationsResponse result = apiInstance.listRepositoryAssociations(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, providerType, state, name, owner, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listRepositoryAssociations");
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
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **providerType** | [**List&lt;ProviderType&gt;**](ProviderType.md)| List of provider types to use as a filter. | [optional] |
| **state** | [**List&lt;RepositoryAssociationState&gt;**](RepositoryAssociationState.md)| &lt;p&gt;List of repository association states to use as a filter.&lt;/p&gt; &lt;p&gt;The valid repository association states are:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Associated&lt;/b&gt;: The repository association is complete.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Associating&lt;/b&gt;: CodeGuru Reviewer is:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Setting up pull request notifications. This is required for pull requests to trigger a CodeGuru Reviewer review.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If your repository &lt;code&gt;ProviderType&lt;/code&gt; is &lt;code&gt;GitHub&lt;/code&gt;, &lt;code&gt;GitHub Enterprise Server&lt;/code&gt;, or &lt;code&gt;Bitbucket&lt;/code&gt;, CodeGuru Reviewer creates webhooks in your repository to trigger CodeGuru Reviewer reviews. If you delete these webhooks, reviews of code in your repository cannot be triggered.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Setting up source code access. This is required for CodeGuru Reviewer to securely clone code in your repository.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Failed&lt;/b&gt;: The repository failed to associate or disassociate.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Disassociating&lt;/b&gt;: CodeGuru Reviewer is removing the repository&#39;s pull request notifications and source code access.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Disassociated&lt;/b&gt;: CodeGuru Reviewer successfully disassociated the repository. You can create a new association with this repository if you want to review source code in it later. You can control access to code reviews created in anassociated repository with tags after it has been disassociated. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/auth-and-access-control-using-tags.html\&quot;&gt;Using tags to control access to associated repositories&lt;/a&gt; in the &lt;i&gt;Amazon CodeGuru Reviewer User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] |
| **name** | [**List&lt;String&gt;**](String.md)| List of repository names to use as a filter. | [optional] |
| **owner** | [**List&lt;String&gt;**](String.md)| List of owners to use as a filter. For Amazon Web Services CodeCommit, it is the name of the CodeCommit account that was used to associate the repository. For other repository source providers, such as Bitbucket and GitHub Enterprise Server, this is name of the account that was used to associate the repository.  | [optional] |
| **maxResults** | **Integer**| The maximum number of repository association results returned by &lt;code&gt;ListRepositoryAssociations&lt;/code&gt; in paginated output. When this parameter is used, &lt;code&gt;ListRepositoryAssociations&lt;/code&gt; only returns &lt;code&gt;maxResults&lt;/code&gt; results in a single page with a &lt;code&gt;nextToken&lt;/code&gt; response element. The remaining results of the initial request can be seen by sending another &lt;code&gt;ListRepositoryAssociations&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If this parameter is not used, &lt;code&gt;ListRepositoryAssociations&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable.  | [optional] |
| **nextToken** | **String**| &lt;p&gt;The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListRepositoryAssociations&lt;/code&gt; request where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Treat this token as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.&lt;/p&gt; &lt;/note&gt; | [optional] |

### Return type

[**ListRepositoryAssociationsResponse**](ListRepositoryAssociationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ValidationException |  -  |
| **482** | ThrottlingException |  -  |

<a id="listTagsForResource"></a>
# **listTagsForResource**
> ListTagsForResourceResponse listTagsForResource(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Returns the list of tags associated with an associated repository resource.

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
    defaultClient.setBasePath("http://codeguru-reviewer.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html\">RepositoryAssociation</a> object. You can retrieve this ARN by calling <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html\">ListRepositoryAssociations</a>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListTagsForResourceResponse result = apiInstance.listTagsForResource(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTagsForResource");
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
| **resourceArn** | **String**| The Amazon Resource Name (ARN) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html\&quot;&gt;RepositoryAssociation&lt;/a&gt; object. You can retrieve this ARN by calling &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html\&quot;&gt;ListRepositoryAssociations&lt;/a&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ValidationException |  -  |
| **482** | ResourceNotFoundException |  -  |

<a id="putRecommendationFeedback"></a>
# **putRecommendationFeedback**
> Object putRecommendationFeedback(putRecommendationFeedbackRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Stores customer feedback for a CodeGuru Reviewer recommendation. When this API is called again with different reactions the previous feedback is overwritten.

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
    defaultClient.setBasePath("http://codeguru-reviewer.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    PutRecommendationFeedbackRequest putRecommendationFeedbackRequest = new PutRecommendationFeedbackRequest(); // PutRecommendationFeedbackRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.putRecommendationFeedback(putRecommendationFeedbackRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putRecommendationFeedback");
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
| **putRecommendationFeedbackRequest** | [**PutRecommendationFeedbackRequest**](PutRecommendationFeedbackRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ValidationException |  -  |
| **483** | AccessDeniedException |  -  |
| **484** | ThrottlingException |  -  |

<a id="tagResource"></a>
# **tagResource**
> Object tagResource(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Adds one or more tags to an associated repository.

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
    defaultClient.setBasePath("http://codeguru-reviewer.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html\">RepositoryAssociation</a> object. You can retrieve this ARN by calling <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html\">ListRepositoryAssociations</a>.
    TagResourceRequest tagResourceRequest = new TagResourceRequest(); // TagResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.tagResource(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tagResource");
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
| **resourceArn** | **String**| The Amazon Resource Name (ARN) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html\&quot;&gt;RepositoryAssociation&lt;/a&gt; object. You can retrieve this ARN by calling &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html\&quot;&gt;ListRepositoryAssociations&lt;/a&gt;. | |
| **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ValidationException |  -  |
| **482** | ResourceNotFoundException |  -  |

<a id="untagResource"></a>
# **untagResource**
> Object untagResource(resourceArn, tagKeys, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Removes a tag from an associated repository.

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
    defaultClient.setBasePath("http://codeguru-reviewer.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html\">RepositoryAssociation</a> object. You can retrieve this ARN by calling <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html\">ListRepositoryAssociations</a>.
    List<String> tagKeys = Arrays.asList(); // List<String> | A list of the keys for each tag you want to remove from an associated repository.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.untagResource(resourceArn, tagKeys, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#untagResource");
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
| **resourceArn** | **String**| The Amazon Resource Name (ARN) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html\&quot;&gt;RepositoryAssociation&lt;/a&gt; object. You can retrieve this ARN by calling &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html\&quot;&gt;ListRepositoryAssociations&lt;/a&gt;. | |
| **tagKeys** | [**List&lt;String&gt;**](String.md)| A list of the keys for each tag you want to remove from an associated repository. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ValidationException |  -  |
| **482** | ResourceNotFoundException |  -  |

