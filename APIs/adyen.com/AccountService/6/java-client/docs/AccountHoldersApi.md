# AccountHoldersApi

All URIs are relative to *https://cal-test.adyen.com/cal/services/Account/v6*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postCloseAccountHolder**](AccountHoldersApi.md#postCloseAccountHolder) | **POST** /closeAccountHolder | Close an account holder |
| [**postCloseStores**](AccountHoldersApi.md#postCloseStores) | **POST** /closeStores | Close stores |
| [**postCreateAccountHolder**](AccountHoldersApi.md#postCreateAccountHolder) | **POST** /createAccountHolder | Create an account holder |
| [**postGetAccountHolder**](AccountHoldersApi.md#postGetAccountHolder) | **POST** /getAccountHolder | Get an account holder |
| [**postGetTaxForm**](AccountHoldersApi.md#postGetTaxForm) | **POST** /getTaxForm | Get a tax form |
| [**postSuspendAccountHolder**](AccountHoldersApi.md#postSuspendAccountHolder) | **POST** /suspendAccountHolder | Suspend an account holder |
| [**postUnSuspendAccountHolder**](AccountHoldersApi.md#postUnSuspendAccountHolder) | **POST** /unSuspendAccountHolder | Unsuspend an account holder |
| [**postUpdateAccountHolder**](AccountHoldersApi.md#postUpdateAccountHolder) | **POST** /updateAccountHolder | Update an account holder |
| [**postUpdateAccountHolderState**](AccountHoldersApi.md#postUpdateAccountHolderState) | **POST** /updateAccountHolderState | Update payout or processing state |


<a id="postCloseAccountHolder"></a>
# **postCloseAccountHolder**
> CloseAccountHolderResponse postCloseAccountHolder(closeAccountHolderRequest)

Close an account holder

Changes the [status of an account holder](https://docs.adyen.com/marketplaces-and-platforms/classic/account-holders-and-accounts#account-holder-statuses) to **Closed**. This state is final. If an account holder is closed, you can&#39;t process transactions, pay out funds, or reopen it. If payments are made to an account of an account holder with a **Closed** [&#x60;status&#x60;](https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status), the payments are sent to your liable account.

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
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Account/v6");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AccountHoldersApi apiInstance = new AccountHoldersApi(defaultClient);
    CloseAccountHolderRequest closeAccountHolderRequest = new CloseAccountHolderRequest(); // CloseAccountHolderRequest | 
    try {
      CloseAccountHolderResponse result = apiInstance.postCloseAccountHolder(closeAccountHolderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountHoldersApi#postCloseAccountHolder");
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
| **closeAccountHolderRequest** | [**CloseAccountHolderRequest**](CloseAccountHolderRequest.md)|  | [optional] |

### Return type

[**CloseAccountHolderResponse**](CloseAccountHolderResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postCloseStores"></a>
# **postCloseStores**
> GenericResponse postCloseStores(closeStoresRequest)

Close stores

Closes stores associated with an account holder.

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
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Account/v6");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AccountHoldersApi apiInstance = new AccountHoldersApi(defaultClient);
    CloseStoresRequest closeStoresRequest = new CloseStoresRequest(); // CloseStoresRequest | 
    try {
      GenericResponse result = apiInstance.postCloseStores(closeStoresRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountHoldersApi#postCloseStores");
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
| **closeStoresRequest** | [**CloseStoresRequest**](CloseStoresRequest.md)|  | [optional] |

### Return type

[**GenericResponse**](GenericResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postCreateAccountHolder"></a>
# **postCreateAccountHolder**
> CreateAccountHolderResponse postCreateAccountHolder(createAccountHolderRequest)

Create an account holder

Creates an account holder that [represents the sub-merchant&#39;s entity](https://docs.adyen.com/marketplaces-and-platforms/classic/account-structure#your-platform) in your platform. The details that you need to provide in the request depend on the sub-merchant&#39;s legal entity type. For more information, refer to [Account holder and accounts](https://docs.adyen.com/marketplaces-and-platforms/classic/account-holders-and-accounts#legal-entity-types).

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
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Account/v6");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AccountHoldersApi apiInstance = new AccountHoldersApi(defaultClient);
    CreateAccountHolderRequest createAccountHolderRequest = new CreateAccountHolderRequest(); // CreateAccountHolderRequest | 
    try {
      CreateAccountHolderResponse result = apiInstance.postCreateAccountHolder(createAccountHolderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountHoldersApi#postCreateAccountHolder");
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
| **createAccountHolderRequest** | [**CreateAccountHolderRequest**](CreateAccountHolderRequest.md)|  | [optional] |

### Return type

[**CreateAccountHolderResponse**](CreateAccountHolderResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postGetAccountHolder"></a>
# **postGetAccountHolder**
> GetAccountHolderResponse postGetAccountHolder(getAccountHolderRequest)

Get an account holder

Returns the details of an account holder.

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
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Account/v6");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AccountHoldersApi apiInstance = new AccountHoldersApi(defaultClient);
    GetAccountHolderRequest getAccountHolderRequest = new GetAccountHolderRequest(); // GetAccountHolderRequest | 
    try {
      GetAccountHolderResponse result = apiInstance.postGetAccountHolder(getAccountHolderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountHoldersApi#postGetAccountHolder");
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
| **getAccountHolderRequest** | [**GetAccountHolderRequest**](GetAccountHolderRequest.md)|  | [optional] |

### Return type

[**GetAccountHolderResponse**](GetAccountHolderResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postGetTaxForm"></a>
# **postGetTaxForm**
> GetTaxFormResponse postGetTaxForm(getTaxFormRequest)

Get a tax form

Generates a tax form for account holders operating in the US. For more information, refer to [Providing tax forms](https://docs.adyen.com/marketplaces-and-platforms/classic/tax-forms).

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
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Account/v6");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AccountHoldersApi apiInstance = new AccountHoldersApi(defaultClient);
    GetTaxFormRequest getTaxFormRequest = new GetTaxFormRequest(); // GetTaxFormRequest | 
    try {
      GetTaxFormResponse result = apiInstance.postGetTaxForm(getTaxFormRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountHoldersApi#postGetTaxForm");
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
| **getTaxFormRequest** | [**GetTaxFormRequest**](GetTaxFormRequest.md)|  | [optional] |

### Return type

[**GetTaxFormResponse**](GetTaxFormResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postSuspendAccountHolder"></a>
# **postSuspendAccountHolder**
> SuspendAccountHolderResponse postSuspendAccountHolder(suspendAccountHolderRequest)

Suspend an account holder

Changes the [status of an account holder](https://docs.adyen.com/marketplaces-and-platforms/classic/account-holders-and-accounts#account-holder-statuses) to **Suspended**.

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
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Account/v6");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AccountHoldersApi apiInstance = new AccountHoldersApi(defaultClient);
    SuspendAccountHolderRequest suspendAccountHolderRequest = new SuspendAccountHolderRequest(); // SuspendAccountHolderRequest | 
    try {
      SuspendAccountHolderResponse result = apiInstance.postSuspendAccountHolder(suspendAccountHolderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountHoldersApi#postSuspendAccountHolder");
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
| **suspendAccountHolderRequest** | [**SuspendAccountHolderRequest**](SuspendAccountHolderRequest.md)|  | [optional] |

### Return type

[**SuspendAccountHolderResponse**](SuspendAccountHolderResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postUnSuspendAccountHolder"></a>
# **postUnSuspendAccountHolder**
> UnSuspendAccountHolderResponse postUnSuspendAccountHolder(unSuspendAccountHolderRequest)

Unsuspend an account holder

Changes the [status of an account holder](https://docs.adyen.com/marketplaces-and-platforms/classic/account-holders-and-accounts#account-holder-statuses) from **Suspended** to **Inactive**.  Account holders can have a **Suspended** [&#x60;status&#x60;](https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status) if you suspend them through the [&#x60;/suspendAccountHolder&#x60;](https://docs.adyen.com/api-explorer/#/Account/v5/post/suspendAccountHolder) endpoint or if a verification deadline expires.  You can only unsuspend account holders if they do not have verification checks with a **FAILED** [&#x60;status&#x60;](https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status).

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
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Account/v6");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AccountHoldersApi apiInstance = new AccountHoldersApi(defaultClient);
    UnSuspendAccountHolderRequest unSuspendAccountHolderRequest = new UnSuspendAccountHolderRequest(); // UnSuspendAccountHolderRequest | 
    try {
      UnSuspendAccountHolderResponse result = apiInstance.postUnSuspendAccountHolder(unSuspendAccountHolderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountHoldersApi#postUnSuspendAccountHolder");
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
| **unSuspendAccountHolderRequest** | [**UnSuspendAccountHolderRequest**](UnSuspendAccountHolderRequest.md)|  | [optional] |

### Return type

[**UnSuspendAccountHolderResponse**](UnSuspendAccountHolderResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postUpdateAccountHolder"></a>
# **postUpdateAccountHolder**
> UpdateAccountHolderResponse postUpdateAccountHolder(updateAccountHolderRequest)

Update an account holder

Updates the &#x60;accountHolderDetails&#x60; and &#x60;processingTier&#x60; of an account holder, and adds bank accounts and shareholders.  When updating &#x60;accountHolderDetails&#x60;, parameters that are not included in the request are left unchanged except for the following object:  * &#x60;metadata&#x60;: Updating the metadata replaces the entire object. This means that to update an existing key-value pair, you must provide the changes, as well as other existing key-value pairs.  When updating any field in the following objects, you must submit all the fields required for validation:   * &#x60;address&#x60;  * &#x60;fullPhoneNumber&#x60;  * &#x60;bankAccountDetails.BankAccountDetail&#x60;  * &#x60;businessDetails.shareholders.ShareholderContact&#x60;   For example, to update the &#x60;address.postalCode&#x60;, you must also submit the &#x60;address.country&#x60;, &#x60;.city&#x60;, &#x60;.street&#x60;, &#x60;.postalCode&#x60;, and possibly &#x60;.stateOrProvince&#x60; so that the address can be validated.  To add a bank account or shareholder, provide the bank account or shareholder details without a &#x60;bankAccountUUID&#x60; or a &#x60;shareholderCode&#x60;.  

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
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Account/v6");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AccountHoldersApi apiInstance = new AccountHoldersApi(defaultClient);
    UpdateAccountHolderRequest updateAccountHolderRequest = new UpdateAccountHolderRequest(); // UpdateAccountHolderRequest | 
    try {
      UpdateAccountHolderResponse result = apiInstance.postUpdateAccountHolder(updateAccountHolderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountHoldersApi#postUpdateAccountHolder");
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
| **updateAccountHolderRequest** | [**UpdateAccountHolderRequest**](UpdateAccountHolderRequest.md)|  | [optional] |

### Return type

[**UpdateAccountHolderResponse**](UpdateAccountHolderResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postUpdateAccountHolderState"></a>
# **postUpdateAccountHolderState**
> GetAccountHolderStatusResponse postUpdateAccountHolderState(updateAccountHolderStateRequest)

Update payout or processing state

Disables or enables the processing or payout state of an account holder.

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
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Account/v6");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AccountHoldersApi apiInstance = new AccountHoldersApi(defaultClient);
    UpdateAccountHolderStateRequest updateAccountHolderStateRequest = new UpdateAccountHolderStateRequest(); // UpdateAccountHolderStateRequest | 
    try {
      GetAccountHolderStatusResponse result = apiInstance.postUpdateAccountHolderState(updateAccountHolderStateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountHoldersApi#postUpdateAccountHolderState");
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
| **updateAccountHolderStateRequest** | [**UpdateAccountHolderStateRequest**](UpdateAccountHolderStateRequest.md)|  | [optional] |

### Return type

[**GetAccountHolderStatusResponse**](GetAccountHolderStatusResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

