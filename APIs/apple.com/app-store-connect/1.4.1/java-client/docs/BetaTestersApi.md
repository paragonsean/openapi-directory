# BetaTestersApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**betaTestersAppsDeleteToManyRelationship**](BetaTestersApi.md#betaTestersAppsDeleteToManyRelationship) | **DELETE** /v1/betaTesters/{id}/relationships/apps |  |
| [**betaTestersAppsGetToManyRelated**](BetaTestersApi.md#betaTestersAppsGetToManyRelated) | **GET** /v1/betaTesters/{id}/apps |  |
| [**betaTestersAppsGetToManyRelationship**](BetaTestersApi.md#betaTestersAppsGetToManyRelationship) | **GET** /v1/betaTesters/{id}/relationships/apps |  |
| [**betaTestersBetaGroupsCreateToManyRelationship**](BetaTestersApi.md#betaTestersBetaGroupsCreateToManyRelationship) | **POST** /v1/betaTesters/{id}/relationships/betaGroups |  |
| [**betaTestersBetaGroupsDeleteToManyRelationship**](BetaTestersApi.md#betaTestersBetaGroupsDeleteToManyRelationship) | **DELETE** /v1/betaTesters/{id}/relationships/betaGroups |  |
| [**betaTestersBetaGroupsGetToManyRelated**](BetaTestersApi.md#betaTestersBetaGroupsGetToManyRelated) | **GET** /v1/betaTesters/{id}/betaGroups |  |
| [**betaTestersBetaGroupsGetToManyRelationship**](BetaTestersApi.md#betaTestersBetaGroupsGetToManyRelationship) | **GET** /v1/betaTesters/{id}/relationships/betaGroups |  |
| [**betaTestersBuildsCreateToManyRelationship**](BetaTestersApi.md#betaTestersBuildsCreateToManyRelationship) | **POST** /v1/betaTesters/{id}/relationships/builds |  |
| [**betaTestersBuildsDeleteToManyRelationship**](BetaTestersApi.md#betaTestersBuildsDeleteToManyRelationship) | **DELETE** /v1/betaTesters/{id}/relationships/builds |  |
| [**betaTestersBuildsGetToManyRelated**](BetaTestersApi.md#betaTestersBuildsGetToManyRelated) | **GET** /v1/betaTesters/{id}/builds |  |
| [**betaTestersBuildsGetToManyRelationship**](BetaTestersApi.md#betaTestersBuildsGetToManyRelationship) | **GET** /v1/betaTesters/{id}/relationships/builds |  |
| [**betaTestersCreateInstance**](BetaTestersApi.md#betaTestersCreateInstance) | **POST** /v1/betaTesters |  |
| [**betaTestersDeleteInstance**](BetaTestersApi.md#betaTestersDeleteInstance) | **DELETE** /v1/betaTesters/{id} |  |
| [**betaTestersGetCollection**](BetaTestersApi.md#betaTestersGetCollection) | **GET** /v1/betaTesters |  |
| [**betaTestersGetInstance**](BetaTestersApi.md#betaTestersGetInstance) | **GET** /v1/betaTesters/{id} |  |


<a id="betaTestersAppsDeleteToManyRelationship"></a>
# **betaTestersAppsDeleteToManyRelationship**
> betaTestersAppsDeleteToManyRelationship(id, betaTesterAppsLinkagesRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaTestersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaTestersApi apiInstance = new BetaTestersApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    BetaTesterAppsLinkagesRequest betaTesterAppsLinkagesRequest = new BetaTesterAppsLinkagesRequest(); // BetaTesterAppsLinkagesRequest | List of related linkages
    try {
      apiInstance.betaTestersAppsDeleteToManyRelationship(id, betaTesterAppsLinkagesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaTestersApi#betaTestersAppsDeleteToManyRelationship");
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
| **id** | **String**| the id of the requested resource | |
| **betaTesterAppsLinkagesRequest** | [**BetaTesterAppsLinkagesRequest**](BetaTesterAppsLinkagesRequest.md)| List of related linkages | |

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success (no content) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="betaTestersAppsGetToManyRelated"></a>
# **betaTestersAppsGetToManyRelated**
> AppsResponse betaTestersAppsGetToManyRelated(id, fieldsApps, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaTestersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaTestersApi apiInstance = new BetaTestersApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    Integer limit = 56; // Integer | maximum resources per page
    try {
      AppsResponse result = apiInstance.betaTestersAppsGetToManyRelated(id, fieldsApps, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaTestersApi#betaTestersAppsGetToManyRelated");
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
| **id** | **String**| the id of the requested resource | |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**AppsResponse**](AppsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of related resources |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="betaTestersAppsGetToManyRelationship"></a>
# **betaTestersAppsGetToManyRelationship**
> BetaTesterAppsLinkagesResponse betaTestersAppsGetToManyRelationship(id, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaTestersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaTestersApi apiInstance = new BetaTestersApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    Integer limit = 56; // Integer | maximum resources per page
    try {
      BetaTesterAppsLinkagesResponse result = apiInstance.betaTestersAppsGetToManyRelationship(id, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaTestersApi#betaTestersAppsGetToManyRelationship");
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
| **id** | **String**| the id of the requested resource | |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**BetaTesterAppsLinkagesResponse**](BetaTesterAppsLinkagesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of related linkages |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="betaTestersBetaGroupsCreateToManyRelationship"></a>
# **betaTestersBetaGroupsCreateToManyRelationship**
> betaTestersBetaGroupsCreateToManyRelationship(id, betaTesterBetaGroupsLinkagesRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaTestersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaTestersApi apiInstance = new BetaTestersApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    BetaTesterBetaGroupsLinkagesRequest betaTesterBetaGroupsLinkagesRequest = new BetaTesterBetaGroupsLinkagesRequest(); // BetaTesterBetaGroupsLinkagesRequest | List of related linkages
    try {
      apiInstance.betaTestersBetaGroupsCreateToManyRelationship(id, betaTesterBetaGroupsLinkagesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaTestersApi#betaTestersBetaGroupsCreateToManyRelationship");
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
| **id** | **String**| the id of the requested resource | |
| **betaTesterBetaGroupsLinkagesRequest** | [**BetaTesterBetaGroupsLinkagesRequest**](BetaTesterBetaGroupsLinkagesRequest.md)| List of related linkages | |

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success (no content) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="betaTestersBetaGroupsDeleteToManyRelationship"></a>
# **betaTestersBetaGroupsDeleteToManyRelationship**
> betaTestersBetaGroupsDeleteToManyRelationship(id, betaTesterBetaGroupsLinkagesRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaTestersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaTestersApi apiInstance = new BetaTestersApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    BetaTesterBetaGroupsLinkagesRequest betaTesterBetaGroupsLinkagesRequest = new BetaTesterBetaGroupsLinkagesRequest(); // BetaTesterBetaGroupsLinkagesRequest | List of related linkages
    try {
      apiInstance.betaTestersBetaGroupsDeleteToManyRelationship(id, betaTesterBetaGroupsLinkagesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaTestersApi#betaTestersBetaGroupsDeleteToManyRelationship");
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
| **id** | **String**| the id of the requested resource | |
| **betaTesterBetaGroupsLinkagesRequest** | [**BetaTesterBetaGroupsLinkagesRequest**](BetaTesterBetaGroupsLinkagesRequest.md)| List of related linkages | |

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success (no content) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="betaTestersBetaGroupsGetToManyRelated"></a>
# **betaTestersBetaGroupsGetToManyRelated**
> BetaGroupsResponse betaTestersBetaGroupsGetToManyRelated(id, fieldsBetaGroups, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaTestersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaTestersApi apiInstance = new BetaTestersApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBetaGroups = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaGroups
    Integer limit = 56; // Integer | maximum resources per page
    try {
      BetaGroupsResponse result = apiInstance.betaTestersBetaGroupsGetToManyRelated(id, fieldsBetaGroups, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaTestersApi#betaTestersBetaGroupsGetToManyRelated");
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
| **id** | **String**| the id of the requested resource | |
| **fieldsBetaGroups** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaGroups | [optional] [enum: app, betaTesters, builds, createdDate, feedbackEnabled, isInternalGroup, name, publicLink, publicLinkEnabled, publicLinkId, publicLinkLimit, publicLinkLimitEnabled] |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**BetaGroupsResponse**](BetaGroupsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of related resources |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="betaTestersBetaGroupsGetToManyRelationship"></a>
# **betaTestersBetaGroupsGetToManyRelationship**
> BetaTesterBetaGroupsLinkagesResponse betaTestersBetaGroupsGetToManyRelationship(id, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaTestersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaTestersApi apiInstance = new BetaTestersApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    Integer limit = 56; // Integer | maximum resources per page
    try {
      BetaTesterBetaGroupsLinkagesResponse result = apiInstance.betaTestersBetaGroupsGetToManyRelationship(id, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaTestersApi#betaTestersBetaGroupsGetToManyRelationship");
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
| **id** | **String**| the id of the requested resource | |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**BetaTesterBetaGroupsLinkagesResponse**](BetaTesterBetaGroupsLinkagesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of related linkages |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="betaTestersBuildsCreateToManyRelationship"></a>
# **betaTestersBuildsCreateToManyRelationship**
> betaTestersBuildsCreateToManyRelationship(id, betaTesterBuildsLinkagesRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaTestersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaTestersApi apiInstance = new BetaTestersApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    BetaTesterBuildsLinkagesRequest betaTesterBuildsLinkagesRequest = new BetaTesterBuildsLinkagesRequest(); // BetaTesterBuildsLinkagesRequest | List of related linkages
    try {
      apiInstance.betaTestersBuildsCreateToManyRelationship(id, betaTesterBuildsLinkagesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaTestersApi#betaTestersBuildsCreateToManyRelationship");
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
| **id** | **String**| the id of the requested resource | |
| **betaTesterBuildsLinkagesRequest** | [**BetaTesterBuildsLinkagesRequest**](BetaTesterBuildsLinkagesRequest.md)| List of related linkages | |

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success (no content) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="betaTestersBuildsDeleteToManyRelationship"></a>
# **betaTestersBuildsDeleteToManyRelationship**
> betaTestersBuildsDeleteToManyRelationship(id, betaTesterBuildsLinkagesRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaTestersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaTestersApi apiInstance = new BetaTestersApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    BetaTesterBuildsLinkagesRequest betaTesterBuildsLinkagesRequest = new BetaTesterBuildsLinkagesRequest(); // BetaTesterBuildsLinkagesRequest | List of related linkages
    try {
      apiInstance.betaTestersBuildsDeleteToManyRelationship(id, betaTesterBuildsLinkagesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaTestersApi#betaTestersBuildsDeleteToManyRelationship");
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
| **id** | **String**| the id of the requested resource | |
| **betaTesterBuildsLinkagesRequest** | [**BetaTesterBuildsLinkagesRequest**](BetaTesterBuildsLinkagesRequest.md)| List of related linkages | |

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success (no content) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="betaTestersBuildsGetToManyRelated"></a>
# **betaTestersBuildsGetToManyRelated**
> BuildsResponse betaTestersBuildsGetToManyRelated(id, fieldsBuilds, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaTestersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaTestersApi apiInstance = new BetaTestersApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    Integer limit = 56; // Integer | maximum resources per page
    try {
      BuildsResponse result = apiInstance.betaTestersBuildsGetToManyRelated(id, fieldsBuilds, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaTestersApi#betaTestersBuildsGetToManyRelated");
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
| **id** | **String**| the id of the requested resource | |
| **fieldsBuilds** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type builds | [optional] [enum: app, appEncryptionDeclaration, appStoreVersion, betaAppReviewSubmission, betaBuildLocalizations, betaGroups, buildBetaDetail, diagnosticSignatures, expirationDate, expired, iconAssetToken, icons, individualTesters, minOsVersion, perfPowerMetrics, preReleaseVersion, processingState, uploadedDate, usesNonExemptEncryption, version] |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**BuildsResponse**](BuildsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of related resources |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="betaTestersBuildsGetToManyRelationship"></a>
# **betaTestersBuildsGetToManyRelationship**
> BetaTesterBuildsLinkagesResponse betaTestersBuildsGetToManyRelationship(id, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaTestersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaTestersApi apiInstance = new BetaTestersApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    Integer limit = 56; // Integer | maximum resources per page
    try {
      BetaTesterBuildsLinkagesResponse result = apiInstance.betaTestersBuildsGetToManyRelationship(id, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaTestersApi#betaTestersBuildsGetToManyRelationship");
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
| **id** | **String**| the id of the requested resource | |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**BetaTesterBuildsLinkagesResponse**](BetaTesterBuildsLinkagesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of related linkages |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="betaTestersCreateInstance"></a>
# **betaTestersCreateInstance**
> BetaTesterResponse betaTestersCreateInstance(betaTesterCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaTestersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaTestersApi apiInstance = new BetaTestersApi(defaultClient);
    BetaTesterCreateRequest betaTesterCreateRequest = new BetaTesterCreateRequest(); // BetaTesterCreateRequest | BetaTester representation
    try {
      BetaTesterResponse result = apiInstance.betaTestersCreateInstance(betaTesterCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaTestersApi#betaTestersCreateInstance");
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
| **betaTesterCreateRequest** | [**BetaTesterCreateRequest**](BetaTesterCreateRequest.md)| BetaTester representation | |

### Return type

[**BetaTesterResponse**](BetaTesterResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single BetaTester |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="betaTestersDeleteInstance"></a>
# **betaTestersDeleteInstance**
> betaTestersDeleteInstance(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaTestersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaTestersApi apiInstance = new BetaTestersApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    try {
      apiInstance.betaTestersDeleteInstance(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaTestersApi#betaTestersDeleteInstance");
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
| **id** | **String**| the id of the requested resource | |

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success (no content) |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="betaTestersGetCollection"></a>
# **betaTestersGetCollection**
> BetaTestersResponse betaTestersGetCollection(filterEmail, filterFirstName, filterInviteType, filterLastName, filterApps, filterBetaGroups, filterBuilds, sort, fieldsBetaTesters, limit, include, fieldsBetaGroups, fieldsBuilds, fieldsApps, limitApps, limitBetaGroups, limitBuilds)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaTestersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaTestersApi apiInstance = new BetaTestersApi(defaultClient);
    List<String> filterEmail = Arrays.asList(); // List<String> | filter by attribute 'email'
    List<String> filterFirstName = Arrays.asList(); // List<String> | filter by attribute 'firstName'
    List<String> filterInviteType = Arrays.asList(); // List<String> | filter by attribute 'inviteType'
    List<String> filterLastName = Arrays.asList(); // List<String> | filter by attribute 'lastName'
    List<String> filterApps = Arrays.asList(); // List<String> | filter by id(s) of related 'apps'
    List<String> filterBetaGroups = Arrays.asList(); // List<String> | filter by id(s) of related 'betaGroups'
    List<String> filterBuilds = Arrays.asList(); // List<String> | filter by id(s) of related 'builds'
    List<String> sort = Arrays.asList(); // List<String> | comma-separated list of sort expressions; resources will be sorted as specified
    List<String> fieldsBetaTesters = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaTesters
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsBetaGroups = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaGroups
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    Integer limitApps = 56; // Integer | maximum number of related apps returned (when they are included)
    Integer limitBetaGroups = 56; // Integer | maximum number of related betaGroups returned (when they are included)
    Integer limitBuilds = 56; // Integer | maximum number of related builds returned (when they are included)
    try {
      BetaTestersResponse result = apiInstance.betaTestersGetCollection(filterEmail, filterFirstName, filterInviteType, filterLastName, filterApps, filterBetaGroups, filterBuilds, sort, fieldsBetaTesters, limit, include, fieldsBetaGroups, fieldsBuilds, fieldsApps, limitApps, limitBetaGroups, limitBuilds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaTestersApi#betaTestersGetCollection");
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
| **filterEmail** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;email&#39; | [optional] |
| **filterFirstName** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;firstName&#39; | [optional] |
| **filterInviteType** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;inviteType&#39; | [optional] [enum: EMAIL, PUBLIC_LINK] |
| **filterLastName** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;lastName&#39; | [optional] |
| **filterApps** | [**List&lt;String&gt;**](String.md)| filter by id(s) of related &#39;apps&#39; | [optional] |
| **filterBetaGroups** | [**List&lt;String&gt;**](String.md)| filter by id(s) of related &#39;betaGroups&#39; | [optional] |
| **filterBuilds** | [**List&lt;String&gt;**](String.md)| filter by id(s) of related &#39;builds&#39; | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| comma-separated list of sort expressions; resources will be sorted as specified | [optional] [enum: email, -email, firstName, -firstName, inviteType, -inviteType, lastName, -lastName] |
| **fieldsBetaTesters** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaTesters | [optional] [enum: apps, betaGroups, builds, email, firstName, inviteType, lastName] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: apps, betaGroups, builds] |
| **fieldsBetaGroups** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaGroups | [optional] [enum: app, betaTesters, builds, createdDate, feedbackEnabled, isInternalGroup, name, publicLink, publicLinkEnabled, publicLinkId, publicLinkLimit, publicLinkLimitEnabled] |
| **fieldsBuilds** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type builds | [optional] [enum: app, appEncryptionDeclaration, appStoreVersion, betaAppReviewSubmission, betaBuildLocalizations, betaGroups, buildBetaDetail, diagnosticSignatures, expirationDate, expired, iconAssetToken, icons, individualTesters, minOsVersion, perfPowerMetrics, preReleaseVersion, processingState, uploadedDate, usesNonExemptEncryption, version] |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |
| **limitApps** | **Integer**| maximum number of related apps returned (when they are included) | [optional] |
| **limitBetaGroups** | **Integer**| maximum number of related betaGroups returned (when they are included) | [optional] |
| **limitBuilds** | **Integer**| maximum number of related builds returned (when they are included) | [optional] |

### Return type

[**BetaTestersResponse**](BetaTestersResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of BetaTesters |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |

<a id="betaTestersGetInstance"></a>
# **betaTestersGetInstance**
> BetaTesterResponse betaTestersGetInstance(id, fieldsBetaTesters, include, fieldsBetaGroups, fieldsBuilds, fieldsApps, limitApps, limitBetaGroups, limitBuilds)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaTestersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaTestersApi apiInstance = new BetaTestersApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBetaTesters = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaTesters
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsBetaGroups = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaGroups
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    Integer limitApps = 56; // Integer | maximum number of related apps returned (when they are included)
    Integer limitBetaGroups = 56; // Integer | maximum number of related betaGroups returned (when they are included)
    Integer limitBuilds = 56; // Integer | maximum number of related builds returned (when they are included)
    try {
      BetaTesterResponse result = apiInstance.betaTestersGetInstance(id, fieldsBetaTesters, include, fieldsBetaGroups, fieldsBuilds, fieldsApps, limitApps, limitBetaGroups, limitBuilds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaTestersApi#betaTestersGetInstance");
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
| **id** | **String**| the id of the requested resource | |
| **fieldsBetaTesters** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaTesters | [optional] [enum: apps, betaGroups, builds, email, firstName, inviteType, lastName] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: apps, betaGroups, builds] |
| **fieldsBetaGroups** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaGroups | [optional] [enum: app, betaTesters, builds, createdDate, feedbackEnabled, isInternalGroup, name, publicLink, publicLinkEnabled, publicLinkId, publicLinkLimit, publicLinkLimitEnabled] |
| **fieldsBuilds** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type builds | [optional] [enum: app, appEncryptionDeclaration, appStoreVersion, betaAppReviewSubmission, betaBuildLocalizations, betaGroups, buildBetaDetail, diagnosticSignatures, expirationDate, expired, iconAssetToken, icons, individualTesters, minOsVersion, perfPowerMetrics, preReleaseVersion, processingState, uploadedDate, usesNonExemptEncryption, version] |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |
| **limitApps** | **Integer**| maximum number of related apps returned (when they are included) | [optional] |
| **limitBetaGroups** | **Integer**| maximum number of related betaGroups returned (when they are included) | [optional] |
| **limitBuilds** | **Integer**| maximum number of related builds returned (when they are included) | [optional] |

### Return type

[**BetaTesterResponse**](BetaTesterResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single BetaTester |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

