# AccountHoldersApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postACCOUNTHOLDERCREATED**](AccountHoldersApi.md#postACCOUNTHOLDERCREATED) | **POST** /ACCOUNT_HOLDER_CREATED | Account holder created |
| [**postACCOUNTHOLDERSTATUSCHANGE**](AccountHoldersApi.md#postACCOUNTHOLDERSTATUSCHANGE) | **POST** /ACCOUNT_HOLDER_STATUS_CHANGE | Account holder status changed |
| [**postACCOUNTHOLDERSTORESTATUSCHANGE**](AccountHoldersApi.md#postACCOUNTHOLDERSTORESTATUSCHANGE) | **POST** /ACCOUNT_HOLDER_STORE_STATUS_CHANGE | Store status changed |
| [**postACCOUNTHOLDERUPCOMINGDEADLINE**](AccountHoldersApi.md#postACCOUNTHOLDERUPCOMINGDEADLINE) | **POST** /ACCOUNT_HOLDER_UPCOMING_DEADLINE | Upcoming deadline |
| [**postACCOUNTHOLDERUPDATED**](AccountHoldersApi.md#postACCOUNTHOLDERUPDATED) | **POST** /ACCOUNT_HOLDER_UPDATED | Account holder updated |
| [**postACCOUNTHOLDERVERIFICATION**](AccountHoldersApi.md#postACCOUNTHOLDERVERIFICATION) | **POST** /ACCOUNT_HOLDER_VERIFICATION | Verification results received |


<a id="postACCOUNTHOLDERCREATED"></a>
# **postACCOUNTHOLDERCREATED**
> NotificationResponse postACCOUNTHOLDERCREATED(accountHolderCreateNotification)

Account holder created

Adyen sends this webhook when [an account holder is created](https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccountHolder).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountHoldersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    AccountHoldersApi apiInstance = new AccountHoldersApi(defaultClient);
    AccountHolderCreateNotification accountHolderCreateNotification = new AccountHolderCreateNotification(); // AccountHolderCreateNotification | 
    try {
      NotificationResponse result = apiInstance.postACCOUNTHOLDERCREATED(accountHolderCreateNotification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountHoldersApi#postACCOUNTHOLDERCREATED");
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
| **accountHolderCreateNotification** | [**AccountHolderCreateNotification**](AccountHolderCreateNotification.md)|  | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

<a id="postACCOUNTHOLDERSTATUSCHANGE"></a>
# **postACCOUNTHOLDERSTATUSCHANGE**
> NotificationResponse postACCOUNTHOLDERSTATUSCHANGE(accountHolderStatusChangeNotification)

Account holder status changed

Adyen sends this webhook when [the status of an account holder is changed](https://docs.adyen.com/api-explorer/#/Account/latest/post/updateAccountHolderState).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountHoldersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    AccountHoldersApi apiInstance = new AccountHoldersApi(defaultClient);
    AccountHolderStatusChangeNotification accountHolderStatusChangeNotification = new AccountHolderStatusChangeNotification(); // AccountHolderStatusChangeNotification | 
    try {
      NotificationResponse result = apiInstance.postACCOUNTHOLDERSTATUSCHANGE(accountHolderStatusChangeNotification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountHoldersApi#postACCOUNTHOLDERSTATUSCHANGE");
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
| **accountHolderStatusChangeNotification** | [**AccountHolderStatusChangeNotification**](AccountHolderStatusChangeNotification.md)|  | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

<a id="postACCOUNTHOLDERSTORESTATUSCHANGE"></a>
# **postACCOUNTHOLDERSTORESTATUSCHANGE**
> NotificationResponse postACCOUNTHOLDERSTORESTATUSCHANGE(accountHolderStoreStatusChangeNotification)

Store status changed

Adyen sends this webhook when [the status of a store](https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccountHolder__reqParam_accountHolderDetails-storeDetails-status) associated with an account holder is changed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountHoldersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    AccountHoldersApi apiInstance = new AccountHoldersApi(defaultClient);
    AccountHolderStoreStatusChangeNotification accountHolderStoreStatusChangeNotification = new AccountHolderStoreStatusChangeNotification(); // AccountHolderStoreStatusChangeNotification | 
    try {
      NotificationResponse result = apiInstance.postACCOUNTHOLDERSTORESTATUSCHANGE(accountHolderStoreStatusChangeNotification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountHoldersApi#postACCOUNTHOLDERSTORESTATUSCHANGE");
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
| **accountHolderStoreStatusChangeNotification** | [**AccountHolderStoreStatusChangeNotification**](AccountHolderStoreStatusChangeNotification.md)|  | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

<a id="postACCOUNTHOLDERUPCOMINGDEADLINE"></a>
# **postACCOUNTHOLDERUPCOMINGDEADLINE**
> NotificationResponse postACCOUNTHOLDERUPCOMINGDEADLINE(accountHolderUpcomingDeadlineNotification)

Upcoming deadline

Adyen sends this notification when an account holder&#39;s deadline to fulfill the requirements of a specific event is coming up.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountHoldersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    AccountHoldersApi apiInstance = new AccountHoldersApi(defaultClient);
    AccountHolderUpcomingDeadlineNotification accountHolderUpcomingDeadlineNotification = new AccountHolderUpcomingDeadlineNotification(); // AccountHolderUpcomingDeadlineNotification | 
    try {
      NotificationResponse result = apiInstance.postACCOUNTHOLDERUPCOMINGDEADLINE(accountHolderUpcomingDeadlineNotification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountHoldersApi#postACCOUNTHOLDERUPCOMINGDEADLINE");
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
| **accountHolderUpcomingDeadlineNotification** | [**AccountHolderUpcomingDeadlineNotification**](AccountHolderUpcomingDeadlineNotification.md)|  | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

<a id="postACCOUNTHOLDERUPDATED"></a>
# **postACCOUNTHOLDERUPDATED**
> NotificationResponse postACCOUNTHOLDERUPDATED(accountHolderUpdateNotification)

Account holder updated

Adyen sends this webhook when [an account holder is updated](https://docs.adyen.com/api-explorer/#/Account/latest/post/updateAccountHolder).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountHoldersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    AccountHoldersApi apiInstance = new AccountHoldersApi(defaultClient);
    AccountHolderUpdateNotification accountHolderUpdateNotification = new AccountHolderUpdateNotification(); // AccountHolderUpdateNotification | 
    try {
      NotificationResponse result = apiInstance.postACCOUNTHOLDERUPDATED(accountHolderUpdateNotification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountHoldersApi#postACCOUNTHOLDERUPDATED");
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
| **accountHolderUpdateNotification** | [**AccountHolderUpdateNotification**](AccountHolderUpdateNotification.md)|  | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

<a id="postACCOUNTHOLDERVERIFICATION"></a>
# **postACCOUNTHOLDERVERIFICATION**
> NotificationResponse postACCOUNTHOLDERVERIFICATION(accountHolderVerificationNotification)

Verification results received

Adyen sends this webhook when verification results are available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountHoldersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    AccountHoldersApi apiInstance = new AccountHoldersApi(defaultClient);
    AccountHolderVerificationNotification accountHolderVerificationNotification = new AccountHolderVerificationNotification(); // AccountHolderVerificationNotification | 
    try {
      NotificationResponse result = apiInstance.postACCOUNTHOLDERVERIFICATION(accountHolderVerificationNotification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountHoldersApi#postACCOUNTHOLDERVERIFICATION");
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
| **accountHolderVerificationNotification** | [**AccountHolderVerificationNotification**](AccountHolderVerificationNotification.md)|  | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

