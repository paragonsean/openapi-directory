# MetaPubApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV2MetapubProgramInformationBatchBatchIdGet**](MetaPubApi.md#apiV2MetapubProgramInformationBatchBatchIdGet) | **GET** /api/v2/metapub/program-information/batch/{batch-id} | Get an EPG batch operation. |
| [**apiV2MetapubProgramInformationBatchPost**](MetaPubApi.md#apiV2MetapubProgramInformationBatchPost) | **POST** /api/v2/metapub/program-information/batch | Create a batch operation on EPG information. |


<a id="apiV2MetapubProgramInformationBatchBatchIdGet"></a>
# **apiV2MetapubProgramInformationBatchBatchIdGet**
> ProgramInformationBatch apiV2MetapubProgramInformationBatchBatchIdGet(batchId)

Get an EPG batch operation.

Gets the batch information which can be used to check the status of the operation or retrieve more details if the batch fails.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaPubApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MetaPubApi apiInstance = new MetaPubApi(defaultClient);
    Long batchId = 56L; // Long | 
    try {
      ProgramInformationBatch result = apiInstance.apiV2MetapubProgramInformationBatchBatchIdGet(batchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaPubApi#apiV2MetapubProgramInformationBatchBatchIdGet");
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
| **batchId** | **Long**|  | |

### Return type

[**ProgramInformationBatch**](ProgramInformationBatch.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The batch information. |  -  |
| **403** | Authorization failed, Username or password not found or incorrect. |  -  |
| **404** | The batch is not found. |  -  |

<a id="apiV2MetapubProgramInformationBatchPost"></a>
# **apiV2MetapubProgramInformationBatchPost**
> ProgramInformationBatch apiV2MetapubProgramInformationBatchPost(apiV2MetapubProgramInformationBatchPostRequest)

Create a batch operation on EPG information.

Create a batch to process the metadata of one or more electronic program guide (EPG) programs using metadata that has been uploaded to the customer&#39;s CD Drive. If multiple EPG programs are present in the metadata, they will all be updated, however updates across programs are not atomic. Note that an EPG program maps to the ContentDepot concept of an episode which is also known as a \&quot;program instance\&quot;.  A batch operation must be explicitly created rather than the server attempting to detect new metadata in order to allow for all the content to be uploaded including any supporting content like images. A batch operation is accepted and queued for asynchronous processing at a later time. A client can poll the batch periodically to determine when it completes and the resulting state. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaPubApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MetaPubApi apiInstance = new MetaPubApi(defaultClient);
    ApiV2MetapubProgramInformationBatchPostRequest apiV2MetapubProgramInformationBatchPostRequest = new ApiV2MetapubProgramInformationBatchPostRequest(); // ApiV2MetapubProgramInformationBatchPostRequest | 
    try {
      ProgramInformationBatch result = apiInstance.apiV2MetapubProgramInformationBatchPost(apiV2MetapubProgramInformationBatchPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaPubApi#apiV2MetapubProgramInformationBatchPost");
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
| **apiV2MetapubProgramInformationBatchPostRequest** | [**ApiV2MetapubProgramInformationBatchPostRequest**](ApiV2MetapubProgramInformationBatchPostRequest.md)|  | [optional] |

### Return type

[**ProgramInformationBatch**](ProgramInformationBatch.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The accepted batch information that is queued for processing. |  -  |

