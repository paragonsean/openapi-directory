# SiteApi

All URIs are relative to *https://api.netlify.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSite**](SiteApi.md#createSite) | **POST** /sites |  |
| [**createSiteInTeam**](SiteApi.md#createSiteInTeam) | **POST** /{account_slug}/sites |  |
| [**deleteSite**](SiteApi.md#deleteSite) | **DELETE** /sites/{site_id} |  |
| [**getSite**](SiteApi.md#getSite) | **GET** /sites/{site_id} |  |
| [**listSites**](SiteApi.md#listSites) | **GET** /sites |  |
| [**listSitesForAccount**](SiteApi.md#listSitesForAccount) | **GET** /{account_slug}/sites |  |
| [**unlinkSiteRepo**](SiteApi.md#unlinkSiteRepo) | **PUT** /sites/{site_id}/unlink_repo |  |
| [**updateSite**](SiteApi.md#updateSite) | **PATCH** /sites/{site_id} |  |


<a id="createSite"></a>
# **createSite**
> Site createSite(site, configureDns)



**Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [createEnvVars](#tag/environmentVariables/operation/createEnvVars) to create environment variables for a site.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SiteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    SiteApi apiInstance = new SiteApi(defaultClient);
    SiteSetup site = new SiteSetup(); // SiteSetup | 
    Boolean configureDns = true; // Boolean | 
    try {
      Site result = apiInstance.createSite(site, configureDns);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SiteApi#createSite");
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
| **site** | [**SiteSetup**](SiteSetup.md)|  | |
| **configureDns** | **Boolean**|  | [optional] |

### Return type

[**Site**](Site.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **0** | error |  -  |

<a id="createSiteInTeam"></a>
# **createSiteInTeam**
> Site createSiteInTeam(accountSlug, configureDns, site)



**Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [createEnvVars](#tag/environmentVariables/operation/createEnvVars) to create environment variables for a site.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SiteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    SiteApi apiInstance = new SiteApi(defaultClient);
    String accountSlug = "accountSlug_example"; // String | 
    Boolean configureDns = true; // Boolean | 
    SiteSetup site = new SiteSetup(); // SiteSetup | 
    try {
      Site result = apiInstance.createSiteInTeam(accountSlug, configureDns, site);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SiteApi#createSiteInTeam");
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
| **accountSlug** | **String**|  | |
| **configureDns** | **Boolean**|  | [optional] |
| **site** | [**SiteSetup**](SiteSetup.md)|  | [optional] |

### Return type

[**Site**](Site.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **0** | error |  -  |

<a id="deleteSite"></a>
# **deleteSite**
> deleteSite(siteId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SiteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    SiteApi apiInstance = new SiteApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    try {
      apiInstance.deleteSite(siteId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SiteApi#deleteSite");
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
| **siteId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Deleted |  -  |
| **0** | error |  -  |

<a id="getSite"></a>
# **getSite**
> Site getSite(siteId)



**Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [getEnvVars](#tag/environmentVariables/operation/getEnvVars) to retrieve site environment variables.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SiteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    SiteApi apiInstance = new SiteApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    try {
      Site result = apiInstance.getSite(siteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SiteApi#getSite");
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
| **siteId** | **String**|  | |

### Return type

[**Site**](Site.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="listSites"></a>
# **listSites**
> List&lt;Site&gt; listSites(name, filter, page, perPage)



**Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [getEnvVars](#tag/environmentVariables/operation/getEnvVars) to retrieve site environment variables.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SiteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    SiteApi apiInstance = new SiteApi(defaultClient);
    String name = "name_example"; // String | 
    String filter = "all"; // String | 
    Integer page = 56; // Integer | 
    Integer perPage = 56; // Integer | 
    try {
      List<Site> result = apiInstance.listSites(name, filter, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SiteApi#listSites");
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
| **name** | **String**|  | [optional] |
| **filter** | **String**|  | [optional] [enum: all, owner, guest] |
| **page** | **Integer**|  | [optional] |
| **perPage** | **Integer**|  | [optional] |

### Return type

[**List&lt;Site&gt;**](Site.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="listSitesForAccount"></a>
# **listSitesForAccount**
> List&lt;Site&gt; listSitesForAccount(accountSlug, name, page, perPage)



**Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [getEnvVars](#tag/environmentVariables/operation/getEnvVars) to retrieve site environment variables.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SiteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    SiteApi apiInstance = new SiteApi(defaultClient);
    String accountSlug = "accountSlug_example"; // String | 
    String name = "name_example"; // String | 
    Integer page = 56; // Integer | 
    Integer perPage = 56; // Integer | 
    try {
      List<Site> result = apiInstance.listSitesForAccount(accountSlug, name, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SiteApi#listSitesForAccount");
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
| **accountSlug** | **String**|  | |
| **name** | **String**|  | [optional] |
| **page** | **Integer**|  | [optional] |
| **perPage** | **Integer**|  | [optional] |

### Return type

[**List&lt;Site&gt;**](Site.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="unlinkSiteRepo"></a>
# **unlinkSiteRepo**
> Site unlinkSiteRepo(siteId)



[Beta] Unlinks the repo from the site.  This action will also: - Delete associated deploy keys - Delete outgoing webhooks for the repo - Delete the site&#39;s build hooks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SiteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    SiteApi apiInstance = new SiteApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    try {
      Site result = apiInstance.unlinkSiteRepo(siteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SiteApi#unlinkSiteRepo");
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
| **siteId** | **String**|  | |

### Return type

[**Site**](Site.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Site not found |  -  |

<a id="updateSite"></a>
# **updateSite**
> Site updateSite(siteId, site)



**Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [updateEnvVar](#tag/environmentVariables/operation/updateEnvVar) to update a site&#39;s environment variables.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SiteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    SiteApi apiInstance = new SiteApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    SiteSetup site = new SiteSetup(); // SiteSetup | 
    try {
      Site result = apiInstance.updateSite(siteId, site);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SiteApi#updateSite");
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
| **siteId** | **String**|  | |
| **site** | [**SiteSetup**](SiteSetup.md)|  | |

### Return type

[**Site**](Site.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

