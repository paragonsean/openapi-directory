# BetaGroupsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**betaGroupsAppGetToOneRelated**](BetaGroupsApi.md#betaGroupsAppGetToOneRelated) | **GET** /v1/betaGroups/{id}/app |  |
| [**betaGroupsBetaTestersCreateToManyRelationship**](BetaGroupsApi.md#betaGroupsBetaTestersCreateToManyRelationship) | **POST** /v1/betaGroups/{id}/relationships/betaTesters |  |
| [**betaGroupsBetaTestersDeleteToManyRelationship**](BetaGroupsApi.md#betaGroupsBetaTestersDeleteToManyRelationship) | **DELETE** /v1/betaGroups/{id}/relationships/betaTesters |  |
| [**betaGroupsBetaTestersGetToManyRelated**](BetaGroupsApi.md#betaGroupsBetaTestersGetToManyRelated) | **GET** /v1/betaGroups/{id}/betaTesters |  |
| [**betaGroupsBetaTestersGetToManyRelationship**](BetaGroupsApi.md#betaGroupsBetaTestersGetToManyRelationship) | **GET** /v1/betaGroups/{id}/relationships/betaTesters |  |
| [**betaGroupsBuildsCreateToManyRelationship**](BetaGroupsApi.md#betaGroupsBuildsCreateToManyRelationship) | **POST** /v1/betaGroups/{id}/relationships/builds |  |
| [**betaGroupsBuildsDeleteToManyRelationship**](BetaGroupsApi.md#betaGroupsBuildsDeleteToManyRelationship) | **DELETE** /v1/betaGroups/{id}/relationships/builds |  |
| [**betaGroupsBuildsGetToManyRelated**](BetaGroupsApi.md#betaGroupsBuildsGetToManyRelated) | **GET** /v1/betaGroups/{id}/builds |  |
| [**betaGroupsBuildsGetToManyRelationship**](BetaGroupsApi.md#betaGroupsBuildsGetToManyRelationship) | **GET** /v1/betaGroups/{id}/relationships/builds |  |
| [**betaGroupsCreateInstance**](BetaGroupsApi.md#betaGroupsCreateInstance) | **POST** /v1/betaGroups |  |
| [**betaGroupsDeleteInstance**](BetaGroupsApi.md#betaGroupsDeleteInstance) | **DELETE** /v1/betaGroups/{id} |  |
| [**betaGroupsGetCollection**](BetaGroupsApi.md#betaGroupsGetCollection) | **GET** /v1/betaGroups |  |
| [**betaGroupsGetInstance**](BetaGroupsApi.md#betaGroupsGetInstance) | **GET** /v1/betaGroups/{id} |  |
| [**betaGroupsUpdateInstance**](BetaGroupsApi.md#betaGroupsUpdateInstance) | **PATCH** /v1/betaGroups/{id} |  |


<a id="betaGroupsAppGetToOneRelated"></a>
# **betaGroupsAppGetToOneRelated**
> AppResponse betaGroupsAppGetToOneRelated(id, fieldsApps)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaGroupsApi apiInstance = new BetaGroupsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    try {
      AppResponse result = apiInstance.betaGroupsAppGetToOneRelated(id, fieldsApps);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaGroupsApi#betaGroupsAppGetToOneRelated");
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

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Related resource |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="betaGroupsBetaTestersCreateToManyRelationship"></a>
# **betaGroupsBetaTestersCreateToManyRelationship**
> betaGroupsBetaTestersCreateToManyRelationship(id, betaGroupBetaTestersLinkagesRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaGroupsApi apiInstance = new BetaGroupsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    BetaGroupBetaTestersLinkagesRequest betaGroupBetaTestersLinkagesRequest = new BetaGroupBetaTestersLinkagesRequest(); // BetaGroupBetaTestersLinkagesRequest | List of related linkages
    try {
      apiInstance.betaGroupsBetaTestersCreateToManyRelationship(id, betaGroupBetaTestersLinkagesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaGroupsApi#betaGroupsBetaTestersCreateToManyRelationship");
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
| **betaGroupBetaTestersLinkagesRequest** | [**BetaGroupBetaTestersLinkagesRequest**](BetaGroupBetaTestersLinkagesRequest.md)| List of related linkages | |

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

<a id="betaGroupsBetaTestersDeleteToManyRelationship"></a>
# **betaGroupsBetaTestersDeleteToManyRelationship**
> betaGroupsBetaTestersDeleteToManyRelationship(id, betaGroupBetaTestersLinkagesRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaGroupsApi apiInstance = new BetaGroupsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    BetaGroupBetaTestersLinkagesRequest betaGroupBetaTestersLinkagesRequest = new BetaGroupBetaTestersLinkagesRequest(); // BetaGroupBetaTestersLinkagesRequest | List of related linkages
    try {
      apiInstance.betaGroupsBetaTestersDeleteToManyRelationship(id, betaGroupBetaTestersLinkagesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaGroupsApi#betaGroupsBetaTestersDeleteToManyRelationship");
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
| **betaGroupBetaTestersLinkagesRequest** | [**BetaGroupBetaTestersLinkagesRequest**](BetaGroupBetaTestersLinkagesRequest.md)| List of related linkages | |

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

<a id="betaGroupsBetaTestersGetToManyRelated"></a>
# **betaGroupsBetaTestersGetToManyRelated**
> BetaTestersResponse betaGroupsBetaTestersGetToManyRelated(id, fieldsBetaTesters, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaGroupsApi apiInstance = new BetaGroupsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBetaTesters = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaTesters
    Integer limit = 56; // Integer | maximum resources per page
    try {
      BetaTestersResponse result = apiInstance.betaGroupsBetaTestersGetToManyRelated(id, fieldsBetaTesters, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaGroupsApi#betaGroupsBetaTestersGetToManyRelated");
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
| **limit** | **Integer**| maximum resources per page | [optional] |

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
| **200** | List of related resources |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="betaGroupsBetaTestersGetToManyRelationship"></a>
# **betaGroupsBetaTestersGetToManyRelationship**
> BetaGroupBetaTestersLinkagesResponse betaGroupsBetaTestersGetToManyRelationship(id, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaGroupsApi apiInstance = new BetaGroupsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    Integer limit = 56; // Integer | maximum resources per page
    try {
      BetaGroupBetaTestersLinkagesResponse result = apiInstance.betaGroupsBetaTestersGetToManyRelationship(id, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaGroupsApi#betaGroupsBetaTestersGetToManyRelationship");
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

[**BetaGroupBetaTestersLinkagesResponse**](BetaGroupBetaTestersLinkagesResponse.md)

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

<a id="betaGroupsBuildsCreateToManyRelationship"></a>
# **betaGroupsBuildsCreateToManyRelationship**
> betaGroupsBuildsCreateToManyRelationship(id, betaGroupBuildsLinkagesRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaGroupsApi apiInstance = new BetaGroupsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    BetaGroupBuildsLinkagesRequest betaGroupBuildsLinkagesRequest = new BetaGroupBuildsLinkagesRequest(); // BetaGroupBuildsLinkagesRequest | List of related linkages
    try {
      apiInstance.betaGroupsBuildsCreateToManyRelationship(id, betaGroupBuildsLinkagesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaGroupsApi#betaGroupsBuildsCreateToManyRelationship");
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
| **betaGroupBuildsLinkagesRequest** | [**BetaGroupBuildsLinkagesRequest**](BetaGroupBuildsLinkagesRequest.md)| List of related linkages | |

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

<a id="betaGroupsBuildsDeleteToManyRelationship"></a>
# **betaGroupsBuildsDeleteToManyRelationship**
> betaGroupsBuildsDeleteToManyRelationship(id, betaGroupBuildsLinkagesRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaGroupsApi apiInstance = new BetaGroupsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    BetaGroupBuildsLinkagesRequest betaGroupBuildsLinkagesRequest = new BetaGroupBuildsLinkagesRequest(); // BetaGroupBuildsLinkagesRequest | List of related linkages
    try {
      apiInstance.betaGroupsBuildsDeleteToManyRelationship(id, betaGroupBuildsLinkagesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaGroupsApi#betaGroupsBuildsDeleteToManyRelationship");
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
| **betaGroupBuildsLinkagesRequest** | [**BetaGroupBuildsLinkagesRequest**](BetaGroupBuildsLinkagesRequest.md)| List of related linkages | |

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

<a id="betaGroupsBuildsGetToManyRelated"></a>
# **betaGroupsBuildsGetToManyRelated**
> BuildsResponse betaGroupsBuildsGetToManyRelated(id, fieldsBuilds, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaGroupsApi apiInstance = new BetaGroupsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    Integer limit = 56; // Integer | maximum resources per page
    try {
      BuildsResponse result = apiInstance.betaGroupsBuildsGetToManyRelated(id, fieldsBuilds, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaGroupsApi#betaGroupsBuildsGetToManyRelated");
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

<a id="betaGroupsBuildsGetToManyRelationship"></a>
# **betaGroupsBuildsGetToManyRelationship**
> BetaGroupBuildsLinkagesResponse betaGroupsBuildsGetToManyRelationship(id, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaGroupsApi apiInstance = new BetaGroupsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    Integer limit = 56; // Integer | maximum resources per page
    try {
      BetaGroupBuildsLinkagesResponse result = apiInstance.betaGroupsBuildsGetToManyRelationship(id, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaGroupsApi#betaGroupsBuildsGetToManyRelationship");
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

[**BetaGroupBuildsLinkagesResponse**](BetaGroupBuildsLinkagesResponse.md)

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

<a id="betaGroupsCreateInstance"></a>
# **betaGroupsCreateInstance**
> BetaGroupResponse betaGroupsCreateInstance(betaGroupCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaGroupsApi apiInstance = new BetaGroupsApi(defaultClient);
    BetaGroupCreateRequest betaGroupCreateRequest = new BetaGroupCreateRequest(); // BetaGroupCreateRequest | BetaGroup representation
    try {
      BetaGroupResponse result = apiInstance.betaGroupsCreateInstance(betaGroupCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaGroupsApi#betaGroupsCreateInstance");
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
| **betaGroupCreateRequest** | [**BetaGroupCreateRequest**](BetaGroupCreateRequest.md)| BetaGroup representation | |

### Return type

[**BetaGroupResponse**](BetaGroupResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single BetaGroup |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="betaGroupsDeleteInstance"></a>
# **betaGroupsDeleteInstance**
> betaGroupsDeleteInstance(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaGroupsApi apiInstance = new BetaGroupsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    try {
      apiInstance.betaGroupsDeleteInstance(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaGroupsApi#betaGroupsDeleteInstance");
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

<a id="betaGroupsGetCollection"></a>
# **betaGroupsGetCollection**
> BetaGroupsResponse betaGroupsGetCollection(filterIsInternalGroup, filterName, filterPublicLink, filterPublicLinkEnabled, filterPublicLinkLimitEnabled, filterApp, filterBuilds, filterId, sort, fieldsBetaGroups, limit, include, fieldsBuilds, fieldsBetaTesters, fieldsApps, limitBetaTesters, limitBuilds)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaGroupsApi apiInstance = new BetaGroupsApi(defaultClient);
    List<String> filterIsInternalGroup = Arrays.asList(); // List<String> | filter by attribute 'isInternalGroup'
    List<String> filterName = Arrays.asList(); // List<String> | filter by attribute 'name'
    List<String> filterPublicLink = Arrays.asList(); // List<String> | filter by attribute 'publicLink'
    List<String> filterPublicLinkEnabled = Arrays.asList(); // List<String> | filter by attribute 'publicLinkEnabled'
    List<String> filterPublicLinkLimitEnabled = Arrays.asList(); // List<String> | filter by attribute 'publicLinkLimitEnabled'
    List<String> filterApp = Arrays.asList(); // List<String> | filter by id(s) of related 'app'
    List<String> filterBuilds = Arrays.asList(); // List<String> | filter by id(s) of related 'builds'
    List<String> filterId = Arrays.asList(); // List<String> | filter by id(s)
    List<String> sort = Arrays.asList(); // List<String> | comma-separated list of sort expressions; resources will be sorted as specified
    List<String> fieldsBetaGroups = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaGroups
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    List<String> fieldsBetaTesters = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaTesters
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    Integer limitBetaTesters = 56; // Integer | maximum number of related betaTesters returned (when they are included)
    Integer limitBuilds = 56; // Integer | maximum number of related builds returned (when they are included)
    try {
      BetaGroupsResponse result = apiInstance.betaGroupsGetCollection(filterIsInternalGroup, filterName, filterPublicLink, filterPublicLinkEnabled, filterPublicLinkLimitEnabled, filterApp, filterBuilds, filterId, sort, fieldsBetaGroups, limit, include, fieldsBuilds, fieldsBetaTesters, fieldsApps, limitBetaTesters, limitBuilds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaGroupsApi#betaGroupsGetCollection");
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
| **filterIsInternalGroup** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;isInternalGroup&#39; | [optional] |
| **filterName** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;name&#39; | [optional] |
| **filterPublicLink** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;publicLink&#39; | [optional] |
| **filterPublicLinkEnabled** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;publicLinkEnabled&#39; | [optional] |
| **filterPublicLinkLimitEnabled** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;publicLinkLimitEnabled&#39; | [optional] |
| **filterApp** | [**List&lt;String&gt;**](String.md)| filter by id(s) of related &#39;app&#39; | [optional] |
| **filterBuilds** | [**List&lt;String&gt;**](String.md)| filter by id(s) of related &#39;builds&#39; | [optional] |
| **filterId** | [**List&lt;String&gt;**](String.md)| filter by id(s) | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| comma-separated list of sort expressions; resources will be sorted as specified | [optional] [enum: createdDate, -createdDate, name, -name, publicLinkEnabled, -publicLinkEnabled, publicLinkLimit, -publicLinkLimit] |
| **fieldsBetaGroups** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaGroups | [optional] [enum: app, betaTesters, builds, createdDate, feedbackEnabled, isInternalGroup, name, publicLink, publicLinkEnabled, publicLinkId, publicLinkLimit, publicLinkLimitEnabled] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: app, betaTesters, builds] |
| **fieldsBuilds** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type builds | [optional] [enum: app, appEncryptionDeclaration, appStoreVersion, betaAppReviewSubmission, betaBuildLocalizations, betaGroups, buildBetaDetail, diagnosticSignatures, expirationDate, expired, iconAssetToken, icons, individualTesters, minOsVersion, perfPowerMetrics, preReleaseVersion, processingState, uploadedDate, usesNonExemptEncryption, version] |
| **fieldsBetaTesters** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaTesters | [optional] [enum: apps, betaGroups, builds, email, firstName, inviteType, lastName] |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |
| **limitBetaTesters** | **Integer**| maximum number of related betaTesters returned (when they are included) | [optional] |
| **limitBuilds** | **Integer**| maximum number of related builds returned (when they are included) | [optional] |

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
| **200** | List of BetaGroups |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |

<a id="betaGroupsGetInstance"></a>
# **betaGroupsGetInstance**
> BetaGroupResponse betaGroupsGetInstance(id, fieldsBetaGroups, include, fieldsBuilds, fieldsBetaTesters, fieldsApps, limitBetaTesters, limitBuilds)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaGroupsApi apiInstance = new BetaGroupsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBetaGroups = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaGroups
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    List<String> fieldsBetaTesters = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaTesters
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    Integer limitBetaTesters = 56; // Integer | maximum number of related betaTesters returned (when they are included)
    Integer limitBuilds = 56; // Integer | maximum number of related builds returned (when they are included)
    try {
      BetaGroupResponse result = apiInstance.betaGroupsGetInstance(id, fieldsBetaGroups, include, fieldsBuilds, fieldsBetaTesters, fieldsApps, limitBetaTesters, limitBuilds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaGroupsApi#betaGroupsGetInstance");
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
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: app, betaTesters, builds] |
| **fieldsBuilds** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type builds | [optional] [enum: app, appEncryptionDeclaration, appStoreVersion, betaAppReviewSubmission, betaBuildLocalizations, betaGroups, buildBetaDetail, diagnosticSignatures, expirationDate, expired, iconAssetToken, icons, individualTesters, minOsVersion, perfPowerMetrics, preReleaseVersion, processingState, uploadedDate, usesNonExemptEncryption, version] |
| **fieldsBetaTesters** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaTesters | [optional] [enum: apps, betaGroups, builds, email, firstName, inviteType, lastName] |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |
| **limitBetaTesters** | **Integer**| maximum number of related betaTesters returned (when they are included) | [optional] |
| **limitBuilds** | **Integer**| maximum number of related builds returned (when they are included) | [optional] |

### Return type

[**BetaGroupResponse**](BetaGroupResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single BetaGroup |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="betaGroupsUpdateInstance"></a>
# **betaGroupsUpdateInstance**
> BetaGroupResponse betaGroupsUpdateInstance(id, betaGroupUpdateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaGroupsApi apiInstance = new BetaGroupsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    BetaGroupUpdateRequest betaGroupUpdateRequest = new BetaGroupUpdateRequest(); // BetaGroupUpdateRequest | BetaGroup representation
    try {
      BetaGroupResponse result = apiInstance.betaGroupsUpdateInstance(id, betaGroupUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaGroupsApi#betaGroupsUpdateInstance");
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
| **betaGroupUpdateRequest** | [**BetaGroupUpdateRequest**](BetaGroupUpdateRequest.md)| BetaGroup representation | |

### Return type

[**BetaGroupResponse**](BetaGroupResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single BetaGroup |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

