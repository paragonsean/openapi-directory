# BankAccountsApi

All URIs are relative to *https://api-sandbox.rebilly.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBankAccount**](BankAccountsApi.md#getBankAccount) | **GET** /bank-accounts/{id} | Retrieve a Bank Account |
| [**getBankAccountCollection**](BankAccountsApi.md#getBankAccountCollection) | **GET** /bank-accounts | Retrieve a list of bank accounts |
| [**patchBankAccount**](BankAccountsApi.md#patchBankAccount) | **PATCH** /bank-accounts/{id} | Update a bank account&#39;s values |
| [**postBankAccount**](BankAccountsApi.md#postBankAccount) | **POST** /bank-accounts | Create a Bank Account |
| [**postBankAccountDeactivation**](BankAccountsApi.md#postBankAccountDeactivation) | **POST** /bank-accounts/{id}/deactivation | Deactivate a Bank Account |
| [**putBankAccount**](BankAccountsApi.md#putBankAccount) | **PUT** /bank-accounts/{id} | Create a Bank Account with predefined ID |


<a id="getBankAccount"></a>
# **getBankAccount**
> BankAccount getBankAccount(id, organizationId)

Retrieve a Bank Account

Retrieve a Bank Account with specified identifier string. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    BankAccountsApi apiInstance = new BankAccountsApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      BankAccount result = apiInstance.getBankAccount(id, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankAccountsApi#getBankAccount");
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
| **id** | **String**| The resource identifier string. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bank Account was retrieved successfully. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |

<a id="getBankAccountCollection"></a>
# **getBankAccountCollection**
> List&lt;BankAccount&gt; getBankAccountCollection(organizationId, limit, offset, q, sort, filter, expand)

Retrieve a list of bank accounts

Retrieve a list of Bank Accounts. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    BankAccountsApi apiInstance = new BankAccountsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    Integer limit = 56; // Integer | The collection items limit.
    Integer offset = 56; // Integer | The collection items offset.
    String q = "q_example"; // String | The partial search of the text fields.
    List<String> sort = Arrays.asList(); // List<String> | The collection items sort field and order (prefix with \"-\" for descending sort).
    String filter = "filter_example"; // String | The collection items filter requires a special format. Use \",\" for multiple allowed values.  Use \";\" for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    String expand = "expand_example"; // String | Expand a response to get a full related object included inside of the `_embedded` path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    try {
      List<BankAccount> result = apiInstance.getBankAccountCollection(organizationId, limit, offset, q, sort, filter, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankAccountsApi#getBankAccountCollection");
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
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |
| **limit** | **Integer**| The collection items limit. | [optional] |
| **offset** | **Integer**| The collection items offset. | [optional] |
| **q** | **String**| The partial search of the text fields. | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). | [optional] |
| **filter** | **String**| The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  | [optional] |
| **expand** | **String**| Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  | [optional] |

### Return type

[**List&lt;BankAccount&gt;**](BankAccount.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Bank Accounts was retrieved successfully. |  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |

<a id="patchBankAccount"></a>
# **patchBankAccount**
> BankAccount patchBankAccount(id, organizationId, bankAccountUpdatePlain)

Update a bank account&#39;s values

Update bank account&#39;s values except for the account number and routing. number. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    BankAccountsApi apiInstance = new BankAccountsApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    BankAccountUpdatePlain bankAccountUpdatePlain = new BankAccountUpdatePlain(); // BankAccountUpdatePlain | Bank Account.
    try {
      BankAccount result = apiInstance.patchBankAccount(id, organizationId, bankAccountUpdatePlain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankAccountsApi#patchBankAccount");
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
| **id** | **String**| The resource identifier string. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |
| **bankAccountUpdatePlain** | [**BankAccountUpdatePlain**](BankAccountUpdatePlain.md)| Bank Account. | [optional] |

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bank Account was updated. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |
| **422** | Invalid data was sent. |  -  |

<a id="postBankAccount"></a>
# **postBankAccount**
> BankAccount postBankAccount(postBankAccountRequest, organizationId)

Create a Bank Account

Create a Bank Account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    BankAccountsApi apiInstance = new BankAccountsApi(defaultClient);
    PostBankAccountRequest postBankAccountRequest = new PostBankAccountRequest(); // PostBankAccountRequest | BankAccount resource.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      BankAccount result = apiInstance.postBankAccount(postBankAccountRequest, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankAccountsApi#postBankAccount");
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
| **postBankAccountRequest** | [**PostBankAccountRequest**](PostBankAccountRequest.md)| BankAccount resource. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Bank Account was created. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **422** | Invalid data was sent. |  -  |

<a id="postBankAccountDeactivation"></a>
# **postBankAccountDeactivation**
> BankAccount postBankAccountDeactivation(id, organizationId)

Deactivate a Bank Account

Deactivate a Bank Account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    BankAccountsApi apiInstance = new BankAccountsApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      BankAccount result = apiInstance.postBankAccountDeactivation(id, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankAccountsApi#postBankAccountDeactivation");
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
| **id** | **String**| The resource identifier string. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Bank Account was deactivated. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |
| **409** | Conflict. |  -  |

<a id="putBankAccount"></a>
# **putBankAccount**
> BankAccount putBankAccount(id, postBankAccountRequest, organizationId)

Create a Bank Account with predefined ID

Create or update a BankAccount with predefined identifier string. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    BankAccountsApi apiInstance = new BankAccountsApi(defaultClient);
    String id = "id_example"; // String | The resource identifier string.
    PostBankAccountRequest postBankAccountRequest = new PostBankAccountRequest(); // PostBankAccountRequest | BankAccount resource.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      BankAccount result = apiInstance.putBankAccount(id, postBankAccountRequest, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankAccountsApi#putBankAccount");
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
| **id** | **String**| The resource identifier string. | |
| **postBankAccountRequest** | [**PostBankAccountRequest**](PostBankAccountRequest.md)| BankAccount resource. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | BankAccount was updated. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **201** | BankAccount was created. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |
| **422** | Invalid data was sent. |  -  |

