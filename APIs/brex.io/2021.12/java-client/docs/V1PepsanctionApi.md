# V1PepsanctionApi

All URIs are relative to *https://api.kompany.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pepMonitorList**](V1PepsanctionApi.md#pepMonitorList) | **GET** /api/v1/pepsanction/monitor/list | Retrieves a list of monitor entries |
| [**pepMonitorUnregister**](V1PepsanctionApi.md#pepMonitorUnregister) | **POST** /api/v1/pepsanction/monitor/unregister/{id} | Deactive a pep sanction monitor |
| [**pepMonitorUpdate**](V1PepsanctionApi.md#pepMonitorUpdate) | **POST** /api/v1/pepsanction/monitor/update/{id} | Update details of active Pep Sanction monitor |
| [**pepOrder**](V1PepsanctionApi.md#pepOrder) | **POST** /api/v1/pepsanction/order/{type}/{search} | Orders a new Pep Sanction Check Report |
| [**pepRetrieve**](V1PepsanctionApi.md#pepRetrieve) | **GET** /api/v1/pepsanction/retrieve/{id} | Returns a json or pdf report |


<a id="pepMonitorList"></a>
# **pepMonitorList**
> List&lt;PepMonitorList200ResponseInner&gt; pepMonitorList()

Retrieves a list of monitor entries

Retrieve a list of all active Pep Sanction Report monitors for this account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1PepsanctionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1PepsanctionApi apiInstance = new V1PepsanctionApi(defaultClient);
    try {
      List<PepMonitorList200ResponseInner> result = apiInstance.pepMonitorList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1PepsanctionApi#pepMonitorList");
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

[**List&lt;PepMonitorList200ResponseInner&gt;**](PepMonitorList200ResponseInner.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | View Pep Sanction Report monitors |  -  |
| **0** |  |  -  |

<a id="pepMonitorUnregister"></a>
# **pepMonitorUnregister**
> pepMonitorUnregister(id)

Deactive a pep sanction monitor

Unregister a previously created Pep Sanction Report Monitor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1PepsanctionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1PepsanctionApi apiInstance = new V1PepsanctionApi(defaultClient);
    String id = "id_example"; // String | The identifier of the Monitor
    try {
      apiInstance.pepMonitorUnregister(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1PepsanctionApi#pepMonitorUnregister");
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
| **id** | **String**| The identifier of the Monitor | |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** |  |  -  |

<a id="pepMonitorUpdate"></a>
# **pepMonitorUpdate**
> PepMonitorList200ResponseInner pepMonitorUpdate(id, webhook)

Update details of active Pep Sanction monitor

Update the webhook URL of an active Pep Sanction Report Monitor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1PepsanctionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1PepsanctionApi apiInstance = new V1PepsanctionApi(defaultClient);
    String id = "id_example"; // String | The identifier of the Monitor
    String webhook = "webhook_example"; // String | If Monitoring is enabled this parameter is required. This is where updates will be sent to
    try {
      PepMonitorList200ResponseInner result = apiInstance.pepMonitorUpdate(id, webhook);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1PepsanctionApi#pepMonitorUpdate");
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
| **id** | **String**| The identifier of the Monitor | |
| **webhook** | **String**| If Monitoring is enabled this parameter is required. This is where updates will be sent to | [optional] |

### Return type

[**PepMonitorList200ResponseInner**](PepMonitorList200ResponseInner.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | View a monitor for a Pep Sanction Report |  -  |
| **0** |  |  -  |

<a id="pepOrder"></a>
# **pepOrder**
> pepOrder(type, search, aliases, country, DOB, familyName, filters, givenName, LEI, locale, medialists, middleName, monitoring, peplists, region, smartMatch, watchlists, webhook)

Orders a new Pep Sanction Check Report

Order a new Pep Sanction Check by providing either a business or person name with some additional optional parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1PepsanctionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1PepsanctionApi apiInstance = new V1PepsanctionApi(defaultClient);
    String type = ""; // String | Type (Business or Person) of the requested Pep Sanction Check
    String search = "search_example"; // String | Search string for the Pep Sanction Check
    String aliases = "aliases_example"; // String | Optional parameter for declaring alias names when doing a person search (seperated by commas)
    String country = "country_example"; // String | Optional name of Country to assist in identifying matches based upon location/geography.
    String DOB = "DOB_example"; // String | Optional parameter for date of birth name when doing a person search
    String familyName = "familyName_example"; // String | Optional parameter for last name when doing a person search
    String filters = "filters_example"; // String | Optional parameter for restricting search when doing a person search (seperated by commas)
    String givenName = "givenName_example"; // String | Optional parameter for first name when doing a person search
    String LEI = "LEI_example"; // String | Optional Legal Entity Identifier for additional business identifier verification.
    String locale = "locale_example"; // String | Optional name of City or Locale to assist in identifying matches based upon location/geography.
    String medialists = "medialists_example"; // String | Optional parameter for selecting only specific media lists. By default all lists are queried
    String middleName = "middleName_example"; // String | Optional parameter for middle name when doing a person search
    Boolean monitoring = true; // Boolean | If this Pep Sanction Check should be continuesly monitored.
    String peplists = "peplists_example"; // String | Optional parameter for selecting only specific pep lists. By default all lists are queried
    String region = "region_example"; // String | Optional name of Region or State to assist in identifying matches based upon location/geography.
    Boolean smartMatch = true; // Boolean | Optional parameter for enabling SmartMatch to retrieve more results
    String watchlists = "watchlists_example"; // String | Optional parameter for selecting only specific watch lists. By default all lists are queried
    String webhook = "webhook_example"; // String | If Monitoring is enabled this parameter is required. This is where updates will be sent to
    try {
      apiInstance.pepOrder(type, search, aliases, country, DOB, familyName, filters, givenName, LEI, locale, medialists, middleName, monitoring, peplists, region, smartMatch, watchlists, webhook);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1PepsanctionApi#pepOrder");
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
| **type** | **String**| Type (Business or Person) of the requested Pep Sanction Check | [enum: , B, P] |
| **search** | **String**| Search string for the Pep Sanction Check | |
| **aliases** | **String**| Optional parameter for declaring alias names when doing a person search (seperated by commas) | [optional] |
| **country** | **String**| Optional name of Country to assist in identifying matches based upon location/geography. | [optional] |
| **DOB** | **String**| Optional parameter for date of birth name when doing a person search | [optional] |
| **familyName** | **String**| Optional parameter for last name when doing a person search | [optional] |
| **filters** | **String**| Optional parameter for restricting search when doing a person search (seperated by commas) | [optional] |
| **givenName** | **String**| Optional parameter for first name when doing a person search | [optional] |
| **LEI** | **String**| Optional Legal Entity Identifier for additional business identifier verification. | [optional] |
| **locale** | **String**| Optional name of City or Locale to assist in identifying matches based upon location/geography. | [optional] |
| **medialists** | **String**| Optional parameter for selecting only specific media lists. By default all lists are queried | [optional] |
| **middleName** | **String**| Optional parameter for middle name when doing a person search | [optional] |
| **monitoring** | **Boolean**| If this Pep Sanction Check should be continuesly monitored. | [optional] |
| **peplists** | **String**| Optional parameter for selecting only specific pep lists. By default all lists are queried | [optional] |
| **region** | **String**| Optional name of Region or State to assist in identifying matches based upon location/geography. | [optional] |
| **smartMatch** | **Boolean**| Optional parameter for enabling SmartMatch to retrieve more results | [optional] |
| **watchlists** | **String**| Optional parameter for selecting only specific watch lists. By default all lists are queried | [optional] |
| **webhook** | **String**| If Monitoring is enabled this parameter is required. This is where updates will be sent to | [optional] |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** |  |  -  |

<a id="pepRetrieve"></a>
# **pepRetrieve**
> PepRetrieve200Response pepRetrieve(id, accept)

Returns a json or pdf report

Retrieve a completed Pep Sanction check structured or in pdf depending on given accept header

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1PepsanctionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1PepsanctionApi apiInstance = new V1PepsanctionApi(defaultClient);
    String id = "id_example"; // String | The id of the ordered Pep Sanction Check (id as returned by orderPepSanction call)
    String accept = "application/json"; // String | The type (pdf or json) in which the check should be returned
    try {
      PepRetrieve200Response result = apiInstance.pepRetrieve(id, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1PepsanctionApi#pepRetrieve");
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
| **id** | **String**| The id of the ordered Pep Sanction Check (id as returned by orderPepSanction call) | |
| **accept** | **String**| The type (pdf or json) in which the check should be returned | [optional] [default to application/json] [enum: application/json, application/pdf] |

### Return type

[**PepRetrieve200Response**](PepRetrieve200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of a PEP and sanctions list check |  -  |
| **0** |  |  -  |

