# AmazonLexModelBuildingService.DefaultApi

All URIs are relative to *http://models.lex.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createBotVersion**](DefaultApi.md#createBotVersion) | **POST** /bots/{name}/versions | 
[**createIntentVersion**](DefaultApi.md#createIntentVersion) | **POST** /intents/{name}/versions | 
[**createSlotTypeVersion**](DefaultApi.md#createSlotTypeVersion) | **POST** /slottypes/{name}/versions | 
[**deleteBot**](DefaultApi.md#deleteBot) | **DELETE** /bots/{name} | 
[**deleteBotAlias**](DefaultApi.md#deleteBotAlias) | **DELETE** /bots/{botName}/aliases/{name} | 
[**deleteBotChannelAssociation**](DefaultApi.md#deleteBotChannelAssociation) | **DELETE** /bots/{botName}/aliases/{aliasName}/channels/{name} | 
[**deleteBotVersion**](DefaultApi.md#deleteBotVersion) | **DELETE** /bots/{name}/versions/{version} | 
[**deleteIntent**](DefaultApi.md#deleteIntent) | **DELETE** /intents/{name} | 
[**deleteIntentVersion**](DefaultApi.md#deleteIntentVersion) | **DELETE** /intents/{name}/versions/{version} | 
[**deleteSlotType**](DefaultApi.md#deleteSlotType) | **DELETE** /slottypes/{name} | 
[**deleteSlotTypeVersion**](DefaultApi.md#deleteSlotTypeVersion) | **DELETE** /slottypes/{name}/version/{version} | 
[**deleteUtterances**](DefaultApi.md#deleteUtterances) | **DELETE** /bots/{botName}/utterances/{userId} | 
[**getBot**](DefaultApi.md#getBot) | **GET** /bots/{name}/versions/{versionoralias} | 
[**getBotAlias**](DefaultApi.md#getBotAlias) | **GET** /bots/{botName}/aliases/{name} | 
[**getBotAliases**](DefaultApi.md#getBotAliases) | **GET** /bots/{botName}/aliases/ | 
[**getBotChannelAssociation**](DefaultApi.md#getBotChannelAssociation) | **GET** /bots/{botName}/aliases/{aliasName}/channels/{name} | 
[**getBotChannelAssociations**](DefaultApi.md#getBotChannelAssociations) | **GET** /bots/{botName}/aliases/{aliasName}/channels/ | 
[**getBotVersions**](DefaultApi.md#getBotVersions) | **GET** /bots/{name}/versions/ | 
[**getBots**](DefaultApi.md#getBots) | **GET** /bots/ | 
[**getBuiltinIntent**](DefaultApi.md#getBuiltinIntent) | **GET** /builtins/intents/{signature} | 
[**getBuiltinIntents**](DefaultApi.md#getBuiltinIntents) | **GET** /builtins/intents/ | 
[**getBuiltinSlotTypes**](DefaultApi.md#getBuiltinSlotTypes) | **GET** /builtins/slottypes/ | 
[**getExport**](DefaultApi.md#getExport) | **GET** /exports/#name&amp;version&amp;resourceType&amp;exportType | 
[**getImport**](DefaultApi.md#getImport) | **GET** /imports/{importId} | 
[**getIntent**](DefaultApi.md#getIntent) | **GET** /intents/{name}/versions/{version} | 
[**getIntentVersions**](DefaultApi.md#getIntentVersions) | **GET** /intents/{name}/versions/ | 
[**getIntents**](DefaultApi.md#getIntents) | **GET** /intents/ | 
[**getMigration**](DefaultApi.md#getMigration) | **GET** /migrations/{migrationId} | 
[**getMigrations**](DefaultApi.md#getMigrations) | **GET** /migrations | 
[**getSlotType**](DefaultApi.md#getSlotType) | **GET** /slottypes/{name}/versions/{version} | 
[**getSlotTypeVersions**](DefaultApi.md#getSlotTypeVersions) | **GET** /slottypes/{name}/versions/ | 
[**getSlotTypes**](DefaultApi.md#getSlotTypes) | **GET** /slottypes/ | 
[**getUtterancesView**](DefaultApi.md#getUtterancesView) | **GET** /bots/{botname}/utterances#view&#x3D;aggregation&amp;bot_versions&amp;status_type | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**putBot**](DefaultApi.md#putBot) | **PUT** /bots/{name}/versions/$LATEST | 
[**putBotAlias**](DefaultApi.md#putBotAlias) | **PUT** /bots/{botName}/aliases/{name} | 
[**putIntent**](DefaultApi.md#putIntent) | **PUT** /intents/{name}/versions/$LATEST | 
[**putSlotType**](DefaultApi.md#putSlotType) | **PUT** /slottypes/{name}/versions/$LATEST | 
[**startImport**](DefaultApi.md#startImport) | **POST** /imports/ | 
[**startMigration**](DefaultApi.md#startMigration) | **POST** /migrations | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 



## createBotVersion

> CreateBotVersionResponse createBotVersion(name, createBotVersionRequest, opts)



&lt;p&gt;Creates a new version of the bot based on the &lt;code&gt;$LATEST&lt;/code&gt; version. If the &lt;code&gt;$LATEST&lt;/code&gt; version of this resource hasn&#39;t changed since you created the last version, Amazon Lex doesn&#39;t create a new version. It returns the last created version.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can update only the &lt;code&gt;$LATEST&lt;/code&gt; version of the bot. You can&#39;t update the numbered versions that you create with the &lt;code&gt;CreateBotVersion&lt;/code&gt; operation.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; When you create the first version of a bot, Amazon Lex sets the version to 1. Subsequent versions increment by 1. For more information, see &lt;a&gt;versioning-intro&lt;/a&gt;. &lt;/p&gt; &lt;p&gt; This operation requires permission for the &lt;code&gt;lex:CreateBotVersion&lt;/code&gt; action. &lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the bot that you want to create a new version of. The name is case sensitive. 
let createBotVersionRequest = new AmazonLexModelBuildingService.CreateBotVersionRequest(); // CreateBotVersionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createBotVersion(name, createBotVersionRequest, opts, (error, data, response) => {
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
 **name** | **String**| The name of the bot that you want to create a new version of. The name is case sensitive.  | 
 **createBotVersionRequest** | [**CreateBotVersionRequest**](CreateBotVersionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateBotVersionResponse**](CreateBotVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createIntentVersion

> CreateIntentVersionResponse createIntentVersion(name, createIntentVersionRequest, opts)



&lt;p&gt;Creates a new version of an intent based on the &lt;code&gt;$LATEST&lt;/code&gt; version of the intent. If the &lt;code&gt;$LATEST&lt;/code&gt; version of this intent hasn&#39;t changed since you last updated it, Amazon Lex doesn&#39;t create a new version. It returns the last version you created.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can update only the &lt;code&gt;$LATEST&lt;/code&gt; version of the intent. You can&#39;t update the numbered versions that you create with the &lt;code&gt;CreateIntentVersion&lt;/code&gt; operation.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; When you create a version of an intent, Amazon Lex sets the version to 1. Subsequent versions increment by 1. For more information, see &lt;a&gt;versioning-intro&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lex:CreateIntentVersion&lt;/code&gt; action. &lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the intent that you want to create a new version of. The name is case sensitive. 
let createIntentVersionRequest = new AmazonLexModelBuildingService.CreateIntentVersionRequest(); // CreateIntentVersionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createIntentVersion(name, createIntentVersionRequest, opts, (error, data, response) => {
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
 **name** | **String**| The name of the intent that you want to create a new version of. The name is case sensitive.  | 
 **createIntentVersionRequest** | [**CreateIntentVersionRequest**](CreateIntentVersionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateIntentVersionResponse**](CreateIntentVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSlotTypeVersion

> CreateSlotTypeVersionResponse createSlotTypeVersion(name, createSlotTypeVersionRequest, opts)



&lt;p&gt;Creates a new version of a slot type based on the &lt;code&gt;$LATEST&lt;/code&gt; version of the specified slot type. If the &lt;code&gt;$LATEST&lt;/code&gt; version of this resource has not changed since the last version that you created, Amazon Lex doesn&#39;t create a new version. It returns the last version that you created. &lt;/p&gt; &lt;note&gt; &lt;p&gt;You can update only the &lt;code&gt;$LATEST&lt;/code&gt; version of a slot type. You can&#39;t update the numbered versions that you create with the &lt;code&gt;CreateSlotTypeVersion&lt;/code&gt; operation.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;When you create a version of a slot type, Amazon Lex sets the version to 1. Subsequent versions increment by 1. For more information, see &lt;a&gt;versioning-intro&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:CreateSlotTypeVersion&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the slot type that you want to create a new version for. The name is case sensitive. 
let createSlotTypeVersionRequest = new AmazonLexModelBuildingService.CreateSlotTypeVersionRequest(); // CreateSlotTypeVersionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSlotTypeVersion(name, createSlotTypeVersionRequest, opts, (error, data, response) => {
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
 **name** | **String**| The name of the slot type that you want to create a new version for. The name is case sensitive.  | 
 **createSlotTypeVersionRequest** | [**CreateSlotTypeVersionRequest**](CreateSlotTypeVersionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSlotTypeVersionResponse**](CreateSlotTypeVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteBot

> deleteBot(name, opts)



&lt;p&gt;Deletes all versions of the bot, including the &lt;code&gt;$LATEST&lt;/code&gt; version. To delete a specific version of the bot, use the &lt;a&gt;DeleteBotVersion&lt;/a&gt; operation. The &lt;code&gt;DeleteBot&lt;/code&gt; operation doesn&#39;t immediately remove the bot schema. Instead, it is marked for deletion and removed later.&lt;/p&gt; &lt;p&gt;Amazon Lex stores utterances indefinitely for improving the ability of your bot to respond to user inputs. These utterances are not removed when the bot is deleted. To remove the utterances, use the &lt;a&gt;DeleteUtterances&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;If a bot has an alias, you can&#39;t delete it. Instead, the &lt;code&gt;DeleteBot&lt;/code&gt; operation returns a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception that includes a reference to the alias that refers to the bot. To remove the reference to the bot, delete the alias. If you get the same exception again, delete the referring alias until the &lt;code&gt;DeleteBot&lt;/code&gt; operation is successful.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:DeleteBot&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the bot. The name is case sensitive. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBot(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the bot. The name is case sensitive.  | 
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

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteBotAlias

> deleteBotAlias(name, botName, opts)



&lt;p&gt;Deletes an alias for the specified bot. &lt;/p&gt; &lt;p&gt;You can&#39;t delete an alias that is used in the association between a bot and a messaging channel. If an alias is used in a channel association, the &lt;code&gt;DeleteBot&lt;/code&gt; operation returns a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception that includes a reference to the channel association that refers to the bot. You can remove the reference to the alias by deleting the channel association. If you get the same exception again, delete the referring association until the &lt;code&gt;DeleteBotAlias&lt;/code&gt; operation is successful.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the alias to delete. The name is case sensitive. 
let botName = "botName_example"; // String | The name of the bot that the alias points to.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBotAlias(name, botName, opts, (error, data, response) => {
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
 **name** | **String**| The name of the alias to delete. The name is case sensitive.  | 
 **botName** | **String**| The name of the bot that the alias points to. | 
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

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteBotChannelAssociation

> deleteBotChannelAssociation(name, botName, aliasName, opts)



&lt;p&gt;Deletes the association between an Amazon Lex bot and a messaging platform.&lt;/p&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;lex:DeleteBotChannelAssociation&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the association. The name is case sensitive. 
let botName = "botName_example"; // String | The name of the Amazon Lex bot.
let aliasName = "aliasName_example"; // String | An alias that points to the specific version of the Amazon Lex bot to which this association is being made.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBotChannelAssociation(name, botName, aliasName, opts, (error, data, response) => {
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
 **name** | **String**| The name of the association. The name is case sensitive.  | 
 **botName** | **String**| The name of the Amazon Lex bot. | 
 **aliasName** | **String**| An alias that points to the specific version of the Amazon Lex bot to which this association is being made. | 
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

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteBotVersion

> deleteBotVersion(name, version, opts)



&lt;p&gt;Deletes a specific version of a bot. To delete all versions of a bot, use the &lt;a&gt;DeleteBot&lt;/a&gt; operation. &lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:DeleteBotVersion&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the bot.
let version = "version_example"; // String | The version of the bot to delete. You cannot delete the <code>$LATEST</code> version of the bot. To delete the <code>$LATEST</code> version, use the <a>DeleteBot</a> operation.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBotVersion(name, version, opts, (error, data, response) => {
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
 **name** | **String**| The name of the bot. | 
 **version** | **String**| The version of the bot to delete. You cannot delete the &lt;code&gt;$LATEST&lt;/code&gt; version of the bot. To delete the &lt;code&gt;$LATEST&lt;/code&gt; version, use the &lt;a&gt;DeleteBot&lt;/a&gt; operation. | 
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

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteIntent

> deleteIntent(name, opts)



&lt;p&gt;Deletes all versions of the intent, including the &lt;code&gt;$LATEST&lt;/code&gt; version. To delete a specific version of the intent, use the &lt;a&gt;DeleteIntentVersion&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt; You can delete a version of an intent only if it is not referenced. To delete an intent that is referred to in one or more bots (see &lt;a&gt;how-it-works&lt;/a&gt;), you must remove those references first. &lt;/p&gt; &lt;note&gt; &lt;p&gt; If you get the &lt;code&gt;ResourceInUseException&lt;/code&gt; exception, it provides an example reference that shows where the intent is referenced. To remove the reference to the intent, either update the bot or delete it. If you get the same exception when you attempt to delete the intent again, repeat until the intent has no references and the call to &lt;code&gt;DeleteIntent&lt;/code&gt; is successful. &lt;/p&gt; &lt;/note&gt; &lt;p&gt; This operation requires permission for the &lt;code&gt;lex:DeleteIntent&lt;/code&gt; action. &lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the intent. The name is case sensitive. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteIntent(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the intent. The name is case sensitive.  | 
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

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteIntentVersion

> deleteIntentVersion(name, version, opts)



&lt;p&gt;Deletes a specific version of an intent. To delete all versions of a intent, use the &lt;a&gt;DeleteIntent&lt;/a&gt; operation. &lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:DeleteIntentVersion&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the intent.
let version = "version_example"; // String | The version of the intent to delete. You cannot delete the <code>$LATEST</code> version of the intent. To delete the <code>$LATEST</code> version, use the <a>DeleteIntent</a> operation.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteIntentVersion(name, version, opts, (error, data, response) => {
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
 **name** | **String**| The name of the intent. | 
 **version** | **String**| The version of the intent to delete. You cannot delete the &lt;code&gt;$LATEST&lt;/code&gt; version of the intent. To delete the &lt;code&gt;$LATEST&lt;/code&gt; version, use the &lt;a&gt;DeleteIntent&lt;/a&gt; operation. | 
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

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSlotType

> deleteSlotType(name, opts)



&lt;p&gt;Deletes all versions of the slot type, including the &lt;code&gt;$LATEST&lt;/code&gt; version. To delete a specific version of the slot type, use the &lt;a&gt;DeleteSlotTypeVersion&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt; You can delete a version of a slot type only if it is not referenced. To delete a slot type that is referred to in one or more intents, you must remove those references first. &lt;/p&gt; &lt;note&gt; &lt;p&gt; If you get the &lt;code&gt;ResourceInUseException&lt;/code&gt; exception, the exception provides an example reference that shows the intent where the slot type is referenced. To remove the reference to the slot type, either update the intent or delete it. If you get the same exception when you attempt to delete the slot type again, repeat until the slot type has no references and the &lt;code&gt;DeleteSlotType&lt;/code&gt; call is successful. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;lex:DeleteSlotType&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the slot type. The name is case sensitive. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSlotType(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the slot type. The name is case sensitive.  | 
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

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSlotTypeVersion

> deleteSlotTypeVersion(name, version, opts)



&lt;p&gt;Deletes a specific version of a slot type. To delete all versions of a slot type, use the &lt;a&gt;DeleteSlotType&lt;/a&gt; operation. &lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:DeleteSlotTypeVersion&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the slot type.
let version = "version_example"; // String | The version of the slot type to delete. You cannot delete the <code>$LATEST</code> version of the slot type. To delete the <code>$LATEST</code> version, use the <a>DeleteSlotType</a> operation.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSlotTypeVersion(name, version, opts, (error, data, response) => {
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
 **name** | **String**| The name of the slot type. | 
 **version** | **String**| The version of the slot type to delete. You cannot delete the &lt;code&gt;$LATEST&lt;/code&gt; version of the slot type. To delete the &lt;code&gt;$LATEST&lt;/code&gt; version, use the &lt;a&gt;DeleteSlotType&lt;/a&gt; operation. | 
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

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteUtterances

> deleteUtterances(botName, userId, opts)



&lt;p&gt;Deletes stored utterances.&lt;/p&gt; &lt;p&gt;Amazon Lex stores the utterances that users send to your bot. Utterances are stored for 15 days for use with the &lt;a&gt;GetUtterancesView&lt;/a&gt; operation, and then stored indefinitely for use in improving the ability of your bot to respond to user input.&lt;/p&gt; &lt;p&gt;Use the &lt;code&gt;DeleteUtterances&lt;/code&gt; operation to manually delete stored utterances for a specific user. When you use the &lt;code&gt;DeleteUtterances&lt;/code&gt; operation, utterances stored for improving your bot&#39;s ability to respond to user input are deleted immediately. Utterances stored for use with the &lt;code&gt;GetUtterancesView&lt;/code&gt; operation are deleted after 15 days.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:DeleteUtterances&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let botName = "botName_example"; // String | The name of the bot that stored the utterances.
let userId = "userId_example"; // String |  The unique identifier for the user that made the utterances. This is the user ID that was sent in the <a href=\"http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostContent.html\">PostContent</a> or <a href=\"http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html\">PostText</a> operation request that contained the utterance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteUtterances(botName, userId, opts, (error, data, response) => {
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
 **botName** | **String**| The name of the bot that stored the utterances. | 
 **userId** | **String**|  The unique identifier for the user that made the utterances. This is the user ID that was sent in the &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostContent.html\&quot;&gt;PostContent&lt;/a&gt; or &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html\&quot;&gt;PostText&lt;/a&gt; operation request that contained the utterance. | 
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

- **Content-Type**: Not defined
- **Accept**: application/json


## getBot

> GetBotResponse getBot(name, versionoralias, opts)



&lt;p&gt;Returns metadata information for a specific bot. You must provide the bot name and the bot version or alias. &lt;/p&gt; &lt;p&gt; This operation requires permissions for the &lt;code&gt;lex:GetBot&lt;/code&gt; action. &lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the bot. The name is case sensitive. 
let versionoralias = "versionoralias_example"; // String | The version or alias of the bot.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBot(name, versionoralias, opts, (error, data, response) => {
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
 **name** | **String**| The name of the bot. The name is case sensitive.  | 
 **versionoralias** | **String**| The version or alias of the bot. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBotResponse**](GetBotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBotAlias

> GetBotAliasResponse getBotAlias(name, botName, opts)



&lt;p&gt;Returns information about an Amazon Lex bot alias. For more information about aliases, see &lt;a&gt;versioning-aliases&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetBotAlias&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the bot alias. The name is case sensitive.
let botName = "botName_example"; // String | The name of the bot.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBotAlias(name, botName, opts, (error, data, response) => {
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
 **name** | **String**| The name of the bot alias. The name is case sensitive. | 
 **botName** | **String**| The name of the bot. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBotAliasResponse**](GetBotAliasResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBotAliases

> GetBotAliasesResponse getBotAliases(botName, opts)



&lt;p&gt;Returns a list of aliases for a specified Amazon Lex bot.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetBotAliases&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let botName = "botName_example"; // String | The name of the bot.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A pagination token for fetching the next page of aliases. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of aliases, specify the pagination token in the next request. 
  'maxResults': 56, // Number | The maximum number of aliases to return in the response. The default is 50. . 
  'nameContains': "nameContains_example" // String | Substring to match in bot alias names. An alias will be returned if any part of its name matches the substring. For example, \"xyz\" matches both \"xyzabc\" and \"abcxyz.\"
};
apiInstance.getBotAliases(botName, opts, (error, data, response) => {
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
 **botName** | **String**| The name of the bot. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| A pagination token for fetching the next page of aliases. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of aliases, specify the pagination token in the next request.  | [optional] 
 **maxResults** | **Number**| The maximum number of aliases to return in the response. The default is 50. .  | [optional] 
 **nameContains** | **String**| Substring to match in bot alias names. An alias will be returned if any part of its name matches the substring. For example, \&quot;xyz\&quot; matches both \&quot;xyzabc\&quot; and \&quot;abcxyz.\&quot; | [optional] 

### Return type

[**GetBotAliasesResponse**](GetBotAliasesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBotChannelAssociation

> GetBotChannelAssociationResponse getBotChannelAssociation(name, botName, aliasName, opts)



&lt;p&gt;Returns information about the association between an Amazon Lex bot and a messaging platform.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetBotChannelAssociation&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the association between the bot and the channel. The name is case sensitive. 
let botName = "botName_example"; // String | The name of the Amazon Lex bot.
let aliasName = "aliasName_example"; // String | An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBotChannelAssociation(name, botName, aliasName, opts, (error, data, response) => {
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
 **name** | **String**| The name of the association between the bot and the channel. The name is case sensitive.  | 
 **botName** | **String**| The name of the Amazon Lex bot. | 
 **aliasName** | **String**| An alias pointing to the specific version of the Amazon Lex bot to which this association is being made. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBotChannelAssociationResponse**](GetBotChannelAssociationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBotChannelAssociations

> GetBotChannelAssociationsResponse getBotChannelAssociations(botName, aliasName, opts)



&lt;p&gt; Returns a list of all of the channels associated with the specified bot. &lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetBotChannelAssociations&lt;/code&gt; operation requires permissions for the &lt;code&gt;lex:GetBotChannelAssociations&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let botName = "botName_example"; // String | The name of the Amazon Lex bot in the association.
let aliasName = "aliasName_example"; // String | An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A pagination token for fetching the next page of associations. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of associations, specify the pagination token in the next request. 
  'maxResults': 56, // Number | The maximum number of associations to return in the response. The default is 50. 
  'nameContains': "nameContains_example" // String | Substring to match in channel association names. An association will be returned if any part of its name matches the substring. For example, \"xyz\" matches both \"xyzabc\" and \"abcxyz.\" To return all bot channel associations, use a hyphen (\"-\") as the <code>nameContains</code> parameter.
};
apiInstance.getBotChannelAssociations(botName, aliasName, opts, (error, data, response) => {
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
 **botName** | **String**| The name of the Amazon Lex bot in the association. | 
 **aliasName** | **String**| An alias pointing to the specific version of the Amazon Lex bot to which this association is being made. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| A pagination token for fetching the next page of associations. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of associations, specify the pagination token in the next request.  | [optional] 
 **maxResults** | **Number**| The maximum number of associations to return in the response. The default is 50.  | [optional] 
 **nameContains** | **String**| Substring to match in channel association names. An association will be returned if any part of its name matches the substring. For example, \&quot;xyz\&quot; matches both \&quot;xyzabc\&quot; and \&quot;abcxyz.\&quot; To return all bot channel associations, use a hyphen (\&quot;-\&quot;) as the &lt;code&gt;nameContains&lt;/code&gt; parameter. | [optional] 

### Return type

[**GetBotChannelAssociationsResponse**](GetBotChannelAssociationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBotVersions

> GetBotVersionsResponse getBotVersions(name, opts)



&lt;p&gt;Gets information about all of the versions of a bot.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetBotVersions&lt;/code&gt; operation returns a &lt;code&gt;BotMetadata&lt;/code&gt; object for each version of a bot. For example, if a bot has three numbered versions, the &lt;code&gt;GetBotVersions&lt;/code&gt; operation returns four &lt;code&gt;BotMetadata&lt;/code&gt; objects in the response, one for each numbered version and one for the &lt;code&gt;$LATEST&lt;/code&gt; version. &lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetBotVersions&lt;/code&gt; operation always returns at least one version, the &lt;code&gt;$LATEST&lt;/code&gt; version.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetBotVersions&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the bot for which versions should be returned.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A pagination token for fetching the next page of bot versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. 
  'maxResults': 56 // Number | The maximum number of bot versions to return in the response. The default is 10.
};
apiInstance.getBotVersions(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the bot for which versions should be returned. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| A pagination token for fetching the next page of bot versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request.  | [optional] 
 **maxResults** | **Number**| The maximum number of bot versions to return in the response. The default is 10. | [optional] 

### Return type

[**GetBotVersionsResponse**](GetBotVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBots

> GetBotsResponse getBots(opts)



&lt;p&gt;Returns bot information as follows: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you provide the &lt;code&gt;nameContains&lt;/code&gt; field, the response includes information for the &lt;code&gt;$LATEST&lt;/code&gt; version of all bots whose name contains the specified string.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you don&#39;t specify the &lt;code&gt;nameContains&lt;/code&gt; field, the operation returns information about the &lt;code&gt;$LATEST&lt;/code&gt; version of all of your bots.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;lex:GetBots&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A pagination token that fetches the next page of bots. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of bots, specify the pagination token in the next request. 
  'maxResults': 56, // Number | The maximum number of bots to return in the response that the request will return. The default is 10.
  'nameContains': "nameContains_example" // String | Substring to match in bot names. A bot will be returned if any part of its name matches the substring. For example, \"xyz\" matches both \"xyzabc\" and \"abcxyz.\"
};
apiInstance.getBots(opts, (error, data, response) => {
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
 **nextToken** | **String**| A pagination token that fetches the next page of bots. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of bots, specify the pagination token in the next request.  | [optional] 
 **maxResults** | **Number**| The maximum number of bots to return in the response that the request will return. The default is 10. | [optional] 
 **nameContains** | **String**| Substring to match in bot names. A bot will be returned if any part of its name matches the substring. For example, \&quot;xyz\&quot; matches both \&quot;xyzabc\&quot; and \&quot;abcxyz.\&quot; | [optional] 

### Return type

[**GetBotsResponse**](GetBotsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBuiltinIntent

> GetBuiltinIntentResponse getBuiltinIntent(signature, opts)



&lt;p&gt;Returns information about a built-in intent.&lt;/p&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;lex:GetBuiltinIntent&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let signature = "signature_example"; // String | The unique identifier for a built-in intent. To find the signature for an intent, see <a href=\"https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents\">Standard Built-in Intents</a> in the <i>Alexa Skills Kit</i>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBuiltinIntent(signature, opts, (error, data, response) => {
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
 **signature** | **String**| The unique identifier for a built-in intent. To find the signature for an intent, see &lt;a href&#x3D;\&quot;https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents\&quot;&gt;Standard Built-in Intents&lt;/a&gt; in the &lt;i&gt;Alexa Skills Kit&lt;/i&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBuiltinIntentResponse**](GetBuiltinIntentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBuiltinIntents

> GetBuiltinIntentsResponse getBuiltinIntents(opts)



&lt;p&gt;Gets a list of built-in intents that meet the specified criteria.&lt;/p&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;lex:GetBuiltinIntents&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'locale': "locale_example", // String | A list of locales that the intent supports.
  'signatureContains': "signatureContains_example", // String | Substring to match in built-in intent signatures. An intent will be returned if any part of its signature matches the substring. For example, \"xyz\" matches both \"xyzabc\" and \"abcxyz.\" To find the signature for an intent, see <a href=\"https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents\">Standard Built-in Intents</a> in the <i>Alexa Skills Kit</i>.
  'nextToken': "nextToken_example", // String | A pagination token that fetches the next page of intents. If this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, use the pagination token in the next request.
  'maxResults': 56 // Number | The maximum number of intents to return in the response. The default is 10.
};
apiInstance.getBuiltinIntents(opts, (error, data, response) => {
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
 **locale** | **String**| A list of locales that the intent supports. | [optional] 
 **signatureContains** | **String**| Substring to match in built-in intent signatures. An intent will be returned if any part of its signature matches the substring. For example, \&quot;xyz\&quot; matches both \&quot;xyzabc\&quot; and \&quot;abcxyz.\&quot; To find the signature for an intent, see &lt;a href&#x3D;\&quot;https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents\&quot;&gt;Standard Built-in Intents&lt;/a&gt; in the &lt;i&gt;Alexa Skills Kit&lt;/i&gt;. | [optional] 
 **nextToken** | **String**| A pagination token that fetches the next page of intents. If this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, use the pagination token in the next request. | [optional] 
 **maxResults** | **Number**| The maximum number of intents to return in the response. The default is 10. | [optional] 

### Return type

[**GetBuiltinIntentsResponse**](GetBuiltinIntentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBuiltinSlotTypes

> GetBuiltinSlotTypesResponse getBuiltinSlotTypes(opts)



&lt;p&gt;Gets a list of built-in slot types that meet the specified criteria.&lt;/p&gt; &lt;p&gt;For a list of built-in slot types, see &lt;a href&#x3D;\&quot;https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference\&quot;&gt;Slot Type Reference&lt;/a&gt; in the &lt;i&gt;Alexa Skills Kit&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;lex:GetBuiltInSlotTypes&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'locale': "locale_example", // String | A list of locales that the slot type supports.
  'signatureContains': "signatureContains_example", // String | Substring to match in built-in slot type signatures. A slot type will be returned if any part of its signature matches the substring. For example, \"xyz\" matches both \"xyzabc\" and \"abcxyz.\"
  'nextToken': "nextToken_example", // String | A pagination token that fetches the next page of slot types. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of slot types, specify the pagination token in the next request.
  'maxResults': 56 // Number | The maximum number of slot types to return in the response. The default is 10.
};
apiInstance.getBuiltinSlotTypes(opts, (error, data, response) => {
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
 **locale** | **String**| A list of locales that the slot type supports. | [optional] 
 **signatureContains** | **String**| Substring to match in built-in slot type signatures. A slot type will be returned if any part of its signature matches the substring. For example, \&quot;xyz\&quot; matches both \&quot;xyzabc\&quot; and \&quot;abcxyz.\&quot; | [optional] 
 **nextToken** | **String**| A pagination token that fetches the next page of slot types. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of slot types, specify the pagination token in the next request. | [optional] 
 **maxResults** | **Number**| The maximum number of slot types to return in the response. The default is 10. | [optional] 

### Return type

[**GetBuiltinSlotTypesResponse**](GetBuiltinSlotTypesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getExport

> GetExportResponse getExport(name, version, resourceType, exportType, opts)



Exports the contents of a Amazon Lex resource in a specified format. 

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the bot to export.
let version = "version_example"; // String | The version of the bot to export.
let resourceType = "resourceType_example"; // String | The type of resource to export. 
let exportType = "exportType_example"; // String | The format of the exported data.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getExport(name, version, resourceType, exportType, opts, (error, data, response) => {
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
 **name** | **String**| The name of the bot to export. | 
 **version** | **String**| The version of the bot to export. | 
 **resourceType** | **String**| The type of resource to export.  | 
 **exportType** | **String**| The format of the exported data. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetExportResponse**](GetExportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImport

> GetImportResponse getImport(importId, opts)



Gets information about an import job started with the &lt;code&gt;StartImport&lt;/code&gt; operation.

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let importId = "importId_example"; // String | The identifier of the import job information to return.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getImport(importId, opts, (error, data, response) => {
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
 **importId** | **String**| The identifier of the import job information to return. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetImportResponse**](GetImportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIntent

> GetIntentResponse getIntent(name, version, opts)



&lt;p&gt; Returns information about an intent. In addition to the intent name, you must specify the intent version. &lt;/p&gt; &lt;p&gt; This operation requires permissions to perform the &lt;code&gt;lex:GetIntent&lt;/code&gt; action. &lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the intent. The name is case sensitive. 
let version = "version_example"; // String | The version of the intent.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getIntent(name, version, opts, (error, data, response) => {
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
 **name** | **String**| The name of the intent. The name is case sensitive.  | 
 **version** | **String**| The version of the intent. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetIntentResponse**](GetIntentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIntentVersions

> GetIntentVersionsResponse getIntentVersions(name, opts)



&lt;p&gt;Gets information about all of the versions of an intent.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetIntentVersions&lt;/code&gt; operation returns an &lt;code&gt;IntentMetadata&lt;/code&gt; object for each version of an intent. For example, if an intent has three numbered versions, the &lt;code&gt;GetIntentVersions&lt;/code&gt; operation returns four &lt;code&gt;IntentMetadata&lt;/code&gt; objects in the response, one for each numbered version and one for the &lt;code&gt;$LATEST&lt;/code&gt; version. &lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetIntentVersions&lt;/code&gt; operation always returns at least one version, the &lt;code&gt;$LATEST&lt;/code&gt; version.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetIntentVersions&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the intent for which versions should be returned.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A pagination token for fetching the next page of intent versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. 
  'maxResults': 56 // Number | The maximum number of intent versions to return in the response. The default is 10.
};
apiInstance.getIntentVersions(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the intent for which versions should be returned. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| A pagination token for fetching the next page of intent versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request.  | [optional] 
 **maxResults** | **Number**| The maximum number of intent versions to return in the response. The default is 10. | [optional] 

### Return type

[**GetIntentVersionsResponse**](GetIntentVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIntents

> GetIntentsResponse getIntents(opts)



&lt;p&gt;Returns intent information as follows: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you specify the &lt;code&gt;nameContains&lt;/code&gt; field, returns the &lt;code&gt;$LATEST&lt;/code&gt; version of all intents that contain the specified string.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; If you don&#39;t specify the &lt;code&gt;nameContains&lt;/code&gt; field, returns information about the &lt;code&gt;$LATEST&lt;/code&gt; version of all intents. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; The operation requires permission for the &lt;code&gt;lex:GetIntents&lt;/code&gt; action. &lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A pagination token that fetches the next page of intents. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, specify the pagination token in the next request. 
  'maxResults': 56, // Number | The maximum number of intents to return in the response. The default is 10.
  'nameContains': "nameContains_example" // String | Substring to match in intent names. An intent will be returned if any part of its name matches the substring. For example, \"xyz\" matches both \"xyzabc\" and \"abcxyz.\"
};
apiInstance.getIntents(opts, (error, data, response) => {
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
 **nextToken** | **String**| A pagination token that fetches the next page of intents. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, specify the pagination token in the next request.  | [optional] 
 **maxResults** | **Number**| The maximum number of intents to return in the response. The default is 10. | [optional] 
 **nameContains** | **String**| Substring to match in intent names. An intent will be returned if any part of its name matches the substring. For example, \&quot;xyz\&quot; matches both \&quot;xyzabc\&quot; and \&quot;abcxyz.\&quot; | [optional] 

### Return type

[**GetIntentsResponse**](GetIntentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMigration

> GetMigrationResponse getMigration(migrationId, opts)



Provides details about an ongoing or complete migration from an Amazon Lex V1 bot to an Amazon Lex V2 bot. Use this operation to view the migration alerts and warnings related to the migration.

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let migrationId = "migrationId_example"; // String | The unique identifier of the migration to view. The <code>migrationID</code> is returned by the operation.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMigration(migrationId, opts, (error, data, response) => {
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
 **migrationId** | **String**| The unique identifier of the migration to view. The &lt;code&gt;migrationID&lt;/code&gt; is returned by the operation. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMigrationResponse**](GetMigrationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMigrations

> GetMigrationsResponse getMigrations(opts)



Gets a list of migrations between Amazon Lex V1 and Amazon Lex V2.

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'sortByAttribute': "sortByAttribute_example", // String | The field to sort the list of migrations by. You can sort by the Amazon Lex V1 bot name or the date and time that the migration was started.
  'sortByOrder': "sortByOrder_example", // String | The order so sort the list.
  'v1BotNameContains': "v1BotNameContains_example", // String | Filters the list to contain only bots whose name contains the specified string. The string is matched anywhere in bot name.
  'migrationStatusEquals': "migrationStatusEquals_example", // String | Filters the list to contain only migrations in the specified state.
  'maxResults': 56, // Number | The maximum number of migrations to return in the response. The default is 10.
  'nextToken': "nextToken_example" // String | A pagination token that fetches the next page of migrations. If the response to this operation is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of migrations, specify the pagination token in the request.
};
apiInstance.getMigrations(opts, (error, data, response) => {
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
 **sortByAttribute** | **String**| The field to sort the list of migrations by. You can sort by the Amazon Lex V1 bot name or the date and time that the migration was started. | [optional] 
 **sortByOrder** | **String**| The order so sort the list. | [optional] 
 **v1BotNameContains** | **String**| Filters the list to contain only bots whose name contains the specified string. The string is matched anywhere in bot name. | [optional] 
 **migrationStatusEquals** | **String**| Filters the list to contain only migrations in the specified state. | [optional] 
 **maxResults** | **Number**| The maximum number of migrations to return in the response. The default is 10. | [optional] 
 **nextToken** | **String**| A pagination token that fetches the next page of migrations. If the response to this operation is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of migrations, specify the pagination token in the request. | [optional] 

### Return type

[**GetMigrationsResponse**](GetMigrationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSlotType

> GetSlotTypeResponse getSlotType(name, version, opts)



&lt;p&gt;Returns information about a specific version of a slot type. In addition to specifying the slot type name, you must specify the slot type version.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetSlotType&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the slot type. The name is case sensitive. 
let version = "version_example"; // String | The version of the slot type. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSlotType(name, version, opts, (error, data, response) => {
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
 **name** | **String**| The name of the slot type. The name is case sensitive.  | 
 **version** | **String**| The version of the slot type.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSlotTypeResponse**](GetSlotTypeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSlotTypeVersions

> GetSlotTypeVersionsResponse getSlotTypeVersions(name, opts)



&lt;p&gt;Gets information about all versions of a slot type.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetSlotTypeVersions&lt;/code&gt; operation returns a &lt;code&gt;SlotTypeMetadata&lt;/code&gt; object for each version of a slot type. For example, if a slot type has three numbered versions, the &lt;code&gt;GetSlotTypeVersions&lt;/code&gt; operation returns four &lt;code&gt;SlotTypeMetadata&lt;/code&gt; objects in the response, one for each numbered version and one for the &lt;code&gt;$LATEST&lt;/code&gt; version. &lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetSlotTypeVersions&lt;/code&gt; operation always returns at least one version, the &lt;code&gt;$LATEST&lt;/code&gt; version.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetSlotTypeVersions&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the slot type for which versions should be returned.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A pagination token for fetching the next page of slot type versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. 
  'maxResults': 56 // Number | The maximum number of slot type versions to return in the response. The default is 10.
};
apiInstance.getSlotTypeVersions(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the slot type for which versions should be returned. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| A pagination token for fetching the next page of slot type versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request.  | [optional] 
 **maxResults** | **Number**| The maximum number of slot type versions to return in the response. The default is 10. | [optional] 

### Return type

[**GetSlotTypeVersionsResponse**](GetSlotTypeVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSlotTypes

> GetSlotTypesResponse getSlotTypes(opts)



&lt;p&gt;Returns slot type information as follows: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you specify the &lt;code&gt;nameContains&lt;/code&gt; field, returns the &lt;code&gt;$LATEST&lt;/code&gt; version of all slot types that contain the specified string.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; If you don&#39;t specify the &lt;code&gt;nameContains&lt;/code&gt; field, returns information about the &lt;code&gt;$LATEST&lt;/code&gt; version of all slot types. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; The operation requires permission for the &lt;code&gt;lex:GetSlotTypes&lt;/code&gt; action. &lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A pagination token that fetches the next page of slot types. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch next page of slot types, specify the pagination token in the next request.
  'maxResults': 56, // Number | The maximum number of slot types to return in the response. The default is 10.
  'nameContains': "nameContains_example" // String | Substring to match in slot type names. A slot type will be returned if any part of its name matches the substring. For example, \"xyz\" matches both \"xyzabc\" and \"abcxyz.\"
};
apiInstance.getSlotTypes(opts, (error, data, response) => {
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
 **nextToken** | **String**| A pagination token that fetches the next page of slot types. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch next page of slot types, specify the pagination token in the next request. | [optional] 
 **maxResults** | **Number**| The maximum number of slot types to return in the response. The default is 10. | [optional] 
 **nameContains** | **String**| Substring to match in slot type names. A slot type will be returned if any part of its name matches the substring. For example, \&quot;xyz\&quot; matches both \&quot;xyzabc\&quot; and \&quot;abcxyz.\&quot; | [optional] 

### Return type

[**GetSlotTypesResponse**](GetSlotTypesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUtterancesView

> GetUtterancesViewResponse getUtterancesView(botname, botVersions, statusType, view, opts)



&lt;p&gt;Use the &lt;code&gt;GetUtterancesView&lt;/code&gt; operation to get information about the utterances that your users have made to your bot. You can use this list to tune the utterances that your bot responds to.&lt;/p&gt; &lt;p&gt;For example, say that you have created a bot to order flowers. After your users have used your bot for a while, use the &lt;code&gt;GetUtterancesView&lt;/code&gt; operation to see the requests that they have made and whether they have been successful. You might find that the utterance \&quot;I want flowers\&quot; is not being recognized. You could add this utterance to the &lt;code&gt;OrderFlowers&lt;/code&gt; intent so that your bot recognizes that utterance.&lt;/p&gt; &lt;p&gt;After you publish a new version of a bot, you can get information about the old version and the new so that you can compare the performance across the two versions. &lt;/p&gt; &lt;p&gt;Utterance statistics are generated once a day. Data is available for the last 15 days. You can request information for up to 5 versions of your bot in each request. Amazon Lex returns the most frequent utterances received by the bot in the last 15 days. The response contains information about a maximum of 100 utterances for each version.&lt;/p&gt; &lt;p&gt;If you set &lt;code&gt;childDirected&lt;/code&gt; field to true when you created your bot, if you are using slot obfuscation with one or more slots, or if you opted out of participating in improving Amazon Lex, utterances are not available.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetUtterancesView&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let botname = "botname_example"; // String | The name of the bot for which utterance information should be returned.
let botVersions = ["null"]; // [String] | An array of bot versions for which utterance information should be returned. The limit is 5 versions per request.
let statusType = "statusType_example"; // String | To return utterances that were recognized and handled, use <code>Detected</code>. To return utterances that were not recognized, use <code>Missed</code>.
let view = "view_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getUtterancesView(botname, botVersions, statusType, view, opts, (error, data, response) => {
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
 **botname** | **String**| The name of the bot for which utterance information should be returned. | 
 **botVersions** | [**[String]**](String.md)| An array of bot versions for which utterance information should be returned. The limit is 5 versions per request. | 
 **statusType** | **String**| To return utterances that were recognized and handled, use &lt;code&gt;Detected&lt;/code&gt;. To return utterances that were not recognized, use &lt;code&gt;Missed&lt;/code&gt;. | 
 **view** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetUtterancesViewResponse**](GetUtterancesViewResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Gets a list of tags associated with the specified resource. Only bots, bot aliases, and bot channels can have tags associated with them.

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource to get a list of tags for.
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource to get a list of tags for. | 
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


## putBot

> PutBotResponse putBot(name, putBotRequest, opts)



&lt;p&gt;Creates an Amazon Lex conversational bot or replaces an existing bot. When you create or update a bot you are only required to specify a name, a locale, and whether the bot is directed toward children under age 13. You can use this to add intents later, or to remove intents from an existing bot. When you create a bot with the minimum information, the bot is created or updated but Amazon Lex returns the &lt;code/&gt; response &lt;code&gt;FAILED&lt;/code&gt;. You can build the bot after you add one or more intents. For more information about Amazon Lex bots, see &lt;a&gt;how-it-works&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;If you specify the name of an existing bot, the fields in the request replace the existing values in the &lt;code&gt;$LATEST&lt;/code&gt; version of the bot. Amazon Lex removes any fields that you don&#39;t provide values for in the request, except for the &lt;code&gt;idleTTLInSeconds&lt;/code&gt; and &lt;code&gt;privacySettings&lt;/code&gt; fields, which are set to their default values. If you don&#39;t specify values for required fields, Amazon Lex throws an exception.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:PutBot&lt;/code&gt; action. For more information, see &lt;a&gt;security-iam&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the bot. The name is <i>not</i> case sensitive. 
let putBotRequest = new AmazonLexModelBuildingService.PutBotRequest(); // PutBotRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putBot(name, putBotRequest, opts, (error, data, response) => {
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
 **name** | **String**| The name of the bot. The name is &lt;i&gt;not&lt;/i&gt; case sensitive.  | 
 **putBotRequest** | [**PutBotRequest**](PutBotRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutBotResponse**](PutBotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putBotAlias

> PutBotAliasResponse putBotAlias(name, botName, putBotAliasRequest, opts)



&lt;p&gt;Creates an alias for the specified version of the bot or replaces an alias for the specified bot. To change the version of the bot that the alias points to, replace the alias. For more information about aliases, see &lt;a&gt;versioning-aliases&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:PutBotAlias&lt;/code&gt; action. &lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | The name of the alias. The name is <i>not</i> case sensitive.
let botName = "botName_example"; // String | The name of the bot.
let putBotAliasRequest = new AmazonLexModelBuildingService.PutBotAliasRequest(); // PutBotAliasRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putBotAlias(name, botName, putBotAliasRequest, opts, (error, data, response) => {
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
 **name** | **String**| The name of the alias. The name is &lt;i&gt;not&lt;/i&gt; case sensitive. | 
 **botName** | **String**| The name of the bot. | 
 **putBotAliasRequest** | [**PutBotAliasRequest**](PutBotAliasRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutBotAliasResponse**](PutBotAliasResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putIntent

> PutIntentResponse putIntent(name, putIntentRequest, opts)



&lt;p&gt;Creates an intent or replaces an existing intent.&lt;/p&gt; &lt;p&gt;To define the interaction between the user and your bot, you use one or more intents. For a pizza ordering bot, for example, you would create an &lt;code&gt;OrderPizza&lt;/code&gt; intent. &lt;/p&gt; &lt;p&gt;To create an intent or replace an existing intent, you must provide the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Intent name. For example, &lt;code&gt;OrderPizza&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Sample utterances. For example, \&quot;Can I order a pizza, please.\&quot; and \&quot;I want to order a pizza.\&quot;&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Information to be gathered. You specify slot types for the information that your bot will request from the user. You can specify standard slot types, such as a date or a time, or custom slot types such as the size and crust of a pizza.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;How the intent will be fulfilled. You can provide a Lambda function or configure the intent to return the intent information to the client application. If you use a Lambda function, when all of the intent information is available, Amazon Lex invokes your Lambda function. If you configure your intent to return the intent information to the client application. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can specify other optional information in the request, such as:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A confirmation prompt to ask the user to confirm an intent. For example, \&quot;Shall I order your pizza?\&quot;&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A conclusion statement to send to the user after the intent has been fulfilled. For example, \&quot;I placed your pizza order.\&quot;&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A follow-up prompt that asks the user for additional activity. For example, asking \&quot;Do you want to order a drink with your pizza?\&quot;&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you specify an existing intent name to update the intent, Amazon Lex replaces the values in the &lt;code&gt;$LATEST&lt;/code&gt; version of the intent with the values in the request. Amazon Lex removes fields that you don&#39;t provide in the request. If you don&#39;t specify the required fields, Amazon Lex throws an exception. When you update the &lt;code&gt;$LATEST&lt;/code&gt; version of an intent, the &lt;code&gt;status&lt;/code&gt; field of any bot that uses the &lt;code&gt;$LATEST&lt;/code&gt; version of the intent is set to &lt;code&gt;NOT_BUILT&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a&gt;how-it-works&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:PutIntent&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | <p>The name of the intent. The name is <i>not</i> case sensitive. </p> <p>The name can't match a built-in intent name, or a built-in intent name with \"AMAZON.\" removed. For example, because there is a built-in intent called <code>AMAZON.HelpIntent</code>, you can't create a custom intent called <code>HelpIntent</code>.</p> <p>For a list of built-in intents, see <a href=\"https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents\">Standard Built-in Intents</a> in the <i>Alexa Skills Kit</i>.</p>
let putIntentRequest = new AmazonLexModelBuildingService.PutIntentRequest(); // PutIntentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putIntent(name, putIntentRequest, opts, (error, data, response) => {
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
 **name** | **String**| &lt;p&gt;The name of the intent. The name is &lt;i&gt;not&lt;/i&gt; case sensitive. &lt;/p&gt; &lt;p&gt;The name can&#39;t match a built-in intent name, or a built-in intent name with \&quot;AMAZON.\&quot; removed. For example, because there is a built-in intent called &lt;code&gt;AMAZON.HelpIntent&lt;/code&gt;, you can&#39;t create a custom intent called &lt;code&gt;HelpIntent&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For a list of built-in intents, see &lt;a href&#x3D;\&quot;https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents\&quot;&gt;Standard Built-in Intents&lt;/a&gt; in the &lt;i&gt;Alexa Skills Kit&lt;/i&gt;.&lt;/p&gt; | 
 **putIntentRequest** | [**PutIntentRequest**](PutIntentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutIntentResponse**](PutIntentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putSlotType

> PutSlotTypeResponse putSlotType(name, putSlotTypeRequest, opts)



&lt;p&gt;Creates a custom slot type or replaces an existing custom slot type.&lt;/p&gt; &lt;p&gt;To create a custom slot type, specify a name for the slot type and a set of enumeration values, which are the values that a slot of this type can assume. For more information, see &lt;a&gt;how-it-works&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you specify the name of an existing slot type, the fields in the request replace the existing values in the &lt;code&gt;$LATEST&lt;/code&gt; version of the slot type. Amazon Lex removes the fields that you don&#39;t provide in the request. If you don&#39;t specify required fields, Amazon Lex throws an exception. When you update the &lt;code&gt;$LATEST&lt;/code&gt; version of a slot type, if a bot uses the &lt;code&gt;$LATEST&lt;/code&gt; version of an intent that contains the slot type, the bot&#39;s &lt;code&gt;status&lt;/code&gt; field is set to &lt;code&gt;NOT_BUILT&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:PutSlotType&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let name = "name_example"; // String | <p>The name of the slot type. The name is <i>not</i> case sensitive. </p> <p>The name can't match a built-in slot type name, or a built-in slot type name with \"AMAZON.\" removed. For example, because there is a built-in slot type called <code>AMAZON.DATE</code>, you can't create a custom slot type called <code>DATE</code>.</p> <p>For a list of built-in slot types, see <a href=\"https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference\">Slot Type Reference</a> in the <i>Alexa Skills Kit</i>.</p>
let putSlotTypeRequest = new AmazonLexModelBuildingService.PutSlotTypeRequest(); // PutSlotTypeRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putSlotType(name, putSlotTypeRequest, opts, (error, data, response) => {
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
 **name** | **String**| &lt;p&gt;The name of the slot type. The name is &lt;i&gt;not&lt;/i&gt; case sensitive. &lt;/p&gt; &lt;p&gt;The name can&#39;t match a built-in slot type name, or a built-in slot type name with \&quot;AMAZON.\&quot; removed. For example, because there is a built-in slot type called &lt;code&gt;AMAZON.DATE&lt;/code&gt;, you can&#39;t create a custom slot type called &lt;code&gt;DATE&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For a list of built-in slot types, see &lt;a href&#x3D;\&quot;https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference\&quot;&gt;Slot Type Reference&lt;/a&gt; in the &lt;i&gt;Alexa Skills Kit&lt;/i&gt;.&lt;/p&gt; | 
 **putSlotTypeRequest** | [**PutSlotTypeRequest**](PutSlotTypeRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutSlotTypeResponse**](PutSlotTypeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startImport

> StartImportResponse startImport(startImportRequest, opts)



Starts a job to import a resource to Amazon Lex.

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let startImportRequest = new AmazonLexModelBuildingService.StartImportRequest(); // StartImportRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startImport(startImportRequest, opts, (error, data, response) => {
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
 **startImportRequest** | [**StartImportRequest**](StartImportRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartImportResponse**](StartImportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startMigration

> StartMigrationResponse startMigration(startMigrationRequest, opts)



&lt;p&gt;Starts migrating a bot from Amazon Lex V1 to Amazon Lex V2. Migrate your bot when you want to take advantage of the new features of Amazon Lex V2.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lex/latest/dg/migrate.html\&quot;&gt;Migrating a bot&lt;/a&gt; in the &lt;i&gt;Amazon Lex developer guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let startMigrationRequest = new AmazonLexModelBuildingService.StartMigrationRequest(); // StartMigrationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startMigration(startMigrationRequest, opts, (error, data, response) => {
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
 **startMigrationRequest** | [**StartMigrationRequest**](StartMigrationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartMigrationResponse**](StartMigrationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



Adds the specified tags to the specified resource. If a tag key already exists, the existing value is replaced with the new value.

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the bot, bot alias, or bot channel to tag.
let tagResourceRequest = new AmazonLexModelBuildingService.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the bot, bot alias, or bot channel to tag. | 
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



Removes tags from a bot, bot alias or bot channel.

### Example

```javascript
import AmazonLexModelBuildingService from 'amazon_lex_model_building_service';
let defaultClient = AmazonLexModelBuildingService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource to remove the tags from.
let tagKeys = ["null"]; // [String] | A list of tag keys to remove from the resource. If a tag key does not exist on the resource, it is ignored.
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource to remove the tags from. | 
 **tagKeys** | [**[String]**](String.md)| A list of tag keys to remove from the resource. If a tag key does not exist on the resource, it is ignored. | 
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

