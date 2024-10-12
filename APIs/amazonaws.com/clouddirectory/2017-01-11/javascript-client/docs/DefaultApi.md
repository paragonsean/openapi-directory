# AmazonCloudDirectory.DefaultApi

All URIs are relative to *http://clouddirectory.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addFacetToObject**](DefaultApi.md#addFacetToObject) | **PUT** /amazonclouddirectory/2017-01-11/object/facets#x-amz-data-partition | 
[**applySchema**](DefaultApi.md#applySchema) | **PUT** /amazonclouddirectory/2017-01-11/schema/apply#x-amz-data-partition | 
[**attachObject**](DefaultApi.md#attachObject) | **PUT** /amazonclouddirectory/2017-01-11/object/attach#x-amz-data-partition | 
[**attachPolicy**](DefaultApi.md#attachPolicy) | **PUT** /amazonclouddirectory/2017-01-11/policy/attach#x-amz-data-partition | 
[**attachToIndex**](DefaultApi.md#attachToIndex) | **PUT** /amazonclouddirectory/2017-01-11/index/attach#x-amz-data-partition | 
[**attachTypedLink**](DefaultApi.md#attachTypedLink) | **PUT** /amazonclouddirectory/2017-01-11/typedlink/attach#x-amz-data-partition | 
[**batchRead**](DefaultApi.md#batchRead) | **POST** /amazonclouddirectory/2017-01-11/batchread#x-amz-data-partition | 
[**batchWrite**](DefaultApi.md#batchWrite) | **PUT** /amazonclouddirectory/2017-01-11/batchwrite#x-amz-data-partition | 
[**createDirectory**](DefaultApi.md#createDirectory) | **PUT** /amazonclouddirectory/2017-01-11/directory/create#x-amz-data-partition | 
[**createFacet**](DefaultApi.md#createFacet) | **PUT** /amazonclouddirectory/2017-01-11/facet/create#x-amz-data-partition | 
[**createIndex**](DefaultApi.md#createIndex) | **PUT** /amazonclouddirectory/2017-01-11/index#x-amz-data-partition | 
[**createObject**](DefaultApi.md#createObject) | **PUT** /amazonclouddirectory/2017-01-11/object#x-amz-data-partition | 
[**createSchema**](DefaultApi.md#createSchema) | **PUT** /amazonclouddirectory/2017-01-11/schema/create | 
[**createTypedLinkFacet**](DefaultApi.md#createTypedLinkFacet) | **PUT** /amazonclouddirectory/2017-01-11/typedlink/facet/create#x-amz-data-partition | 
[**deleteDirectory**](DefaultApi.md#deleteDirectory) | **PUT** /amazonclouddirectory/2017-01-11/directory#x-amz-data-partition | 
[**deleteFacet**](DefaultApi.md#deleteFacet) | **PUT** /amazonclouddirectory/2017-01-11/facet/delete#x-amz-data-partition | 
[**deleteObject**](DefaultApi.md#deleteObject) | **PUT** /amazonclouddirectory/2017-01-11/object/delete#x-amz-data-partition | 
[**deleteSchema**](DefaultApi.md#deleteSchema) | **PUT** /amazonclouddirectory/2017-01-11/schema#x-amz-data-partition | 
[**deleteTypedLinkFacet**](DefaultApi.md#deleteTypedLinkFacet) | **PUT** /amazonclouddirectory/2017-01-11/typedlink/facet/delete#x-amz-data-partition | 
[**detachFromIndex**](DefaultApi.md#detachFromIndex) | **PUT** /amazonclouddirectory/2017-01-11/index/detach#x-amz-data-partition | 
[**detachObject**](DefaultApi.md#detachObject) | **PUT** /amazonclouddirectory/2017-01-11/object/detach#x-amz-data-partition | 
[**detachPolicy**](DefaultApi.md#detachPolicy) | **PUT** /amazonclouddirectory/2017-01-11/policy/detach#x-amz-data-partition | 
[**detachTypedLink**](DefaultApi.md#detachTypedLink) | **PUT** /amazonclouddirectory/2017-01-11/typedlink/detach#x-amz-data-partition | 
[**disableDirectory**](DefaultApi.md#disableDirectory) | **PUT** /amazonclouddirectory/2017-01-11/directory/disable#x-amz-data-partition | 
[**enableDirectory**](DefaultApi.md#enableDirectory) | **PUT** /amazonclouddirectory/2017-01-11/directory/enable#x-amz-data-partition | 
[**getAppliedSchemaVersion**](DefaultApi.md#getAppliedSchemaVersion) | **POST** /amazonclouddirectory/2017-01-11/schema/getappliedschema | 
[**getDirectory**](DefaultApi.md#getDirectory) | **POST** /amazonclouddirectory/2017-01-11/directory/get#x-amz-data-partition | 
[**getFacet**](DefaultApi.md#getFacet) | **POST** /amazonclouddirectory/2017-01-11/facet#x-amz-data-partition | 
[**getLinkAttributes**](DefaultApi.md#getLinkAttributes) | **POST** /amazonclouddirectory/2017-01-11/typedlink/attributes/get#x-amz-data-partition | 
[**getObjectAttributes**](DefaultApi.md#getObjectAttributes) | **POST** /amazonclouddirectory/2017-01-11/object/attributes/get#x-amz-data-partition | 
[**getObjectInformation**](DefaultApi.md#getObjectInformation) | **POST** /amazonclouddirectory/2017-01-11/object/information#x-amz-data-partition | 
[**getSchemaAsJson**](DefaultApi.md#getSchemaAsJson) | **POST** /amazonclouddirectory/2017-01-11/schema/json#x-amz-data-partition | 
[**getTypedLinkFacetInformation**](DefaultApi.md#getTypedLinkFacetInformation) | **POST** /amazonclouddirectory/2017-01-11/typedlink/facet/get#x-amz-data-partition | 
[**listAppliedSchemaArns**](DefaultApi.md#listAppliedSchemaArns) | **POST** /amazonclouddirectory/2017-01-11/schema/applied | 
[**listAttachedIndices**](DefaultApi.md#listAttachedIndices) | **POST** /amazonclouddirectory/2017-01-11/object/indices#x-amz-data-partition | 
[**listDevelopmentSchemaArns**](DefaultApi.md#listDevelopmentSchemaArns) | **POST** /amazonclouddirectory/2017-01-11/schema/development | 
[**listDirectories**](DefaultApi.md#listDirectories) | **POST** /amazonclouddirectory/2017-01-11/directory/list | 
[**listFacetAttributes**](DefaultApi.md#listFacetAttributes) | **POST** /amazonclouddirectory/2017-01-11/facet/attributes#x-amz-data-partition | 
[**listFacetNames**](DefaultApi.md#listFacetNames) | **POST** /amazonclouddirectory/2017-01-11/facet/list#x-amz-data-partition | 
[**listIncomingTypedLinks**](DefaultApi.md#listIncomingTypedLinks) | **POST** /amazonclouddirectory/2017-01-11/typedlink/incoming#x-amz-data-partition | 
[**listIndex**](DefaultApi.md#listIndex) | **POST** /amazonclouddirectory/2017-01-11/index/targets#x-amz-data-partition | 
[**listManagedSchemaArns**](DefaultApi.md#listManagedSchemaArns) | **POST** /amazonclouddirectory/2017-01-11/schema/managed | 
[**listObjectAttributes**](DefaultApi.md#listObjectAttributes) | **POST** /amazonclouddirectory/2017-01-11/object/attributes#x-amz-data-partition | 
[**listObjectChildren**](DefaultApi.md#listObjectChildren) | **POST** /amazonclouddirectory/2017-01-11/object/children#x-amz-data-partition | 
[**listObjectParentPaths**](DefaultApi.md#listObjectParentPaths) | **POST** /amazonclouddirectory/2017-01-11/object/parentpaths#x-amz-data-partition | 
[**listObjectParents**](DefaultApi.md#listObjectParents) | **POST** /amazonclouddirectory/2017-01-11/object/parent#x-amz-data-partition | 
[**listObjectPolicies**](DefaultApi.md#listObjectPolicies) | **POST** /amazonclouddirectory/2017-01-11/object/policy#x-amz-data-partition | 
[**listOutgoingTypedLinks**](DefaultApi.md#listOutgoingTypedLinks) | **POST** /amazonclouddirectory/2017-01-11/typedlink/outgoing#x-amz-data-partition | 
[**listPolicyAttachments**](DefaultApi.md#listPolicyAttachments) | **POST** /amazonclouddirectory/2017-01-11/policy/attachment#x-amz-data-partition | 
[**listPublishedSchemaArns**](DefaultApi.md#listPublishedSchemaArns) | **POST** /amazonclouddirectory/2017-01-11/schema/published | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /amazonclouddirectory/2017-01-11/tags | 
[**listTypedLinkFacetAttributes**](DefaultApi.md#listTypedLinkFacetAttributes) | **POST** /amazonclouddirectory/2017-01-11/typedlink/facet/attributes#x-amz-data-partition | 
[**listTypedLinkFacetNames**](DefaultApi.md#listTypedLinkFacetNames) | **POST** /amazonclouddirectory/2017-01-11/typedlink/facet/list#x-amz-data-partition | 
[**lookupPolicy**](DefaultApi.md#lookupPolicy) | **POST** /amazonclouddirectory/2017-01-11/policy/lookup#x-amz-data-partition | 
[**publishSchema**](DefaultApi.md#publishSchema) | **PUT** /amazonclouddirectory/2017-01-11/schema/publish#x-amz-data-partition | 
[**putSchemaFromJson**](DefaultApi.md#putSchemaFromJson) | **PUT** /amazonclouddirectory/2017-01-11/schema/json#x-amz-data-partition | 
[**removeFacetFromObject**](DefaultApi.md#removeFacetFromObject) | **PUT** /amazonclouddirectory/2017-01-11/object/facets/delete#x-amz-data-partition | 
[**tagResource**](DefaultApi.md#tagResource) | **PUT** /amazonclouddirectory/2017-01-11/tags/add | 
[**untagResource**](DefaultApi.md#untagResource) | **PUT** /amazonclouddirectory/2017-01-11/tags/remove | 
[**updateFacet**](DefaultApi.md#updateFacet) | **PUT** /amazonclouddirectory/2017-01-11/facet#x-amz-data-partition | 
[**updateLinkAttributes**](DefaultApi.md#updateLinkAttributes) | **POST** /amazonclouddirectory/2017-01-11/typedlink/attributes/update#x-amz-data-partition | 
[**updateObjectAttributes**](DefaultApi.md#updateObjectAttributes) | **PUT** /amazonclouddirectory/2017-01-11/object/update#x-amz-data-partition | 
[**updateSchema**](DefaultApi.md#updateSchema) | **PUT** /amazonclouddirectory/2017-01-11/schema/update#x-amz-data-partition | 
[**updateTypedLinkFacet**](DefaultApi.md#updateTypedLinkFacet) | **PUT** /amazonclouddirectory/2017-01-11/typedlink/facet#x-amz-data-partition | 
[**upgradeAppliedSchema**](DefaultApi.md#upgradeAppliedSchema) | **PUT** /amazonclouddirectory/2017-01-11/schema/upgradeapplied | 
[**upgradePublishedSchema**](DefaultApi.md#upgradePublishedSchema) | **PUT** /amazonclouddirectory/2017-01-11/schema/upgradepublished | 



## addFacetToObject

> Object addFacetToObject(xAmzDataPartition, addFacetToObjectRequest, opts)



Adds a new &lt;a&gt;Facet&lt;/a&gt; to an object. An object can have more than one facet applied on it.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.
let addFacetToObjectRequest = new AmazonCloudDirectory.AddFacetToObjectRequest(); // AddFacetToObjectRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.addFacetToObject(xAmzDataPartition, addFacetToObjectRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where the object resides. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **addFacetToObjectRequest** | [**AddFacetToObjectRequest**](AddFacetToObjectRequest.md)|  | 
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

- **Content-Type**: application/json
- **Accept**: application/json


## applySchema

> ApplySchemaResponse applySchema(xAmzDataPartition, applySchemaRequest, opts)



Copies the input published schema, at the specified version, into the &lt;a&gt;Directory&lt;/a&gt; with the same name and version as that of the published schema.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> into which the schema is copied. For more information, see <a>arns</a>.
let applySchemaRequest = new AmazonCloudDirectory.ApplySchemaRequest(); // ApplySchemaRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.applySchema(xAmzDataPartition, applySchemaRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; into which the schema is copied. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **applySchemaRequest** | [**ApplySchemaRequest**](ApplySchemaRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ApplySchemaResponse**](ApplySchemaResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## attachObject

> AttachObjectResponse attachObject(xAmzDataPartition, attachObjectRequest, opts)



&lt;p&gt;Attaches an existing object to another object. An object can be accessed in two ways:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Using the path&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Using &lt;code&gt;ObjectIdentifier&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where both objects reside. For more information, see <a>arns</a>.
let attachObjectRequest = new AmazonCloudDirectory.AttachObjectRequest(); // AttachObjectRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.attachObject(xAmzDataPartition, attachObjectRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where both objects reside. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **attachObjectRequest** | [**AttachObjectRequest**](AttachObjectRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AttachObjectResponse**](AttachObjectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## attachPolicy

> Object attachPolicy(xAmzDataPartition, attachPolicyRequest, opts)



Attaches a policy object to a regular object. An object can have a limited number of attached policies.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where both objects reside. For more information, see <a>arns</a>.
let attachPolicyRequest = new AmazonCloudDirectory.AttachPolicyRequest(); // AttachPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.attachPolicy(xAmzDataPartition, attachPolicyRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where both objects reside. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **attachPolicyRequest** | [**AttachPolicyRequest**](AttachPolicyRequest.md)|  | 
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

- **Content-Type**: application/json
- **Accept**: application/json


## attachToIndex

> AttachToIndexResponse attachToIndex(xAmzDataPartition, attachToIndexRequest, opts)



Attaches the specified object to the specified index.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) of the directory where the object and index exist.
let attachToIndexRequest = new AmazonCloudDirectory.AttachToIndexRequest(); // AttachToIndexRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.attachToIndex(xAmzDataPartition, attachToIndexRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) of the directory where the object and index exist. | 
 **attachToIndexRequest** | [**AttachToIndexRequest**](AttachToIndexRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AttachToIndexResponse**](AttachToIndexResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## attachTypedLink

> AttachTypedLinkResponse attachTypedLink(xAmzDataPartition, attachTypedLinkRequest, opts)



Attaches a typed link to a specified source and target object. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\&quot;&gt;Typed Links&lt;/a&gt;.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) of the directory where you want to attach the typed link.
let attachTypedLinkRequest = new AmazonCloudDirectory.AttachTypedLinkRequest(); // AttachTypedLinkRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.attachTypedLink(xAmzDataPartition, attachTypedLinkRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) of the directory where you want to attach the typed link. | 
 **attachTypedLinkRequest** | [**AttachTypedLinkRequest**](AttachTypedLinkRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AttachTypedLinkResponse**](AttachTypedLinkResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchRead

> BatchReadResponse batchRead(xAmzDataPartition, batchReadRequest, opts)



Performs all the read operations in a batch. 

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a>. For more information, see <a>arns</a>.
let batchReadRequest = new AmazonCloudDirectory.BatchReadRequest(); // BatchReadRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzConsistencyLevel': "xAmzConsistencyLevel_example" // String | Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
};
apiInstance.batchRead(xAmzDataPartition, batchReadRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt;. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **batchReadRequest** | [**BatchReadRequest**](BatchReadRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzConsistencyLevel** | **String**| Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object. | [optional] 

### Return type

[**BatchReadResponse**](BatchReadResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchWrite

> BatchWriteResponse batchWrite(xAmzDataPartition, batchWriteRequest, opts)



Performs all the write operations in a batch. Either all the operations succeed or none.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a>. For more information, see <a>arns</a>.
let batchWriteRequest = new AmazonCloudDirectory.BatchWriteRequest(); // BatchWriteRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchWrite(xAmzDataPartition, batchWriteRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt;. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **batchWriteRequest** | [**BatchWriteRequest**](BatchWriteRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchWriteResponse**](BatchWriteResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDirectory

> CreateDirectoryResponse createDirectory(xAmzDataPartition, createDirectoryRequest, opts)



&lt;p&gt;Creates a &lt;a&gt;Directory&lt;/a&gt; by copying the published schema into the directory. A directory cannot be created without a schema.&lt;/p&gt; &lt;p&gt;You can also quickly create a directory using a managed schema, called the &lt;code&gt;QuickStartSchema&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_managed.html\&quot;&gt;Managed Schema&lt;/a&gt; in the &lt;i&gt;Amazon Cloud Directory Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) of the published schema that will be copied into the data <a>Directory</a>. For more information, see <a>arns</a>.
let createDirectoryRequest = new AmazonCloudDirectory.CreateDirectoryRequest(); // CreateDirectoryRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDirectory(xAmzDataPartition, createDirectoryRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) of the published schema that will be copied into the data &lt;a&gt;Directory&lt;/a&gt;. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **createDirectoryRequest** | [**CreateDirectoryRequest**](CreateDirectoryRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateDirectoryResponse**](CreateDirectoryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createFacet

> Object createFacet(xAmzDataPartition, createFacetRequest, opts)



Creates a new &lt;a&gt;Facet&lt;/a&gt; in a schema. Facet creation is allowed only in development or applied schemas.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The schema ARN in which the new <a>Facet</a> will be created. For more information, see <a>arns</a>.
let createFacetRequest = new AmazonCloudDirectory.CreateFacetRequest(); // CreateFacetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createFacet(xAmzDataPartition, createFacetRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The schema ARN in which the new &lt;a&gt;Facet&lt;/a&gt; will be created. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **createFacetRequest** | [**CreateFacetRequest**](CreateFacetRequest.md)|  | 
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

- **Content-Type**: application/json
- **Accept**: application/json


## createIndex

> CreateIndexResponse createIndex(xAmzDataPartition, createIndexRequest, opts)



Creates an index object. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clouddirectory/latest/developerguide/indexing_search.html\&quot;&gt;Indexing and search&lt;/a&gt; for more information.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the directory where the index should be created.
let createIndexRequest = new AmazonCloudDirectory.CreateIndexRequest(); // CreateIndexRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createIndex(xAmzDataPartition, createIndexRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The ARN of the directory where the index should be created. | 
 **createIndexRequest** | [**CreateIndexRequest**](CreateIndexRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateIndexResponse**](CreateIndexResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createObject

> CreateObjectResponse createObject(xAmzDataPartition, createObjectRequest, opts)



Creates an object in a &lt;a&gt;Directory&lt;/a&gt;. Additionally attaches the object to a parent, if a parent reference and &lt;code&gt;LinkName&lt;/code&gt; is specified. An object is simply a collection of &lt;a&gt;Facet&lt;/a&gt; attributes. You can also use this API call to create a policy object, if the facet from which you create the object is a policy facet. 

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> in which the object will be created. For more information, see <a>arns</a>.
let createObjectRequest = new AmazonCloudDirectory.CreateObjectRequest(); // CreateObjectRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createObject(xAmzDataPartition, createObjectRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; in which the object will be created. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **createObjectRequest** | [**CreateObjectRequest**](CreateObjectRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateObjectResponse**](CreateObjectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSchema

> CreateSchemaResponse createSchema(createSchemaRequest, opts)



&lt;p&gt;Creates a new schema in a development state. A schema can exist in three phases:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Development:&lt;/i&gt; This is a mutable phase of the schema. All new schemas are in the development phase. Once the schema is finalized, it can be published.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Published:&lt;/i&gt; Published schemas are immutable and have a version associated with them.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Applied:&lt;/i&gt; Applied schemas are mutable in a way that allows you to add new schema facets. You can also add new, nonrequired attributes to existing schema facets. You can apply only published schemas to directories. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let createSchemaRequest = new AmazonCloudDirectory.CreateSchemaRequest(); // CreateSchemaRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSchema(createSchemaRequest, opts, (error, data, response) => {
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
 **createSchemaRequest** | [**CreateSchemaRequest**](CreateSchemaRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSchemaResponse**](CreateSchemaResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTypedLinkFacet

> Object createTypedLinkFacet(xAmzDataPartition, createTypedLinkFacetRequest, opts)



Creates a &lt;a&gt;TypedLinkFacet&lt;/a&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\&quot;&gt;Typed Links&lt;/a&gt;.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.
let createTypedLinkFacetRequest = new AmazonCloudDirectory.CreateTypedLinkFacetRequest(); // CreateTypedLinkFacetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createTypedLinkFacet(xAmzDataPartition, createTypedLinkFacetRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the schema. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **createTypedLinkFacetRequest** | [**CreateTypedLinkFacetRequest**](CreateTypedLinkFacetRequest.md)|  | 
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

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDirectory

> DeleteDirectoryResponse deleteDirectory(xAmzDataPartition, opts)



Deletes a directory. Only disabled directories can be deleted. A deleted directory cannot be undone. Exercise extreme caution when deleting directories.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the directory to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteDirectory(xAmzDataPartition, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The ARN of the directory to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteDirectoryResponse**](DeleteDirectoryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteFacet

> Object deleteFacet(xAmzDataPartition, deleteFacetRequest, opts)



Deletes a given &lt;a&gt;Facet&lt;/a&gt;. All attributes and &lt;a&gt;Rule&lt;/a&gt;s that are associated with the facet will be deleted. Only development schema facets are allowed deletion.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Facet</a>. For more information, see <a>arns</a>.
let deleteFacetRequest = new AmazonCloudDirectory.DeleteFacetRequest(); // DeleteFacetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteFacet(xAmzDataPartition, deleteFacetRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Facet&lt;/a&gt;. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **deleteFacetRequest** | [**DeleteFacetRequest**](DeleteFacetRequest.md)|  | 
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

- **Content-Type**: application/json
- **Accept**: application/json


## deleteObject

> Object deleteObject(xAmzDataPartition, deleteObjectRequest, opts)



Deletes an object and its associated attributes. Only objects with no children and no parents can be deleted. The maximum number of attributes that can be deleted during an object deletion is 30. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clouddirectory/latest/developerguide/limits.html\&quot;&gt;Amazon Cloud Directory Limits&lt;/a&gt;.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.
let deleteObjectRequest = new AmazonCloudDirectory.DeleteObjectRequest(); // DeleteObjectRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteObject(xAmzDataPartition, deleteObjectRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where the object resides. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **deleteObjectRequest** | [**DeleteObjectRequest**](DeleteObjectRequest.md)|  | 
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

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSchema

> DeleteSchemaResponse deleteSchema(xAmzDataPartition, opts)



Deletes a given schema. Schemas in a development and published state can only be deleted. 

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) of the development schema. For more information, see <a>arns</a>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSchema(xAmzDataPartition, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) of the development schema. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteSchemaResponse**](DeleteSchemaResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTypedLinkFacet

> Object deleteTypedLinkFacet(xAmzDataPartition, deleteTypedLinkFacetRequest, opts)



Deletes a &lt;a&gt;TypedLinkFacet&lt;/a&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\&quot;&gt;Typed Links&lt;/a&gt;.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.
let deleteTypedLinkFacetRequest = new AmazonCloudDirectory.DeleteTypedLinkFacetRequest(); // DeleteTypedLinkFacetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteTypedLinkFacet(xAmzDataPartition, deleteTypedLinkFacetRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the schema. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **deleteTypedLinkFacetRequest** | [**DeleteTypedLinkFacetRequest**](DeleteTypedLinkFacetRequest.md)|  | 
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

- **Content-Type**: application/json
- **Accept**: application/json


## detachFromIndex

> DetachFromIndexResponse detachFromIndex(xAmzDataPartition, attachToIndexRequest, opts)



Detaches the specified object from the specified index.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) of the directory the index and object exist in.
let attachToIndexRequest = new AmazonCloudDirectory.AttachToIndexRequest(); // AttachToIndexRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.detachFromIndex(xAmzDataPartition, attachToIndexRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) of the directory the index and object exist in. | 
 **attachToIndexRequest** | [**AttachToIndexRequest**](AttachToIndexRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DetachFromIndexResponse**](DetachFromIndexResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## detachObject

> DetachObjectResponse detachObject(xAmzDataPartition, detachObjectRequest, opts)



Detaches a given object from the parent object. The object that is to be detached from the parent is specified by the link name.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where objects reside. For more information, see <a>arns</a>.
let detachObjectRequest = new AmazonCloudDirectory.DetachObjectRequest(); // DetachObjectRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.detachObject(xAmzDataPartition, detachObjectRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where objects reside. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **detachObjectRequest** | [**DetachObjectRequest**](DetachObjectRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DetachObjectResponse**](DetachObjectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## detachPolicy

> Object detachPolicy(xAmzDataPartition, attachPolicyRequest, opts)



Detaches a policy from an object.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where both objects reside. For more information, see <a>arns</a>.
let attachPolicyRequest = new AmazonCloudDirectory.AttachPolicyRequest(); // AttachPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.detachPolicy(xAmzDataPartition, attachPolicyRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where both objects reside. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **attachPolicyRequest** | [**AttachPolicyRequest**](AttachPolicyRequest.md)|  | 
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

- **Content-Type**: application/json
- **Accept**: application/json


## detachTypedLink

> detachTypedLink(xAmzDataPartition, detachTypedLinkRequest, opts)



Detaches a typed link from a specified source and target object. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\&quot;&gt;Typed Links&lt;/a&gt;.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) of the directory where you want to detach the typed link.
let detachTypedLinkRequest = new AmazonCloudDirectory.DetachTypedLinkRequest(); // DetachTypedLinkRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.detachTypedLink(xAmzDataPartition, detachTypedLinkRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) of the directory where you want to detach the typed link. | 
 **detachTypedLinkRequest** | [**DetachTypedLinkRequest**](DetachTypedLinkRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disableDirectory

> DisableDirectoryResponse disableDirectory(xAmzDataPartition, opts)



Disables the specified directory. Disabled directories cannot be read or written to. Only enabled directories can be disabled. Disabled directories may be reenabled.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the directory to disable.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disableDirectory(xAmzDataPartition, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The ARN of the directory to disable. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DisableDirectoryResponse**](DisableDirectoryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enableDirectory

> EnableDirectoryResponse enableDirectory(xAmzDataPartition, opts)



Enables the specified directory. Only disabled directories can be enabled. Once enabled, the directory can then be read and written to.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the directory to enable.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.enableDirectory(xAmzDataPartition, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The ARN of the directory to enable. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**EnableDirectoryResponse**](EnableDirectoryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAppliedSchemaVersion

> GetAppliedSchemaVersionResponse getAppliedSchemaVersion(getAppliedSchemaVersionRequest, opts)



Returns current applied schema version ARN, including the minor version in use.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let getAppliedSchemaVersionRequest = new AmazonCloudDirectory.GetAppliedSchemaVersionRequest(); // GetAppliedSchemaVersionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAppliedSchemaVersion(getAppliedSchemaVersionRequest, opts, (error, data, response) => {
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
 **getAppliedSchemaVersionRequest** | [**GetAppliedSchemaVersionRequest**](GetAppliedSchemaVersionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAppliedSchemaVersionResponse**](GetAppliedSchemaVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getDirectory

> GetDirectoryResponse getDirectory(xAmzDataPartition, opts)



Retrieves metadata about a directory.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the directory.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDirectory(xAmzDataPartition, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The ARN of the directory. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDirectoryResponse**](GetDirectoryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFacet

> GetFacetResponse getFacet(xAmzDataPartition, getFacetRequest, opts)



Gets details of the &lt;a&gt;Facet&lt;/a&gt;, such as facet name, attributes, &lt;a&gt;Rule&lt;/a&gt;s, or &lt;code&gt;ObjectType&lt;/code&gt;. You can call this on all kinds of schema facets -- published, development, or applied.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Facet</a>. For more information, see <a>arns</a>.
let getFacetRequest = new AmazonCloudDirectory.GetFacetRequest(); // GetFacetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getFacet(xAmzDataPartition, getFacetRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Facet&lt;/a&gt;. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **getFacetRequest** | [**GetFacetRequest**](GetFacetRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetFacetResponse**](GetFacetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getLinkAttributes

> GetLinkAttributesResponse getLinkAttributes(xAmzDataPartition, getLinkAttributesRequest, opts)



Retrieves attributes that are associated with a typed link.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the Directory where the typed link resides. For more information, see <a>arns</a> or <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\">Typed Links</a>.
let getLinkAttributesRequest = new AmazonCloudDirectory.GetLinkAttributesRequest(); // GetLinkAttributesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getLinkAttributes(xAmzDataPartition, getLinkAttributesRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the Directory where the typed link resides. For more information, see &lt;a&gt;arns&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\&quot;&gt;Typed Links&lt;/a&gt;. | 
 **getLinkAttributesRequest** | [**GetLinkAttributesRequest**](GetLinkAttributesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetLinkAttributesResponse**](GetLinkAttributesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getObjectAttributes

> GetObjectAttributesResponse getObjectAttributes(xAmzDataPartition, getObjectAttributesRequest, opts)



Retrieves attributes within a facet that are associated with an object.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides.
let getObjectAttributesRequest = new AmazonCloudDirectory.GetObjectAttributesRequest(); // GetObjectAttributesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzConsistencyLevel': "xAmzConsistencyLevel_example" // String | The consistency level at which to retrieve the attributes on an object.
};
apiInstance.getObjectAttributes(xAmzDataPartition, getObjectAttributesRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where the object resides. | 
 **getObjectAttributesRequest** | [**GetObjectAttributesRequest**](GetObjectAttributesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzConsistencyLevel** | **String**| The consistency level at which to retrieve the attributes on an object. | [optional] 

### Return type

[**GetObjectAttributesResponse**](GetObjectAttributesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getObjectInformation

> GetObjectInformationResponse getObjectInformation(xAmzDataPartition, deleteObjectRequest, opts)



Retrieves metadata about an object.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the directory being retrieved.
let deleteObjectRequest = new AmazonCloudDirectory.DeleteObjectRequest(); // DeleteObjectRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzConsistencyLevel': "xAmzConsistencyLevel_example" // String | The consistency level at which to retrieve the object information.
};
apiInstance.getObjectInformation(xAmzDataPartition, deleteObjectRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The ARN of the directory being retrieved. | 
 **deleteObjectRequest** | [**DeleteObjectRequest**](DeleteObjectRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzConsistencyLevel** | **String**| The consistency level at which to retrieve the object information. | [optional] 

### Return type

[**GetObjectInformationResponse**](GetObjectInformationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSchemaAsJson

> GetSchemaAsJsonResponse getSchemaAsJson(xAmzDataPartition, opts)



Retrieves a JSON representation of the schema. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_jsonformat.html#schemas_json\&quot;&gt;JSON Schema Format&lt;/a&gt; for more information.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the schema to retrieve.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSchemaAsJson(xAmzDataPartition, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The ARN of the schema to retrieve. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSchemaAsJsonResponse**](GetSchemaAsJsonResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTypedLinkFacetInformation

> GetTypedLinkFacetInformationResponse getTypedLinkFacetInformation(xAmzDataPartition, deleteTypedLinkFacetRequest, opts)



Returns the identity attribute order for a specific &lt;a&gt;TypedLinkFacet&lt;/a&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\&quot;&gt;Typed Links&lt;/a&gt;.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.
let deleteTypedLinkFacetRequest = new AmazonCloudDirectory.DeleteTypedLinkFacetRequest(); // DeleteTypedLinkFacetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getTypedLinkFacetInformation(xAmzDataPartition, deleteTypedLinkFacetRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the schema. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **deleteTypedLinkFacetRequest** | [**DeleteTypedLinkFacetRequest**](DeleteTypedLinkFacetRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetTypedLinkFacetInformationResponse**](GetTypedLinkFacetInformationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAppliedSchemaArns

> ListAppliedSchemaArnsResponse listAppliedSchemaArns(listAppliedSchemaArnsRequest, opts)



Lists schema major versions applied to a directory. If &lt;code&gt;SchemaArn&lt;/code&gt; is provided, lists the minor version.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let listAppliedSchemaArnsRequest = new AmazonCloudDirectory.ListAppliedSchemaArnsRequest(); // ListAppliedSchemaArnsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listAppliedSchemaArns(listAppliedSchemaArnsRequest, opts, (error, data, response) => {
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
 **listAppliedSchemaArnsRequest** | [**ListAppliedSchemaArnsRequest**](ListAppliedSchemaArnsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListAppliedSchemaArnsResponse**](ListAppliedSchemaArnsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAttachedIndices

> ListAttachedIndicesResponse listAttachedIndices(xAmzDataPartition, listAttachedIndicesRequest, opts)



Lists indices attached to the specified object.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the directory.
let listAttachedIndicesRequest = new AmazonCloudDirectory.ListAttachedIndicesRequest(); // ListAttachedIndicesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzConsistencyLevel': "xAmzConsistencyLevel_example", // String | The consistency level to use for this operation.
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listAttachedIndices(xAmzDataPartition, listAttachedIndicesRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The ARN of the directory. | 
 **listAttachedIndicesRequest** | [**ListAttachedIndicesRequest**](ListAttachedIndicesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzConsistencyLevel** | **String**| The consistency level to use for this operation. | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListAttachedIndicesResponse**](ListAttachedIndicesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listDevelopmentSchemaArns

> ListDevelopmentSchemaArnsResponse listDevelopmentSchemaArns(listDevelopmentSchemaArnsRequest, opts)



Retrieves each Amazon Resource Name (ARN) of schemas in the development state.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let listDevelopmentSchemaArnsRequest = new AmazonCloudDirectory.ListDevelopmentSchemaArnsRequest(); // ListDevelopmentSchemaArnsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listDevelopmentSchemaArns(listDevelopmentSchemaArnsRequest, opts, (error, data, response) => {
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
 **listDevelopmentSchemaArnsRequest** | [**ListDevelopmentSchemaArnsRequest**](ListDevelopmentSchemaArnsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListDevelopmentSchemaArnsResponse**](ListDevelopmentSchemaArnsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listDirectories

> ListDirectoriesResponse listDirectories(listDirectoriesRequest, opts)



Lists directories created within an account.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let listDirectoriesRequest = new AmazonCloudDirectory.ListDirectoriesRequest(); // ListDirectoriesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listDirectories(listDirectoriesRequest, opts, (error, data, response) => {
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
 **listDirectoriesRequest** | [**ListDirectoriesRequest**](ListDirectoriesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListDirectoriesResponse**](ListDirectoriesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listFacetAttributes

> ListFacetAttributesResponse listFacetAttributes(xAmzDataPartition, listFacetAttributesRequest, opts)



Retrieves attributes attached to the facet.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the schema where the facet resides.
let listFacetAttributesRequest = new AmazonCloudDirectory.ListFacetAttributesRequest(); // ListFacetAttributesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listFacetAttributes(xAmzDataPartition, listFacetAttributesRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The ARN of the schema where the facet resides. | 
 **listFacetAttributesRequest** | [**ListFacetAttributesRequest**](ListFacetAttributesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListFacetAttributesResponse**](ListFacetAttributesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listFacetNames

> ListFacetNamesResponse listFacetNames(xAmzDataPartition, listDevelopmentSchemaArnsRequest, opts)



Retrieves the names of facets that exist in a schema.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) to retrieve facet names from.
let listDevelopmentSchemaArnsRequest = new AmazonCloudDirectory.ListDevelopmentSchemaArnsRequest(); // ListDevelopmentSchemaArnsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listFacetNames(xAmzDataPartition, listDevelopmentSchemaArnsRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) to retrieve facet names from. | 
 **listDevelopmentSchemaArnsRequest** | [**ListDevelopmentSchemaArnsRequest**](ListDevelopmentSchemaArnsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListFacetNamesResponse**](ListFacetNamesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listIncomingTypedLinks

> ListIncomingTypedLinksResponse listIncomingTypedLinks(xAmzDataPartition, listIncomingTypedLinksRequest, opts)



Returns a paginated list of all the incoming &lt;a&gt;TypedLinkSpecifier&lt;/a&gt; information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\&quot;&gt;Typed Links&lt;/a&gt;.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) of the directory where you want to list the typed links.
let listIncomingTypedLinksRequest = new AmazonCloudDirectory.ListIncomingTypedLinksRequest(); // ListIncomingTypedLinksRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listIncomingTypedLinks(xAmzDataPartition, listIncomingTypedLinksRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) of the directory where you want to list the typed links. | 
 **listIncomingTypedLinksRequest** | [**ListIncomingTypedLinksRequest**](ListIncomingTypedLinksRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListIncomingTypedLinksResponse**](ListIncomingTypedLinksResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listIndex

> ListIndexResponse listIndex(xAmzDataPartition, listIndexRequest, opts)



Lists objects attached to the specified index.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the directory that the index exists in.
let listIndexRequest = new AmazonCloudDirectory.ListIndexRequest(); // ListIndexRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzConsistencyLevel': "xAmzConsistencyLevel_example", // String | The consistency level to execute the request at.
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listIndex(xAmzDataPartition, listIndexRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The ARN of the directory that the index exists in. | 
 **listIndexRequest** | [**ListIndexRequest**](ListIndexRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzConsistencyLevel** | **String**| The consistency level to execute the request at. | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListIndexResponse**](ListIndexResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listManagedSchemaArns

> ListManagedSchemaArnsResponse listManagedSchemaArns(listManagedSchemaArnsRequest, opts)



Lists the major version families of each managed schema. If a major version ARN is provided as SchemaArn, the minor version revisions in that family are listed instead.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let listManagedSchemaArnsRequest = new AmazonCloudDirectory.ListManagedSchemaArnsRequest(); // ListManagedSchemaArnsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listManagedSchemaArns(listManagedSchemaArnsRequest, opts, (error, data, response) => {
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
 **listManagedSchemaArnsRequest** | [**ListManagedSchemaArnsRequest**](ListManagedSchemaArnsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListManagedSchemaArnsResponse**](ListManagedSchemaArnsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listObjectAttributes

> ListObjectAttributesResponse listObjectAttributes(xAmzDataPartition, listObjectAttributesRequest, opts)



Lists all attributes that are associated with an object. 

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.
let listObjectAttributesRequest = new AmazonCloudDirectory.ListObjectAttributesRequest(); // ListObjectAttributesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzConsistencyLevel': "xAmzConsistencyLevel_example", // String | Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listObjectAttributes(xAmzDataPartition, listObjectAttributesRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where the object resides. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **listObjectAttributesRequest** | [**ListObjectAttributesRequest**](ListObjectAttributesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzConsistencyLevel** | **String**| Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object. | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListObjectAttributesResponse**](ListObjectAttributesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listObjectChildren

> ListObjectChildrenResponse listObjectChildren(xAmzDataPartition, listObjectChildrenRequest, opts)



Returns a paginated list of child objects that are associated with a given object.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.
let listObjectChildrenRequest = new AmazonCloudDirectory.ListObjectChildrenRequest(); // ListObjectChildrenRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzConsistencyLevel': "xAmzConsistencyLevel_example", // String | Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listObjectChildren(xAmzDataPartition, listObjectChildrenRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where the object resides. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **listObjectChildrenRequest** | [**ListObjectChildrenRequest**](ListObjectChildrenRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzConsistencyLevel** | **String**| Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object. | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListObjectChildrenResponse**](ListObjectChildrenResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listObjectParentPaths

> ListObjectParentPathsResponse listObjectParentPaths(xAmzDataPartition, listObjectChildrenRequest, opts)



&lt;p&gt;Retrieves all available parent paths for any object type such as node, leaf node, policy node, and index node objects. For more information about objects, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directorystructure.html\&quot;&gt;Directory Structure&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Use this API to evaluate all parents for an object. The call returns all objects from the root of the directory up to the requested object. The API returns the number of paths based on user-defined &lt;code&gt;MaxResults&lt;/code&gt;, in case there are multiple paths to the parent. The order of the paths and nodes returned is consistent among multiple API calls unless the objects are deleted or moved. Paths not leading to the directory root are ignored from the target object.&lt;/p&gt;

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the directory to which the parent path applies.
let listObjectChildrenRequest = new AmazonCloudDirectory.ListObjectChildrenRequest(); // ListObjectChildrenRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listObjectParentPaths(xAmzDataPartition, listObjectChildrenRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The ARN of the directory to which the parent path applies. | 
 **listObjectChildrenRequest** | [**ListObjectChildrenRequest**](ListObjectChildrenRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListObjectParentPathsResponse**](ListObjectParentPathsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listObjectParents

> ListObjectParentsResponse listObjectParents(xAmzDataPartition, listObjectParentsRequest, opts)



Lists parent objects that are associated with a given object in pagination fashion.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.
let listObjectParentsRequest = new AmazonCloudDirectory.ListObjectParentsRequest(); // ListObjectParentsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzConsistencyLevel': "xAmzConsistencyLevel_example", // String | Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listObjectParents(xAmzDataPartition, listObjectParentsRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where the object resides. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **listObjectParentsRequest** | [**ListObjectParentsRequest**](ListObjectParentsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzConsistencyLevel** | **String**| Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object. | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListObjectParentsResponse**](ListObjectParentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listObjectPolicies

> ListObjectPoliciesResponse listObjectPolicies(xAmzDataPartition, listObjectChildrenRequest, opts)



Returns policies attached to an object in pagination fashion.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where objects reside. For more information, see <a>arns</a>.
let listObjectChildrenRequest = new AmazonCloudDirectory.ListObjectChildrenRequest(); // ListObjectChildrenRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzConsistencyLevel': "xAmzConsistencyLevel_example", // String | Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listObjectPolicies(xAmzDataPartition, listObjectChildrenRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where objects reside. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **listObjectChildrenRequest** | [**ListObjectChildrenRequest**](ListObjectChildrenRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzConsistencyLevel** | **String**| Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object. | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListObjectPoliciesResponse**](ListObjectPoliciesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listOutgoingTypedLinks

> ListOutgoingTypedLinksResponse listOutgoingTypedLinks(xAmzDataPartition, listIncomingTypedLinksRequest, opts)



Returns a paginated list of all the outgoing &lt;a&gt;TypedLinkSpecifier&lt;/a&gt; information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\&quot;&gt;Typed Links&lt;/a&gt;.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) of the directory where you want to list the typed links.
let listIncomingTypedLinksRequest = new AmazonCloudDirectory.ListIncomingTypedLinksRequest(); // ListIncomingTypedLinksRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listOutgoingTypedLinks(xAmzDataPartition, listIncomingTypedLinksRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) of the directory where you want to list the typed links. | 
 **listIncomingTypedLinksRequest** | [**ListIncomingTypedLinksRequest**](ListIncomingTypedLinksRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListOutgoingTypedLinksResponse**](ListOutgoingTypedLinksResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPolicyAttachments

> ListPolicyAttachmentsResponse listPolicyAttachments(xAmzDataPartition, listPolicyAttachmentsRequest, opts)



Returns all of the &lt;code&gt;ObjectIdentifiers&lt;/code&gt; to which a given policy is attached.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where objects reside. For more information, see <a>arns</a>.
let listPolicyAttachmentsRequest = new AmazonCloudDirectory.ListPolicyAttachmentsRequest(); // ListPolicyAttachmentsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzConsistencyLevel': "xAmzConsistencyLevel_example", // String | Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listPolicyAttachments(xAmzDataPartition, listPolicyAttachmentsRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where objects reside. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **listPolicyAttachmentsRequest** | [**ListPolicyAttachmentsRequest**](ListPolicyAttachmentsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzConsistencyLevel** | **String**| Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object. | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListPolicyAttachmentsResponse**](ListPolicyAttachmentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPublishedSchemaArns

> ListPublishedSchemaArnsResponse listPublishedSchemaArns(listPublishedSchemaArnsRequest, opts)



Lists the major version families of each published schema. If a major version ARN is provided as &lt;code&gt;SchemaArn&lt;/code&gt;, the minor version revisions in that family are listed instead.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let listPublishedSchemaArnsRequest = new AmazonCloudDirectory.ListPublishedSchemaArnsRequest(); // ListPublishedSchemaArnsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listPublishedSchemaArns(listPublishedSchemaArnsRequest, opts, (error, data, response) => {
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
 **listPublishedSchemaArnsRequest** | [**ListPublishedSchemaArnsRequest**](ListPublishedSchemaArnsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListPublishedSchemaArnsResponse**](ListPublishedSchemaArnsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(listTagsForResourceRequest, opts)



Returns tags for a resource. Tagging is currently supported only for directories with a limit of 50 tags per directory. All 50 tags are returned for a given directory with this API call.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let listTagsForResourceRequest = new AmazonCloudDirectory.ListTagsForResourceRequest(); // ListTagsForResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listTagsForResource(listTagsForResourceRequest, opts, (error, data, response) => {
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
 **listTagsForResourceRequest** | [**ListTagsForResourceRequest**](ListTagsForResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTypedLinkFacetAttributes

> ListTypedLinkFacetAttributesResponse listTypedLinkFacetAttributes(xAmzDataPartition, listTypedLinkFacetAttributesRequest, opts)



Returns a paginated list of all attribute definitions for a particular &lt;a&gt;TypedLinkFacet&lt;/a&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\&quot;&gt;Typed Links&lt;/a&gt;.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.
let listTypedLinkFacetAttributesRequest = new AmazonCloudDirectory.ListTypedLinkFacetAttributesRequest(); // ListTypedLinkFacetAttributesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listTypedLinkFacetAttributes(xAmzDataPartition, listTypedLinkFacetAttributesRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the schema. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **listTypedLinkFacetAttributesRequest** | [**ListTypedLinkFacetAttributesRequest**](ListTypedLinkFacetAttributesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListTypedLinkFacetAttributesResponse**](ListTypedLinkFacetAttributesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTypedLinkFacetNames

> ListTypedLinkFacetNamesResponse listTypedLinkFacetNames(xAmzDataPartition, listDevelopmentSchemaArnsRequest, opts)



Returns a paginated list of &lt;code&gt;TypedLink&lt;/code&gt; facet names for a particular schema. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\&quot;&gt;Typed Links&lt;/a&gt;.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.
let listDevelopmentSchemaArnsRequest = new AmazonCloudDirectory.ListDevelopmentSchemaArnsRequest(); // ListDevelopmentSchemaArnsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listTypedLinkFacetNames(xAmzDataPartition, listDevelopmentSchemaArnsRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the schema. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **listDevelopmentSchemaArnsRequest** | [**ListDevelopmentSchemaArnsRequest**](ListDevelopmentSchemaArnsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListTypedLinkFacetNamesResponse**](ListTypedLinkFacetNamesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## lookupPolicy

> LookupPolicyResponse lookupPolicy(xAmzDataPartition, lookupPolicyRequest, opts)



Lists all policies from the root of the &lt;a&gt;Directory&lt;/a&gt; to the object specified. If there are no policies present, an empty list is returned. If policies are present, and if some objects don&#39;t have the policies attached, it returns the &lt;code&gt;ObjectIdentifier&lt;/code&gt; for such objects. If policies are present, it returns &lt;code&gt;ObjectIdentifier&lt;/code&gt;, &lt;code&gt;policyId&lt;/code&gt;, and &lt;code&gt;policyType&lt;/code&gt;. Paths that don&#39;t lead to the root from the target object are ignored. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies\&quot;&gt;Policies&lt;/a&gt;.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a>. For more information, see <a>arns</a>.
let lookupPolicyRequest = new AmazonCloudDirectory.LookupPolicyRequest(); // LookupPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.lookupPolicy(xAmzDataPartition, lookupPolicyRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt;. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **lookupPolicyRequest** | [**LookupPolicyRequest**](LookupPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**LookupPolicyResponse**](LookupPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## publishSchema

> PublishSchemaResponse publishSchema(xAmzDataPartition, publishSchemaRequest, opts)



Publishes a development schema with a major version and a recommended minor version.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the development schema. For more information, see <a>arns</a>.
let publishSchemaRequest = new AmazonCloudDirectory.PublishSchemaRequest(); // PublishSchemaRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.publishSchema(xAmzDataPartition, publishSchemaRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the development schema. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **publishSchemaRequest** | [**PublishSchemaRequest**](PublishSchemaRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PublishSchemaResponse**](PublishSchemaResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putSchemaFromJson

> PutSchemaFromJsonResponse putSchemaFromJson(xAmzDataPartition, putSchemaFromJsonRequest, opts)



Allows a schema to be updated using JSON upload. Only available for development schemas. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_jsonformat.html#schemas_json\&quot;&gt;JSON Schema Format&lt;/a&gt; for more information.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the schema to update.
let putSchemaFromJsonRequest = new AmazonCloudDirectory.PutSchemaFromJsonRequest(); // PutSchemaFromJsonRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putSchemaFromJson(xAmzDataPartition, putSchemaFromJsonRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The ARN of the schema to update. | 
 **putSchemaFromJsonRequest** | [**PutSchemaFromJsonRequest**](PutSchemaFromJsonRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutSchemaFromJsonResponse**](PutSchemaFromJsonResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeFacetFromObject

> Object removeFacetFromObject(xAmzDataPartition, removeFacetFromObjectRequest, opts)



Removes the specified facet from the specified object.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The ARN of the directory in which the object resides.
let removeFacetFromObjectRequest = new AmazonCloudDirectory.RemoveFacetFromObjectRequest(); // RemoveFacetFromObjectRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.removeFacetFromObject(xAmzDataPartition, removeFacetFromObjectRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The ARN of the directory in which the object resides. | 
 **removeFacetFromObjectRequest** | [**RemoveFacetFromObjectRequest**](RemoveFacetFromObjectRequest.md)|  | 
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

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(tagResourceRequest, opts)



An API operation for adding tags to a resource.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let tagResourceRequest = new AmazonCloudDirectory.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(tagResourceRequest, opts, (error, data, response) => {
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
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
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

- **Content-Type**: application/json
- **Accept**: application/json


## untagResource

> Object untagResource(untagResourceRequest, opts)



An API operation for removing tags from a resource.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let untagResourceRequest = new AmazonCloudDirectory.UntagResourceRequest(); // UntagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(untagResourceRequest, opts, (error, data, response) => {
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
 **untagResourceRequest** | [**UntagResourceRequest**](UntagResourceRequest.md)|  | 
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

- **Content-Type**: application/json
- **Accept**: application/json


## updateFacet

> Object updateFacet(xAmzDataPartition, updateFacetRequest, opts)



&lt;p&gt;Does the following:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Adds new &lt;code&gt;Attributes&lt;/code&gt;, &lt;code&gt;Rules&lt;/code&gt;, or &lt;code&gt;ObjectTypes&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Updates existing &lt;code&gt;Attributes&lt;/code&gt;, &lt;code&gt;Rules&lt;/code&gt;, or &lt;code&gt;ObjectTypes&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Deletes existing &lt;code&gt;Attributes&lt;/code&gt;, &lt;code&gt;Rules&lt;/code&gt;, or &lt;code&gt;ObjectTypes&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Facet</a>. For more information, see <a>arns</a>.
let updateFacetRequest = new AmazonCloudDirectory.UpdateFacetRequest(); // UpdateFacetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateFacet(xAmzDataPartition, updateFacetRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Facet&lt;/a&gt;. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **updateFacetRequest** | [**UpdateFacetRequest**](UpdateFacetRequest.md)|  | 
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

- **Content-Type**: application/json
- **Accept**: application/json


## updateLinkAttributes

> Object updateLinkAttributes(xAmzDataPartition, updateLinkAttributesRequest, opts)



Updates a given typed link’s attributes. Attributes to be updated must not contribute to the typed link’s identity, as defined by its &lt;code&gt;IdentityAttributeOrder&lt;/code&gt;.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the Directory where the updated typed link resides. For more information, see <a>arns</a> or <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\">Typed Links</a>.
let updateLinkAttributesRequest = new AmazonCloudDirectory.UpdateLinkAttributesRequest(); // UpdateLinkAttributesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateLinkAttributes(xAmzDataPartition, updateLinkAttributesRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the Directory where the updated typed link resides. For more information, see &lt;a&gt;arns&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\&quot;&gt;Typed Links&lt;/a&gt;. | 
 **updateLinkAttributesRequest** | [**UpdateLinkAttributesRequest**](UpdateLinkAttributesRequest.md)|  | 
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

- **Content-Type**: application/json
- **Accept**: application/json


## updateObjectAttributes

> UpdateObjectAttributesResponse updateObjectAttributes(xAmzDataPartition, updateObjectAttributesRequest, opts)



Updates a given object&#39;s attributes.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.
let updateObjectAttributesRequest = new AmazonCloudDirectory.UpdateObjectAttributesRequest(); // UpdateObjectAttributesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateObjectAttributes(xAmzDataPartition, updateObjectAttributesRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where the object resides. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **updateObjectAttributesRequest** | [**UpdateObjectAttributesRequest**](UpdateObjectAttributesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateObjectAttributesResponse**](UpdateObjectAttributesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSchema

> UpdateSchemaResponse updateSchema(xAmzDataPartition, updateSchemaRequest, opts)



Updates the schema name with a new name. Only development schema names can be updated.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) of the development schema. For more information, see <a>arns</a>.
let updateSchemaRequest = new AmazonCloudDirectory.UpdateSchemaRequest(); // UpdateSchemaRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSchema(xAmzDataPartition, updateSchemaRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) of the development schema. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **updateSchemaRequest** | [**UpdateSchemaRequest**](UpdateSchemaRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateSchemaResponse**](UpdateSchemaResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTypedLinkFacet

> Object updateTypedLinkFacet(xAmzDataPartition, updateTypedLinkFacetRequest, opts)



Updates a &lt;a&gt;TypedLinkFacet&lt;/a&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\&quot;&gt;Typed Links&lt;/a&gt;.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let xAmzDataPartition = "xAmzDataPartition_example"; // String | The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.
let updateTypedLinkFacetRequest = new AmazonCloudDirectory.UpdateTypedLinkFacetRequest(); // UpdateTypedLinkFacetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateTypedLinkFacet(xAmzDataPartition, updateTypedLinkFacetRequest, opts, (error, data, response) => {
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
 **xAmzDataPartition** | **String**| The Amazon Resource Name (ARN) that is associated with the schema. For more information, see &lt;a&gt;arns&lt;/a&gt;. | 
 **updateTypedLinkFacetRequest** | [**UpdateTypedLinkFacetRequest**](UpdateTypedLinkFacetRequest.md)|  | 
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

- **Content-Type**: application/json
- **Accept**: application/json


## upgradeAppliedSchema

> UpgradeAppliedSchemaResponse upgradeAppliedSchema(upgradeAppliedSchemaRequest, opts)



Upgrades a single directory in-place using the &lt;code&gt;PublishedSchemaArn&lt;/code&gt; with schema updates found in &lt;code&gt;MinorVersion&lt;/code&gt;. Backwards-compatible minor version upgrades are instantaneously available for readers on all objects in the directory. Note: This is a synchronous API call and upgrades only one schema on a given directory per call. To upgrade multiple directories from one schema, you would need to call this API on each directory.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let upgradeAppliedSchemaRequest = new AmazonCloudDirectory.UpgradeAppliedSchemaRequest(); // UpgradeAppliedSchemaRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.upgradeAppliedSchema(upgradeAppliedSchemaRequest, opts, (error, data, response) => {
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
 **upgradeAppliedSchemaRequest** | [**UpgradeAppliedSchemaRequest**](UpgradeAppliedSchemaRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpgradeAppliedSchemaResponse**](UpgradeAppliedSchemaResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## upgradePublishedSchema

> UpgradePublishedSchemaResponse upgradePublishedSchema(upgradePublishedSchemaRequest, opts)



Upgrades a published schema under a new minor version revision using the current contents of &lt;code&gt;DevelopmentSchemaArn&lt;/code&gt;.

### Example

```javascript
import AmazonCloudDirectory from 'amazon_cloud_directory';
let defaultClient = AmazonCloudDirectory.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudDirectory.DefaultApi();
let upgradePublishedSchemaRequest = new AmazonCloudDirectory.UpgradePublishedSchemaRequest(); // UpgradePublishedSchemaRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.upgradePublishedSchema(upgradePublishedSchemaRequest, opts, (error, data, response) => {
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
 **upgradePublishedSchemaRequest** | [**UpgradePublishedSchemaRequest**](UpgradePublishedSchemaRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpgradePublishedSchemaResponse**](UpgradePublishedSchemaResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

