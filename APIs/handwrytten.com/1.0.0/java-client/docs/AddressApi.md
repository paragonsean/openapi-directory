# AddressApi

All URIs are relative to *https://api.handwrytten.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addRecipientAddress**](AddressApi.md#addRecipientAddress) | **POST** /profile/profileAddRecipient | add a new recipient address |
| [**deleteRecipient**](AddressApi.md#deleteRecipient) | **POST** /profile/deleteRecipient | deletes an existing recipient address |
| [**recipientsList**](AddressApi.md#recipientsList) | **POST** /profile/recipientsList | list the addresses in the user&#39;s account |
| [**updateRecipient**](AddressApi.md#updateRecipient) | **POST** /profile/updateRecipient | updates an existing new recipient address |


<a id="addRecipientAddress"></a>
# **addRecipientAddress**
> AddRecipientAddress200Response addRecipientAddress(body)

add a new recipient address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    AddressApi apiInstance = new AddressApi(defaultClient);
    AddRecipientAddressRequest body = new AddRecipientAddressRequest(); // AddRecipientAddressRequest | additional parameters
    try {
      AddRecipientAddress200Response result = apiInstance.addRecipientAddress(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressApi#addRecipientAddress");
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
| **body** | [**AddRecipientAddressRequest**](AddRecipientAddressRequest.md)| additional parameters | [optional] |

### Return type

[**AddRecipientAddress200Response**](AddRecipientAddress200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="deleteRecipient"></a>
# **deleteRecipient**
> DeleteRecipient200Response deleteRecipient(body)

deletes an existing recipient address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    AddressApi apiInstance = new AddressApi(defaultClient);
    DeleteRecipientRequest body = new DeleteRecipientRequest(); // DeleteRecipientRequest | additional parameters
    try {
      DeleteRecipient200Response result = apiInstance.deleteRecipient(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressApi#deleteRecipient");
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
| **body** | [**DeleteRecipientRequest**](DeleteRecipientRequest.md)| additional parameters | |

### Return type

[**DeleteRecipient200Response**](DeleteRecipient200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="recipientsList"></a>
# **recipientsList**
> List&lt;RecipientAddress&gt; recipientsList(body)

list the addresses in the user&#39;s account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    AddressApi apiInstance = new AddressApi(defaultClient);
    RecipientsListRequest body = new RecipientsListRequest(); // RecipientsListRequest | additional parameters
    try {
      List<RecipientAddress> result = apiInstance.recipientsList(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressApi#recipientsList");
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
| **body** | [**RecipientsListRequest**](RecipientsListRequest.md)| additional parameters | |

### Return type

[**List&lt;RecipientAddress&gt;**](RecipientAddress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="updateRecipient"></a>
# **updateRecipient**
> AddRecipientAddress200Response updateRecipient(body)

updates an existing new recipient address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    AddressApi apiInstance = new AddressApi(defaultClient);
    UpdateRecipientRequest body = new UpdateRecipientRequest(); // UpdateRecipientRequest | additional parameters
    try {
      AddRecipientAddress200Response result = apiInstance.updateRecipient(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressApi#updateRecipient");
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
| **body** | [**UpdateRecipientRequest**](UpdateRecipientRequest.md)| additional parameters | |

### Return type

[**AddRecipientAddress200Response**](AddRecipientAddress200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

