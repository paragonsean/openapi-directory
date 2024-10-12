# TransfersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**partnerTransfersCancel**](TransfersApi.md#partnerTransfersCancel) | **DELETE** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/customers/{customerName}/transfers/{transferName} |  |
| [**partnerTransfersGet**](TransfersApi.md#partnerTransfersGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/customers/{customerName}/transfers/{transferName} |  |
| [**partnerTransfersInitiate**](TransfersApi.md#partnerTransfersInitiate) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/customers/{customerName}/initiateTransfer |  |
| [**partnerTransfersList**](TransfersApi.md#partnerTransfersList) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/customers/{customerName}/transfers |  |
| [**transfersCancel**](TransfersApi.md#transfersCancel) | **DELETE** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/transfers/{transferName} |  |
| [**transfersGet**](TransfersApi.md#transfersGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/transfers/{transferName} |  |
| [**transfersInitiate**](TransfersApi.md#transfersInitiate) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/initiateTransfer |  |
| [**transfersList**](TransfersApi.md#transfersList) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/transfers |  |


<a id="partnerTransfersCancel"></a>
# **partnerTransfersCancel**
> TransferDetails partnerTransfersCancel(billingAccountName, billingProfileName, customerName, transferName)



Cancels the transfer for given transfer Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransfersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TransfersApi apiInstance = new TransfersApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String customerName = "customerName_example"; // String | Customer name.
    String transferName = "transferName_example"; // String | Transfer Name.
    try {
      TransferDetails result = apiInstance.partnerTransfersCancel(billingAccountName, billingProfileName, customerName, transferName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransfersApi#partnerTransfersCancel");
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
| **billingAccountName** | **String**| billing Account Id. | |
| **billingProfileName** | **String**| Billing Profile Id. | |
| **customerName** | **String**| Customer name. | |
| **transferName** | **String**| Transfer Name. | |

### Return type

[**TransferDetails**](TransferDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of canceled transfer. |  -  |
| **0** | Unexpected error. |  -  |

<a id="partnerTransfersGet"></a>
# **partnerTransfersGet**
> TransferDetails partnerTransfersGet(billingAccountName, billingProfileName, customerName, transferName)



Gets the transfer details for given transfer Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransfersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TransfersApi apiInstance = new TransfersApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String customerName = "customerName_example"; // String | Customer name.
    String transferName = "transferName_example"; // String | Transfer Name.
    try {
      TransferDetails result = apiInstance.partnerTransfersGet(billingAccountName, billingProfileName, customerName, transferName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransfersApi#partnerTransfersGet");
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
| **billingAccountName** | **String**| billing Account Id. | |
| **billingProfileName** | **String**| Billing Profile Id. | |
| **customerName** | **String**| Customer name. | |
| **transferName** | **String**| Transfer Name. | |

### Return type

[**TransferDetails**](TransferDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of transfer. |  -  |
| **0** | Unexpected error. |  -  |

<a id="partnerTransfersInitiate"></a>
# **partnerTransfersInitiate**
> TransferDetails partnerTransfersInitiate(billingAccountName, billingProfileName, customerName, parameters)



Initiates the request to transfer the legacy subscriptions or RIs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransfersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TransfersApi apiInstance = new TransfersApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String customerName = "customerName_example"; // String | Customer name.
    InitiateTransferRequest parameters = new InitiateTransferRequest(); // InitiateTransferRequest | Parameters supplied to initiate the transfer.
    try {
      TransferDetails result = apiInstance.partnerTransfersInitiate(billingAccountName, billingProfileName, customerName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransfersApi#partnerTransfersInitiate");
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
| **billingAccountName** | **String**| billing Account Id. | |
| **billingProfileName** | **String**| Billing Profile Id. | |
| **customerName** | **String**| Customer name. | |
| **parameters** | [**InitiateTransferRequest**](InitiateTransferRequest.md)| Parameters supplied to initiate the transfer. | |

### Return type

[**TransferDetails**](TransferDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Initiated transfer details. |  -  |
| **0** | Unexpected error. |  -  |

<a id="partnerTransfersList"></a>
# **partnerTransfersList**
> TransferDetailsListResult partnerTransfersList(billingAccountName, billingProfileName, customerName)



Lists all transfer&#39;s details initiated from given invoice section.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransfersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TransfersApi apiInstance = new TransfersApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String customerName = "customerName_example"; // String | Customer name.
    try {
      TransferDetailsListResult result = apiInstance.partnerTransfersList(billingAccountName, billingProfileName, customerName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransfersApi#partnerTransfersList");
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
| **billingAccountName** | **String**| billing Account Id. | |
| **billingProfileName** | **String**| Billing Profile Id. | |
| **customerName** | **String**| Customer name. | |

### Return type

[**TransferDetailsListResult**](TransferDetailsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of transfers initiated from this invoice section. |  -  |
| **0** | Unexpected error. |  -  |

<a id="transfersCancel"></a>
# **transfersCancel**
> TransferDetails transfersCancel(billingAccountName, billingProfileName, invoiceSectionName, transferName)



Cancels the transfer for given transfer Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransfersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TransfersApi apiInstance = new TransfersApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String transferName = "transferName_example"; // String | Transfer Name.
    try {
      TransferDetails result = apiInstance.transfersCancel(billingAccountName, billingProfileName, invoiceSectionName, transferName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransfersApi#transfersCancel");
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
| **billingAccountName** | **String**| billing Account Id. | |
| **billingProfileName** | **String**| Billing Profile Id. | |
| **invoiceSectionName** | **String**| InvoiceSection Id. | |
| **transferName** | **String**| Transfer Name. | |

### Return type

[**TransferDetails**](TransferDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of canceled transfer. |  -  |
| **0** | Unexpected error. |  -  |

<a id="transfersGet"></a>
# **transfersGet**
> TransferDetails transfersGet(billingAccountName, billingProfileName, invoiceSectionName, transferName)



Gets the transfer details for given transfer Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransfersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TransfersApi apiInstance = new TransfersApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String transferName = "transferName_example"; // String | Transfer Name.
    try {
      TransferDetails result = apiInstance.transfersGet(billingAccountName, billingProfileName, invoiceSectionName, transferName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransfersApi#transfersGet");
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
| **billingAccountName** | **String**| billing Account Id. | |
| **billingProfileName** | **String**| Billing Profile Id. | |
| **invoiceSectionName** | **String**| InvoiceSection Id. | |
| **transferName** | **String**| Transfer Name. | |

### Return type

[**TransferDetails**](TransferDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of transfer. |  -  |
| **0** | Unexpected error. |  -  |

<a id="transfersInitiate"></a>
# **transfersInitiate**
> TransferDetails transfersInitiate(billingAccountName, billingProfileName, invoiceSectionName, parameters)



Initiates the request to transfer the legacy subscriptions or RIs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransfersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TransfersApi apiInstance = new TransfersApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    InitiateTransferRequest parameters = new InitiateTransferRequest(); // InitiateTransferRequest | Parameters supplied to initiate the transfer.
    try {
      TransferDetails result = apiInstance.transfersInitiate(billingAccountName, billingProfileName, invoiceSectionName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransfersApi#transfersInitiate");
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
| **billingAccountName** | **String**| billing Account Id. | |
| **billingProfileName** | **String**| Billing Profile Id. | |
| **invoiceSectionName** | **String**| InvoiceSection Id. | |
| **parameters** | [**InitiateTransferRequest**](InitiateTransferRequest.md)| Parameters supplied to initiate the transfer. | |

### Return type

[**TransferDetails**](TransferDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Initiated transfer details. |  -  |
| **0** | Unexpected error. |  -  |

<a id="transfersList"></a>
# **transfersList**
> TransferDetailsListResult transfersList(billingAccountName, billingProfileName, invoiceSectionName)



Lists all transfer&#39;s details initiated from given invoice section.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransfersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TransfersApi apiInstance = new TransfersApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    try {
      TransferDetailsListResult result = apiInstance.transfersList(billingAccountName, billingProfileName, invoiceSectionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransfersApi#transfersList");
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
| **billingAccountName** | **String**| billing Account Id. | |
| **billingProfileName** | **String**| Billing Profile Id. | |
| **invoiceSectionName** | **String**| InvoiceSection Id. | |

### Return type

[**TransferDetailsListResult**](TransferDetailsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of transfers initiated from this invoice section. |  -  |
| **0** | Unexpected error. |  -  |

