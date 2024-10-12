# DefaultApi

All URIs are relative to *http://metering.marketplace.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**batchMeterUsage**](DefaultApi.md#batchMeterUsage) | **POST** /#X-Amz-Target&#x3D;AWSMPMeteringService.BatchMeterUsage |  |
| [**meterUsage**](DefaultApi.md#meterUsage) | **POST** /#X-Amz-Target&#x3D;AWSMPMeteringService.MeterUsage |  |
| [**registerUsage**](DefaultApi.md#registerUsage) | **POST** /#X-Amz-Target&#x3D;AWSMPMeteringService.RegisterUsage |  |
| [**resolveCustomer**](DefaultApi.md#resolveCustomer) | **POST** /#X-Amz-Target&#x3D;AWSMPMeteringService.ResolveCustomer |  |


<a id="batchMeterUsage"></a>
# **batchMeterUsage**
> BatchMeterUsageResult batchMeterUsage(xAmzTarget, batchMeterUsageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt; &lt;code&gt;BatchMeterUsage&lt;/code&gt; is called from a SaaS application listed on AWS Marketplace to post metering records for a set of customers.&lt;/p&gt; &lt;p&gt;For identical requests, the API is idempotent; requests can be retried with the same records or a subset of the input records.&lt;/p&gt; &lt;p&gt;Every request to &lt;code&gt;BatchMeterUsage&lt;/code&gt; is for one product. If you need to meter usage for multiple products, you must make multiple calls to &lt;code&gt;BatchMeterUsage&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Usage records are expected to be submitted as quickly as possible after the event that is being recorded, and are not accepted more than 6 hours after the event.&lt;/p&gt; &lt;p&gt; &lt;code&gt;BatchMeterUsage&lt;/code&gt; can process up to 25 &lt;code&gt;UsageRecords&lt;/code&gt; at a time.&lt;/p&gt; &lt;p&gt;A &lt;code&gt;UsageRecord&lt;/code&gt; can optionally include multiple usage allocations, to provide customers with usage data split into buckets by tags that you define (or allow the customer to define).&lt;/p&gt; &lt;p&gt; &lt;code&gt;BatchMeterUsage&lt;/code&gt; returns a list of &lt;code&gt;UsageRecordResult&lt;/code&gt; objects, showing the result for each &lt;code&gt;UsageRecord&lt;/code&gt;, as well as a list of &lt;code&gt;UnprocessedRecords&lt;/code&gt;, indicating errors in the service side that you should retry.&lt;/p&gt; &lt;p&gt; &lt;code&gt;BatchMeterUsage&lt;/code&gt; requests must be less than 1MB in size.&lt;/p&gt; &lt;note&gt; &lt;p&gt;For an example of using &lt;code&gt;BatchMeterUsage&lt;/code&gt;, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace/latest/userguide/saas-code-examples.html#saas-batchmeterusage-example\&quot;&gt; BatchMeterUsage code example&lt;/a&gt; in the &lt;i&gt;AWS Marketplace Seller Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("http://metering.marketplace.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSMPMeteringService.BatchMeterUsage"; // String | 
    BatchMeterUsageRequest batchMeterUsageRequest = new BatchMeterUsageRequest(); // BatchMeterUsageRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      BatchMeterUsageResult result = apiInstance.batchMeterUsage(xAmzTarget, batchMeterUsageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchMeterUsage");
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
| **xAmzTarget** | **String**|  | [enum: AWSMPMeteringService.BatchMeterUsage] |
| **batchMeterUsageRequest** | [**BatchMeterUsageRequest**](BatchMeterUsageRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**BatchMeterUsageResult**](BatchMeterUsageResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceErrorException |  -  |
| **481** | InvalidProductCodeException |  -  |
| **482** | InvalidUsageDimensionException |  -  |
| **483** | InvalidTagException |  -  |
| **484** | InvalidUsageAllocationsException |  -  |
| **485** | InvalidCustomerIdentifierException |  -  |
| **486** | TimestampOutOfBoundsException |  -  |
| **487** | ThrottlingException |  -  |
| **488** | DisabledApiException |  -  |

<a id="meterUsage"></a>
# **meterUsage**
> MeterUsageResult meterUsage(xAmzTarget, meterUsageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;API to emit metering records. For identical requests, the API is idempotent. It simply returns the metering record ID.&lt;/p&gt; &lt;p&gt; &lt;code&gt;MeterUsage&lt;/code&gt; is authenticated on the buyer&#39;s AWS account using credentials from the EC2 instance, ECS task, or EKS pod.&lt;/p&gt; &lt;p&gt; &lt;code&gt;MeterUsage&lt;/code&gt; can optionally include multiple usage allocations, to provide customers with usage data split into buckets by tags that you define (or allow the customer to define).&lt;/p&gt; &lt;p&gt;Usage records are expected to be submitted as quickly as possible after the event that is being recorded, and are not accepted more than 6 hours after the event.&lt;/p&gt;

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
    defaultClient.setBasePath("http://metering.marketplace.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSMPMeteringService.MeterUsage"; // String | 
    MeterUsageRequest meterUsageRequest = new MeterUsageRequest(); // MeterUsageRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      MeterUsageResult result = apiInstance.meterUsage(xAmzTarget, meterUsageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#meterUsage");
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
| **xAmzTarget** | **String**|  | [enum: AWSMPMeteringService.MeterUsage] |
| **meterUsageRequest** | [**MeterUsageRequest**](MeterUsageRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**MeterUsageResult**](MeterUsageResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServiceErrorException |  -  |
| **481** | InvalidProductCodeException |  -  |
| **482** | InvalidUsageDimensionException |  -  |
| **483** | InvalidTagException |  -  |
| **484** | InvalidUsageAllocationsException |  -  |
| **485** | InvalidEndpointRegionException |  -  |
| **486** | TimestampOutOfBoundsException |  -  |
| **487** | DuplicateRequestException |  -  |
| **488** | ThrottlingException |  -  |
| **489** | CustomerNotEntitledException |  -  |

<a id="registerUsage"></a>
# **registerUsage**
> RegisterUsageResult registerUsage(xAmzTarget, registerUsageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Paid container software products sold through AWS Marketplace must integrate with the AWS Marketplace Metering Service and call the &lt;code&gt;RegisterUsage&lt;/code&gt; operation for software entitlement and metering. Free and BYOL products for Amazon ECS or Amazon EKS aren&#39;t required to call &lt;code&gt;RegisterUsage&lt;/code&gt;, but you may choose to do so if you would like to receive usage data in your seller reports. The sections below explain the behavior of &lt;code&gt;RegisterUsage&lt;/code&gt;. &lt;code&gt;RegisterUsage&lt;/code&gt; performs two primary functions: metering and entitlement.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Entitlement&lt;/i&gt;: &lt;code&gt;RegisterUsage&lt;/code&gt; allows you to verify that the customer running your paid software is subscribed to your product on AWS Marketplace, enabling you to guard against unauthorized use. Your container image that integrates with &lt;code&gt;RegisterUsage&lt;/code&gt; is only required to guard against unauthorized use at container startup, as such a &lt;code&gt;CustomerNotSubscribedException&lt;/code&gt; or &lt;code&gt;PlatformNotSupportedException&lt;/code&gt; will only be thrown on the initial call to &lt;code&gt;RegisterUsage&lt;/code&gt;. Subsequent calls from the same Amazon ECS task instance (e.g. task-id) or Amazon EKS pod will not throw a &lt;code&gt;CustomerNotSubscribedException&lt;/code&gt;, even if the customer unsubscribes while the Amazon ECS task or Amazon EKS pod is still running.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Metering&lt;/i&gt;: &lt;code&gt;RegisterUsage&lt;/code&gt; meters software use per ECS task, per hour, or per pod for Amazon EKS with usage prorated to the second. A minimum of 1 minute of usage applies to tasks that are short lived. For example, if a customer has a 10 node Amazon ECS or Amazon EKS cluster and a service configured as a Daemon Set, then Amazon ECS or Amazon EKS will launch a task on all 10 cluster nodes and the customer will be charged: (10 * hourly_rate). Metering for software use is automatically handled by the AWS Marketplace Metering Control Plane -- your software is not required to perform any metering specific actions, other than call &lt;code&gt;RegisterUsage&lt;/code&gt; once for metering of software use to commence. The AWS Marketplace Metering Control Plane will also continue to bill customers for running ECS tasks and Amazon EKS pods, regardless of the customers subscription state, removing the need for your software to perform entitlement checks at runtime.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    defaultClient.setBasePath("http://metering.marketplace.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSMPMeteringService.RegisterUsage"; // String | 
    RegisterUsageRequest registerUsageRequest = new RegisterUsageRequest(); // RegisterUsageRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      RegisterUsageResult result = apiInstance.registerUsage(xAmzTarget, registerUsageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#registerUsage");
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
| **xAmzTarget** | **String**|  | [enum: AWSMPMeteringService.RegisterUsage] |
| **registerUsageRequest** | [**RegisterUsageRequest**](RegisterUsageRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**RegisterUsageResult**](RegisterUsageResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidProductCodeException |  -  |
| **481** | InvalidRegionException |  -  |
| **482** | InvalidPublicKeyVersionException |  -  |
| **483** | PlatformNotSupportedException |  -  |
| **484** | CustomerNotEntitledException |  -  |
| **485** | ThrottlingException |  -  |
| **486** | InternalServiceErrorException |  -  |
| **487** | DisabledApiException |  -  |

<a id="resolveCustomer"></a>
# **resolveCustomer**
> ResolveCustomerResult resolveCustomer(xAmzTarget, resolveCustomerRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt; &lt;code&gt;ResolveCustomer&lt;/code&gt; is called by a SaaS application during the registration process. When a buyer visits your website during the registration process, the buyer submits a registration token through their browser. The registration token is resolved through this API to obtain a &lt;code&gt;CustomerIdentifier&lt;/code&gt; along with the &lt;code&gt;CustomerAWSAccountId&lt;/code&gt; and &lt;code&gt;ProductCode&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The API needs to called from the seller account id used to publish the SaaS application to successfully resolve the token.&lt;/p&gt; &lt;p&gt;For an example of using &lt;code&gt;ResolveCustomer&lt;/code&gt;, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace/latest/userguide/saas-code-examples.html#saas-resolvecustomer-example\&quot;&gt; ResolveCustomer code example&lt;/a&gt; in the &lt;i&gt;AWS Marketplace Seller Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("http://metering.marketplace.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "AWSMPMeteringService.ResolveCustomer"; // String | 
    ResolveCustomerRequest resolveCustomerRequest = new ResolveCustomerRequest(); // ResolveCustomerRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ResolveCustomerResult result = apiInstance.resolveCustomer(xAmzTarget, resolveCustomerRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#resolveCustomer");
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
| **xAmzTarget** | **String**|  | [enum: AWSMPMeteringService.ResolveCustomer] |
| **resolveCustomerRequest** | [**ResolveCustomerRequest**](ResolveCustomerRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ResolveCustomerResult**](ResolveCustomerResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidTokenException |  -  |
| **481** | ExpiredTokenException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | InternalServiceErrorException |  -  |
| **484** | DisabledApiException |  -  |

