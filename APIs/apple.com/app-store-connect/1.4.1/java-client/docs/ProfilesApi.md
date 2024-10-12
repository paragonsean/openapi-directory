# ProfilesApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**profilesBundleIdGetToOneRelated**](ProfilesApi.md#profilesBundleIdGetToOneRelated) | **GET** /v1/profiles/{id}/bundleId |  |
| [**profilesCertificatesGetToManyRelated**](ProfilesApi.md#profilesCertificatesGetToManyRelated) | **GET** /v1/profiles/{id}/certificates |  |
| [**profilesCreateInstance**](ProfilesApi.md#profilesCreateInstance) | **POST** /v1/profiles |  |
| [**profilesDeleteInstance**](ProfilesApi.md#profilesDeleteInstance) | **DELETE** /v1/profiles/{id} |  |
| [**profilesDevicesGetToManyRelated**](ProfilesApi.md#profilesDevicesGetToManyRelated) | **GET** /v1/profiles/{id}/devices |  |
| [**profilesGetCollection**](ProfilesApi.md#profilesGetCollection) | **GET** /v1/profiles |  |
| [**profilesGetInstance**](ProfilesApi.md#profilesGetInstance) | **GET** /v1/profiles/{id} |  |


<a id="profilesBundleIdGetToOneRelated"></a>
# **profilesBundleIdGetToOneRelated**
> BundleIdResponse profilesBundleIdGetToOneRelated(id, fieldsBundleIds)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBundleIds = Arrays.asList(); // List<String> | the fields to include for returned resources of type bundleIds
    try {
      BundleIdResponse result = apiInstance.profilesBundleIdGetToOneRelated(id, fieldsBundleIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesBundleIdGetToOneRelated");
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
| **fieldsBundleIds** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type bundleIds | [optional] [enum: app, bundleIdCapabilities, identifier, name, platform, profiles, seedId] |

### Return type

[**BundleIdResponse**](BundleIdResponse.md)

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

<a id="profilesCertificatesGetToManyRelated"></a>
# **profilesCertificatesGetToManyRelated**
> CertificatesResponse profilesCertificatesGetToManyRelated(id, fieldsCertificates, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsCertificates = Arrays.asList(); // List<String> | the fields to include for returned resources of type certificates
    Integer limit = 56; // Integer | maximum resources per page
    try {
      CertificatesResponse result = apiInstance.profilesCertificatesGetToManyRelated(id, fieldsCertificates, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesCertificatesGetToManyRelated");
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
| **fieldsCertificates** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type certificates | [optional] [enum: certificateContent, certificateType, csrContent, displayName, expirationDate, name, platform, serialNumber] |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**CertificatesResponse**](CertificatesResponse.md)

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

<a id="profilesCreateInstance"></a>
# **profilesCreateInstance**
> ProfileResponse profilesCreateInstance(profileCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    ProfileCreateRequest profileCreateRequest = new ProfileCreateRequest(); // ProfileCreateRequest | Profile representation
    try {
      ProfileResponse result = apiInstance.profilesCreateInstance(profileCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesCreateInstance");
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
| **profileCreateRequest** | [**ProfileCreateRequest**](ProfileCreateRequest.md)| Profile representation | |

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single Profile |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="profilesDeleteInstance"></a>
# **profilesDeleteInstance**
> profilesDeleteInstance(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    try {
      apiInstance.profilesDeleteInstance(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesDeleteInstance");
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

<a id="profilesDevicesGetToManyRelated"></a>
# **profilesDevicesGetToManyRelated**
> DevicesResponse profilesDevicesGetToManyRelated(id, fieldsDevices, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsDevices = Arrays.asList(); // List<String> | the fields to include for returned resources of type devices
    Integer limit = 56; // Integer | maximum resources per page
    try {
      DevicesResponse result = apiInstance.profilesDevicesGetToManyRelated(id, fieldsDevices, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesDevicesGetToManyRelated");
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
| **fieldsDevices** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type devices | [optional] [enum: addedDate, deviceClass, model, name, platform, status, udid] |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**DevicesResponse**](DevicesResponse.md)

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

<a id="profilesGetCollection"></a>
# **profilesGetCollection**
> ProfilesResponse profilesGetCollection(filterName, filterProfileState, filterProfileType, filterId, sort, fieldsProfiles, limit, include, fieldsCertificates, fieldsDevices, fieldsBundleIds, limitCertificates, limitDevices)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    List<String> filterName = Arrays.asList(); // List<String> | filter by attribute 'name'
    List<String> filterProfileState = Arrays.asList(); // List<String> | filter by attribute 'profileState'
    List<String> filterProfileType = Arrays.asList(); // List<String> | filter by attribute 'profileType'
    List<String> filterId = Arrays.asList(); // List<String> | filter by id(s)
    List<String> sort = Arrays.asList(); // List<String> | comma-separated list of sort expressions; resources will be sorted as specified
    List<String> fieldsProfiles = Arrays.asList(); // List<String> | the fields to include for returned resources of type profiles
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsCertificates = Arrays.asList(); // List<String> | the fields to include for returned resources of type certificates
    List<String> fieldsDevices = Arrays.asList(); // List<String> | the fields to include for returned resources of type devices
    List<String> fieldsBundleIds = Arrays.asList(); // List<String> | the fields to include for returned resources of type bundleIds
    Integer limitCertificates = 56; // Integer | maximum number of related certificates returned (when they are included)
    Integer limitDevices = 56; // Integer | maximum number of related devices returned (when they are included)
    try {
      ProfilesResponse result = apiInstance.profilesGetCollection(filterName, filterProfileState, filterProfileType, filterId, sort, fieldsProfiles, limit, include, fieldsCertificates, fieldsDevices, fieldsBundleIds, limitCertificates, limitDevices);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesGetCollection");
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
| **filterName** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;name&#39; | [optional] |
| **filterProfileState** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;profileState&#39; | [optional] [enum: ACTIVE, INVALID] |
| **filterProfileType** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;profileType&#39; | [optional] [enum: IOS_APP_DEVELOPMENT, IOS_APP_STORE, IOS_APP_ADHOC, IOS_APP_INHOUSE, MAC_APP_DEVELOPMENT, MAC_APP_STORE, MAC_APP_DIRECT, TVOS_APP_DEVELOPMENT, TVOS_APP_STORE, TVOS_APP_ADHOC, TVOS_APP_INHOUSE, MAC_CATALYST_APP_DEVELOPMENT, MAC_CATALYST_APP_STORE, MAC_CATALYST_APP_DIRECT] |
| **filterId** | [**List&lt;String&gt;**](String.md)| filter by id(s) | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| comma-separated list of sort expressions; resources will be sorted as specified | [optional] [enum: id, -id, name, -name, profileState, -profileState, profileType, -profileType] |
| **fieldsProfiles** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type profiles | [optional] [enum: bundleId, certificates, createdDate, devices, expirationDate, name, platform, profileContent, profileState, profileType, uuid] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: bundleId, certificates, devices] |
| **fieldsCertificates** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type certificates | [optional] [enum: certificateContent, certificateType, csrContent, displayName, expirationDate, name, platform, serialNumber] |
| **fieldsDevices** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type devices | [optional] [enum: addedDate, deviceClass, model, name, platform, status, udid] |
| **fieldsBundleIds** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type bundleIds | [optional] [enum: app, bundleIdCapabilities, identifier, name, platform, profiles, seedId] |
| **limitCertificates** | **Integer**| maximum number of related certificates returned (when they are included) | [optional] |
| **limitDevices** | **Integer**| maximum number of related devices returned (when they are included) | [optional] |

### Return type

[**ProfilesResponse**](ProfilesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Profiles |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |

<a id="profilesGetInstance"></a>
# **profilesGetInstance**
> ProfileResponse profilesGetInstance(id, fieldsProfiles, include, fieldsCertificates, fieldsDevices, fieldsBundleIds, limitCertificates, limitDevices)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsProfiles = Arrays.asList(); // List<String> | the fields to include for returned resources of type profiles
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsCertificates = Arrays.asList(); // List<String> | the fields to include for returned resources of type certificates
    List<String> fieldsDevices = Arrays.asList(); // List<String> | the fields to include for returned resources of type devices
    List<String> fieldsBundleIds = Arrays.asList(); // List<String> | the fields to include for returned resources of type bundleIds
    Integer limitCertificates = 56; // Integer | maximum number of related certificates returned (when they are included)
    Integer limitDevices = 56; // Integer | maximum number of related devices returned (when they are included)
    try {
      ProfileResponse result = apiInstance.profilesGetInstance(id, fieldsProfiles, include, fieldsCertificates, fieldsDevices, fieldsBundleIds, limitCertificates, limitDevices);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesGetInstance");
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
| **fieldsProfiles** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type profiles | [optional] [enum: bundleId, certificates, createdDate, devices, expirationDate, name, platform, profileContent, profileState, profileType, uuid] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: bundleId, certificates, devices] |
| **fieldsCertificates** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type certificates | [optional] [enum: certificateContent, certificateType, csrContent, displayName, expirationDate, name, platform, serialNumber] |
| **fieldsDevices** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type devices | [optional] [enum: addedDate, deviceClass, model, name, platform, status, udid] |
| **fieldsBundleIds** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type bundleIds | [optional] [enum: app, bundleIdCapabilities, identifier, name, platform, profiles, seedId] |
| **limitCertificates** | **Integer**| maximum number of related certificates returned (when they are included) | [optional] |
| **limitDevices** | **Integer**| maximum number of related devices returned (when they are included) | [optional] |

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single Profile |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

