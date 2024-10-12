# ObjectStorageApi

All URIs are relative to *https://api.linode.com/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelObjectStorage**](ObjectStorageApi.md#cancelObjectStorage) | **POST** /object-storage/cancel | Object Storage Cancel |
| [**createObjectStorageBucket**](ObjectStorageApi.md#createObjectStorageBucket) | **POST** /object-storage/buckets | Object Storage Bucket Create |
| [**createObjectStorageKeys**](ObjectStorageApi.md#createObjectStorageKeys) | **POST** /object-storage/keys | Object Storage Key Create |
| [**createObjectStorageObjectURL**](ObjectStorageApi.md#createObjectStorageObjectURL) | **POST** /object-storage/buckets/{clusterId}/{bucket}/object-url | Object Storage Object URL Create |
| [**createObjectStorageSSL**](ObjectStorageApi.md#createObjectStorageSSL) | **POST** /object-storage/buckets/{clusterId}/{bucket}/ssl | Object Storage TLS/SSL Cert Upload |
| [**deleteObjectStorageBucket**](ObjectStorageApi.md#deleteObjectStorageBucket) | **DELETE** /object-storage/buckets/{clusterId}/{bucket} | Object Storage Bucket Remove |
| [**deleteObjectStorageKey**](ObjectStorageApi.md#deleteObjectStorageKey) | **DELETE** /object-storage/keys/{keyId} | Object Storage Key Revoke |
| [**deleteObjectStorageSSL**](ObjectStorageApi.md#deleteObjectStorageSSL) | **DELETE** /object-storage/buckets/{clusterId}/{bucket}/ssl | Object Storage TLS/SSL Cert Delete |
| [**getObjectStorageBucket**](ObjectStorageApi.md#getObjectStorageBucket) | **GET** /object-storage/buckets/{clusterId}/{bucket} | Object Storage Bucket View |
| [**getObjectStorageBucketContent**](ObjectStorageApi.md#getObjectStorageBucketContent) | **GET** /object-storage/buckets/{clusterId}/{bucket}/object-list | Object Storage Bucket Contents List |
| [**getObjectStorageBucketinCluster**](ObjectStorageApi.md#getObjectStorageBucketinCluster) | **GET** /object-storage/buckets/{clusterId} | Object Storage Buckets in Cluster List |
| [**getObjectStorageBuckets**](ObjectStorageApi.md#getObjectStorageBuckets) | **GET** /object-storage/buckets | Object Storage Buckets List |
| [**getObjectStorageCluster**](ObjectStorageApi.md#getObjectStorageCluster) | **GET** /object-storage/clusters/{clusterId} | Cluster View |
| [**getObjectStorageClusters**](ObjectStorageApi.md#getObjectStorageClusters) | **GET** /object-storage/clusters | Clusters List |
| [**getObjectStorageKey**](ObjectStorageApi.md#getObjectStorageKey) | **GET** /object-storage/keys/{keyId} | Object Storage Key View |
| [**getObjectStorageKeys**](ObjectStorageApi.md#getObjectStorageKeys) | **GET** /object-storage/keys | Object Storage Keys List |
| [**getObjectStorageSSL**](ObjectStorageApi.md#getObjectStorageSSL) | **GET** /object-storage/buckets/{clusterId}/{bucket}/ssl | Object Storage TLS/SSL Cert View |
| [**getObjectStorageTransfer**](ObjectStorageApi.md#getObjectStorageTransfer) | **GET** /object-storage/transfer | Object Storage Transfer View |
| [**modifyObjectStorageBucketAccess**](ObjectStorageApi.md#modifyObjectStorageBucketAccess) | **POST** /object-storage/buckets/{clusterId}/{bucket}/access | Object Storage Bucket Access Modify |
| [**updateObjectStorageBucketACL**](ObjectStorageApi.md#updateObjectStorageBucketACL) | **PUT** /object-storage/buckets/{clusterId}/{bucket}/object-acl | Object Storage Object ACL Config Update |
| [**updateObjectStorageBucketAccess**](ObjectStorageApi.md#updateObjectStorageBucketAccess) | **PUT** /object-storage/buckets/{clusterId}/{bucket}/access | Object Storage Bucket Access Update |
| [**updateObjectStorageKey**](ObjectStorageApi.md#updateObjectStorageKey) | **PUT** /object-storage/keys/{keyId} | Object Storage Key Update |
| [**viewObjectStorageBucketACL**](ObjectStorageApi.md#viewObjectStorageBucketACL) | **GET** /object-storage/buckets/{clusterId}/{bucket}/object-acl | Object Storage Object ACL Config View |


<a id="cancelObjectStorage"></a>
# **cancelObjectStorage**
> Object cancelObjectStorage()

Object Storage Cancel

Cancel Object Storage on an Account.  **Warning**: Removes all buckets and their contents from your Account. This data is irretrievable once removed. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    try {
      Object result = apiInstance.cancelObjectStorage();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#cancelObjectStorage");
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

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Object Storage cancellation successful. |  -  |
| **0** | Error |  -  |

<a id="createObjectStorageBucket"></a>
# **createObjectStorageBucket**
> ObjectStorageBucket createObjectStorageBucket(createObjectStorageBucketRequest)

Object Storage Bucket Create

Creates an Object Storage Bucket in the specified cluster.  Accounts with negative balances cannot access this command.  If the bucket already exists and is owned by you, this endpoint returns a &#x60;200&#x60; response with that bucket as if it had just been created.  This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket) directly. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    CreateObjectStorageBucketRequest createObjectStorageBucketRequest = new CreateObjectStorageBucketRequest(); // CreateObjectStorageBucketRequest | Information about the bucket you want to create. 
    try {
      ObjectStorageBucket result = apiInstance.createObjectStorageBucket(createObjectStorageBucketRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#createObjectStorageBucket");
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
| **createObjectStorageBucketRequest** | [**CreateObjectStorageBucketRequest**](CreateObjectStorageBucketRequest.md)| Information about the bucket you want to create.  | [optional] |

### Return type

[**ObjectStorageBucket**](ObjectStorageBucket.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The bucket created successfully. |  -  |
| **0** | Error |  -  |

<a id="createObjectStorageKeys"></a>
# **createObjectStorageKeys**
> ObjectStorageKey createObjectStorageKeys(objectStorageKey)

Object Storage Key Create

Provisions a new Object Storage Key on your account.  Accounts with negative balances cannot access this command.  * To create a Limited Access Key with specific permissions, send a &#x60;bucket_access&#x60; array.  * To create a Limited Access Key without access to any buckets, send an empty &#x60;bucket_access&#x60; array.  * To create an Access Key with unlimited access to all clusters and all buckets, omit the &#x60;bucket_access&#x60; array. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    ObjectStorageKey objectStorageKey = new ObjectStorageKey(); // ObjectStorageKey | The label of the key to create. This is used to identify the created key. 
    try {
      ObjectStorageKey result = apiInstance.createObjectStorageKeys(objectStorageKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#createObjectStorageKeys");
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
| **objectStorageKey** | [**ObjectStorageKey**](ObjectStorageKey.md)| The label of the key to create. This is used to identify the created key.  | [optional] |

### Return type

[**ObjectStorageKey**](ObjectStorageKey.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The new keypair.  **This is the only time** the secret key is returned. |  -  |
| **0** | Error |  -  |

<a id="createObjectStorageObjectURL"></a>
# **createObjectStorageObjectURL**
> CreateObjectStorageObjectURL200Response createObjectStorageObjectURL(clusterId, bucket, createObjectStorageObjectURLRequest)

Object Storage Object URL Create

Creates a pre-signed URL to access a single Object in a bucket. This can be used to share objects, and also to create/delete objects by using the appropriate HTTP method in your request body&#39;s &#x60;method&#x60; parameter.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/) directly. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    String clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
    String bucket = "bucket_example"; // String | The bucket name.
    CreateObjectStorageObjectURLRequest createObjectStorageObjectURLRequest = new CreateObjectStorageObjectURLRequest(); // CreateObjectStorageObjectURLRequest | Information about the request to sign.
    try {
      CreateObjectStorageObjectURL200Response result = apiInstance.createObjectStorageObjectURL(clusterId, bucket, createObjectStorageObjectURLRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#createObjectStorageObjectURL");
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
| **clusterId** | **String**| The ID of the cluster this bucket exists in. | |
| **bucket** | **String**| The bucket name. | |
| **createObjectStorageObjectURLRequest** | [**CreateObjectStorageObjectURLRequest**](CreateObjectStorageObjectURLRequest.md)| Information about the request to sign. | [optional] |

### Return type

[**CreateObjectStorageObjectURL200Response**](CreateObjectStorageObjectURL200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The URL with which to access your object. |  -  |
| **0** | Error |  -  |

<a id="createObjectStorageSSL"></a>
# **createObjectStorageSSL**
> ObjectStorageSSLResponse createObjectStorageSSL(clusterId, bucket, objectStorageSSL)

Object Storage TLS/SSL Cert Upload

Upload a TLS/SSL certificate and private key to be served when you visit your Object Storage bucket via HTTPS. Your TLS/SSL certificate and private key are stored encrypted at rest.   To replace an expired certificate, [delete your current certificate](/docs/api/object-storage/#object-storage-tlsssl-cert-delete) and upload a new one. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    String clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
    String bucket = "bucket_example"; // String | The bucket name.
    ObjectStorageSSL objectStorageSSL = new ObjectStorageSSL(); // ObjectStorageSSL | Upload this TLS/SSL certificate with its corresponding secret key.
    try {
      ObjectStorageSSLResponse result = apiInstance.createObjectStorageSSL(clusterId, bucket, objectStorageSSL);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#createObjectStorageSSL");
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
| **clusterId** | **String**| The ID of the cluster this bucket exists in. | |
| **bucket** | **String**| The bucket name. | |
| **objectStorageSSL** | [**ObjectStorageSSL**](ObjectStorageSSL.md)| Upload this TLS/SSL certificate with its corresponding secret key. | [optional] |

### Return type

[**ObjectStorageSSLResponse**](ObjectStorageSSLResponse.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns whether this bucket has a corresponding TLS/SSL certificate that was uploaded by a user. |  -  |
| **0** | Error |  -  |

<a id="deleteObjectStorageBucket"></a>
# **deleteObjectStorageBucket**
> Object deleteObjectStorageBucket(clusterId, bucket)

Object Storage Bucket Remove

Removes a single bucket.  Bucket objects must be removed prior to removing the bucket. While buckets containing objects _may_ be deleted using the [s3cmd command-line tool](/docs/products/storage/object-storage/guides/s3cmd/#delete-a-bucket), such operations can fail if the bucket contains too many objects. The recommended way to empty large buckets is to use the [S3 API to configure lifecycle policies](https://docs.ceph.com/en/latest/radosgw/bucketpolicy/#) that remove all objects, then delete the bucket.  This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#delete-bucket) directly. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    String clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
    String bucket = "bucket_example"; // String | The bucket name.
    try {
      Object result = apiInstance.deleteObjectStorageBucket(clusterId, bucket);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#deleteObjectStorageBucket");
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
| **clusterId** | **String**| The ID of the cluster this bucket exists in. | |
| **bucket** | **String**| The bucket name. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bucket deleted successfully. |  -  |
| **0** | Error |  -  |

<a id="deleteObjectStorageKey"></a>
# **deleteObjectStorageKey**
> Object deleteObjectStorageKey(keyId)

Object Storage Key Revoke

Revokes an Object Storage Key.  This keypair will no longer be usable by third-party clients. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    Integer keyId = 56; // Integer | The key to look up.
    try {
      Object result = apiInstance.deleteObjectStorageKey(keyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#deleteObjectStorageKey");
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
| **keyId** | **Integer**| The key to look up. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deletion successful |  -  |
| **0** | Error |  -  |

<a id="deleteObjectStorageSSL"></a>
# **deleteObjectStorageSSL**
> Object deleteObjectStorageSSL(clusterId, bucket)

Object Storage TLS/SSL Cert Delete

Deletes this Object Storage bucket&#39;s user uploaded TLS/SSL certificate and private key. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    String clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
    String bucket = "bucket_example"; // String | The bucket name.
    try {
      Object result = apiInstance.deleteObjectStorageSSL(clusterId, bucket);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#deleteObjectStorageSSL");
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
| **clusterId** | **String**| The ID of the cluster this bucket exists in. | |
| **bucket** | **String**| The bucket name. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deletes this Object Storage bucket&#39;s user uploaded TLS/SSL certificate and private key. |  -  |
| **0** | Error |  -  |

<a id="getObjectStorageBucket"></a>
# **getObjectStorageBucket**
> ObjectStorageBucket getObjectStorageBucket(clusterId, bucket)

Object Storage Bucket View

Returns a single Object Storage Bucket.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#get-bucket) directly. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    String clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
    String bucket = "bucket_example"; // String | The bucket name.
    try {
      ObjectStorageBucket result = apiInstance.getObjectStorageBucket(clusterId, bucket);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#getObjectStorageBucket");
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
| **clusterId** | **String**| The ID of the cluster this bucket exists in. | |
| **bucket** | **String**| The bucket name. | |

### Return type

[**ObjectStorageBucket**](ObjectStorageBucket.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested bucket. |  -  |
| **0** | Error |  -  |

<a id="getObjectStorageBucketContent"></a>
# **getObjectStorageBucketContent**
> GetObjectStorageBucketContent200Response getObjectStorageBucketContent(clusterId, bucket, marker, delimiter, prefix, pageSize)

Object Storage Bucket Contents List

Returns the contents of a bucket. The contents are paginated using a &#x60;marker&#x60;, which is the name of the last object on the previous page.  Objects may be filtered by &#x60;prefix&#x60; and &#x60;delimiter&#x60; as well; see Query Parameters for more information.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#get-object) directly. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    String clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
    String bucket = "bucket_example"; // String | The bucket name.
    String marker = "marker_example"; // String | The \"marker\" for this request, which can be used to paginate through large buckets. Its value should be the value of the `next_marker` property returned with the last page. Listing bucket contents *does not* support arbitrary page access. See the `next_marker` property in the responses section for more details. 
    String delimiter = "delimiter_example"; // String | The delimiter for object names; if given, object names will be returned up to the first occurrence of this character. This is most commonly used with the `/` character to allow bucket transversal in a manner similar to a filesystem, however any delimiter may be used. Use in conjunction with `prefix` to see object names past the first occurrence of the delimiter. 
    String prefix = "prefix_example"; // String | Filters objects returned to only those whose name start with the given prefix. Commonly used in conjunction with `delimiter` to allow transversal of bucket contents in a manner similar to a filesystem. 
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetObjectStorageBucketContent200Response result = apiInstance.getObjectStorageBucketContent(clusterId, bucket, marker, delimiter, prefix, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#getObjectStorageBucketContent");
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
| **clusterId** | **String**| The ID of the cluster this bucket exists in. | |
| **bucket** | **String**| The bucket name. | |
| **marker** | **String**| The \&quot;marker\&quot; for this request, which can be used to paginate through large buckets. Its value should be the value of the &#x60;next_marker&#x60; property returned with the last page. Listing bucket contents *does not* support arbitrary page access. See the &#x60;next_marker&#x60; property in the responses section for more details.  | [optional] |
| **delimiter** | **String**| The delimiter for object names; if given, object names will be returned up to the first occurrence of this character. This is most commonly used with the &#x60;/&#x60; character to allow bucket transversal in a manner similar to a filesystem, however any delimiter may be used. Use in conjunction with &#x60;prefix&#x60; to see object names past the first occurrence of the delimiter.  | [optional] |
| **prefix** | **String**| Filters objects returned to only those whose name start with the given prefix. Commonly used in conjunction with &#x60;delimiter&#x60; to allow transversal of bucket contents in a manner similar to a filesystem.  | [optional] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetObjectStorageBucketContent200Response**](GetObjectStorageBucketContent200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One page of the requested bucket&#39;s contents. |  -  |
| **0** | Error |  -  |

<a id="getObjectStorageBucketinCluster"></a>
# **getObjectStorageBucketinCluster**
> GetObjectStorageBuckets200Response getObjectStorageBucketinCluster(clusterId)

Object Storage Buckets in Cluster List

Returns a list of Buckets in this cluster belonging to this Account.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#get-bucket) directly. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    String clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
    try {
      GetObjectStorageBuckets200Response result = apiInstance.getObjectStorageBucketinCluster(clusterId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#getObjectStorageBucketinCluster");
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
| **clusterId** | **String**| The ID of the cluster this bucket exists in. | |

### Return type

[**GetObjectStorageBuckets200Response**](GetObjectStorageBuckets200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of buckets you own in this cluster. |  -  |
| **0** | Error |  -  |

<a id="getObjectStorageBuckets"></a>
# **getObjectStorageBuckets**
> GetObjectStorageBuckets200Response getObjectStorageBuckets()

Object Storage Buckets List

Returns a paginated list of all Object Storage Buckets that you own.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/serviceops/#list-buckets) directly. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    try {
      GetObjectStorageBuckets200Response result = apiInstance.getObjectStorageBuckets();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#getObjectStorageBuckets");
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

[**GetObjectStorageBuckets200Response**](GetObjectStorageBuckets200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of buckets you own. |  -  |
| **0** | Error |  -  |

<a id="getObjectStorageCluster"></a>
# **getObjectStorageCluster**
> ObjectStorageCluster getObjectStorageCluster(clusterId)

Cluster View

Returns a single Object Storage Cluster. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    String clusterId = "clusterId_example"; // String | The ID of the Cluster.
    try {
      ObjectStorageCluster result = apiInstance.getObjectStorageCluster(clusterId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#getObjectStorageCluster");
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
| **clusterId** | **String**| The ID of the Cluster. | |

### Return type

[**ObjectStorageCluster**](ObjectStorageCluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested Cluster |  -  |
| **0** | Error |  -  |

<a id="getObjectStorageClusters"></a>
# **getObjectStorageClusters**
> GetObjectStorageClusters200Response getObjectStorageClusters()

Clusters List

Returns a paginated list of Object Storage Clusters that are available for use.  Users can connect to the clusters with third party clients to create buckets and upload objects. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    try {
      GetObjectStorageClusters200Response result = apiInstance.getObjectStorageClusters();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#getObjectStorageClusters");
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

[**GetObjectStorageClusters200Response**](GetObjectStorageClusters200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of available clusters. |  -  |
| **0** | Error |  -  |

<a id="getObjectStorageKey"></a>
# **getObjectStorageKey**
> ObjectStorageKey getObjectStorageKey(keyId)

Object Storage Key View

Returns a single Object Storage Key provisioned for your account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    Integer keyId = 56; // Integer | The key to look up.
    try {
      ObjectStorageKey result = apiInstance.getObjectStorageKey(keyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#getObjectStorageKey");
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
| **keyId** | **Integer**| The key to look up. | |

### Return type

[**ObjectStorageKey**](ObjectStorageKey.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The keypair |  -  |
| **0** | Error |  -  |

<a id="getObjectStorageKeys"></a>
# **getObjectStorageKeys**
> GetObjectStorageKeys200Response getObjectStorageKeys()

Object Storage Keys List

Returns a paginated list of Object Storage Keys for authenticating to the Object Storage S3 API. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    try {
      GetObjectStorageKeys200Response result = apiInstance.getObjectStorageKeys();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#getObjectStorageKeys");
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

[**GetObjectStorageKeys200Response**](GetObjectStorageKeys200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of Object Storage Keys |  -  |
| **0** | Error |  -  |

<a id="getObjectStorageSSL"></a>
# **getObjectStorageSSL**
> ObjectStorageSSLResponse getObjectStorageSSL(clusterId, bucket)

Object Storage TLS/SSL Cert View

Returns a boolean value indicating if this bucket has a corresponding TLS/SSL certificate that was uploaded by an Account user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    String clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
    String bucket = "bucket_example"; // String | The bucket name.
    try {
      ObjectStorageSSLResponse result = apiInstance.getObjectStorageSSL(clusterId, bucket);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#getObjectStorageSSL");
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
| **clusterId** | **String**| The ID of the cluster this bucket exists in. | |
| **bucket** | **String**| The bucket name. | |

### Return type

[**ObjectStorageSSLResponse**](ObjectStorageSSLResponse.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a boolean value indicating if this bucket has a corresponding TLS/SSL certificate that was uploaded by an Account user.  |  -  |
| **0** | Error |  -  |

<a id="getObjectStorageTransfer"></a>
# **getObjectStorageTransfer**
> GetObjectStorageTransfer200Response getObjectStorageTransfer()

Object Storage Transfer View

The amount of outbound data transfer used by your account&#39;s Object Storage buckets. Object Storage adds 1 terabyte of outbound data transfer to your data transfer pool. See the [Object Storage Overview](/docs/products/storage/object-storage/#pricing) guide for details on Object Storage transfer quotas. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    try {
      GetObjectStorageTransfer200Response result = apiInstance.getObjectStorageTransfer();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#getObjectStorageTransfer");
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

[**GetObjectStorageTransfer200Response**](GetObjectStorageTransfer200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the amount of outbound data transfer used by your account&#39;s Object Storage buckets.  |  -  |
| **0** | Error |  -  |

<a id="modifyObjectStorageBucketAccess"></a>
# **modifyObjectStorageBucketAccess**
> Object modifyObjectStorageBucketAccess(clusterId, bucket, updateObjectStorageBucketAccessRequest)

Object Storage Bucket Access Modify

Allows changing basic Cross-origin Resource Sharing (CORS) and Access Control Level (ACL) settings. Only allows enabling/disabling CORS for all origins, and/or setting canned ACLs.   For more fine-grained control of both systems, please use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket-acl) directly. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    String clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
    String bucket = "bucket_example"; // String | The bucket name.
    UpdateObjectStorageBucketAccessRequest updateObjectStorageBucketAccessRequest = new UpdateObjectStorageBucketAccessRequest(); // UpdateObjectStorageBucketAccessRequest | The changes to make to the bucket's access controls.
    try {
      Object result = apiInstance.modifyObjectStorageBucketAccess(clusterId, bucket, updateObjectStorageBucketAccessRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#modifyObjectStorageBucketAccess");
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
| **clusterId** | **String**| The ID of the cluster this bucket exists in. | |
| **bucket** | **String**| The bucket name. | |
| **updateObjectStorageBucketAccessRequest** | [**UpdateObjectStorageBucketAccessRequest**](UpdateObjectStorageBucketAccessRequest.md)| The changes to make to the bucket&#39;s access controls. | [optional] |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Access controls updated. |  -  |
| **0** | Error |  -  |

<a id="updateObjectStorageBucketACL"></a>
# **updateObjectStorageBucketACL**
> ViewObjectStorageBucketACL200Response updateObjectStorageBucketACL(clusterId, bucket, updateObjectStorageBucketACLRequest)

Object Storage Object ACL Config Update

Update an Object&#39;s configured Access Control List (ACL) in this Object Storage bucket. ACLs define who can access your buckets and objects and specify the level of access granted to those users.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#set-object-acl) directly. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    String clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
    String bucket = "bucket_example"; // String | The bucket name.
    UpdateObjectStorageBucketACLRequest updateObjectStorageBucketACLRequest = new UpdateObjectStorageBucketACLRequest(); // UpdateObjectStorageBucketACLRequest | The changes to make to this Object's access controls.
    try {
      ViewObjectStorageBucketACL200Response result = apiInstance.updateObjectStorageBucketACL(clusterId, bucket, updateObjectStorageBucketACLRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#updateObjectStorageBucketACL");
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
| **clusterId** | **String**| The ID of the cluster this bucket exists in. | |
| **bucket** | **String**| The bucket name. | |
| **updateObjectStorageBucketACLRequest** | [**UpdateObjectStorageBucketACLRequest**](UpdateObjectStorageBucketACLRequest.md)| The changes to make to this Object&#39;s access controls. | [optional] |

### Return type

[**ViewObjectStorageBucketACL200Response**](ViewObjectStorageBucketACL200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Object&#39;s canned ACL and policy. |  -  |
| **0** | Error |  -  |

<a id="updateObjectStorageBucketAccess"></a>
# **updateObjectStorageBucketAccess**
> Object updateObjectStorageBucketAccess(clusterId, bucket, updateObjectStorageBucketAccessRequest)

Object Storage Bucket Access Update

Allows changing basic Cross-origin Resource Sharing (CORS) and Access Control Level (ACL) settings. Only allows enabling/disabling CORS for all origins, and/or setting canned ACLs.   For more fine-grained control of both systems, please use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket-acl) directly. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    String clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
    String bucket = "bucket_example"; // String | The bucket name.
    UpdateObjectStorageBucketAccessRequest updateObjectStorageBucketAccessRequest = new UpdateObjectStorageBucketAccessRequest(); // UpdateObjectStorageBucketAccessRequest | The changes to make to the bucket's access controls.
    try {
      Object result = apiInstance.updateObjectStorageBucketAccess(clusterId, bucket, updateObjectStorageBucketAccessRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#updateObjectStorageBucketAccess");
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
| **clusterId** | **String**| The ID of the cluster this bucket exists in. | |
| **bucket** | **String**| The bucket name. | |
| **updateObjectStorageBucketAccessRequest** | [**UpdateObjectStorageBucketAccessRequest**](UpdateObjectStorageBucketAccessRequest.md)| The changes to make to the bucket&#39;s access controls. | [optional] |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Access controls updated. |  -  |
| **0** | Error |  -  |

<a id="updateObjectStorageKey"></a>
# **updateObjectStorageKey**
> ObjectStorageKey updateObjectStorageKey(keyId, updateObjectStorageKeyRequest)

Object Storage Key Update

Updates an Object Storage Key on your account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    Integer keyId = 56; // Integer | The key to look up.
    UpdateObjectStorageKeyRequest updateObjectStorageKeyRequest = new UpdateObjectStorageKeyRequest(); // UpdateObjectStorageKeyRequest | The fields to update.
    try {
      ObjectStorageKey result = apiInstance.updateObjectStorageKey(keyId, updateObjectStorageKeyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#updateObjectStorageKey");
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
| **keyId** | **Integer**| The key to look up. | |
| **updateObjectStorageKeyRequest** | [**UpdateObjectStorageKeyRequest**](UpdateObjectStorageKeyRequest.md)| The fields to update. | [optional] |

### Return type

[**ObjectStorageKey**](ObjectStorageKey.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update Successful |  -  |
| **0** | Error |  -  |

<a id="viewObjectStorageBucketACL"></a>
# **viewObjectStorageBucketACL**
> ViewObjectStorageBucketACL200Response viewObjectStorageBucketACL(clusterId, bucket, name)

Object Storage Object ACL Config View

View an Object&#39;s configured Access Control List (ACL) in this Object Storage bucket. ACLs define who can access your buckets and objects and specify the level of access granted to those users.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#get-object-acl) directly. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ObjectStorageApi apiInstance = new ObjectStorageApi(defaultClient);
    String clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
    String bucket = "bucket_example"; // String | The bucket name.
    String name = "name_example"; // String | The `name` of the object for which to retrieve its Access Control List (ACL). Use the [Object Storage Bucket Contents List](/docs/api/object-storage/#object-storage-bucket-contents-list) endpoint to access all object names in a bucket. 
    try {
      ViewObjectStorageBucketACL200Response result = apiInstance.viewObjectStorageBucketACL(clusterId, bucket, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectStorageApi#viewObjectStorageBucketACL");
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
| **clusterId** | **String**| The ID of the cluster this bucket exists in. | |
| **bucket** | **String**| The bucket name. | |
| **name** | **String**| The &#x60;name&#x60; of the object for which to retrieve its Access Control List (ACL). Use the [Object Storage Bucket Contents List](/docs/api/object-storage/#object-storage-bucket-contents-list) endpoint to access all object names in a bucket.  | |

### Return type

[**ViewObjectStorageBucketACL200Response**](ViewObjectStorageBucketACL200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Object&#39;s canned ACL and policy. |  -  |
| **0** | Error |  -  |

