# MerchantRetrievalApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMerchantTransferById**](MerchantRetrievalApi.md#getMerchantTransferById) | **GET** /send/#env/v1/partners/{partnerId}/merchant/transfers/{transferId} | Purpose of this service is to retrieve the Transfer resource associated with the specified transfer-id. |
| [**getMerchantTransferByRef**](MerchantRetrievalApi.md#getMerchantTransferByRef) | **GET** /send/#env/v1/partners/{partnerId}/merchant/transfers | Purpose of this service is to retrieve the Transfer resource associated with a specified transfer_reference value. |


<a id="getMerchantTransferById"></a>
# **getMerchantTransferById**
> MerchantTransfer54Wrapper getMerchantTransferById(partnerId, transferId)

Purpose of this service is to retrieve the Transfer resource associated with the specified transfer-id.

Purpose of this service is to retrieve the Transfer resource associated with the specified transfer-id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MerchantRetrievalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    MerchantRetrievalApi apiInstance = new MerchantRetrievalApi(defaultClient);
    String partnerId = "partnerId_example"; // String | Path Param - Provider assigned partner id. Details - string, 32
    String transferId = "transferId_example"; // String | Path Param - Valid transfer id
    try {
      MerchantTransfer54Wrapper result = apiInstance.getMerchantTransferById(partnerId, transferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MerchantRetrievalApi#getMerchantTransferById");
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
| **partnerId** | **String**| Path Param - Provider assigned partner id. Details - string, 32 | |
| **transferId** | **String**| Path Param - Valid transfer id | |

### Return type

[**MerchantTransfer54Wrapper**](MerchantTransfer54Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response details for a merchant transfer. |  -  |

<a id="getMerchantTransferByRef"></a>
# **getMerchantTransferByRef**
> MerchantTransfers69Wrapper getMerchantTransferByRef(partnerId, ref)

Purpose of this service is to retrieve the Transfer resource associated with a specified transfer_reference value.

Purpose of this service is to retrieve the Transfer resource associated with a specified transfer_reference value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MerchantRetrievalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    MerchantRetrievalApi apiInstance = new MerchantRetrievalApi(defaultClient);
    String partnerId = "partnerId_example"; // String | Path Param - Provider assigned partner id. Details - string, 32
    String ref = "ref_example"; // String | Query Param - Is the client specified transfer reference when initiating the transfer. Allowable characters are alphanumeric and * , - . _ ~. Details- 6-40 Example- DEF123456
    try {
      MerchantTransfers69Wrapper result = apiInstance.getMerchantTransferByRef(partnerId, ref);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MerchantRetrievalApi#getMerchantTransferByRef");
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
| **partnerId** | **String**| Path Param - Provider assigned partner id. Details - string, 32 | |
| **ref** | **String**| Query Param - Is the client specified transfer reference when initiating the transfer. Allowable characters are alphanumeric and * , - . _ ~. Details- 6-40 Example- DEF123456 | |

### Return type

[**MerchantTransfers69Wrapper**](MerchantTransfers69Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response details for a merchant transfer. |  -  |

