# AwsCleanRoomsService.DefaultApi

All URIs are relative to *http://cleanrooms.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchGetCollaborationAnalysisTemplate**](DefaultApi.md#batchGetCollaborationAnalysisTemplate) | **POST** /collaborations/{collaborationIdentifier}/batch-analysistemplates | 
[**batchGetSchema**](DefaultApi.md#batchGetSchema) | **POST** /collaborations/{collaborationIdentifier}/batch-schema | 
[**createAnalysisTemplate**](DefaultApi.md#createAnalysisTemplate) | **POST** /memberships/{membershipIdentifier}/analysistemplates | 
[**createCollaboration**](DefaultApi.md#createCollaboration) | **POST** /collaborations | 
[**createConfiguredTable**](DefaultApi.md#createConfiguredTable) | **POST** /configuredTables | 
[**createConfiguredTableAnalysisRule**](DefaultApi.md#createConfiguredTableAnalysisRule) | **POST** /configuredTables/{configuredTableIdentifier}/analysisRule | 
[**createConfiguredTableAssociation**](DefaultApi.md#createConfiguredTableAssociation) | **POST** /memberships/{membershipIdentifier}/configuredTableAssociations | 
[**createMembership**](DefaultApi.md#createMembership) | **POST** /memberships | 
[**deleteAnalysisTemplate**](DefaultApi.md#deleteAnalysisTemplate) | **DELETE** /memberships/{membershipIdentifier}/analysistemplates/{analysisTemplateIdentifier} | 
[**deleteCollaboration**](DefaultApi.md#deleteCollaboration) | **DELETE** /collaborations/{collaborationIdentifier} | 
[**deleteConfiguredTable**](DefaultApi.md#deleteConfiguredTable) | **DELETE** /configuredTables/{configuredTableIdentifier} | 
[**deleteConfiguredTableAnalysisRule**](DefaultApi.md#deleteConfiguredTableAnalysisRule) | **DELETE** /configuredTables/{configuredTableIdentifier}/analysisRule/{analysisRuleType} | 
[**deleteConfiguredTableAssociation**](DefaultApi.md#deleteConfiguredTableAssociation) | **DELETE** /memberships/{membershipIdentifier}/configuredTableAssociations/{configuredTableAssociationIdentifier} | 
[**deleteMember**](DefaultApi.md#deleteMember) | **DELETE** /collaborations/{collaborationIdentifier}/member/{accountId} | 
[**deleteMembership**](DefaultApi.md#deleteMembership) | **DELETE** /memberships/{membershipIdentifier} | 
[**getAnalysisTemplate**](DefaultApi.md#getAnalysisTemplate) | **GET** /memberships/{membershipIdentifier}/analysistemplates/{analysisTemplateIdentifier} | 
[**getCollaboration**](DefaultApi.md#getCollaboration) | **GET** /collaborations/{collaborationIdentifier} | 
[**getCollaborationAnalysisTemplate**](DefaultApi.md#getCollaborationAnalysisTemplate) | **GET** /collaborations/{collaborationIdentifier}/analysistemplates/{analysisTemplateArn} | 
[**getConfiguredTable**](DefaultApi.md#getConfiguredTable) | **GET** /configuredTables/{configuredTableIdentifier} | 
[**getConfiguredTableAnalysisRule**](DefaultApi.md#getConfiguredTableAnalysisRule) | **GET** /configuredTables/{configuredTableIdentifier}/analysisRule/{analysisRuleType} | 
[**getConfiguredTableAssociation**](DefaultApi.md#getConfiguredTableAssociation) | **GET** /memberships/{membershipIdentifier}/configuredTableAssociations/{configuredTableAssociationIdentifier} | 
[**getMembership**](DefaultApi.md#getMembership) | **GET** /memberships/{membershipIdentifier} | 
[**getProtectedQuery**](DefaultApi.md#getProtectedQuery) | **GET** /memberships/{membershipIdentifier}/protectedQueries/{protectedQueryIdentifier} | 
[**getSchema**](DefaultApi.md#getSchema) | **GET** /collaborations/{collaborationIdentifier}/schemas/{name} | 
[**getSchemaAnalysisRule**](DefaultApi.md#getSchemaAnalysisRule) | **GET** /collaborations/{collaborationIdentifier}/schemas/{name}/analysisRule/{type} | 
[**listAnalysisTemplates**](DefaultApi.md#listAnalysisTemplates) | **GET** /memberships/{membershipIdentifier}/analysistemplates | 
[**listCollaborationAnalysisTemplates**](DefaultApi.md#listCollaborationAnalysisTemplates) | **GET** /collaborations/{collaborationIdentifier}/analysistemplates | 
[**listCollaborations**](DefaultApi.md#listCollaborations) | **GET** /collaborations | 
[**listConfiguredTableAssociations**](DefaultApi.md#listConfiguredTableAssociations) | **GET** /memberships/{membershipIdentifier}/configuredTableAssociations | 
[**listConfiguredTables**](DefaultApi.md#listConfiguredTables) | **GET** /configuredTables | 
[**listMembers**](DefaultApi.md#listMembers) | **GET** /collaborations/{collaborationIdentifier}/members | 
[**listMemberships**](DefaultApi.md#listMemberships) | **GET** /memberships | 
[**listProtectedQueries**](DefaultApi.md#listProtectedQueries) | **GET** /memberships/{membershipIdentifier}/protectedQueries | 
[**listSchemas**](DefaultApi.md#listSchemas) | **GET** /collaborations/{collaborationIdentifier}/schemas | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**startProtectedQuery**](DefaultApi.md#startProtectedQuery) | **POST** /memberships/{membershipIdentifier}/protectedQueries | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
[**updateAnalysisTemplate**](DefaultApi.md#updateAnalysisTemplate) | **PATCH** /memberships/{membershipIdentifier}/analysistemplates/{analysisTemplateIdentifier} | 
[**updateCollaboration**](DefaultApi.md#updateCollaboration) | **PATCH** /collaborations/{collaborationIdentifier} | 
[**updateConfiguredTable**](DefaultApi.md#updateConfiguredTable) | **PATCH** /configuredTables/{configuredTableIdentifier} | 
[**updateConfiguredTableAnalysisRule**](DefaultApi.md#updateConfiguredTableAnalysisRule) | **PATCH** /configuredTables/{configuredTableIdentifier}/analysisRule/{analysisRuleType} | 
[**updateConfiguredTableAssociation**](DefaultApi.md#updateConfiguredTableAssociation) | **PATCH** /memberships/{membershipIdentifier}/configuredTableAssociations/{configuredTableAssociationIdentifier} | 
[**updateMembership**](DefaultApi.md#updateMembership) | **PATCH** /memberships/{membershipIdentifier} | 
[**updateProtectedQuery**](DefaultApi.md#updateProtectedQuery) | **PATCH** /memberships/{membershipIdentifier}/protectedQueries/{protectedQueryIdentifier} | 



## batchGetCollaborationAnalysisTemplate

> BatchGetCollaborationAnalysisTemplateOutput batchGetCollaborationAnalysisTemplate(collaborationIdentifier, batchGetCollaborationAnalysisTemplateRequest, opts)



Retrieves multiple analysis templates within a collaboration by their Amazon Resource Names (ARNs).

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let collaborationIdentifier = "collaborationIdentifier_example"; // String | A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.
let batchGetCollaborationAnalysisTemplateRequest = new AwsCleanRoomsService.BatchGetCollaborationAnalysisTemplateRequest(); // BatchGetCollaborationAnalysisTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchGetCollaborationAnalysisTemplate(collaborationIdentifier, batchGetCollaborationAnalysisTemplateRequest, opts, (error, data, response) => {
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
 **collaborationIdentifier** | **String**| A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID. | 
 **batchGetCollaborationAnalysisTemplateRequest** | [**BatchGetCollaborationAnalysisTemplateRequest**](BatchGetCollaborationAnalysisTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchGetCollaborationAnalysisTemplateOutput**](BatchGetCollaborationAnalysisTemplateOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchGetSchema

> BatchGetSchemaOutput batchGetSchema(collaborationIdentifier, batchGetSchemaRequest, opts)



Retrieves multiple schemas by their identifiers.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let collaborationIdentifier = "collaborationIdentifier_example"; // String | A unique identifier for the collaboration that the schemas belong to. Currently accepts collaboration ID.
let batchGetSchemaRequest = new AwsCleanRoomsService.BatchGetSchemaRequest(); // BatchGetSchemaRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchGetSchema(collaborationIdentifier, batchGetSchemaRequest, opts, (error, data, response) => {
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
 **collaborationIdentifier** | **String**| A unique identifier for the collaboration that the schemas belong to. Currently accepts collaboration ID. | 
 **batchGetSchemaRequest** | [**BatchGetSchemaRequest**](BatchGetSchemaRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchGetSchemaOutput**](BatchGetSchemaOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAnalysisTemplate

> CreateAnalysisTemplateOutput createAnalysisTemplate(membershipIdentifier, createAnalysisTemplateRequest, opts)



Creates a new analysis template.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let membershipIdentifier = "membershipIdentifier_example"; // String | The identifier for a membership resource.
let createAnalysisTemplateRequest = new AwsCleanRoomsService.CreateAnalysisTemplateRequest(); // CreateAnalysisTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAnalysisTemplate(membershipIdentifier, createAnalysisTemplateRequest, opts, (error, data, response) => {
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
 **membershipIdentifier** | **String**| The identifier for a membership resource. | 
 **createAnalysisTemplateRequest** | [**CreateAnalysisTemplateRequest**](CreateAnalysisTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAnalysisTemplateOutput**](CreateAnalysisTemplateOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createCollaboration

> CreateCollaborationOutput createCollaboration(createCollaborationRequest, opts)



Creates a new collaboration.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let createCollaborationRequest = new AwsCleanRoomsService.CreateCollaborationRequest(); // CreateCollaborationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createCollaboration(createCollaborationRequest, opts, (error, data, response) => {
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
 **createCollaborationRequest** | [**CreateCollaborationRequest**](CreateCollaborationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateCollaborationOutput**](CreateCollaborationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createConfiguredTable

> CreateConfiguredTableOutput createConfiguredTable(createConfiguredTableRequest, opts)



Creates a new configured table resource.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let createConfiguredTableRequest = new AwsCleanRoomsService.CreateConfiguredTableRequest(); // CreateConfiguredTableRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createConfiguredTable(createConfiguredTableRequest, opts, (error, data, response) => {
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
 **createConfiguredTableRequest** | [**CreateConfiguredTableRequest**](CreateConfiguredTableRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateConfiguredTableOutput**](CreateConfiguredTableOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createConfiguredTableAnalysisRule

> CreateConfiguredTableAnalysisRuleOutput createConfiguredTableAnalysisRule(configuredTableIdentifier, createConfiguredTableAnalysisRuleRequest, opts)



Creates a new analysis rule for a configured table. Currently, only one analysis rule can be created for a given configured table.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let configuredTableIdentifier = "configuredTableIdentifier_example"; // String | The identifier for the configured table to create the analysis rule for. Currently accepts the configured table ID. 
let createConfiguredTableAnalysisRuleRequest = new AwsCleanRoomsService.CreateConfiguredTableAnalysisRuleRequest(); // CreateConfiguredTableAnalysisRuleRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createConfiguredTableAnalysisRule(configuredTableIdentifier, createConfiguredTableAnalysisRuleRequest, opts, (error, data, response) => {
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
 **configuredTableIdentifier** | **String**| The identifier for the configured table to create the analysis rule for. Currently accepts the configured table ID.  | 
 **createConfiguredTableAnalysisRuleRequest** | [**CreateConfiguredTableAnalysisRuleRequest**](CreateConfiguredTableAnalysisRuleRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateConfiguredTableAnalysisRuleOutput**](CreateConfiguredTableAnalysisRuleOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createConfiguredTableAssociation

> CreateConfiguredTableAssociationOutput createConfiguredTableAssociation(membershipIdentifier, createConfiguredTableAssociationRequest, opts)



Creates a configured table association. A configured table association links a configured table with a collaboration.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let membershipIdentifier = "membershipIdentifier_example"; // String | A unique identifier for one of your memberships for a collaboration. The configured table is associated to the collaboration that this membership belongs to. Currently accepts a membership ID.
let createConfiguredTableAssociationRequest = new AwsCleanRoomsService.CreateConfiguredTableAssociationRequest(); // CreateConfiguredTableAssociationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createConfiguredTableAssociation(membershipIdentifier, createConfiguredTableAssociationRequest, opts, (error, data, response) => {
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
 **membershipIdentifier** | **String**| A unique identifier for one of your memberships for a collaboration. The configured table is associated to the collaboration that this membership belongs to. Currently accepts a membership ID. | 
 **createConfiguredTableAssociationRequest** | [**CreateConfiguredTableAssociationRequest**](CreateConfiguredTableAssociationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateConfiguredTableAssociationOutput**](CreateConfiguredTableAssociationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMembership

> CreateMembershipOutput createMembership(createMembershipRequest, opts)



Creates a membership for a specific collaboration identifier and joins the collaboration.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let createMembershipRequest = new AwsCleanRoomsService.CreateMembershipRequest(); // CreateMembershipRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMembership(createMembershipRequest, opts, (error, data, response) => {
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
 **createMembershipRequest** | [**CreateMembershipRequest**](CreateMembershipRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMembershipOutput**](CreateMembershipOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAnalysisTemplate

> Object deleteAnalysisTemplate(membershipIdentifier, analysisTemplateIdentifier, opts)



Deletes an analysis template.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let membershipIdentifier = "membershipIdentifier_example"; // String | The identifier for a membership resource.
let analysisTemplateIdentifier = "analysisTemplateIdentifier_example"; // String | The identifier for the analysis template resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAnalysisTemplate(membershipIdentifier, analysisTemplateIdentifier, opts, (error, data, response) => {
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
 **membershipIdentifier** | **String**| The identifier for a membership resource. | 
 **analysisTemplateIdentifier** | **String**| The identifier for the analysis template resource. | 
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


## deleteCollaboration

> Object deleteCollaboration(collaborationIdentifier, opts)



Deletes a collaboration. It can only be called by the collaboration owner.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let collaborationIdentifier = "collaborationIdentifier_example"; // String | The identifier for the collaboration.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteCollaboration(collaborationIdentifier, opts, (error, data, response) => {
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
 **collaborationIdentifier** | **String**| The identifier for the collaboration. | 
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


## deleteConfiguredTable

> Object deleteConfiguredTable(configuredTableIdentifier, opts)



Deletes a configured table.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let configuredTableIdentifier = "configuredTableIdentifier_example"; // String | The unique ID for the configured table to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteConfiguredTable(configuredTableIdentifier, opts, (error, data, response) => {
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
 **configuredTableIdentifier** | **String**| The unique ID for the configured table to delete. | 
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


## deleteConfiguredTableAnalysisRule

> Object deleteConfiguredTableAnalysisRule(configuredTableIdentifier, analysisRuleType, opts)



Deletes a configured table analysis rule.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let configuredTableIdentifier = "configuredTableIdentifier_example"; // String | The unique identifier for the configured table that the analysis rule applies to. Currently accepts the configured table ID.
let analysisRuleType = "analysisRuleType_example"; // String | The analysis rule type to be deleted. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteConfiguredTableAnalysisRule(configuredTableIdentifier, analysisRuleType, opts, (error, data, response) => {
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
 **configuredTableIdentifier** | **String**| The unique identifier for the configured table that the analysis rule applies to. Currently accepts the configured table ID. | 
 **analysisRuleType** | **String**| The analysis rule type to be deleted. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type. | 
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


## deleteConfiguredTableAssociation

> Object deleteConfiguredTableAssociation(configuredTableAssociationIdentifier, membershipIdentifier, opts)



Deletes a configured table association.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let configuredTableAssociationIdentifier = "configuredTableAssociationIdentifier_example"; // String | The unique ID for the configured table association to be deleted. Currently accepts the configured table ID.
let membershipIdentifier = "membershipIdentifier_example"; // String | A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteConfiguredTableAssociation(configuredTableAssociationIdentifier, membershipIdentifier, opts, (error, data, response) => {
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
 **configuredTableAssociationIdentifier** | **String**| The unique ID for the configured table association to be deleted. Currently accepts the configured table ID. | 
 **membershipIdentifier** | **String**| A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID. | 
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


## deleteMember

> Object deleteMember(collaborationIdentifier, accountId, opts)



Removes the specified member from a collaboration. The removed member is placed in the Removed status and can&#39;t interact with the collaboration. The removed member&#39;s data is inaccessible to active members of the collaboration.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let collaborationIdentifier = "collaborationIdentifier_example"; // String | The unique identifier for the associated collaboration.
let accountId = "accountId_example"; // String | The account ID of the member to remove.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteMember(collaborationIdentifier, accountId, opts, (error, data, response) => {
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
 **collaborationIdentifier** | **String**| The unique identifier for the associated collaboration. | 
 **accountId** | **String**| The account ID of the member to remove. | 
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


## deleteMembership

> Object deleteMembership(membershipIdentifier, opts)



Deletes a specified membership. All resources under a membership must be deleted.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let membershipIdentifier = "membershipIdentifier_example"; // String | The identifier for a membership resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteMembership(membershipIdentifier, opts, (error, data, response) => {
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
 **membershipIdentifier** | **String**| The identifier for a membership resource. | 
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


## getAnalysisTemplate

> GetAnalysisTemplateOutput getAnalysisTemplate(membershipIdentifier, analysisTemplateIdentifier, opts)



Retrieves an analysis template.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let membershipIdentifier = "membershipIdentifier_example"; // String | The identifier for a membership resource.
let analysisTemplateIdentifier = "analysisTemplateIdentifier_example"; // String | The identifier for the analysis template resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAnalysisTemplate(membershipIdentifier, analysisTemplateIdentifier, opts, (error, data, response) => {
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
 **membershipIdentifier** | **String**| The identifier for a membership resource. | 
 **analysisTemplateIdentifier** | **String**| The identifier for the analysis template resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAnalysisTemplateOutput**](GetAnalysisTemplateOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCollaboration

> GetCollaborationOutput getCollaboration(collaborationIdentifier, opts)



Returns metadata about a collaboration.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let collaborationIdentifier = "collaborationIdentifier_example"; // String | The identifier for the collaboration.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getCollaboration(collaborationIdentifier, opts, (error, data, response) => {
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
 **collaborationIdentifier** | **String**| The identifier for the collaboration. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetCollaborationOutput**](GetCollaborationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCollaborationAnalysisTemplate

> GetCollaborationAnalysisTemplateOutput getCollaborationAnalysisTemplate(collaborationIdentifier, analysisTemplateArn, opts)



Retrieves an analysis template within a collaboration.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let collaborationIdentifier = "collaborationIdentifier_example"; // String | A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.
let analysisTemplateArn = "analysisTemplateArn_example"; // String | The Amazon Resource Name (ARN) associated with the analysis template within a collaboration.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getCollaborationAnalysisTemplate(collaborationIdentifier, analysisTemplateArn, opts, (error, data, response) => {
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
 **collaborationIdentifier** | **String**| A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID. | 
 **analysisTemplateArn** | **String**| The Amazon Resource Name (ARN) associated with the analysis template within a collaboration. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetCollaborationAnalysisTemplateOutput**](GetCollaborationAnalysisTemplateOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getConfiguredTable

> GetConfiguredTableOutput getConfiguredTable(configuredTableIdentifier, opts)



Retrieves a configured table.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let configuredTableIdentifier = "configuredTableIdentifier_example"; // String | The unique ID for the configured table to retrieve.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getConfiguredTable(configuredTableIdentifier, opts, (error, data, response) => {
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
 **configuredTableIdentifier** | **String**| The unique ID for the configured table to retrieve. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetConfiguredTableOutput**](GetConfiguredTableOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getConfiguredTableAnalysisRule

> GetConfiguredTableAnalysisRuleOutput getConfiguredTableAnalysisRule(configuredTableIdentifier, analysisRuleType, opts)



Retrieves a configured table analysis rule.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let configuredTableIdentifier = "configuredTableIdentifier_example"; // String | The unique identifier for the configured table to retrieve. Currently accepts the configured table ID.
let analysisRuleType = "analysisRuleType_example"; // String | The analysis rule to be retrieved. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getConfiguredTableAnalysisRule(configuredTableIdentifier, analysisRuleType, opts, (error, data, response) => {
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
 **configuredTableIdentifier** | **String**| The unique identifier for the configured table to retrieve. Currently accepts the configured table ID. | 
 **analysisRuleType** | **String**| The analysis rule to be retrieved. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetConfiguredTableAnalysisRuleOutput**](GetConfiguredTableAnalysisRuleOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getConfiguredTableAssociation

> GetConfiguredTableAssociationOutput getConfiguredTableAssociation(configuredTableAssociationIdentifier, membershipIdentifier, opts)



Retrieves a configured table association.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let configuredTableAssociationIdentifier = "configuredTableAssociationIdentifier_example"; // String | The unique ID for the configured table association to retrieve. Currently accepts the configured table ID.
let membershipIdentifier = "membershipIdentifier_example"; // String | A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getConfiguredTableAssociation(configuredTableAssociationIdentifier, membershipIdentifier, opts, (error, data, response) => {
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
 **configuredTableAssociationIdentifier** | **String**| The unique ID for the configured table association to retrieve. Currently accepts the configured table ID. | 
 **membershipIdentifier** | **String**| A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetConfiguredTableAssociationOutput**](GetConfiguredTableAssociationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMembership

> GetMembershipOutput getMembership(membershipIdentifier, opts)



Retrieves a specified membership for an identifier.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let membershipIdentifier = "membershipIdentifier_example"; // String | The identifier for a membership resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMembership(membershipIdentifier, opts, (error, data, response) => {
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
 **membershipIdentifier** | **String**| The identifier for a membership resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMembershipOutput**](GetMembershipOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProtectedQuery

> GetProtectedQueryOutput getProtectedQuery(membershipIdentifier, protectedQueryIdentifier, opts)



Returns query processing metadata.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let membershipIdentifier = "membershipIdentifier_example"; // String | The identifier for a membership in a protected query instance.
let protectedQueryIdentifier = "protectedQueryIdentifier_example"; // String | The identifier for a protected query instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getProtectedQuery(membershipIdentifier, protectedQueryIdentifier, opts, (error, data, response) => {
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
 **membershipIdentifier** | **String**| The identifier for a membership in a protected query instance. | 
 **protectedQueryIdentifier** | **String**| The identifier for a protected query instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetProtectedQueryOutput**](GetProtectedQueryOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSchema

> GetSchemaOutput getSchema(collaborationIdentifier, name, opts)



Retrieves the schema for a relation within a collaboration.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let collaborationIdentifier = "collaborationIdentifier_example"; // String | A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.
let name = "name_example"; // String | The name of the relation to retrieve the schema for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSchema(collaborationIdentifier, name, opts, (error, data, response) => {
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
 **collaborationIdentifier** | **String**| A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID. | 
 **name** | **String**| The name of the relation to retrieve the schema for. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSchemaOutput**](GetSchemaOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSchemaAnalysisRule

> GetSchemaAnalysisRuleOutput getSchemaAnalysisRule(collaborationIdentifier, name, type, opts)



Retrieves a schema analysis rule.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let collaborationIdentifier = "collaborationIdentifier_example"; // String | A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.
let name = "name_example"; // String | The name of the schema to retrieve the analysis rule for.
let type = "type_example"; // String | The type of the schema analysis rule to retrieve. Schema analysis rules are uniquely identified by a combination of the collaboration, the schema name, and their type.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSchemaAnalysisRule(collaborationIdentifier, name, type, opts, (error, data, response) => {
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
 **collaborationIdentifier** | **String**| A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID. | 
 **name** | **String**| The name of the schema to retrieve the analysis rule for. | 
 **type** | **String**| The type of the schema analysis rule to retrieve. Schema analysis rules are uniquely identified by a combination of the collaboration, the schema name, and their type. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSchemaAnalysisRuleOutput**](GetSchemaAnalysisRuleOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAnalysisTemplates

> ListAnalysisTemplatesOutput listAnalysisTemplates(membershipIdentifier, opts)



Lists analysis templates that the caller owns.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let membershipIdentifier = "membershipIdentifier_example"; // String | The identifier for a membership resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token value retrieved from a previous call to access the next page of results.
  'maxResults': 56 // Number | The maximum size of the results that is returned per call.
};
apiInstance.listAnalysisTemplates(membershipIdentifier, opts, (error, data, response) => {
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
 **membershipIdentifier** | **String**| The identifier for a membership resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token value retrieved from a previous call to access the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum size of the results that is returned per call. | [optional] 

### Return type

[**ListAnalysisTemplatesOutput**](ListAnalysisTemplatesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCollaborationAnalysisTemplates

> ListCollaborationAnalysisTemplatesOutput listCollaborationAnalysisTemplates(collaborationIdentifier, opts)



Lists analysis templates within a collaboration.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let collaborationIdentifier = "collaborationIdentifier_example"; // String | A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token value retrieved from a previous call to access the next page of results.
  'maxResults': 56 // Number | The maximum size of the results that is returned per call.
};
apiInstance.listCollaborationAnalysisTemplates(collaborationIdentifier, opts, (error, data, response) => {
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
 **collaborationIdentifier** | **String**| A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token value retrieved from a previous call to access the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum size of the results that is returned per call. | [optional] 

### Return type

[**ListCollaborationAnalysisTemplatesOutput**](ListCollaborationAnalysisTemplatesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCollaborations

> ListCollaborationsOutput listCollaborations(opts)



Lists collaborations the caller owns, is active in, or has been invited to.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token value retrieved from a previous call to access the next page of results.
  'maxResults': 56, // Number | The maximum size of the results that is returned per call. Service chooses a default if it has not been set. Service may return a nextToken even if the maximum results has not been met.
  'memberStatus': "memberStatus_example" // String | The caller's status in a collaboration.
};
apiInstance.listCollaborations(opts, (error, data, response) => {
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
 **nextToken** | **String**| The token value retrieved from a previous call to access the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum size of the results that is returned per call. Service chooses a default if it has not been set. Service may return a nextToken even if the maximum results has not been met. | [optional] 
 **memberStatus** | **String**| The caller&#39;s status in a collaboration. | [optional] 

### Return type

[**ListCollaborationsOutput**](ListCollaborationsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConfiguredTableAssociations

> ListConfiguredTableAssociationsOutput listConfiguredTableAssociations(membershipIdentifier, opts)



Lists configured table associations for a membership.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let membershipIdentifier = "membershipIdentifier_example"; // String | A unique identifier for the membership to list configured table associations for. Currently accepts the membership ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token value retrieved from a previous call to access the next page of results.
  'maxResults': 56 // Number | The maximum size of the results that is returned per call.
};
apiInstance.listConfiguredTableAssociations(membershipIdentifier, opts, (error, data, response) => {
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
 **membershipIdentifier** | **String**| A unique identifier for the membership to list configured table associations for. Currently accepts the membership ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token value retrieved from a previous call to access the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum size of the results that is returned per call. | [optional] 

### Return type

[**ListConfiguredTableAssociationsOutput**](ListConfiguredTableAssociationsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConfiguredTables

> ListConfiguredTablesOutput listConfiguredTables(opts)



Lists configured tables.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token value retrieved from a previous call to access the next page of results.
  'maxResults': 56 // Number | The maximum size of the results that is returned per call.
};
apiInstance.listConfiguredTables(opts, (error, data, response) => {
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
 **nextToken** | **String**| The token value retrieved from a previous call to access the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum size of the results that is returned per call. | [optional] 

### Return type

[**ListConfiguredTablesOutput**](ListConfiguredTablesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMembers

> ListMembersOutput listMembers(collaborationIdentifier, opts)



Lists all members within a collaboration.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let collaborationIdentifier = "collaborationIdentifier_example"; // String | The identifier of the collaboration in which the members are listed.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token value retrieved from a previous call to access the next page of results.
  'maxResults': 56 // Number | The maximum size of the results that is returned per call.
};
apiInstance.listMembers(collaborationIdentifier, opts, (error, data, response) => {
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
 **collaborationIdentifier** | **String**| The identifier of the collaboration in which the members are listed. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token value retrieved from a previous call to access the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum size of the results that is returned per call. | [optional] 

### Return type

[**ListMembersOutput**](ListMembersOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMemberships

> ListMembershipsOutput listMemberships(opts)



Lists all memberships resources within the caller&#39;s account.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token value retrieved from a previous call to access the next page of results.
  'maxResults': 56, // Number | The maximum size of the results that is returned per call.
  'status': "status_example" // String | A filter which will return only memberships in the specified status.
};
apiInstance.listMemberships(opts, (error, data, response) => {
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
 **nextToken** | **String**| The token value retrieved from a previous call to access the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum size of the results that is returned per call. | [optional] 
 **status** | **String**| A filter which will return only memberships in the specified status. | [optional] 

### Return type

[**ListMembershipsOutput**](ListMembershipsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listProtectedQueries

> ListProtectedQueriesOutput listProtectedQueries(membershipIdentifier, opts)



Lists protected queries, sorted by the most recent query.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let membershipIdentifier = "membershipIdentifier_example"; // String | The identifier for the membership in the collaboration.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'status': "status_example", // String | A filter on the status of the protected query.
  'nextToken': "nextToken_example", // String | The token value retrieved from a previous call to access the next page of results.
  'maxResults': 56 // Number | The maximum size of the results that is returned per call. Service chooses a default if it has not been set. Service can return a nextToken even if the maximum results has not been met. 
};
apiInstance.listProtectedQueries(membershipIdentifier, opts, (error, data, response) => {
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
 **membershipIdentifier** | **String**| The identifier for the membership in the collaboration. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **status** | **String**| A filter on the status of the protected query. | [optional] 
 **nextToken** | **String**| The token value retrieved from a previous call to access the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum size of the results that is returned per call. Service chooses a default if it has not been set. Service can return a nextToken even if the maximum results has not been met.  | [optional] 

### Return type

[**ListProtectedQueriesOutput**](ListProtectedQueriesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSchemas

> ListSchemasOutput listSchemas(collaborationIdentifier, opts)



Lists the schemas for relations within a collaboration.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let collaborationIdentifier = "collaborationIdentifier_example"; // String | A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'schemaType': "schemaType_example", // String | If present, filter schemas by schema type. The only valid schema type is currently `TABLE`.
  'nextToken': "nextToken_example", // String | The token value retrieved from a previous call to access the next page of results.
  'maxResults': 56 // Number | The maximum size of the results that is returned per call.
};
apiInstance.listSchemas(collaborationIdentifier, opts, (error, data, response) => {
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
 **collaborationIdentifier** | **String**| A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **schemaType** | **String**| If present, filter schemas by schema type. The only valid schema type is currently &#x60;TABLE&#x60;. | [optional] 
 **nextToken** | **String**| The token value retrieved from a previous call to access the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum size of the results that is returned per call. | [optional] 

### Return type

[**ListSchemasOutput**](ListSchemasOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceOutput listTagsForResource(resourceArn, opts)



Lists all of the tags that have been added to a resource.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) associated with the resource you want to list tags on.
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) associated with the resource you want to list tags on. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceOutput**](ListTagsForResourceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startProtectedQuery

> StartProtectedQueryOutput startProtectedQuery(membershipIdentifier, startProtectedQueryRequest, opts)



Creates a protected query that is started by Clean Rooms .

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let membershipIdentifier = "membershipIdentifier_example"; // String | A unique identifier for the membership to run this query against. Currently accepts a membership ID.
let startProtectedQueryRequest = new AwsCleanRoomsService.StartProtectedQueryRequest(); // StartProtectedQueryRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startProtectedQuery(membershipIdentifier, startProtectedQueryRequest, opts, (error, data, response) => {
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
 **membershipIdentifier** | **String**| A unique identifier for the membership to run this query against. Currently accepts a membership ID. | 
 **startProtectedQueryRequest** | [**StartProtectedQueryRequest**](StartProtectedQueryRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartProtectedQueryOutput**](StartProtectedQueryOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



Tags a resource.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) associated with the resource you want to tag.
let tagResourceRequest = new AwsCleanRoomsService.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) associated with the resource you want to tag. | 
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



Removes a tag or list of tags from a resource.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) associated with the resource you want to remove the tag from.
let tagKeys = ["null"]; // [String] | A list of key names of tags to be removed.
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) associated with the resource you want to remove the tag from. | 
 **tagKeys** | [**[String]**](String.md)| A list of key names of tags to be removed. | 
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


## updateAnalysisTemplate

> UpdateAnalysisTemplateOutput updateAnalysisTemplate(membershipIdentifier, analysisTemplateIdentifier, updateAnalysisTemplateRequest, opts)



Updates the analysis template metadata.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let membershipIdentifier = "membershipIdentifier_example"; // String | The identifier for a membership resource.
let analysisTemplateIdentifier = "analysisTemplateIdentifier_example"; // String | The identifier for the analysis template resource.
let updateAnalysisTemplateRequest = new AwsCleanRoomsService.UpdateAnalysisTemplateRequest(); // UpdateAnalysisTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAnalysisTemplate(membershipIdentifier, analysisTemplateIdentifier, updateAnalysisTemplateRequest, opts, (error, data, response) => {
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
 **membershipIdentifier** | **String**| The identifier for a membership resource. | 
 **analysisTemplateIdentifier** | **String**| The identifier for the analysis template resource. | 
 **updateAnalysisTemplateRequest** | [**UpdateAnalysisTemplateRequest**](UpdateAnalysisTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAnalysisTemplateOutput**](UpdateAnalysisTemplateOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCollaboration

> UpdateCollaborationOutput updateCollaboration(collaborationIdentifier, updateCollaborationRequest, opts)



Updates collaboration metadata and can only be called by the collaboration owner.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let collaborationIdentifier = "collaborationIdentifier_example"; // String | The identifier for the collaboration.
let updateCollaborationRequest = new AwsCleanRoomsService.UpdateCollaborationRequest(); // UpdateCollaborationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateCollaboration(collaborationIdentifier, updateCollaborationRequest, opts, (error, data, response) => {
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
 **collaborationIdentifier** | **String**| The identifier for the collaboration. | 
 **updateCollaborationRequest** | [**UpdateCollaborationRequest**](UpdateCollaborationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateCollaborationOutput**](UpdateCollaborationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateConfiguredTable

> UpdateConfiguredTableOutput updateConfiguredTable(configuredTableIdentifier, updateConfiguredTableRequest, opts)



Updates a configured table.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let configuredTableIdentifier = "configuredTableIdentifier_example"; // String | The identifier for the configured table to update. Currently accepts the configured table ID.
let updateConfiguredTableRequest = new AwsCleanRoomsService.UpdateConfiguredTableRequest(); // UpdateConfiguredTableRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateConfiguredTable(configuredTableIdentifier, updateConfiguredTableRequest, opts, (error, data, response) => {
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
 **configuredTableIdentifier** | **String**| The identifier for the configured table to update. Currently accepts the configured table ID. | 
 **updateConfiguredTableRequest** | [**UpdateConfiguredTableRequest**](UpdateConfiguredTableRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateConfiguredTableOutput**](UpdateConfiguredTableOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateConfiguredTableAnalysisRule

> UpdateConfiguredTableAnalysisRuleOutput updateConfiguredTableAnalysisRule(configuredTableIdentifier, analysisRuleType, updateConfiguredTableAnalysisRuleRequest, opts)



Updates a configured table analysis rule.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let configuredTableIdentifier = "configuredTableIdentifier_example"; // String | The unique identifier for the configured table that the analysis rule applies to. Currently accepts the configured table ID.
let analysisRuleType = "analysisRuleType_example"; // String | The analysis rule type to be updated. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.
let updateConfiguredTableAnalysisRuleRequest = new AwsCleanRoomsService.UpdateConfiguredTableAnalysisRuleRequest(); // UpdateConfiguredTableAnalysisRuleRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateConfiguredTableAnalysisRule(configuredTableIdentifier, analysisRuleType, updateConfiguredTableAnalysisRuleRequest, opts, (error, data, response) => {
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
 **configuredTableIdentifier** | **String**| The unique identifier for the configured table that the analysis rule applies to. Currently accepts the configured table ID. | 
 **analysisRuleType** | **String**| The analysis rule type to be updated. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type. | 
 **updateConfiguredTableAnalysisRuleRequest** | [**UpdateConfiguredTableAnalysisRuleRequest**](UpdateConfiguredTableAnalysisRuleRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateConfiguredTableAnalysisRuleOutput**](UpdateConfiguredTableAnalysisRuleOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateConfiguredTableAssociation

> UpdateConfiguredTableAssociationOutput updateConfiguredTableAssociation(configuredTableAssociationIdentifier, membershipIdentifier, updateConfiguredTableAssociationRequest, opts)



Updates a configured table association.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let configuredTableAssociationIdentifier = "configuredTableAssociationIdentifier_example"; // String | The unique identifier for the configured table association to update. Currently accepts the configured table association ID.
let membershipIdentifier = "membershipIdentifier_example"; // String | The unique ID for the membership that the configured table association belongs to.
let updateConfiguredTableAssociationRequest = new AwsCleanRoomsService.UpdateConfiguredTableAssociationRequest(); // UpdateConfiguredTableAssociationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateConfiguredTableAssociation(configuredTableAssociationIdentifier, membershipIdentifier, updateConfiguredTableAssociationRequest, opts, (error, data, response) => {
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
 **configuredTableAssociationIdentifier** | **String**| The unique identifier for the configured table association to update. Currently accepts the configured table association ID. | 
 **membershipIdentifier** | **String**| The unique ID for the membership that the configured table association belongs to. | 
 **updateConfiguredTableAssociationRequest** | [**UpdateConfiguredTableAssociationRequest**](UpdateConfiguredTableAssociationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateConfiguredTableAssociationOutput**](UpdateConfiguredTableAssociationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMembership

> UpdateMembershipOutput updateMembership(membershipIdentifier, updateMembershipRequest, opts)



Updates a membership.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let membershipIdentifier = "membershipIdentifier_example"; // String | The unique identifier of the membership.
let updateMembershipRequest = new AwsCleanRoomsService.UpdateMembershipRequest(); // UpdateMembershipRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateMembership(membershipIdentifier, updateMembershipRequest, opts, (error, data, response) => {
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
 **membershipIdentifier** | **String**| The unique identifier of the membership. | 
 **updateMembershipRequest** | [**UpdateMembershipRequest**](UpdateMembershipRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateMembershipOutput**](UpdateMembershipOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateProtectedQuery

> UpdateProtectedQueryOutput updateProtectedQuery(membershipIdentifier, protectedQueryIdentifier, updateProtectedQueryRequest, opts)



Updates the processing of a currently running query.

### Example

```javascript
import AwsCleanRoomsService from 'aws_clean_rooms_service';
let defaultClient = AwsCleanRoomsService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsCleanRoomsService.DefaultApi();
let membershipIdentifier = "membershipIdentifier_example"; // String | The identifier for a member of a protected query instance.
let protectedQueryIdentifier = "protectedQueryIdentifier_example"; // String | The identifier for a protected query instance.
let updateProtectedQueryRequest = new AwsCleanRoomsService.UpdateProtectedQueryRequest(); // UpdateProtectedQueryRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateProtectedQuery(membershipIdentifier, protectedQueryIdentifier, updateProtectedQueryRequest, opts, (error, data, response) => {
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
 **membershipIdentifier** | **String**| The identifier for a member of a protected query instance. | 
 **protectedQueryIdentifier** | **String**| The identifier for a protected query instance. | 
 **updateProtectedQueryRequest** | [**UpdateProtectedQueryRequest**](UpdateProtectedQueryRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateProtectedQueryOutput**](UpdateProtectedQueryOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

