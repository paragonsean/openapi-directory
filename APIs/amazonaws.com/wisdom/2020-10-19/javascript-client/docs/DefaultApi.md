# AmazonConnectWisdomService.DefaultApi

All URIs are relative to *http://wisdom.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAssistant**](DefaultApi.md#createAssistant) | **POST** /assistants | 
[**createAssistantAssociation**](DefaultApi.md#createAssistantAssociation) | **POST** /assistants/{assistantId}/associations | 
[**createContent**](DefaultApi.md#createContent) | **POST** /knowledgeBases/{knowledgeBaseId}/contents | 
[**createKnowledgeBase**](DefaultApi.md#createKnowledgeBase) | **POST** /knowledgeBases | 
[**createSession**](DefaultApi.md#createSession) | **POST** /assistants/{assistantId}/sessions | 
[**deleteAssistant**](DefaultApi.md#deleteAssistant) | **DELETE** /assistants/{assistantId} | 
[**deleteAssistantAssociation**](DefaultApi.md#deleteAssistantAssociation) | **DELETE** /assistants/{assistantId}/associations/{assistantAssociationId} | 
[**deleteContent**](DefaultApi.md#deleteContent) | **DELETE** /knowledgeBases/{knowledgeBaseId}/contents/{contentId} | 
[**deleteKnowledgeBase**](DefaultApi.md#deleteKnowledgeBase) | **DELETE** /knowledgeBases/{knowledgeBaseId} | 
[**getAssistant**](DefaultApi.md#getAssistant) | **GET** /assistants/{assistantId} | 
[**getAssistantAssociation**](DefaultApi.md#getAssistantAssociation) | **GET** /assistants/{assistantId}/associations/{assistantAssociationId} | 
[**getContent**](DefaultApi.md#getContent) | **GET** /knowledgeBases/{knowledgeBaseId}/contents/{contentId} | 
[**getContentSummary**](DefaultApi.md#getContentSummary) | **GET** /knowledgeBases/{knowledgeBaseId}/contents/{contentId}/summary | 
[**getKnowledgeBase**](DefaultApi.md#getKnowledgeBase) | **GET** /knowledgeBases/{knowledgeBaseId} | 
[**getRecommendations**](DefaultApi.md#getRecommendations) | **GET** /assistants/{assistantId}/sessions/{sessionId}/recommendations | 
[**getSession**](DefaultApi.md#getSession) | **GET** /assistants/{assistantId}/sessions/{sessionId} | 
[**listAssistantAssociations**](DefaultApi.md#listAssistantAssociations) | **GET** /assistants/{assistantId}/associations | 
[**listAssistants**](DefaultApi.md#listAssistants) | **GET** /assistants | 
[**listContents**](DefaultApi.md#listContents) | **GET** /knowledgeBases/{knowledgeBaseId}/contents | 
[**listKnowledgeBases**](DefaultApi.md#listKnowledgeBases) | **GET** /knowledgeBases | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**notifyRecommendationsReceived**](DefaultApi.md#notifyRecommendationsReceived) | **POST** /assistants/{assistantId}/sessions/{sessionId}/recommendations/notify | 
[**queryAssistant**](DefaultApi.md#queryAssistant) | **POST** /assistants/{assistantId}/query | 
[**removeKnowledgeBaseTemplateUri**](DefaultApi.md#removeKnowledgeBaseTemplateUri) | **DELETE** /knowledgeBases/{knowledgeBaseId}/templateUri | 
[**searchContent**](DefaultApi.md#searchContent) | **POST** /knowledgeBases/{knowledgeBaseId}/search | 
[**searchSessions**](DefaultApi.md#searchSessions) | **POST** /assistants/{assistantId}/searchSessions | 
[**startContentUpload**](DefaultApi.md#startContentUpload) | **POST** /knowledgeBases/{knowledgeBaseId}/upload | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
[**updateContent**](DefaultApi.md#updateContent) | **POST** /knowledgeBases/{knowledgeBaseId}/contents/{contentId} | 
[**updateKnowledgeBaseTemplateUri**](DefaultApi.md#updateKnowledgeBaseTemplateUri) | **POST** /knowledgeBases/{knowledgeBaseId}/templateUri | 



## createAssistant

> CreateAssistantResponse createAssistant(createAssistantRequest, opts)



Creates an Amazon Connect Wisdom assistant.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let createAssistantRequest = new AmazonConnectWisdomService.CreateAssistantRequest(); // CreateAssistantRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAssistant(createAssistantRequest, opts, (error, data, response) => {
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
 **createAssistantRequest** | [**CreateAssistantRequest**](CreateAssistantRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAssistantResponse**](CreateAssistantResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAssistantAssociation

> CreateAssistantAssociationResponse createAssistantAssociation(assistantId, createAssistantAssociationRequest, opts)



Creates an association between an Amazon Connect Wisdom assistant and another resource. Currently, the only supported association is with a knowledge base. An assistant can have only a single association.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let assistantId = "assistantId_example"; // String | The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
let createAssistantAssociationRequest = new AmazonConnectWisdomService.CreateAssistantAssociationRequest(); // CreateAssistantAssociationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAssistantAssociation(assistantId, createAssistantAssociationRequest, opts, (error, data, response) => {
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
 **assistantId** | **String**| The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **createAssistantAssociationRequest** | [**CreateAssistantAssociationRequest**](CreateAssistantAssociationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAssistantAssociationResponse**](CreateAssistantAssociationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createContent

> CreateContentResponse createContent(knowledgeBaseId, createContentRequest, opts)



Creates Wisdom content. Before to calling this API, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html\&quot;&gt;StartContentUpload&lt;/a&gt; to upload an asset.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let knowledgeBaseId = "knowledgeBaseId_example"; // String | The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
let createContentRequest = new AmazonConnectWisdomService.CreateContentRequest(); // CreateContentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createContent(knowledgeBaseId, createContentRequest, opts, (error, data, response) => {
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
 **knowledgeBaseId** | **String**| The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **createContentRequest** | [**CreateContentRequest**](CreateContentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateContentResponse**](CreateContentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createKnowledgeBase

> CreateKnowledgeBaseResponse createKnowledgeBase(createKnowledgeBaseRequest, opts)



&lt;p&gt;Creates a knowledge base.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When using this API, you cannot reuse &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appintegrations/latest/APIReference/Welcome.html\&quot;&gt;Amazon AppIntegrations&lt;/a&gt; DataIntegrations with external knowledge bases such as Salesforce and ServiceNow. If you do, you&#39;ll get an &lt;code&gt;InvalidRequestException&lt;/code&gt; error. &lt;/p&gt; &lt;p&gt;For example, you&#39;re programmatically managing your external knowledge base, and you want to add or remove one of the fields that is being ingested from Salesforce. Do the following:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wisdom/latest/APIReference/API_DeleteKnowledgeBase.html\&quot;&gt;DeleteKnowledgeBase&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteDataIntegration.html\&quot;&gt;DeleteDataIntegration&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html\&quot;&gt;CreateDataIntegration&lt;/a&gt; to recreate the DataIntegration or a create different one.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call CreateKnowledgeBase.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;/note&gt;

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let createKnowledgeBaseRequest = new AmazonConnectWisdomService.CreateKnowledgeBaseRequest(); // CreateKnowledgeBaseRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createKnowledgeBase(createKnowledgeBaseRequest, opts, (error, data, response) => {
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
 **createKnowledgeBaseRequest** | [**CreateKnowledgeBaseRequest**](CreateKnowledgeBaseRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateKnowledgeBaseResponse**](CreateKnowledgeBaseResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSession

> CreateSessionResponse createSession(assistantId, createSessionRequest, opts)



Creates a session. A session is a contextual container used for generating recommendations. Amazon Connect creates a new Wisdom session for each contact on which Wisdom is enabled.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let assistantId = "assistantId_example"; // String | The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
let createSessionRequest = new AmazonConnectWisdomService.CreateSessionRequest(); // CreateSessionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSession(assistantId, createSessionRequest, opts, (error, data, response) => {
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
 **assistantId** | **String**| The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **createSessionRequest** | [**CreateSessionRequest**](CreateSessionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSessionResponse**](CreateSessionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAssistant

> Object deleteAssistant(assistantId, opts)



Deletes an assistant.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let assistantId = "assistantId_example"; // String | The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAssistant(assistantId, opts, (error, data, response) => {
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
 **assistantId** | **String**| The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
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


## deleteAssistantAssociation

> Object deleteAssistantAssociation(assistantAssociationId, assistantId, opts)



Deletes an assistant association.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let assistantAssociationId = "assistantAssociationId_example"; // String | The identifier of the assistant association. Can be either the ID or the ARN. URLs cannot contain the ARN.
let assistantId = "assistantId_example"; // String | The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAssistantAssociation(assistantAssociationId, assistantId, opts, (error, data, response) => {
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
 **assistantAssociationId** | **String**| The identifier of the assistant association. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **assistantId** | **String**| The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
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


## deleteContent

> Object deleteContent(contentId, knowledgeBaseId, opts)



Deletes the content.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let contentId = "contentId_example"; // String | The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.
let knowledgeBaseId = "knowledgeBaseId_example"; // String | The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteContent(contentId, knowledgeBaseId, opts, (error, data, response) => {
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
 **contentId** | **String**| The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **knowledgeBaseId** | **String**| The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
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


## deleteKnowledgeBase

> Object deleteKnowledgeBase(knowledgeBaseId, opts)



&lt;p&gt;Deletes the knowledge base.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When you use this API to delete an external knowledge base such as Salesforce or ServiceNow, you must also delete the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appintegrations/latest/APIReference/Welcome.html\&quot;&gt;Amazon AppIntegrations&lt;/a&gt; DataIntegration. This is because you can&#39;t reuse the DataIntegration after it&#39;s been associated with an external knowledge base. However, you can delete and recreate it. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteDataIntegration.html\&quot;&gt;DeleteDataIntegration&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html\&quot;&gt;CreateDataIntegration&lt;/a&gt; in the &lt;i&gt;Amazon AppIntegrations API Reference&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let knowledgeBaseId = "knowledgeBaseId_example"; // String | The knowledge base to delete content from. Can be either the ID or the ARN. URLs cannot contain the ARN.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteKnowledgeBase(knowledgeBaseId, opts, (error, data, response) => {
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
 **knowledgeBaseId** | **String**| The knowledge base to delete content from. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
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


## getAssistant

> GetAssistantResponse getAssistant(assistantId, opts)



Retrieves information about an assistant.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let assistantId = "assistantId_example"; // String | The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAssistant(assistantId, opts, (error, data, response) => {
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
 **assistantId** | **String**| The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAssistantResponse**](GetAssistantResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAssistantAssociation

> GetAssistantAssociationResponse getAssistantAssociation(assistantAssociationId, assistantId, opts)



Retrieves information about an assistant association.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let assistantAssociationId = "assistantAssociationId_example"; // String | The identifier of the assistant association. Can be either the ID or the ARN. URLs cannot contain the ARN.
let assistantId = "assistantId_example"; // String | The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAssistantAssociation(assistantAssociationId, assistantId, opts, (error, data, response) => {
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
 **assistantAssociationId** | **String**| The identifier of the assistant association. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **assistantId** | **String**| The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAssistantAssociationResponse**](GetAssistantAssociationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContent

> GetContentResponse getContent(contentId, knowledgeBaseId, opts)



Retrieves content, including a pre-signed URL to download the content.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let contentId = "contentId_example"; // String | The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.
let knowledgeBaseId = "knowledgeBaseId_example"; // String | The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getContent(contentId, knowledgeBaseId, opts, (error, data, response) => {
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
 **contentId** | **String**| The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **knowledgeBaseId** | **String**| The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetContentResponse**](GetContentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContentSummary

> GetContentSummaryResponse getContentSummary(contentId, knowledgeBaseId, opts)



Retrieves summary information about the content.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let contentId = "contentId_example"; // String | The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.
let knowledgeBaseId = "knowledgeBaseId_example"; // String | The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getContentSummary(contentId, knowledgeBaseId, opts, (error, data, response) => {
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
 **contentId** | **String**| The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **knowledgeBaseId** | **String**| The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetContentSummaryResponse**](GetContentSummaryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getKnowledgeBase

> GetKnowledgeBaseResponse getKnowledgeBase(knowledgeBaseId, opts)



Retrieves information about the knowledge base.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let knowledgeBaseId = "knowledgeBaseId_example"; // String | The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getKnowledgeBase(knowledgeBaseId, opts, (error, data, response) => {
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
 **knowledgeBaseId** | **String**| The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetKnowledgeBaseResponse**](GetKnowledgeBaseResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRecommendations

> GetRecommendationsResponse getRecommendations(assistantId, sessionId, opts)



Retrieves recommendations for the specified session. To avoid retrieving the same recommendations in subsequent calls, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wisdom/latest/APIReference/API_NotifyRecommendationsReceived.html\&quot;&gt;NotifyRecommendationsReceived&lt;/a&gt;. This API supports long-polling behavior with the &lt;code&gt;waitTimeSeconds&lt;/code&gt; parameter. Short poll is the default behavior and only returns recommendations already available. To perform a manual query against an assistant, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wisdom/latest/APIReference/API_QueryAssistant.html\&quot;&gt;QueryAssistant&lt;/a&gt;.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let assistantId = "assistantId_example"; // String | The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
let sessionId = "sessionId_example"; // String | The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'waitTimeSeconds': 56 // Number | The duration (in seconds) for which the call waits for a recommendation to be made available before returning. If a recommendation is available, the call returns sooner than <code>WaitTimeSeconds</code>. If no messages are available and the wait time expires, the call returns successfully with an empty list.
};
apiInstance.getRecommendations(assistantId, sessionId, opts, (error, data, response) => {
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
 **assistantId** | **String**| The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **sessionId** | **String**| The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **waitTimeSeconds** | **Number**| The duration (in seconds) for which the call waits for a recommendation to be made available before returning. If a recommendation is available, the call returns sooner than &lt;code&gt;WaitTimeSeconds&lt;/code&gt;. If no messages are available and the wait time expires, the call returns successfully with an empty list. | [optional] 

### Return type

[**GetRecommendationsResponse**](GetRecommendationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSession

> GetSessionResponse getSession(assistantId, sessionId, opts)



Retrieves information for a specified session.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let assistantId = "assistantId_example"; // String | The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
let sessionId = "sessionId_example"; // String | The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSession(assistantId, sessionId, opts, (error, data, response) => {
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
 **assistantId** | **String**| The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **sessionId** | **String**| The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSessionResponse**](GetSessionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAssistantAssociations

> ListAssistantAssociationsResponse listAssistantAssociations(assistantId, opts)



Lists information about assistant associations.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let assistantId = "assistantId_example"; // String | The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'nextToken': "nextToken_example" // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
};
apiInstance.listAssistantAssociations(assistantId, opts, (error, data, response) => {
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
 **assistantId** | **String**| The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 

### Return type

[**ListAssistantAssociationsResponse**](ListAssistantAssociationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAssistants

> ListAssistantsResponse listAssistants(opts)



Lists information about assistants.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'nextToken': "nextToken_example" // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
};
apiInstance.listAssistants(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 

### Return type

[**ListAssistantsResponse**](ListAssistantsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listContents

> ListContentsResponse listContents(knowledgeBaseId, opts)



Lists the content.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let knowledgeBaseId = "knowledgeBaseId_example"; // String | The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'nextToken': "nextToken_example" // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
};
apiInstance.listContents(knowledgeBaseId, opts, (error, data, response) => {
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
 **knowledgeBaseId** | **String**| The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 

### Return type

[**ListContentsResponse**](ListContentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listKnowledgeBases

> ListKnowledgeBasesResponse listKnowledgeBases(opts)



Lists the knowledge bases.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'nextToken': "nextToken_example" // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
};
apiInstance.listKnowledgeBases(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 

### Return type

[**ListKnowledgeBasesResponse**](ListKnowledgeBasesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Lists the tags for the specified resource.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(resourceArn, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## notifyRecommendationsReceived

> NotifyRecommendationsReceivedResponse notifyRecommendationsReceived(assistantId, sessionId, notifyRecommendationsReceivedRequest, opts)



Removes the specified recommendations from the specified assistant&#39;s queue of newly available recommendations. You can use this API in conjunction with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetRecommendations.html\&quot;&gt;GetRecommendations&lt;/a&gt; and a &lt;code&gt;waitTimeSeconds&lt;/code&gt; input for long-polling behavior and avoiding duplicate recommendations.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let assistantId = "assistantId_example"; // String | The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
let sessionId = "sessionId_example"; // String | The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.
let notifyRecommendationsReceivedRequest = new AmazonConnectWisdomService.NotifyRecommendationsReceivedRequest(); // NotifyRecommendationsReceivedRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.notifyRecommendationsReceived(assistantId, sessionId, notifyRecommendationsReceivedRequest, opts, (error, data, response) => {
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
 **assistantId** | **String**| The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **sessionId** | **String**| The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **notifyRecommendationsReceivedRequest** | [**NotifyRecommendationsReceivedRequest**](NotifyRecommendationsReceivedRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**NotifyRecommendationsReceivedResponse**](NotifyRecommendationsReceivedResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryAssistant

> QueryAssistantResponse queryAssistant(assistantId, queryAssistantRequest, opts)



Performs a manual search against the specified assistant. To retrieve recommendations for an assistant, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetRecommendations.html\&quot;&gt;GetRecommendations&lt;/a&gt;. 

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let assistantId = "assistantId_example"; // String | The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
let queryAssistantRequest = new AmazonConnectWisdomService.QueryAssistantRequest(); // QueryAssistantRequest | 
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
apiInstance.queryAssistant(assistantId, queryAssistantRequest, opts, (error, data, response) => {
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
 **assistantId** | **String**| The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **queryAssistantRequest** | [**QueryAssistantRequest**](QueryAssistantRequest.md)|  | 
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

[**QueryAssistantResponse**](QueryAssistantResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeKnowledgeBaseTemplateUri

> Object removeKnowledgeBaseTemplateUri(knowledgeBaseId, opts)



Removes a URI template from a knowledge base.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let knowledgeBaseId = "knowledgeBaseId_example"; // String | The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.removeKnowledgeBaseTemplateUri(knowledgeBaseId, opts, (error, data, response) => {
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
 **knowledgeBaseId** | **String**| The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
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


## searchContent

> SearchContentResponse searchContent(knowledgeBaseId, searchContentRequest, opts)



Searches for content in a specified knowledge base. Can be used to get a specific content resource by its name.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let knowledgeBaseId = "knowledgeBaseId_example"; // String | The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
let searchContentRequest = new AmazonConnectWisdomService.SearchContentRequest(); // SearchContentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'nextToken': "nextToken_example" // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
};
apiInstance.searchContent(knowledgeBaseId, searchContentRequest, opts, (error, data, response) => {
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
 **knowledgeBaseId** | **String**| The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **searchContentRequest** | [**SearchContentRequest**](SearchContentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 

### Return type

[**SearchContentResponse**](SearchContentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchSessions

> SearchSessionsResponse searchSessions(assistantId, searchContentRequest, opts)



Searches for sessions.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let assistantId = "assistantId_example"; // String | The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
let searchContentRequest = new AmazonConnectWisdomService.SearchContentRequest(); // SearchContentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'nextToken': "nextToken_example" // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
};
apiInstance.searchSessions(assistantId, searchContentRequest, opts, (error, data, response) => {
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
 **assistantId** | **String**| The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **searchContentRequest** | [**SearchContentRequest**](SearchContentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 

### Return type

[**SearchSessionsResponse**](SearchSessionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startContentUpload

> StartContentUploadResponse startContentUpload(knowledgeBaseId, startContentUploadRequest, opts)



Get a URL to upload content to a knowledge base. To upload content, first make a PUT request to the returned URL with your file, making sure to include the required headers. Then use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wisdom/latest/APIReference/API_CreateContent.html\&quot;&gt;CreateContent&lt;/a&gt; to finalize the content creation process or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wisdom/latest/APIReference/API_UpdateContent.html\&quot;&gt;UpdateContent&lt;/a&gt; to modify an existing resource. You can only upload content to a knowledge base of type CUSTOM.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let knowledgeBaseId = "knowledgeBaseId_example"; // String | The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
let startContentUploadRequest = new AmazonConnectWisdomService.StartContentUploadRequest(); // StartContentUploadRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startContentUpload(knowledgeBaseId, startContentUploadRequest, opts, (error, data, response) => {
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
 **knowledgeBaseId** | **String**| The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **startContentUploadRequest** | [**StartContentUploadRequest**](StartContentUploadRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartContentUploadResponse**](StartContentUploadResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



Adds the specified tags to the specified resource.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource.
let tagResourceRequest = new AmazonConnectWisdomService.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(resourceArn, tagResourceRequest, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource. | 
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

> Object untagResource(resourceArn, tagKeys, opts)



Removes the specified tags from the specified resource.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource.
let tagKeys = ["null"]; // [String] | The tag keys.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(resourceArn, tagKeys, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource. | 
 **tagKeys** | [**[String]**](String.md)| The tag keys. | 
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


## updateContent

> UpdateContentResponse updateContent(contentId, knowledgeBaseId, updateContentRequest, opts)



Updates information about the content.

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let contentId = "contentId_example"; // String | The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.
let knowledgeBaseId = "knowledgeBaseId_example"; // String | The identifier of the knowledge base. Can be either the ID or the ARN
let updateContentRequest = new AmazonConnectWisdomService.UpdateContentRequest(); // UpdateContentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateContent(contentId, knowledgeBaseId, updateContentRequest, opts, (error, data, response) => {
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
 **contentId** | **String**| The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **knowledgeBaseId** | **String**| The identifier of the knowledge base. Can be either the ID or the ARN | 
 **updateContentRequest** | [**UpdateContentRequest**](UpdateContentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateContentResponse**](UpdateContentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateKnowledgeBaseTemplateUri

> UpdateKnowledgeBaseTemplateUriResponse updateKnowledgeBaseTemplateUri(knowledgeBaseId, updateKnowledgeBaseTemplateUriRequest, opts)



Updates the template URI of a knowledge base. This is only supported for knowledge bases of type EXTERNAL. Include a single variable in &lt;code&gt;${variable}&lt;/code&gt; format; this interpolated by Wisdom using ingested content. For example, if you ingest a Salesforce article, it has an &lt;code&gt;Id&lt;/code&gt; value, and you can set the template URI to &lt;code&gt;https://myInstanceName.lightning.force.com/lightning/r/Knowledge__kav/_*${Id}*_/view&lt;/code&gt;. 

### Example

```javascript
import AmazonConnectWisdomService from 'amazon_connect_wisdom_service';
let defaultClient = AmazonConnectWisdomService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectWisdomService.DefaultApi();
let knowledgeBaseId = "knowledgeBaseId_example"; // String | The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
let updateKnowledgeBaseTemplateUriRequest = new AmazonConnectWisdomService.UpdateKnowledgeBaseTemplateUriRequest(); // UpdateKnowledgeBaseTemplateUriRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateKnowledgeBaseTemplateUri(knowledgeBaseId, updateKnowledgeBaseTemplateUriRequest, opts, (error, data, response) => {
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
 **knowledgeBaseId** | **String**| The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN. | 
 **updateKnowledgeBaseTemplateUriRequest** | [**UpdateKnowledgeBaseTemplateUriRequest**](UpdateKnowledgeBaseTemplateUriRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateKnowledgeBaseTemplateUriResponse**](UpdateKnowledgeBaseTemplateUriResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

