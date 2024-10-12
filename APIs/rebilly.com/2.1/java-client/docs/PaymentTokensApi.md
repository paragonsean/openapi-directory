# PaymentTokensApi

All URIs are relative to *https://api-sandbox.rebilly.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getToken**](PaymentTokensApi.md#getToken) | **GET** /tokens/{token} | Retrieve a token |
| [**getTokenCollection**](PaymentTokensApi.md#getTokenCollection) | **GET** /tokens | Retrieve a list of tokens |
| [**postDigitalWalletValidation**](PaymentTokensApi.md#postDigitalWalletValidation) | **POST** /digital-wallets/validation | Validate a digital wallet session |
| [**postToken**](PaymentTokensApi.md#postToken) | **POST** /tokens | Create a payment token |


<a id="getToken"></a>
# **getToken**
> CompositeToken getToken(token, organizationId)

Retrieve a token

Retrieve a token with specified identifier string. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentTokensApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: PublishableApiKey
    ApiKeyAuth PublishableApiKey = (ApiKeyAuth) defaultClient.getAuthentication("PublishableApiKey");
    PublishableApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //PublishableApiKey.setApiKeyPrefix("Token");

    PaymentTokensApi apiInstance = new PaymentTokensApi(defaultClient);
    String token = "token_example"; // String | The token identifier string.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      CompositeToken result = apiInstance.getToken(token, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentTokensApi#getToken");
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
| **token** | **String**| The token identifier string. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**CompositeToken**](CompositeToken.md)

### Authorization

[PublishableApiKey](../README.md#PublishableApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Token was retrieved successfully. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |

<a id="getTokenCollection"></a>
# **getTokenCollection**
> List&lt;CompositeToken&gt; getTokenCollection(organizationId, limit, offset)

Retrieve a list of tokens

Retrieve a list of tokens. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentTokensApi;

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

    PaymentTokensApi apiInstance = new PaymentTokensApi(defaultClient);
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    Integer limit = 56; // Integer | The collection items limit.
    Integer offset = 56; // Integer | The collection items offset.
    try {
      List<CompositeToken> result = apiInstance.getTokenCollection(organizationId, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentTokensApi#getTokenCollection");
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

### Return type

[**List&lt;CompositeToken&gt;**](CompositeToken.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of tokens was retrieved successfully. |  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |

<a id="postDigitalWalletValidation"></a>
# **postDigitalWalletValidation**
> DigitalWalletValidation postDigitalWalletValidation(digitalWalletValidation)

Validate a digital wallet session

[FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is the recommended way to use when validating a digital wallet session. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentTokensApi;

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

    // Configure API key authorization: PublishableApiKey
    ApiKeyAuth PublishableApiKey = (ApiKeyAuth) defaultClient.getAuthentication("PublishableApiKey");
    PublishableApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //PublishableApiKey.setApiKeyPrefix("Token");

    PaymentTokensApi apiInstance = new PaymentTokensApi(defaultClient);
    DigitalWalletValidation digitalWalletValidation = new DigitalWalletValidation(); // DigitalWalletValidation | Digital wallet validation request.
    try {
      DigitalWalletValidation result = apiInstance.postDigitalWalletValidation(digitalWalletValidation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentTokensApi#postDigitalWalletValidation");
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
| **digitalWalletValidation** | [**DigitalWalletValidation**](DigitalWalletValidation.md)| Digital wallet validation request. | |

### Return type

[**DigitalWalletValidation**](DigitalWalletValidation.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT), [PublishableApiKey](../README.md#PublishableApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Digital wallet validation was made. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **422** | Invalid data was sent. |  -  |

<a id="postToken"></a>
# **postToken**
> CompositeToken postToken(compositeToken, organizationId)

Create a payment token

[FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is the recommended way to create a payment token because it minimizes PCI DSS compliance.  Once a payment token is created, it can only be used once.  A payment token expires upon first use or within 30 minutes of the token creation (whichever comes first). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentTokensApi;

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

    // Configure API key authorization: PublishableApiKey
    ApiKeyAuth PublishableApiKey = (ApiKeyAuth) defaultClient.getAuthentication("PublishableApiKey");
    PublishableApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //PublishableApiKey.setApiKeyPrefix("Token");

    PaymentTokensApi apiInstance = new PaymentTokensApi(defaultClient);
    CompositeToken compositeToken = new CompositeToken(); // CompositeToken | PaymentToken resource.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      CompositeToken result = apiInstance.postToken(compositeToken, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentTokensApi#postToken");
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
| **compositeToken** | [**CompositeToken**](CompositeToken.md)| PaymentToken resource. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**CompositeToken**](CompositeToken.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT), [PublishableApiKey](../README.md#PublishableApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Token was created. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **422** | Invalid data was sent. |  -  |

