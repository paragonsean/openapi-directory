# UserInvitationsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**userInvitationsCreateInstance**](UserInvitationsApi.md#userInvitationsCreateInstance) | **POST** /v1/userInvitations |  |
| [**userInvitationsDeleteInstance**](UserInvitationsApi.md#userInvitationsDeleteInstance) | **DELETE** /v1/userInvitations/{id} |  |
| [**userInvitationsGetCollection**](UserInvitationsApi.md#userInvitationsGetCollection) | **GET** /v1/userInvitations |  |
| [**userInvitationsGetInstance**](UserInvitationsApi.md#userInvitationsGetInstance) | **GET** /v1/userInvitations/{id} |  |
| [**userInvitationsVisibleAppsGetToManyRelated**](UserInvitationsApi.md#userInvitationsVisibleAppsGetToManyRelated) | **GET** /v1/userInvitations/{id}/visibleApps |  |


<a id="userInvitationsCreateInstance"></a>
# **userInvitationsCreateInstance**
> UserInvitationResponse userInvitationsCreateInstance(userInvitationCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserInvitationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    UserInvitationsApi apiInstance = new UserInvitationsApi(defaultClient);
    UserInvitationCreateRequest userInvitationCreateRequest = new UserInvitationCreateRequest(); // UserInvitationCreateRequest | UserInvitation representation
    try {
      UserInvitationResponse result = apiInstance.userInvitationsCreateInstance(userInvitationCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserInvitationsApi#userInvitationsCreateInstance");
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
| **userInvitationCreateRequest** | [**UserInvitationCreateRequest**](UserInvitationCreateRequest.md)| UserInvitation representation | |

### Return type

[**UserInvitationResponse**](UserInvitationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single UserInvitation |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="userInvitationsDeleteInstance"></a>
# **userInvitationsDeleteInstance**
> userInvitationsDeleteInstance(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserInvitationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    UserInvitationsApi apiInstance = new UserInvitationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    try {
      apiInstance.userInvitationsDeleteInstance(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserInvitationsApi#userInvitationsDeleteInstance");
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

<a id="userInvitationsGetCollection"></a>
# **userInvitationsGetCollection**
> UserInvitationsResponse userInvitationsGetCollection(filterEmail, filterRoles, filterVisibleApps, sort, fieldsUserInvitations, limit, include, fieldsApps, limitVisibleApps)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserInvitationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    UserInvitationsApi apiInstance = new UserInvitationsApi(defaultClient);
    List<String> filterEmail = Arrays.asList(); // List<String> | filter by attribute 'email'
    List<String> filterRoles = Arrays.asList(); // List<String> | filter by attribute 'roles'
    List<String> filterVisibleApps = Arrays.asList(); // List<String> | filter by id(s) of related 'visibleApps'
    List<String> sort = Arrays.asList(); // List<String> | comma-separated list of sort expressions; resources will be sorted as specified
    List<String> fieldsUserInvitations = Arrays.asList(); // List<String> | the fields to include for returned resources of type userInvitations
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    Integer limitVisibleApps = 56; // Integer | maximum number of related visibleApps returned (when they are included)
    try {
      UserInvitationsResponse result = apiInstance.userInvitationsGetCollection(filterEmail, filterRoles, filterVisibleApps, sort, fieldsUserInvitations, limit, include, fieldsApps, limitVisibleApps);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserInvitationsApi#userInvitationsGetCollection");
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
| **filterRoles** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;roles&#39; | [optional] [enum: ADMIN, FINANCE, TECHNICAL, ACCOUNT_HOLDER, READ_ONLY, SALES, MARKETING, APP_MANAGER, DEVELOPER, ACCESS_TO_REPORTS, CUSTOMER_SUPPORT, CREATE_APPS, CLOUD_MANAGED_DEVELOPER_ID, CLOUD_MANAGED_APP_DISTRIBUTION] |
| **filterVisibleApps** | [**List&lt;String&gt;**](String.md)| filter by id(s) of related &#39;visibleApps&#39; | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| comma-separated list of sort expressions; resources will be sorted as specified | [optional] [enum: email, -email, lastName, -lastName] |
| **fieldsUserInvitations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type userInvitations | [optional] [enum: allAppsVisible, email, expirationDate, firstName, lastName, provisioningAllowed, roles, visibleApps] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: visibleApps] |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |
| **limitVisibleApps** | **Integer**| maximum number of related visibleApps returned (when they are included) | [optional] |

### Return type

[**UserInvitationsResponse**](UserInvitationsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of UserInvitations |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |

<a id="userInvitationsGetInstance"></a>
# **userInvitationsGetInstance**
> UserInvitationResponse userInvitationsGetInstance(id, fieldsUserInvitations, include, fieldsApps, limitVisibleApps)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserInvitationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    UserInvitationsApi apiInstance = new UserInvitationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsUserInvitations = Arrays.asList(); // List<String> | the fields to include for returned resources of type userInvitations
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    Integer limitVisibleApps = 56; // Integer | maximum number of related visibleApps returned (when they are included)
    try {
      UserInvitationResponse result = apiInstance.userInvitationsGetInstance(id, fieldsUserInvitations, include, fieldsApps, limitVisibleApps);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserInvitationsApi#userInvitationsGetInstance");
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
| **fieldsUserInvitations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type userInvitations | [optional] [enum: allAppsVisible, email, expirationDate, firstName, lastName, provisioningAllowed, roles, visibleApps] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: visibleApps] |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |
| **limitVisibleApps** | **Integer**| maximum number of related visibleApps returned (when they are included) | [optional] |

### Return type

[**UserInvitationResponse**](UserInvitationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single UserInvitation |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="userInvitationsVisibleAppsGetToManyRelated"></a>
# **userInvitationsVisibleAppsGetToManyRelated**
> AppsResponse userInvitationsVisibleAppsGetToManyRelated(id, fieldsApps, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserInvitationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    UserInvitationsApi apiInstance = new UserInvitationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    Integer limit = 56; // Integer | maximum resources per page
    try {
      AppsResponse result = apiInstance.userInvitationsVisibleAppsGetToManyRelated(id, fieldsApps, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserInvitationsApi#userInvitationsVisibleAppsGetToManyRelated");
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

