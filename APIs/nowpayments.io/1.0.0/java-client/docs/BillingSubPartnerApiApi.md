# BillingSubPartnerApiApi

All URIs are relative to *https://api.nowpayments.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllTransfers**](BillingSubPartnerApiApi.md#getAllTransfers) | **GET** /v1/sub-partner/transfers | Get all transfers |
| [**getSubPartnerBalance**](BillingSubPartnerApiApi.md#getSubPartnerBalance) | **GET** /v1/sub-partner/balance/{id} | Get sub-partner balance |
| [**getSubPartners**](BillingSubPartnerApiApi.md#getSubPartners) | **GET** /v1/sub-partner | Get sub-partners |
| [**getTransfer**](BillingSubPartnerApiApi.md#getTransfer) | **GET** /v1/sub-partner/transfer/{id} | Get transfer |


<a id="getAllTransfers"></a>
# **getAllTransfers**
> GetAllTransfers200Response getAllTransfers(id, status, limit, offset, order)

Get all transfers

Returns the entire list of transfers created by your sub-partners.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingSubPartnerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nowpayments.io");

    BillingSubPartnerApiApi apiInstance = new BillingSubPartnerApiApi(defaultClient);
    String id = "111"; // String | int or array of int (optional)
    String status = "CREATED"; // String | string or array of string  \"WAITING\"/\"CREATED\"/\"FINISHED\"/\"REJECTED\" (optional)
    String limit = "10"; // String | (optional) default 10
    String offset = "0"; // String | (optional) default 0
    String order = "ASC"; // String | ASC / DESC (optional) default ASC
    try {
      GetAllTransfers200Response result = apiInstance.getAllTransfers(id, status, limit, offset, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingSubPartnerApiApi#getAllTransfers");
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
| **id** | **String**| int or array of int (optional) | [optional] |
| **status** | **String**| string or array of string  \&quot;WAITING\&quot;/\&quot;CREATED\&quot;/\&quot;FINISHED\&quot;/\&quot;REJECTED\&quot; (optional) | [optional] |
| **limit** | **String**| (optional) default 10 | [optional] |
| **offset** | **String**| (optional) default 0 | [optional] |
| **order** | **String**| ASC / DESC (optional) default ASC | [optional] |

### Return type

[**GetAllTransfers200Response**](GetAllTransfers200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  -  |

<a id="getSubPartnerBalance"></a>
# **getSubPartnerBalance**
> GetSubPartnerBalance200Response getSubPartnerBalance(id, xApiKey)

Get sub-partner balance

This request can be made only from a whitelisted IP.   If IP whitelisting is disabled, this request can be made by any user that has an API key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingSubPartnerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nowpayments.io");

    BillingSubPartnerApiApi apiInstance = new BillingSubPartnerApiApi(defaultClient);
    String id = "id_example"; // String | 
    String xApiKey = "{{your_api_key}}"; // String | 
    try {
      GetSubPartnerBalance200Response result = apiInstance.getSubPartnerBalance(id, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingSubPartnerApiApi#getSubPartnerBalance");
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
| **id** | **String**|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**GetSubPartnerBalance200Response**](GetSubPartnerBalance200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  -  |

<a id="getSubPartners"></a>
# **getSubPartners**
> getSubPartners(id, offset, limit, order)

Get sub-partners

This method returns the entire list of your sub-partners.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingSubPartnerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nowpayments.io");

    BillingSubPartnerApiApi apiInstance = new BillingSubPartnerApiApi(defaultClient);
    String id = "111"; // String | int or array of int (optional)
    String offset = "0"; // String | (optional) default 0
    String limit = "10"; // String | (optional) default 10
    String order = "DESC"; // String | ASC / DESC (optional) default ASC
    try {
      apiInstance.getSubPartners(id, offset, limit, order);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingSubPartnerApiApi#getSubPartners");
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
| **id** | **String**| int or array of int (optional) | [optional] |
| **offset** | **String**| (optional) default 0 | [optional] |
| **limit** | **String**| (optional) default 10 | [optional] |
| **order** | **String**| ASC / DESC (optional) default ASC | [optional] |

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
| **200** |  |  -  |

<a id="getTransfer"></a>
# **getTransfer**
> GetTransfer200Response getTransfer(id)

Get transfer

Get the actual information about the transfer. You need to provide the transfer ID in the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingSubPartnerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nowpayments.io");

    BillingSubPartnerApiApi apiInstance = new BillingSubPartnerApiApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      GetTransfer200Response result = apiInstance.getTransfer(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingSubPartnerApiApi#getTransfer");
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
| **id** | **String**|  | |

### Return type

[**GetTransfer200Response**](GetTransfer200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  -  |

