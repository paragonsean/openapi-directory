# TransactionsApi

All URIs are relative to *http://slicebox.local/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**transactionsTokenImagePost**](TransactionsApi.md#transactionsTokenImagePost) | **POST** /transactions/{token}/image |  |
| [**transactionsTokenOutgoingDonePost**](TransactionsApi.md#transactionsTokenOutgoingDonePost) | **POST** /transactions/{token}/outgoing/done |  |
| [**transactionsTokenOutgoingFailedPost**](TransactionsApi.md#transactionsTokenOutgoingFailedPost) | **POST** /transactions/{token}/outgoing/failed |  |
| [**transactionsTokenOutgoingGet**](TransactionsApi.md#transactionsTokenOutgoingGet) | **GET** /transactions/{token}/outgoing |  |
| [**transactionsTokenOutgoingPollGet**](TransactionsApi.md#transactionsTokenOutgoingPollGet) | **GET** /transactions/{token}/outgoing/poll |  |
| [**transactionsTokenStatusGet**](TransactionsApi.md#transactionsTokenStatusGet) | **GET** /transactions/{token}/status |  |
| [**transactionsTokenStatusPut**](TransactionsApi.md#transactionsTokenStatusPut) | **PUT** /transactions/{token}/status |  |


<a id="transactionsTokenImagePost"></a>
# **transactionsTokenImagePost**
> transactionsTokenImagePost(token, transactionid, sequencenumber, totalimagecount, dataset)



add an image (dataset) as part of a transaction. This method is used when sending images using the push method to a public slicebox.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String token = "token_example"; // String | authentication token identifying the current box-to-box connection
    Long transactionid = 56L; // Long | the ID of the client's outgoing transaction
    Long sequencenumber = 56L; // Long | the index of this image in the transaction
    Long totalimagecount = 56L; // Long | the total number of images in this transaction
    Object dataset = null; // Object | the dataset byte array
    try {
      apiInstance.transactionsTokenImagePost(token, transactionid, sequencenumber, totalimagecount, dataset);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#transactionsTokenImagePost");
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
| **token** | **String**| authentication token identifying the current box-to-box connection | |
| **transactionid** | **Long**| the ID of the client&#39;s outgoing transaction | |
| **sequencenumber** | **Long**| the index of this image in the transaction | |
| **totalimagecount** | **Long**| the total number of images in this transaction | |
| **dataset** | **Object**| the dataset byte array | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | image data received |  -  |
| **401** | unauthorized, invalid token |  -  |

<a id="transactionsTokenOutgoingDonePost"></a>
# **transactionsTokenOutgoingDonePost**
> transactionsTokenOutgoingDonePost(token, outgoingEntryAndImageInformationBlock)



signal that the supplied outgoing transaction and image was successfully received and can be marked as sent. This method is used when sending images using the poll method from a public slicebox.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String token = "token_example"; // String | authentication token identifying the current box-to-box connection
    OutgoingTransactionImage outgoingEntryAndImageInformationBlock = new OutgoingTransactionImage(); // OutgoingTransactionImage | outgoing transaction and image that has been successfully received
    try {
      apiInstance.transactionsTokenOutgoingDonePost(token, outgoingEntryAndImageInformationBlock);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#transactionsTokenOutgoingDonePost");
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
| **token** | **String**| authentication token identifying the current box-to-box connection | |
| **outgoingEntryAndImageInformationBlock** | [**OutgoingTransactionImage**](OutgoingTransactionImage.md)| outgoing transaction and image that has been successfully received | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | done message received |  -  |
| **401** | unauthorized, invalid token |  -  |

<a id="transactionsTokenOutgoingFailedPost"></a>
# **transactionsTokenOutgoingFailedPost**
> transactionsTokenOutgoingFailedPost(token, outgoingTransactionAndImageCommaAndErrorMessage)



signal that the image corresponding to the supplied outgoing transaction and image could not be read or stored properly on the receiving side, and that the transaction should be marked as failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String token = "token_example"; // String | authentication token identifying the current box-to-box connection
    FailedOutgoingTransactionImage outgoingTransactionAndImageCommaAndErrorMessage = new FailedOutgoingTransactionImage(); // FailedOutgoingTransactionImage | the outgoing transaction and image information block corresponding to the failed image transfer, along with the associated error message
    try {
      apiInstance.transactionsTokenOutgoingFailedPost(token, outgoingTransactionAndImageCommaAndErrorMessage);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#transactionsTokenOutgoingFailedPost");
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
| **token** | **String**| authentication token identifying the current box-to-box connection | |
| **outgoingTransactionAndImageCommaAndErrorMessage** | [**FailedOutgoingTransactionImage**](FailedOutgoingTransactionImage.md)| the outgoing transaction and image information block corresponding to the failed image transfer, along with the associated error message | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | failed message received |  -  |
| **401** | unauthorized, invalid token |  -  |

<a id="transactionsTokenOutgoingGet"></a>
# **transactionsTokenOutgoingGet**
> transactionsTokenOutgoingGet(token, transactionid, imageid)



fetch an image from the connected box as part of a transaction. This method is used when sending images using the poll method from a public slicebox.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String token = "token_example"; // String | authentication token identifying the current box-to-box connection
    Long transactionid = 56L; // Long | the ID of the outgoing transaction
    Long imageid = 56L; // Long | the ID of the outgoing transaction image
    try {
      apiInstance.transactionsTokenOutgoingGet(token, transactionid, imageid);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#transactionsTokenOutgoingGet");
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
| **token** | **String**| authentication token identifying the current box-to-box connection | |
| **transactionid** | **Long**| the ID of the outgoing transaction | |
| **imageid** | **Long**| the ID of the outgoing transaction image | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | binary data of dataset |  -  |
| **401** | unauthorized, invalid token |  -  |
| **404** | no outgoing trensaction and/or image found for the supplied transaction id and transaction image id |  -  |

<a id="transactionsTokenOutgoingPollGet"></a>
# **transactionsTokenOutgoingPollGet**
> List&lt;OutgoingTransactionImage&gt; transactionsTokenOutgoingPollGet(token)



get next outgoing transaction and image (information on the next image that the connected box wishes to send to you), if any. This method is used when sending images using the poll method from a public slicebox.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String token = "token_example"; // String | authentication token identifying the current box-to-box connection
    try {
      List<OutgoingTransactionImage> result = apiInstance.transactionsTokenOutgoingPollGet(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#transactionsTokenOutgoingPollGet");
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
| **token** | **String**| authentication token identifying the current box-to-box connection | |

### Return type

[**List&lt;OutgoingTransactionImage&gt;**](OutgoingTransactionImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | next outgoing transaction and image information block |  -  |
| **401** | unauthorized, invalid token |  -  |
| **404** | there are currently no outgoing transactions to fetch for the box connection with the supplied token |  -  |

<a id="transactionsTokenStatusGet"></a>
# **transactionsTokenStatusGet**
> transactionsTokenStatusGet(token, transactionid)



get the status of the remote incoming transaction with the supplied transaction ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String token = "token_example"; // String | authentication token identifying the current box-to-box connection
    Long transactionid = 56L; // Long | the ID of the client's outgoing transaction
    try {
      apiInstance.transactionsTokenStatusGet(token, transactionid);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#transactionsTokenStatusGet");
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
| **token** | **String**| authentication token identifying the current box-to-box connection | |
| **transactionid** | **Long**| the ID of the client&#39;s outgoing transaction | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | string representation of the transaction status (FINISHED, FAILED, WAITING or PROCESSING) |  -  |
| **401** | unauthorized, invalid token |  -  |
| **404** | no transaction found for the supplied transaction ID and box token |  -  |

<a id="transactionsTokenStatusPut"></a>
# **transactionsTokenStatusPut**
> transactionsTokenStatusPut(token, transactionid, transactionStatus)



update the status of the transaction with the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String token = "token_example"; // String | authentication token identifying the current box-to-box connection
    Long transactionid = 56L; // Long | the ID of the client's outgoing transaction
    String transactionStatus = "transactionStatus_example"; // String | the updated status of the transaction
    try {
      apiInstance.transactionsTokenStatusPut(token, transactionid, transactionStatus);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#transactionsTokenStatusPut");
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
| **token** | **String**| authentication token identifying the current box-to-box connection | |
| **transactionid** | **Long**| the ID of the client&#39;s outgoing transaction | |
| **transactionStatus** | **String**| the updated status of the transaction | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | status update successfully applied to transaction |  -  |
| **404** | no transaction found for the supplied transaction ID and box token |  -  |

