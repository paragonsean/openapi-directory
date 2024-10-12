# OtherApi

All URIs are relative to *https://api.figshare.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**categoriesList**](OtherApi.md#categoriesList) | **GET** /categories | Public Categories |
| [**fileDownload**](OtherApi.md#fileDownload) | **GET** /file/download/{file_id} | Public File Download |
| [**itemTypesList**](OtherApi.md#itemTypesList) | **GET** /item_types | Item Types |
| [**licensesList**](OtherApi.md#licensesList) | **GET** /licenses | Public Licenses |
| [**privateAccount**](OtherApi.md#privateAccount) | **GET** /account | Private Account information |
| [**privateFundingSearch**](OtherApi.md#privateFundingSearch) | **POST** /account/funding/search | Search Funding |
| [**privateLicensesList**](OtherApi.md#privateLicensesList) | **GET** /account/licenses | Private Account Licenses |


<a id="categoriesList"></a>
# **categoriesList**
> List&lt;Category&gt; categoriesList()

Public Categories

Returns a list of public categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OtherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");

    OtherApi apiInstance = new OtherApi(defaultClient);
    try {
      List<Category> result = apiInstance.categoriesList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OtherApi#categoriesList");
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

[**List&lt;Category&gt;**](Category.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of categories |  -  |
| **500** | Internal Server Error |  -  |

<a id="fileDownload"></a>
# **fileDownload**
> fileDownload(fileId)

Public File Download

Starts the download of a file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OtherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");

    OtherApi apiInstance = new OtherApi(defaultClient);
    Long fileId = 56L; // Long | 
    try {
      apiInstance.fileDownload(fileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OtherApi#fileDownload");
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
| **fileId** | **Long**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **500** | Internal Server Error |  -  |

<a id="itemTypesList"></a>
# **itemTypesList**
> List&lt;ItemType&gt; itemTypesList(groupId)

Item Types

Returns the list of Item Types of the requested group. If no user is authenticated, returns the item types available for Figshare.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OtherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    OtherApi apiInstance = new OtherApi(defaultClient);
    Long groupId = 0L; // Long | Identifier of the group for which the item types are requested
    try {
      List<ItemType> result = apiInstance.itemTypesList(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OtherApi#itemTypesList");
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
| **groupId** | **Long**| Identifier of the group for which the item types are requested | [optional] [default to 0] |

### Return type

[**List&lt;ItemType&gt;**](ItemType.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of item types |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="licensesList"></a>
# **licensesList**
> List&lt;License&gt; licensesList()

Public Licenses

Returns a list of public licenses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OtherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");

    OtherApi apiInstance = new OtherApi(defaultClient);
    try {
      List<License> result = apiInstance.licensesList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OtherApi#licensesList");
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

[**List&lt;License&gt;**](License.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of licenses |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateAccount"></a>
# **privateAccount**
> Account privateAccount()

Private Account information

Account information for token/personal token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OtherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    OtherApi apiInstance = new OtherApi(defaultClient);
    try {
      Account result = apiInstance.privateAccount();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OtherApi#privateAccount");
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

[**Account**](Account.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Account representation |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateFundingSearch"></a>
# **privateFundingSearch**
> List&lt;FundingInformation&gt; privateFundingSearch(fundingSearch)

Search Funding

Search for fundings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OtherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    OtherApi apiInstance = new OtherApi(defaultClient);
    FundingSearch fundingSearch = new FundingSearch(); // FundingSearch | Search Parameters
    try {
      List<FundingInformation> result = apiInstance.privateFundingSearch(fundingSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OtherApi#privateFundingSearch");
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
| **fundingSearch** | [**FundingSearch**](FundingSearch.md)| Search Parameters | [optional] |

### Return type

[**List&lt;FundingInformation&gt;**](FundingInformation.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of funding information |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateLicensesList"></a>
# **privateLicensesList**
> List&lt;License&gt; privateLicensesList()

Private Account Licenses

This is a private endpoint that requires OAuth. It will return a list with figshare public licenses AND licenses defined for account&#39;s institution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OtherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    OtherApi apiInstance = new OtherApi(defaultClient);
    try {
      List<License> result = apiInstance.privateLicensesList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OtherApi#privateLicensesList");
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

[**List&lt;License&gt;**](License.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of personal licenses |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

