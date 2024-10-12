# GameCenterEnabledVersionsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gameCenterEnabledVersionsCompatibleVersionsCreateToManyRelationship**](GameCenterEnabledVersionsApi.md#gameCenterEnabledVersionsCompatibleVersionsCreateToManyRelationship) | **POST** /v1/gameCenterEnabledVersions/{id}/relationships/compatibleVersions |  |
| [**gameCenterEnabledVersionsCompatibleVersionsDeleteToManyRelationship**](GameCenterEnabledVersionsApi.md#gameCenterEnabledVersionsCompatibleVersionsDeleteToManyRelationship) | **DELETE** /v1/gameCenterEnabledVersions/{id}/relationships/compatibleVersions |  |
| [**gameCenterEnabledVersionsCompatibleVersionsGetToManyRelated**](GameCenterEnabledVersionsApi.md#gameCenterEnabledVersionsCompatibleVersionsGetToManyRelated) | **GET** /v1/gameCenterEnabledVersions/{id}/compatibleVersions |  |
| [**gameCenterEnabledVersionsCompatibleVersionsGetToManyRelationship**](GameCenterEnabledVersionsApi.md#gameCenterEnabledVersionsCompatibleVersionsGetToManyRelationship) | **GET** /v1/gameCenterEnabledVersions/{id}/relationships/compatibleVersions |  |
| [**gameCenterEnabledVersionsCompatibleVersionsReplaceToManyRelationship**](GameCenterEnabledVersionsApi.md#gameCenterEnabledVersionsCompatibleVersionsReplaceToManyRelationship) | **PATCH** /v1/gameCenterEnabledVersions/{id}/relationships/compatibleVersions |  |


<a id="gameCenterEnabledVersionsCompatibleVersionsCreateToManyRelationship"></a>
# **gameCenterEnabledVersionsCompatibleVersionsCreateToManyRelationship**
> gameCenterEnabledVersionsCompatibleVersionsCreateToManyRelationship(id, gameCenterEnabledVersionCompatibleVersionsLinkagesRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GameCenterEnabledVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    GameCenterEnabledVersionsApi apiInstance = new GameCenterEnabledVersionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    GameCenterEnabledVersionCompatibleVersionsLinkagesRequest gameCenterEnabledVersionCompatibleVersionsLinkagesRequest = new GameCenterEnabledVersionCompatibleVersionsLinkagesRequest(); // GameCenterEnabledVersionCompatibleVersionsLinkagesRequest | List of related linkages
    try {
      apiInstance.gameCenterEnabledVersionsCompatibleVersionsCreateToManyRelationship(id, gameCenterEnabledVersionCompatibleVersionsLinkagesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling GameCenterEnabledVersionsApi#gameCenterEnabledVersionsCompatibleVersionsCreateToManyRelationship");
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
| **gameCenterEnabledVersionCompatibleVersionsLinkagesRequest** | [**GameCenterEnabledVersionCompatibleVersionsLinkagesRequest**](GameCenterEnabledVersionCompatibleVersionsLinkagesRequest.md)| List of related linkages | |

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

<a id="gameCenterEnabledVersionsCompatibleVersionsDeleteToManyRelationship"></a>
# **gameCenterEnabledVersionsCompatibleVersionsDeleteToManyRelationship**
> gameCenterEnabledVersionsCompatibleVersionsDeleteToManyRelationship(id, gameCenterEnabledVersionCompatibleVersionsLinkagesRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GameCenterEnabledVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    GameCenterEnabledVersionsApi apiInstance = new GameCenterEnabledVersionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    GameCenterEnabledVersionCompatibleVersionsLinkagesRequest gameCenterEnabledVersionCompatibleVersionsLinkagesRequest = new GameCenterEnabledVersionCompatibleVersionsLinkagesRequest(); // GameCenterEnabledVersionCompatibleVersionsLinkagesRequest | List of related linkages
    try {
      apiInstance.gameCenterEnabledVersionsCompatibleVersionsDeleteToManyRelationship(id, gameCenterEnabledVersionCompatibleVersionsLinkagesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling GameCenterEnabledVersionsApi#gameCenterEnabledVersionsCompatibleVersionsDeleteToManyRelationship");
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
| **gameCenterEnabledVersionCompatibleVersionsLinkagesRequest** | [**GameCenterEnabledVersionCompatibleVersionsLinkagesRequest**](GameCenterEnabledVersionCompatibleVersionsLinkagesRequest.md)| List of related linkages | |

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

<a id="gameCenterEnabledVersionsCompatibleVersionsGetToManyRelated"></a>
# **gameCenterEnabledVersionsCompatibleVersionsGetToManyRelated**
> GameCenterEnabledVersionsResponse gameCenterEnabledVersionsCompatibleVersionsGetToManyRelated(id, filterPlatform, filterVersionString, filterApp, filterId, sort, fieldsGameCenterEnabledVersions, fieldsApps, limit, include)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GameCenterEnabledVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    GameCenterEnabledVersionsApi apiInstance = new GameCenterEnabledVersionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> filterPlatform = Arrays.asList(); // List<String> | filter by attribute 'platform'
    List<String> filterVersionString = Arrays.asList(); // List<String> | filter by attribute 'versionString'
    List<String> filterApp = Arrays.asList(); // List<String> | filter by id(s) of related 'app'
    List<String> filterId = Arrays.asList(); // List<String> | filter by id(s)
    List<String> sort = Arrays.asList(); // List<String> | comma-separated list of sort expressions; resources will be sorted as specified
    List<String> fieldsGameCenterEnabledVersions = Arrays.asList(); // List<String> | the fields to include for returned resources of type gameCenterEnabledVersions
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    try {
      GameCenterEnabledVersionsResponse result = apiInstance.gameCenterEnabledVersionsCompatibleVersionsGetToManyRelated(id, filterPlatform, filterVersionString, filterApp, filterId, sort, fieldsGameCenterEnabledVersions, fieldsApps, limit, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GameCenterEnabledVersionsApi#gameCenterEnabledVersionsCompatibleVersionsGetToManyRelated");
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
| **filterPlatform** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;platform&#39; | [optional] [enum: IOS, MAC_OS, TV_OS] |
| **filterVersionString** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;versionString&#39; | [optional] |
| **filterApp** | [**List&lt;String&gt;**](String.md)| filter by id(s) of related &#39;app&#39; | [optional] |
| **filterId** | [**List&lt;String&gt;**](String.md)| filter by id(s) | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| comma-separated list of sort expressions; resources will be sorted as specified | [optional] [enum: versionString, -versionString] |
| **fieldsGameCenterEnabledVersions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type gameCenterEnabledVersions | [optional] [enum: app, compatibleVersions, iconAsset, platform, versionString] |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: app, compatibleVersions] |

### Return type

[**GameCenterEnabledVersionsResponse**](GameCenterEnabledVersionsResponse.md)

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

<a id="gameCenterEnabledVersionsCompatibleVersionsGetToManyRelationship"></a>
# **gameCenterEnabledVersionsCompatibleVersionsGetToManyRelationship**
> GameCenterEnabledVersionCompatibleVersionsLinkagesResponse gameCenterEnabledVersionsCompatibleVersionsGetToManyRelationship(id, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GameCenterEnabledVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    GameCenterEnabledVersionsApi apiInstance = new GameCenterEnabledVersionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    Integer limit = 56; // Integer | maximum resources per page
    try {
      GameCenterEnabledVersionCompatibleVersionsLinkagesResponse result = apiInstance.gameCenterEnabledVersionsCompatibleVersionsGetToManyRelationship(id, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GameCenterEnabledVersionsApi#gameCenterEnabledVersionsCompatibleVersionsGetToManyRelationship");
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

[**GameCenterEnabledVersionCompatibleVersionsLinkagesResponse**](GameCenterEnabledVersionCompatibleVersionsLinkagesResponse.md)

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

<a id="gameCenterEnabledVersionsCompatibleVersionsReplaceToManyRelationship"></a>
# **gameCenterEnabledVersionsCompatibleVersionsReplaceToManyRelationship**
> gameCenterEnabledVersionsCompatibleVersionsReplaceToManyRelationship(id, gameCenterEnabledVersionCompatibleVersionsLinkagesRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GameCenterEnabledVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    GameCenterEnabledVersionsApi apiInstance = new GameCenterEnabledVersionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    GameCenterEnabledVersionCompatibleVersionsLinkagesRequest gameCenterEnabledVersionCompatibleVersionsLinkagesRequest = new GameCenterEnabledVersionCompatibleVersionsLinkagesRequest(); // GameCenterEnabledVersionCompatibleVersionsLinkagesRequest | List of related linkages
    try {
      apiInstance.gameCenterEnabledVersionsCompatibleVersionsReplaceToManyRelationship(id, gameCenterEnabledVersionCompatibleVersionsLinkagesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling GameCenterEnabledVersionsApi#gameCenterEnabledVersionsCompatibleVersionsReplaceToManyRelationship");
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
| **gameCenterEnabledVersionCompatibleVersionsLinkagesRequest** | [**GameCenterEnabledVersionCompatibleVersionsLinkagesRequest**](GameCenterEnabledVersionCompatibleVersionsLinkagesRequest.md)| List of related linkages | |

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

