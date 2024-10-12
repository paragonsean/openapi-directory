# RecipientTransfersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**recipientTransfersAccept**](RecipientTransfersApi.md#recipientTransfersAccept) | **POST** /providers/Microsoft.Billing/transfers/{transferName}/acceptTransfer | Accepts the transfer with given transfer Id. |
| [**recipientTransfersDecline**](RecipientTransfersApi.md#recipientTransfersDecline) | **POST** /providers/Microsoft.Billing/transfers/{transferName}/declineTransfer | Declines the transfer with given transfer Id. |
| [**recipientTransfersGet**](RecipientTransfersApi.md#recipientTransfersGet) | **GET** /providers/Microsoft.Billing/transfers/{transferName}/ | Gets the transfer with given transfer Id. |
| [**recipientTransfersList**](RecipientTransfersApi.md#recipientTransfersList) | **GET** /providers/Microsoft.Billing/transfers | Lists the transfers received by caller. |


<a id="recipientTransfersAccept"></a>
# **recipientTransfersAccept**
> RecipientTransferDetails recipientTransfersAccept(transferName, body)

Accepts the transfer with given transfer Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipientTransfersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RecipientTransfersApi apiInstance = new RecipientTransfersApi(defaultClient);
    String transferName = "transferName_example"; // String | Transfer Name.
    AcceptTransferRequest body = new AcceptTransferRequest(); // AcceptTransferRequest | Accept transfer parameters.
    try {
      RecipientTransferDetails result = apiInstance.recipientTransfersAccept(transferName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipientTransfersApi#recipientTransfersAccept");
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
| **transferName** | **String**| Transfer Name. | |
| **body** | [**AcceptTransferRequest**](AcceptTransferRequest.md)| Accept transfer parameters. | |

### Return type

[**RecipientTransferDetails**](RecipientTransferDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of the accepted transfer. |  -  |
| **0** | Unexpected error. |  -  |

<a id="recipientTransfersDecline"></a>
# **recipientTransfersDecline**
> RecipientTransferDetails recipientTransfersDecline(transferName)

Declines the transfer with given transfer Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipientTransfersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RecipientTransfersApi apiInstance = new RecipientTransfersApi(defaultClient);
    String transferName = "transferName_example"; // String | Transfer Name.
    try {
      RecipientTransferDetails result = apiInstance.recipientTransfersDecline(transferName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipientTransfersApi#recipientTransfersDecline");
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
| **transferName** | **String**| Transfer Name. | |

### Return type

[**RecipientTransferDetails**](RecipientTransferDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of the declined transfer. |  -  |
| **0** | Unexpected error. |  -  |

<a id="recipientTransfersGet"></a>
# **recipientTransfersGet**
> RecipientTransferDetails recipientTransfersGet(transferName)

Gets the transfer with given transfer Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipientTransfersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RecipientTransfersApi apiInstance = new RecipientTransfersApi(defaultClient);
    String transferName = "transferName_example"; // String | Transfer Name.
    try {
      RecipientTransferDetails result = apiInstance.recipientTransfersGet(transferName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipientTransfersApi#recipientTransfersGet");
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
| **transferName** | **String**| Transfer Name. | |

### Return type

[**RecipientTransferDetails**](RecipientTransferDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of the transfers with given Id. |  -  |
| **0** | Unexpected error. |  -  |

<a id="recipientTransfersList"></a>
# **recipientTransfersList**
> RecipientTransferDetailsListResult recipientTransfersList()

Lists the transfers received by caller.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipientTransfersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RecipientTransfersApi apiInstance = new RecipientTransfersApi(defaultClient);
    try {
      RecipientTransferDetailsListResult result = apiInstance.recipientTransfersList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipientTransfersApi#recipientTransfersList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RecipientTransferDetailsListResult**](RecipientTransferDetailsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of transfers received by caller. |  -  |
| **0** | Unexpected error. |  -  |

