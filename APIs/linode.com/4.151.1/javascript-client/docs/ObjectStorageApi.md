# LinodeApi.ObjectStorageApi

All URIs are relative to *https://api.linode.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelObjectStorage**](ObjectStorageApi.md#cancelObjectStorage) | **POST** /object-storage/cancel | Object Storage Cancel
[**createObjectStorageBucket**](ObjectStorageApi.md#createObjectStorageBucket) | **POST** /object-storage/buckets | Object Storage Bucket Create
[**createObjectStorageKeys**](ObjectStorageApi.md#createObjectStorageKeys) | **POST** /object-storage/keys | Object Storage Key Create
[**createObjectStorageObjectURL**](ObjectStorageApi.md#createObjectStorageObjectURL) | **POST** /object-storage/buckets/{clusterId}/{bucket}/object-url | Object Storage Object URL Create
[**createObjectStorageSSL**](ObjectStorageApi.md#createObjectStorageSSL) | **POST** /object-storage/buckets/{clusterId}/{bucket}/ssl | Object Storage TLS/SSL Cert Upload
[**deleteObjectStorageBucket**](ObjectStorageApi.md#deleteObjectStorageBucket) | **DELETE** /object-storage/buckets/{clusterId}/{bucket} | Object Storage Bucket Remove
[**deleteObjectStorageKey**](ObjectStorageApi.md#deleteObjectStorageKey) | **DELETE** /object-storage/keys/{keyId} | Object Storage Key Revoke
[**deleteObjectStorageSSL**](ObjectStorageApi.md#deleteObjectStorageSSL) | **DELETE** /object-storage/buckets/{clusterId}/{bucket}/ssl | Object Storage TLS/SSL Cert Delete
[**getObjectStorageBucket**](ObjectStorageApi.md#getObjectStorageBucket) | **GET** /object-storage/buckets/{clusterId}/{bucket} | Object Storage Bucket View
[**getObjectStorageBucketContent**](ObjectStorageApi.md#getObjectStorageBucketContent) | **GET** /object-storage/buckets/{clusterId}/{bucket}/object-list | Object Storage Bucket Contents List
[**getObjectStorageBucketinCluster**](ObjectStorageApi.md#getObjectStorageBucketinCluster) | **GET** /object-storage/buckets/{clusterId} | Object Storage Buckets in Cluster List
[**getObjectStorageBuckets**](ObjectStorageApi.md#getObjectStorageBuckets) | **GET** /object-storage/buckets | Object Storage Buckets List
[**getObjectStorageCluster**](ObjectStorageApi.md#getObjectStorageCluster) | **GET** /object-storage/clusters/{clusterId} | Cluster View
[**getObjectStorageClusters**](ObjectStorageApi.md#getObjectStorageClusters) | **GET** /object-storage/clusters | Clusters List
[**getObjectStorageKey**](ObjectStorageApi.md#getObjectStorageKey) | **GET** /object-storage/keys/{keyId} | Object Storage Key View
[**getObjectStorageKeys**](ObjectStorageApi.md#getObjectStorageKeys) | **GET** /object-storage/keys | Object Storage Keys List
[**getObjectStorageSSL**](ObjectStorageApi.md#getObjectStorageSSL) | **GET** /object-storage/buckets/{clusterId}/{bucket}/ssl | Object Storage TLS/SSL Cert View
[**getObjectStorageTransfer**](ObjectStorageApi.md#getObjectStorageTransfer) | **GET** /object-storage/transfer | Object Storage Transfer View
[**modifyObjectStorageBucketAccess**](ObjectStorageApi.md#modifyObjectStorageBucketAccess) | **POST** /object-storage/buckets/{clusterId}/{bucket}/access | Object Storage Bucket Access Modify
[**updateObjectStorageBucketACL**](ObjectStorageApi.md#updateObjectStorageBucketACL) | **PUT** /object-storage/buckets/{clusterId}/{bucket}/object-acl | Object Storage Object ACL Config Update
[**updateObjectStorageBucketAccess**](ObjectStorageApi.md#updateObjectStorageBucketAccess) | **PUT** /object-storage/buckets/{clusterId}/{bucket}/access | Object Storage Bucket Access Update
[**updateObjectStorageKey**](ObjectStorageApi.md#updateObjectStorageKey) | **PUT** /object-storage/keys/{keyId} | Object Storage Key Update
[**viewObjectStorageBucketACL**](ObjectStorageApi.md#viewObjectStorageBucketACL) | **GET** /object-storage/buckets/{clusterId}/{bucket}/object-acl | Object Storage Object ACL Config View



## cancelObjectStorage

> Object cancelObjectStorage()

Object Storage Cancel

Cancel Object Storage on an Account.  **Warning**: Removes all buckets and their contents from your Account. This data is irretrievable once removed. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ObjectStorageApi();
apiInstance.cancelObjectStorage((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## createObjectStorageBucket

> ObjectStorageBucket createObjectStorageBucket(opts)

Object Storage Bucket Create

Creates an Object Storage Bucket in the specified cluster.  Accounts with negative balances cannot access this command.  If the bucket already exists and is owned by you, this endpoint returns a &#x60;200&#x60; response with that bucket as if it had just been created.  This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket) directly. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ObjectStorageApi();
let opts = {
  'createObjectStorageBucketRequest': new LinodeApi.CreateObjectStorageBucketRequest() // CreateObjectStorageBucketRequest | Information about the bucket you want to create. 
};
apiInstance.createObjectStorageBucket(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createObjectStorageBucketRequest** | [**CreateObjectStorageBucketRequest**](CreateObjectStorageBucketRequest.md)| Information about the bucket you want to create.  | [optional] 

### Return type

[**ObjectStorageBucket**](ObjectStorageBucket.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createObjectStorageKeys

> ObjectStorageKey createObjectStorageKeys(opts)

Object Storage Key Create

Provisions a new Object Storage Key on your account.  Accounts with negative balances cannot access this command.  * To create a Limited Access Key with specific permissions, send a &#x60;bucket_access&#x60; array.  * To create a Limited Access Key without access to any buckets, send an empty &#x60;bucket_access&#x60; array.  * To create an Access Key with unlimited access to all clusters and all buckets, omit the &#x60;bucket_access&#x60; array. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ObjectStorageApi();
let opts = {
  'objectStorageKey': new LinodeApi.ObjectStorageKey() // ObjectStorageKey | The label of the key to create. This is used to identify the created key. 
};
apiInstance.createObjectStorageKeys(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **objectStorageKey** | [**ObjectStorageKey**](ObjectStorageKey.md)| The label of the key to create. This is used to identify the created key.  | [optional] 

### Return type

[**ObjectStorageKey**](ObjectStorageKey.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createObjectStorageObjectURL

> CreateObjectStorageObjectURL200Response createObjectStorageObjectURL(clusterId, bucket, opts)

Object Storage Object URL Create

Creates a pre-signed URL to access a single Object in a bucket. This can be used to share objects, and also to create/delete objects by using the appropriate HTTP method in your request body&#39;s &#x60;method&#x60; parameter.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/) directly. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ObjectStorageApi();
let clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
let bucket = "bucket_example"; // String | The bucket name.
let opts = {
  'createObjectStorageObjectURLRequest': new LinodeApi.CreateObjectStorageObjectURLRequest() // CreateObjectStorageObjectURLRequest | Information about the request to sign.
};
apiInstance.createObjectStorageObjectURL(clusterId, bucket, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **String**| The ID of the cluster this bucket exists in. | 
 **bucket** | **String**| The bucket name. | 
 **createObjectStorageObjectURLRequest** | [**CreateObjectStorageObjectURLRequest**](CreateObjectStorageObjectURLRequest.md)| Information about the request to sign. | [optional] 

### Return type

[**CreateObjectStorageObjectURL200Response**](CreateObjectStorageObjectURL200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createObjectStorageSSL

> ObjectStorageSSLResponse createObjectStorageSSL(clusterId, bucket, opts)

Object Storage TLS/SSL Cert Upload

Upload a TLS/SSL certificate and private key to be served when you visit your Object Storage bucket via HTTPS. Your TLS/SSL certificate and private key are stored encrypted at rest.   To replace an expired certificate, [delete your current certificate](/docs/api/object-storage/#object-storage-tlsssl-cert-delete) and upload a new one. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ObjectStorageApi();
let clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
let bucket = "bucket_example"; // String | The bucket name.
let opts = {
  'objectStorageSSL': new LinodeApi.ObjectStorageSSL() // ObjectStorageSSL | Upload this TLS/SSL certificate with its corresponding secret key.
};
apiInstance.createObjectStorageSSL(clusterId, bucket, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **String**| The ID of the cluster this bucket exists in. | 
 **bucket** | **String**| The bucket name. | 
 **objectStorageSSL** | [**ObjectStorageSSL**](ObjectStorageSSL.md)| Upload this TLS/SSL certificate with its corresponding secret key. | [optional] 

### Return type

[**ObjectStorageSSLResponse**](ObjectStorageSSLResponse.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteObjectStorageBucket

> Object deleteObjectStorageBucket(clusterId, bucket)

Object Storage Bucket Remove

Removes a single bucket.  Bucket objects must be removed prior to removing the bucket. While buckets containing objects _may_ be deleted using the [s3cmd command-line tool](/docs/products/storage/object-storage/guides/s3cmd/#delete-a-bucket), such operations can fail if the bucket contains too many objects. The recommended way to empty large buckets is to use the [S3 API to configure lifecycle policies](https://docs.ceph.com/en/latest/radosgw/bucketpolicy/#) that remove all objects, then delete the bucket.  This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#delete-bucket) directly. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ObjectStorageApi();
let clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
let bucket = "bucket_example"; // String | The bucket name.
apiInstance.deleteObjectStorageBucket(clusterId, bucket, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **String**| The ID of the cluster this bucket exists in. | 
 **bucket** | **String**| The bucket name. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteObjectStorageKey

> Object deleteObjectStorageKey(keyId)

Object Storage Key Revoke

Revokes an Object Storage Key.  This keypair will no longer be usable by third-party clients. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ObjectStorageApi();
let keyId = 56; // Number | The key to look up.
apiInstance.deleteObjectStorageKey(keyId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyId** | **Number**| The key to look up. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteObjectStorageSSL

> Object deleteObjectStorageSSL(clusterId, bucket)

Object Storage TLS/SSL Cert Delete

Deletes this Object Storage bucket&#39;s user uploaded TLS/SSL certificate and private key. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ObjectStorageApi();
let clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
let bucket = "bucket_example"; // String | The bucket name.
apiInstance.deleteObjectStorageSSL(clusterId, bucket, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **String**| The ID of the cluster this bucket exists in. | 
 **bucket** | **String**| The bucket name. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getObjectStorageBucket

> ObjectStorageBucket getObjectStorageBucket(clusterId, bucket)

Object Storage Bucket View

Returns a single Object Storage Bucket.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#get-bucket) directly. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ObjectStorageApi();
let clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
let bucket = "bucket_example"; // String | The bucket name.
apiInstance.getObjectStorageBucket(clusterId, bucket, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **String**| The ID of the cluster this bucket exists in. | 
 **bucket** | **String**| The bucket name. | 

### Return type

[**ObjectStorageBucket**](ObjectStorageBucket.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getObjectStorageBucketContent

> GetObjectStorageBucketContent200Response getObjectStorageBucketContent(clusterId, bucket, opts)

Object Storage Bucket Contents List

Returns the contents of a bucket. The contents are paginated using a &#x60;marker&#x60;, which is the name of the last object on the previous page.  Objects may be filtered by &#x60;prefix&#x60; and &#x60;delimiter&#x60; as well; see Query Parameters for more information.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#get-object) directly. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ObjectStorageApi();
let clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
let bucket = "bucket_example"; // String | The bucket name.
let opts = {
  'marker': "marker_example", // String | The \"marker\" for this request, which can be used to paginate through large buckets. Its value should be the value of the `next_marker` property returned with the last page. Listing bucket contents *does not* support arbitrary page access. See the `next_marker` property in the responses section for more details. 
  'delimiter': "delimiter_example", // String | The delimiter for object names; if given, object names will be returned up to the first occurrence of this character. This is most commonly used with the `/` character to allow bucket transversal in a manner similar to a filesystem, however any delimiter may be used. Use in conjunction with `prefix` to see object names past the first occurrence of the delimiter. 
  'prefix': "prefix_example", // String | Filters objects returned to only those whose name start with the given prefix. Commonly used in conjunction with `delimiter` to allow transversal of bucket contents in a manner similar to a filesystem. 
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getObjectStorageBucketContent(clusterId, bucket, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **String**| The ID of the cluster this bucket exists in. | 
 **bucket** | **String**| The bucket name. | 
 **marker** | **String**| The \&quot;marker\&quot; for this request, which can be used to paginate through large buckets. Its value should be the value of the &#x60;next_marker&#x60; property returned with the last page. Listing bucket contents *does not* support arbitrary page access. See the &#x60;next_marker&#x60; property in the responses section for more details.  | [optional] 
 **delimiter** | **String**| The delimiter for object names; if given, object names will be returned up to the first occurrence of this character. This is most commonly used with the &#x60;/&#x60; character to allow bucket transversal in a manner similar to a filesystem, however any delimiter may be used. Use in conjunction with &#x60;prefix&#x60; to see object names past the first occurrence of the delimiter.  | [optional] 
 **prefix** | **String**| Filters objects returned to only those whose name start with the given prefix. Commonly used in conjunction with &#x60;delimiter&#x60; to allow transversal of bucket contents in a manner similar to a filesystem.  | [optional] 
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetObjectStorageBucketContent200Response**](GetObjectStorageBucketContent200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getObjectStorageBucketinCluster

> GetObjectStorageBuckets200Response getObjectStorageBucketinCluster(clusterId)

Object Storage Buckets in Cluster List

Returns a list of Buckets in this cluster belonging to this Account.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#get-bucket) directly. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ObjectStorageApi();
let clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
apiInstance.getObjectStorageBucketinCluster(clusterId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **String**| The ID of the cluster this bucket exists in. | 

### Return type

[**GetObjectStorageBuckets200Response**](GetObjectStorageBuckets200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getObjectStorageBuckets

> GetObjectStorageBuckets200Response getObjectStorageBuckets()

Object Storage Buckets List

Returns a paginated list of all Object Storage Buckets that you own.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/serviceops/#list-buckets) directly. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ObjectStorageApi();
apiInstance.getObjectStorageBuckets((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## getObjectStorageCluster

> ObjectStorageCluster getObjectStorageCluster(clusterId)

Cluster View

Returns a single Object Storage Cluster. 

### Example

```javascript
import LinodeApi from 'linode_api';

let apiInstance = new LinodeApi.ObjectStorageApi();
let clusterId = "clusterId_example"; // String | The ID of the Cluster.
apiInstance.getObjectStorageCluster(clusterId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **String**| The ID of the Cluster. | 

### Return type

[**ObjectStorageCluster**](ObjectStorageCluster.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getObjectStorageClusters

> GetObjectStorageClusters200Response getObjectStorageClusters()

Clusters List

Returns a paginated list of Object Storage Clusters that are available for use.  Users can connect to the clusters with third party clients to create buckets and upload objects. 

### Example

```javascript
import LinodeApi from 'linode_api';

let apiInstance = new LinodeApi.ObjectStorageApi();
apiInstance.getObjectStorageClusters((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## getObjectStorageKey

> ObjectStorageKey getObjectStorageKey(keyId)

Object Storage Key View

Returns a single Object Storage Key provisioned for your account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ObjectStorageApi();
let keyId = 56; // Number | The key to look up.
apiInstance.getObjectStorageKey(keyId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyId** | **Number**| The key to look up. | 

### Return type

[**ObjectStorageKey**](ObjectStorageKey.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getObjectStorageKeys

> GetObjectStorageKeys200Response getObjectStorageKeys()

Object Storage Keys List

Returns a paginated list of Object Storage Keys for authenticating to the Object Storage S3 API. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ObjectStorageApi();
apiInstance.getObjectStorageKeys((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## getObjectStorageSSL

> ObjectStorageSSLResponse getObjectStorageSSL(clusterId, bucket)

Object Storage TLS/SSL Cert View

Returns a boolean value indicating if this bucket has a corresponding TLS/SSL certificate that was uploaded by an Account user. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ObjectStorageApi();
let clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
let bucket = "bucket_example"; // String | The bucket name.
apiInstance.getObjectStorageSSL(clusterId, bucket, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **String**| The ID of the cluster this bucket exists in. | 
 **bucket** | **String**| The bucket name. | 

### Return type

[**ObjectStorageSSLResponse**](ObjectStorageSSLResponse.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getObjectStorageTransfer

> GetObjectStorageTransfer200Response getObjectStorageTransfer()

Object Storage Transfer View

The amount of outbound data transfer used by your account&#39;s Object Storage buckets. Object Storage adds 1 terabyte of outbound data transfer to your data transfer pool. See the [Object Storage Overview](/docs/products/storage/object-storage/#pricing) guide for details on Object Storage transfer quotas. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ObjectStorageApi();
apiInstance.getObjectStorageTransfer((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## modifyObjectStorageBucketAccess

> Object modifyObjectStorageBucketAccess(clusterId, bucket, opts)

Object Storage Bucket Access Modify

Allows changing basic Cross-origin Resource Sharing (CORS) and Access Control Level (ACL) settings. Only allows enabling/disabling CORS for all origins, and/or setting canned ACLs.   For more fine-grained control of both systems, please use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket-acl) directly. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ObjectStorageApi();
let clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
let bucket = "bucket_example"; // String | The bucket name.
let opts = {
  'updateObjectStorageBucketAccessRequest': new LinodeApi.UpdateObjectStorageBucketAccessRequest() // UpdateObjectStorageBucketAccessRequest | The changes to make to the bucket's access controls.
};
apiInstance.modifyObjectStorageBucketAccess(clusterId, bucket, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **String**| The ID of the cluster this bucket exists in. | 
 **bucket** | **String**| The bucket name. | 
 **updateObjectStorageBucketAccessRequest** | [**UpdateObjectStorageBucketAccessRequest**](UpdateObjectStorageBucketAccessRequest.md)| The changes to make to the bucket&#39;s access controls. | [optional] 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateObjectStorageBucketACL

> ViewObjectStorageBucketACL200Response updateObjectStorageBucketACL(clusterId, bucket, opts)

Object Storage Object ACL Config Update

Update an Object&#39;s configured Access Control List (ACL) in this Object Storage bucket. ACLs define who can access your buckets and objects and specify the level of access granted to those users.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#set-object-acl) directly. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ObjectStorageApi();
let clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
let bucket = "bucket_example"; // String | The bucket name.
let opts = {
  'updateObjectStorageBucketACLRequest': new LinodeApi.UpdateObjectStorageBucketACLRequest() // UpdateObjectStorageBucketACLRequest | The changes to make to this Object's access controls.
};
apiInstance.updateObjectStorageBucketACL(clusterId, bucket, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **String**| The ID of the cluster this bucket exists in. | 
 **bucket** | **String**| The bucket name. | 
 **updateObjectStorageBucketACLRequest** | [**UpdateObjectStorageBucketACLRequest**](UpdateObjectStorageBucketACLRequest.md)| The changes to make to this Object&#39;s access controls. | [optional] 

### Return type

[**ViewObjectStorageBucketACL200Response**](ViewObjectStorageBucketACL200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateObjectStorageBucketAccess

> Object updateObjectStorageBucketAccess(clusterId, bucket, opts)

Object Storage Bucket Access Update

Allows changing basic Cross-origin Resource Sharing (CORS) and Access Control Level (ACL) settings. Only allows enabling/disabling CORS for all origins, and/or setting canned ACLs.   For more fine-grained control of both systems, please use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket-acl) directly. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ObjectStorageApi();
let clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
let bucket = "bucket_example"; // String | The bucket name.
let opts = {
  'updateObjectStorageBucketAccessRequest': new LinodeApi.UpdateObjectStorageBucketAccessRequest() // UpdateObjectStorageBucketAccessRequest | The changes to make to the bucket's access controls.
};
apiInstance.updateObjectStorageBucketAccess(clusterId, bucket, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **String**| The ID of the cluster this bucket exists in. | 
 **bucket** | **String**| The bucket name. | 
 **updateObjectStorageBucketAccessRequest** | [**UpdateObjectStorageBucketAccessRequest**](UpdateObjectStorageBucketAccessRequest.md)| The changes to make to the bucket&#39;s access controls. | [optional] 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateObjectStorageKey

> ObjectStorageKey updateObjectStorageKey(keyId, opts)

Object Storage Key Update

Updates an Object Storage Key on your account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ObjectStorageApi();
let keyId = 56; // Number | The key to look up.
let opts = {
  'updateObjectStorageKeyRequest': new LinodeApi.UpdateObjectStorageKeyRequest() // UpdateObjectStorageKeyRequest | The fields to update.
};
apiInstance.updateObjectStorageKey(keyId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyId** | **Number**| The key to look up. | 
 **updateObjectStorageKeyRequest** | [**UpdateObjectStorageKeyRequest**](UpdateObjectStorageKeyRequest.md)| The fields to update. | [optional] 

### Return type

[**ObjectStorageKey**](ObjectStorageKey.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## viewObjectStorageBucketACL

> ViewObjectStorageBucketACL200Response viewObjectStorageBucketACL(clusterId, bucket, name)

Object Storage Object ACL Config View

View an Object&#39;s configured Access Control List (ACL) in this Object Storage bucket. ACLs define who can access your buckets and objects and specify the level of access granted to those users.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#get-object-acl) directly. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ObjectStorageApi();
let clusterId = "clusterId_example"; // String | The ID of the cluster this bucket exists in.
let bucket = "bucket_example"; // String | The bucket name.
let name = "name_example"; // String | The `name` of the object for which to retrieve its Access Control List (ACL). Use the [Object Storage Bucket Contents List](/docs/api/object-storage/#object-storage-bucket-contents-list) endpoint to access all object names in a bucket. 
apiInstance.viewObjectStorageBucketACL(clusterId, bucket, name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **String**| The ID of the cluster this bucket exists in. | 
 **bucket** | **String**| The bucket name. | 
 **name** | **String**| The &#x60;name&#x60; of the object for which to retrieve its Access Control List (ACL). Use the [Object Storage Bucket Contents List](/docs/api/object-storage/#object-storage-bucket-contents-list) endpoint to access all object names in a bucket.  | 

### Return type

[**ViewObjectStorageBucketACL200Response**](ViewObjectStorageBucketACL200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

