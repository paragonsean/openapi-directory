# CampaignsApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**allCampaigns**](CampaignsApi.md#allCampaigns) | **GET** /campaigns | Get all campaigns details |
| [**deleteCampaign**](CampaignsApi.md#deleteCampaign) | **DELETE** /campaigns/{id} | Delete a campaign |
| [**deleteCampaignEvent**](CampaignsApi.md#deleteCampaignEvent) | **DELETE** /campaigns/events/{id} | Delete a campaign event details |
| [**getAllCampaignEvents**](CampaignsApi.md#getAllCampaignEvents) | **GET** /campaigns/events | Get all campaign events |
| [**getCampaign**](CampaignsApi.md#getCampaign) | **GET** /campaigns/{id} | Get a campaign details |
| [**getCampaignEvent**](CampaignsApi.md#getCampaignEvent) | **GET** /campaigns/events/{id} | Get a campaign event details |
| [**getEventsCampaign**](CampaignsApi.md#getEventsCampaign) | **GET** /campaigns/{id}/events | Get campaign events for a campaign |
| [**saveCampaign**](CampaignsApi.md#saveCampaign) | **POST** /campaigns | Save a campaign |
| [**saveCampaignEvent**](CampaignsApi.md#saveCampaignEvent) | **POST** /campaigns/events/{id} | Update an existing event |
| [**scheduleCampaign**](CampaignsApi.md#scheduleCampaign) | **POST** /campaigns/{id}/schedule | Schedule a campaign event for a campaign |


<a id="allCampaigns"></a>
# **allCampaigns**
> AllCampaigns200Response allCampaigns(campaignType, status)

Get all campaigns details

Get all campaigns details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    CampaignsApi apiInstance = new CampaignsApi(defaultClient);
    String campaignType = "system-update"; // String | Type of the campaigns we want
    String status = "enabled"; // String | Status of the campaigns we want
    try {
      AllCampaigns200Response result = apiInstance.allCampaigns(campaignType, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignsApi#allCampaigns");
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
| **campaignType** | **String**| Type of the campaigns we want | [optional] [enum: system-update, software-update] |
| **status** | **String**| Status of the campaigns we want | [optional] [enum: enabled, disabled, archived] |

### Return type

[**AllCampaigns200Response**](AllCampaigns200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign details result |  -  |

<a id="deleteCampaign"></a>
# **deleteCampaign**
> DeleteCampaign200Response deleteCampaign(id)

Delete a campaign

Delete a campaign

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    CampaignsApi apiInstance = new CampaignsApi(defaultClient);
    UUID id = UUID.fromString("0076a379-f32d-4732-9e91-33ab219d8fde"); // UUID | Id of the campaign
    try {
      DeleteCampaign200Response result = apiInstance.deleteCampaign(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignsApi#deleteCampaign");
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
| **id** | **UUID**| Id of the campaign | |

### Return type

[**DeleteCampaign200Response**](DeleteCampaign200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign details result |  -  |

<a id="deleteCampaignEvent"></a>
# **deleteCampaignEvent**
> DeleteCampaignEvent200Response deleteCampaignEvent(id)

Delete a campaign event details

Delete a campaign event details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    CampaignsApi apiInstance = new CampaignsApi(defaultClient);
    UUID id = UUID.fromString("0076a379-f32d-4732-9e91-33ab219d8fde"); // UUID | Id of the campaign event
    try {
      DeleteCampaignEvent200Response result = apiInstance.deleteCampaignEvent(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignsApi#deleteCampaignEvent");
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
| **id** | **UUID**| Id of the campaign event | |

### Return type

[**DeleteCampaignEvent200Response**](DeleteCampaignEvent200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign event details result |  -  |

<a id="getAllCampaignEvents"></a>
# **getAllCampaignEvents**
> GetAllCampaignEvents200Response getAllCampaignEvents(campaignType, state, campaignId, limit, offset, before, after, order, asc)

Get all campaign events

Get all campaign events

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    CampaignsApi apiInstance = new CampaignsApi(defaultClient);
    String campaignType = "system-update"; // String | Type of the campaigns we want
    String state = "scheduled"; // String | Status of the campaign events we want
    String campaignId = "system-update"; // String | id of the campaigns we want
    Integer limit = 56; // Integer | Max number of elements in response
    Integer offset = 56; // Integer | Offset of data in response (skip X elements)
    LocalDate before = LocalDate.now(); // LocalDate | 
    LocalDate after = LocalDate.now(); // LocalDate | 
    String order = "order_example"; // String | 
    String asc = "asc"; // String | 
    try {
      GetAllCampaignEvents200Response result = apiInstance.getAllCampaignEvents(campaignType, state, campaignId, limit, offset, before, after, order, asc);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignsApi#getAllCampaignEvents");
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
| **campaignType** | **String**| Type of the campaigns we want | [optional] [enum: system-update, software-update] |
| **state** | **String**| Status of the campaign events we want | [optional] [enum: scheduled, running, finished, skipped] |
| **campaignId** | **String**| id of the campaigns we want | [optional] [enum: system-update, software-update] |
| **limit** | **Integer**| Max number of elements in response | [optional] |
| **offset** | **Integer**| Offset of data in response (skip X elements) | [optional] |
| **before** | **LocalDate**|  | [optional] |
| **after** | **LocalDate**|  | [optional] |
| **order** | **String**|  | [optional] |
| **asc** | **String**|  | [optional] [enum: asc, desc] |

### Return type

[**GetAllCampaignEvents200Response**](GetAllCampaignEvents200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign event details result |  -  |

<a id="getCampaign"></a>
# **getCampaign**
> GetCampaign200Response getCampaign(id)

Get a campaign details

Get a campaign details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    CampaignsApi apiInstance = new CampaignsApi(defaultClient);
    UUID id = UUID.fromString("0076a379-f32d-4732-9e91-33ab219d8fde"); // UUID | Id of the campaign
    try {
      GetCampaign200Response result = apiInstance.getCampaign(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignsApi#getCampaign");
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
| **id** | **UUID**| Id of the campaign | |

### Return type

[**GetCampaign200Response**](GetCampaign200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign details result |  -  |

<a id="getCampaignEvent"></a>
# **getCampaignEvent**
> GetAllCampaignEvents200Response getCampaignEvent(id)

Get a campaign event details

Get a campaign event details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    CampaignsApi apiInstance = new CampaignsApi(defaultClient);
    UUID id = UUID.fromString("0076a379-f32d-4732-9e91-33ab219d8fde"); // UUID | Id of the campaign event
    try {
      GetAllCampaignEvents200Response result = apiInstance.getCampaignEvent(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignsApi#getCampaignEvent");
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
| **id** | **UUID**| Id of the campaign event | |

### Return type

[**GetAllCampaignEvents200Response**](GetAllCampaignEvents200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign details result |  -  |

<a id="getEventsCampaign"></a>
# **getEventsCampaign**
> GetEventsCampaign200Response getEventsCampaign(id, campaignType, state, limit, offset, before, after, order, asc)

Get campaign events for a campaign

Get campaign events for a campaign

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    CampaignsApi apiInstance = new CampaignsApi(defaultClient);
    UUID id = UUID.fromString("0076a379-f32d-4732-9e91-33ab219d8fde"); // UUID | Id of the campaign
    String campaignType = "system-update"; // String | Type of the campaigns we want
    String state = "scheduled"; // String | Status of the campaign events we want
    Integer limit = 56; // Integer | Max number of elements in response
    Integer offset = 56; // Integer | Offset of data in response (skip X elements)
    LocalDate before = LocalDate.now(); // LocalDate | 
    LocalDate after = LocalDate.now(); // LocalDate | 
    String order = "order_example"; // String | 
    String asc = "asc"; // String | 
    try {
      GetEventsCampaign200Response result = apiInstance.getEventsCampaign(id, campaignType, state, limit, offset, before, after, order, asc);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignsApi#getEventsCampaign");
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
| **id** | **UUID**| Id of the campaign | |
| **campaignType** | **String**| Type of the campaigns we want | [optional] [enum: system-update, software-update] |
| **state** | **String**| Status of the campaign events we want | [optional] [enum: scheduled, running, finished, skipped] |
| **limit** | **Integer**| Max number of elements in response | [optional] |
| **offset** | **Integer**| Offset of data in response (skip X elements) | [optional] |
| **before** | **LocalDate**|  | [optional] |
| **after** | **LocalDate**|  | [optional] |
| **order** | **String**|  | [optional] |
| **asc** | **String**|  | [optional] [enum: asc, desc] |

### Return type

[**GetEventsCampaign200Response**](GetEventsCampaign200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign details result |  -  |

<a id="saveCampaign"></a>
# **saveCampaign**
> SaveCampaign200Response saveCampaign(campaignDetails)

Save a campaign

Save a campaign details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    CampaignsApi apiInstance = new CampaignsApi(defaultClient);
    CampaignDetails campaignDetails = new CampaignDetails(); // CampaignDetails | 
    try {
      SaveCampaign200Response result = apiInstance.saveCampaign(campaignDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignsApi#saveCampaign");
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
| **campaignDetails** | [**CampaignDetails**](CampaignDetails.md)|  | |

### Return type

[**SaveCampaign200Response**](SaveCampaign200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign details result |  -  |

<a id="saveCampaignEvent"></a>
# **saveCampaignEvent**
> SaveCampaignEvent200Response saveCampaignEvent(id)

Update an existing event

Update an existing event

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    CampaignsApi apiInstance = new CampaignsApi(defaultClient);
    UUID id = UUID.fromString("0076a379-f32d-4732-9e91-33ab219d8fde"); // UUID | Id of the campaign event
    try {
      SaveCampaignEvent200Response result = apiInstance.saveCampaignEvent(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignsApi#saveCampaignEvent");
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
| **id** | **UUID**| Id of the campaign event | |

### Return type

[**SaveCampaignEvent200Response**](SaveCampaignEvent200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign event details result |  -  |

<a id="scheduleCampaign"></a>
# **scheduleCampaign**
> ScheduleCampaign200Response scheduleCampaign(id)

Schedule a campaign event for a campaign

Schedule a campaign event for a campaign

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    CampaignsApi apiInstance = new CampaignsApi(defaultClient);
    UUID id = UUID.fromString("0076a379-f32d-4732-9e91-33ab219d8fde"); // UUID | Id of the campaign
    try {
      ScheduleCampaign200Response result = apiInstance.scheduleCampaign(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignsApi#scheduleCampaign");
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
| **id** | **UUID**| Id of the campaign | |

### Return type

[**ScheduleCampaign200Response**](ScheduleCampaign200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign events details result |  -  |

