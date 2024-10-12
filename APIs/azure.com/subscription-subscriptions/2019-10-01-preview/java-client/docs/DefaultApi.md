# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**operationsList**](DefaultApi.md#operationsList) | **GET** /providers/Microsoft.Subscription/operations |  |
| [**subscriptionCancel**](DefaultApi.md#subscriptionCancel) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Subscription/cancel |  |
| [**subscriptionCreateCspSubscription**](DefaultApi.md#subscriptionCreateCspSubscription) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/providers/Microsoft.Subscription/createSubscription |  |
| [**subscriptionCreateSubscription**](DefaultApi.md#subscriptionCreateSubscription) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Subscription/createSubscription |  |
| [**subscriptionCreateSubscriptionInEnrollmentAccount**](DefaultApi.md#subscriptionCreateSubscriptionInEnrollmentAccount) | **POST** /providers/Microsoft.Billing/enrollmentAccounts/{enrollmentAccountName}/providers/Microsoft.Subscription/createSubscription |  |
| [**subscriptionEnable**](DefaultApi.md#subscriptionEnable) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Subscription/enable |  |
| [**subscriptionOperationGet**](DefaultApi.md#subscriptionOperationGet) | **GET** /providers/Microsoft.Subscription/subscriptionOperations/{operationId} |  |
| [**subscriptionRename**](DefaultApi.md#subscriptionRename) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Subscription/rename |  |


<a id="operationsList"></a>
# **operationsList**
> OperationListResult operationsList(apiVersion)



Lists all of the available Microsoft.Subscription API operations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-10-01-preview
    try {
      OperationListResult result = apiInstance.operationsList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#operationsList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-10-01-preview | |

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

<a id="subscriptionCancel"></a>
# **subscriptionCancel**
> CanceledSubscriptionId subscriptionCancel(subscriptionId, apiVersion)



The operation to cancel a subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-10-01-preview
    try {
      CanceledSubscriptionId result = apiInstance.subscriptionCancel(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subscriptionCancel");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-10-01-preview | |

### Return type

[**CanceledSubscriptionId**](CanceledSubscriptionId.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Describes the error if the operation is not successful. |  -  |

<a id="subscriptionCreateCspSubscription"></a>
# **subscriptionCreateCspSubscription**
> SubscriptionCreationResult subscriptionCreateCspSubscription(billingAccountName, customerName, apiVersion, body)



The operation to create a new CSP subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | The name of the Microsoft Customer Agreement billing account for which you want to create the subscription.
    String customerName = "customerName_example"; // String | The name of the customer.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-10-01-preview
    ModernCspSubscriptionCreationParameters body = new ModernCspSubscriptionCreationParameters(); // ModernCspSubscriptionCreationParameters | The subscription creation parameters.
    try {
      SubscriptionCreationResult result = apiInstance.subscriptionCreateCspSubscription(billingAccountName, customerName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subscriptionCreateCspSubscription");
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
| **billingAccountName** | **String**| The name of the Microsoft Customer Agreement billing account for which you want to create the subscription. | |
| **customerName** | **String**| The name of the customer. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-10-01-preview | |
| **body** | [**ModernCspSubscriptionCreationParameters**](ModernCspSubscriptionCreationParameters.md)| The subscription creation parameters. | |

### Return type

[**SubscriptionCreationResult**](SubscriptionCreationResult.md)

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

<a id="subscriptionCreateSubscription"></a>
# **subscriptionCreateSubscription**
> SubscriptionCreationResult subscriptionCreateSubscription(billingAccountName, billingProfileName, invoiceSectionName, apiVersion, body)



The operation to create a new WebDirect or EA Azure subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | The name of the Microsoft Customer Agreement billing account for which you want to create the subscription.
    String billingProfileName = "billingProfileName_example"; // String | The name of the billing profile in the billing account for which you want to create the subscription.
    String invoiceSectionName = "invoiceSectionName_example"; // String | The name of the invoice section in the billing account for which you want to create the subscription.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-10-01-preview
    ModernSubscriptionCreationParameters body = new ModernSubscriptionCreationParameters(); // ModernSubscriptionCreationParameters | The subscription creation parameters.
    try {
      SubscriptionCreationResult result = apiInstance.subscriptionCreateSubscription(billingAccountName, billingProfileName, invoiceSectionName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subscriptionCreateSubscription");
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
| **billingAccountName** | **String**| The name of the Microsoft Customer Agreement billing account for which you want to create the subscription. | |
| **billingProfileName** | **String**| The name of the billing profile in the billing account for which you want to create the subscription. | |
| **invoiceSectionName** | **String**| The name of the invoice section in the billing account for which you want to create the subscription. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-10-01-preview | |
| **body** | [**ModernSubscriptionCreationParameters**](ModernSubscriptionCreationParameters.md)| The subscription creation parameters. | |

### Return type

[**SubscriptionCreationResult**](SubscriptionCreationResult.md)

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

<a id="subscriptionCreateSubscriptionInEnrollmentAccount"></a>
# **subscriptionCreateSubscriptionInEnrollmentAccount**
> SubscriptionCreationResult subscriptionCreateSubscriptionInEnrollmentAccount(enrollmentAccountName, apiVersion, body)



Creates an Azure subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String enrollmentAccountName = "enrollmentAccountName_example"; // String | The name of the enrollment account to which the subscription will be billed.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-10-01-preview
    SubscriptionCreationParameters body = new SubscriptionCreationParameters(); // SubscriptionCreationParameters | The subscription creation parameters.
    try {
      SubscriptionCreationResult result = apiInstance.subscriptionCreateSubscriptionInEnrollmentAccount(enrollmentAccountName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subscriptionCreateSubscriptionInEnrollmentAccount");
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
| **enrollmentAccountName** | **String**| The name of the enrollment account to which the subscription will be billed. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-10-01-preview | |
| **body** | [**SubscriptionCreationParameters**](SubscriptionCreationParameters.md)| The subscription creation parameters. | |

### Return type

[**SubscriptionCreationResult**](SubscriptionCreationResult.md)

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

<a id="subscriptionEnable"></a>
# **subscriptionEnable**
> EnabledSubscriptionId subscriptionEnable(subscriptionId, apiVersion)



The operation to enable a subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-10-01-preview
    try {
      EnabledSubscriptionId result = apiInstance.subscriptionEnable(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subscriptionEnable");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-10-01-preview | |

### Return type

[**EnabledSubscriptionId**](EnabledSubscriptionId.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Describes the error if the operation is not successful. |  -  |

<a id="subscriptionOperationGet"></a>
# **subscriptionOperationGet**
> SubscriptionCreationResult subscriptionOperationGet(operationId, apiVersion)



Get the status of the pending Microsoft.Subscription API operations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String operationId = "operationId_example"; // String | The operation ID, which can be found from the Location field in the generate recommendation response header.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-10-01-preview
    try {
      SubscriptionCreationResult result = apiInstance.subscriptionOperationGet(operationId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subscriptionOperationGet");
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
| **operationId** | **String**| The operation ID, which can be found from the Location field in the generate recommendation response header. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-10-01-preview | |

### Return type

[**SubscriptionCreationResult**](SubscriptionCreationResult.md)

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

<a id="subscriptionRename"></a>
# **subscriptionRename**
> RenamedSubscriptionId subscriptionRename(subscriptionId, apiVersion, body)



The operation to rename a subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-10-01-preview
    SubscriptionName body = new SubscriptionName(); // SubscriptionName | Subscription Name
    try {
      RenamedSubscriptionId result = apiInstance.subscriptionRename(subscriptionId, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subscriptionRename");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-10-01-preview | |
| **body** | [**SubscriptionName**](SubscriptionName.md)| Subscription Name | |

### Return type

[**RenamedSubscriptionId**](RenamedSubscriptionId.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Describes the error if the operation is not successful. |  -  |

