# AmazonSimpleDb.DefaultApi

All URIs are relative to *http://sdb.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gETBatchDeleteAttributes**](DefaultApi.md#gETBatchDeleteAttributes) | **GET** /#Action&#x3D;BatchDeleteAttributes | 
[**gETBatchPutAttributes**](DefaultApi.md#gETBatchPutAttributes) | **GET** /#Action&#x3D;BatchPutAttributes | 
[**gETCreateDomain**](DefaultApi.md#gETCreateDomain) | **GET** /#Action&#x3D;CreateDomain | 
[**gETDeleteAttributes**](DefaultApi.md#gETDeleteAttributes) | **GET** /#Action&#x3D;DeleteAttributes | 
[**gETDeleteDomain**](DefaultApi.md#gETDeleteDomain) | **GET** /#Action&#x3D;DeleteDomain | 
[**gETDomainMetadata**](DefaultApi.md#gETDomainMetadata) | **GET** /#Action&#x3D;DomainMetadata | 
[**gETGetAttributes**](DefaultApi.md#gETGetAttributes) | **GET** /#Action&#x3D;GetAttributes | 
[**gETListDomains**](DefaultApi.md#gETListDomains) | **GET** /#Action&#x3D;ListDomains | 
[**gETPutAttributes**](DefaultApi.md#gETPutAttributes) | **GET** /#Action&#x3D;PutAttributes | 
[**gETSelect**](DefaultApi.md#gETSelect) | **GET** /#Action&#x3D;Select | 
[**pOSTBatchDeleteAttributes**](DefaultApi.md#pOSTBatchDeleteAttributes) | **POST** /#Action&#x3D;BatchDeleteAttributes | 
[**pOSTBatchPutAttributes**](DefaultApi.md#pOSTBatchPutAttributes) | **POST** /#Action&#x3D;BatchPutAttributes | 
[**pOSTCreateDomain**](DefaultApi.md#pOSTCreateDomain) | **POST** /#Action&#x3D;CreateDomain | 
[**pOSTDeleteAttributes**](DefaultApi.md#pOSTDeleteAttributes) | **POST** /#Action&#x3D;DeleteAttributes | 
[**pOSTDeleteDomain**](DefaultApi.md#pOSTDeleteDomain) | **POST** /#Action&#x3D;DeleteDomain | 
[**pOSTDomainMetadata**](DefaultApi.md#pOSTDomainMetadata) | **POST** /#Action&#x3D;DomainMetadata | 
[**pOSTGetAttributes**](DefaultApi.md#pOSTGetAttributes) | **POST** /#Action&#x3D;GetAttributes | 
[**pOSTListDomains**](DefaultApi.md#pOSTListDomains) | **POST** /#Action&#x3D;ListDomains | 
[**pOSTPutAttributes**](DefaultApi.md#pOSTPutAttributes) | **POST** /#Action&#x3D;PutAttributes | 
[**pOSTSelect**](DefaultApi.md#pOSTSelect) | **POST** /#Action&#x3D;Select | 



## gETBatchDeleteAttributes

> gETBatchDeleteAttributes(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, domainName, items, action, version)



&lt;p&gt; Performs multiple DeleteAttributes operations in a single call, which reduces round trips and latencies. This enables Amazon SimpleDB to optimize requests, which generally yields better throughput. &lt;/p&gt; &lt;note&gt; &lt;p&gt; If you specify BatchDeleteAttributes without attributes or values, all the attributes for the item are deleted. &lt;/p&gt; &lt;p&gt; BatchDeleteAttributes is an idempotent operation; running it multiple times on the same item or attribute doesn&#39;t result in an error. &lt;/p&gt; &lt;p&gt; The BatchDeleteAttributes operation succeeds or fails in its entirety. There are no partial deletes. You can execute multiple BatchDeleteAttributes operations and other operations in parallel. However, large numbers of concurrent BatchDeleteAttributes calls can result in Service Unavailable (503) responses. &lt;/p&gt; &lt;p&gt; This operation is vulnerable to exceeding the maximum URL size when making a REST request using the HTTP GET method. &lt;/p&gt; &lt;p&gt; This operation does not support conditions using Expected.X.Name, Expected.X.Value, or Expected.X.Exists. &lt;/p&gt; &lt;/note&gt; &lt;p&gt; The following limitations are enforced for this operation: &lt;ul&gt; &lt;li&gt;1 MB request size&lt;/li&gt; &lt;li&gt;25 item limit per BatchDeleteAttributes operation&lt;/li&gt; &lt;/ul&gt; &lt;/p&gt;

### Example

```javascript
import AmazonSimpleDb from 'amazon_simple_db';
let defaultClient = AmazonSimpleDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleDb.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let domainName = "domainName_example"; // String | The name of the domain in which the attributes are being deleted.
let items = [new AmazonSimpleDb.GETBatchDeleteAttributesItemsParameterInner()]; // [GETBatchDeleteAttributesItemsParameterInner] | A list of items on which to perform the operation.
let action = "action_example"; // String | 
let version = "version_example"; // String | 
apiInstance.gETBatchDeleteAttributes(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, domainName, items, action, version, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **domainName** | **String**| The name of the domain in which the attributes are being deleted. | 
 **items** | [**[GETBatchDeleteAttributesItemsParameterInner]**](GETBatchDeleteAttributesItemsParameterInner.md)| A list of items on which to perform the operation. | 
 **action** | **String**|  | 
 **version** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## gETBatchPutAttributes

> gETBatchPutAttributes(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, domainName, items, action, version)



&lt;p&gt; The &lt;code&gt;BatchPutAttributes&lt;/code&gt; operation creates or replaces attributes within one or more items. By using this operation, the client can perform multiple &lt;a&gt;PutAttribute&lt;/a&gt; operation with a single call. This helps yield savings in round trips and latencies, enabling Amazon SimpleDB to optimize requests and generally produce better throughput. &lt;/p&gt; &lt;p&gt; The client may specify the item name with the &lt;code&gt;Item.X.ItemName&lt;/code&gt; parameter. The client may specify new attributes using a combination of the &lt;code&gt;Item.X.Attribute.Y.Name&lt;/code&gt; and &lt;code&gt;Item.X.Attribute.Y.Value&lt;/code&gt; parameters. The client may specify the first attribute for the first item using the parameters &lt;code&gt;Item.0.Attribute.0.Name&lt;/code&gt; and &lt;code&gt;Item.0.Attribute.0.Value&lt;/code&gt;, and for the second attribute for the first item by the parameters &lt;code&gt;Item.0.Attribute.1.Name&lt;/code&gt; and &lt;code&gt;Item.0.Attribute.1.Value&lt;/code&gt;, and so on. &lt;/p&gt; &lt;p&gt; Attributes are uniquely identified within an item by their name/value combination. For example, a single item can have the attributes &lt;code&gt;{ \&quot;first_name\&quot;, \&quot;first_value\&quot; }&lt;/code&gt; and &lt;code&gt;{ \&quot;first_name\&quot;, \&quot;second_value\&quot; }&lt;/code&gt;. However, it cannot have two attribute instances where both the &lt;code&gt;Item.X.Attribute.Y.Name&lt;/code&gt; and &lt;code&gt;Item.X.Attribute.Y.Value&lt;/code&gt; are the same. &lt;/p&gt; &lt;p&gt; Optionally, the requester can supply the &lt;code&gt;Replace&lt;/code&gt; parameter for each individual value. Setting this value to &lt;code&gt;true&lt;/code&gt; will cause the new attribute values to replace the existing attribute values. For example, if an item &lt;code&gt;I&lt;/code&gt; has the attributes &lt;code&gt;{ &#39;a&#39;, &#39;1&#39; }, { &#39;b&#39;, &#39;2&#39;}&lt;/code&gt; and &lt;code&gt;{ &#39;b&#39;, &#39;3&#39; }&lt;/code&gt; and the requester does a BatchPutAttributes of &lt;code&gt;{&#39;I&#39;, &#39;b&#39;, &#39;4&#39; }&lt;/code&gt; with the Replace parameter set to true, the final attributes of the item will be &lt;code&gt;{ &#39;a&#39;, &#39;1&#39; }&lt;/code&gt; and &lt;code&gt;{ &#39;b&#39;, &#39;4&#39; }&lt;/code&gt;, replacing the previous values of the &#39;b&#39; attribute with the new value. &lt;/p&gt; &lt;note&gt; You cannot specify an empty string as an item or as an attribute name. The &lt;code&gt;BatchPutAttributes&lt;/code&gt; operation succeeds or fails in its entirety. There are no partial puts. &lt;/note&gt; &lt;important&gt; This operation is vulnerable to exceeding the maximum URL size when making a REST request using the HTTP GET method. This operation does not support conditions using &lt;code&gt;Expected.X.Name&lt;/code&gt;, &lt;code&gt;Expected.X.Value&lt;/code&gt;, or &lt;code&gt;Expected.X.Exists&lt;/code&gt;. &lt;/important&gt; &lt;p&gt; You can execute multiple &lt;code&gt;BatchPutAttributes&lt;/code&gt; operations and other operations in parallel. However, large numbers of concurrent &lt;code&gt;BatchPutAttributes&lt;/code&gt; calls can result in Service Unavailable (503) responses. &lt;/p&gt; &lt;p&gt; The following limitations are enforced for this operation: &lt;ul&gt; &lt;li&gt;256 attribute name-value pairs per item&lt;/li&gt; &lt;li&gt;1 MB request size&lt;/li&gt; &lt;li&gt;1 billion attributes per domain&lt;/li&gt; &lt;li&gt;10 GB of total user data storage per domain&lt;/li&gt; &lt;li&gt;25 item limit per &lt;code&gt;BatchPutAttributes&lt;/code&gt; operation&lt;/li&gt; &lt;/ul&gt; &lt;/p&gt;

### Example

```javascript
import AmazonSimpleDb from 'amazon_simple_db';
let defaultClient = AmazonSimpleDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleDb.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let domainName = "domainName_example"; // String | The name of the domain in which the attributes are being stored.
let items = [new AmazonSimpleDb.GETBatchPutAttributesItemsParameterInner()]; // [GETBatchPutAttributesItemsParameterInner] | A list of items on which to perform the operation.
let action = "action_example"; // String | 
let version = "version_example"; // String | 
apiInstance.gETBatchPutAttributes(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, domainName, items, action, version, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **domainName** | **String**| The name of the domain in which the attributes are being stored. | 
 **items** | [**[GETBatchPutAttributesItemsParameterInner]**](GETBatchPutAttributesItemsParameterInner.md)| A list of items on which to perform the operation. | 
 **action** | **String**|  | 
 **version** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## gETCreateDomain

> gETCreateDomain(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, domainName, action, version)



&lt;p&gt; The &lt;code&gt;CreateDomain&lt;/code&gt; operation creates a new domain. The domain name should be unique among the domains associated with the Access Key ID provided in the request. The &lt;code&gt;CreateDomain&lt;/code&gt; operation may take 10 or more seconds to complete. &lt;/p&gt; &lt;note&gt; CreateDomain is an idempotent operation; running it multiple times using the same domain name will not result in an error response. &lt;/note&gt; &lt;p&gt; The client can create up to 100 domains per account. &lt;/p&gt; &lt;p&gt; If the client requires additional domains, go to &lt;a href&#x3D;\&quot;http://aws.amazon.com/contact-us/simpledb-limit-request/\&quot;&gt; http://aws.amazon.com/contact-us/simpledb-limit-request/&lt;/a&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonSimpleDb from 'amazon_simple_db';
let defaultClient = AmazonSimpleDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleDb.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let domainName = "domainName_example"; // String | The name of the domain to create. The name can range between 3 and 255 characters and can contain the following characters: a-z, A-Z, 0-9, '_', '-', and '.'.
let action = "action_example"; // String | 
let version = "version_example"; // String | 
apiInstance.gETCreateDomain(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, domainName, action, version, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **domainName** | **String**| The name of the domain to create. The name can range between 3 and 255 characters and can contain the following characters: a-z, A-Z, 0-9, &#39;_&#39;, &#39;-&#39;, and &#39;.&#39;. | 
 **action** | **String**|  | 
 **version** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## gETDeleteAttributes

> gETDeleteAttributes(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, domainName, itemName, action, version, opts)



&lt;p&gt; Deletes one or more attributes associated with an item. If all attributes of the item are deleted, the item is deleted. &lt;/p&gt; &lt;note&gt; If &lt;code&gt;DeleteAttributes&lt;/code&gt; is called without being passed any attributes or values specified, all the attributes for the item are deleted. &lt;/note&gt; &lt;p&gt; &lt;code&gt;DeleteAttributes&lt;/code&gt; is an idempotent operation; running it multiple times on the same item or attribute does not result in an error response. &lt;/p&gt; &lt;p&gt; Because Amazon SimpleDB makes multiple copies of item data and uses an eventual consistency update model, performing a &lt;a&gt;GetAttributes&lt;/a&gt; or &lt;a&gt;Select&lt;/a&gt; operation (read) immediately after a &lt;code&gt;DeleteAttributes&lt;/code&gt; or &lt;a&gt;PutAttributes&lt;/a&gt; operation (write) might not return updated item data. &lt;/p&gt;

### Example

```javascript
import AmazonSimpleDb from 'amazon_simple_db';
let defaultClient = AmazonSimpleDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleDb.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let domainName = "domainName_example"; // String | The name of the domain in which to perform the operation.
let itemName = "itemName_example"; // String | The name of the item. Similar to rows on a spreadsheet, items represent individual objects that contain one or more value-attribute pairs.
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'attributes': [new AmazonSimpleDb.GETDeleteAttributesAttributesParameterInner()], // [GETDeleteAttributesAttributesParameterInner] | A list of Attributes. Similar to columns on a spreadsheet, attributes represent categories of data that can be assigned to items.
  'expected': new AmazonSimpleDb.GETDeleteAttributesExpectedParameter() // GETDeleteAttributesExpectedParameter | The update condition which, if specified, determines whether the specified attributes will be deleted or not. The update condition must be satisfied in order for this request to be processed and the attributes to be deleted.
};
apiInstance.gETDeleteAttributes(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, domainName, itemName, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **domainName** | **String**| The name of the domain in which to perform the operation. | 
 **itemName** | **String**| The name of the item. Similar to rows on a spreadsheet, items represent individual objects that contain one or more value-attribute pairs. | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **attributes** | [**[GETDeleteAttributesAttributesParameterInner]**](GETDeleteAttributesAttributesParameterInner.md)| A list of Attributes. Similar to columns on a spreadsheet, attributes represent categories of data that can be assigned to items. | [optional] 
 **expected** | [**GETDeleteAttributesExpectedParameter**](.md)| The update condition which, if specified, determines whether the specified attributes will be deleted or not. The update condition must be satisfied in order for this request to be processed and the attributes to be deleted. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## gETDeleteDomain

> gETDeleteDomain(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, domainName, action, version)



&lt;p&gt; The &lt;code&gt;DeleteDomain&lt;/code&gt; operation deletes a domain. Any items (and their attributes) in the domain are deleted as well. The &lt;code&gt;DeleteDomain&lt;/code&gt; operation might take 10 or more seconds to complete. &lt;/p&gt; &lt;note&gt; Running &lt;code&gt;DeleteDomain&lt;/code&gt; on a domain that does not exist or running the function multiple times using the same domain name will not result in an error response. &lt;/note&gt;

### Example

```javascript
import AmazonSimpleDb from 'amazon_simple_db';
let defaultClient = AmazonSimpleDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleDb.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let domainName = "domainName_example"; // String | The name of the domain to delete.
let action = "action_example"; // String | 
let version = "version_example"; // String | 
apiInstance.gETDeleteDomain(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, domainName, action, version, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **domainName** | **String**| The name of the domain to delete. | 
 **action** | **String**|  | 
 **version** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## gETDomainMetadata

> DomainMetadataResult gETDomainMetadata(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, domainName, action, version)



 Returns information about the domain, including when the domain was created, the number of items and attributes in the domain, and the size of the attribute names and values. 

### Example

```javascript
import AmazonSimpleDb from 'amazon_simple_db';
let defaultClient = AmazonSimpleDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleDb.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let domainName = "domainName_example"; // String | The name of the domain for which to display the metadata of.
let action = "action_example"; // String | 
let version = "version_example"; // String | 
apiInstance.gETDomainMetadata(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, domainName, action, version, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **domainName** | **String**| The name of the domain for which to display the metadata of. | 
 **action** | **String**|  | 
 **version** | **String**|  | 

### Return type

[**DomainMetadataResult**](DomainMetadataResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## gETGetAttributes

> GetAttributesResult gETGetAttributes(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, domainName, itemName, action, version, opts)



&lt;p&gt; Returns all of the attributes associated with the specified item. Optionally, the attributes returned can be limited to one or more attributes by specifying an attribute name parameter. &lt;/p&gt; &lt;p&gt; If the item does not exist on the replica that was accessed for this operation, an empty set is returned. The system does not return an error as it cannot guarantee the item does not exist on other replicas. &lt;/p&gt; &lt;note&gt; If GetAttributes is called without being passed any attribute names, all the attributes for the item are returned. &lt;/note&gt;

### Example

```javascript
import AmazonSimpleDb from 'amazon_simple_db';
let defaultClient = AmazonSimpleDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleDb.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let domainName = "domainName_example"; // String | The name of the domain in which to perform the operation.
let itemName = "itemName_example"; // String | The name of the item.
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'attributeNames': [null], // [String] | The names of the attributes.
  'consistentRead': true // Boolean | Determines whether or not strong consistency should be enforced when data is read from SimpleDB. If <code>true</code>, any data previously written to SimpleDB will be returned. Otherwise, results will be consistent eventually, and the client may not see data that was written immediately before your read.
};
apiInstance.gETGetAttributes(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, domainName, itemName, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **domainName** | **String**| The name of the domain in which to perform the operation. | 
 **itemName** | **String**| The name of the item. | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **attributeNames** | [**[String]**](String.md)| The names of the attributes. | [optional] 
 **consistentRead** | **Boolean**| Determines whether or not strong consistency should be enforced when data is read from SimpleDB. If &lt;code&gt;true&lt;/code&gt;, any data previously written to SimpleDB will be returned. Otherwise, results will be consistent eventually, and the client may not see data that was written immediately before your read. | [optional] 

### Return type

[**GetAttributesResult**](GetAttributesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## gETListDomains

> ListDomainsResult gETListDomains(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts)



 The &lt;code&gt;ListDomains&lt;/code&gt; operation lists all domains associated with the Access Key ID. It returns domain names up to the limit set by &lt;a href&#x3D;\&quot;#MaxNumberOfDomains\&quot;&gt;MaxNumberOfDomains&lt;/a&gt;. A &lt;a href&#x3D;\&quot;#NextToken\&quot;&gt;NextToken&lt;/a&gt; is returned if there are more than &lt;code&gt;MaxNumberOfDomains&lt;/code&gt; domains. Calling &lt;code&gt;ListDomains&lt;/code&gt; successive times with the &lt;code&gt;NextToken&lt;/code&gt; provided by the operation returns up to &lt;code&gt;MaxNumberOfDomains&lt;/code&gt; more domain names with each successive operation call. 

### Example

```javascript
import AmazonSimpleDb from 'amazon_simple_db';
let defaultClient = AmazonSimpleDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleDb.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'maxNumberOfDomains': 56, // Number | The maximum number of domain names you want returned. The range is 1 to 100. The default setting is 100.
  'nextToken': "nextToken_example" // String | A string informing Amazon SimpleDB where to start the next list of domain names.
};
apiInstance.gETListDomains(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **maxNumberOfDomains** | **Number**| The maximum number of domain names you want returned. The range is 1 to 100. The default setting is 100. | [optional] 
 **nextToken** | **String**| A string informing Amazon SimpleDB where to start the next list of domain names. | [optional] 

### Return type

[**ListDomainsResult**](ListDomainsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## gETPutAttributes

> gETPutAttributes(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, domainName, itemName, attributes, action, version, opts)



&lt;p&gt; The PutAttributes operation creates or replaces attributes in an item. The client may specify new attributes using a combination of the &lt;code&gt;Attribute.X.Name&lt;/code&gt; and &lt;code&gt;Attribute.X.Value&lt;/code&gt; parameters. The client specifies the first attribute by the parameters &lt;code&gt;Attribute.0.Name&lt;/code&gt; and &lt;code&gt;Attribute.0.Value&lt;/code&gt;, the second attribute by the parameters &lt;code&gt;Attribute.1.Name&lt;/code&gt; and &lt;code&gt;Attribute.1.Value&lt;/code&gt;, and so on. &lt;/p&gt; &lt;p&gt; Attributes are uniquely identified in an item by their name/value combination. For example, a single item can have the attributes &lt;code&gt;{ \&quot;first_name\&quot;, \&quot;first_value\&quot; }&lt;/code&gt; and &lt;code&gt;{ \&quot;first_name\&quot;, second_value\&quot; }&lt;/code&gt;. However, it cannot have two attribute instances where both the &lt;code&gt;Attribute.X.Name&lt;/code&gt; and &lt;code&gt;Attribute.X.Value&lt;/code&gt; are the same. &lt;/p&gt; &lt;p&gt; Optionally, the requestor can supply the &lt;code&gt;Replace&lt;/code&gt; parameter for each individual attribute. Setting this value to &lt;code&gt;true&lt;/code&gt; causes the new attribute value to replace the existing attribute value(s). For example, if an item has the attributes &lt;code&gt;{ &#39;a&#39;, &#39;1&#39; }&lt;/code&gt;, &lt;code&gt;{ &#39;b&#39;, &#39;2&#39;}&lt;/code&gt; and &lt;code&gt;{ &#39;b&#39;, &#39;3&#39; }&lt;/code&gt; and the requestor calls &lt;code&gt;PutAttributes&lt;/code&gt; using the attributes &lt;code&gt;{ &#39;b&#39;, &#39;4&#39; }&lt;/code&gt; with the &lt;code&gt;Replace&lt;/code&gt; parameter set to true, the final attributes of the item are changed to &lt;code&gt;{ &#39;a&#39;, &#39;1&#39; }&lt;/code&gt; and &lt;code&gt;{ &#39;b&#39;, &#39;4&#39; }&lt;/code&gt;, which replaces the previous values of the &#39;b&#39; attribute with the new value. &lt;/p&gt; &lt;note&gt; Using &lt;code&gt;PutAttributes&lt;/code&gt; to replace attribute values that do not exist will not result in an error response. &lt;/note&gt; &lt;p&gt; You cannot specify an empty string as an attribute name. &lt;/p&gt; &lt;p&gt; Because Amazon SimpleDB makes multiple copies of client data and uses an eventual consistency update model, an immediate &lt;a&gt;GetAttributes&lt;/a&gt; or &lt;a&gt;Select&lt;/a&gt; operation (read) immediately after a &lt;a&gt;PutAttributes&lt;/a&gt; or &lt;a&gt;DeleteAttributes&lt;/a&gt; operation (write) might not return the updated data. &lt;/p&gt; &lt;p&gt; The following limitations are enforced for this operation: &lt;ul&gt; &lt;li&gt;256 total attribute name-value pairs per item&lt;/li&gt; &lt;li&gt;One billion attributes per domain&lt;/li&gt; &lt;li&gt;10 GB of total user data storage per domain&lt;/li&gt; &lt;/ul&gt; &lt;/p&gt;

### Example

```javascript
import AmazonSimpleDb from 'amazon_simple_db';
let defaultClient = AmazonSimpleDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleDb.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let domainName = "domainName_example"; // String | The name of the domain in which to perform the operation.
let itemName = "itemName_example"; // String | The name of the item.
let attributes = [new AmazonSimpleDb.GETPutAttributesAttributesParameterInner()]; // [GETPutAttributesAttributesParameterInner] | The list of attributes.
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'expected': new AmazonSimpleDb.GETDeleteAttributesExpectedParameter() // GETDeleteAttributesExpectedParameter | The update condition which, if specified, determines whether the specified attributes will be updated or not. The update condition must be satisfied in order for this request to be processed and the attributes to be updated.
};
apiInstance.gETPutAttributes(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, domainName, itemName, attributes, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **domainName** | **String**| The name of the domain in which to perform the operation. | 
 **itemName** | **String**| The name of the item. | 
 **attributes** | [**[GETPutAttributesAttributesParameterInner]**](GETPutAttributesAttributesParameterInner.md)| The list of attributes. | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **expected** | [**GETDeleteAttributesExpectedParameter**](.md)| The update condition which, if specified, determines whether the specified attributes will be updated or not. The update condition must be satisfied in order for this request to be processed and the attributes to be updated. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## gETSelect

> SelectResult gETSelect(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, selectExpression, action, version, opts)



&lt;p&gt; The &lt;code&gt;Select&lt;/code&gt; operation returns a set of attributes for &lt;code&gt;ItemNames&lt;/code&gt; that match the select expression. &lt;code&gt;Select&lt;/code&gt; is similar to the standard SQL SELECT statement. &lt;/p&gt; &lt;p&gt; The total size of the response cannot exceed 1 MB in total size. Amazon SimpleDB automatically adjusts the number of items returned per page to enforce this limit. For example, if the client asks to retrieve 2500 items, but each individual item is 10 kB in size, the system returns 100 items and an appropriate &lt;code&gt;NextToken&lt;/code&gt; so the client can access the next page of results. &lt;/p&gt; &lt;p&gt; For information on how to construct select expressions, see Using Select to Create Amazon SimpleDB Queries in the Developer Guide. &lt;/p&gt;

### Example

```javascript
import AmazonSimpleDb from 'amazon_simple_db';
let defaultClient = AmazonSimpleDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleDb.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let selectExpression = "selectExpression_example"; // String | The expression used to query the domain.
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'nextToken': "nextToken_example", // String | A string informing Amazon SimpleDB where to start the next list of <code>ItemNames</code>.
  'consistentRead': true // Boolean | Determines whether or not strong consistency should be enforced when data is read from SimpleDB. If <code>true</code>, any data previously written to SimpleDB will be returned. Otherwise, results will be consistent eventually, and the client may not see data that was written immediately before your read.
};
apiInstance.gETSelect(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, selectExpression, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **selectExpression** | **String**| The expression used to query the domain. | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **nextToken** | **String**| A string informing Amazon SimpleDB where to start the next list of &lt;code&gt;ItemNames&lt;/code&gt;. | [optional] 
 **consistentRead** | **Boolean**| Determines whether or not strong consistency should be enforced when data is read from SimpleDB. If &lt;code&gt;true&lt;/code&gt;, any data previously written to SimpleDB will be returned. Otherwise, results will be consistent eventually, and the client may not see data that was written immediately before your read. | [optional] 

### Return type

[**SelectResult**](SelectResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## pOSTBatchDeleteAttributes

> pOSTBatchDeleteAttributes(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts)



&lt;p&gt; Performs multiple DeleteAttributes operations in a single call, which reduces round trips and latencies. This enables Amazon SimpleDB to optimize requests, which generally yields better throughput. &lt;/p&gt; &lt;note&gt; &lt;p&gt; If you specify BatchDeleteAttributes without attributes or values, all the attributes for the item are deleted. &lt;/p&gt; &lt;p&gt; BatchDeleteAttributes is an idempotent operation; running it multiple times on the same item or attribute doesn&#39;t result in an error. &lt;/p&gt; &lt;p&gt; The BatchDeleteAttributes operation succeeds or fails in its entirety. There are no partial deletes. You can execute multiple BatchDeleteAttributes operations and other operations in parallel. However, large numbers of concurrent BatchDeleteAttributes calls can result in Service Unavailable (503) responses. &lt;/p&gt; &lt;p&gt; This operation is vulnerable to exceeding the maximum URL size when making a REST request using the HTTP GET method. &lt;/p&gt; &lt;p&gt; This operation does not support conditions using Expected.X.Name, Expected.X.Value, or Expected.X.Exists. &lt;/p&gt; &lt;/note&gt; &lt;p&gt; The following limitations are enforced for this operation: &lt;ul&gt; &lt;li&gt;1 MB request size&lt;/li&gt; &lt;li&gt;25 item limit per BatchDeleteAttributes operation&lt;/li&gt; &lt;/ul&gt; &lt;/p&gt;

### Example

```javascript
import AmazonSimpleDb from 'amazon_simple_db';
let defaultClient = AmazonSimpleDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleDb.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'batchDeleteAttributesRequest': new AmazonSimpleDb.BatchDeleteAttributesRequest() // BatchDeleteAttributesRequest | 
};
apiInstance.pOSTBatchDeleteAttributes(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **batchDeleteAttributesRequest** | [**BatchDeleteAttributesRequest**](BatchDeleteAttributesRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: Not defined


## pOSTBatchPutAttributes

> pOSTBatchPutAttributes(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts)



&lt;p&gt; The &lt;code&gt;BatchPutAttributes&lt;/code&gt; operation creates or replaces attributes within one or more items. By using this operation, the client can perform multiple &lt;a&gt;PutAttribute&lt;/a&gt; operation with a single call. This helps yield savings in round trips and latencies, enabling Amazon SimpleDB to optimize requests and generally produce better throughput. &lt;/p&gt; &lt;p&gt; The client may specify the item name with the &lt;code&gt;Item.X.ItemName&lt;/code&gt; parameter. The client may specify new attributes using a combination of the &lt;code&gt;Item.X.Attribute.Y.Name&lt;/code&gt; and &lt;code&gt;Item.X.Attribute.Y.Value&lt;/code&gt; parameters. The client may specify the first attribute for the first item using the parameters &lt;code&gt;Item.0.Attribute.0.Name&lt;/code&gt; and &lt;code&gt;Item.0.Attribute.0.Value&lt;/code&gt;, and for the second attribute for the first item by the parameters &lt;code&gt;Item.0.Attribute.1.Name&lt;/code&gt; and &lt;code&gt;Item.0.Attribute.1.Value&lt;/code&gt;, and so on. &lt;/p&gt; &lt;p&gt; Attributes are uniquely identified within an item by their name/value combination. For example, a single item can have the attributes &lt;code&gt;{ \&quot;first_name\&quot;, \&quot;first_value\&quot; }&lt;/code&gt; and &lt;code&gt;{ \&quot;first_name\&quot;, \&quot;second_value\&quot; }&lt;/code&gt;. However, it cannot have two attribute instances where both the &lt;code&gt;Item.X.Attribute.Y.Name&lt;/code&gt; and &lt;code&gt;Item.X.Attribute.Y.Value&lt;/code&gt; are the same. &lt;/p&gt; &lt;p&gt; Optionally, the requester can supply the &lt;code&gt;Replace&lt;/code&gt; parameter for each individual value. Setting this value to &lt;code&gt;true&lt;/code&gt; will cause the new attribute values to replace the existing attribute values. For example, if an item &lt;code&gt;I&lt;/code&gt; has the attributes &lt;code&gt;{ &#39;a&#39;, &#39;1&#39; }, { &#39;b&#39;, &#39;2&#39;}&lt;/code&gt; and &lt;code&gt;{ &#39;b&#39;, &#39;3&#39; }&lt;/code&gt; and the requester does a BatchPutAttributes of &lt;code&gt;{&#39;I&#39;, &#39;b&#39;, &#39;4&#39; }&lt;/code&gt; with the Replace parameter set to true, the final attributes of the item will be &lt;code&gt;{ &#39;a&#39;, &#39;1&#39; }&lt;/code&gt; and &lt;code&gt;{ &#39;b&#39;, &#39;4&#39; }&lt;/code&gt;, replacing the previous values of the &#39;b&#39; attribute with the new value. &lt;/p&gt; &lt;note&gt; You cannot specify an empty string as an item or as an attribute name. The &lt;code&gt;BatchPutAttributes&lt;/code&gt; operation succeeds or fails in its entirety. There are no partial puts. &lt;/note&gt; &lt;important&gt; This operation is vulnerable to exceeding the maximum URL size when making a REST request using the HTTP GET method. This operation does not support conditions using &lt;code&gt;Expected.X.Name&lt;/code&gt;, &lt;code&gt;Expected.X.Value&lt;/code&gt;, or &lt;code&gt;Expected.X.Exists&lt;/code&gt;. &lt;/important&gt; &lt;p&gt; You can execute multiple &lt;code&gt;BatchPutAttributes&lt;/code&gt; operations and other operations in parallel. However, large numbers of concurrent &lt;code&gt;BatchPutAttributes&lt;/code&gt; calls can result in Service Unavailable (503) responses. &lt;/p&gt; &lt;p&gt; The following limitations are enforced for this operation: &lt;ul&gt; &lt;li&gt;256 attribute name-value pairs per item&lt;/li&gt; &lt;li&gt;1 MB request size&lt;/li&gt; &lt;li&gt;1 billion attributes per domain&lt;/li&gt; &lt;li&gt;10 GB of total user data storage per domain&lt;/li&gt; &lt;li&gt;25 item limit per &lt;code&gt;BatchPutAttributes&lt;/code&gt; operation&lt;/li&gt; &lt;/ul&gt; &lt;/p&gt;

### Example

```javascript
import AmazonSimpleDb from 'amazon_simple_db';
let defaultClient = AmazonSimpleDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleDb.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'batchPutAttributesRequest': new AmazonSimpleDb.BatchPutAttributesRequest() // BatchPutAttributesRequest | 
};
apiInstance.pOSTBatchPutAttributes(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **batchPutAttributesRequest** | [**BatchPutAttributesRequest**](BatchPutAttributesRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## pOSTCreateDomain

> pOSTCreateDomain(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts)



&lt;p&gt; The &lt;code&gt;CreateDomain&lt;/code&gt; operation creates a new domain. The domain name should be unique among the domains associated with the Access Key ID provided in the request. The &lt;code&gt;CreateDomain&lt;/code&gt; operation may take 10 or more seconds to complete. &lt;/p&gt; &lt;note&gt; CreateDomain is an idempotent operation; running it multiple times using the same domain name will not result in an error response. &lt;/note&gt; &lt;p&gt; The client can create up to 100 domains per account. &lt;/p&gt; &lt;p&gt; If the client requires additional domains, go to &lt;a href&#x3D;\&quot;http://aws.amazon.com/contact-us/simpledb-limit-request/\&quot;&gt; http://aws.amazon.com/contact-us/simpledb-limit-request/&lt;/a&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonSimpleDb from 'amazon_simple_db';
let defaultClient = AmazonSimpleDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleDb.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'createDomainRequest': new AmazonSimpleDb.CreateDomainRequest() // CreateDomainRequest | 
};
apiInstance.pOSTCreateDomain(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **createDomainRequest** | [**CreateDomainRequest**](CreateDomainRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## pOSTDeleteAttributes

> pOSTDeleteAttributes(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts)



&lt;p&gt; Deletes one or more attributes associated with an item. If all attributes of the item are deleted, the item is deleted. &lt;/p&gt; &lt;note&gt; If &lt;code&gt;DeleteAttributes&lt;/code&gt; is called without being passed any attributes or values specified, all the attributes for the item are deleted. &lt;/note&gt; &lt;p&gt; &lt;code&gt;DeleteAttributes&lt;/code&gt; is an idempotent operation; running it multiple times on the same item or attribute does not result in an error response. &lt;/p&gt; &lt;p&gt; Because Amazon SimpleDB makes multiple copies of item data and uses an eventual consistency update model, performing a &lt;a&gt;GetAttributes&lt;/a&gt; or &lt;a&gt;Select&lt;/a&gt; operation (read) immediately after a &lt;code&gt;DeleteAttributes&lt;/code&gt; or &lt;a&gt;PutAttributes&lt;/a&gt; operation (write) might not return updated item data. &lt;/p&gt;

### Example

```javascript
import AmazonSimpleDb from 'amazon_simple_db';
let defaultClient = AmazonSimpleDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleDb.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'deleteAttributesRequest': new AmazonSimpleDb.DeleteAttributesRequest() // DeleteAttributesRequest | 
};
apiInstance.pOSTDeleteAttributes(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **deleteAttributesRequest** | [**DeleteAttributesRequest**](DeleteAttributesRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## pOSTDeleteDomain

> pOSTDeleteDomain(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts)



&lt;p&gt; The &lt;code&gt;DeleteDomain&lt;/code&gt; operation deletes a domain. Any items (and their attributes) in the domain are deleted as well. The &lt;code&gt;DeleteDomain&lt;/code&gt; operation might take 10 or more seconds to complete. &lt;/p&gt; &lt;note&gt; Running &lt;code&gt;DeleteDomain&lt;/code&gt; on a domain that does not exist or running the function multiple times using the same domain name will not result in an error response. &lt;/note&gt;

### Example

```javascript
import AmazonSimpleDb from 'amazon_simple_db';
let defaultClient = AmazonSimpleDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleDb.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'deleteDomainRequest': new AmazonSimpleDb.DeleteDomainRequest() // DeleteDomainRequest | 
};
apiInstance.pOSTDeleteDomain(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **deleteDomainRequest** | [**DeleteDomainRequest**](DeleteDomainRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## pOSTDomainMetadata

> DomainMetadataResult pOSTDomainMetadata(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts)



 Returns information about the domain, including when the domain was created, the number of items and attributes in the domain, and the size of the attribute names and values. 

### Example

```javascript
import AmazonSimpleDb from 'amazon_simple_db';
let defaultClient = AmazonSimpleDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleDb.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'domainMetadataRequest': new AmazonSimpleDb.DomainMetadataRequest() // DomainMetadataRequest | 
};
apiInstance.pOSTDomainMetadata(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **domainMetadataRequest** | [**DomainMetadataRequest**](DomainMetadataRequest.md)|  | [optional] 

### Return type

[**DomainMetadataResult**](DomainMetadataResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## pOSTGetAttributes

> GetAttributesResult pOSTGetAttributes(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts)



&lt;p&gt; Returns all of the attributes associated with the specified item. Optionally, the attributes returned can be limited to one or more attributes by specifying an attribute name parameter. &lt;/p&gt; &lt;p&gt; If the item does not exist on the replica that was accessed for this operation, an empty set is returned. The system does not return an error as it cannot guarantee the item does not exist on other replicas. &lt;/p&gt; &lt;note&gt; If GetAttributes is called without being passed any attribute names, all the attributes for the item are returned. &lt;/note&gt;

### Example

```javascript
import AmazonSimpleDb from 'amazon_simple_db';
let defaultClient = AmazonSimpleDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleDb.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'getAttributesRequest': new AmazonSimpleDb.GetAttributesRequest() // GetAttributesRequest | 
};
apiInstance.pOSTGetAttributes(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **getAttributesRequest** | [**GetAttributesRequest**](GetAttributesRequest.md)|  | [optional] 

### Return type

[**GetAttributesResult**](GetAttributesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## pOSTListDomains

> ListDomainsResult pOSTListDomains(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts)



 The &lt;code&gt;ListDomains&lt;/code&gt; operation lists all domains associated with the Access Key ID. It returns domain names up to the limit set by &lt;a href&#x3D;\&quot;#MaxNumberOfDomains\&quot;&gt;MaxNumberOfDomains&lt;/a&gt;. A &lt;a href&#x3D;\&quot;#NextToken\&quot;&gt;NextToken&lt;/a&gt; is returned if there are more than &lt;code&gt;MaxNumberOfDomains&lt;/code&gt; domains. Calling &lt;code&gt;ListDomains&lt;/code&gt; successive times with the &lt;code&gt;NextToken&lt;/code&gt; provided by the operation returns up to &lt;code&gt;MaxNumberOfDomains&lt;/code&gt; more domain names with each successive operation call. 

### Example

```javascript
import AmazonSimpleDb from 'amazon_simple_db';
let defaultClient = AmazonSimpleDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleDb.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'maxNumberOfDomains': "maxNumberOfDomains_example", // String | Pagination limit
  'nextToken': "nextToken_example", // String | Pagination token
  'listDomainsRequest': new AmazonSimpleDb.ListDomainsRequest() // ListDomainsRequest | 
};
apiInstance.pOSTListDomains(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **maxNumberOfDomains** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 
 **listDomainsRequest** | [**ListDomainsRequest**](ListDomainsRequest.md)|  | [optional] 

### Return type

[**ListDomainsResult**](ListDomainsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## pOSTPutAttributes

> pOSTPutAttributes(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts)



&lt;p&gt; The PutAttributes operation creates or replaces attributes in an item. The client may specify new attributes using a combination of the &lt;code&gt;Attribute.X.Name&lt;/code&gt; and &lt;code&gt;Attribute.X.Value&lt;/code&gt; parameters. The client specifies the first attribute by the parameters &lt;code&gt;Attribute.0.Name&lt;/code&gt; and &lt;code&gt;Attribute.0.Value&lt;/code&gt;, the second attribute by the parameters &lt;code&gt;Attribute.1.Name&lt;/code&gt; and &lt;code&gt;Attribute.1.Value&lt;/code&gt;, and so on. &lt;/p&gt; &lt;p&gt; Attributes are uniquely identified in an item by their name/value combination. For example, a single item can have the attributes &lt;code&gt;{ \&quot;first_name\&quot;, \&quot;first_value\&quot; }&lt;/code&gt; and &lt;code&gt;{ \&quot;first_name\&quot;, second_value\&quot; }&lt;/code&gt;. However, it cannot have two attribute instances where both the &lt;code&gt;Attribute.X.Name&lt;/code&gt; and &lt;code&gt;Attribute.X.Value&lt;/code&gt; are the same. &lt;/p&gt; &lt;p&gt; Optionally, the requestor can supply the &lt;code&gt;Replace&lt;/code&gt; parameter for each individual attribute. Setting this value to &lt;code&gt;true&lt;/code&gt; causes the new attribute value to replace the existing attribute value(s). For example, if an item has the attributes &lt;code&gt;{ &#39;a&#39;, &#39;1&#39; }&lt;/code&gt;, &lt;code&gt;{ &#39;b&#39;, &#39;2&#39;}&lt;/code&gt; and &lt;code&gt;{ &#39;b&#39;, &#39;3&#39; }&lt;/code&gt; and the requestor calls &lt;code&gt;PutAttributes&lt;/code&gt; using the attributes &lt;code&gt;{ &#39;b&#39;, &#39;4&#39; }&lt;/code&gt; with the &lt;code&gt;Replace&lt;/code&gt; parameter set to true, the final attributes of the item are changed to &lt;code&gt;{ &#39;a&#39;, &#39;1&#39; }&lt;/code&gt; and &lt;code&gt;{ &#39;b&#39;, &#39;4&#39; }&lt;/code&gt;, which replaces the previous values of the &#39;b&#39; attribute with the new value. &lt;/p&gt; &lt;note&gt; Using &lt;code&gt;PutAttributes&lt;/code&gt; to replace attribute values that do not exist will not result in an error response. &lt;/note&gt; &lt;p&gt; You cannot specify an empty string as an attribute name. &lt;/p&gt; &lt;p&gt; Because Amazon SimpleDB makes multiple copies of client data and uses an eventual consistency update model, an immediate &lt;a&gt;GetAttributes&lt;/a&gt; or &lt;a&gt;Select&lt;/a&gt; operation (read) immediately after a &lt;a&gt;PutAttributes&lt;/a&gt; or &lt;a&gt;DeleteAttributes&lt;/a&gt; operation (write) might not return the updated data. &lt;/p&gt; &lt;p&gt; The following limitations are enforced for this operation: &lt;ul&gt; &lt;li&gt;256 total attribute name-value pairs per item&lt;/li&gt; &lt;li&gt;One billion attributes per domain&lt;/li&gt; &lt;li&gt;10 GB of total user data storage per domain&lt;/li&gt; &lt;/ul&gt; &lt;/p&gt;

### Example

```javascript
import AmazonSimpleDb from 'amazon_simple_db';
let defaultClient = AmazonSimpleDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleDb.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'putAttributesRequest': new AmazonSimpleDb.PutAttributesRequest() // PutAttributesRequest | 
};
apiInstance.pOSTPutAttributes(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **putAttributesRequest** | [**PutAttributesRequest**](PutAttributesRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml


## pOSTSelect

> SelectResult pOSTSelect(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts)



&lt;p&gt; The &lt;code&gt;Select&lt;/code&gt; operation returns a set of attributes for &lt;code&gt;ItemNames&lt;/code&gt; that match the select expression. &lt;code&gt;Select&lt;/code&gt; is similar to the standard SQL SELECT statement. &lt;/p&gt; &lt;p&gt; The total size of the response cannot exceed 1 MB in total size. Amazon SimpleDB automatically adjusts the number of items returned per page to enforce this limit. For example, if the client asks to retrieve 2500 items, but each individual item is 10 kB in size, the system returns 100 items and an appropriate &lt;code&gt;NextToken&lt;/code&gt; so the client can access the next page of results. &lt;/p&gt; &lt;p&gt; For information on how to construct select expressions, see Using Select to Create Amazon SimpleDB Queries in the Developer Guide. &lt;/p&gt;

### Example

```javascript
import AmazonSimpleDb from 'amazon_simple_db';
let defaultClient = AmazonSimpleDb.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleDb.DefaultApi();
let aWSAccessKeyId = "aWSAccessKeyId_example"; // String | 
let signatureMethod = "signatureMethod_example"; // String | 
let signatureVersion = "signatureVersion_example"; // String | 
let timestamp = "timestamp_example"; // String | 
let signature = "signature_example"; // String | 
let action = "action_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  'nextToken': "nextToken_example", // String | Pagination token
  'selectRequest': new AmazonSimpleDb.SelectRequest() // SelectRequest | 
};
apiInstance.pOSTSelect(aWSAccessKeyId, signatureMethod, signatureVersion, timestamp, signature, action, version, opts, (error, data, response) => {
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
 **aWSAccessKeyId** | **String**|  | 
 **signatureMethod** | **String**|  | 
 **signatureVersion** | **String**|  | 
 **timestamp** | **String**|  | 
 **signature** | **String**|  | 
 **action** | **String**|  | 
 **version** | **String**|  | 
 **nextToken** | **String**| Pagination token | [optional] 
 **selectRequest** | [**SelectRequest**](SelectRequest.md)|  | [optional] 

### Return type

[**SelectResult**](SelectResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: text/xml

