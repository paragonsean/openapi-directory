# ProvidersApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllProviders**](ProvidersApi.md#getAllProviders) | **GET** /providers | Get Providers |
| [**getProvider**](ProvidersApi.md#getProvider) | **GET** /providers/{providerId} | Get Provider Details |
| [**getProvidersCount**](ProvidersApi.md#getProvidersCount) | **GET** /providers/count | Get Providers Count |


<a id="getAllProviders"></a>
# **getAllProviders**
> ProviderResponse getAllProviders(capability, dataset$filter, fullAccountNumberFields, institutionId, name, priority, providerId, skip, top)

Get Providers

The get provider service is used to get all the providers that are enabled, search a provider service by name or routing number and get popular sites of a region. &lt;br&gt;Searching for a provider using a routing number is applicable only to the USA and Canada regions.&lt;br&gt;The valid values for priority are: &lt;br&gt;   1. cobrand: Returns providers enabled for the cobrand (Default priority)&lt;br&gt;   2. popular: Returns providers popular among users of the customer&lt;br&gt;&lt;br&gt;Only the datasets, attributes, and containers that are enabled for the customer will be returned in the response.&lt;br&gt;Input for the dataset$filter should adhere to the following expression:&lt;br&gt;&lt;dataset.name&gt;[&lt;attribute.name&gt;.container[&lt;container&gt; OR &lt;container&gt;] OR &lt;attribute.name&gt;.container[&lt;container&gt;]] &lt;br&gt;OR &lt;dataset.name&gt;[&lt;attribute.name&gt; OR &lt;attribute.name&gt;]&lt;br&gt;&lt;b&gt;dataset$filter value examples:&lt;/b&gt;&lt;br&gt;ACCT_PROFILE[FULL_ACCT_NUMBER.container[bank OR investment OR creditCard]]&lt;br&gt;ACCT_PROFILE[FULL_ACCT_NUMBER.container[bank]]&lt;br&gt;BASIC_AGG_DATA[ACCOUNT_DETAILS.container[bank OR investment] OR HOLDINGS.container[bank]] OR ACCT_PROFILE[FULL_ACCT_NUMBER.container[bank]]&lt;br&gt;BASIC_AGG_DATA&lt;br&gt;BASIC_AGG_DATA OR ACCT_PROFILE&lt;br&gt;BASIC_AGG_DATA [ ACCOUNT_DETAILS OR HOLDINGS ]&lt;br&gt;BASIC_AGG_DATA [ ACCOUNT_DETAILS] OR DOCUMENT &lt;br&gt;BASIC_AGG_DATA [ BASIC_ACCOUNT_INFO OR ACCOUNT_DETAILS ] &lt;br&gt;&lt;br&gt;The fullAcountNumberFields is specified to filter the providers that have paymentAccountNumber or unmaskedAccountNumber support in the FULL_ACCT_NUMBER dataset attribute.&lt;br&gt;&lt;b&gt;Examples for usage of fullAccountNumberFields &lt;/b&gt;&lt;br&gt;dataset$filter&#x3D;ACCT_PROFILE[ FULL_ACCT_NUMBER.container [ bank ]] &amp;amp; fullAccountNumberFields&#x3D;paymentAccountNumber&lt;br&gt;dataset$filter&#x3D;ACCT_PROFILE[ FULL_ACCT_NUMBER.container [ bank ]] &amp;amp; fullAccountNumberFields&#x3D;unmaskedAccountNumber&lt;br&gt;dataset$filter&#x3D;ACCT_PROFILE[ FULL_ACCT_NUMBER.container [ bank ]] &amp;amp; fullAccountNumberFields&#x3D;unmaskedAccountNumber,paymentAccountNumber&lt;br&gt;&lt;br&gt;The skip and top parameters are used for pagination. In the skip and top parameters, pass the number of records to be skipped and retrieved, respectively.&lt;br&gt;The response header provides the links to retrieve the next and previous set of transactions.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;ol&gt;&lt;li&gt;In a product flow involving user interaction, Yodlee recommends invoking this service with filters.&lt;li&gt;Without filters, the service may perform slowly as it takes a few minutes to return data in the response.&lt;li&gt;The AuthParameter appears in the response only in case of token-based aggregation sites.&lt;li&gt;The pagination feature only applies when the priority parameter is set as cobrand. If no values are provided in the skip and top parameters, the API will only return the first 500 records.&lt;li&gt;This service supports the localization feature and accepts locale as a header parameter.&lt;li&gt;The capability has been deprecated in query parameter and response.&lt;/li&gt;&lt;/ol&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ProvidersApi apiInstance = new ProvidersApi(defaultClient);
    String capability = "capability_example"; // String | CHALLENGE_DEPOSIT_VERIFICATION - capability search is deprecated
    String dataset$filter = "dataset$filter_example"; // String | Expression to filter the providers by dataset(s) or dataset attribute(s). The default value will be the dataset or dataset attributes configured as default for the customer.
    String fullAccountNumberFields = "fullAccountNumberFields_example"; // String | Specify to filter the providers with values paymentAccountNumber,unmaskedAccountNumber.
    Long institutionId = 56L; // Long | Institution Id for Single site selection
    String name = "name_example"; // String | Name in minimum 1 character or routing number.
    String priority = "priority_example"; // String | Search priority
    String providerId = "providerId_example"; // String | Max 5 Comma seperated Provider Ids
    Integer skip = 56; // Integer | skip (Min 0) - This is not applicable along with 'name' parameter.
    Integer top = 56; // Integer | top (Max 500) - This is not applicable along with 'name' parameter.
    try {
      ProviderResponse result = apiInstance.getAllProviders(capability, dataset$filter, fullAccountNumberFields, institutionId, name, priority, providerId, skip, top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvidersApi#getAllProviders");
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
| **capability** | **String**| CHALLENGE_DEPOSIT_VERIFICATION - capability search is deprecated | [optional] |
| **dataset$filter** | **String**| Expression to filter the providers by dataset(s) or dataset attribute(s). The default value will be the dataset or dataset attributes configured as default for the customer. | [optional] |
| **fullAccountNumberFields** | **String**| Specify to filter the providers with values paymentAccountNumber,unmaskedAccountNumber. | [optional] |
| **institutionId** | **Long**| Institution Id for Single site selection | [optional] |
| **name** | **String**| Name in minimum 1 character or routing number. | [optional] |
| **priority** | **String**| Search priority | [optional] |
| **providerId** | **String**| Max 5 Comma seperated Provider Ids | [optional] |
| **skip** | **Integer**| skip (Min 0) - This is not applicable along with &#39;name&#39; parameter. | [optional] |
| **top** | **Integer**| top (Max 500) - This is not applicable along with &#39;name&#39; parameter. | [optional] |

### Return type

[**ProviderResponse**](ProviderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y800 : Invalid value for priority&lt;br&gt;Y800 : Invalid value for providerName&lt;br&gt;Y801 : Invalid length for a site search. The search string must have atleast 1 character&lt;br&gt;Y800 : Invalid value for skip&lt;br&gt;Y804 : Permitted values of top between 1 - 500&lt;br&gt;Y821 : Dataset not supported&lt;br&gt;Y820 : The additionalDataSet is not supported for Get provider API |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getProvider"></a>
# **getProvider**
> ProviderDetailResponse getProvider(providerId)

Get Provider Details

The get provider detail service is used to get detailed information including the login form for a provider.&lt;br&gt;The response is a provider object that includes information such as name of the provider, &lt;br&gt;provider&#39;s base URL, a list of containers supported by the provider, the login form details of the provider, etc.&lt;br&gt;Only enabled datasets, attributes and containers gets returned in the response.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;li&gt;This service supports the localization feature and accepts locale as a header parameter.&lt;li&gt;The capability has been deprecated in the response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ProvidersApi apiInstance = new ProvidersApi(defaultClient);
    Long providerId = 56L; // Long | providerId
    try {
      ProviderDetailResponse result = apiInstance.getProvider(providerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvidersApi#getProvider");
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
| **providerId** | **Long**| providerId | |

### Return type

[**ProviderDetailResponse**](ProviderDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y800 : Invalid value for providerId |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getProvidersCount"></a>
# **getProvidersCount**
> ProvidersCountResponse getProvidersCount(capability, dataset$filter, fullAccountNumberFields, name, priority)

Get Providers Count

The count service provides the total number of providers that get returned in the GET /providers depending on the input parameters passed.&lt;br&gt;If you are implementing pagination for providers, call this endpoint before calling GET /providers to know the number of providers that are returned for the input parameters passed.&lt;br&gt;The functionality of the input parameters remains the same as that of the GET /providers endpoint&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;li&gt;The capability has been deprecated in the query parameter.&lt;/li&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ProvidersApi apiInstance = new ProvidersApi(defaultClient);
    String capability = "capability_example"; // String | CHALLENGE_DEPOSIT_VERIFICATION - capability search is deprecated
    String dataset$filter = "dataset$filter_example"; // String | Expression to filter the providers by dataset(s) or dataset attribute(s). The default value will be the dataset or dataset attributes configured as default for the customer.
    String fullAccountNumberFields = "fullAccountNumberFields_example"; // String | Specify to filter the providers with values paymentAccountNumber,unmaskedAccountNumber.
    String name = "name_example"; // String | Name in minimum 1 character or routing number.
    String priority = "priority_example"; // String | Search priority
    try {
      ProvidersCountResponse result = apiInstance.getProvidersCount(capability, dataset$filter, fullAccountNumberFields, name, priority);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvidersApi#getProvidersCount");
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
| **capability** | **String**| CHALLENGE_DEPOSIT_VERIFICATION - capability search is deprecated | [optional] |
| **dataset$filter** | **String**| Expression to filter the providers by dataset(s) or dataset attribute(s). The default value will be the dataset or dataset attributes configured as default for the customer. | [optional] |
| **fullAccountNumberFields** | **String**| Specify to filter the providers with values paymentAccountNumber,unmaskedAccountNumber. | [optional] |
| **name** | **String**| Name in minimum 1 character or routing number. | [optional] |
| **priority** | **String**| Search priority | [optional] |

### Return type

[**ProvidersCountResponse**](ProvidersCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y800 : Invalid value for priority&lt;br&gt;Y800 : Invalid value for providerName&lt;br&gt;Y801 : Invalid length for a site search. The search string must have at least 1 character&lt;br&gt;Y800 : Invalid value for skip&lt;br&gt;Y804 : Permitted values of top between 1 - 500&lt;br&gt;Y821 : Dataset not supported&lt;br&gt;Y820 : The additionalDataSet is not supported for Get provider API |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

