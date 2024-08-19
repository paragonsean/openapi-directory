# ActionApi

All URIs are relative to *https://catalogue.data.gov.bc.ca/api/3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**actionOrganizationActivityListGet**](ActionApi.md#actionOrganizationActivityListGet) | **GET** /action/organization_activity_list | Get the activity stream of an organization |
| [**actionOrganizationActivityListHtmlGet**](ActionApi.md#actionOrganizationActivityListHtmlGet) | **GET** /action/organization_activity_list_html | Get the activity stream of an organization, HTML format |
| [**actionOrganizationAutocompleteGet**](ActionApi.md#actionOrganizationAutocompleteGet) | **GET** /action/organization_autocomplete | Get names of organizations that match a query string |
| [**actionOrganizationFollowerCountGet**](ActionApi.md#actionOrganizationFollowerCountGet) | **GET** /action/organization_follower_count | Get number of followers of an organization |
| [**actionOrganizationFollowerListGet**](ActionApi.md#actionOrganizationFollowerListGet) | **GET** /action/organization_follower_list | Get users following an organization |
| [**actionOrganizationListForUserGet**](ActionApi.md#actionOrganizationListForUserGet) | **GET** /action/organization_list_for_user | Get organizations that a user has a given permission for |
| [**actionOrganizationListGet**](ActionApi.md#actionOrganizationListGet) | **GET** /action/organization_list | Get names of all organizations |
| [**actionOrganizationRevisionListGet**](ActionApi.md#actionOrganizationRevisionListGet) | **GET** /action/organization_revision_list | Get organization revisions |
| [**actionOrganizationShowGet**](ActionApi.md#actionOrganizationShowGet) | **GET** /action/organization_show | Get details of a specific organization |
| [**actionPackageActivityListGet**](ActionApi.md#actionPackageActivityListGet) | **GET** /action/package_activity_list | Get the activity stream of a package (dataset) |
| [**actionPackageActivityListHtmlGet**](ActionApi.md#actionPackageActivityListHtmlGet) | **GET** /action/package_activity_list_html | Get the activity stream of a package (dataset), HTML format |
| [**actionPackageAutocompleteGet**](ActionApi.md#actionPackageAutocompleteGet) | **GET** /action/package_autocomplete | Find packages (datasets) matching a query |
| [**actionPackageListGet**](ActionApi.md#actionPackageListGet) | **GET** /action/package_list | Get a list of all packages (datasets) |
| [**actionPackageRelationshipsListGet**](ActionApi.md#actionPackageRelationshipsListGet) | **GET** /action/package_relationships_list | Get package (dataset) relationships |
| [**actionPackageRevisionListGet**](ActionApi.md#actionPackageRevisionListGet) | **GET** /action/package_revision_list | Get list of revisions for a package (dataset) |
| [**actionPackageSearchGet**](ActionApi.md#actionPackageSearchGet) | **GET** /action/package_search | Find packages (datasets) matching query terms |
| [**actionPackageShowGet**](ActionApi.md#actionPackageShowGet) | **GET** /action/package_show | Get metadata about one specific package (dataset) |
| [**actionRelatedListGet**](ActionApi.md#actionRelatedListGet) | **GET** /action/related_list | Gets items related to a package (dataset) |
| [**actionResourceSearchGet**](ActionApi.md#actionResourceSearchGet) | **GET** /action/resource_search | Find resources |
| [**actionResourceShowGet**](ActionApi.md#actionResourceShowGet) | **GET** /action/resource_show | Get metadata for a specific resource |
| [**actionStatusShowGet**](ActionApi.md#actionStatusShowGet) | **GET** /action/status_show | Get the site status |
| [**actionTagListGet**](ActionApi.md#actionTagListGet) | **GET** /action/tag_list | Get a list of tags |


<a id="actionOrganizationActivityListGet"></a>
# **actionOrganizationActivityListGet**
> actionOrganizationActivityListGet(id)

Get the activity stream of an organization

Return an organization&#39;s activity stream

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String id = "ministry-of-agriculture"; // String | The id or name of the organization
    try {
      apiInstance.actionOrganizationActivityListGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionOrganizationActivityListGet");
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
| **id** | **String**| The id or name of the organization | [optional] [default to ministry-of-agriculture] |

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of an organization&#39;s activities |  -  |

<a id="actionOrganizationActivityListHtmlGet"></a>
# **actionOrganizationActivityListHtmlGet**
> actionOrganizationActivityListHtmlGet(id)

Get the activity stream of an organization, HTML format

Return an organization&#39;s activity stream as HTML

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String id = "ministry-of-agriculture"; // String | The id or name of the organization
    try {
      apiInstance.actionOrganizationActivityListHtmlGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionOrganizationActivityListHtmlGet");
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
| **id** | **String**| The id or name of the organization | [optional] [default to ministry-of-agriculture] |

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of an organization&#39;s activities in HTML |  -  |

<a id="actionOrganizationAutocompleteGet"></a>
# **actionOrganizationAutocompleteGet**
> actionOrganizationAutocompleteGet(q, limit)

Get names of organizations that match a query string

Return a list of organization names that contain a string

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String q = "ministry"; // String | The string to search for
    Integer limit = 20; // Integer | The maximum number of organizations to return (optional)
    try {
      apiInstance.actionOrganizationAutocompleteGet(q, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionOrganizationAutocompleteGet");
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
| **q** | **String**| The string to search for | [optional] [default to ministry] |
| **limit** | **Integer**| The maximum number of organizations to return (optional) | [optional] [default to 20] |

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of organizations |  -  |

<a id="actionOrganizationFollowerCountGet"></a>
# **actionOrganizationFollowerCountGet**
> actionOrganizationFollowerCountGet(id)

Get number of followers of an organization

Return the number of followers of an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String id = "ministry-of-agriculture"; // String | The id or name of the organization
    try {
      apiInstance.actionOrganizationFollowerCountGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionOrganizationFollowerCountGet");
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
| **id** | **String**| The id or name of the organization | [optional] [default to ministry-of-agriculture] |

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Count of organization followers |  -  |

<a id="actionOrganizationFollowerListGet"></a>
# **actionOrganizationFollowerListGet**
> actionOrganizationFollowerListGet(id)

Get users following an organization

Return a list of users that are following a given organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String id = "ministry-of-agriculture"; // String | The id or name of the organization
    try {
      apiInstance.actionOrganizationFollowerListGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionOrganizationFollowerListGet");
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
| **id** | **String**| The id or name of the organization | [optional] [default to ministry-of-agriculture] |

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of organization followers |  -  |

<a id="actionOrganizationListForUserGet"></a>
# **actionOrganizationListForUserGet**
> actionOrganizationListForUserGet(permission)

Get organizations that a user has a given permission for

Return the organizations that the user has a given permission for

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String permission = "\\\"edit_group\\\""; // String | The permission the user has against the returned organization
    try {
      apiInstance.actionOrganizationListForUserGet(permission);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionOrganizationListForUserGet");
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
| **permission** | **String**| The permission the user has against the returned organization | [optional] [default to \&quot;edit_group\&quot;] |

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of organizations for given permission |  -  |

<a id="actionOrganizationListGet"></a>
# **actionOrganizationListGet**
> actionOrganizationListGet(offset, limit)

Get names of all organizations

Returns the names of all indexed organizations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    Integer offset = 0; // Integer | The offset (index) of the first organizations to return
    Integer limit = 100; // Integer | The number of organizations to be returned per page
    try {
      apiInstance.actionOrganizationListGet(offset, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionOrganizationListGet");
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
| **offset** | **Integer**| The offset (index) of the first organizations to return | [optional] [default to 0] |
| **limit** | **Integer**| The number of organizations to be returned per page | [optional] [default to 100] |

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of organizations |  -  |

<a id="actionOrganizationRevisionListGet"></a>
# **actionOrganizationRevisionListGet**
> actionOrganizationRevisionListGet(id)

Get organization revisions

Return an organization&#39;s revisions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String id = "ministry-of-agriculture"; // String | The name or id of the organization
    try {
      apiInstance.actionOrganizationRevisionListGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionOrganizationRevisionListGet");
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
| **id** | **String**| The name or id of the organization | [optional] [default to ministry-of-agriculture] |

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of an organization&#39;s revisions |  -  |

<a id="actionOrganizationShowGet"></a>
# **actionOrganizationShowGet**
> actionOrganizationShowGet(id, includeDatasets)

Get details of a specific organization

Return the details of an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String id = "ministry-of-agriculture"; // String | The id or name of the organization
    Boolean includeDatasets = true; // Boolean | include a list of the organization's datasets
    try {
      apiInstance.actionOrganizationShowGet(id, includeDatasets);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionOrganizationShowGet");
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
| **id** | **String**| The id or name of the organization | [optional] [default to ministry-of-agriculture] |
| **includeDatasets** | **Boolean**| include a list of the organization&#39;s datasets | [optional] [default to true] |

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List organization details |  -  |

<a id="actionPackageActivityListGet"></a>
# **actionPackageActivityListGet**
> actionPackageActivityListGet(id, offset, limit)

Get the activity stream of a package (dataset)

Returns a package&#39;s activity stream

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String id = "grizzly-bear-population-units"; // String | The id or name of the package
    Integer offset = 0; // Integer | Where to start getting activity items from
    Integer limit = 31; // Integer | The maximum number of activities to return
    try {
      apiInstance.actionPackageActivityListGet(id, offset, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionPackageActivityListGet");
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
| **id** | **String**| The id or name of the package | [optional] [default to grizzly-bear-population-units] |
| **offset** | **Integer**| Where to start getting activity items from | [optional] [default to 0] |
| **limit** | **Integer**| The maximum number of activities to return | [optional] [default to 31] |

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of activities |  -  |

<a id="actionPackageActivityListHtmlGet"></a>
# **actionPackageActivityListHtmlGet**
> actionPackageActivityListHtmlGet(id, offset, limit)

Get the activity stream of a package (dataset), HTML format

The activity stream is rendered as a snippet of HTML meant to be included in an HTML pag, i.e it doesn&#39;t have any header or footer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String id = "grizzly-bear-population-units"; // String | The id or name of the package
    Integer offset = 0; // Integer | Where to start getting activity items from
    Integer limit = 31; // Integer | The maximum number of activities to return
    try {
      apiInstance.actionPackageActivityListHtmlGet(id, offset, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionPackageActivityListHtmlGet");
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
| **id** | **String**| The id or name of the package | [optional] [default to grizzly-bear-population-units] |
| **offset** | **Integer**| Where to start getting activity items from | [optional] [default to 0] |
| **limit** | **Integer**| The maximum number of activities to return | [optional] [default to 31] |

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of activities rendered as HTML snippet |  -  |

<a id="actionPackageAutocompleteGet"></a>
# **actionPackageAutocompleteGet**
> actionPackageAutocompleteGet(q, limit)

Find packages (datasets) matching a query

Return a list of datasets that match a string

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String q = "\\\"Okanagan Lake\\\""; // String | The string to query
    Integer limit = 10; // Integer | The maximum number of resource formats to return
    try {
      apiInstance.actionPackageAutocompleteGet(q, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionPackageAutocompleteGet");
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
| **q** | **String**| The string to query | [optional] [default to \&quot;Okanagan Lake\&quot;] |
| **limit** | **Integer**| The maximum number of resource formats to return | [optional] [default to 10] |

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of datasets that match a string |  -  |

<a id="actionPackageListGet"></a>
# **actionPackageListGet**
> actionPackageListGet(offset, limit)

Get a list of all packages (datasets)

Returns the names of all indexed packages (datasets)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    Integer offset = 0; // Integer | The offset (index) of the first package to return
    Integer limit = 100; // Integer | The number of packages to be returned per page
    try {
      apiInstance.actionPackageListGet(offset, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionPackageListGet");
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
| **offset** | **Integer**| The offset (index) of the first package to return | [optional] [default to 0] |
| **limit** | **Integer**| The number of packages to be returned per page | [optional] [default to 100] |

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of packages |  -  |

<a id="actionPackageRelationshipsListGet"></a>
# **actionPackageRelationshipsListGet**
> actionPackageRelationshipsListGet(id, id2, rel)

Get package (dataset) relationships

Return a dataset&#39;s relationships

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String id = "grizzly-bear-population-units"; // String | The id or name of the first package
    String id2 = "important-fossil-areas"; // String | The id or name of the second package
    String rel = "rel_example"; // String | relationship as string
    try {
      apiInstance.actionPackageRelationshipsListGet(id, id2, rel);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionPackageRelationshipsListGet");
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
| **id** | **String**| The id or name of the first package | [optional] [default to grizzly-bear-population-units] |
| **id2** | **String**| The id or name of the second package | [optional] [default to important-fossil-areas] |
| **rel** | **String**| relationship as string | [optional] |

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of dataset relationships |  -  |

<a id="actionPackageRevisionListGet"></a>
# **actionPackageRevisionListGet**
> actionPackageRevisionListGet(id)

Get list of revisions for a package (dataset)

Return a dataset&#39;s revision as a list of dictionaries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String id = "grizzly-bear-population-units"; // String | The id or name of the dataset
    try {
      apiInstance.actionPackageRevisionListGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionPackageRevisionListGet");
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
| **id** | **String**| The id or name of the dataset | [optional] [default to grizzly-bear-population-units] |

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of dataset revisions |  -  |

<a id="actionPackageSearchGet"></a>
# **actionPackageSearchGet**
> actionPackageSearchGet(q)

Find packages (datasets) matching query terms

Searches for packages (datasets) matching the specified query terms

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String q = "\\\"Okanagan Lake\\\""; // String | A query string
    try {
      apiInstance.actionPackageSearchGet(q);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionPackageSearchGet");
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
| **q** | **String**| A query string | [optional] [default to \&quot;Okanagan Lake\&quot;] |

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of packages |  -  |

<a id="actionPackageShowGet"></a>
# **actionPackageShowGet**
> actionPackageShowGet(id)

Get metadata about one specific package (dataset)

Returns metadata about the package (dataset) corresponding to the specified unique name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String id = "grizzly-bear-population-units"; // String | The package name
    try {
      apiInstance.actionPackageShowGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionPackageShowGet");
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
| **id** | **String**| The package name | [optional] [default to grizzly-bear-population-units] |

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A package metadata object |  -  |

<a id="actionRelatedListGet"></a>
# **actionRelatedListGet**
> actionRelatedListGet(id, dataset, typeFilter, sort, featured)

Gets items related to a package (dataset)

Returns a dataset&#39;s related items.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String id = "id_example"; // String | id or name of the dataset (optional)
    String dataset = "dataset_example"; // String | Dataset dictionary of the dataset (optional)
    String typeFilter = "typeFilter_example"; // String | The type of related item to show (optional)
    String sort = "sort_example"; // String | The order to sort the related items in
    String featured = "featured_example"; // String | whether or not to restrict the results to only featured items
    try {
      apiInstance.actionRelatedListGet(id, dataset, typeFilter, sort, featured);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionRelatedListGet");
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
| **id** | **String**| id or name of the dataset (optional) | [optional] |
| **dataset** | **String**| Dataset dictionary of the dataset (optional) | [optional] |
| **typeFilter** | **String**| The type of related item to show (optional) | [optional] |
| **sort** | **String**| The order to sort the related items in | [optional] |
| **featured** | **String**| whether or not to restrict the results to only featured items | [optional] |

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Search for related items |  -  |

<a id="actionResourceSearchGet"></a>
# **actionResourceSearchGet**
> actionResourceSearchGet(query, fields, orderBy, offset, limit)

Find resources

Returns a dictionary with two fields &#x60;&#x60;count&#x60;&#x60; and &#x60;&#x60;results&#x60;&#x60;.             The &#x60;&#x60;count&#x60;&#x60; field contains the total number of Resources                found without the limit or query parameters having an effect.             The &#x60;&#x60;results&#x60;&#x60; field is a list of dictized Resource objects.             The query parameter is a required field. It is a string in                the form &#x60;&#x60;{field}:{term}&#x60;&#x60; or a list of strings, each of the             same form. Within each string, &#x60;&#x60;{field}&#x60;&#x60; is a field or extra             field on the Resource domain object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String query = "format:csv"; // String | The search criteria string or list of strings of the form ``{field}:{term1}``
    String fields = "fields_example"; // String | Depreciated
    String orderBy = "orderBy_example"; // String | A field on the resource model that orders the results
    Integer offset = 0; // Integer | Apply an offset to the query
    Integer limit = 0; // Integer | Apply a limit to the query
    try {
      apiInstance.actionResourceSearchGet(query, fields, orderBy, offset, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionResourceSearchGet");
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
| **query** | **String**| The search criteria string or list of strings of the form &#x60;&#x60;{field}:{term1}&#x60;&#x60; | [optional] [default to format:csv] |
| **fields** | **String**| Depreciated | [optional] |
| **orderBy** | **String**| A field on the resource model that orders the results | [optional] |
| **offset** | **Integer**| Apply an offset to the query | [optional] [default to 0] |
| **limit** | **Integer**| Apply a limit to the query | [optional] [default to 0] |

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Search for resources |  -  |

<a id="actionResourceShowGet"></a>
# **actionResourceShowGet**
> actionResourceShowGet(id, includeTracking)

Get metadata for a specific resource

Return the metadata of a resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String id = "e6c8bb1d-3726-418b-9b7e-1d97a9bbb817"; // String | The id of the resource
    Boolean includeTracking = false; // Boolean | Add tracking information to dataset
    try {
      apiInstance.actionResourceShowGet(id, includeTracking);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionResourceShowGet");
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
| **id** | **String**| The id of the resource | [optional] [default to e6c8bb1d-3726-418b-9b7e-1d97a9bbb817] |
| **includeTracking** | **Boolean**| Add tracking information to dataset | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return metadata of a resource |  -  |

<a id="actionStatusShowGet"></a>
# **actionStatusShowGet**
> actionStatusShowGet()

Get the site status

Returns the site status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    try {
      apiInstance.actionStatusShowGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionStatusShowGet");
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

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the site status, version, installed extensions |  -  |

<a id="actionTagListGet"></a>
# **actionTagListGet**
> actionTagListGet(offset, limit)

Get a list of tags

Returns the names of all indexed tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://catalogue.data.gov.bc.ca/api/3");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: githubAccessCode
    OAuth githubAccessCode = (OAuth) defaultClient.getAuthentication("githubAccessCode");
    githubAccessCode.setAccessToken("YOUR ACCESS TOKEN");

    ActionApi apiInstance = new ActionApi(defaultClient);
    Integer offset = 0; // Integer | The offset (index) of the first tag to return
    Integer limit = 100; // Integer | The number of tags to be returned per page
    try {
      apiInstance.actionTagListGet(offset, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#actionTagListGet");
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
| **offset** | **Integer**| The offset (index) of the first tag to return | [optional] [default to 0] |
| **limit** | **Integer**| The number of tags to be returned per page | [optional] [default to 100] |

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of tags |  -  |

