# LicensesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assignOrganizationLicensesSeats_1**](LicensesApi.md#assignOrganizationLicensesSeats_1) | **POST** /organizations/{organizationId}/licenses/assignSeats | Assign SM seats to a network |
| [**getOrganizationLicense_1**](LicensesApi.md#getOrganizationLicense_1) | **GET** /organizations/{organizationId}/licenses/{licenseId} | Display a license |
| [**getOrganizationLicensesOverview_1**](LicensesApi.md#getOrganizationLicensesOverview_1) | **GET** /organizations/{organizationId}/licenses/overview | Return an overview of the license state for an organization |
| [**getOrganizationLicenses_1**](LicensesApi.md#getOrganizationLicenses_1) | **GET** /organizations/{organizationId}/licenses | List the licenses for an organization |
| [**getOrganizationLicensingCotermLicenses_2**](LicensesApi.md#getOrganizationLicensingCotermLicenses_2) | **GET** /organizations/{organizationId}/licensing/coterm/licenses | List the licenses in a coterm organization |
| [**moveOrganizationLicensesSeats_1**](LicensesApi.md#moveOrganizationLicensesSeats_1) | **POST** /organizations/{organizationId}/licenses/moveSeats | Move SM seats to another organization |
| [**moveOrganizationLicenses_1**](LicensesApi.md#moveOrganizationLicenses_1) | **POST** /organizations/{organizationId}/licenses/move | Move licenses to another organization |
| [**moveOrganizationLicensingCotermLicenses_2**](LicensesApi.md#moveOrganizationLicensingCotermLicenses_2) | **POST** /organizations/{organizationId}/licensing/coterm/licenses/move | Moves a license to a different organization (coterm only) |
| [**renewOrganizationLicensesSeats_1**](LicensesApi.md#renewOrganizationLicensesSeats_1) | **POST** /organizations/{organizationId}/licenses/renewSeats | Renew SM seats of a license |
| [**updateOrganizationLicense_1**](LicensesApi.md#updateOrganizationLicense_1) | **PUT** /organizations/{organizationId}/licenses/{licenseId} | Update a license |


<a id="assignOrganizationLicensesSeats_1"></a>
# **assignOrganizationLicensesSeats_1**
> AssignOrganizationLicensesSeats200Response assignOrganizationLicensesSeats_1(organizationId, assignOrganizationLicensesSeatsRequest)

Assign SM seats to a network

Assign SM seats to a network. This will increase the managed SM device limit of the network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LicensesApi apiInstance = new LicensesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    AssignOrganizationLicensesSeatsRequest assignOrganizationLicensesSeatsRequest = new AssignOrganizationLicensesSeatsRequest(); // AssignOrganizationLicensesSeatsRequest | 
    try {
      AssignOrganizationLicensesSeats200Response result = apiInstance.assignOrganizationLicensesSeats_1(organizationId, assignOrganizationLicensesSeatsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensesApi#assignOrganizationLicensesSeats_1");
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
| **organizationId** | **String**|  | |
| **assignOrganizationLicensesSeatsRequest** | [**AssignOrganizationLicensesSeatsRequest**](AssignOrganizationLicensesSeatsRequest.md)|  | |

### Return type

[**AssignOrganizationLicensesSeats200Response**](AssignOrganizationLicensesSeats200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationLicense_1"></a>
# **getOrganizationLicense_1**
> GetOrganizationLicenses200ResponseInner getOrganizationLicense_1(organizationId, licenseId)

Display a license

Display a license

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LicensesApi apiInstance = new LicensesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String licenseId = "licenseId_example"; // String | 
    try {
      GetOrganizationLicenses200ResponseInner result = apiInstance.getOrganizationLicense_1(organizationId, licenseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensesApi#getOrganizationLicense_1");
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
| **organizationId** | **String**|  | |
| **licenseId** | **String**|  | |

### Return type

[**GetOrganizationLicenses200ResponseInner**](GetOrganizationLicenses200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationLicensesOverview_1"></a>
# **getOrganizationLicensesOverview_1**
> Object getOrganizationLicensesOverview_1(organizationId)

Return an overview of the license state for an organization

Return an overview of the license state for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LicensesApi apiInstance = new LicensesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationLicensesOverview_1(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensesApi#getOrganizationLicensesOverview_1");
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
| **organizationId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationLicenses_1"></a>
# **getOrganizationLicenses_1**
> List&lt;GetOrganizationLicenses200ResponseInner&gt; getOrganizationLicenses_1(organizationId, perPage, startingAfter, endingBefore, deviceSerial, networkId, state)

List the licenses for an organization

List the licenses for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LicensesApi apiInstance = new LicensesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String deviceSerial = "deviceSerial_example"; // String | Filter the licenses to those assigned to a particular device. Returned in the same order that they are queued to the device.
    String networkId = "networkId_example"; // String | Filter the licenses to those assigned in a particular network
    String state = "active"; // String | Filter the licenses to those in a particular state. Can be one of 'active', 'expired', 'expiring', 'recentlyQueued', 'unused' or 'unusedActive'
    try {
      List<GetOrganizationLicenses200ResponseInner> result = apiInstance.getOrganizationLicenses_1(organizationId, perPage, startingAfter, endingBefore, deviceSerial, networkId, state);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensesApi#getOrganizationLicenses_1");
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
| **organizationId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **deviceSerial** | **String**| Filter the licenses to those assigned to a particular device. Returned in the same order that they are queued to the device. | [optional] |
| **networkId** | **String**| Filter the licenses to those assigned in a particular network | [optional] |
| **state** | **String**| Filter the licenses to those in a particular state. Can be one of &#39;active&#39;, &#39;expired&#39;, &#39;expiring&#39;, &#39;recentlyQueued&#39;, &#39;unused&#39; or &#39;unusedActive&#39; | [optional] [enum: active, expired, expiring, recentlyQueued, unused, unusedActive] |

### Return type

[**List&lt;GetOrganizationLicenses200ResponseInner&gt;**](GetOrganizationLicenses200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getOrganizationLicensingCotermLicenses_2"></a>
# **getOrganizationLicensingCotermLicenses_2**
> List&lt;GetOrganizationLicensingCotermLicenses200ResponseInner&gt; getOrganizationLicensingCotermLicenses_2(organizationId, perPage, startingAfter, endingBefore, invalidated, expired)

List the licenses in a coterm organization

List the licenses in a coterm organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LicensesApi apiInstance = new LicensesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    Boolean invalidated = true; // Boolean | Filter for licenses that are invalidated
    Boolean expired = true; // Boolean | Filter for licenses that are expired
    try {
      List<GetOrganizationLicensingCotermLicenses200ResponseInner> result = apiInstance.getOrganizationLicensingCotermLicenses_2(organizationId, perPage, startingAfter, endingBefore, invalidated, expired);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensesApi#getOrganizationLicensingCotermLicenses_2");
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
| **organizationId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **invalidated** | **Boolean**| Filter for licenses that are invalidated | [optional] |
| **expired** | **Boolean**| Filter for licenses that are expired | [optional] |

### Return type

[**List&lt;GetOrganizationLicensingCotermLicenses200ResponseInner&gt;**](GetOrganizationLicensingCotermLicenses200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="moveOrganizationLicensesSeats_1"></a>
# **moveOrganizationLicensesSeats_1**
> MoveOrganizationLicensesSeats200Response moveOrganizationLicensesSeats_1(organizationId, moveOrganizationLicensesSeatsRequest)

Move SM seats to another organization

Move SM seats to another organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LicensesApi apiInstance = new LicensesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    MoveOrganizationLicensesSeatsRequest moveOrganizationLicensesSeatsRequest = new MoveOrganizationLicensesSeatsRequest(); // MoveOrganizationLicensesSeatsRequest | 
    try {
      MoveOrganizationLicensesSeats200Response result = apiInstance.moveOrganizationLicensesSeats_1(organizationId, moveOrganizationLicensesSeatsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensesApi#moveOrganizationLicensesSeats_1");
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
| **organizationId** | **String**|  | |
| **moveOrganizationLicensesSeatsRequest** | [**MoveOrganizationLicensesSeatsRequest**](MoveOrganizationLicensesSeatsRequest.md)|  | |

### Return type

[**MoveOrganizationLicensesSeats200Response**](MoveOrganizationLicensesSeats200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="moveOrganizationLicenses_1"></a>
# **moveOrganizationLicenses_1**
> MoveOrganizationLicenses200Response moveOrganizationLicenses_1(organizationId, moveOrganizationLicensesRequest)

Move licenses to another organization

Move licenses to another organization. This will also move any devices that the licenses are assigned to

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LicensesApi apiInstance = new LicensesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    MoveOrganizationLicensesRequest moveOrganizationLicensesRequest = new MoveOrganizationLicensesRequest(); // MoveOrganizationLicensesRequest | 
    try {
      MoveOrganizationLicenses200Response result = apiInstance.moveOrganizationLicenses_1(organizationId, moveOrganizationLicensesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensesApi#moveOrganizationLicenses_1");
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
| **organizationId** | **String**|  | |
| **moveOrganizationLicensesRequest** | [**MoveOrganizationLicensesRequest**](MoveOrganizationLicensesRequest.md)|  | |

### Return type

[**MoveOrganizationLicenses200Response**](MoveOrganizationLicenses200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="moveOrganizationLicensingCotermLicenses_2"></a>
# **moveOrganizationLicensingCotermLicenses_2**
> MoveOrganizationLicensingCotermLicenses200Response moveOrganizationLicensingCotermLicenses_2(organizationId, moveOrganizationLicensingCotermLicensesRequest)

Moves a license to a different organization (coterm only)

Moves a license to a different organization (coterm only)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LicensesApi apiInstance = new LicensesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    MoveOrganizationLicensingCotermLicensesRequest moveOrganizationLicensingCotermLicensesRequest = new MoveOrganizationLicensingCotermLicensesRequest(); // MoveOrganizationLicensingCotermLicensesRequest | 
    try {
      MoveOrganizationLicensingCotermLicenses200Response result = apiInstance.moveOrganizationLicensingCotermLicenses_2(organizationId, moveOrganizationLicensingCotermLicensesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensesApi#moveOrganizationLicensingCotermLicenses_2");
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
| **organizationId** | **String**|  | |
| **moveOrganizationLicensingCotermLicensesRequest** | [**MoveOrganizationLicensingCotermLicensesRequest**](MoveOrganizationLicensingCotermLicensesRequest.md)|  | |

### Return type

[**MoveOrganizationLicensingCotermLicenses200Response**](MoveOrganizationLicensingCotermLicenses200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="renewOrganizationLicensesSeats_1"></a>
# **renewOrganizationLicensesSeats_1**
> AssignOrganizationLicensesSeats200Response renewOrganizationLicensesSeats_1(organizationId, renewOrganizationLicensesSeatsRequest)

Renew SM seats of a license

Renew SM seats of a license. This will extend the license expiration date of managed SM devices covered by this license

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LicensesApi apiInstance = new LicensesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    RenewOrganizationLicensesSeatsRequest renewOrganizationLicensesSeatsRequest = new RenewOrganizationLicensesSeatsRequest(); // RenewOrganizationLicensesSeatsRequest | 
    try {
      AssignOrganizationLicensesSeats200Response result = apiInstance.renewOrganizationLicensesSeats_1(organizationId, renewOrganizationLicensesSeatsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensesApi#renewOrganizationLicensesSeats_1");
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
| **organizationId** | **String**|  | |
| **renewOrganizationLicensesSeatsRequest** | [**RenewOrganizationLicensesSeatsRequest**](RenewOrganizationLicensesSeatsRequest.md)|  | |

### Return type

[**AssignOrganizationLicensesSeats200Response**](AssignOrganizationLicensesSeats200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateOrganizationLicense_1"></a>
# **updateOrganizationLicense_1**
> GetOrganizationLicenses200ResponseInner updateOrganizationLicense_1(organizationId, licenseId, updateOrganizationLicenseRequest)

Update a license

Update a license

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LicensesApi apiInstance = new LicensesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String licenseId = "licenseId_example"; // String | 
    UpdateOrganizationLicenseRequest updateOrganizationLicenseRequest = new UpdateOrganizationLicenseRequest(); // UpdateOrganizationLicenseRequest | 
    try {
      GetOrganizationLicenses200ResponseInner result = apiInstance.updateOrganizationLicense_1(organizationId, licenseId, updateOrganizationLicenseRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensesApi#updateOrganizationLicense_1");
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
| **organizationId** | **String**|  | |
| **licenseId** | **String**|  | |
| **updateOrganizationLicenseRequest** | [**UpdateOrganizationLicenseRequest**](UpdateOrganizationLicenseRequest.md)|  | [optional] |

### Return type

[**GetOrganizationLicenses200ResponseInner**](GetOrganizationLicenses200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

