# DefaultApi

All URIs are relative to *http://featurestore-runtime.sagemaker.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**batchGetRecord**](DefaultApi.md#batchGetRecord) | **POST** /BatchGetRecord |  |
| [**deleteRecord**](DefaultApi.md#deleteRecord) | **DELETE** /FeatureGroup/{FeatureGroupName}#RecordIdentifierValueAsString&amp;EventTime |  |
| [**getRecord**](DefaultApi.md#getRecord) | **GET** /FeatureGroup/{FeatureGroupName}#RecordIdentifierValueAsString |  |
| [**putRecord**](DefaultApi.md#putRecord) | **PUT** /FeatureGroup/{FeatureGroupName} |  |


<a id="batchGetRecord"></a>
# **batchGetRecord**
> BatchGetRecordResponse batchGetRecord(batchGetRecordRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves a batch of &lt;code&gt;Records&lt;/code&gt; from a &lt;code&gt;FeatureGroup&lt;/code&gt;.

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
    defaultClient.setBasePath("http://featurestore-runtime.sagemaker.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    BatchGetRecordRequest batchGetRecordRequest = new BatchGetRecordRequest(); // BatchGetRecordRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      BatchGetRecordResponse result = apiInstance.batchGetRecord(batchGetRecordRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchGetRecord");
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
| **batchGetRecordRequest** | [**BatchGetRecordRequest**](BatchGetRecordRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**BatchGetRecordResponse**](BatchGetRecordResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ValidationError |  -  |
| **481** | InternalFailure |  -  |
| **482** | ServiceUnavailable |  -  |
| **483** | AccessForbidden |  -  |

<a id="deleteRecord"></a>
# **deleteRecord**
> deleteRecord(featureGroupName, recordIdentifierValueAsString, eventTime, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, targetStores, deletionMode)



&lt;p&gt;Deletes a &lt;code&gt;Record&lt;/code&gt; from a &lt;code&gt;FeatureGroup&lt;/code&gt; in the &lt;code&gt;OnlineStore&lt;/code&gt;. Feature Store supports both &lt;code&gt;SoftDelete&lt;/code&gt; and &lt;code&gt;HardDelete&lt;/code&gt;. For &lt;code&gt;SoftDelete&lt;/code&gt; (default), feature columns are set to &lt;code&gt;null&lt;/code&gt; and the record is no longer retrievable by &lt;code&gt;GetRecord&lt;/code&gt; or &lt;code&gt;BatchGetRecord&lt;/code&gt;. For &lt;code&gt;HardDelete&lt;/code&gt;, the complete &lt;code&gt;Record&lt;/code&gt; is removed from the &lt;code&gt;OnlineStore&lt;/code&gt;. In both cases, Feature Store appends the deleted record marker to the &lt;code&gt;OfflineStore&lt;/code&gt; with feature values set to &lt;code&gt;null&lt;/code&gt;, &lt;code&gt;is_deleted&lt;/code&gt; value set to &lt;code&gt;True&lt;/code&gt;, and &lt;code&gt;EventTime&lt;/code&gt; set to the delete input &lt;code&gt;EventTime&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Note that the &lt;code&gt;EventTime&lt;/code&gt; specified in &lt;code&gt;DeleteRecord&lt;/code&gt; should be set later than the &lt;code&gt;EventTime&lt;/code&gt; of the existing record in the &lt;code&gt;OnlineStore&lt;/code&gt; for that &lt;code&gt;RecordIdentifer&lt;/code&gt;. If it is not, the deletion does not occur:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For &lt;code&gt;SoftDelete&lt;/code&gt;, the existing (undeleted) record remains in the &lt;code&gt;OnlineStore&lt;/code&gt;, though the delete record marker is still written to the &lt;code&gt;OfflineStore&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HardDelete&lt;/code&gt; returns &lt;code&gt;EventTime&lt;/code&gt;: &lt;code&gt;400 ValidationException&lt;/code&gt; to indicate that the delete operation failed. No delete record marker is written to the &lt;code&gt;OfflineStore&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    defaultClient.setBasePath("http://featurestore-runtime.sagemaker.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String featureGroupName = "featureGroupName_example"; // String | The name or Amazon Resource Name (ARN) of the feature group to delete the record from. 
    String recordIdentifierValueAsString = "recordIdentifierValueAsString_example"; // String | The value for the <code>RecordIdentifier</code> that uniquely identifies the record, in string format. 
    String eventTime = "eventTime_example"; // String | Timestamp indicating when the deletion event occurred. <code>EventTime</code> can be used to query data at a certain point in time.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    List<TargetStore> targetStores = Arrays.asList(); // List<TargetStore> | A list of stores from which you're deleting the record. By default, Feature Store deletes the record from all of the stores that you're using for the <code>FeatureGroup</code>.
    String deletionMode = "SoftDelete"; // String | The name of the deletion mode for deleting the record. By default, the deletion mode is set to <code>SoftDelete</code>.
    try {
      apiInstance.deleteRecord(featureGroupName, recordIdentifierValueAsString, eventTime, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, targetStores, deletionMode);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteRecord");
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
| **featureGroupName** | **String**| The name or Amazon Resource Name (ARN) of the feature group to delete the record from.  | |
| **recordIdentifierValueAsString** | **String**| The value for the &lt;code&gt;RecordIdentifier&lt;/code&gt; that uniquely identifies the record, in string format.  | |
| **eventTime** | **String**| Timestamp indicating when the deletion event occurred. &lt;code&gt;EventTime&lt;/code&gt; can be used to query data at a certain point in time. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **targetStores** | [**List&lt;TargetStore&gt;**](TargetStore.md)| A list of stores from which you&#39;re deleting the record. By default, Feature Store deletes the record from all of the stores that you&#39;re using for the &lt;code&gt;FeatureGroup&lt;/code&gt;. | [optional] |
| **deletionMode** | **String**| The name of the deletion mode for deleting the record. By default, the deletion mode is set to &lt;code&gt;SoftDelete&lt;/code&gt;. | [optional] [enum: SoftDelete, HardDelete] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ValidationError |  -  |
| **481** | InternalFailure |  -  |
| **482** | ServiceUnavailable |  -  |
| **483** | AccessForbidden |  -  |

<a id="getRecord"></a>
# **getRecord**
> GetRecordResponse getRecord(featureGroupName, recordIdentifierValueAsString, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, featureName, expirationTimeResponse)



Use for &lt;code&gt;OnlineStore&lt;/code&gt; serving from a &lt;code&gt;FeatureStore&lt;/code&gt;. Only the latest records stored in the &lt;code&gt;OnlineStore&lt;/code&gt; can be retrieved. If no Record with &lt;code&gt;RecordIdentifierValue&lt;/code&gt; is found, then an empty result is returned. 

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
    defaultClient.setBasePath("http://featurestore-runtime.sagemaker.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String featureGroupName = "featureGroupName_example"; // String | The name or Amazon Resource Name (ARN) of the feature group from which you want to retrieve a record.
    String recordIdentifierValueAsString = "recordIdentifierValueAsString_example"; // String | The value that corresponds to <code>RecordIdentifier</code> type and uniquely identifies the record in the <code>FeatureGroup</code>. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    List<String> featureName = Arrays.asList(); // List<String> | List of names of Features to be retrieved. If not specified, the latest value for all the Features are returned.
    String expirationTimeResponse = "Enabled"; // String | Parameter to request <code>ExpiresAt</code> in response. If <code>Enabled</code>, <code>GetRecord</code> will return the value of <code>ExpiresAt</code>, if it is not null. If <code>Disabled</code> and null, <code>GetRecord</code> will return null.
    try {
      GetRecordResponse result = apiInstance.getRecord(featureGroupName, recordIdentifierValueAsString, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, featureName, expirationTimeResponse);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRecord");
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
| **featureGroupName** | **String**| The name or Amazon Resource Name (ARN) of the feature group from which you want to retrieve a record. | |
| **recordIdentifierValueAsString** | **String**| The value that corresponds to &lt;code&gt;RecordIdentifier&lt;/code&gt; type and uniquely identifies the record in the &lt;code&gt;FeatureGroup&lt;/code&gt;.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **featureName** | [**List&lt;String&gt;**](String.md)| List of names of Features to be retrieved. If not specified, the latest value for all the Features are returned. | [optional] |
| **expirationTimeResponse** | **String**| Parameter to request &lt;code&gt;ExpiresAt&lt;/code&gt; in response. If &lt;code&gt;Enabled&lt;/code&gt;, &lt;code&gt;GetRecord&lt;/code&gt; will return the value of &lt;code&gt;ExpiresAt&lt;/code&gt;, if it is not null. If &lt;code&gt;Disabled&lt;/code&gt; and null, &lt;code&gt;GetRecord&lt;/code&gt; will return null. | [optional] [enum: Enabled, Disabled] |

### Return type

[**GetRecordResponse**](GetRecordResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ValidationError |  -  |
| **481** | ResourceNotFound |  -  |
| **482** | InternalFailure |  -  |
| **483** | ServiceUnavailable |  -  |
| **484** | AccessForbidden |  -  |

<a id="putRecord"></a>
# **putRecord**
> putRecord(featureGroupName, putRecordRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;The &lt;code&gt;PutRecord&lt;/code&gt; API is used to ingest a list of &lt;code&gt;Records&lt;/code&gt; into your feature group. &lt;/p&gt; &lt;p&gt;If a new record’s &lt;code&gt;EventTime&lt;/code&gt; is greater, the new record is written to both the &lt;code&gt;OnlineStore&lt;/code&gt; and &lt;code&gt;OfflineStore&lt;/code&gt;. Otherwise, the record is a historic record and it is written only to the &lt;code&gt;OfflineStore&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;You can specify the ingestion to be applied to the &lt;code&gt;OnlineStore&lt;/code&gt;, &lt;code&gt;OfflineStore&lt;/code&gt;, or both by using the &lt;code&gt;TargetStores&lt;/code&gt; request parameter. &lt;/p&gt; &lt;p&gt;You can set the ingested record to expire at a given time to live (TTL) duration after the record’s event time, &lt;code&gt;ExpiresAt&lt;/code&gt; &#x3D; &lt;code&gt;EventTime&lt;/code&gt; + &lt;code&gt;TtlDuration&lt;/code&gt;, by specifying the &lt;code&gt;TtlDuration&lt;/code&gt; parameter. A record level &lt;code&gt;TtlDuration&lt;/code&gt; is set when specifying the &lt;code&gt;TtlDuration&lt;/code&gt; parameter using the &lt;code&gt;PutRecord&lt;/code&gt; API call. If the input &lt;code&gt;TtlDuration&lt;/code&gt; is &lt;code&gt;null&lt;/code&gt; or unspecified, &lt;code&gt;TtlDuration&lt;/code&gt; is set to the default feature group level &lt;code&gt;TtlDuration&lt;/code&gt;. A record level &lt;code&gt;TtlDuration&lt;/code&gt; supersedes the group level &lt;code&gt;TtlDuration&lt;/code&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("http://featurestore-runtime.sagemaker.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String featureGroupName = "featureGroupName_example"; // String | The name or Amazon Resource Name (ARN) of the feature group that you want to insert the record into.
    PutRecordRequest putRecordRequest = new PutRecordRequest(); // PutRecordRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.putRecord(featureGroupName, putRecordRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putRecord");
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
| **featureGroupName** | **String**| The name or Amazon Resource Name (ARN) of the feature group that you want to insert the record into. | |
| **putRecordRequest** | [**PutRecordRequest**](PutRecordRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ValidationError |  -  |
| **481** | InternalFailure |  -  |
| **482** | ServiceUnavailable |  -  |
| **483** | AccessForbidden |  -  |

