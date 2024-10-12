# PreviewMarketplaceInstalledAddOnApi

All URIs are relative to *https://preview.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createMarketplaceInstalledAddOn**](PreviewMarketplaceInstalledAddOnApi.md#createMarketplaceInstalledAddOn) | **POST** /marketplace/InstalledAddOns |  |
| [**deleteMarketplaceInstalledAddOn**](PreviewMarketplaceInstalledAddOnApi.md#deleteMarketplaceInstalledAddOn) | **DELETE** /marketplace/InstalledAddOns/{Sid} |  |
| [**fetchMarketplaceInstalledAddOn**](PreviewMarketplaceInstalledAddOnApi.md#fetchMarketplaceInstalledAddOn) | **GET** /marketplace/InstalledAddOns/{Sid} |  |
| [**listMarketplaceInstalledAddOn**](PreviewMarketplaceInstalledAddOnApi.md#listMarketplaceInstalledAddOn) | **GET** /marketplace/InstalledAddOns |  |
| [**updateMarketplaceInstalledAddOn**](PreviewMarketplaceInstalledAddOnApi.md#updateMarketplaceInstalledAddOn) | **POST** /marketplace/InstalledAddOns/{Sid} |  |


<a id="createMarketplaceInstalledAddOn"></a>
# **createMarketplaceInstalledAddOn**
> PreviewMarketplaceInstalledAddOn createMarketplaceInstalledAddOn(acceptTermsOfService, availableAddOnSid, _configuration, uniqueName)



Install an Add-on for the Account specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewMarketplaceInstalledAddOnApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewMarketplaceInstalledAddOnApi apiInstance = new PreviewMarketplaceInstalledAddOnApi(defaultClient);
    Boolean acceptTermsOfService = true; // Boolean | Whether the Terms of Service were accepted.
    String availableAddOnSid = "availableAddOnSid_example"; // String | The SID of the AvaliableAddOn to install.
    Object _configuration = null; // Object | The JSON object that represents the configuration of the new Add-on being installed.
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the resource. This value must be unique within the Account.
    try {
      PreviewMarketplaceInstalledAddOn result = apiInstance.createMarketplaceInstalledAddOn(acceptTermsOfService, availableAddOnSid, _configuration, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewMarketplaceInstalledAddOnApi#createMarketplaceInstalledAddOn");
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
| **acceptTermsOfService** | **Boolean**| Whether the Terms of Service were accepted. | |
| **availableAddOnSid** | **String**| The SID of the AvaliableAddOn to install. | |
| **_configuration** | [**Object**](Object.md)| The JSON object that represents the configuration of the new Add-on being installed. | [optional] |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. This value must be unique within the Account. | [optional] |

### Return type

[**PreviewMarketplaceInstalledAddOn**](PreviewMarketplaceInstalledAddOn.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteMarketplaceInstalledAddOn"></a>
# **deleteMarketplaceInstalledAddOn**
> deleteMarketplaceInstalledAddOn(sid)



Remove an Add-on installation from your account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewMarketplaceInstalledAddOnApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewMarketplaceInstalledAddOnApi apiInstance = new PreviewMarketplaceInstalledAddOnApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the InstalledAddOn resource to delete.
    try {
      apiInstance.deleteMarketplaceInstalledAddOn(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewMarketplaceInstalledAddOnApi#deleteMarketplaceInstalledAddOn");
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
| **sid** | **String**| The SID of the InstalledAddOn resource to delete. | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchMarketplaceInstalledAddOn"></a>
# **fetchMarketplaceInstalledAddOn**
> PreviewMarketplaceInstalledAddOn fetchMarketplaceInstalledAddOn(sid)



Fetch an instance of an Add-on currently installed on this Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewMarketplaceInstalledAddOnApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewMarketplaceInstalledAddOnApi apiInstance = new PreviewMarketplaceInstalledAddOnApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the InstalledAddOn resource to fetch.
    try {
      PreviewMarketplaceInstalledAddOn result = apiInstance.fetchMarketplaceInstalledAddOn(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewMarketplaceInstalledAddOnApi#fetchMarketplaceInstalledAddOn");
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
| **sid** | **String**| The SID of the InstalledAddOn resource to fetch. | |

### Return type

[**PreviewMarketplaceInstalledAddOn**](PreviewMarketplaceInstalledAddOn.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listMarketplaceInstalledAddOn"></a>
# **listMarketplaceInstalledAddOn**
> ListMarketplaceInstalledAddOnResponse listMarketplaceInstalledAddOn(pageSize, page, pageToken)



Retrieve a list of Add-ons currently installed on this Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewMarketplaceInstalledAddOnApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewMarketplaceInstalledAddOnApi apiInstance = new PreviewMarketplaceInstalledAddOnApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListMarketplaceInstalledAddOnResponse result = apiInstance.listMarketplaceInstalledAddOn(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewMarketplaceInstalledAddOnApi#listMarketplaceInstalledAddOn");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListMarketplaceInstalledAddOnResponse**](ListMarketplaceInstalledAddOnResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateMarketplaceInstalledAddOn"></a>
# **updateMarketplaceInstalledAddOn**
> PreviewMarketplaceInstalledAddOn updateMarketplaceInstalledAddOn(sid, _configuration, uniqueName)



Update an Add-on installation for the Account specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewMarketplaceInstalledAddOnApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewMarketplaceInstalledAddOnApi apiInstance = new PreviewMarketplaceInstalledAddOnApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the InstalledAddOn resource to update.
    Object _configuration = null; // Object | Valid JSON object that conform to the configuration schema exposed by the associated AvailableAddOn resource. This is only required by Add-ons that need to be configured
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the resource. This value must be unique within the Account.
    try {
      PreviewMarketplaceInstalledAddOn result = apiInstance.updateMarketplaceInstalledAddOn(sid, _configuration, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewMarketplaceInstalledAddOnApi#updateMarketplaceInstalledAddOn");
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
| **sid** | **String**| The SID of the InstalledAddOn resource to update. | |
| **_configuration** | [**Object**](Object.md)| Valid JSON object that conform to the configuration schema exposed by the associated AvailableAddOn resource. This is only required by Add-ons that need to be configured | [optional] |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. This value must be unique within the Account. | [optional] |

### Return type

[**PreviewMarketplaceInstalledAddOn**](PreviewMarketplaceInstalledAddOn.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

