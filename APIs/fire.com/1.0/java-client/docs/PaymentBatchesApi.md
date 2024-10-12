# PaymentBatchesApi

All URIs are relative to *https://api.fire.com/business*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addBankTransferBatchPayment**](PaymentBatchesApi.md#addBankTransferBatchPayment) | **POST** /v1/batches/{batchUuid}/banktransfers | Add a bank transfer payment to the batch. |
| [**addInternalTransferBatchPayment**](PaymentBatchesApi.md#addInternalTransferBatchPayment) | **POST** /v1/batches/{batchUuid}/internaltransfers | Add an internal transfer payment to the batch |
| [**addInternationalTransferBatchPayment**](PaymentBatchesApi.md#addInternationalTransferBatchPayment) | **POST** /v2/batches/{batchUuid}/internationaltransfers | Add an international transfer payment to the batch. |
| [**cancelBatchPayment**](PaymentBatchesApi.md#cancelBatchPayment) | **DELETE** /v1/batches/{batchUuid} | Cancel a batch |
| [**createBatchPayment**](PaymentBatchesApi.md#createBatchPayment) | **POST** /v1/batches | Create a new batch of payments |
| [**deleteBankTransferBatchPayment**](PaymentBatchesApi.md#deleteBankTransferBatchPayment) | **DELETE** /v1/batches/{batchUuid}/banktransfers/{itemUuid} | Remove a Payment from the Batch (Bank Transfers) |
| [**deleteInternalTransferBatchPayment**](PaymentBatchesApi.md#deleteInternalTransferBatchPayment) | **DELETE** /v1/batches/{batchUuid}/internaltransfers/{itemUuid} | Remove a Payment from the Batch (Internal Transfer) |
| [**deleteInternationalTransferBatchPayment**](PaymentBatchesApi.md#deleteInternationalTransferBatchPayment) | **DELETE** /v2/batches/{batchUuid}/internationaltransfers/{itemUuid} | Remove a Payment from the Batch (International Transfers) |
| [**getBatches**](PaymentBatchesApi.md#getBatches) | **GET** /v1/batches | List batches |
| [**getDetailsSingleBatch**](PaymentBatchesApi.md#getDetailsSingleBatch) | **GET** /v1/batches/{batchUuid} | Get details of a single Batch |
| [**getItemsBatchBankTransfer**](PaymentBatchesApi.md#getItemsBatchBankTransfer) | **GET** /v1/batches/{batchUuid}/banktransfers | List items in a Batch (Bank Transfers) |
| [**getItemsBatchInternalTrasnfer**](PaymentBatchesApi.md#getItemsBatchInternalTrasnfer) | **GET** /v1/batches/{batchUuid}/internaltransfers | List items in a Batch (Internal Transfers) |
| [**getItemsBatchInternationalTransfer**](PaymentBatchesApi.md#getItemsBatchInternationalTransfer) | **GET** /v2/batches/{batchUuid}/internationaltransfers | List items in a Batch (International Transfers) |
| [**getListofApproversForBatch**](PaymentBatchesApi.md#getListofApproversForBatch) | **GET** /v1/batches/{batchUuid}/approvals | List Approvers for a Batch |
| [**submitBatch**](PaymentBatchesApi.md#submitBatch) | **PUT** /v1/batches/{batchUuid} | Submit a batch for approval |


<a id="addBankTransferBatchPayment"></a>
# **addBankTransferBatchPayment**
> NewBatchItemResponse addBankTransferBatchPayment(batchUuid, addBankTransferBatchPaymentRequest)

Add a bank transfer payment to the batch.

There are two ways to process bank transfers - by Payee ID (**Mode 1**) or by Payee Account Details (**Mode 2**).  **Mode 1:** Use the payee IDs of existing approved payees set up against your account. These batches can be approved in the normal manner.  **Mode 2:** Use the account details of the payee. In the event that these details correspond to an existing approved payee, the batch can be approved as normal. If the account details are new, a batch of New Payees will automatically be created. This batch will need to be approved before the Payment batch can be approved. These payees will then exist as approved payees for future batches. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PaymentBatchesApi apiInstance = new PaymentBatchesApi(defaultClient);
    String batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
    AddBankTransferBatchPaymentRequest addBankTransferBatchPaymentRequest = new AddBankTransferBatchPaymentRequest(); // AddBankTransferBatchPaymentRequest | Details of **Mode 1** & **Mode 2**.
    try {
      NewBatchItemResponse result = apiInstance.addBankTransferBatchPayment(batchUuid, addBankTransferBatchPaymentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentBatchesApi#addBankTransferBatchPayment");
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
| **batchUuid** | **String**|  | |
| **addBankTransferBatchPaymentRequest** | [**AddBankTransferBatchPaymentRequest**](AddBankTransferBatchPaymentRequest.md)| Details of **Mode 1** &amp; **Mode 2**. | |

### Return type

[**NewBatchItemResponse**](NewBatchItemResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Batch payment added successfully. **Note*** Please use batchUuid when submitting a batch, not batchItemUuid. |  -  |

<a id="addInternalTransferBatchPayment"></a>
# **addInternalTransferBatchPayment**
> NewBatchItemResponse addInternalTransferBatchPayment(batchUuid, batchItemInternalTransfer)

Add an internal transfer payment to the batch

Simply specify the source account, destination account, amount and a reference.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PaymentBatchesApi apiInstance = new PaymentBatchesApi(defaultClient);
    String batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
    BatchItemInternalTransfer batchItemInternalTransfer = new BatchItemInternalTransfer(); // BatchItemInternalTransfer | Details of the source account, destination account, amount and a reference.
    try {
      NewBatchItemResponse result = apiInstance.addInternalTransferBatchPayment(batchUuid, batchItemInternalTransfer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentBatchesApi#addInternalTransferBatchPayment");
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
| **batchUuid** | **String**|  | |
| **batchItemInternalTransfer** | [**BatchItemInternalTransfer**](BatchItemInternalTransfer.md)| Details of the source account, destination account, amount and a reference. | |

### Return type

[**NewBatchItemResponse**](NewBatchItemResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Batch payment added successfully. Note* Please use batchUuid when submitting a batch, not batchItemUuid. |  -  |

<a id="addInternationalTransferBatchPayment"></a>
# **addInternationalTransferBatchPayment**
> NewBatchItemResponse addInternationalTransferBatchPayment(batchUuid, batchItemInternationalTransferMode1)

Add an international transfer payment to the batch.

International transfers must be added to a batch using the Payee ID (**Mode 1**). Payees must be set up using the web application.  **Mode 1:** Use the payee IDs of existing approved payees set up against your account. These batches can be approved in the normal manner. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PaymentBatchesApi apiInstance = new PaymentBatchesApi(defaultClient);
    String batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
    BatchItemInternationalTransferMode1 batchItemInternationalTransferMode1 = new BatchItemInternationalTransferMode1(); // BatchItemInternationalTransferMode1 | Details of **Mode 1**
    try {
      NewBatchItemResponse result = apiInstance.addInternationalTransferBatchPayment(batchUuid, batchItemInternationalTransferMode1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentBatchesApi#addInternationalTransferBatchPayment");
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
| **batchUuid** | **String**|  | |
| **batchItemInternationalTransferMode1** | [**BatchItemInternationalTransferMode1**](BatchItemInternationalTransferMode1.md)| Details of **Mode 1** | |

### Return type

[**NewBatchItemResponse**](NewBatchItemResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Batch payment added successfully. **Note*** Please use batchUuid when submitting a batch, not batchItemUuid. |  -  |

<a id="cancelBatchPayment"></a>
# **cancelBatchPayment**
> cancelBatchPayment(batchUuid)

Cancel a batch

Cancels the Batch. You can only cancel a batch before it is submitted for approval (while it is in the OPEN state).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PaymentBatchesApi apiInstance = new PaymentBatchesApi(defaultClient);
    String batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
    try {
      apiInstance.cancelBatchPayment(batchUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentBatchesApi#cancelBatchPayment");
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
| **batchUuid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Batch payment deleted successfully. |  -  |

<a id="createBatchPayment"></a>
# **createBatchPayment**
> NewBatchResponse createBatchPayment(newBatch)

Create a new batch of payments

The fire.com API allows businesses to automate payments between their accounts or to third parties across the UK and Europe.  For added security, the API can only set up the payments in batches. These batches must be approved by an authorised user via the firework mobile app.   The process is as follows:  **1.**Create a new batch  **2.**Add payments to the batch  **3.**Submit the batch for approval  Once the batch is submitted, the authorised users will receive notifications to their firework mobile apps. They can review the contents of the batch and then approve or reject it. If approved, the batch is then processed. You can avail of enhanced security by using Dual Authorisation to verify payments if you wish. Dual Authorisation can be enabled by you when setting up your API application in firework online.  **Batch Life Cycle Events**  A batch webhook can be specified to receive details of all the payments as they are processed. This webhook receives notifications for every event in the batch lifecycle.  The following events are triggered during a batch:  **batch.opened:** Contains the details of the batch opened. Checks that the callback URL exists - unless a HTTP 200 response is returned, the callback URL will not be configured.  **batch.item-added:** Details of the item added to the batch  **batch.item-removed:** Details of the item removed from the batch  **batch.cancelled:** Notifies that the batch was cancelled.  **batch.submitted:** Notifes that the batch was submitted  **batch.approved:** Notifies that the batch was approved.  **batch.rejected:** Notifies that the batch was rejected.  **batch.failed:** Notifies that the batch failed - includes the details of the failure (insufficient funds etc)  **batch.completed:** Notifies that the batch completed successfully. Includes a summary.  Push notifications are sent to the firework mobile app for many of these events too - these can be configured from within the app.  This is the first step in creating a batch payment. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PaymentBatchesApi apiInstance = new PaymentBatchesApi(defaultClient);
    NewBatch newBatch = new NewBatch(); // NewBatch | Details of the batch payment
    try {
      NewBatchResponse result = apiInstance.createBatchPayment(newBatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentBatchesApi#createBatchPayment");
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
| **newBatch** | [**NewBatch**](NewBatch.md)| Details of the batch payment | |

### Return type

[**NewBatchResponse**](NewBatchResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Batch created successfully |  -  |

<a id="deleteBankTransferBatchPayment"></a>
# **deleteBankTransferBatchPayment**
> deleteBankTransferBatchPayment(batchUuid, itemUuid)

Remove a Payment from the Batch (Bank Transfers)

Removes a Payment from the Batch (Bank Transfers). You can only remove payments before the batch is submitted for approval (while it is in the OPEN state).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PaymentBatchesApi apiInstance = new PaymentBatchesApi(defaultClient);
    String batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
    String itemUuid = "itemUuid_example"; // String | 
    try {
      apiInstance.deleteBankTransferBatchPayment(batchUuid, itemUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentBatchesApi#deleteBankTransferBatchPayment");
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
| **batchUuid** | **String**|  | |
| **itemUuid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Batch payment deleted successfully. |  -  |

<a id="deleteInternalTransferBatchPayment"></a>
# **deleteInternalTransferBatchPayment**
> deleteInternalTransferBatchPayment(batchUuid, itemUuid)

Remove a Payment from the Batch (Internal Transfer)

Removes a Payment from the Batch (Internal Transfer). You can only remove payments before the batch is submitted for approval (while it is in the OPEN state).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PaymentBatchesApi apiInstance = new PaymentBatchesApi(defaultClient);
    String batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
    String itemUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
    try {
      apiInstance.deleteInternalTransferBatchPayment(batchUuid, itemUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentBatchesApi#deleteInternalTransferBatchPayment");
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
| **batchUuid** | **String**|  | |
| **itemUuid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Batch payment deleted successfully. |  -  |

<a id="deleteInternationalTransferBatchPayment"></a>
# **deleteInternationalTransferBatchPayment**
> deleteInternationalTransferBatchPayment(batchUuid, itemUuid)

Remove a Payment from the Batch (International Transfers)

Removes a Payment from the Batch (International Transfers). You can only remove payments before the batch is submitted for approval (while it is in the OPEN state).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PaymentBatchesApi apiInstance = new PaymentBatchesApi(defaultClient);
    String batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
    String itemUuid = "itemUuid_example"; // String | 
    try {
      apiInstance.deleteInternationalTransferBatchPayment(batchUuid, itemUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentBatchesApi#deleteInternationalTransferBatchPayment");
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
| **batchUuid** | **String**|  | |
| **itemUuid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Batch payment deleted successfully. |  -  |

<a id="getBatches"></a>
# **getBatches**
> BatchItems getBatches(batchStatus, batchTypes, orderBy, order)

List batches

Returns the list of batch with the specified types and statuses. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PaymentBatchesApi apiInstance = new PaymentBatchesApi(defaultClient);
    String batchStatus = "SUBMITTED"; // String | 
    String batchTypes = "INTERNAL_TRANSFER"; // String | 
    String orderBy = "DATE"; // String | 
    String order = "DESC"; // String | 
    try {
      BatchItems result = apiInstance.getBatches(batchStatus, batchTypes, orderBy, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentBatchesApi#getBatches");
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
| **batchStatus** | **String**|  | [optional] [enum: SUBMITTED, REMOVED, SUCCEEDED, FAILED] |
| **batchTypes** | **String**|  | [optional] [enum: INTERNAL_TRANSFER, BANK_TRANSFER, INTERNATIONAL_TRANSFER, NEW_PAYEE] |
| **orderBy** | **String**|  | [optional] [enum: DATE] |
| **order** | **String**|  | [optional] [enum: DESC, ASC] |

### Return type

[**BatchItems**](BatchItems.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List all batches. |  -  |

<a id="getDetailsSingleBatch"></a>
# **getDetailsSingleBatch**
> Batch getDetailsSingleBatch(batchUuid)

Get details of a single Batch

Returns the details of the batch specified in the API endpoint - {batchUuid}.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PaymentBatchesApi apiInstance = new PaymentBatchesApi(defaultClient);
    String batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
    try {
      Batch result = apiInstance.getDetailsSingleBatch(batchUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentBatchesApi#getDetailsSingleBatch");
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
| **batchUuid** | **String**|  | |

### Return type

[**Batch**](Batch.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the details of the batch specified in the API endpoint - {batchUuid}. |  -  |

<a id="getItemsBatchBankTransfer"></a>
# **getItemsBatchBankTransfer**
> BatchItems getItemsBatchBankTransfer(batchUuid, offset, limit)

List items in a Batch (Bank Transfers)

Returns a paginated list of items in the specified batch.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PaymentBatchesApi apiInstance = new PaymentBatchesApi(defaultClient);
    String batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
    Long offset = 0L; // Long | 
    Long limit = 10L; // Long | 
    try {
      BatchItems result = apiInstance.getItemsBatchBankTransfer(batchUuid, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentBatchesApi#getItemsBatchBankTransfer");
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
| **batchUuid** | **String**|  | |
| **offset** | **Long**|  | [optional] |
| **limit** | **Long**|  | [optional] |

### Return type

[**BatchItems**](BatchItems.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A fire.com list object of Batch Items (Internal transfers or Bank transfers). |  -  |

<a id="getItemsBatchInternalTrasnfer"></a>
# **getItemsBatchInternalTrasnfer**
> BatchItems getItemsBatchInternalTrasnfer(batchUuid, offset, limit)

List items in a Batch (Internal Transfers)

Returns a paginated list of items in the specified batch.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PaymentBatchesApi apiInstance = new PaymentBatchesApi(defaultClient);
    String batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
    Long offset = 0L; // Long | 
    Long limit = 10L; // Long | 
    try {
      BatchItems result = apiInstance.getItemsBatchInternalTrasnfer(batchUuid, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentBatchesApi#getItemsBatchInternalTrasnfer");
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
| **batchUuid** | **String**|  | |
| **offset** | **Long**|  | [optional] |
| **limit** | **Long**|  | [optional] |

### Return type

[**BatchItems**](BatchItems.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A fire.com list object of Batch Items (Internal transfers or Bank transfers). |  -  |

<a id="getItemsBatchInternationalTransfer"></a>
# **getItemsBatchInternationalTransfer**
> BatchItems getItemsBatchInternationalTransfer(batchUuid, offset, limit)

List items in a Batch (International Transfers)

Returns a paginated list of items in the specified batch.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PaymentBatchesApi apiInstance = new PaymentBatchesApi(defaultClient);
    String batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
    Long offset = 0L; // Long | 
    Long limit = 10L; // Long | 
    try {
      BatchItems result = apiInstance.getItemsBatchInternationalTransfer(batchUuid, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentBatchesApi#getItemsBatchInternationalTransfer");
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
| **batchUuid** | **String**|  | |
| **offset** | **Long**|  | [optional] |
| **limit** | **Long**|  | [optional] |

### Return type

[**BatchItems**](BatchItems.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A fire.com list object of Batch Items (Internal transfers, Bank transfers or International transfers). |  -  |

<a id="getListofApproversForBatch"></a>
# **getListofApproversForBatch**
> BatchApprovers getListofApproversForBatch(batchUuid)

List Approvers for a Batch

Returns a list of approvers for this batch.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PaymentBatchesApi apiInstance = new PaymentBatchesApi(defaultClient);
    String batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
    try {
      BatchApprovers result = apiInstance.getListofApproversForBatch(batchUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentBatchesApi#getListofApproversForBatch");
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
| **batchUuid** | **String**|  | |

### Return type

[**BatchApprovers**](BatchApprovers.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of approvers for this batch. |  -  |

<a id="submitBatch"></a>
# **submitBatch**
> submitBatch(batchUuid)

Submit a batch for approval

Submits the Batch (for approval in the case of a **BANK_TRANSFER** or **INTERNATIONAL_TRANSFER**). If this is an **INTERNAL_TRANSFER** batch, the transfers are immediately queued for processing. If this is a **BANK_TRANSFER** or **INTERNATIONAL_TRANSFER** batch, this will trigger requests for approval to the firework mobile apps of authorised users. Once those users approve the batch, it is queued for processing.  You can only submit a batch while it is in the OPEN state. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PaymentBatchesApi apiInstance = new PaymentBatchesApi(defaultClient);
    String batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
    try {
      apiInstance.submitBatch(batchUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentBatchesApi#submitBatch");
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
| **batchUuid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No body is returned - a HTTP 204 No Content response signifies the call was successful. |  -  |

