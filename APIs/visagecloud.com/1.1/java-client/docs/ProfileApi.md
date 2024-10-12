# ProfileApi

All URIs are relative to *https://visagecloud.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addProfileUsingPOST**](ProfileApi.md#addProfileUsingPOST) | **POST** /rest/v1.1/profile/profile | Creates a new profile with no faces associated to it (empty profile) |
| [**deleteProfile2UsingDELETE**](ProfileApi.md#deleteProfile2UsingDELETE) | **DELETE** /rest/v1.1/profile/profile | Deletes a profile and unmaps all its faces |
| [**deleteProfileUsingDELETE**](ProfileApi.md#deleteProfileUsingDELETE) | **DELETE** /rest/v1.1/profile/{id} | Deletes a profile and unmaps all its faces |
| [**getClassificationAttributesFromProfileUsingGET**](ProfileApi.md#getClassificationAttributesFromProfileUsingGET) | **GET** /rest/v1.1/profile/classificationAttributes | Gets classification attributes from a profile |
| [**getFacesFromProfileUsingGET**](ProfileApi.md#getFacesFromProfileUsingGET) | **GET** /rest/v1.1/profile/map | Gets all the faceHashes associated to a profile |
| [**getProfileEnrollmentStatusUsingGET**](ProfileApi.md#getProfileEnrollmentStatusUsingGET) | **GET** /rest/v1.1/profile/enrollmentStatus | Gets the enrollment status of a profile: information on whether it is suitable for authentication. |
| [**getProfileUsingGET**](ProfileApi.md#getProfileUsingGET) | **GET** /rest/v1.1/profile/{id} | Retrieves a profile |
| [**mapClassificationAttributesToProfileUsingPUT**](ProfileApi.md#mapClassificationAttributesToProfileUsingPUT) | **PUT** /rest/v1.1/profile/classificationAttributes | Maps classification attributes to a profile |
| [**mapFacesToProfileUsingPOST**](ProfileApi.md#mapFacesToProfileUsingPOST) | **POST** /rest/v1.1/profile/map | Adds (maps) a list of faces, identified by faceHashes, to a profile, identified by profileId |
| [**removeClassificationAttributesFromProfileUsingDELETE**](ProfileApi.md#removeClassificationAttributesFromProfileUsingDELETE) | **DELETE** /rest/v1.1/profile/classificationAttributes | Removes classification attributes from a profile |
| [**removeFacesFromProfileUsingDELETE**](ProfileApi.md#removeFacesFromProfileUsingDELETE) | **DELETE** /rest/v1.1/profile/map | Removes (unmaps) a list of faces, identified by faceHashes, from a profile, identified by profileId |
| [**updateProfileUsingPATCH**](ProfileApi.md#updateProfileUsingPATCH) | **PATCH** /rest/v1.1/profile/{id} | Update an existing profile with a given id |


<a id="addProfileUsingPOST"></a>
# **addProfileUsingPOST**
> RestResponse addProfileUsingPOST(accessKey, secretKey, collectionId, externalId, screenName, labels, classificationAttributes, details)

Creates a new profile with no faces associated to it (empty profile)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
    String collectionId = "collectionId_example"; // String | Uniquely identified collection that can store multiple profiles
    String externalId = "externalId_example"; // String | External reference to additional information you don’t want to share with VisageCloud
    String screenName = "screenName_example"; // String | Human-readable label for the profile
    List<String> labels = Arrays.asList(); // List<String> | Allows you to do finer filtering in face recognition
    String classificationAttributes = "classificationAttributes_example"; // String | Comma separated key:value classification attributes
    String details = "details_example"; // String | Comma separated key:value details of profile
    try {
      RestResponse result = apiInstance.addProfileUsingPOST(accessKey, secretKey, collectionId, externalId, screenName, labels, classificationAttributes, details);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#addProfileUsingPOST");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey provided by VisageCloud | |
| **collectionId** | **String**| Uniquely identified collection that can store multiple profiles | |
| **externalId** | **String**| External reference to additional information you don’t want to share with VisageCloud | [optional] |
| **screenName** | **String**| Human-readable label for the profile | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| Allows you to do finer filtering in face recognition | [optional] |
| **classificationAttributes** | **String**| Comma separated key:value classification attributes | [optional] |
| **details** | **String**| Comma separated key:value details of profile | [optional] |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="deleteProfile2UsingDELETE"></a>
# **deleteProfile2UsingDELETE**
> RestResponse deleteProfile2UsingDELETE(accessKey, secretKey, collectionId, profileId)

Deletes a profile and unmaps all its faces

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
    String collectionId = "collectionId_example"; // String | Uniquely identified collection that can store multiple profiles
    String profileId = "profileId_example"; // String | The profile id (provide this if you don't have the externalId
    try {
      RestResponse result = apiInstance.deleteProfile2UsingDELETE(accessKey, secretKey, collectionId, profileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#deleteProfile2UsingDELETE");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey provided by VisageCloud | |
| **collectionId** | **String**| Uniquely identified collection that can store multiple profiles | |
| **profileId** | **String**| The profile id (provide this if you don&#39;t have the externalId | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="deleteProfileUsingDELETE"></a>
# **deleteProfileUsingDELETE**
> RestResponse deleteProfileUsingDELETE(accessKey, secretKey, collectionId, id)

Deletes a profile and unmaps all its faces

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
    String collectionId = "collectionId_example"; // String | Uniquely identified collection that can store multiple profiles
    String id = "id_example"; // String | The profile id (provide this if you don't have the externalId
    try {
      RestResponse result = apiInstance.deleteProfileUsingDELETE(accessKey, secretKey, collectionId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#deleteProfileUsingDELETE");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey provided by VisageCloud | |
| **collectionId** | **String**| Uniquely identified collection that can store multiple profiles | |
| **id** | **String**| The profile id (provide this if you don&#39;t have the externalId | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getClassificationAttributesFromProfileUsingGET"></a>
# **getClassificationAttributesFromProfileUsingGET**
> RestResponse getClassificationAttributesFromProfileUsingGET(accessKey, secretKey, profileId, collectionId)

Gets classification attributes from a profile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    String profileId = "profileId_example"; // String | The profile associated with the classification attributes
    String collectionId = "collectionId_example"; // String | The collection that contains the profile
    try {
      RestResponse result = apiInstance.getClassificationAttributesFromProfileUsingGET(accessKey, secretKey, profileId, collectionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#getClassificationAttributesFromProfileUsingGET");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |
| **profileId** | **String**| The profile associated with the classification attributes | |
| **collectionId** | **String**| The collection that contains the profile | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getFacesFromProfileUsingGET"></a>
# **getFacesFromProfileUsingGET**
> RestResponse getFacesFromProfileUsingGET(accessKey, secretKey, profileId, collectionId)

Gets all the faceHashes associated to a profile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    String profileId = "profileId_example"; // String | The profile that contains the faces
    String collectionId = "collectionId_example"; // String | The collection that contains the profile
    try {
      RestResponse result = apiInstance.getFacesFromProfileUsingGET(accessKey, secretKey, profileId, collectionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#getFacesFromProfileUsingGET");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |
| **profileId** | **String**| The profile that contains the faces | |
| **collectionId** | **String**| The collection that contains the profile | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getProfileEnrollmentStatusUsingGET"></a>
# **getProfileEnrollmentStatusUsingGET**
> RestResponse getProfileEnrollmentStatusUsingGET(accessKey, secretKey, profileId, collectionId)

Gets the enrollment status of a profile: information on whether it is suitable for authentication.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    String profileId = "profileId_example"; // String | The profile that contains the faces
    String collectionId = "collectionId_example"; // String | The collection that contains the profile
    try {
      RestResponse result = apiInstance.getProfileEnrollmentStatusUsingGET(accessKey, secretKey, profileId, collectionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#getProfileEnrollmentStatusUsingGET");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |
| **profileId** | **String**| The profile that contains the faces | |
| **collectionId** | **String**| The collection that contains the profile | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getProfileUsingGET"></a>
# **getProfileUsingGET**
> RestResponse getProfileUsingGET(accessKey, secretKey, collectionId, id, withFaces)

Retrieves a profile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    String collectionId = "collectionId_example"; // String | Uniquely identified collection that can store multiple profiles
    String id = "id_example"; // String | The profile id (provide this if you don't have the externalId
    String withFaces = "false"; // String | Retrieves the profile with all its associated faces
    try {
      RestResponse result = apiInstance.getProfileUsingGET(accessKey, secretKey, collectionId, id, withFaces);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#getProfileUsingGET");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |
| **collectionId** | **String**| Uniquely identified collection that can store multiple profiles | |
| **id** | **String**| The profile id (provide this if you don&#39;t have the externalId | |
| **withFaces** | **String**| Retrieves the profile with all its associated faces | [optional] [default to false] |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="mapClassificationAttributesToProfileUsingPUT"></a>
# **mapClassificationAttributesToProfileUsingPUT**
> RestResponse mapClassificationAttributesToProfileUsingPUT(accessKey, secretKey, profileId, collectionId, classificationAttributes)

Maps classification attributes to a profile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
    String profileId = "profileId_example"; // String | The profile associated with the classification attributes
    String collectionId = "collectionId_example"; // String | The collection that contains the profile
    String classificationAttributes = "classificationAttributes_example"; // String | Comma separated key:value classification attributes
    try {
      RestResponse result = apiInstance.mapClassificationAttributesToProfileUsingPUT(accessKey, secretKey, profileId, collectionId, classificationAttributes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#mapClassificationAttributesToProfileUsingPUT");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey provided by VisageCloud | |
| **profileId** | **String**| The profile associated with the classification attributes | |
| **collectionId** | **String**| The collection that contains the profile | |
| **classificationAttributes** | **String**| Comma separated key:value classification attributes | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="mapFacesToProfileUsingPOST"></a>
# **mapFacesToProfileUsingPOST**
> RestResponse mapFacesToProfileUsingPOST(accessKey, secretKey, faceHashes, profileId, collectionId)

Adds (maps) a list of faces, identified by faceHashes, to a profile, identified by profileId

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
    String faceHashes = "faceHashes_example"; // String | Comma separated face hashes, that will be associated to a profile
    String profileId = "profileId_example"; // String | The profile that will store the face
    String collectionId = "collectionId_example"; // String | The collection that contains the profile
    try {
      RestResponse result = apiInstance.mapFacesToProfileUsingPOST(accessKey, secretKey, faceHashes, profileId, collectionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#mapFacesToProfileUsingPOST");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey provided by VisageCloud | |
| **faceHashes** | **String**| Comma separated face hashes, that will be associated to a profile | |
| **profileId** | **String**| The profile that will store the face | |
| **collectionId** | **String**| The collection that contains the profile | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="removeClassificationAttributesFromProfileUsingDELETE"></a>
# **removeClassificationAttributesFromProfileUsingDELETE**
> RestResponse removeClassificationAttributesFromProfileUsingDELETE(accessKey, secretKey, profileId, collectionId)

Removes classification attributes from a profile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
    String profileId = "profileId_example"; // String | The profile associated with the classification attributes
    String collectionId = "collectionId_example"; // String | The collection that contains the profile
    try {
      RestResponse result = apiInstance.removeClassificationAttributesFromProfileUsingDELETE(accessKey, secretKey, profileId, collectionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#removeClassificationAttributesFromProfileUsingDELETE");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey provided by VisageCloud | |
| **profileId** | **String**| The profile associated with the classification attributes | |
| **collectionId** | **String**| The collection that contains the profile | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="removeFacesFromProfileUsingDELETE"></a>
# **removeFacesFromProfileUsingDELETE**
> RestResponse removeFacesFromProfileUsingDELETE(accessKey, secretKey, faceHashes, profileId, collectionId)

Removes (unmaps) a list of faces, identified by faceHashes, from a profile, identified by profileId

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
    String faceHashes = "faceHashes_example"; // String | Comma separated face hashes, that will be removed from a profile
    String profileId = "profileId_example"; // String | The profile that contains the face
    String collectionId = "collectionId_example"; // String | The collection that contains the profile
    try {
      RestResponse result = apiInstance.removeFacesFromProfileUsingDELETE(accessKey, secretKey, faceHashes, profileId, collectionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#removeFacesFromProfileUsingDELETE");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey provided by VisageCloud | |
| **faceHashes** | **String**| Comma separated face hashes, that will be removed from a profile | |
| **profileId** | **String**| The profile that contains the face | |
| **collectionId** | **String**| The collection that contains the profile | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="updateProfileUsingPATCH"></a>
# **updateProfileUsingPATCH**
> RestResponse updateProfileUsingPATCH(accessKey, secretKey, id, collectionId, externalId, screenName, labels, classificationAttributes, details)

Update an existing profile with a given id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    String id = "id_example"; // String | The id of the profile that will be updated
    String collectionId = "collectionId_example"; // String | Uniquely identified collection that can store multiple profiles
    String externalId = "externalId_example"; // String | External reference to additional information you don’t want to share with VisageCloud
    String screenName = "screenName_example"; // String | Human-readable label for the profile
    List<String> labels = Arrays.asList(); // List<String> | Allows you to do finer filtering in face recognition
    String classificationAttributes = "classificationAttributes_example"; // String | Comma separated key:value classification attributes
    String details = "details_example"; // String | Comma separated key:value details of profile
    try {
      RestResponse result = apiInstance.updateProfileUsingPATCH(accessKey, secretKey, id, collectionId, externalId, screenName, labels, classificationAttributes, details);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#updateProfileUsingPATCH");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |
| **id** | **String**| The id of the profile that will be updated | |
| **collectionId** | **String**| Uniquely identified collection that can store multiple profiles | |
| **externalId** | **String**| External reference to additional information you don’t want to share with VisageCloud | [optional] |
| **screenName** | **String**| Human-readable label for the profile | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| Allows you to do finer filtering in face recognition | [optional] |
| **classificationAttributes** | **String**| Comma separated key:value classification attributes | [optional] |
| **details** | **String**| Comma separated key:value details of profile | [optional] |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

