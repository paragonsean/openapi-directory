# AwsElementalMediaStoreDataPlane.DefaultApi

All URIs are relative to *http://data.mediastore.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteObject**](DefaultApi.md#deleteObject) | **DELETE** /{Path} | 
[**describeObject**](DefaultApi.md#describeObject) | **HEAD** /{Path} | 
[**getObject**](DefaultApi.md#getObject) | **GET** /{Path} | 
[**listItems**](DefaultApi.md#listItems) | **GET** / | 
[**putObject**](DefaultApi.md#putObject) | **PUT** /{Path} | 



## deleteObject

> Object deleteObject(path, opts)



Deletes an object at the specified path.

### Example

```javascript
import AwsElementalMediaStoreDataPlane from 'aws_elemental_media_store_data_plane';
let defaultClient = AwsElementalMediaStoreDataPlane.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStoreDataPlane.DefaultApi();
let path = "path_example"; // String | The path (including the file name) where the object is stored in the container. Format: &lt;folder name&gt;/&lt;folder name&gt;/&lt;file name&gt;
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteObject(path, opts, (error, data, response) => {
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
 **path** | **String**| The path (including the file name) where the object is stored in the container. Format: &amp;lt;folder name&amp;gt;/&amp;lt;folder name&amp;gt;/&amp;lt;file name&amp;gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeObject

> Object describeObject(path, opts)



Gets the headers for an object at the specified path.

### Example

```javascript
import AwsElementalMediaStoreDataPlane from 'aws_elemental_media_store_data_plane';
let defaultClient = AwsElementalMediaStoreDataPlane.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStoreDataPlane.DefaultApi();
let path = "path_example"; // String | The path (including the file name) where the object is stored in the container. Format: &lt;folder name&gt;/&lt;folder name&gt;/&lt;file name&gt;
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeObject(path, opts, (error, data, response) => {
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
 **path** | **String**| The path (including the file name) where the object is stored in the container. Format: &amp;lt;folder name&amp;gt;/&amp;lt;folder name&amp;gt;/&amp;lt;file name&amp;gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getObject

> GetObjectResponse getObject(path, opts)



Downloads the object at the specified path. If the object’s upload availability is set to &lt;code&gt;streaming&lt;/code&gt;, AWS Elemental MediaStore downloads the object even if it’s still uploading the object.

### Example

```javascript
import AwsElementalMediaStoreDataPlane from 'aws_elemental_media_store_data_plane';
let defaultClient = AwsElementalMediaStoreDataPlane.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStoreDataPlane.DefaultApi();
let path = "path_example"; // String | <p>The path (including the file name) where the object is stored in the container. Format: &lt;folder name&gt;/&lt;folder name&gt;/&lt;file name&gt;</p> <p>For example, to upload the file <code>mlaw.avi</code> to the folder path <code>premium\\canada</code> in the container <code>movies</code>, enter the path <code>premium/canada/mlaw.avi</code>.</p> <p>Do not include the container name in this path.</p> <p>If the path includes any folders that don't exist yet, the service creates them. For example, suppose you have an existing <code>premium/usa</code> subfolder. If you specify <code>premium/canada</code>, the service creates a <code>canada</code> subfolder in the <code>premium</code> folder. You then have two subfolders, <code>usa</code> and <code>canada</code>, in the <code>premium</code> folder. </p> <p>There is no correlation between the path to the source and the path (folders) in the container in AWS Elemental MediaStore.</p> <p>For more information about folders and how they exist in a container, see the <a href=\"http://docs.aws.amazon.com/mediastore/latest/ug/\">AWS Elemental MediaStore User Guide</a>.</p> <p>The file name is the name that is assigned to the file that you upload. The file can have the same name inside and outside of AWS Elemental MediaStore, or it can have the same name. The file name can include or omit an extension. </p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'range': "range_example" // String | The range bytes of an object to retrieve. For more information about the <code>Range</code> header, see <a href=\"http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35\">http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35</a>. AWS Elemental MediaStore ignores this header for partially uploaded objects that have streaming upload availability.
};
apiInstance.getObject(path, opts, (error, data, response) => {
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
 **path** | **String**| &lt;p&gt;The path (including the file name) where the object is stored in the container. Format: &amp;lt;folder name&amp;gt;/&amp;lt;folder name&amp;gt;/&amp;lt;file name&amp;gt;&lt;/p&gt; &lt;p&gt;For example, to upload the file &lt;code&gt;mlaw.avi&lt;/code&gt; to the folder path &lt;code&gt;premium\\canada&lt;/code&gt; in the container &lt;code&gt;movies&lt;/code&gt;, enter the path &lt;code&gt;premium/canada/mlaw.avi&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Do not include the container name in this path.&lt;/p&gt; &lt;p&gt;If the path includes any folders that don&#39;t exist yet, the service creates them. For example, suppose you have an existing &lt;code&gt;premium/usa&lt;/code&gt; subfolder. If you specify &lt;code&gt;premium/canada&lt;/code&gt;, the service creates a &lt;code&gt;canada&lt;/code&gt; subfolder in the &lt;code&gt;premium&lt;/code&gt; folder. You then have two subfolders, &lt;code&gt;usa&lt;/code&gt; and &lt;code&gt;canada&lt;/code&gt;, in the &lt;code&gt;premium&lt;/code&gt; folder. &lt;/p&gt; &lt;p&gt;There is no correlation between the path to the source and the path (folders) in the container in AWS Elemental MediaStore.&lt;/p&gt; &lt;p&gt;For more information about folders and how they exist in a container, see the &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/mediastore/latest/ug/\&quot;&gt;AWS Elemental MediaStore User Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The file name is the name that is assigned to the file that you upload. The file can have the same name inside and outside of AWS Elemental MediaStore, or it can have the same name. The file name can include or omit an extension. &lt;/p&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **range** | **String**| The range bytes of an object to retrieve. For more information about the &lt;code&gt;Range&lt;/code&gt; header, see &lt;a href&#x3D;\&quot;http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35\&quot;&gt;http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35&lt;/a&gt;. AWS Elemental MediaStore ignores this header for partially uploaded objects that have streaming upload availability. | [optional] 

### Return type

[**GetObjectResponse**](GetObjectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listItems

> ListItemsResponse listItems(opts)



Provides a list of metadata entries about folders and objects in the specified folder.

### Example

```javascript
import AwsElementalMediaStoreDataPlane from 'aws_elemental_media_store_data_plane';
let defaultClient = AwsElementalMediaStoreDataPlane.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStoreDataPlane.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'path': "path_example", // String | The path in the container from which to retrieve items. Format: &lt;folder name&gt;/&lt;folder name&gt;/&lt;file name&gt;
  'maxResults': 56, // Number | <p>The maximum number of results to return per API request. For example, you submit a <code>ListItems</code> request with <code>MaxResults</code> set at 500. Although 2,000 items match your request, the service returns no more than the first 500 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) The service might return fewer results than the <code>MaxResults</code> value.</p> <p>If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 1,000 results per page.</p>
  'nextToken': "nextToken_example" // String | <p>The token that identifies which batch of results that you want to see. For example, you submit a <code>ListItems</code> request with <code>MaxResults</code> set at 500. The service returns the first batch of results (up to 500) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListItems</code> request a second time and specify the <code>NextToken</code> value.</p> <p>Tokens expire after 15 minutes.</p>
};
apiInstance.listItems(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **path** | **String**| The path in the container from which to retrieve items. Format: &amp;lt;folder name&amp;gt;/&amp;lt;folder name&amp;gt;/&amp;lt;file name&amp;gt; | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return per API request. For example, you submit a &lt;code&gt;ListItems&lt;/code&gt; request with &lt;code&gt;MaxResults&lt;/code&gt; set at 500. Although 2,000 items match your request, the service returns no more than the first 500 items. (The service also returns a &lt;code&gt;NextToken&lt;/code&gt; value that you can use to fetch the next batch of results.) The service might return fewer results than the &lt;code&gt;MaxResults&lt;/code&gt; value.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;MaxResults&lt;/code&gt; is not included in the request, the service defaults to pagination with a maximum of 1,000 results per page.&lt;/p&gt; | [optional] 
 **nextToken** | **String**| &lt;p&gt;The token that identifies which batch of results that you want to see. For example, you submit a &lt;code&gt;ListItems&lt;/code&gt; request with &lt;code&gt;MaxResults&lt;/code&gt; set at 500. The service returns the first batch of results (up to 500) and a &lt;code&gt;NextToken&lt;/code&gt; value. To see the next batch of results, you can submit the &lt;code&gt;ListItems&lt;/code&gt; request a second time and specify the &lt;code&gt;NextToken&lt;/code&gt; value.&lt;/p&gt; &lt;p&gt;Tokens expire after 15 minutes.&lt;/p&gt; | [optional] 

### Return type

[**ListItemsResponse**](ListItemsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putObject

> PutObjectResponse putObject(path, putObjectRequest, opts)



Uploads an object to the specified path. Object sizes are limited to 25 MB for standard upload availability and 10 MB for streaming upload availability.

### Example

```javascript
import AwsElementalMediaStoreDataPlane from 'aws_elemental_media_store_data_plane';
let defaultClient = AwsElementalMediaStoreDataPlane.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaStoreDataPlane.DefaultApi();
let path = "path_example"; // String | <p>The path (including the file name) where the object is stored in the container. Format: &lt;folder name&gt;/&lt;folder name&gt;/&lt;file name&gt;</p> <p>For example, to upload the file <code>mlaw.avi</code> to the folder path <code>premium\\canada</code> in the container <code>movies</code>, enter the path <code>premium/canada/mlaw.avi</code>.</p> <p>Do not include the container name in this path.</p> <p>If the path includes any folders that don't exist yet, the service creates them. For example, suppose you have an existing <code>premium/usa</code> subfolder. If you specify <code>premium/canada</code>, the service creates a <code>canada</code> subfolder in the <code>premium</code> folder. You then have two subfolders, <code>usa</code> and <code>canada</code>, in the <code>premium</code> folder. </p> <p>There is no correlation between the path to the source and the path (folders) in the container in AWS Elemental MediaStore.</p> <p>For more information about folders and how they exist in a container, see the <a href=\"http://docs.aws.amazon.com/mediastore/latest/ug/\">AWS Elemental MediaStore User Guide</a>.</p> <p>The file name is the name that is assigned to the file that you upload. The file can have the same name inside and outside of AWS Elemental MediaStore, or it can have the same name. The file name can include or omit an extension. </p>
let putObjectRequest = new AwsElementalMediaStoreDataPlane.PutObjectRequest(); // PutObjectRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'contentType': "contentType_example", // String | The content type of the object.
  'cacheControl': "cacheControl_example", // String | <p>An optional <code>CacheControl</code> header that allows the caller to control the object's cache behavior. Headers can be passed in as specified in the HTTP at <a href=\"https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9\">https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9</a>.</p> <p>Headers with a custom user-defined value are also accepted.</p>
  'xAmzStorageClass': "xAmzStorageClass_example", // String | Indicates the storage class of a <code>Put</code> request. Defaults to high-performance temporal storage class, and objects are persisted into durable storage shortly after being received.
  'xAmzUploadAvailability': "xAmzUploadAvailability_example" // String | <p>Indicates the availability of an object while it is still uploading. If the value is set to <code>streaming</code>, the object is available for downloading after some initial buffering but before the object is uploaded completely. If the value is set to <code>standard</code>, the object is available for downloading only when it is uploaded completely. The default value for this header is <code>standard</code>.</p> <p>To use this header, you must also set the HTTP <code>Transfer-Encoding</code> header to <code>chunked</code>.</p>
};
apiInstance.putObject(path, putObjectRequest, opts, (error, data, response) => {
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
 **path** | **String**| &lt;p&gt;The path (including the file name) where the object is stored in the container. Format: &amp;lt;folder name&amp;gt;/&amp;lt;folder name&amp;gt;/&amp;lt;file name&amp;gt;&lt;/p&gt; &lt;p&gt;For example, to upload the file &lt;code&gt;mlaw.avi&lt;/code&gt; to the folder path &lt;code&gt;premium\\canada&lt;/code&gt; in the container &lt;code&gt;movies&lt;/code&gt;, enter the path &lt;code&gt;premium/canada/mlaw.avi&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Do not include the container name in this path.&lt;/p&gt; &lt;p&gt;If the path includes any folders that don&#39;t exist yet, the service creates them. For example, suppose you have an existing &lt;code&gt;premium/usa&lt;/code&gt; subfolder. If you specify &lt;code&gt;premium/canada&lt;/code&gt;, the service creates a &lt;code&gt;canada&lt;/code&gt; subfolder in the &lt;code&gt;premium&lt;/code&gt; folder. You then have two subfolders, &lt;code&gt;usa&lt;/code&gt; and &lt;code&gt;canada&lt;/code&gt;, in the &lt;code&gt;premium&lt;/code&gt; folder. &lt;/p&gt; &lt;p&gt;There is no correlation between the path to the source and the path (folders) in the container in AWS Elemental MediaStore.&lt;/p&gt; &lt;p&gt;For more information about folders and how they exist in a container, see the &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/mediastore/latest/ug/\&quot;&gt;AWS Elemental MediaStore User Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The file name is the name that is assigned to the file that you upload. The file can have the same name inside and outside of AWS Elemental MediaStore, or it can have the same name. The file name can include or omit an extension. &lt;/p&gt; | 
 **putObjectRequest** | [**PutObjectRequest**](PutObjectRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **contentType** | **String**| The content type of the object. | [optional] 
 **cacheControl** | **String**| &lt;p&gt;An optional &lt;code&gt;CacheControl&lt;/code&gt; header that allows the caller to control the object&#39;s cache behavior. Headers can be passed in as specified in the HTTP at &lt;a href&#x3D;\&quot;https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9\&quot;&gt;https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Headers with a custom user-defined value are also accepted.&lt;/p&gt; | [optional] 
 **xAmzStorageClass** | **String**| Indicates the storage class of a &lt;code&gt;Put&lt;/code&gt; request. Defaults to high-performance temporal storage class, and objects are persisted into durable storage shortly after being received. | [optional] 
 **xAmzUploadAvailability** | **String**| &lt;p&gt;Indicates the availability of an object while it is still uploading. If the value is set to &lt;code&gt;streaming&lt;/code&gt;, the object is available for downloading after some initial buffering but before the object is uploaded completely. If the value is set to &lt;code&gt;standard&lt;/code&gt;, the object is available for downloading only when it is uploaded completely. The default value for this header is &lt;code&gt;standard&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To use this header, you must also set the HTTP &lt;code&gt;Transfer-Encoding&lt;/code&gt; header to &lt;code&gt;chunked&lt;/code&gt;.&lt;/p&gt; | [optional] 

### Return type

[**PutObjectResponse**](PutObjectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

