# BillingApi

All URIs are relative to *https://api.appcenter.ms*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**billingAggregatedInformationGetAll**](BillingApi.md#billingAggregatedInformationGetAll) | **GET** /v0.1/billing/allAccountsAggregated |  |
| [**billingAggregatedInformationGetByApp**](BillingApi.md#billingAggregatedInformationGetByApp) | **GET** /v0.1/apps/{owner_name}/{app_name}/billing/aggregated |  |
| [**billingAggregatedInformationGetForOrg**](BillingApi.md#billingAggregatedInformationGetForOrg) | **GET** /v0.1/orgs/{orgName}/billing/aggregated |  |


<a id="billingAggregatedInformationGetAll"></a>
# **billingAggregatedInformationGetAll**
> BillingAggregatedInformationGetAll200Response billingAggregatedInformationGetAll(service, period, showOriginalPlans)



Aggregated Billing Information for the requesting user and the organizations in which the user is an admin.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String service = "Test"; // String | Type of service that should be included in the Billing Information
    String period = "Previous"; // String | Type of period that should be included in the Billing Information
    Boolean showOriginalPlans = true; // Boolean | Controls whether the API should show the original plan when Azure Subscription is not enabled
    try {
      BillingAggregatedInformationGetAll200Response result = apiInstance.billingAggregatedInformationGetAll(service, period, showOriginalPlans);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingAggregatedInformationGetAll");
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
| **service** | **String**| Type of service that should be included in the Billing Information | [optional] [enum: Test, Build] |
| **period** | **String**| Type of period that should be included in the Billing Information | [optional] [enum: Previous, Current, Next] |
| **showOriginalPlans** | **Boolean**| Controls whether the API should show the original plan when Azure Subscription is not enabled | [optional] |

### Return type

[**BillingAggregatedInformationGetAll200Response**](BillingAggregatedInformationGetAll200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Aggregated Billing Information for the requesting user and the organizations in which the user is an admin. |  -  |
| **0** | Error code with reason |  -  |

<a id="billingAggregatedInformationGetByApp"></a>
# **billingAggregatedInformationGetByApp**
> BillingAggregatedInformationGetByApp200Response billingAggregatedInformationGetByApp(ownerName, appName, service, period, showOriginalPlans)



Aggregated Billing Information for owner of a given app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String service = "Test"; // String | Type of service that should be included in the Billing Information
    String period = "Previous"; // String | Type of period that should be included in the Billing Information
    Boolean showOriginalPlans = true; // Boolean | Controls whether the API should show the original plan when Azure Subscription is not enabled
    try {
      BillingAggregatedInformationGetByApp200Response result = apiInstance.billingAggregatedInformationGetByApp(ownerName, appName, service, period, showOriginalPlans);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingAggregatedInformationGetByApp");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **service** | **String**| Type of service that should be included in the Billing Information | [optional] [enum: Test, Build] |
| **period** | **String**| Type of period that should be included in the Billing Information | [optional] [enum: Previous, Current, Next] |
| **showOriginalPlans** | **Boolean**| Controls whether the API should show the original plan when Azure Subscription is not enabled | [optional] |

### Return type

[**BillingAggregatedInformationGetByApp200Response**](BillingAggregatedInformationGetByApp200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Aggregated Billing Information for owner of a given app |  -  |
| **0** | Error code with reason |  -  |

<a id="billingAggregatedInformationGetForOrg"></a>
# **billingAggregatedInformationGetForOrg**
> BillingAggregatedInformationGetByApp200Response billingAggregatedInformationGetForOrg(orgName, service, period, showOriginalPlans)



Aggregated Billing Information for a given Organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String orgName = "orgName_example"; // String | The name of the Organization
    String service = "Test"; // String | Type of service that should be included in the Billing Information
    String period = "Previous"; // String | Type of period that should be included in the Billing Information
    Boolean showOriginalPlans = true; // Boolean | Controls whether the API should show the original plan when Azure Subscription is not enabled
    try {
      BillingAggregatedInformationGetByApp200Response result = apiInstance.billingAggregatedInformationGetForOrg(orgName, service, period, showOriginalPlans);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingAggregatedInformationGetForOrg");
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
| **orgName** | **String**| The name of the Organization | |
| **service** | **String**| Type of service that should be included in the Billing Information | [optional] [enum: Test, Build] |
| **period** | **String**| Type of period that should be included in the Billing Information | [optional] [enum: Previous, Current, Next] |
| **showOriginalPlans** | **Boolean**| Controls whether the API should show the original plan when Azure Subscription is not enabled | [optional] |

### Return type

[**BillingAggregatedInformationGetByApp200Response**](BillingAggregatedInformationGetByApp200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Aggregated Billing Information for a given Organization |  -  |
| **0** | Error code with reason |  -  |

