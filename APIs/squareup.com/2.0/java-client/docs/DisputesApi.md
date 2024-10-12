# DisputesApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**acceptDispute**](DisputesApi.md#acceptDispute) | **POST** /v2/disputes/{dispute_id}/accept | AcceptDispute |
| [**createDisputeEvidenceText**](DisputesApi.md#createDisputeEvidenceText) | **POST** /v2/disputes/{dispute_id}/evidence-text | CreateDisputeEvidenceText |
| [**deleteDisputeEvidence**](DisputesApi.md#deleteDisputeEvidence) | **DELETE** /v2/disputes/{dispute_id}/evidence/{evidence_id} | DeleteDisputeEvidence |
| [**listDisputeEvidence**](DisputesApi.md#listDisputeEvidence) | **GET** /v2/disputes/{dispute_id}/evidence | ListDisputeEvidence |
| [**listDisputes**](DisputesApi.md#listDisputes) | **GET** /v2/disputes | ListDisputes |
| [**retrieveDispute**](DisputesApi.md#retrieveDispute) | **GET** /v2/disputes/{dispute_id} | RetrieveDispute |
| [**retrieveDisputeEvidence**](DisputesApi.md#retrieveDisputeEvidence) | **GET** /v2/disputes/{dispute_id}/evidence/{evidence_id} | RetrieveDisputeEvidence |
| [**submitEvidence**](DisputesApi.md#submitEvidence) | **POST** /v2/disputes/{dispute_id}/submit-evidence | SubmitEvidence |


<a id="acceptDispute"></a>
# **acceptDispute**
> AcceptDisputeResponse acceptDispute(disputeId)

AcceptDispute

Accepts the loss on a dispute. Square returns the disputed amount to the cardholder and updates the dispute state to ACCEPTED.  Square debits the disputed amount from the seller’s Square account. If the Square account does not have sufficient funds, Square debits the associated bank account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisputesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DisputesApi apiInstance = new DisputesApi(defaultClient);
    String disputeId = "disputeId_example"; // String | The ID of the dispute you want to accept.
    try {
      AcceptDisputeResponse result = apiInstance.acceptDispute(disputeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisputesApi#acceptDispute");
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
| **disputeId** | **String**| The ID of the dispute you want to accept. | |

### Return type

[**AcceptDisputeResponse**](AcceptDisputeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="createDisputeEvidenceText"></a>
# **createDisputeEvidenceText**
> CreateDisputeEvidenceTextResponse createDisputeEvidenceText(disputeId, createDisputeEvidenceTextRequest)

CreateDisputeEvidenceText

Uploads text to use as evidence for a dispute challenge.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisputesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DisputesApi apiInstance = new DisputesApi(defaultClient);
    String disputeId = "disputeId_example"; // String | The ID of the dispute you want to upload evidence for.
    CreateDisputeEvidenceTextRequest createDisputeEvidenceTextRequest = new CreateDisputeEvidenceTextRequest(); // CreateDisputeEvidenceTextRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      CreateDisputeEvidenceTextResponse result = apiInstance.createDisputeEvidenceText(disputeId, createDisputeEvidenceTextRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisputesApi#createDisputeEvidenceText");
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
| **disputeId** | **String**| The ID of the dispute you want to upload evidence for. | |
| **createDisputeEvidenceTextRequest** | [**CreateDisputeEvidenceTextRequest**](CreateDisputeEvidenceTextRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**CreateDisputeEvidenceTextResponse**](CreateDisputeEvidenceTextResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="deleteDisputeEvidence"></a>
# **deleteDisputeEvidence**
> DeleteDisputeEvidenceResponse deleteDisputeEvidence(disputeId, evidenceId)

DeleteDisputeEvidence

Removes specified evidence from a dispute.  Square does not send the bank any evidence that is removed. Also, you cannot remove evidence after submitting it to the bank using [SubmitEvidence](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/submit-evidence).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisputesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DisputesApi apiInstance = new DisputesApi(defaultClient);
    String disputeId = "disputeId_example"; // String | The ID of the dispute you want to remove evidence from.
    String evidenceId = "evidenceId_example"; // String | The ID of the evidence you want to remove.
    try {
      DeleteDisputeEvidenceResponse result = apiInstance.deleteDisputeEvidence(disputeId, evidenceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisputesApi#deleteDisputeEvidence");
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
| **disputeId** | **String**| The ID of the dispute you want to remove evidence from. | |
| **evidenceId** | **String**| The ID of the evidence you want to remove. | |

### Return type

[**DeleteDisputeEvidenceResponse**](DeleteDisputeEvidenceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="listDisputeEvidence"></a>
# **listDisputeEvidence**
> ListDisputeEvidenceResponse listDisputeEvidence(disputeId, cursor)

ListDisputeEvidence

Returns a list of evidence associated with a dispute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisputesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DisputesApi apiInstance = new DisputesApi(defaultClient);
    String disputeId = "disputeId_example"; // String | The ID of the dispute.
    String cursor = "cursor_example"; // String | A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query. For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    try {
      ListDisputeEvidenceResponse result = apiInstance.listDisputeEvidence(disputeId, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisputesApi#listDisputeEvidence");
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
| **disputeId** | **String**| The ID of the dispute. | |
| **cursor** | **String**| A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query. For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). | [optional] |

### Return type

[**ListDisputeEvidenceResponse**](ListDisputeEvidenceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="listDisputes"></a>
# **listDisputes**
> ListDisputesResponse listDisputes(cursor, states, locationId)

ListDisputes

Returns a list of disputes associated with a particular account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisputesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DisputesApi apiInstance = new DisputesApi(defaultClient);
    String cursor = "cursor_example"; // String | A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query. For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    String states = "states_example"; // String | The dispute states to filter the result. If not specified, the endpoint returns all open disputes (the dispute status is not `INQUIRY_CLOSED`, `WON`, or `LOST`).
    String locationId = "locationId_example"; // String | The ID of the location for which to return a list of disputes. If not specified, the endpoint returns all open disputes (the dispute status is not `INQUIRY_CLOSED`, `WON`, or `LOST`) associated with all locations.
    try {
      ListDisputesResponse result = apiInstance.listDisputes(cursor, states, locationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisputesApi#listDisputes");
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
| **cursor** | **String**| A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query. For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). | [optional] |
| **states** | **String**| The dispute states to filter the result. If not specified, the endpoint returns all open disputes (the dispute status is not &#x60;INQUIRY_CLOSED&#x60;, &#x60;WON&#x60;, or &#x60;LOST&#x60;). | [optional] |
| **locationId** | **String**| The ID of the location for which to return a list of disputes. If not specified, the endpoint returns all open disputes (the dispute status is not &#x60;INQUIRY_CLOSED&#x60;, &#x60;WON&#x60;, or &#x60;LOST&#x60;) associated with all locations. | [optional] |

### Return type

[**ListDisputesResponse**](ListDisputesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveDispute"></a>
# **retrieveDispute**
> RetrieveDisputeResponse retrieveDispute(disputeId)

RetrieveDispute

Returns details about a specific dispute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisputesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DisputesApi apiInstance = new DisputesApi(defaultClient);
    String disputeId = "disputeId_example"; // String | The ID of the dispute you want more details about.
    try {
      RetrieveDisputeResponse result = apiInstance.retrieveDispute(disputeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisputesApi#retrieveDispute");
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
| **disputeId** | **String**| The ID of the dispute you want more details about. | |

### Return type

[**RetrieveDisputeResponse**](RetrieveDisputeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveDisputeEvidence"></a>
# **retrieveDisputeEvidence**
> RetrieveDisputeEvidenceResponse retrieveDisputeEvidence(disputeId, evidenceId)

RetrieveDisputeEvidence

Returns the evidence metadata specified by the evidence ID in the request URL path  You must maintain a copy of the evidence you upload if you want to reference it later. You cannot download the evidence after you upload it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisputesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DisputesApi apiInstance = new DisputesApi(defaultClient);
    String disputeId = "disputeId_example"; // String | The ID of the dispute that you want to retrieve evidence from.
    String evidenceId = "evidenceId_example"; // String | The ID of the evidence to retrieve.
    try {
      RetrieveDisputeEvidenceResponse result = apiInstance.retrieveDisputeEvidence(disputeId, evidenceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisputesApi#retrieveDisputeEvidence");
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
| **disputeId** | **String**| The ID of the dispute that you want to retrieve evidence from. | |
| **evidenceId** | **String**| The ID of the evidence to retrieve. | |

### Return type

[**RetrieveDisputeEvidenceResponse**](RetrieveDisputeEvidenceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="submitEvidence"></a>
# **submitEvidence**
> SubmitEvidenceResponse submitEvidence(disputeId)

SubmitEvidence

Submits evidence to the cardholder&#39;s bank.  Before submitting evidence, Square compiles all available evidence. This includes evidence uploaded using the [CreateDisputeEvidenceFile](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/create-dispute-evidence-file) and [CreateDisputeEvidenceText](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/create-dispute-evidence-text) endpoints and evidence automatically provided by Square, when available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisputesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DisputesApi apiInstance = new DisputesApi(defaultClient);
    String disputeId = "disputeId_example"; // String | The ID of the dispute that you want to submit evidence for.
    try {
      SubmitEvidenceResponse result = apiInstance.submitEvidence(disputeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisputesApi#submitEvidence");
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
| **disputeId** | **String**| The ID of the dispute that you want to submit evidence for. | |

### Return type

[**SubmitEvidenceResponse**](SubmitEvidenceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

