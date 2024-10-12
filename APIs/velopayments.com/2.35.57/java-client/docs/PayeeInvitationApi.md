# PayeeInvitationApi

All URIs are relative to *https://api.sandbox.velopayments.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPayeeV3**](PayeeInvitationApi.md#createPayeeV3) | **POST** /v3/payees | Initiate Payee Creation |
| [**getPayeesInvitationStatusV3**](PayeeInvitationApi.md#getPayeesInvitationStatusV3) | **GET** /v3/payees/payors/{payorId}/invitationStatus | Get Payee Invitation Status |
| [**getPayeesInvitationStatusV4**](PayeeInvitationApi.md#getPayeesInvitationStatusV4) | **GET** /v4/payees/payors/{payorId}/invitationStatus | Get Payee Invitation Status |
| [**queryBatchStatusV3**](PayeeInvitationApi.md#queryBatchStatusV3) | **GET** /v3/payees/batch/{batchId} | Query Batch Status |
| [**queryBatchStatusV4**](PayeeInvitationApi.md#queryBatchStatusV4) | **GET** /v4/payees/batch/{batchId} | Query Batch Status |
| [**resendPayeeInviteV3**](PayeeInvitationApi.md#resendPayeeInviteV3) | **POST** /v3/payees/{payeeId}/invite | Resend Payee Invite |
| [**resendPayeeInviteV4**](PayeeInvitationApi.md#resendPayeeInviteV4) | **POST** /v4/payees/{payeeId}/invite | Resend Payee Invite |
| [**v4CreatePayee**](PayeeInvitationApi.md#v4CreatePayee) | **POST** /v4/payees | Initiate Payee Creation |


<a id="createPayeeV3"></a>
# **createPayeeV3**
> CreatePayeesCSVResponseV3 createPayeeV3(createPayeesRequestV3)

Initiate Payee Creation

&lt;p&gt;Use v4 instead&lt;/p&gt; Initiate the process of creating 1 to 2000 payees in a batch Use the response location header to query for status (201 - Created, 400 - invalid request body. In addition to standard semantic validations, a 400 will also result if there is a duplicate remote id within the batch / if there is a duplicate email within the batch, i.e. if there is a conflict between the data provided for one payee within the batch and that provided for another payee within the same batch). The validation at this stage is intra-batch only. Validation against payees who have already been invited occurs subsequently during processing of the batch. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayeeInvitationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayeeInvitationApi apiInstance = new PayeeInvitationApi(defaultClient);
    CreatePayeesRequestV3 createPayeesRequestV3 = new CreatePayeesRequestV3(); // CreatePayeesRequestV3 | Post payees to create.
    try {
      CreatePayeesCSVResponseV3 result = apiInstance.createPayeeV3(createPayeesRequestV3);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayeeInvitationApi#createPayeeV3");
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
| **createPayeesRequestV3** | [**CreatePayeesRequestV3**](CreatePayeesRequestV3.md)| Post payees to create. | [optional] |

### Return type

[**CreatePayeesCSVResponseV3**](CreatePayeesCSVResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | HTTP Created. Body created only on CSV requests |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="getPayeesInvitationStatusV3"></a>
# **getPayeesInvitationStatusV3**
> PagedPayeeInvitationStatusResponseV3 getPayeesInvitationStatusV3(payorId, payeeId, invitationStatus, page, pageSize)

Get Payee Invitation Status

&lt;p&gt;Use v4 instead&lt;/p&gt; &lt;p&gt;Returns a filtered, paginated list of payees associated with a payor, along with invitation status and grace period end date.&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayeeInvitationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayeeInvitationApi apiInstance = new PayeeInvitationApi(defaultClient);
    UUID payorId = UUID.fromString("9ac75325-5dcd-42d5-b992-175d7e0a035e"); // UUID | The account owner Payor ID
    UUID payeeId = UUID.fromString("2aa5d7e0-2ecb-403f-8494-1865ed0454e9"); // UUID | The UUID of the payee.
    String invitationStatus = "invitationStatus_example"; // String | The invitation status of the payees.
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 25; // Integer | Page size. Default is 25. Max allowable is 100.
    try {
      PagedPayeeInvitationStatusResponseV3 result = apiInstance.getPayeesInvitationStatusV3(payorId, payeeId, invitationStatus, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayeeInvitationApi#getPayeesInvitationStatusV3");
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
| **payorId** | **UUID**| The account owner Payor ID | |
| **payeeId** | **UUID**| The UUID of the payee. | [optional] |
| **invitationStatus** | **String**| The invitation status of the payees. | [optional] |
| **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| Page size. Default is 25. Max allowable is 100. | [optional] [default to 25] |

### Return type

[**PagedPayeeInvitationStatusResponseV3**](PagedPayeeInvitationStatusResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Payees with Invitaion status - filters of payeeId and invitationStatus |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="getPayeesInvitationStatusV4"></a>
# **getPayeesInvitationStatusV4**
> PagedPayeeInvitationStatusResponseV4 getPayeesInvitationStatusV4(payorId, payeeId, invitationStatus, page, pageSize)

Get Payee Invitation Status

Returns a filtered, paginated list of payees associated with a payor, along with invitation status and grace period end date. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayeeInvitationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayeeInvitationApi apiInstance = new PayeeInvitationApi(defaultClient);
    UUID payorId = UUID.fromString("9ac75325-5dcd-42d5-b992-175d7e0a035e"); // UUID | The account owner Payor ID
    UUID payeeId = UUID.fromString("2aa5d7e0-2ecb-403f-8494-1865ed0454e9"); // UUID | The UUID of the payee.
    String invitationStatus = "invitationStatus_example"; // String | The invitation status of the payees.
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 25; // Integer | Page size. Default is 25. Max allowable is 100.
    try {
      PagedPayeeInvitationStatusResponseV4 result = apiInstance.getPayeesInvitationStatusV4(payorId, payeeId, invitationStatus, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayeeInvitationApi#getPayeesInvitationStatusV4");
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
| **payorId** | **UUID**| The account owner Payor ID | |
| **payeeId** | **UUID**| The UUID of the payee. | [optional] |
| **invitationStatus** | **String**| The invitation status of the payees. | [optional] |
| **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| Page size. Default is 25. Max allowable is 100. | [optional] [default to 25] |

### Return type

[**PagedPayeeInvitationStatusResponseV4**](PagedPayeeInvitationStatusResponseV4.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Payees with Invitaion status - filters of payeeId and invitationStatus |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="queryBatchStatusV3"></a>
# **queryBatchStatusV3**
> QueryBatchResponseV3 queryBatchStatusV3(batchId)

Query Batch Status

&lt;p&gt;Use v4 instead&lt;/p&gt; Fetch the status of a specific batch of payees. The batch is fully processed when status is ACCEPTED and pendingCount is 0 ( 200 - OK, 404 - batch not found ). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayeeInvitationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayeeInvitationApi apiInstance = new PayeeInvitationApi(defaultClient);
    UUID batchId = UUID.randomUUID(); // UUID | Batch Id
    try {
      QueryBatchResponseV3 result = apiInstance.queryBatchStatusV3(batchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayeeInvitationApi#queryBatchStatusV3");
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
| **batchId** | **UUID**| Batch Id | |

### Return type

[**QueryBatchResponseV3**](QueryBatchResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Batch Status |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="queryBatchStatusV4"></a>
# **queryBatchStatusV4**
> QueryBatchResponseV4 queryBatchStatusV4(batchId)

Query Batch Status

Fetch the status of a specific batch of payees. The batch is fully processed when status is ACCEPTED and pendingCount is 0 ( 200 - OK, 404 - batch not found ). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayeeInvitationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayeeInvitationApi apiInstance = new PayeeInvitationApi(defaultClient);
    UUID batchId = UUID.randomUUID(); // UUID | Batch Id
    try {
      QueryBatchResponseV4 result = apiInstance.queryBatchStatusV4(batchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayeeInvitationApi#queryBatchStatusV4");
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
| **batchId** | **UUID**| Batch Id | |

### Return type

[**QueryBatchResponseV4**](QueryBatchResponseV4.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Batch Status |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="resendPayeeInviteV3"></a>
# **resendPayeeInviteV3**
> resendPayeeInviteV3(payeeId, invitePayeeRequestV3)

Resend Payee Invite

&lt;p&gt;Use v4 instead&lt;/p&gt; &lt;p&gt;Resend an invite to the Payee The payee must have already been invited by the payor and not yet accepted or declined&lt;/p&gt; &lt;p&gt;Any previous invites to the payee by this Payor will be invalidated&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayeeInvitationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayeeInvitationApi apiInstance = new PayeeInvitationApi(defaultClient);
    UUID payeeId = UUID.fromString("2aa5d7e0-2ecb-403f-8494-1865ed0454e9"); // UUID | The UUID of the payee.
    InvitePayeeRequestV3 invitePayeeRequestV3 = new InvitePayeeRequestV3(); // InvitePayeeRequestV3 | Provide Payor Id in body of request
    try {
      apiInstance.resendPayeeInviteV3(payeeId, invitePayeeRequestV3);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayeeInvitationApi#resendPayeeInviteV3");
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
| **payeeId** | **UUID**| The UUID of the payee. | |
| **invitePayeeRequestV3** | [**InvitePayeeRequestV3**](InvitePayeeRequestV3.md)| Provide Payor Id in body of request | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the request was accepted |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |
| **409** | The request contained data that would result in a duplicate value  |  -  |

<a id="resendPayeeInviteV4"></a>
# **resendPayeeInviteV4**
> resendPayeeInviteV4(payeeId, invitePayeeRequestV4)

Resend Payee Invite

&lt;p&gt;Resend an invite to the Payee The payee must have already been invited by the payor and not yet accepted or declined&lt;/p&gt; &lt;p&gt;Any previous invites to the payee by this Payor will be invalidated&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayeeInvitationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayeeInvitationApi apiInstance = new PayeeInvitationApi(defaultClient);
    UUID payeeId = UUID.fromString("2aa5d7e0-2ecb-403f-8494-1865ed0454e9"); // UUID | The UUID of the payee.
    InvitePayeeRequestV4 invitePayeeRequestV4 = new InvitePayeeRequestV4(); // InvitePayeeRequestV4 | Provide Payor Id in body of request
    try {
      apiInstance.resendPayeeInviteV4(payeeId, invitePayeeRequestV4);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayeeInvitationApi#resendPayeeInviteV4");
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
| **payeeId** | **UUID**| The UUID of the payee. | |
| **invitePayeeRequestV4** | [**InvitePayeeRequestV4**](InvitePayeeRequestV4.md)| Provide Payor Id in body of request | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the request was accepted |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |
| **409** | The request contained data that would result in a duplicate value  |  -  |

<a id="v4CreatePayee"></a>
# **v4CreatePayee**
> CreatePayeesCSVResponseV4 v4CreatePayee(createPayeesRequestV4)

Initiate Payee Creation

&lt;p&gt;Initiate the process of creating 1 to 2000 payees in a batch&lt;/p&gt; &lt;p&gt;Use the batchId in the response to query for status.&lt;/p&gt; &lt;p&gt;In addition to standard semantic validations, a 400 will also result if: &lt;/p&gt; &lt;ul&gt; &lt;li&gt;there is a duplicate remote id within the batch&lt;/li&gt; &lt;li&gt;there is a duplicate email within the batch, i.e. if there is a conflict between the data provided for one payee within the batch and that provided for another payee within the same batch).&lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The validation at this stage is intra-batch only.&lt;/p&gt; &lt;p&gt;Validation against payees who have already been invited occurs subsequently during processing of the batch.&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayeeInvitationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayeeInvitationApi apiInstance = new PayeeInvitationApi(defaultClient);
    CreatePayeesRequestV4 createPayeesRequestV4 = new CreatePayeesRequestV4(); // CreatePayeesRequestV4 | Post payees to create.
    try {
      CreatePayeesCSVResponseV4 result = apiInstance.v4CreatePayee(createPayeesRequestV4);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayeeInvitationApi#v4CreatePayee");
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
| **createPayeesRequestV4** | [**CreatePayeesRequestV4**](CreatePayeesRequestV4.md)| Post payees to create. | [optional] |

### Return type

[**CreatePayeesCSVResponseV4**](CreatePayeesCSVResponseV4.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | HTTP Created. Body created only on CSV requests |  * Location -  <br>  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

