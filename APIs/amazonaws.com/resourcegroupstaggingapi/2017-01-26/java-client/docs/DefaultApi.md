# DefaultApi

All URIs are relative to *http://tagging.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**describeReportCreation**](DefaultApi.md#describeReportCreation) | **POST** /#X-Amz-Target&#x3D;ResourceGroupsTaggingAPI_20170126.DescribeReportCreation |  |
| [**getComplianceSummary**](DefaultApi.md#getComplianceSummary) | **POST** /#X-Amz-Target&#x3D;ResourceGroupsTaggingAPI_20170126.GetComplianceSummary |  |
| [**getResources**](DefaultApi.md#getResources) | **POST** /#X-Amz-Target&#x3D;ResourceGroupsTaggingAPI_20170126.GetResources |  |
| [**getTagKeys**](DefaultApi.md#getTagKeys) | **POST** /#X-Amz-Target&#x3D;ResourceGroupsTaggingAPI_20170126.GetTagKeys |  |
| [**getTagValues**](DefaultApi.md#getTagValues) | **POST** /#X-Amz-Target&#x3D;ResourceGroupsTaggingAPI_20170126.GetTagValues |  |
| [**startReportCreation**](DefaultApi.md#startReportCreation) | **POST** /#X-Amz-Target&#x3D;ResourceGroupsTaggingAPI_20170126.StartReportCreation |  |
| [**tagResources**](DefaultApi.md#tagResources) | **POST** /#X-Amz-Target&#x3D;ResourceGroupsTaggingAPI_20170126.TagResources |  |
| [**untagResources**](DefaultApi.md#untagResources) | **POST** /#X-Amz-Target&#x3D;ResourceGroupsTaggingAPI_20170126.UntagResources |  |


<a id="describeReportCreation"></a>
# **describeReportCreation**
> DescribeReportCreationOutput describeReportCreation(xAmzTarget, body, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Describes the status of the &lt;code&gt;StartReportCreation&lt;/code&gt; operation. &lt;/p&gt; &lt;p&gt;You can call this operation only from the organization&#39;s management account and from the us-east-1 Region.&lt;/p&gt;

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
    defaultClient.setBasePath("http://tagging.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ResourceGroupsTaggingAPI_20170126.DescribeReportCreation"; // String | 
    Object body = null; // Object | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeReportCreationOutput result = apiInstance.describeReportCreation(xAmzTarget, body, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeReportCreation");
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
| **xAmzTarget** | **String**|  | [enum: ResourceGroupsTaggingAPI_20170126.DescribeReportCreation] |
| **body** | **Object**|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeReportCreationOutput**](DescribeReportCreationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ConstraintViolationException |  -  |
| **481** | InternalServiceException |  -  |
| **482** | InvalidParameterException |  -  |
| **483** | ThrottledException |  -  |

<a id="getComplianceSummary"></a>
# **getComplianceSummary**
> GetComplianceSummaryOutput getComplianceSummary(xAmzTarget, getComplianceSummaryInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, paginationToken)



&lt;p&gt;Returns a table that shows counts of resources that are noncompliant with their tag policies.&lt;/p&gt; &lt;p&gt;For more information on tag policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html\&quot;&gt;Tag Policies&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;You can call this operation only from the organization&#39;s management account and from the us-east-1 Region.&lt;/p&gt; &lt;p&gt;This operation supports pagination, where the response can be sent in multiple pages. You should check the &lt;code&gt;PaginationToken&lt;/code&gt; response parameter to determine if there are additional results available to return. Repeat the query, passing the &lt;code&gt;PaginationToken&lt;/code&gt; response parameter value as an input to the next request until you recieve a &lt;code&gt;null&lt;/code&gt; value. A null value for &lt;code&gt;PaginationToken&lt;/code&gt; indicates that there are no more results waiting to be returned.&lt;/p&gt;

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
    defaultClient.setBasePath("http://tagging.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ResourceGroupsTaggingAPI_20170126.GetComplianceSummary"; // String | 
    GetComplianceSummaryInput getComplianceSummaryInput = new GetComplianceSummaryInput(); // GetComplianceSummaryInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String paginationToken = "paginationToken_example"; // String | Pagination token
    try {
      GetComplianceSummaryOutput result = apiInstance.getComplianceSummary(xAmzTarget, getComplianceSummaryInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, paginationToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getComplianceSummary");
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
| **xAmzTarget** | **String**|  | [enum: ResourceGroupsTaggingAPI_20170126.GetComplianceSummary] |
| **getComplianceSummaryInput** | [**GetComplianceSummaryInput**](GetComplianceSummaryInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **paginationToken** | **String**| Pagination token | [optional] |

### Return type

[**GetComplianceSummaryOutput**](GetComplianceSummaryOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ConstraintViolationException |  -  |
| **481** | InternalServiceException |  -  |
| **482** | InvalidParameterException |  -  |
| **483** | ThrottledException |  -  |

<a id="getResources"></a>
# **getResources**
> GetResourcesOutput getResources(xAmzTarget, getResourcesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, resourcesPerPage, paginationToken)



&lt;p&gt;Returns all the tagged or previously tagged resources that are located in the specified Amazon Web Services Region for the account.&lt;/p&gt; &lt;p&gt;Depending on what information you want returned, you can also specify the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Filters&lt;/i&gt; that specify what tags and resource types you want returned. The response includes all tags that are associated with the requested resources.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Information about compliance with the account&#39;s effective tag policy. For more information on tag policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html\&quot;&gt;Tag Policies&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation supports pagination, where the response can be sent in multiple pages. You should check the &lt;code&gt;PaginationToken&lt;/code&gt; response parameter to determine if there are additional results available to return. Repeat the query, passing the &lt;code&gt;PaginationToken&lt;/code&gt; response parameter value as an input to the next request until you recieve a &lt;code&gt;null&lt;/code&gt; value. A null value for &lt;code&gt;PaginationToken&lt;/code&gt; indicates that there are no more results waiting to be returned.&lt;/p&gt;

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
    defaultClient.setBasePath("http://tagging.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ResourceGroupsTaggingAPI_20170126.GetResources"; // String | 
    GetResourcesInput getResourcesInput = new GetResourcesInput(); // GetResourcesInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String resourcesPerPage = "resourcesPerPage_example"; // String | Pagination limit
    String paginationToken = "paginationToken_example"; // String | Pagination token
    try {
      GetResourcesOutput result = apiInstance.getResources(xAmzTarget, getResourcesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, resourcesPerPage, paginationToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getResources");
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
| **xAmzTarget** | **String**|  | [enum: ResourceGroupsTaggingAPI_20170126.GetResources] |
| **getResourcesInput** | [**GetResourcesInput**](GetResourcesInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **resourcesPerPage** | **String**| Pagination limit | [optional] |
| **paginationToken** | **String**| Pagination token | [optional] |

### Return type

[**GetResourcesOutput**](GetResourcesOutput.md)

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
| **481** | ThrottledException |  -  |
| **482** | InternalServiceException |  -  |
| **483** | PaginationTokenExpiredException |  -  |

<a id="getTagKeys"></a>
# **getTagKeys**
> GetTagKeysOutput getTagKeys(xAmzTarget, getTagKeysInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, paginationToken)



&lt;p&gt;Returns all tag keys currently in use in the specified Amazon Web Services Region for the calling account.&lt;/p&gt; &lt;p&gt;This operation supports pagination, where the response can be sent in multiple pages. You should check the &lt;code&gt;PaginationToken&lt;/code&gt; response parameter to determine if there are additional results available to return. Repeat the query, passing the &lt;code&gt;PaginationToken&lt;/code&gt; response parameter value as an input to the next request until you recieve a &lt;code&gt;null&lt;/code&gt; value. A null value for &lt;code&gt;PaginationToken&lt;/code&gt; indicates that there are no more results waiting to be returned.&lt;/p&gt;

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
    defaultClient.setBasePath("http://tagging.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ResourceGroupsTaggingAPI_20170126.GetTagKeys"; // String | 
    GetTagKeysInput getTagKeysInput = new GetTagKeysInput(); // GetTagKeysInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String paginationToken = "paginationToken_example"; // String | Pagination token
    try {
      GetTagKeysOutput result = apiInstance.getTagKeys(xAmzTarget, getTagKeysInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, paginationToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getTagKeys");
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
| **xAmzTarget** | **String**|  | [enum: ResourceGroupsTaggingAPI_20170126.GetTagKeys] |
| **getTagKeysInput** | [**GetTagKeysInput**](GetTagKeysInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **paginationToken** | **String**| Pagination token | [optional] |

### Return type

[**GetTagKeysOutput**](GetTagKeysOutput.md)

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
| **481** | ThrottledException |  -  |
| **482** | InternalServiceException |  -  |
| **483** | PaginationTokenExpiredException |  -  |

<a id="getTagValues"></a>
# **getTagValues**
> GetTagValuesOutput getTagValues(xAmzTarget, getTagValuesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, paginationToken)



&lt;p&gt;Returns all tag values for the specified key that are used in the specified Amazon Web Services Region for the calling account.&lt;/p&gt; &lt;p&gt;This operation supports pagination, where the response can be sent in multiple pages. You should check the &lt;code&gt;PaginationToken&lt;/code&gt; response parameter to determine if there are additional results available to return. Repeat the query, passing the &lt;code&gt;PaginationToken&lt;/code&gt; response parameter value as an input to the next request until you recieve a &lt;code&gt;null&lt;/code&gt; value. A null value for &lt;code&gt;PaginationToken&lt;/code&gt; indicates that there are no more results waiting to be returned.&lt;/p&gt;

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
    defaultClient.setBasePath("http://tagging.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ResourceGroupsTaggingAPI_20170126.GetTagValues"; // String | 
    GetTagValuesInput getTagValuesInput = new GetTagValuesInput(); // GetTagValuesInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String paginationToken = "paginationToken_example"; // String | Pagination token
    try {
      GetTagValuesOutput result = apiInstance.getTagValues(xAmzTarget, getTagValuesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, paginationToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getTagValues");
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
| **xAmzTarget** | **String**|  | [enum: ResourceGroupsTaggingAPI_20170126.GetTagValues] |
| **getTagValuesInput** | [**GetTagValuesInput**](GetTagValuesInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **paginationToken** | **String**| Pagination token | [optional] |

### Return type

[**GetTagValuesOutput**](GetTagValuesOutput.md)

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
| **481** | ThrottledException |  -  |
| **482** | InternalServiceException |  -  |
| **483** | PaginationTokenExpiredException |  -  |

<a id="startReportCreation"></a>
# **startReportCreation**
> Object startReportCreation(xAmzTarget, startReportCreationInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Generates a report that lists all tagged resources in the accounts across your organization and tells whether each resource is compliant with the effective tag policy. Compliance data is refreshed daily. The report is generated asynchronously.&lt;/p&gt; &lt;p&gt;The generated report is saved to the following location:&lt;/p&gt; &lt;p&gt; &lt;code&gt;s3://example-bucket/AwsTagPolicies/o-exampleorgid/YYYY-MM-ddTHH:mm:ssZ/report.csv&lt;/code&gt; &lt;/p&gt; &lt;p&gt;You can call this operation only from the organization&#39;s management account and from the us-east-1 Region.&lt;/p&gt;

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
    defaultClient.setBasePath("http://tagging.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ResourceGroupsTaggingAPI_20170126.StartReportCreation"; // String | 
    StartReportCreationInput startReportCreationInput = new StartReportCreationInput(); // StartReportCreationInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.startReportCreation(xAmzTarget, startReportCreationInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startReportCreation");
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
| **xAmzTarget** | **String**|  | [enum: ResourceGroupsTaggingAPI_20170126.StartReportCreation] |
| **startReportCreationInput** | [**StartReportCreationInput**](StartReportCreationInput.md)|  | |
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
| **480** | ConcurrentModificationException |  -  |
| **481** | ConstraintViolationException |  -  |
| **482** | InternalServiceException |  -  |
| **483** | InvalidParameterException |  -  |
| **484** | ThrottledException |  -  |

<a id="tagResources"></a>
# **tagResources**
> TagResourcesOutput tagResources(xAmzTarget, tagResourcesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Applies one or more tags to the specified resources. Note the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Not all resources can have tags. For a list of services with resources that support tagging using this operation, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/supported-services.html\&quot;&gt;Services that support the Resource Groups Tagging API&lt;/a&gt;. If the resource doesn&#39;t yet support this operation, the resource&#39;s service might support tagging using its own API operations. For more information, refer to the documentation for that service.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Each resource can have up to 50 tags. For other limits, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions\&quot;&gt;Tag Naming and Usage Conventions&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can only tag resources that are located in the specified Amazon Web Services Region for the Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To add tags to a resource, you need the necessary permissions for the service that the resource belongs to as well as permissions for adding tags. For more information, see the documentation for each service.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;important&gt; &lt;p&gt;Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. We use tags to provide you with billing and administration services. Tags are not intended to be used for private or sensitive data.&lt;/p&gt; &lt;/important&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;In addition to the &lt;code&gt;tag:TagResources&lt;/code&gt; permission required by this operation, you must also have the tagging permission defined by the service that created the resource. For example, to tag an Amazon EC2 instance using the &lt;code&gt;TagResources&lt;/code&gt; operation, you must have both of the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;tag:TagResource&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ec2:CreateTags&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    defaultClient.setBasePath("http://tagging.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ResourceGroupsTaggingAPI_20170126.TagResources"; // String | 
    TagResourcesInput tagResourcesInput = new TagResourcesInput(); // TagResourcesInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      TagResourcesOutput result = apiInstance.tagResources(xAmzTarget, tagResourcesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tagResources");
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
| **xAmzTarget** | **String**|  | [enum: ResourceGroupsTaggingAPI_20170126.TagResources] |
| **tagResourcesInput** | [**TagResourcesInput**](TagResourcesInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**TagResourcesOutput**](TagResourcesOutput.md)

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
| **481** | ThrottledException |  -  |
| **482** | InternalServiceException |  -  |

<a id="untagResources"></a>
# **untagResources**
> UntagResourcesOutput untagResources(xAmzTarget, untagResourcesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Removes the specified tags from the specified resources. When you specify a tag key, the action removes both that key and its associated value. The operation succeeds even if you attempt to remove tags from a resource that were already removed. Note the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To remove tags from a resource, you need the necessary permissions for the service that the resource belongs to as well as permissions for removing tags. For more information, see the documentation for the service whose resource you want to untag.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can only tag resources that are located in the specified Amazon Web Services Region for the calling Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;In addition to the &lt;code&gt;tag:UntagResources&lt;/code&gt; permission required by this operation, you must also have the remove tags permission defined by the service that created the resource. For example, to remove the tags from an Amazon EC2 instance using the &lt;code&gt;UntagResources&lt;/code&gt; operation, you must have both of the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;tag:UntagResource&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ec2:DeleteTags&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    defaultClient.setBasePath("http://tagging.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "ResourceGroupsTaggingAPI_20170126.UntagResources"; // String | 
    UntagResourcesInput untagResourcesInput = new UntagResourcesInput(); // UntagResourcesInput | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UntagResourcesOutput result = apiInstance.untagResources(xAmzTarget, untagResourcesInput, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#untagResources");
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
| **xAmzTarget** | **String**|  | [enum: ResourceGroupsTaggingAPI_20170126.UntagResources] |
| **untagResourcesInput** | [**UntagResourcesInput**](UntagResourcesInput.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UntagResourcesOutput**](UntagResourcesOutput.md)

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
| **481** | ThrottledException |  -  |
| **482** | InternalServiceException |  -  |

