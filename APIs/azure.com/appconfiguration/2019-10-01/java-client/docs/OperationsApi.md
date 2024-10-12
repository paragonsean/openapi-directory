# OperationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**operationsCheckNameAvailability**](OperationsApi.md#operationsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.AppConfiguration/checkNameAvailability |  |
| [**operationsList**](OperationsApi.md#operationsList) | **GET** /providers/Microsoft.AppConfiguration/operations |  |


<a id="operationsCheckNameAvailability"></a>
# **operationsCheckNameAvailability**
> NameAvailabilityStatus operationsCheckNameAvailability(subscriptionId, apiVersion, checkNameAvailabilityParameters)



Checks whether the configuration store name is available for use.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OperationsApi apiInstance = new OperationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    CheckNameAvailabilityParameters checkNameAvailabilityParameters = new CheckNameAvailabilityParameters(); // CheckNameAvailabilityParameters | The object containing information for the availability request.
    try {
      NameAvailabilityStatus result = apiInstance.operationsCheckNameAvailability(subscriptionId, apiVersion, checkNameAvailabilityParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationsApi#operationsCheckNameAvailability");
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |
| **checkNameAvailabilityParameters** | [**CheckNameAvailabilityParameters**](CheckNameAvailabilityParameters.md)| The object containing information for the availability request. | |

### Return type

[**NameAvailabilityStatus**](NameAvailabilityStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="operationsList"></a>
# **operationsList**
> OperationDefinitionListResult operationsList(apiVersion, $skipToken)



Lists the operations available from this provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OperationsApi apiInstance = new OperationsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String $skipToken = "$skipToken_example"; // String | A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls.
    try {
      OperationDefinitionListResult result = apiInstance.operationsList(apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationsApi#operationsList");
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
| **apiVersion** | **String**| The client API version. | |
| **$skipToken** | **String**| A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls. | [optional] |

### Return type

[**OperationDefinitionListResult**](OperationDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed |  -  |

