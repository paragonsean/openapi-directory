# DefaultApi

All URIs are relative to *http://kinesisanalytics.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addApplicationCloudWatchLoggingOption**](DefaultApi.md#addApplicationCloudWatchLoggingOption) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20150814.AddApplicationCloudWatchLoggingOption |  |
| [**addApplicationInput**](DefaultApi.md#addApplicationInput) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20150814.AddApplicationInput |  |
| [**addApplicationInputProcessingConfiguration**](DefaultApi.md#addApplicationInputProcessingConfiguration) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20150814.AddApplicationInputProcessingConfiguration |  |
| [**addApplicationOutput**](DefaultApi.md#addApplicationOutput) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20150814.AddApplicationOutput |  |
| [**addApplicationReferenceDataSource**](DefaultApi.md#addApplicationReferenceDataSource) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20150814.AddApplicationReferenceDataSource |  |
| [**createApplication**](DefaultApi.md#createApplication) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20150814.CreateApplication |  |
| [**deleteApplication**](DefaultApi.md#deleteApplication) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20150814.DeleteApplication |  |
| [**deleteApplicationCloudWatchLoggingOption**](DefaultApi.md#deleteApplicationCloudWatchLoggingOption) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20150814.DeleteApplicationCloudWatchLoggingOption |  |
| [**deleteApplicationInputProcessingConfiguration**](DefaultApi.md#deleteApplicationInputProcessingConfiguration) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20150814.DeleteApplicationInputProcessingConfiguration |  |
| [**deleteApplicationOutput**](DefaultApi.md#deleteApplicationOutput) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20150814.DeleteApplicationOutput |  |
| [**deleteApplicationReferenceDataSource**](DefaultApi.md#deleteApplicationReferenceDataSource) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20150814.DeleteApplicationReferenceDataSource |  |
| [**describeApplication**](DefaultApi.md#describeApplication) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20150814.DescribeApplication |  |
| [**discoverInputSchema**](DefaultApi.md#discoverInputSchema) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20150814.DiscoverInputSchema |  |
| [**listApplications**](DefaultApi.md#listApplications) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20150814.ListApplications |  |
| [**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20150814.ListTagsForResource |  |
| [**startApplication**](DefaultApi.md#startApplication) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20150814.StartApplication |  |
| [**stopApplication**](DefaultApi.md#stopApplication) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20150814.StopApplication |  |
| [**tagResource**](DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20150814.TagResource |  |
| [**untagResource**](DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20150814.UntagResource |  |
| [**updateApplication**](DefaultApi.md#updateApplication) | **POST** /#X-Amz-Target&#x3D;KinesisAnalytics_20150814.UpdateApplication |  |


<a id="addApplicationCloudWatchLoggingOption"></a>
# **addApplicationCloudWatchLoggingOption**
> Object addApplicationCloudWatchLoggingOption(xAmzTarget, addApplicationCloudWatchLoggingOptionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Adds a CloudWatch log stream to monitor application configuration errors. For more information about using CloudWatch log streams with Amazon Kinesis Analytics applications, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-logs.html\&quot;&gt;Working with Amazon CloudWatch Logs&lt;/a&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("http://kinesisanalytics.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "KinesisAnalytics_20150814.AddApplicationCloudWatchLoggingOption"; // String | 
    AddApplicationCloudWatchLoggingOptionRequest addApplicationCloudWatchLoggingOptionRequest = new AddApplicationCloudWatchLoggingOptionRequest(); // AddApplicationCloudWatchLoggingOptionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.addApplicationCloudWatchLoggingOption(xAmzTarget, addApplicationCloudWatchLoggingOptionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addApplicationCloudWatchLoggingOption");
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
| **xAmzTarget** | **String**|  | [enum: KinesisAnalytics_20150814.AddApplicationCloudWatchLoggingOption] |
| **addApplicationCloudWatchLoggingOptionRequest** | [**AddApplicationCloudWatchLoggingOptionRequest**](AddApplicationCloudWatchLoggingOptionRequest.md)|  | |
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
| **481** | ResourceInUseException |  -  |
| **482** | InvalidArgumentException |  -  |
| **483** | ConcurrentModificationException |  -  |
| **484** | UnsupportedOperationException |  -  |

<a id="addApplicationInput"></a>
# **addApplicationInput**
> Object addApplicationInput(xAmzTarget, addApplicationInputRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; Adds a streaming source to your Amazon Kinesis application. For conceptual information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html\&quot;&gt;Configuring Application Input&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;You can add a streaming source either when you create an application or you can use this operation to add a streaming source after you create an application. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_CreateApplication.html\&quot;&gt;CreateApplication&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html\&quot;&gt;DescribeApplication&lt;/a&gt; operation to find the current application version. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:AddApplicationInput&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://kinesisanalytics.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "KinesisAnalytics_20150814.AddApplicationInput"; // String | 
    AddApplicationInputRequest addApplicationInputRequest = new AddApplicationInputRequest(); // AddApplicationInputRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.addApplicationInput(xAmzTarget, addApplicationInputRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addApplicationInput");
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
| **xAmzTarget** | **String**|  | [enum: KinesisAnalytics_20150814.AddApplicationInput] |
| **addApplicationInputRequest** | [**AddApplicationInputRequest**](AddApplicationInputRequest.md)|  | |
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
| **481** | ResourceInUseException |  -  |
| **482** | InvalidArgumentException |  -  |
| **483** | ConcurrentModificationException |  -  |
| **484** | CodeValidationException |  -  |
| **485** | UnsupportedOperationException |  -  |

<a id="addApplicationInputProcessingConfiguration"></a>
# **addApplicationInputProcessingConfiguration**
> Object addApplicationInputProcessingConfiguration(xAmzTarget, addApplicationInputProcessingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Adds an &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfiguration.html\&quot;&gt;InputProcessingConfiguration&lt;/a&gt; to an application. An input processor preprocesses records on the input stream before the application&#39;s SQL code executes. Currently, the only input processor available is &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lambda/\&quot;&gt;AWS Lambda&lt;/a&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("http://kinesisanalytics.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "KinesisAnalytics_20150814.AddApplicationInputProcessingConfiguration"; // String | 
    AddApplicationInputProcessingConfigurationRequest addApplicationInputProcessingConfigurationRequest = new AddApplicationInputProcessingConfigurationRequest(); // AddApplicationInputProcessingConfigurationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.addApplicationInputProcessingConfiguration(xAmzTarget, addApplicationInputProcessingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addApplicationInputProcessingConfiguration");
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
| **xAmzTarget** | **String**|  | [enum: KinesisAnalytics_20150814.AddApplicationInputProcessingConfiguration] |
| **addApplicationInputProcessingConfigurationRequest** | [**AddApplicationInputProcessingConfigurationRequest**](AddApplicationInputProcessingConfigurationRequest.md)|  | |
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
| **481** | ResourceInUseException |  -  |
| **482** | InvalidArgumentException |  -  |
| **483** | ConcurrentModificationException |  -  |
| **484** | UnsupportedOperationException |  -  |

<a id="addApplicationOutput"></a>
# **addApplicationOutput**
> Object addApplicationOutput(xAmzTarget, addApplicationOutputRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Adds an external destination to your Amazon Kinesis Analytics application.&lt;/p&gt; &lt;p&gt;If you want Amazon Kinesis Analytics to deliver data from an in-application stream within your application to an external destination (such as an Amazon Kinesis stream, an Amazon Kinesis Firehose delivery stream, or an AWS Lambda function), you add the relevant configuration to your application using this operation. You can configure one or more outputs for your application. Each output configuration maps an in-application stream and an external destination.&lt;/p&gt; &lt;p&gt; You can use one of the output configurations to deliver data from your in-application error stream to an external destination so that you can analyze the errors. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html\&quot;&gt;Understanding Application Output (Destination)&lt;/a&gt;. &lt;/p&gt; &lt;p&gt; Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html\&quot;&gt;DescribeApplication&lt;/a&gt; operation to find the current application version.&lt;/p&gt; &lt;p&gt;For the limits on the number of application inputs and outputs you can configure, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html\&quot;&gt;Limits&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:AddApplicationOutput&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://kinesisanalytics.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "KinesisAnalytics_20150814.AddApplicationOutput"; // String | 
    AddApplicationOutputRequest addApplicationOutputRequest = new AddApplicationOutputRequest(); // AddApplicationOutputRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.addApplicationOutput(xAmzTarget, addApplicationOutputRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addApplicationOutput");
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
| **xAmzTarget** | **String**|  | [enum: KinesisAnalytics_20150814.AddApplicationOutput] |
| **addApplicationOutputRequest** | [**AddApplicationOutputRequest**](AddApplicationOutputRequest.md)|  | |
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
| **481** | ResourceInUseException |  -  |
| **482** | InvalidArgumentException |  -  |
| **483** | ConcurrentModificationException |  -  |
| **484** | UnsupportedOperationException |  -  |

<a id="addApplicationReferenceDataSource"></a>
# **addApplicationReferenceDataSource**
> Object addApplicationReferenceDataSource(xAmzTarget, addApplicationReferenceDataSourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Adds a reference data source to an existing application.&lt;/p&gt; &lt;p&gt;Amazon Kinesis Analytics reads reference data (that is, an Amazon S3 object) and creates an in-application table within your application. In the request, you provide the source (S3 bucket name and object key name), name of the in-application table to create, and the necessary mapping information that describes how data in Amazon S3 object maps to columns in the resulting in-application table.&lt;/p&gt; &lt;p&gt; For conceptual information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html\&quot;&gt;Configuring Application Input&lt;/a&gt;. For the limits on data sources you can add to your application, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html\&quot;&gt;Limits&lt;/a&gt;. &lt;/p&gt; &lt;p&gt; This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:AddApplicationOutput&lt;/code&gt; action. &lt;/p&gt;

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
    defaultClient.setBasePath("http://kinesisanalytics.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "KinesisAnalytics_20150814.AddApplicationReferenceDataSource"; // String | 
    AddApplicationReferenceDataSourceRequest addApplicationReferenceDataSourceRequest = new AddApplicationReferenceDataSourceRequest(); // AddApplicationReferenceDataSourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.addApplicationReferenceDataSource(xAmzTarget, addApplicationReferenceDataSourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addApplicationReferenceDataSource");
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
| **xAmzTarget** | **String**|  | [enum: KinesisAnalytics_20150814.AddApplicationReferenceDataSource] |
| **addApplicationReferenceDataSourceRequest** | [**AddApplicationReferenceDataSourceRequest**](AddApplicationReferenceDataSourceRequest.md)|  | |
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
| **481** | ResourceInUseException |  -  |
| **482** | InvalidArgumentException |  -  |
| **483** | ConcurrentModificationException |  -  |
| **484** | UnsupportedOperationException |  -  |

<a id="createApplication"></a>
# **createApplication**
> CreateApplicationResponse createApplication(xAmzTarget, createApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; Creates an Amazon Kinesis Analytics application. You can configure each application with one streaming source as input, application code to process the input, and up to three destinations where you want Amazon Kinesis Analytics to write the output data from your application. For an overview, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works.html\&quot;&gt;How it Works&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;In the input configuration, you map the streaming source to an in-application stream, which you can think of as a constantly updating table. In the mapping, you must provide a schema for the in-application stream and map each data column in the in-application stream to a data element in the streaming source.&lt;/p&gt; &lt;p&gt;Your application code is one or more SQL statements that read input data, transform it, and generate output. Your application code can create one or more SQL artifacts like SQL streams or pumps.&lt;/p&gt; &lt;p&gt;In the output configuration, you can configure the application to write data from in-application streams created in your applications to up to three destinations.&lt;/p&gt; &lt;p&gt; To read data from your source stream or write data to destination streams, Amazon Kinesis Analytics needs your permissions. You grant these permissions by creating IAM roles. This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:CreateApplication&lt;/code&gt; action. &lt;/p&gt; &lt;p&gt; For introductory exercises to create an Amazon Kinesis Analytics application, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/getting-started.html\&quot;&gt;Getting Started&lt;/a&gt;. &lt;/p&gt;

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
    defaultClient.setBasePath("http://kinesisanalytics.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "KinesisAnalytics_20150814.CreateApplication"; // String | 
    CreateApplicationRequest createApplicationRequest = new CreateApplicationRequest(); // CreateApplicationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateApplicationResponse result = apiInstance.createApplication(xAmzTarget, createApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createApplication");
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
| **xAmzTarget** | **String**|  | [enum: KinesisAnalytics_20150814.CreateApplication] |
| **createApplicationRequest** | [**CreateApplicationRequest**](CreateApplicationRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateApplicationResponse**](CreateApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | CodeValidationException |  -  |
| **481** | ResourceInUseException |  -  |
| **482** | LimitExceededException |  -  |
| **483** | InvalidArgumentException |  -  |
| **484** | TooManyTagsException |  -  |
| **485** | ConcurrentModificationException |  -  |

<a id="deleteApplication"></a>
# **deleteApplication**
> Object deleteApplication(xAmzTarget, deleteApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Deletes the specified application. Amazon Kinesis Analytics halts application execution and deletes the application, including any application artifacts (such as in-application streams, reference table, and application code).&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:DeleteApplication&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://kinesisanalytics.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "KinesisAnalytics_20150814.DeleteApplication"; // String | 
    DeleteApplicationRequest deleteApplicationRequest = new DeleteApplicationRequest(); // DeleteApplicationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteApplication(xAmzTarget, deleteApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteApplication");
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
| **xAmzTarget** | **String**|  | [enum: KinesisAnalytics_20150814.DeleteApplication] |
| **deleteApplicationRequest** | [**DeleteApplicationRequest**](DeleteApplicationRequest.md)|  | |
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
| **481** | ResourceNotFoundException |  -  |
| **482** | ResourceInUseException |  -  |
| **483** | UnsupportedOperationException |  -  |

<a id="deleteApplicationCloudWatchLoggingOption"></a>
# **deleteApplicationCloudWatchLoggingOption**
> Object deleteApplicationCloudWatchLoggingOption(xAmzTarget, deleteApplicationCloudWatchLoggingOptionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Deletes a CloudWatch log stream from an application. For more information about using CloudWatch log streams with Amazon Kinesis Analytics applications, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-logs.html\&quot;&gt;Working with Amazon CloudWatch Logs&lt;/a&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("http://kinesisanalytics.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "KinesisAnalytics_20150814.DeleteApplicationCloudWatchLoggingOption"; // String | 
    DeleteApplicationCloudWatchLoggingOptionRequest deleteApplicationCloudWatchLoggingOptionRequest = new DeleteApplicationCloudWatchLoggingOptionRequest(); // DeleteApplicationCloudWatchLoggingOptionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteApplicationCloudWatchLoggingOption(xAmzTarget, deleteApplicationCloudWatchLoggingOptionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteApplicationCloudWatchLoggingOption");
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
| **xAmzTarget** | **String**|  | [enum: KinesisAnalytics_20150814.DeleteApplicationCloudWatchLoggingOption] |
| **deleteApplicationCloudWatchLoggingOptionRequest** | [**DeleteApplicationCloudWatchLoggingOptionRequest**](DeleteApplicationCloudWatchLoggingOptionRequest.md)|  | |
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
| **481** | ResourceInUseException |  -  |
| **482** | InvalidArgumentException |  -  |
| **483** | ConcurrentModificationException |  -  |
| **484** | UnsupportedOperationException |  -  |

<a id="deleteApplicationInputProcessingConfiguration"></a>
# **deleteApplicationInputProcessingConfiguration**
> Object deleteApplicationInputProcessingConfiguration(xAmzTarget, deleteApplicationInputProcessingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Deletes an &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfiguration.html\&quot;&gt;InputProcessingConfiguration&lt;/a&gt; from an input.&lt;/p&gt;

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
    defaultClient.setBasePath("http://kinesisanalytics.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "KinesisAnalytics_20150814.DeleteApplicationInputProcessingConfiguration"; // String | 
    DeleteApplicationInputProcessingConfigurationRequest deleteApplicationInputProcessingConfigurationRequest = new DeleteApplicationInputProcessingConfigurationRequest(); // DeleteApplicationInputProcessingConfigurationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteApplicationInputProcessingConfiguration(xAmzTarget, deleteApplicationInputProcessingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteApplicationInputProcessingConfiguration");
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
| **xAmzTarget** | **String**|  | [enum: KinesisAnalytics_20150814.DeleteApplicationInputProcessingConfiguration] |
| **deleteApplicationInputProcessingConfigurationRequest** | [**DeleteApplicationInputProcessingConfigurationRequest**](DeleteApplicationInputProcessingConfigurationRequest.md)|  | |
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
| **481** | ResourceInUseException |  -  |
| **482** | InvalidArgumentException |  -  |
| **483** | ConcurrentModificationException |  -  |
| **484** | UnsupportedOperationException |  -  |

<a id="deleteApplicationOutput"></a>
# **deleteApplicationOutput**
> Object deleteApplicationOutput(xAmzTarget, deleteApplicationOutputRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Deletes output destination configuration from your application configuration. Amazon Kinesis Analytics will no longer write data from the corresponding in-application stream to the external output destination.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:DeleteApplicationOutput&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://kinesisanalytics.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "KinesisAnalytics_20150814.DeleteApplicationOutput"; // String | 
    DeleteApplicationOutputRequest deleteApplicationOutputRequest = new DeleteApplicationOutputRequest(); // DeleteApplicationOutputRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteApplicationOutput(xAmzTarget, deleteApplicationOutputRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteApplicationOutput");
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
| **xAmzTarget** | **String**|  | [enum: KinesisAnalytics_20150814.DeleteApplicationOutput] |
| **deleteApplicationOutputRequest** | [**DeleteApplicationOutputRequest**](DeleteApplicationOutputRequest.md)|  | |
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
| **481** | ResourceInUseException |  -  |
| **482** | InvalidArgumentException |  -  |
| **483** | ConcurrentModificationException |  -  |
| **484** | UnsupportedOperationException |  -  |

<a id="deleteApplicationReferenceDataSource"></a>
# **deleteApplicationReferenceDataSource**
> Object deleteApplicationReferenceDataSource(xAmzTarget, deleteApplicationReferenceDataSourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Deletes a reference data source configuration from the specified application configuration.&lt;/p&gt; &lt;p&gt;If the application is running, Amazon Kinesis Analytics immediately removes the in-application table that you created using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationReferenceDataSource.html\&quot;&gt;AddApplicationReferenceDataSource&lt;/a&gt; operation. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;kinesisanalytics.DeleteApplicationReferenceDataSource&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://kinesisanalytics.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "KinesisAnalytics_20150814.DeleteApplicationReferenceDataSource"; // String | 
    DeleteApplicationReferenceDataSourceRequest deleteApplicationReferenceDataSourceRequest = new DeleteApplicationReferenceDataSourceRequest(); // DeleteApplicationReferenceDataSourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteApplicationReferenceDataSource(xAmzTarget, deleteApplicationReferenceDataSourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteApplicationReferenceDataSource");
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
| **xAmzTarget** | **String**|  | [enum: KinesisAnalytics_20150814.DeleteApplicationReferenceDataSource] |
| **deleteApplicationReferenceDataSourceRequest** | [**DeleteApplicationReferenceDataSourceRequest**](DeleteApplicationReferenceDataSourceRequest.md)|  | |
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
| **481** | ResourceInUseException |  -  |
| **482** | InvalidArgumentException |  -  |
| **483** | ConcurrentModificationException |  -  |
| **484** | UnsupportedOperationException |  -  |

<a id="describeApplication"></a>
# **describeApplication**
> DescribeApplicationResponse describeApplication(xAmzTarget, describeApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns information about a specific Amazon Kinesis Analytics application.&lt;/p&gt; &lt;p&gt;If you want to retrieve a list of all applications in your account, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_ListApplications.html\&quot;&gt;ListApplications&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:DescribeApplication&lt;/code&gt; action. You can use &lt;code&gt;DescribeApplication&lt;/code&gt; to get the current application versionId, which you need to call other operations such as &lt;code&gt;Update&lt;/code&gt;. &lt;/p&gt;

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
    defaultClient.setBasePath("http://kinesisanalytics.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "KinesisAnalytics_20150814.DescribeApplication"; // String | 
    DescribeApplicationRequest describeApplicationRequest = new DescribeApplicationRequest(); // DescribeApplicationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeApplicationResponse result = apiInstance.describeApplication(xAmzTarget, describeApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeApplication");
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
| **xAmzTarget** | **String**|  | [enum: KinesisAnalytics_20150814.DescribeApplication] |
| **describeApplicationRequest** | [**DescribeApplicationRequest**](DescribeApplicationRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeApplicationResponse**](DescribeApplicationResponse.md)

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
| **481** | UnsupportedOperationException |  -  |

<a id="discoverInputSchema"></a>
# **discoverInputSchema**
> DiscoverInputSchemaResponse discoverInputSchema(xAmzTarget, discoverInputSchemaRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Infers a schema by evaluating sample records on the specified streaming source (Amazon Kinesis stream or Amazon Kinesis Firehose delivery stream) or S3 object. In the response, the operation returns the inferred schema and also the sample records that the operation used to infer the schema.&lt;/p&gt; &lt;p&gt; You can use the inferred schema when configuring a streaming source for your application. For conceptual information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html\&quot;&gt;Configuring Application Input&lt;/a&gt;. Note that when you create an application using the Amazon Kinesis Analytics console, the console uses this operation to infer a schema and show it in the console user interface. &lt;/p&gt; &lt;p&gt; This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:DiscoverInputSchema&lt;/code&gt; action. &lt;/p&gt;

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
    defaultClient.setBasePath("http://kinesisanalytics.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "KinesisAnalytics_20150814.DiscoverInputSchema"; // String | 
    DiscoverInputSchemaRequest discoverInputSchemaRequest = new DiscoverInputSchemaRequest(); // DiscoverInputSchemaRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DiscoverInputSchemaResponse result = apiInstance.discoverInputSchema(xAmzTarget, discoverInputSchemaRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#discoverInputSchema");
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
| **xAmzTarget** | **String**|  | [enum: KinesisAnalytics_20150814.DiscoverInputSchema] |
| **discoverInputSchemaRequest** | [**DiscoverInputSchemaRequest**](DiscoverInputSchemaRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DiscoverInputSchemaResponse**](DiscoverInputSchemaResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidArgumentException |  -  |
| **481** | UnableToDetectSchemaException |  -  |
| **482** | ResourceProvisionedThroughputExceededException |  -  |
| **483** | ServiceUnavailableException |  -  |

<a id="listApplications"></a>
# **listApplications**
> ListApplicationsResponse listApplications(xAmzTarget, listApplicationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns a list of Amazon Kinesis Analytics applications in your account. For each application, the response includes the application name, Amazon Resource Name (ARN), and status. If the response returns the &lt;code&gt;HasMoreApplications&lt;/code&gt; value as true, you can send another request by adding the &lt;code&gt;ExclusiveStartApplicationName&lt;/code&gt; in the request body, and set the value of this to the last application name from the previous response. &lt;/p&gt; &lt;p&gt;If you want detailed information about a specific application, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html\&quot;&gt;DescribeApplication&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:ListApplications&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://kinesisanalytics.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "KinesisAnalytics_20150814.ListApplications"; // String | 
    ListApplicationsRequest listApplicationsRequest = new ListApplicationsRequest(); // ListApplicationsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListApplicationsResponse result = apiInstance.listApplications(xAmzTarget, listApplicationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listApplications");
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
| **xAmzTarget** | **String**|  | [enum: KinesisAnalytics_20150814.ListApplications] |
| **listApplicationsRequest** | [**ListApplicationsRequest**](ListApplicationsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListApplicationsResponse**](ListApplicationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="listTagsForResource"></a>
# **listTagsForResource**
> ListTagsForResourceResponse listTagsForResource(xAmzTarget, listTagsForResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves the list of key-value tags assigned to the application. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html\&quot;&gt;Using Tagging&lt;/a&gt;.

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
    defaultClient.setBasePath("http://kinesisanalytics.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "KinesisAnalytics_20150814.ListTagsForResource"; // String | 
    ListTagsForResourceRequest listTagsForResourceRequest = new ListTagsForResourceRequest(); // ListTagsForResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListTagsForResourceResponse result = apiInstance.listTagsForResource(xAmzTarget, listTagsForResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
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
| **xAmzTarget** | **String**|  | [enum: KinesisAnalytics_20150814.ListTagsForResource] |
| **listTagsForResourceRequest** | [**ListTagsForResourceRequest**](ListTagsForResourceRequest.md)|  | |
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

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidArgumentException |  -  |
| **482** | ConcurrentModificationException |  -  |

<a id="startApplication"></a>
# **startApplication**
> Object startApplication(xAmzTarget, startApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Starts the specified Amazon Kinesis Analytics application. After creating an application, you must exclusively call this operation to start your application.&lt;/p&gt; &lt;p&gt;After the application starts, it begins consuming the input data, processes it, and writes the output to the configured destination.&lt;/p&gt; &lt;p&gt; The application status must be &lt;code&gt;READY&lt;/code&gt; for you to start an application. You can get the application status in the console or using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html\&quot;&gt;DescribeApplication&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;After you start the application, you can stop the application from processing the input by calling the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_StopApplication.html\&quot;&gt;StopApplication&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:StartApplication&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://kinesisanalytics.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "KinesisAnalytics_20150814.StartApplication"; // String | 
    StartApplicationRequest startApplicationRequest = new StartApplicationRequest(); // StartApplicationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.startApplication(xAmzTarget, startApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startApplication");
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
| **xAmzTarget** | **String**|  | [enum: KinesisAnalytics_20150814.StartApplication] |
| **startApplicationRequest** | [**StartApplicationRequest**](StartApplicationRequest.md)|  | |
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
| **481** | ResourceInUseException |  -  |
| **482** | InvalidArgumentException |  -  |
| **483** | InvalidApplicationConfigurationException |  -  |
| **484** | UnsupportedOperationException |  -  |

<a id="stopApplication"></a>
# **stopApplication**
> Object stopApplication(xAmzTarget, stopApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Stops the application from processing input data. You can stop an application only if it is in the running state. You can use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html\&quot;&gt;DescribeApplication&lt;/a&gt; operation to find the application state. After the application is stopped, Amazon Kinesis Analytics stops reading data from the input, the application stops processing data, and there is no output written to the destination. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:StopApplication&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://kinesisanalytics.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "KinesisAnalytics_20150814.StopApplication"; // String | 
    StopApplicationRequest stopApplicationRequest = new StopApplicationRequest(); // StopApplicationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.stopApplication(xAmzTarget, stopApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#stopApplication");
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
| **xAmzTarget** | **String**|  | [enum: KinesisAnalytics_20150814.StopApplication] |
| **stopApplicationRequest** | [**StopApplicationRequest**](StopApplicationRequest.md)|  | |
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
| **481** | ResourceInUseException |  -  |
| **482** | UnsupportedOperationException |  -  |

<a id="tagResource"></a>
# **tagResource**
> Object tagResource(xAmzTarget, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Adds one or more key-value tags to a Kinesis Analytics application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html\&quot;&gt;Using Tagging&lt;/a&gt;.

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
    defaultClient.setBasePath("http://kinesisanalytics.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "KinesisAnalytics_20150814.TagResource"; // String | 
    TagResourceRequest tagResourceRequest = new TagResourceRequest(); // TagResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.tagResource(xAmzTarget, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
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
| **xAmzTarget** | **String**|  | [enum: KinesisAnalytics_20150814.TagResource] |
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
| **480** | ResourceNotFoundException |  -  |
| **481** | ResourceInUseException |  -  |
| **482** | TooManyTagsException |  -  |
| **483** | InvalidArgumentException |  -  |
| **484** | ConcurrentModificationException |  -  |

<a id="untagResource"></a>
# **untagResource**
> Object untagResource(xAmzTarget, untagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Removes one or more tags from a Kinesis Analytics application. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html\&quot;&gt;Using Tagging&lt;/a&gt;.

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
    defaultClient.setBasePath("http://kinesisanalytics.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "KinesisAnalytics_20150814.UntagResource"; // String | 
    UntagResourceRequest untagResourceRequest = new UntagResourceRequest(); // UntagResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.untagResource(xAmzTarget, untagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
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
| **xAmzTarget** | **String**|  | [enum: KinesisAnalytics_20150814.UntagResource] |
| **untagResourceRequest** | [**UntagResourceRequest**](UntagResourceRequest.md)|  | |
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
| **481** | ResourceInUseException |  -  |
| **482** | TooManyTagsException |  -  |
| **483** | InvalidArgumentException |  -  |
| **484** | ConcurrentModificationException |  -  |

<a id="updateApplication"></a>
# **updateApplication**
> Object updateApplication(xAmzTarget, updateApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Updates an existing Amazon Kinesis Analytics application. Using this API, you can update application code, input configuration, and output configuration. &lt;/p&gt; &lt;p&gt;Note that Amazon Kinesis Analytics updates the &lt;code&gt;CurrentApplicationVersionId&lt;/code&gt; each time you update your application. &lt;/p&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;kinesisanalytics:UpdateApplication&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://kinesisanalytics.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzTarget = "KinesisAnalytics_20150814.UpdateApplication"; // String | 
    UpdateApplicationRequest updateApplicationRequest = new UpdateApplicationRequest(); // UpdateApplicationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.updateApplication(xAmzTarget, updateApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateApplication");
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
| **xAmzTarget** | **String**|  | [enum: KinesisAnalytics_20150814.UpdateApplication] |
| **updateApplicationRequest** | [**UpdateApplicationRequest**](UpdateApplicationRequest.md)|  | |
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
| **480** | CodeValidationException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | ResourceInUseException |  -  |
| **483** | InvalidArgumentException |  -  |
| **484** | ConcurrentModificationException |  -  |
| **485** | UnsupportedOperationException |  -  |

