# SubscriptionDefinitionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**subscriptionDefinitionsCreate**](SubscriptionDefinitionsApi.md#subscriptionDefinitionsCreate) | **PUT** /providers/Microsoft.Subscription/subscriptionDefinitions/{subscriptionDefinitionName} |  |
| [**subscriptionDefinitionsGet**](SubscriptionDefinitionsApi.md#subscriptionDefinitionsGet) | **GET** /providers/Microsoft.Subscription/subscriptionDefinitions/{subscriptionDefinitionName} |  |
| [**subscriptionDefinitionsGetOperationStatus**](SubscriptionDefinitionsApi.md#subscriptionDefinitionsGetOperationStatus) | **GET** /providers/Microsoft.Subscription/subscriptionOperations/{operationId} |  |
| [**subscriptionDefinitionsList**](SubscriptionDefinitionsApi.md#subscriptionDefinitionsList) | **GET** /providers/Microsoft.Subscription/subscriptionDefinitions |  |
| [**subscriptionDefinitionsOperationMetadataList**](SubscriptionDefinitionsApi.md#subscriptionDefinitionsOperationMetadataList) | **GET** /providers/Microsoft.Subscription/operations |  |


<a id="subscriptionDefinitionsCreate"></a>
# **subscriptionDefinitionsCreate**
> SubscriptionDefinition subscriptionDefinitionsCreate(subscriptionDefinitionName, apiVersion, body)



Create an Azure subscription definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SubscriptionDefinitionsApi apiInstance = new SubscriptionDefinitionsApi(defaultClient);
    String subscriptionDefinitionName = "subscriptionDefinitionName_example"; // String | The name of the Azure subscription definition.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    SubscriptionDefinition body = new SubscriptionDefinition(); // SubscriptionDefinition | The subscription definition creation.
    try {
      SubscriptionDefinition result = apiInstance.subscriptionDefinitionsCreate(subscriptionDefinitionName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionDefinitionsApi#subscriptionDefinitionsCreate");
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
| **subscriptionDefinitionName** | **String**| The name of the Azure subscription definition. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |
| **body** | [**SubscriptionDefinition**](SubscriptionDefinition.md)| The subscription definition creation. | |

### Return type

[**SubscriptionDefinition**](SubscriptionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Normal response for a successful query. The response body will contain the data that matches the filters specified in the query parameters. |  -  |
| **202** | Accepted. Subscription creation is in progress. |  * Retry-After - The amount of delay to use while the status of the operation is checked. The value is expressed in seconds. <br>  * Location - The URL where the status of the asynchronous operation can be checked. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="subscriptionDefinitionsGet"></a>
# **subscriptionDefinitionsGet**
> SubscriptionDefinition subscriptionDefinitionsGet(subscriptionDefinitionName, apiVersion)



Get an Azure subscription definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SubscriptionDefinitionsApi apiInstance = new SubscriptionDefinitionsApi(defaultClient);
    String subscriptionDefinitionName = "subscriptionDefinitionName_example"; // String | The name of the Azure subscription definition.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    try {
      SubscriptionDefinition result = apiInstance.subscriptionDefinitionsGet(subscriptionDefinitionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionDefinitionsApi#subscriptionDefinitionsGet");
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
| **subscriptionDefinitionName** | **String**| The name of the Azure subscription definition. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |

### Return type

[**SubscriptionDefinition**](SubscriptionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Normal response for a successful query. The response body will contain the data that matches the filters specified in the query parameters. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="subscriptionDefinitionsGetOperationStatus"></a>
# **subscriptionDefinitionsGetOperationStatus**
> SubscriptionDefinition subscriptionDefinitionsGetOperationStatus(apiVersion, operationId)



Retrieves the status of the subscription definition PUT operation. The URI of this API is returned in the Location field of the response header.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SubscriptionDefinitionsApi apiInstance = new SubscriptionDefinitionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    UUID operationId = UUID.randomUUID(); // UUID | The operation ID, which can be found from the Location field in the generate recommendation response header.
    try {
      SubscriptionDefinition result = apiInstance.subscriptionDefinitionsGetOperationStatus(apiVersion, operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionDefinitionsApi#subscriptionDefinitionsGetOperationStatus");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |
| **operationId** | **UUID**| The operation ID, which can be found from the Location field in the generate recommendation response header. | |

### Return type

[**SubscriptionDefinition**](SubscriptionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful completion of the asynchronous operation |  -  |
| **202** | Accepted. Subscription update is in progress. |  * Retry-After - The amount of delay to use while the status of the operation is checked. The value is expressed in seconds. <br>  * Location - The URL where the status of the asynchronous operation can be checked. <br>  |

<a id="subscriptionDefinitionsList"></a>
# **subscriptionDefinitionsList**
> SubscriptionDefinitionList subscriptionDefinitionsList(apiVersion)



List an Azure subscription definition by subscriptionId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SubscriptionDefinitionsApi apiInstance = new SubscriptionDefinitionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    try {
      SubscriptionDefinitionList result = apiInstance.subscriptionDefinitionsList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionDefinitionsApi#subscriptionDefinitionsList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |

### Return type

[**SubscriptionDefinitionList**](SubscriptionDefinitionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Normal response for a successful query. The response body will contain the data that matches the filters specified in the query parameters. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="subscriptionDefinitionsOperationMetadataList"></a>
# **subscriptionDefinitionsOperationMetadataList**
> OperationListResult subscriptionDefinitionsOperationMetadataList(apiVersion)



Lists all of the available Microsoft.Subscription API operations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SubscriptionDefinitionsApi apiInstance = new SubscriptionDefinitionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    try {
      OperationListResult result = apiInstance.subscriptionDefinitionsOperationMetadataList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionDefinitionsApi#subscriptionDefinitionsOperationMetadataList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |

### Return type

[**OperationListResult**](OperationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

