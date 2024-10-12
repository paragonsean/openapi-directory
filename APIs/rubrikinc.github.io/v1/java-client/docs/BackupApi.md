# BackupApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createBackupRemediationAsyncTask**](BackupApi.md#createBackupRemediationAsyncTask) | **POST** /backup/retry | Reschedule unsuccessful backup tasks |
| [**getBackupRemediationAsyncTaskStatus**](BackupApi.md#getBackupRemediationAsyncTaskStatus) | **GET** /backup/retry/{id} | Get status of reschedule attempt |
| [**getBackupVerificationAsyncRequestStatus**](BackupApi.md#getBackupVerificationAsyncRequestStatus) | **GET** /backup/verify/{id} | Get asynchronous request details for Backup Verification |
| [**verifySnapshot**](BackupApi.md#verifySnapshot) | **POST** /backup/verify | Trigger a job for snapshot verification |


<a id="createBackupRemediationAsyncTask"></a>
# **createBackupRemediationAsyncTask**
> RemediationResponse createBackupRemediationAsyncTask(remediationRequest)

Reschedule unsuccessful backup tasks

Create an asynchronous task for rescheduling unsuccessful backup tasks. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    BackupApi apiInstance = new BackupApi(defaultClient);
    RemediationRequest remediationRequest = new RemediationRequest(); // RemediationRequest | Parameters required to reschedule unsuccessful backup tasks. 
    try {
      RemediationResponse result = apiInstance.createBackupRemediationAsyncTask(remediationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupApi#createBackupRemediationAsyncTask");
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
| **remediationRequest** | [**RemediationRequest**](RemediationRequest.md)| Parameters required to reschedule unsuccessful backup tasks.  | |

### Return type

[**RemediationResponse**](RemediationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status details of the async request. |  -  |
| **422** | The re-scheduling API failed. |  -  |

<a id="getBackupRemediationAsyncTaskStatus"></a>
# **getBackupRemediationAsyncTaskStatus**
> AsyncRequestStatus getBackupRemediationAsyncTaskStatus(id)

Get status of reschedule attempt

Retrieve the details of a specified asynchronous task to use for rescheduling unsuccessful tasks. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    BackupApi apiInstance = new BackupApi(defaultClient);
    String id = "id_example"; // String | Async request id.
    try {
      AsyncRequestStatus result = apiInstance.getBackupRemediationAsyncTaskStatus(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupApi#getBackupRemediationAsyncTaskStatus");
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
| **id** | **String**| Async request id. | |

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status details of async request. |  -  |
| **422** | The status API failed. |  -  |

<a id="getBackupVerificationAsyncRequestStatus"></a>
# **getBackupVerificationAsyncRequestStatus**
> VerificationResponse getBackupVerificationAsyncRequestStatus(id)

Get asynchronous request details for Backup Verification

Get the details of an asynchronous request for a backup verification job. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    BackupApi apiInstance = new BackupApi(defaultClient);
    String id = "id_example"; // String | ID of the asynchronous request.
    try {
      VerificationResponse result = apiInstance.getBackupVerificationAsyncRequestStatus(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupApi#getBackupVerificationAsyncRequestStatus");
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
| **id** | **String**| ID of the asynchronous request. | |

### Return type

[**VerificationResponse**](VerificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status of the asynchronous request. |  -  |
| **422** | The status retrieval API failed. |  -  |

<a id="verifySnapshot"></a>
# **verifySnapshot**
> VerificationResponse verifySnapshot(verificationParameters)

Trigger a job for snapshot verification

This REST API triggers the job \&quot;BACKUP_INTEGRITY_VERIFICATION\&quot;, which verifies whether or not the specified snapshot is restorable. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    BackupApi apiInstance = new BackupApi(defaultClient);
    VerificationParameters verificationParameters = new VerificationParameters(); // VerificationParameters | Parameters needed to schedule a snapshot verification job. 
    try {
      VerificationResponse result = apiInstance.verifySnapshot(verificationParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupApi#verifySnapshot");
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
| **verificationParameters** | [**VerificationParameters**](VerificationParameters.md)| Parameters needed to schedule a snapshot verification job.  | |

### Return type

[**VerificationResponse**](VerificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sucessfully scheduled the job to verify the snapshot. |  -  |
| **422** | The verification API failed. |  -  |

