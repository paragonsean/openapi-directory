# AppInfosApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appInfosAgeRatingDeclarationGetToOneRelated**](AppInfosApi.md#appInfosAgeRatingDeclarationGetToOneRelated) | **GET** /v1/appInfos/{id}/ageRatingDeclaration |  |
| [**appInfosAppInfoLocalizationsGetToManyRelated**](AppInfosApi.md#appInfosAppInfoLocalizationsGetToManyRelated) | **GET** /v1/appInfos/{id}/appInfoLocalizations |  |
| [**appInfosGetInstance**](AppInfosApi.md#appInfosGetInstance) | **GET** /v1/appInfos/{id} |  |
| [**appInfosPrimaryCategoryGetToOneRelated**](AppInfosApi.md#appInfosPrimaryCategoryGetToOneRelated) | **GET** /v1/appInfos/{id}/primaryCategory |  |
| [**appInfosPrimarySubcategoryOneGetToOneRelated**](AppInfosApi.md#appInfosPrimarySubcategoryOneGetToOneRelated) | **GET** /v1/appInfos/{id}/primarySubcategoryOne |  |
| [**appInfosPrimarySubcategoryTwoGetToOneRelated**](AppInfosApi.md#appInfosPrimarySubcategoryTwoGetToOneRelated) | **GET** /v1/appInfos/{id}/primarySubcategoryTwo |  |
| [**appInfosSecondaryCategoryGetToOneRelated**](AppInfosApi.md#appInfosSecondaryCategoryGetToOneRelated) | **GET** /v1/appInfos/{id}/secondaryCategory |  |
| [**appInfosSecondarySubcategoryOneGetToOneRelated**](AppInfosApi.md#appInfosSecondarySubcategoryOneGetToOneRelated) | **GET** /v1/appInfos/{id}/secondarySubcategoryOne |  |
| [**appInfosSecondarySubcategoryTwoGetToOneRelated**](AppInfosApi.md#appInfosSecondarySubcategoryTwoGetToOneRelated) | **GET** /v1/appInfos/{id}/secondarySubcategoryTwo |  |
| [**appInfosUpdateInstance**](AppInfosApi.md#appInfosUpdateInstance) | **PATCH** /v1/appInfos/{id} |  |


<a id="appInfosAgeRatingDeclarationGetToOneRelated"></a>
# **appInfosAgeRatingDeclarationGetToOneRelated**
> AgeRatingDeclarationResponse appInfosAgeRatingDeclarationGetToOneRelated(id, fieldsAgeRatingDeclarations)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppInfosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppInfosApi apiInstance = new AppInfosApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAgeRatingDeclarations = Arrays.asList(); // List<String> | the fields to include for returned resources of type ageRatingDeclarations
    try {
      AgeRatingDeclarationResponse result = apiInstance.appInfosAgeRatingDeclarationGetToOneRelated(id, fieldsAgeRatingDeclarations);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppInfosApi#appInfosAgeRatingDeclarationGetToOneRelated");
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
| **fieldsAgeRatingDeclarations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type ageRatingDeclarations | [optional] [enum: alcoholTobaccoOrDrugUseOrReferences, contests, gambling, gamblingAndContests, gamblingSimulated, horrorOrFearThemes, kidsAgeBand, matureOrSuggestiveThemes, medicalOrTreatmentInformation, profanityOrCrudeHumor, seventeenPlus, sexualContentGraphicAndNudity, sexualContentOrNudity, unrestrictedWebAccess, violenceCartoonOrFantasy, violenceRealistic, violenceRealisticProlongedGraphicOrSadistic] |

### Return type

[**AgeRatingDeclarationResponse**](AgeRatingDeclarationResponse.md)

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

<a id="appInfosAppInfoLocalizationsGetToManyRelated"></a>
# **appInfosAppInfoLocalizationsGetToManyRelated**
> AppInfoLocalizationsResponse appInfosAppInfoLocalizationsGetToManyRelated(id, filterLocale, fieldsAppInfos, fieldsAppInfoLocalizations, limit, include)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppInfosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppInfosApi apiInstance = new AppInfosApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> filterLocale = Arrays.asList(); // List<String> | filter by attribute 'locale'
    List<String> fieldsAppInfos = Arrays.asList(); // List<String> | the fields to include for returned resources of type appInfos
    List<String> fieldsAppInfoLocalizations = Arrays.asList(); // List<String> | the fields to include for returned resources of type appInfoLocalizations
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    try {
      AppInfoLocalizationsResponse result = apiInstance.appInfosAppInfoLocalizationsGetToManyRelated(id, filterLocale, fieldsAppInfos, fieldsAppInfoLocalizations, limit, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppInfosApi#appInfosAppInfoLocalizationsGetToManyRelated");
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
| **filterLocale** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;locale&#39; | [optional] |
| **fieldsAppInfos** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appInfos | [optional] [enum: ageRatingDeclaration, app, appInfoLocalizations, appStoreAgeRating, appStoreState, brazilAgeRating, kidsAgeBand, primaryCategory, primarySubcategoryOne, primarySubcategoryTwo, secondaryCategory, secondarySubcategoryOne, secondarySubcategoryTwo] |
| **fieldsAppInfoLocalizations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appInfoLocalizations | [optional] [enum: appInfo, locale, name, privacyPolicyText, privacyPolicyUrl, subtitle] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: appInfo] |

### Return type

[**AppInfoLocalizationsResponse**](AppInfoLocalizationsResponse.md)

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

<a id="appInfosGetInstance"></a>
# **appInfosGetInstance**
> AppInfoResponse appInfosGetInstance(id, fieldsAppInfos, include, fieldsAgeRatingDeclarations, fieldsAppCategories, fieldsAppInfoLocalizations, limitAppInfoLocalizations)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppInfosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppInfosApi apiInstance = new AppInfosApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppInfos = Arrays.asList(); // List<String> | the fields to include for returned resources of type appInfos
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsAgeRatingDeclarations = Arrays.asList(); // List<String> | the fields to include for returned resources of type ageRatingDeclarations
    List<String> fieldsAppCategories = Arrays.asList(); // List<String> | the fields to include for returned resources of type appCategories
    List<String> fieldsAppInfoLocalizations = Arrays.asList(); // List<String> | the fields to include for returned resources of type appInfoLocalizations
    Integer limitAppInfoLocalizations = 56; // Integer | maximum number of related appInfoLocalizations returned (when they are included)
    try {
      AppInfoResponse result = apiInstance.appInfosGetInstance(id, fieldsAppInfos, include, fieldsAgeRatingDeclarations, fieldsAppCategories, fieldsAppInfoLocalizations, limitAppInfoLocalizations);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppInfosApi#appInfosGetInstance");
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
| **fieldsAppInfos** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appInfos | [optional] [enum: ageRatingDeclaration, app, appInfoLocalizations, appStoreAgeRating, appStoreState, brazilAgeRating, kidsAgeBand, primaryCategory, primarySubcategoryOne, primarySubcategoryTwo, secondaryCategory, secondarySubcategoryOne, secondarySubcategoryTwo] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: ageRatingDeclaration, app, appInfoLocalizations, primaryCategory, primarySubcategoryOne, primarySubcategoryTwo, secondaryCategory, secondarySubcategoryOne, secondarySubcategoryTwo] |
| **fieldsAgeRatingDeclarations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type ageRatingDeclarations | [optional] [enum: alcoholTobaccoOrDrugUseOrReferences, contests, gambling, gamblingAndContests, gamblingSimulated, horrorOrFearThemes, kidsAgeBand, matureOrSuggestiveThemes, medicalOrTreatmentInformation, profanityOrCrudeHumor, seventeenPlus, sexualContentGraphicAndNudity, sexualContentOrNudity, unrestrictedWebAccess, violenceCartoonOrFantasy, violenceRealistic, violenceRealisticProlongedGraphicOrSadistic] |
| **fieldsAppCategories** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appCategories | [optional] [enum: parent, platforms, subcategories] |
| **fieldsAppInfoLocalizations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appInfoLocalizations | [optional] [enum: appInfo, locale, name, privacyPolicyText, privacyPolicyUrl, subtitle] |
| **limitAppInfoLocalizations** | **Integer**| maximum number of related appInfoLocalizations returned (when they are included) | [optional] |

### Return type

[**AppInfoResponse**](AppInfoResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single AppInfo |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appInfosPrimaryCategoryGetToOneRelated"></a>
# **appInfosPrimaryCategoryGetToOneRelated**
> AppCategoryResponse appInfosPrimaryCategoryGetToOneRelated(id, fieldsAppCategories)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppInfosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppInfosApi apiInstance = new AppInfosApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppCategories = Arrays.asList(); // List<String> | the fields to include for returned resources of type appCategories
    try {
      AppCategoryResponse result = apiInstance.appInfosPrimaryCategoryGetToOneRelated(id, fieldsAppCategories);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppInfosApi#appInfosPrimaryCategoryGetToOneRelated");
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
| **fieldsAppCategories** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appCategories | [optional] [enum: parent, platforms, subcategories] |

### Return type

[**AppCategoryResponse**](AppCategoryResponse.md)

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

<a id="appInfosPrimarySubcategoryOneGetToOneRelated"></a>
# **appInfosPrimarySubcategoryOneGetToOneRelated**
> AppCategoryResponse appInfosPrimarySubcategoryOneGetToOneRelated(id, fieldsAppCategories)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppInfosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppInfosApi apiInstance = new AppInfosApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppCategories = Arrays.asList(); // List<String> | the fields to include for returned resources of type appCategories
    try {
      AppCategoryResponse result = apiInstance.appInfosPrimarySubcategoryOneGetToOneRelated(id, fieldsAppCategories);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppInfosApi#appInfosPrimarySubcategoryOneGetToOneRelated");
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
| **fieldsAppCategories** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appCategories | [optional] [enum: parent, platforms, subcategories] |

### Return type

[**AppCategoryResponse**](AppCategoryResponse.md)

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

<a id="appInfosPrimarySubcategoryTwoGetToOneRelated"></a>
# **appInfosPrimarySubcategoryTwoGetToOneRelated**
> AppCategoryResponse appInfosPrimarySubcategoryTwoGetToOneRelated(id, fieldsAppCategories)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppInfosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppInfosApi apiInstance = new AppInfosApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppCategories = Arrays.asList(); // List<String> | the fields to include for returned resources of type appCategories
    try {
      AppCategoryResponse result = apiInstance.appInfosPrimarySubcategoryTwoGetToOneRelated(id, fieldsAppCategories);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppInfosApi#appInfosPrimarySubcategoryTwoGetToOneRelated");
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
| **fieldsAppCategories** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appCategories | [optional] [enum: parent, platforms, subcategories] |

### Return type

[**AppCategoryResponse**](AppCategoryResponse.md)

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

<a id="appInfosSecondaryCategoryGetToOneRelated"></a>
# **appInfosSecondaryCategoryGetToOneRelated**
> AppCategoryResponse appInfosSecondaryCategoryGetToOneRelated(id, fieldsAppCategories)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppInfosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppInfosApi apiInstance = new AppInfosApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppCategories = Arrays.asList(); // List<String> | the fields to include for returned resources of type appCategories
    try {
      AppCategoryResponse result = apiInstance.appInfosSecondaryCategoryGetToOneRelated(id, fieldsAppCategories);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppInfosApi#appInfosSecondaryCategoryGetToOneRelated");
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
| **fieldsAppCategories** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appCategories | [optional] [enum: parent, platforms, subcategories] |

### Return type

[**AppCategoryResponse**](AppCategoryResponse.md)

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

<a id="appInfosSecondarySubcategoryOneGetToOneRelated"></a>
# **appInfosSecondarySubcategoryOneGetToOneRelated**
> AppCategoryResponse appInfosSecondarySubcategoryOneGetToOneRelated(id, fieldsAppCategories)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppInfosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppInfosApi apiInstance = new AppInfosApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppCategories = Arrays.asList(); // List<String> | the fields to include for returned resources of type appCategories
    try {
      AppCategoryResponse result = apiInstance.appInfosSecondarySubcategoryOneGetToOneRelated(id, fieldsAppCategories);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppInfosApi#appInfosSecondarySubcategoryOneGetToOneRelated");
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
| **fieldsAppCategories** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appCategories | [optional] [enum: parent, platforms, subcategories] |

### Return type

[**AppCategoryResponse**](AppCategoryResponse.md)

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

<a id="appInfosSecondarySubcategoryTwoGetToOneRelated"></a>
# **appInfosSecondarySubcategoryTwoGetToOneRelated**
> AppCategoryResponse appInfosSecondarySubcategoryTwoGetToOneRelated(id, fieldsAppCategories)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppInfosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppInfosApi apiInstance = new AppInfosApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppCategories = Arrays.asList(); // List<String> | the fields to include for returned resources of type appCategories
    try {
      AppCategoryResponse result = apiInstance.appInfosSecondarySubcategoryTwoGetToOneRelated(id, fieldsAppCategories);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppInfosApi#appInfosSecondarySubcategoryTwoGetToOneRelated");
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
| **fieldsAppCategories** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appCategories | [optional] [enum: parent, platforms, subcategories] |

### Return type

[**AppCategoryResponse**](AppCategoryResponse.md)

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

<a id="appInfosUpdateInstance"></a>
# **appInfosUpdateInstance**
> AppInfoResponse appInfosUpdateInstance(id, appInfoUpdateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppInfosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppInfosApi apiInstance = new AppInfosApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    AppInfoUpdateRequest appInfoUpdateRequest = new AppInfoUpdateRequest(); // AppInfoUpdateRequest | AppInfo representation
    try {
      AppInfoResponse result = apiInstance.appInfosUpdateInstance(id, appInfoUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppInfosApi#appInfosUpdateInstance");
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
| **appInfoUpdateRequest** | [**AppInfoUpdateRequest**](AppInfoUpdateRequest.md)| AppInfo representation | |

### Return type

[**AppInfoResponse**](AppInfoResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single AppInfo |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

