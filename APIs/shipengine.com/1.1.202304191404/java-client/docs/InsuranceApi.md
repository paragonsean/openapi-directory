# InsuranceApi

All URIs are relative to *https://api.shipengine.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addFundsToInsurance**](InsuranceApi.md#addFundsToInsurance) | **PATCH** /v1/insurance/shipsurance/add_funds | Add Funds To Insurance |
| [**connectInsurer**](InsuranceApi.md#connectInsurer) | **POST** /v1/connections/insurance/shipsurance | Connect a Shipsurance Account |
| [**disconnectInsurer**](InsuranceApi.md#disconnectInsurer) | **DELETE** /v1/connections/insurance/shipsurance | Disconnect a Shipsurance Account |
| [**getInsuranceBalance**](InsuranceApi.md#getInsuranceBalance) | **GET** /v1/insurance/shipsurance/balance | Get Insurance Funds Balance |


<a id="addFundsToInsurance"></a>
# **addFundsToInsurance**
> AddFundsToInsuranceResponseBody addFundsToInsurance(addFundsToInsuranceRequestBody)

Add Funds To Insurance

You may need to auto fund your account from time to time. For example, if you don&#39;t normally ship items over $100, and may want to add funds to insurance rather than keeping the account funded. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsuranceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    InsuranceApi apiInstance = new InsuranceApi(defaultClient);
    AddFundsToInsuranceRequestBody addFundsToInsuranceRequestBody = new AddFundsToInsuranceRequestBody(); // AddFundsToInsuranceRequestBody | 
    try {
      AddFundsToInsuranceResponseBody result = apiInstance.addFundsToInsurance(addFundsToInsuranceRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsuranceApi#addFundsToInsurance");
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
| **addFundsToInsuranceRequestBody** | [**AddFundsToInsuranceRequestBody**](AddFundsToInsuranceRequestBody.md)|  | |

### Return type

[**AddFundsToInsuranceResponseBody**](AddFundsToInsuranceResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="connectInsurer"></a>
# **connectInsurer**
> Object connectInsurer(connectInsurerRequestBody)

Connect a Shipsurance Account

Connect a Shipsurance Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsuranceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    InsuranceApi apiInstance = new InsuranceApi(defaultClient);
    ConnectInsurerRequestBody connectInsurerRequestBody = new ConnectInsurerRequestBody(); // ConnectInsurerRequestBody | 
    try {
      Object result = apiInstance.connectInsurer(connectInsurerRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsuranceApi#connectInsurer");
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
| **connectInsurerRequestBody** | [**ConnectInsurerRequestBody**](ConnectInsurerRequestBody.md)|  | |

### Return type

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success |  -  |
| **400** | The request contained errors. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="disconnectInsurer"></a>
# **disconnectInsurer**
> Object disconnectInsurer()

Disconnect a Shipsurance Account

Disconnect a Shipsurance Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsuranceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    InsuranceApi apiInstance = new InsuranceApi(defaultClient);
    try {
      Object result = apiInstance.disconnectInsurer();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsuranceApi#disconnectInsurer");
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

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success |  -  |
| **400** | The request contained errors. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="getInsuranceBalance"></a>
# **getInsuranceBalance**
> GetInsuranceBalanceResponseBody getInsuranceBalance()

Get Insurance Funds Balance

Retrieve the balance of your Shipsurance account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsuranceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    InsuranceApi apiInstance = new InsuranceApi(defaultClient);
    try {
      GetInsuranceBalanceResponseBody result = apiInstance.getInsuranceBalance();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsuranceApi#getInsuranceBalance");
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

[**GetInsuranceBalanceResponseBody**](GetInsuranceBalanceResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

