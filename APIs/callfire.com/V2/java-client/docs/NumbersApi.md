# NumbersApi

All URIs are relative to *https://api.callfire.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**findNumberLeaseConfigs**](NumbersApi.md#findNumberLeaseConfigs) | **GET** /numbers/leases/configs | Find lease configs |
| [**findNumberLeases**](NumbersApi.md#findNumberLeases) | **GET** /numbers/leases | Find leases |
| [**findNumberRegions**](NumbersApi.md#findNumberRegions) | **GET** /numbers/regions | Find number regions |
| [**findNumbersLocal**](NumbersApi.md#findNumbersLocal) | **GET** /numbers/local | Find local numbers |
| [**findNumbersTollfree**](NumbersApi.md#findNumbersTollfree) | **GET** /numbers/tollfree | Find tollfree numbers |
| [**getNumberLease**](NumbersApi.md#getNumberLease) | **GET** /numbers/leases/{number} | Find a specific lease |
| [**getNumberLeaseConfig**](NumbersApi.md#getNumberLeaseConfig) | **GET** /numbers/leases/configs/{number} | Find a specific lease config |
| [**updateNumberLease**](NumbersApi.md#updateNumberLease) | **PUT** /numbers/leases/{number} | Update a lease |
| [**updateNumberLeaseConfig**](NumbersApi.md#updateNumberLeaseConfig) | **PUT** /numbers/leases/configs/{number} | Update a lease config |


<a id="findNumberLeaseConfigs"></a>
# **findNumberLeaseConfigs**
> NumberConfigPage findNumberLeaseConfigs(limit, offset, prefix, city, state, zipcode, labelName, fields)

Find lease configs

Searches for all number lease configs for the user. Returns a paged list of NumberConfig

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NumbersApi apiInstance = new NumbersApi(defaultClient);
    Integer limit = 100; // Integer | To set the maximum number of records to return in a paged list response. The default is 100
    Integer offset = 0; // Integer | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    String prefix = "prefix_example"; // String | A 4-7 digit prefix
    String city = "city_example"; // String | A city name
    String state = "state_example"; // String | A two-letter state code. Example: CA, IL, etc.
    String zipcode = "zipcode_example"; // String | A five-digit Zipcode
    String labelName = "labelName_example"; // String | A label name
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      NumberConfigPage result = apiInstance.findNumberLeaseConfigs(limit, offset, prefix, city, state, zipcode, labelName, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersApi#findNumberLeaseConfigs");
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
| **limit** | **Integer**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100] |
| **offset** | **Integer**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0] |
| **prefix** | **String**| A 4-7 digit prefix | [optional] |
| **city** | **String**| A city name | [optional] |
| **state** | **String**| A two-letter state code. Example: CA, IL, etc. | [optional] |
| **zipcode** | **String**| A five-digit Zipcode | [optional] |
| **labelName** | **String**| A label name | [optional] |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**NumberConfigPage**](NumberConfigPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="findNumberLeases"></a>
# **findNumberLeases**
> NumberLeasePage findNumberLeases(limit, offset, prefix, city, state, zipcode, labelName, tollFree, fields)

Find leases

Searches for all numbers leased by account user. This API is useful for finding all numbers currently owned by the user. Returns a paged list of number leases.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NumbersApi apiInstance = new NumbersApi(defaultClient);
    Integer limit = 100; // Integer | To set the maximum number of records to return in a paged list response. The default is 100
    Integer offset = 0; // Integer | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    String prefix = "prefix_example"; // String | A 4-7 digit prefix
    String city = "city_example"; // String | A city name
    String state = "state_example"; // String | A two-letter state code. Example: CA, IL, etc.
    String zipcode = "zipcode_example"; // String | A five-digit Zipcode
    String labelName = "labelName_example"; // String | A label name
    Boolean tollFree = true; // Boolean | ~
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      NumberLeasePage result = apiInstance.findNumberLeases(limit, offset, prefix, city, state, zipcode, labelName, tollFree, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersApi#findNumberLeases");
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
| **limit** | **Integer**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100] |
| **offset** | **Integer**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0] |
| **prefix** | **String**| A 4-7 digit prefix | [optional] |
| **city** | **String**| A city name | [optional] |
| **state** | **String**| A two-letter state code. Example: CA, IL, etc. | [optional] |
| **zipcode** | **String**| A five-digit Zipcode | [optional] |
| **labelName** | **String**| A label name | [optional] |
| **tollFree** | **Boolean**| ~ | [optional] |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**NumberLeasePage**](NumberLeasePage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="findNumberRegions"></a>
# **findNumberRegions**
> RegionPage findNumberRegions(limit, offset, prefix, city, cityPrefix, state, zipcode, country, fields)

Find number regions

Searches for region information. Use this API to obtain detailed region information that can be used to query for more specific phone numbers than a general query.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NumbersApi apiInstance = new NumbersApi(defaultClient);
    Integer limit = 100; // Integer | To set the maximum number of records to return in a paged list response. The default is 100
    Integer offset = 0; // Integer | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    String prefix = "prefix_example"; // String | A 4-7 digit prefix
    String city = "city_example"; // String | A city name
    String cityPrefix = "cityPrefix_example"; // String | ~
    String state = "state_example"; // String | A two-letter state code. Example: CA, IL, etc.
    String zipcode = "zipcode_example"; // String | A five-digit Zipcode
    String country = "country_example"; // String | ~
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      RegionPage result = apiInstance.findNumberRegions(limit, offset, prefix, city, cityPrefix, state, zipcode, country, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersApi#findNumberRegions");
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
| **limit** | **Integer**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100] |
| **offset** | **Integer**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0] |
| **prefix** | **String**| A 4-7 digit prefix | [optional] |
| **city** | **String**| A city name | [optional] |
| **cityPrefix** | **String**| ~ | [optional] |
| **state** | **String**| A two-letter state code. Example: CA, IL, etc. | [optional] |
| **zipcode** | **String**| A five-digit Zipcode | [optional] |
| **country** | **String**| ~ | [optional] |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**RegionPage**](RegionPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="findNumbersLocal"></a>
# **findNumbersLocal**
> NumberList findNumbersLocal(limit, prefix, city, state, zipcode, fields)

Find local numbers

Searches for numbers available for purchase in CallFire local numbers catalog . At least one additional parameter is required. User may filter local numbers by their region information. If all numbers with desirable zip code is already busy search will return available numbers with nearest zip code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NumbersApi apiInstance = new NumbersApi(defaultClient);
    Integer limit = 100; // Integer | To set the maximum number of records to return in a paged list response. The default is 100
    String prefix = "prefix_example"; // String | A 4-7 digit prefix
    String city = "city_example"; // String | A city name
    String state = "state_example"; // String | A two-letter state code. Example: CA, IL, etc.
    String zipcode = "zipcode_example"; // String | A five-digit Zipcode
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      NumberList result = apiInstance.findNumbersLocal(limit, prefix, city, state, zipcode, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersApi#findNumbersLocal");
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
| **limit** | **Integer**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100] |
| **prefix** | **String**| A 4-7 digit prefix | [optional] |
| **city** | **String**| A city name | [optional] |
| **state** | **String**| A two-letter state code. Example: CA, IL, etc. | [optional] |
| **zipcode** | **String**| A five-digit Zipcode | [optional] |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**NumberList**](NumberList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="findNumbersTollfree"></a>
# **findNumbersTollfree**
> NumberList findNumbersTollfree(pattern, limit, fields)

Find tollfree numbers

Searches for the toll free numbers which are available for purchase in the CallFire catalog

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NumbersApi apiInstance = new NumbersApi(defaultClient);
    String pattern = "pattern_example"; // String | Filter toll free numbers by prefix, pattern must be 3 char long and should end with '*'. Examples: 8**, 85*, 87* (but 855 will fail because pattern must end with '*').
    Integer limit = 100; // Integer | To set the maximum number of records to return in a paged list response. The default is 100
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      NumberList result = apiInstance.findNumbersTollfree(pattern, limit, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersApi#findNumbersTollfree");
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
| **pattern** | **String**| Filter toll free numbers by prefix, pattern must be 3 char long and should end with &#39;*&#39;. Examples: 8**, 85*, 87* (but 855 will fail because pattern must end with &#39;*&#39;). | [optional] |
| **limit** | **Integer**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100] |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**NumberList**](NumberList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getNumberLease"></a>
# **getNumberLease**
> NumberLease getNumberLease(number, fields)

Find a specific lease

Returns a single NumberLease instance for a given number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NumbersApi apiInstance = new NumbersApi(defaultClient);
    String number = "number_example"; // String | A phone number in E.164 format (11-digit). Example: 12132000384
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      NumberLease result = apiInstance.getNumberLease(number, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersApi#getNumberLease");
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
| **number** | **String**| A phone number in E.164 format (11-digit). Example: 12132000384 | |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**NumberLease**](NumberLease.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getNumberLeaseConfig"></a>
# **getNumberLeaseConfig**
> NumberConfig getNumberLeaseConfig(number, fields)

Find a specific lease config

Returns a single NumberConfig instance for a given number lease

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NumbersApi apiInstance = new NumbersApi(defaultClient);
    String number = "number_example"; // String | A phone number in E.164 format (11-digit). Example: 12132000384
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      NumberConfig result = apiInstance.getNumberLeaseConfig(number, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersApi#getNumberLeaseConfig");
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
| **number** | **String**| A phone number in E.164 format (11-digit). Example: 12132000384 | |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**NumberConfig**](NumberConfig.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="updateNumberLease"></a>
# **updateNumberLease**
> updateNumberLease(number, numberLease)

Update a lease

Updates a number lease instance. Ability to turn on/off autoRenew and toggle call/text features for a particular number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NumbersApi apiInstance = new NumbersApi(defaultClient);
    String number = "number_example"; // String | A phone number in E.164 format (11-digit). Example: 12132000384
    NumberLease numberLease = new NumberLease(); // NumberLease | A NumberLease object to update
    try {
      apiInstance.updateNumberLease(number, numberLease);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersApi#updateNumberLease");
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
| **number** | **String**| A phone number in E.164 format (11-digit). Example: 12132000384 | |
| **numberLease** | [**NumberLease**](NumberLease.md)| A NumberLease object to update | [optional] |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="updateNumberLeaseConfig"></a>
# **updateNumberLeaseConfig**
> updateNumberLeaseConfig(number, numberConfig)

Update a lease config

Updates a phone number lease configuration. Use this API endpoint to add an Inbound IVR or Call Tracking feature to a CallFire phone number. Call tracking configuration allows you to track the incoming calls, to analyze and to respond customers using sms or voice replies. For more information see [call tracking page](https://www.callfire.com/products/call-tracking)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NumbersApi apiInstance = new NumbersApi(defaultClient);
    String number = "number_example"; // String | A phone number in E.164 format (11-digit) which needs to be verified. Example: 12132000384
    NumberConfig numberConfig = new NumberConfig(); // NumberConfig | The configuration of a number lease object. There are two available types of configuration: IVR, TRACKING 
    try {
      apiInstance.updateNumberLeaseConfig(number, numberConfig);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersApi#updateNumberLeaseConfig");
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
| **number** | **String**| A phone number in E.164 format (11-digit) which needs to be verified. Example: 12132000384 | |
| **numberConfig** | [**NumberConfig**](NumberConfig.md)| The configuration of a number lease object. There are two available types of configuration: IVR, TRACKING  | [optional] |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

