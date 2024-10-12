# ThirdPartyTransmissionApi

All URIs are relative to *https://api.test.payrun.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteThirdPartyTransaction**](ThirdPartyTransmissionApi.md#deleteThirdPartyTransaction) | **DELETE** /Employer/{EmployerId}/ThirdPartyTransaction/{ThirdPartyTransactionId} | Delete third party transaction |
| [**getThirdPartyTransaction**](ThirdPartyTransmissionApi.md#getThirdPartyTransaction) | **GET** /Employer/{EmployerId}/ThirdPartyTransaction/{ThirdPartyTransactionId} | Get a third party transaction |
| [**getThirdPartyTransactions**](ThirdPartyTransmissionApi.md#getThirdPartyTransactions) | **GET** /Employer/{EmployerId}/ThirdPartyTransactions | Get all third party transaction links |


<a id="deleteThirdPartyTransaction"></a>
# **deleteThirdPartyTransaction**
> deleteThirdPartyTransaction(employerId, thirdPartyTransactionId, authorization, apiVersion)

Delete third party transaction

Deletes a third party transaction record from the given resource location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ThirdPartyTransmissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ThirdPartyTransmissionApi apiInstance = new ThirdPartyTransmissionApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String thirdPartyTransactionId = "thirdPartyTransactionId_example"; // String | The third party transaction unique identifier. E.g TP001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteThirdPartyTransaction(employerId, thirdPartyTransactionId, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ThirdPartyTransmissionApi#deleteThirdPartyTransaction");
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
| **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | |
| **thirdPartyTransactionId** | **String**| The third party transaction unique identifier. E.g TP001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getThirdPartyTransaction"></a>
# **getThirdPartyTransaction**
> ThirdPartyTransaction getThirdPartyTransaction(employerId, thirdPartyTransactionId, authorization, apiVersion)

Get a third party transaction

Get a third party transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ThirdPartyTransmissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ThirdPartyTransmissionApi apiInstance = new ThirdPartyTransmissionApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String thirdPartyTransactionId = "thirdPartyTransactionId_example"; // String | The third party transaction unique identifier. E.g TP001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      ThirdPartyTransaction result = apiInstance.getThirdPartyTransaction(employerId, thirdPartyTransactionId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ThirdPartyTransmissionApi#getThirdPartyTransaction");
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
| **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | |
| **thirdPartyTransactionId** | **String**| The third party transaction unique identifier. E.g TP001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**ThirdPartyTransaction**](ThirdPartyTransaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The third party transaction object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getThirdPartyTransactions"></a>
# **getThirdPartyTransactions**
> LinkCollection getThirdPartyTransactions(employerId, authorization, apiVersion)

Get all third party transaction links

Get all third party transaction links

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ThirdPartyTransmissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ThirdPartyTransmissionApi apiInstance = new ThirdPartyTransmissionApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getThirdPartyTransactions(employerId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ThirdPartyTransmissionApi#getThirdPartyTransactions");
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
| **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The link collection object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

