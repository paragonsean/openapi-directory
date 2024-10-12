# LicensesApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assignOrganizationLicensesSeats**](LicensesApi.md#assignOrganizationLicensesSeats) | **POST** /organizations/{organizationId}/licenses/assignSeats | Assign SM seats to a network |
| [**getOrganizationLicense**](LicensesApi.md#getOrganizationLicense) | **GET** /organizations/{organizationId}/licenses/{licenseId} | Display a license |
| [**getOrganizationLicenseState**](LicensesApi.md#getOrganizationLicenseState) | **GET** /organizations/{organizationId}/licenseState | Return an overview of the license state for an organization |
| [**getOrganizationLicenses**](LicensesApi.md#getOrganizationLicenses) | **GET** /organizations/{organizationId}/licenses | List the licenses for an organization |
| [**moveOrganizationLicensesSeats**](LicensesApi.md#moveOrganizationLicensesSeats) | **POST** /organizations/{organizationId}/licenses/moveSeats | Move SM seats to another organization |
| [**renewOrganizationLicensesSeats**](LicensesApi.md#renewOrganizationLicensesSeats) | **POST** /organizations/{organizationId}/licenses/renewSeats | Renew SM seats of a license |


<a id="assignOrganizationLicensesSeats"></a>
# **assignOrganizationLicensesSeats**
> Object assignOrganizationLicensesSeats(organizationId, assignOrganizationLicensesSeatsRequest)

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
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LicensesApi apiInstance = new LicensesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    AssignOrganizationLicensesSeatsRequest assignOrganizationLicensesSeatsRequest = new AssignOrganizationLicensesSeatsRequest(); // AssignOrganizationLicensesSeatsRequest | 
    try {
      Object result = apiInstance.assignOrganizationLicensesSeats(organizationId, assignOrganizationLicensesSeatsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensesApi#assignOrganizationLicensesSeats");
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

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationLicense"></a>
# **getOrganizationLicense**
> Object getOrganizationLicense(organizationId, licenseId)

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
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LicensesApi apiInstance = new LicensesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String licenseId = "licenseId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationLicense(organizationId, licenseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensesApi#getOrganizationLicense");
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

<a id="getOrganizationLicenseState"></a>
# **getOrganizationLicenseState**
> Object getOrganizationLicenseState(organizationId)

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
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LicensesApi apiInstance = new LicensesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationLicenseState(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensesApi#getOrganizationLicenseState");
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

<a id="getOrganizationLicenses"></a>
# **getOrganizationLicenses**
> List&lt;Object&gt; getOrganizationLicenses(organizationId, perPage, startingAfter, endingBefore, deviceSerial, networkId, state)

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
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
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
    String deviceSerial = "deviceSerial_example"; // String | Filter the licenses to those assigned to a particular device
    String networkId = "networkId_example"; // String | Filter the licenses to those assigned in a particular network
    String state = "active"; // String | Filter the licenses to those in a particular state. Can be one of 'active', 'expired', 'expiring', 'recentlyQueued', 'unused' or 'unusedActive'
    try {
      List<Object> result = apiInstance.getOrganizationLicenses(organizationId, perPage, startingAfter, endingBefore, deviceSerial, networkId, state);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensesApi#getOrganizationLicenses");
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
| **deviceSerial** | **String**| Filter the licenses to those assigned to a particular device | [optional] |
| **networkId** | **String**| Filter the licenses to those assigned in a particular network | [optional] |
| **state** | **String**| Filter the licenses to those in a particular state. Can be one of &#39;active&#39;, &#39;expired&#39;, &#39;expiring&#39;, &#39;recentlyQueued&#39;, &#39;unused&#39; or &#39;unusedActive&#39; | [optional] [enum: active, expired, expiring, recentlyQueued, unused, unusedActive] |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="moveOrganizationLicensesSeats"></a>
# **moveOrganizationLicensesSeats**
> Object moveOrganizationLicensesSeats(organizationId, moveOrganizationLicensesSeatsRequest)

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
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LicensesApi apiInstance = new LicensesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    MoveOrganizationLicensesSeatsRequest moveOrganizationLicensesSeatsRequest = new MoveOrganizationLicensesSeatsRequest(); // MoveOrganizationLicensesSeatsRequest | 
    try {
      Object result = apiInstance.moveOrganizationLicensesSeats(organizationId, moveOrganizationLicensesSeatsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensesApi#moveOrganizationLicensesSeats");
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

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="renewOrganizationLicensesSeats"></a>
# **renewOrganizationLicensesSeats**
> Object renewOrganizationLicensesSeats(organizationId, renewOrganizationLicensesSeatsRequest)

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
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LicensesApi apiInstance = new LicensesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    RenewOrganizationLicensesSeatsRequest renewOrganizationLicensesSeatsRequest = new RenewOrganizationLicensesSeatsRequest(); // RenewOrganizationLicensesSeatsRequest | 
    try {
      Object result = apiInstance.renewOrganizationLicensesSeats(organizationId, renewOrganizationLicensesSeatsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensesApi#renewOrganizationLicensesSeats");
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

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

