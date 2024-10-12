# AmazonLexModelBuildingV2.DefaultApi

All URIs are relative to *http://models-v2-lex.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchCreateCustomVocabularyItem**](DefaultApi.md#batchCreateCustomVocabularyItem) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/customvocabulary/DEFAULT/batchcreate | 
[**batchDeleteCustomVocabularyItem**](DefaultApi.md#batchDeleteCustomVocabularyItem) | **POST** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/customvocabulary/DEFAULT/batchdelete | 
[**batchUpdateCustomVocabularyItem**](DefaultApi.md#batchUpdateCustomVocabularyItem) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/customvocabulary/DEFAULT/batchupdate | 
[**buildBotLocale**](DefaultApi.md#buildBotLocale) | **POST** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/ | 
[**createBot**](DefaultApi.md#createBot) | **PUT** /bots/ | 
[**createBotAlias**](DefaultApi.md#createBotAlias) | **PUT** /bots/{botId}/botaliases/ | 
[**createBotLocale**](DefaultApi.md#createBotLocale) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/ | 
[**createBotVersion**](DefaultApi.md#createBotVersion) | **PUT** /bots/{botId}/botversions/ | 
[**createExport**](DefaultApi.md#createExport) | **PUT** /exports/ | 
[**createIntent**](DefaultApi.md#createIntent) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/intents/ | 
[**createResourcePolicy**](DefaultApi.md#createResourcePolicy) | **POST** /policy/{resourceArn}/ | 
[**createResourcePolicyStatement**](DefaultApi.md#createResourcePolicyStatement) | **POST** /policy/{resourceArn}/statements/ | 
[**createSlot**](DefaultApi.md#createSlot) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/intents/{intentId}/slots/ | 
[**createSlotType**](DefaultApi.md#createSlotType) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/slottypes/ | 
[**createTestSetDiscrepancyReport**](DefaultApi.md#createTestSetDiscrepancyReport) | **POST** /testsets/{testSetId}/testsetdiscrepancy | 
[**createUploadUrl**](DefaultApi.md#createUploadUrl) | **POST** /createuploadurl/ | 
[**deleteBot**](DefaultApi.md#deleteBot) | **DELETE** /bots/{botId}/ | 
[**deleteBotAlias**](DefaultApi.md#deleteBotAlias) | **DELETE** /bots/{botId}/botaliases/{botAliasId}/ | 
[**deleteBotLocale**](DefaultApi.md#deleteBotLocale) | **DELETE** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/ | 
[**deleteBotVersion**](DefaultApi.md#deleteBotVersion) | **DELETE** /bots/{botId}/botversions/{botVersion}/ | 
[**deleteCustomVocabulary**](DefaultApi.md#deleteCustomVocabulary) | **DELETE** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/customvocabulary | 
[**deleteExport**](DefaultApi.md#deleteExport) | **DELETE** /exports/{exportId}/ | 
[**deleteImport**](DefaultApi.md#deleteImport) | **DELETE** /imports/{importId}/ | 
[**deleteIntent**](DefaultApi.md#deleteIntent) | **DELETE** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/intents/{intentId}/ | 
[**deleteResourcePolicy**](DefaultApi.md#deleteResourcePolicy) | **DELETE** /policy/{resourceArn}/ | 
[**deleteResourcePolicyStatement**](DefaultApi.md#deleteResourcePolicyStatement) | **DELETE** /policy/{resourceArn}/statements/{statementId}/ | 
[**deleteSlot**](DefaultApi.md#deleteSlot) | **DELETE** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/intents/{intentId}/slots/{slotId}/ | 
[**deleteSlotType**](DefaultApi.md#deleteSlotType) | **DELETE** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/slottypes/{slotTypeId}/ | 
[**deleteTestSet**](DefaultApi.md#deleteTestSet) | **DELETE** /testsets/{testSetId} | 
[**deleteUtterances**](DefaultApi.md#deleteUtterances) | **DELETE** /bots/{botId}/utterances/ | 
[**describeBot**](DefaultApi.md#describeBot) | **GET** /bots/{botId}/ | 
[**describeBotAlias**](DefaultApi.md#describeBotAlias) | **GET** /bots/{botId}/botaliases/{botAliasId}/ | 
[**describeBotLocale**](DefaultApi.md#describeBotLocale) | **GET** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/ | 
[**describeBotRecommendation**](DefaultApi.md#describeBotRecommendation) | **GET** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/botrecommendations/{botRecommendationId}/ | 
[**describeBotVersion**](DefaultApi.md#describeBotVersion) | **GET** /bots/{botId}/botversions/{botVersion}/ | 
[**describeCustomVocabularyMetadata**](DefaultApi.md#describeCustomVocabularyMetadata) | **GET** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/customvocabulary/DEFAULT/metadata | 
[**describeExport**](DefaultApi.md#describeExport) | **GET** /exports/{exportId}/ | 
[**describeImport**](DefaultApi.md#describeImport) | **GET** /imports/{importId}/ | 
[**describeIntent**](DefaultApi.md#describeIntent) | **GET** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/intents/{intentId}/ | 
[**describeResourcePolicy**](DefaultApi.md#describeResourcePolicy) | **GET** /policy/{resourceArn}/ | 
[**describeSlot**](DefaultApi.md#describeSlot) | **GET** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/intents/{intentId}/slots/{slotId}/ | 
[**describeSlotType**](DefaultApi.md#describeSlotType) | **GET** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/slottypes/{slotTypeId}/ | 
[**describeTestExecution**](DefaultApi.md#describeTestExecution) | **GET** /testexecutions/{testExecutionId} | 
[**describeTestSet**](DefaultApi.md#describeTestSet) | **GET** /testsets/{testSetId} | 
[**describeTestSetDiscrepancyReport**](DefaultApi.md#describeTestSetDiscrepancyReport) | **GET** /testsetdiscrepancy/{testSetDiscrepancyReportId} | 
[**describeTestSetGeneration**](DefaultApi.md#describeTestSetGeneration) | **GET** /testsetgenerations/{testSetGenerationId} | 
[**getTestExecutionArtifactsUrl**](DefaultApi.md#getTestExecutionArtifactsUrl) | **GET** /testexecutions/{testExecutionId}/artifacturl | 
[**listAggregatedUtterances**](DefaultApi.md#listAggregatedUtterances) | **POST** /bots/{botId}/aggregatedutterances/ | 
[**listBotAliases**](DefaultApi.md#listBotAliases) | **POST** /bots/{botId}/botaliases/ | 
[**listBotLocales**](DefaultApi.md#listBotLocales) | **POST** /bots/{botId}/botversions/{botVersion}/botlocales/ | 
[**listBotRecommendations**](DefaultApi.md#listBotRecommendations) | **POST** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/botrecommendations/ | 
[**listBotVersions**](DefaultApi.md#listBotVersions) | **POST** /bots/{botId}/botversions/ | 
[**listBots**](DefaultApi.md#listBots) | **POST** /bots/ | 
[**listBuiltInIntents**](DefaultApi.md#listBuiltInIntents) | **POST** /builtins/locales/{localeId}/intents/ | 
[**listBuiltInSlotTypes**](DefaultApi.md#listBuiltInSlotTypes) | **POST** /builtins/locales/{localeId}/slottypes/ | 
[**listCustomVocabularyItems**](DefaultApi.md#listCustomVocabularyItems) | **POST** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/customvocabulary/DEFAULT/list | 
[**listExports**](DefaultApi.md#listExports) | **POST** /exports/ | 
[**listImports**](DefaultApi.md#listImports) | **POST** /imports/ | 
[**listIntentMetrics**](DefaultApi.md#listIntentMetrics) | **POST** /bots/{botId}/analytics/intentmetrics | 
[**listIntentPaths**](DefaultApi.md#listIntentPaths) | **POST** /bots/{botId}/analytics/intentpaths | 
[**listIntentStageMetrics**](DefaultApi.md#listIntentStageMetrics) | **POST** /bots/{botId}/analytics/intentstagemetrics | 
[**listIntents**](DefaultApi.md#listIntents) | **POST** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/intents/ | 
[**listRecommendedIntents**](DefaultApi.md#listRecommendedIntents) | **POST** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/botrecommendations/{botRecommendationId}/intents | 
[**listSessionAnalyticsData**](DefaultApi.md#listSessionAnalyticsData) | **POST** /bots/{botId}/analytics/sessions | 
[**listSessionMetrics**](DefaultApi.md#listSessionMetrics) | **POST** /bots/{botId}/analytics/sessionmetrics | 
[**listSlotTypes**](DefaultApi.md#listSlotTypes) | **POST** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/slottypes/ | 
[**listSlots**](DefaultApi.md#listSlots) | **POST** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/intents/{intentId}/slots/ | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceARN} | 
[**listTestExecutionResultItems**](DefaultApi.md#listTestExecutionResultItems) | **POST** /testexecutions/{testExecutionId}/results | 
[**listTestExecutions**](DefaultApi.md#listTestExecutions) | **POST** /testexecutions | 
[**listTestSetRecords**](DefaultApi.md#listTestSetRecords) | **POST** /testsets/{testSetId}/records | 
[**listTestSets**](DefaultApi.md#listTestSets) | **POST** /testsets | 
[**listUtteranceAnalyticsData**](DefaultApi.md#listUtteranceAnalyticsData) | **POST** /bots/{botId}/analytics/utterances | 
[**listUtteranceMetrics**](DefaultApi.md#listUtteranceMetrics) | **POST** /bots/{botId}/analytics/utterancemetrics | 
[**searchAssociatedTranscripts**](DefaultApi.md#searchAssociatedTranscripts) | **POST** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/botrecommendations/{botRecommendationId}/associatedtranscripts | 
[**startBotRecommendation**](DefaultApi.md#startBotRecommendation) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/botrecommendations/ | 
[**startImport**](DefaultApi.md#startImport) | **PUT** /imports/ | 
[**startTestExecution**](DefaultApi.md#startTestExecution) | **POST** /testsets/{testSetId}/testexecutions | 
[**startTestSetGeneration**](DefaultApi.md#startTestSetGeneration) | **PUT** /testsetgenerations | 
[**stopBotRecommendation**](DefaultApi.md#stopBotRecommendation) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/botrecommendations/{botRecommendationId}/stopbotrecommendation | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceARN} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceARN}#tagKeys | 
[**updateBot**](DefaultApi.md#updateBot) | **PUT** /bots/{botId}/ | 
[**updateBotAlias**](DefaultApi.md#updateBotAlias) | **PUT** /bots/{botId}/botaliases/{botAliasId}/ | 
[**updateBotLocale**](DefaultApi.md#updateBotLocale) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/ | 
[**updateBotRecommendation**](DefaultApi.md#updateBotRecommendation) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/botrecommendations/{botRecommendationId}/ | 
[**updateExport**](DefaultApi.md#updateExport) | **PUT** /exports/{exportId}/ | 
[**updateIntent**](DefaultApi.md#updateIntent) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/intents/{intentId}/ | 
[**updateResourcePolicy**](DefaultApi.md#updateResourcePolicy) | **PUT** /policy/{resourceArn}/ | 
[**updateSlot**](DefaultApi.md#updateSlot) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/intents/{intentId}/slots/{slotId}/ | 
[**updateSlotType**](DefaultApi.md#updateSlotType) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/slottypes/{slotTypeId}/ | 
[**updateTestSet**](DefaultApi.md#updateTestSet) | **PUT** /testsets/{testSetId} | 



## batchCreateCustomVocabularyItem

> BatchCreateCustomVocabularyItemResponse batchCreateCustomVocabularyItem(botId, botVersion, localeId, batchCreateCustomVocabularyItemRequest, opts)



Create a batch of custom vocabulary items for a given bot locale&#39;s custom vocabulary.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier of the bot associated with this custom vocabulary.
let botVersion = "botVersion_example"; // String | The identifier of the version of the bot associated with this custom vocabulary.
let localeId = "localeId_example"; // String | The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\"> Supported Languages </a>.
let batchCreateCustomVocabularyItemRequest = new AmazonLexModelBuildingV2.BatchCreateCustomVocabularyItemRequest(); // BatchCreateCustomVocabularyItemRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchCreateCustomVocabularyItem(botId, botVersion, localeId, batchCreateCustomVocabularyItemRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier of the bot associated with this custom vocabulary. | 
 **botVersion** | **String**| The identifier of the version of the bot associated with this custom vocabulary. | 
 **localeId** | **String**| The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt; Supported Languages &lt;/a&gt;. | 
 **batchCreateCustomVocabularyItemRequest** | [**BatchCreateCustomVocabularyItemRequest**](BatchCreateCustomVocabularyItemRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchCreateCustomVocabularyItemResponse**](BatchCreateCustomVocabularyItemResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchDeleteCustomVocabularyItem

> BatchDeleteCustomVocabularyItemResponse batchDeleteCustomVocabularyItem(botId, botVersion, localeId, batchDeleteCustomVocabularyItemRequest, opts)



Delete a batch of custom vocabulary items for a given bot locale&#39;s custom vocabulary.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier of the bot associated with this custom vocabulary.
let botVersion = "botVersion_example"; // String | The identifier of the version of the bot associated with this custom vocabulary.
let localeId = "localeId_example"; // String | The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\"> Supported Languages </a>.
let batchDeleteCustomVocabularyItemRequest = new AmazonLexModelBuildingV2.BatchDeleteCustomVocabularyItemRequest(); // BatchDeleteCustomVocabularyItemRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchDeleteCustomVocabularyItem(botId, botVersion, localeId, batchDeleteCustomVocabularyItemRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier of the bot associated with this custom vocabulary. | 
 **botVersion** | **String**| The identifier of the version of the bot associated with this custom vocabulary. | 
 **localeId** | **String**| The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt; Supported Languages &lt;/a&gt;. | 
 **batchDeleteCustomVocabularyItemRequest** | [**BatchDeleteCustomVocabularyItemRequest**](BatchDeleteCustomVocabularyItemRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchDeleteCustomVocabularyItemResponse**](BatchDeleteCustomVocabularyItemResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchUpdateCustomVocabularyItem

> BatchUpdateCustomVocabularyItemResponse batchUpdateCustomVocabularyItem(botId, botVersion, localeId, batchUpdateCustomVocabularyItemRequest, opts)



Update a batch of custom vocabulary items for a given bot locale&#39;s custom vocabulary.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier of the bot associated with this custom vocabulary
let botVersion = "botVersion_example"; // String | The identifier of the version of the bot associated with this custom vocabulary.
let localeId = "localeId_example"; // String | The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\"> Supported Languages </a>.
let batchUpdateCustomVocabularyItemRequest = new AmazonLexModelBuildingV2.BatchUpdateCustomVocabularyItemRequest(); // BatchUpdateCustomVocabularyItemRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchUpdateCustomVocabularyItem(botId, botVersion, localeId, batchUpdateCustomVocabularyItemRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier of the bot associated with this custom vocabulary | 
 **botVersion** | **String**| The identifier of the version of the bot associated with this custom vocabulary. | 
 **localeId** | **String**| The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt; Supported Languages &lt;/a&gt;. | 
 **batchUpdateCustomVocabularyItemRequest** | [**BatchUpdateCustomVocabularyItemRequest**](BatchUpdateCustomVocabularyItemRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchUpdateCustomVocabularyItemResponse**](BatchUpdateCustomVocabularyItemResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## buildBotLocale

> BuildBotLocaleResponse buildBotLocale(botId, botVersion, localeId, opts)



Builds a bot, its intents, and its slot types into a specific locale. A bot can be built into multiple locales. At runtime the locale is used to choose a specific build of the bot.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier of the bot to build. The identifier is returned in the response from the <a href=\"https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html\">CreateBot</a> operation.
let botVersion = "botVersion_example"; // String | The version of the bot to build. This can only be the draft version of the bot.
let localeId = "localeId_example"; // String | The identifier of the language and locale that the bot will be used in. The string must match one of the supported locales. All of the intents, slot types, and slots used in the bot must have the same locale. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.buildBotLocale(botId, botVersion, localeId, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier of the bot to build. The identifier is returned in the response from the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html\&quot;&gt;CreateBot&lt;/a&gt; operation. | 
 **botVersion** | **String**| The version of the bot to build. This can only be the draft version of the bot. | 
 **localeId** | **String**| The identifier of the language and locale that the bot will be used in. The string must match one of the supported locales. All of the intents, slot types, and slots used in the bot must have the same locale. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BuildBotLocaleResponse**](BuildBotLocaleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createBot

> CreateBotResponse createBot(createBotRequest, opts)



Creates an Amazon Lex conversational bot. 

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let createBotRequest = new AmazonLexModelBuildingV2.CreateBotRequest(); // CreateBotRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createBot(createBotRequest, opts, (error, data, response) => {
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
 **createBotRequest** | [**CreateBotRequest**](CreateBotRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateBotResponse**](CreateBotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBotAlias

> CreateBotAliasResponse createBotAlias(botId, createBotAliasRequest, opts)



&lt;p&gt;Creates an alias for the specified version of a bot. Use an alias to enable you to change the version of a bot without updating applications that use the bot.&lt;/p&gt; &lt;p&gt;For example, you can create an alias called \&quot;PROD\&quot; that your applications use to call the Amazon Lex bot. &lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The unique identifier of the bot that the alias applies to.
let createBotAliasRequest = new AmazonLexModelBuildingV2.CreateBotAliasRequest(); // CreateBotAliasRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createBotAlias(botId, createBotAliasRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The unique identifier of the bot that the alias applies to. | 
 **createBotAliasRequest** | [**CreateBotAliasRequest**](CreateBotAliasRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateBotAliasResponse**](CreateBotAliasResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBotLocale

> CreateBotLocaleResponse createBotLocale(botId, botVersion, createBotLocaleRequest, opts)



Creates a locale in the bot. The locale contains the intents and slot types that the bot uses in conversations with users in the specified language and locale. You must add a locale to a bot before you can add intents and slot types to the bot.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier of the bot to create the locale for.
let botVersion = "botVersion_example"; // String | The version of the bot to create the locale for. This can only be the draft version of the bot.
let createBotLocaleRequest = new AmazonLexModelBuildingV2.CreateBotLocaleRequest(); // CreateBotLocaleRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createBotLocale(botId, botVersion, createBotLocaleRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier of the bot to create the locale for. | 
 **botVersion** | **String**| The version of the bot to create the locale for. This can only be the draft version of the bot. | 
 **createBotLocaleRequest** | [**CreateBotLocaleRequest**](CreateBotLocaleRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateBotLocaleResponse**](CreateBotLocaleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBotVersion

> CreateBotVersionResponse createBotVersion(botId, createBotVersionRequest, opts)



&lt;p&gt;Creates a new version of the bot based on the &lt;code&gt;DRAFT&lt;/code&gt; version. If the &lt;code&gt;DRAFT&lt;/code&gt; version of this resource hasn&#39;t changed since you created the last version, Amazon Lex doesn&#39;t create a new version, it returns the last created version.&lt;/p&gt; &lt;p&gt;When you create the first version of a bot, Amazon Lex sets the version to 1. Subsequent versions increment by 1.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier of the bot to create the version for.
let createBotVersionRequest = new AmazonLexModelBuildingV2.CreateBotVersionRequest(); // CreateBotVersionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createBotVersion(botId, createBotVersionRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier of the bot to create the version for. | 
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


## createExport

> CreateExportResponse createExport(createExportRequest, opts)



&lt;p&gt;Creates a zip archive containing the contents of a bot or a bot locale. The archive contains a directory structure that contains JSON files that define the bot.&lt;/p&gt; &lt;p&gt;You can create an archive that contains the complete definition of a bot, or you can specify that the archive contain only the definition of a single bot locale.&lt;/p&gt; &lt;p&gt;For more information about exporting bots, and about the structure of the export archive, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/importing-exporting.html\&quot;&gt; Importing and exporting bots &lt;/a&gt; &lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let createExportRequest = new AmazonLexModelBuildingV2.CreateExportRequest(); // CreateExportRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createExport(createExportRequest, opts, (error, data, response) => {
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
 **createExportRequest** | [**CreateExportRequest**](CreateExportRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateExportResponse**](CreateExportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createIntent

> CreateIntentResponse createIntent(botId, botVersion, localeId, createIntentRequest, opts)



&lt;p&gt;Creates an intent.&lt;/p&gt; &lt;p&gt;To define the interaction between the user and your bot, you define one or more intents. For example, for a pizza ordering bot you would create an &lt;code&gt;OrderPizza&lt;/code&gt; intent.&lt;/p&gt; &lt;p&gt;When you create an intent, you must provide a name. You can optionally provide the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Sample utterances. For example, \&quot;I want to order a pizza\&quot; and \&quot;Can I order a pizza.\&quot; You can&#39;t provide utterances for built-in intents.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Information to be gathered. You specify slots for the information that you bot requests from the user. You can specify standard slot types, such as date and time, or custom slot types for your application.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;How the intent is fulfilled. You can provide a Lambda function or configure the intent to return the intent information to your client application. If you use a Lambda function, Amazon Lex invokes the function when all of the intent information is available.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A confirmation prompt to send to the user to confirm an intent. For example, \&quot;Shall I order your pizza?\&quot;&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A conclusion statement to send to the user after the intent is fulfilled. For example, \&quot;I ordered your pizza.\&quot;&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A follow-up prompt that asks the user for additional activity. For example, \&quot;Do you want a drink with your pizza?\&quot;&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier of the bot associated with this intent.
let botVersion = "botVersion_example"; // String | The version of the bot associated with this intent.
let localeId = "localeId_example"; // String | The identifier of the language and locale where this intent is used. All of the bots, slot types, and slots used by the intent must have the same locale. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
let createIntentRequest = new AmazonLexModelBuildingV2.CreateIntentRequest(); // CreateIntentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createIntent(botId, botVersion, localeId, createIntentRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier of the bot associated with this intent. | 
 **botVersion** | **String**| The version of the bot associated with this intent. | 
 **localeId** | **String**| The identifier of the language and locale where this intent is used. All of the bots, slot types, and slots used by the intent must have the same locale. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
 **createIntentRequest** | [**CreateIntentRequest**](CreateIntentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateIntentResponse**](CreateIntentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createResourcePolicy

> CreateResourcePolicyResponse createResourcePolicy(resourceArn, updateResourcePolicyRequest, opts)



Creates a new resource policy with the specified policy statements.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.
let updateResourcePolicyRequest = new AmazonLexModelBuildingV2.UpdateResourcePolicyRequest(); // UpdateResourcePolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createResourcePolicy(resourceArn, updateResourcePolicyRequest, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to. | 
 **updateResourcePolicyRequest** | [**UpdateResourcePolicyRequest**](UpdateResourcePolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateResourcePolicyResponse**](CreateResourcePolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createResourcePolicyStatement

> CreateResourcePolicyStatementResponse createResourcePolicyStatement(resourceArn, createResourcePolicyStatementRequest, opts)



&lt;p&gt;Adds a new resource policy statement to a bot or bot alias. If a resource policy exists, the statement is added to the current resource policy. If a policy doesn&#39;t exist, a new policy is created.&lt;/p&gt; &lt;p&gt;You can&#39;t create a resource policy statement that allows cross-account access.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.
let createResourcePolicyStatementRequest = new AmazonLexModelBuildingV2.CreateResourcePolicyStatementRequest(); // CreateResourcePolicyStatementRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'expectedRevisionId': "expectedRevisionId_example" // String | <p>The identifier of the revision of the policy to edit. If this revision ID doesn't match the current revision ID, Amazon Lex throws an exception.</p> <p>If you don't specify a revision, Amazon Lex overwrites the contents of the policy with the new values.</p>
};
apiInstance.createResourcePolicyStatement(resourceArn, createResourcePolicyStatementRequest, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to. | 
 **createResourcePolicyStatementRequest** | [**CreateResourcePolicyStatementRequest**](CreateResourcePolicyStatementRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **expectedRevisionId** | **String**| &lt;p&gt;The identifier of the revision of the policy to edit. If this revision ID doesn&#39;t match the current revision ID, Amazon Lex throws an exception.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a revision, Amazon Lex overwrites the contents of the policy with the new values.&lt;/p&gt; | [optional] 

### Return type

[**CreateResourcePolicyStatementResponse**](CreateResourcePolicyStatementResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSlot

> CreateSlotResponse createSlot(botId, botVersion, localeId, intentId, createSlotRequest, opts)



Creates a slot in an intent. A slot is a variable needed to fulfill an intent. For example, an &lt;code&gt;OrderPizza&lt;/code&gt; intent might need slots for size, crust, and number of pizzas. For each slot, you define one or more utterances that Amazon Lex uses to elicit a response from the user. 

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier of the bot associated with the slot.
let botVersion = "botVersion_example"; // String | The version of the bot associated with the slot.
let localeId = "localeId_example"; // String | The identifier of the language and locale that the slot will be used in. The string must match one of the supported locales. All of the bots, intents, slot types used by the slot must have the same locale. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
let intentId = "intentId_example"; // String | The identifier of the intent that contains the slot.
let createSlotRequest = new AmazonLexModelBuildingV2.CreateSlotRequest(); // CreateSlotRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSlot(botId, botVersion, localeId, intentId, createSlotRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier of the bot associated with the slot. | 
 **botVersion** | **String**| The version of the bot associated with the slot. | 
 **localeId** | **String**| The identifier of the language and locale that the slot will be used in. The string must match one of the supported locales. All of the bots, intents, slot types used by the slot must have the same locale. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
 **intentId** | **String**| The identifier of the intent that contains the slot. | 
 **createSlotRequest** | [**CreateSlotRequest**](CreateSlotRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSlotResponse**](CreateSlotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSlotType

> CreateSlotTypeResponse createSlotType(botId, botVersion, localeId, createSlotTypeRequest, opts)



&lt;p&gt;Creates a custom slot type&lt;/p&gt; &lt;p&gt; To create a custom slot type, specify a name for the slot type and a set of enumeration values, the values that a slot of this type can assume. &lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier of the bot associated with this slot type.
let botVersion = "botVersion_example"; // String | The identifier of the bot version associated with this slot type.
let localeId = "localeId_example"; // String | The identifier of the language and locale that the slot type will be used in. The string must match one of the supported locales. All of the bots, intents, and slots used by the slot type must have the same locale. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
let createSlotTypeRequest = new AmazonLexModelBuildingV2.CreateSlotTypeRequest(); // CreateSlotTypeRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSlotType(botId, botVersion, localeId, createSlotTypeRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier of the bot associated with this slot type. | 
 **botVersion** | **String**| The identifier of the bot version associated with this slot type. | 
 **localeId** | **String**| The identifier of the language and locale that the slot type will be used in. The string must match one of the supported locales. All of the bots, intents, and slots used by the slot type must have the same locale. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
 **createSlotTypeRequest** | [**CreateSlotTypeRequest**](CreateSlotTypeRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSlotTypeResponse**](CreateSlotTypeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTestSetDiscrepancyReport

> CreateTestSetDiscrepancyReportResponse createTestSetDiscrepancyReport(testSetId, createTestSetDiscrepancyReportRequest, opts)



Create a report that describes the differences between the bot and the test set.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let testSetId = "testSetId_example"; // String | The test set Id for the test set discrepancy report.
let createTestSetDiscrepancyReportRequest = new AmazonLexModelBuildingV2.CreateTestSetDiscrepancyReportRequest(); // CreateTestSetDiscrepancyReportRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createTestSetDiscrepancyReport(testSetId, createTestSetDiscrepancyReportRequest, opts, (error, data, response) => {
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
 **testSetId** | **String**| The test set Id for the test set discrepancy report. | 
 **createTestSetDiscrepancyReportRequest** | [**CreateTestSetDiscrepancyReportRequest**](CreateTestSetDiscrepancyReportRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateTestSetDiscrepancyReportResponse**](CreateTestSetDiscrepancyReportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createUploadUrl

> CreateUploadUrlResponse createUploadUrl(opts)



Gets a pre-signed S3 write URL that you use to upload the zip archive when importing a bot or a bot locale. 

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createUploadUrl(opts, (error, data, response) => {
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

### Return type

[**CreateUploadUrlResponse**](CreateUploadUrlResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteBot

> DeleteBotResponse deleteBot(botId, opts)



&lt;p&gt;Deletes all versions of a bot, including the &lt;code&gt;Draft&lt;/code&gt; version. To delete a specific version, use the &lt;code&gt;DeleteBotVersion&lt;/code&gt; operation.&lt;/p&gt; &lt;p&gt;When you delete a bot, all of the resources contained in the bot are also deleted. Deleting a bot removes all locales, intents, slot, and slot types defined for the bot.&lt;/p&gt; &lt;p&gt;If a bot has an alias, the &lt;code&gt;DeleteBot&lt;/code&gt; operation returns a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception. If you want to delete the bot and the alias, set the &lt;code&gt;skipResourceInUseCheck&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier of the bot to delete. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'skipResourceInUseCheck': true // Boolean | By default, Amazon Lex checks if any other resource, such as an alias or bot network, is using the bot version before it is deleted and throws a <code>ResourceInUseException</code> exception if the bot is being used by another resource. Set this parameter to <code>true</code> to skip this check and remove the bot even if it is being used by another resource.
};
apiInstance.deleteBot(botId, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier of the bot to delete.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **skipResourceInUseCheck** | **Boolean**| By default, Amazon Lex checks if any other resource, such as an alias or bot network, is using the bot version before it is deleted and throws a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception if the bot is being used by another resource. Set this parameter to &lt;code&gt;true&lt;/code&gt; to skip this check and remove the bot even if it is being used by another resource. | [optional] 

### Return type

[**DeleteBotResponse**](DeleteBotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteBotAlias

> DeleteBotAliasResponse deleteBotAlias(botAliasId, botId, opts)



Deletes the specified bot alias.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botAliasId = "botAliasId_example"; // String | The unique identifier of the bot alias to delete.
let botId = "botId_example"; // String | The unique identifier of the bot associated with the alias to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'skipResourceInUseCheck': true // Boolean | By default, Amazon Lex checks if any other resource, such as a bot network, is using the bot alias before it is deleted and throws a <code>ResourceInUseException</code> exception if the alias is being used by another resource. Set this parameter to <code>true</code> to skip this check and remove the alias even if it is being used by another resource.
};
apiInstance.deleteBotAlias(botAliasId, botId, opts, (error, data, response) => {
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
 **botAliasId** | **String**| The unique identifier of the bot alias to delete. | 
 **botId** | **String**| The unique identifier of the bot associated with the alias to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **skipResourceInUseCheck** | **Boolean**| By default, Amazon Lex checks if any other resource, such as a bot network, is using the bot alias before it is deleted and throws a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception if the alias is being used by another resource. Set this parameter to &lt;code&gt;true&lt;/code&gt; to skip this check and remove the alias even if it is being used by another resource. | [optional] 

### Return type

[**DeleteBotAliasResponse**](DeleteBotAliasResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteBotLocale

> DeleteBotLocaleResponse deleteBotLocale(botId, botVersion, localeId, opts)



&lt;p&gt;Removes a locale from a bot.&lt;/p&gt; &lt;p&gt;When you delete a locale, all intents, slots, and slot types defined for the locale are also deleted.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The unique identifier of the bot that contains the locale.
let botVersion = "botVersion_example"; // String | The version of the bot that contains the locale. 
let localeId = "localeId_example"; // String | The identifier of the language and locale that will be deleted. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBotLocale(botId, botVersion, localeId, opts, (error, data, response) => {
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
 **botId** | **String**| The unique identifier of the bot that contains the locale. | 
 **botVersion** | **String**| The version of the bot that contains the locale.  | 
 **localeId** | **String**| The identifier of the language and locale that will be deleted. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteBotLocaleResponse**](DeleteBotLocaleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteBotVersion

> DeleteBotVersionResponse deleteBotVersion(botId, botVersion, opts)



Deletes a specific version of a bot. To delete all versions of a bot, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteBot.html\&quot;&gt;DeleteBot&lt;/a&gt; operation.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier of the bot that contains the version.
let botVersion = "botVersion_example"; // String | The version of the bot to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'skipResourceInUseCheck': true // Boolean | By default, Amazon Lex checks if any other resource, such as an alias or bot network, is using the bot version before it is deleted and throws a <code>ResourceInUseException</code> exception if the version is being used by another resource. Set this parameter to <code>true</code> to skip this check and remove the version even if it is being used by another resource.
};
apiInstance.deleteBotVersion(botId, botVersion, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier of the bot that contains the version. | 
 **botVersion** | **String**| The version of the bot to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **skipResourceInUseCheck** | **Boolean**| By default, Amazon Lex checks if any other resource, such as an alias or bot network, is using the bot version before it is deleted and throws a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception if the version is being used by another resource. Set this parameter to &lt;code&gt;true&lt;/code&gt; to skip this check and remove the version even if it is being used by another resource. | [optional] 

### Return type

[**DeleteBotVersionResponse**](DeleteBotVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteCustomVocabulary

> DeleteCustomVocabularyResponse deleteCustomVocabulary(botId, botVersion, localeId, opts)



Removes a custom vocabulary from the specified locale in the specified bot.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The unique identifier of the bot to remove the custom vocabulary from.
let botVersion = "botVersion_example"; // String | The version of the bot to remove the custom vocabulary from.
let localeId = "localeId_example"; // String | The locale identifier for the locale that contains the custom vocabulary to remove.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteCustomVocabulary(botId, botVersion, localeId, opts, (error, data, response) => {
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
 **botId** | **String**| The unique identifier of the bot to remove the custom vocabulary from. | 
 **botVersion** | **String**| The version of the bot to remove the custom vocabulary from. | 
 **localeId** | **String**| The locale identifier for the locale that contains the custom vocabulary to remove. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteCustomVocabularyResponse**](DeleteCustomVocabularyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteExport

> DeleteExportResponse deleteExport(exportId, opts)



Removes a previous export and the associated files stored in an S3 bucket.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let exportId = "exportId_example"; // String | The unique identifier of the export to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteExport(exportId, opts, (error, data, response) => {
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
 **exportId** | **String**| The unique identifier of the export to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteExportResponse**](DeleteExportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteImport

> DeleteImportResponse deleteImport(importId, opts)



Removes a previous import and the associated file stored in an S3 bucket.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let importId = "importId_example"; // String | The unique identifier of the import to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteImport(importId, opts, (error, data, response) => {
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
 **importId** | **String**| The unique identifier of the import to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteImportResponse**](DeleteImportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteIntent

> deleteIntent(intentId, botId, botVersion, localeId, opts)



&lt;p&gt;Removes the specified intent.&lt;/p&gt; &lt;p&gt;Deleting an intent also deletes the slots associated with the intent.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let intentId = "intentId_example"; // String | The unique identifier of the intent to delete.
let botId = "botId_example"; // String | The identifier of the bot associated with the intent.
let botVersion = "botVersion_example"; // String | The version of the bot associated with the intent.
let localeId = "localeId_example"; // String | The identifier of the language and locale where the bot will be deleted. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteIntent(intentId, botId, botVersion, localeId, opts, (error, data, response) => {
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
 **intentId** | **String**| The unique identifier of the intent to delete. | 
 **botId** | **String**| The identifier of the bot associated with the intent. | 
 **botVersion** | **String**| The version of the bot associated with the intent. | 
 **localeId** | **String**| The identifier of the language and locale where the bot will be deleted. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
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


## deleteResourcePolicy

> DeleteResourcePolicyResponse deleteResourcePolicy(resourceArn, opts)



Removes an existing policy from a bot or bot alias. If the resource doesn&#39;t have a policy attached, Amazon Lex returns an exception.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the bot or bot alias that has the resource policy attached.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'expectedRevisionId': "expectedRevisionId_example" // String | <p>The identifier of the revision to edit. If this ID doesn't match the current revision number, Amazon Lex returns an exception</p> <p>If you don't specify a revision ID, Amazon Lex will delete the current policy.</p>
};
apiInstance.deleteResourcePolicy(resourceArn, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the bot or bot alias that has the resource policy attached. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **expectedRevisionId** | **String**| &lt;p&gt;The identifier of the revision to edit. If this ID doesn&#39;t match the current revision number, Amazon Lex returns an exception&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a revision ID, Amazon Lex will delete the current policy.&lt;/p&gt; | [optional] 

### Return type

[**DeleteResourcePolicyResponse**](DeleteResourcePolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteResourcePolicyStatement

> DeleteResourcePolicyStatementResponse deleteResourcePolicyStatement(resourceArn, statementId, opts)



Deletes a policy statement from a resource policy. If you delete the last statement from a policy, the policy is deleted. If you specify a statement ID that doesn&#39;t exist in the policy, or if the bot or bot alias doesn&#39;t have a policy attached, Amazon Lex returns an exception.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.
let statementId = "statementId_example"; // String | The name of the statement (SID) to delete from the policy.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'expectedRevisionId': "expectedRevisionId_example" // String | <p>The identifier of the revision of the policy to delete the statement from. If this revision ID doesn't match the current revision ID, Amazon Lex throws an exception.</p> <p>If you don't specify a revision, Amazon Lex removes the current contents of the statement. </p>
};
apiInstance.deleteResourcePolicyStatement(resourceArn, statementId, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to. | 
 **statementId** | **String**| The name of the statement (SID) to delete from the policy. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **expectedRevisionId** | **String**| &lt;p&gt;The identifier of the revision of the policy to delete the statement from. If this revision ID doesn&#39;t match the current revision ID, Amazon Lex throws an exception.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a revision, Amazon Lex removes the current contents of the statement. &lt;/p&gt; | [optional] 

### Return type

[**DeleteResourcePolicyStatementResponse**](DeleteResourcePolicyStatementResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSlot

> deleteSlot(slotId, botId, botVersion, localeId, intentId, opts)



Deletes the specified slot from an intent.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let slotId = "slotId_example"; // String | The identifier of the slot to delete. 
let botId = "botId_example"; // String | The identifier of the bot associated with the slot to delete.
let botVersion = "botVersion_example"; // String | The version of the bot associated with the slot to delete.
let localeId = "localeId_example"; // String | The identifier of the language and locale that the slot will be deleted from. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
let intentId = "intentId_example"; // String | The identifier of the intent associated with the slot.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSlot(slotId, botId, botVersion, localeId, intentId, opts, (error, data, response) => {
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
 **slotId** | **String**| The identifier of the slot to delete.  | 
 **botId** | **String**| The identifier of the bot associated with the slot to delete. | 
 **botVersion** | **String**| The version of the bot associated with the slot to delete. | 
 **localeId** | **String**| The identifier of the language and locale that the slot will be deleted from. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
 **intentId** | **String**| The identifier of the intent associated with the slot. | 
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

> deleteSlotType(slotTypeId, botId, botVersion, localeId, opts)



&lt;p&gt;Deletes a slot type from a bot locale.&lt;/p&gt; &lt;p&gt;If a slot is using the slot type, Amazon Lex throws a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception. To avoid the exception, set the &lt;code&gt;skipResourceInUseCheck&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let slotTypeId = "slotTypeId_example"; // String | The identifier of the slot type to delete.
let botId = "botId_example"; // String | The identifier of the bot associated with the slot type.
let botVersion = "botVersion_example"; // String | The version of the bot associated with the slot type.
let localeId = "localeId_example"; // String | The identifier of the language and locale that the slot type will be deleted from. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'skipResourceInUseCheck': true // Boolean | By default, the <code>DeleteSlotType</code> operations throws a <code>ResourceInUseException</code> exception if you try to delete a slot type used by a slot. Set the <code>skipResourceInUseCheck</code> parameter to <code>true</code> to skip this check and remove the slot type even if a slot uses it.
};
apiInstance.deleteSlotType(slotTypeId, botId, botVersion, localeId, opts, (error, data, response) => {
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
 **slotTypeId** | **String**| The identifier of the slot type to delete. | 
 **botId** | **String**| The identifier of the bot associated with the slot type. | 
 **botVersion** | **String**| The version of the bot associated with the slot type. | 
 **localeId** | **String**| The identifier of the language and locale that the slot type will be deleted from. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **skipResourceInUseCheck** | **Boolean**| By default, the &lt;code&gt;DeleteSlotType&lt;/code&gt; operations throws a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception if you try to delete a slot type used by a slot. Set the &lt;code&gt;skipResourceInUseCheck&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt; to skip this check and remove the slot type even if a slot uses it. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTestSet

> deleteTestSet(testSetId, opts)



The action to delete the selected test set.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let testSetId = "testSetId_example"; // String | The test set Id of the test set to be deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteTestSet(testSetId, opts, (error, data, response) => {
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
 **testSetId** | **String**| The test set Id of the test set to be deleted. | 
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

> Object deleteUtterances(botId, opts)



&lt;p&gt;Deletes stored utterances.&lt;/p&gt; &lt;p&gt;Amazon Lex stores the utterances that users send to your bot. Utterances are stored for 15 days for use with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListAggregatedUtterances.html\&quot;&gt;ListAggregatedUtterances&lt;/a&gt; operation, and then stored indefinitely for use in improving the ability of your bot to respond to user input..&lt;/p&gt; &lt;p&gt;Use the &lt;code&gt;DeleteUtterances&lt;/code&gt; operation to manually delete utterances for a specific session. When you use the &lt;code&gt;DeleteUtterances&lt;/code&gt; operation, utterances stored for improving your bot&#39;s ability to respond to user input are deleted immediately. Utterances stored for use with the &lt;code&gt;ListAggregatedUtterances&lt;/code&gt; operation are deleted after 15 days.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The unique identifier of the bot that contains the utterances.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'localeId': "localeId_example", // String | The identifier of the language and locale where the utterances were collected. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
  'sessionId': "sessionId_example" // String | The unique identifier of the session with the user. The ID is returned in the response from the <a href=\"https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeText.html\">RecognizeText</a> and <a href=\"https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeUtterance.html\">RecognizeUtterance</a> operations.
};
apiInstance.deleteUtterances(botId, opts, (error, data, response) => {
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
 **botId** | **String**| The unique identifier of the bot that contains the utterances. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **localeId** | **String**| The identifier of the language and locale where the utterances were collected. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | [optional] 
 **sessionId** | **String**| The unique identifier of the session with the user. The ID is returned in the response from the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeText.html\&quot;&gt;RecognizeText&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeUtterance.html\&quot;&gt;RecognizeUtterance&lt;/a&gt; operations. | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeBot

> DescribeBotResponse describeBot(botId, opts)



Provides metadata information about a bot. 

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The unique identifier of the bot to describe.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeBot(botId, opts, (error, data, response) => {
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
 **botId** | **String**| The unique identifier of the bot to describe. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeBotResponse**](DescribeBotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeBotAlias

> DescribeBotAliasResponse describeBotAlias(botAliasId, botId, opts)



Get information about a specific bot alias.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botAliasId = "botAliasId_example"; // String | The identifier of the bot alias to describe.
let botId = "botId_example"; // String | The identifier of the bot associated with the bot alias to describe.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeBotAlias(botAliasId, botId, opts, (error, data, response) => {
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
 **botAliasId** | **String**| The identifier of the bot alias to describe. | 
 **botId** | **String**| The identifier of the bot associated with the bot alias to describe. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeBotAliasResponse**](DescribeBotAliasResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeBotLocale

> DescribeBotLocaleResponse describeBotLocale(botId, botVersion, localeId, opts)



Describes the settings that a bot has for a specific locale. 

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier of the bot associated with the locale.
let botVersion = "botVersion_example"; // String | The version of the bot associated with the locale.
let localeId = "localeId_example"; // String | The unique identifier of the locale to describe. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeBotLocale(botId, botVersion, localeId, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier of the bot associated with the locale. | 
 **botVersion** | **String**| The version of the bot associated with the locale. | 
 **localeId** | **String**| The unique identifier of the locale to describe. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeBotLocaleResponse**](DescribeBotLocaleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeBotRecommendation

> DescribeBotRecommendationResponse describeBotRecommendation(botId, botVersion, localeId, botRecommendationId, opts)



Provides metadata information about a bot recommendation. This information will enable you to get a description on the request inputs, to download associated transcripts after processing is complete, and to download intents and slot-types generated by the bot recommendation.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The unique identifier of the bot associated with the bot recommendation.
let botVersion = "botVersion_example"; // String | The version of the bot associated with the bot recommendation.
let localeId = "localeId_example"; // String | The identifier of the language and locale of the bot recommendation to describe. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
let botRecommendationId = "botRecommendationId_example"; // String | The identifier of the bot recommendation to describe.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeBotRecommendation(botId, botVersion, localeId, botRecommendationId, opts, (error, data, response) => {
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
 **botId** | **String**| The unique identifier of the bot associated with the bot recommendation. | 
 **botVersion** | **String**| The version of the bot associated with the bot recommendation. | 
 **localeId** | **String**| The identifier of the language and locale of the bot recommendation to describe. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
 **botRecommendationId** | **String**| The identifier of the bot recommendation to describe. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeBotRecommendationResponse**](DescribeBotRecommendationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeBotVersion

> DescribeBotVersionResponse describeBotVersion(botId, botVersion, opts)



Provides metadata about a version of a bot.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier of the bot containing the version to return metadata for.
let botVersion = "botVersion_example"; // String | The version of the bot to return metadata for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeBotVersion(botId, botVersion, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier of the bot containing the version to return metadata for. | 
 **botVersion** | **String**| The version of the bot to return metadata for. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeBotVersionResponse**](DescribeBotVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeCustomVocabularyMetadata

> DescribeCustomVocabularyMetadataResponse describeCustomVocabularyMetadata(botId, botVersion, localeId, opts)



Provides metadata information about a custom vocabulary.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The unique identifier of the bot that contains the custom vocabulary.
let botVersion = "botVersion_example"; // String | The bot version of the bot to return metadata for.
let localeId = "localeId_example"; // String | The locale to return the custom vocabulary information for. The locale must be <code>en_GB</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeCustomVocabularyMetadata(botId, botVersion, localeId, opts, (error, data, response) => {
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
 **botId** | **String**| The unique identifier of the bot that contains the custom vocabulary. | 
 **botVersion** | **String**| The bot version of the bot to return metadata for. | 
 **localeId** | **String**| The locale to return the custom vocabulary information for. The locale must be &lt;code&gt;en_GB&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeCustomVocabularyMetadataResponse**](DescribeCustomVocabularyMetadataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeExport

> DescribeExportResponse describeExport(exportId, opts)



Gets information about a specific export.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let exportId = "exportId_example"; // String | The unique identifier of the export to describe.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeExport(exportId, opts, (error, data, response) => {
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
 **exportId** | **String**| The unique identifier of the export to describe. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeExportResponse**](DescribeExportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeImport

> DescribeImportResponse describeImport(importId, opts)



Gets information about a specific import.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let importId = "importId_example"; // String | The unique identifier of the import to describe.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeImport(importId, opts, (error, data, response) => {
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
 **importId** | **String**| The unique identifier of the import to describe. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeImportResponse**](DescribeImportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeIntent

> DescribeIntentResponse describeIntent(intentId, botId, botVersion, localeId, opts)



Returns metadata about an intent.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let intentId = "intentId_example"; // String | The identifier of the intent to describe.
let botId = "botId_example"; // String | The identifier of the bot associated with the intent.
let botVersion = "botVersion_example"; // String | The version of the bot associated with the intent.
let localeId = "localeId_example"; // String | The identifier of the language and locale of the intent to describe. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeIntent(intentId, botId, botVersion, localeId, opts, (error, data, response) => {
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
 **intentId** | **String**| The identifier of the intent to describe. | 
 **botId** | **String**| The identifier of the bot associated with the intent. | 
 **botVersion** | **String**| The version of the bot associated with the intent. | 
 **localeId** | **String**| The identifier of the language and locale of the intent to describe. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeIntentResponse**](DescribeIntentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeResourcePolicy

> DescribeResourcePolicyResponse describeResourcePolicy(resourceArn, opts)



Gets the resource policy and policy revision for a bot or bot alias.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeResourcePolicy(resourceArn, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeResourcePolicyResponse**](DescribeResourcePolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeSlot

> DescribeSlotResponse describeSlot(slotId, botId, botVersion, localeId, intentId, opts)



Gets metadata information about a slot.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let slotId = "slotId_example"; // String | The unique identifier for the slot.
let botId = "botId_example"; // String | The identifier of the bot associated with the slot.
let botVersion = "botVersion_example"; // String | The version of the bot associated with the slot.
let localeId = "localeId_example"; // String | The identifier of the language and locale of the slot to describe. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
let intentId = "intentId_example"; // String | The identifier of the intent that contains the slot.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeSlot(slotId, botId, botVersion, localeId, intentId, opts, (error, data, response) => {
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
 **slotId** | **String**| The unique identifier for the slot. | 
 **botId** | **String**| The identifier of the bot associated with the slot. | 
 **botVersion** | **String**| The version of the bot associated with the slot. | 
 **localeId** | **String**| The identifier of the language and locale of the slot to describe. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
 **intentId** | **String**| The identifier of the intent that contains the slot. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeSlotResponse**](DescribeSlotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeSlotType

> DescribeSlotTypeResponse describeSlotType(slotTypeId, botId, botVersion, localeId, opts)



Gets metadata information about a slot type.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let slotTypeId = "slotTypeId_example"; // String | The identifier of the slot type.
let botId = "botId_example"; // String | The identifier of the bot associated with the slot type.
let botVersion = "botVersion_example"; // String | The version of the bot associated with the slot type.
let localeId = "localeId_example"; // String | The identifier of the language and locale of the slot type to describe. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeSlotType(slotTypeId, botId, botVersion, localeId, opts, (error, data, response) => {
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
 **slotTypeId** | **String**| The identifier of the slot type. | 
 **botId** | **String**| The identifier of the bot associated with the slot type. | 
 **botVersion** | **String**| The version of the bot associated with the slot type. | 
 **localeId** | **String**| The identifier of the language and locale of the slot type to describe. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeSlotTypeResponse**](DescribeSlotTypeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeTestExecution

> DescribeTestExecutionResponse describeTestExecution(testExecutionId, opts)



Gets metadata information about the test execution.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let testExecutionId = "testExecutionId_example"; // String | The execution Id of the test set execution.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeTestExecution(testExecutionId, opts, (error, data, response) => {
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
 **testExecutionId** | **String**| The execution Id of the test set execution. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeTestExecutionResponse**](DescribeTestExecutionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeTestSet

> DescribeTestSetResponse describeTestSet(testSetId, opts)



Gets metadata information about the test set.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let testSetId = "testSetId_example"; // String | The test set Id for the test set request.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeTestSet(testSetId, opts, (error, data, response) => {
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
 **testSetId** | **String**| The test set Id for the test set request. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeTestSetResponse**](DescribeTestSetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeTestSetDiscrepancyReport

> DescribeTestSetDiscrepancyReportResponse describeTestSetDiscrepancyReport(testSetDiscrepancyReportId, opts)



Gets metadata information about the test set discrepancy report.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let testSetDiscrepancyReportId = "testSetDiscrepancyReportId_example"; // String | The unique identifier of the test set discrepancy report.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeTestSetDiscrepancyReport(testSetDiscrepancyReportId, opts, (error, data, response) => {
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
 **testSetDiscrepancyReportId** | **String**| The unique identifier of the test set discrepancy report. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeTestSetDiscrepancyReportResponse**](DescribeTestSetDiscrepancyReportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeTestSetGeneration

> DescribeTestSetGenerationResponse describeTestSetGeneration(testSetGenerationId, opts)



Gets metadata information about the test set generation.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let testSetGenerationId = "testSetGenerationId_example"; // String | The unique identifier of the test set generation.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeTestSetGeneration(testSetGenerationId, opts, (error, data, response) => {
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
 **testSetGenerationId** | **String**| The unique identifier of the test set generation. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeTestSetGenerationResponse**](DescribeTestSetGenerationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTestExecutionArtifactsUrl

> GetTestExecutionArtifactsUrlResponse getTestExecutionArtifactsUrl(testExecutionId, opts)



The pre-signed Amazon S3 URL to download the test execution result artifacts.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let testExecutionId = "testExecutionId_example"; // String | The unique identifier of the completed test execution.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getTestExecutionArtifactsUrl(testExecutionId, opts, (error, data, response) => {
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
 **testExecutionId** | **String**| The unique identifier of the completed test execution. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetTestExecutionArtifactsUrlResponse**](GetTestExecutionArtifactsUrlResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAggregatedUtterances

> ListAggregatedUtterancesResponse listAggregatedUtterances(botId, listAggregatedUtterancesRequest, opts)



&lt;p&gt;Provides a list of utterances that users have sent to the bot.&lt;/p&gt; &lt;p&gt;Utterances are aggregated by the text of the utterance. For example, all instances where customers used the phrase \&quot;I want to order pizza\&quot; are aggregated into the same line in the response.&lt;/p&gt; &lt;p&gt;You can see both detected utterances and missed utterances. A detected utterance is where the bot properly recognized the utterance and activated the associated intent. A missed utterance was not recognized by the bot and didn&#39;t activate an intent.&lt;/p&gt; &lt;p&gt;Utterances can be aggregated for a bot alias or for a bot version, but not both at the same time.&lt;/p&gt; &lt;p&gt;Utterances statistics are not generated under the following conditions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;childDirected&lt;/code&gt; field was set to true when the bot was created.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You are using slot obfuscation with one or more slots.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You opted out of participating in improving Amazon Lex.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The unique identifier of the bot associated with this request.
let listAggregatedUtterancesRequest = new AmazonLexModelBuildingV2.ListAggregatedUtterancesRequest(); // ListAggregatedUtterancesRequest | 
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
apiInstance.listAggregatedUtterances(botId, listAggregatedUtterancesRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The unique identifier of the bot associated with this request. | 
 **listAggregatedUtterancesRequest** | [**ListAggregatedUtterancesRequest**](ListAggregatedUtterancesRequest.md)|  | 
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

[**ListAggregatedUtterancesResponse**](ListAggregatedUtterancesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listBotAliases

> ListBotAliasesResponse listBotAliases(botId, listBotAliasesRequest, opts)



Gets a list of aliases for the specified bot.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier of the bot to list aliases for.
let listBotAliasesRequest = new AmazonLexModelBuildingV2.ListBotAliasesRequest(); // ListBotAliasesRequest | 
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
apiInstance.listBotAliases(botId, listBotAliasesRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier of the bot to list aliases for. | 
 **listBotAliasesRequest** | [**ListBotAliasesRequest**](ListBotAliasesRequest.md)|  | 
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

[**ListBotAliasesResponse**](ListBotAliasesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listBotLocales

> ListBotLocalesResponse listBotLocales(botId, botVersion, listBotLocalesRequest, opts)



Gets a list of locales for the specified bot.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier of the bot to list locales for.
let botVersion = "botVersion_example"; // String | The version of the bot to list locales for.
let listBotLocalesRequest = new AmazonLexModelBuildingV2.ListBotLocalesRequest(); // ListBotLocalesRequest | 
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
apiInstance.listBotLocales(botId, botVersion, listBotLocalesRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier of the bot to list locales for. | 
 **botVersion** | **String**| The version of the bot to list locales for. | 
 **listBotLocalesRequest** | [**ListBotLocalesRequest**](ListBotLocalesRequest.md)|  | 
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

[**ListBotLocalesResponse**](ListBotLocalesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listBotRecommendations

> ListBotRecommendationsResponse listBotRecommendations(botId, botVersion, localeId, listBotRecommendationsRequest, opts)



Get a list of bot recommendations that meet the specified criteria.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The unique identifier of the bot that contains the bot recommendation list.
let botVersion = "botVersion_example"; // String | The version of the bot that contains the bot recommendation list.
let localeId = "localeId_example"; // String | The identifier of the language and locale of the bot recommendation list.
let listBotRecommendationsRequest = new AmazonLexModelBuildingV2.ListBotRecommendationsRequest(); // ListBotRecommendationsRequest | 
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
apiInstance.listBotRecommendations(botId, botVersion, localeId, listBotRecommendationsRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The unique identifier of the bot that contains the bot recommendation list. | 
 **botVersion** | **String**| The version of the bot that contains the bot recommendation list. | 
 **localeId** | **String**| The identifier of the language and locale of the bot recommendation list. | 
 **listBotRecommendationsRequest** | [**ListBotRecommendationsRequest**](ListBotRecommendationsRequest.md)|  | 
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

[**ListBotRecommendationsResponse**](ListBotRecommendationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listBotVersions

> ListBotVersionsResponse listBotVersions(botId, listBotVersionsRequest, opts)



&lt;p&gt;Gets information about all of the versions of a bot.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;ListBotVersions&lt;/code&gt; operation returns a summary of each version of a bot. For example, if a bot has three numbered versions, the &lt;code&gt;ListBotVersions&lt;/code&gt; operation returns for summaries, one for each numbered version and one for the &lt;code&gt;DRAFT&lt;/code&gt; version.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;ListBotVersions&lt;/code&gt; operation always returns at least one version, the &lt;code&gt;DRAFT&lt;/code&gt; version.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier of the bot to list versions for.
let listBotVersionsRequest = new AmazonLexModelBuildingV2.ListBotVersionsRequest(); // ListBotVersionsRequest | 
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
apiInstance.listBotVersions(botId, listBotVersionsRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier of the bot to list versions for. | 
 **listBotVersionsRequest** | [**ListBotVersionsRequest**](ListBotVersionsRequest.md)|  | 
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

[**ListBotVersionsResponse**](ListBotVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listBots

> ListBotsResponse listBots(listBotsRequest, opts)



Gets a list of available bots.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let listBotsRequest = new AmazonLexModelBuildingV2.ListBotsRequest(); // ListBotsRequest | 
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
apiInstance.listBots(listBotsRequest, opts, (error, data, response) => {
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
 **listBotsRequest** | [**ListBotsRequest**](ListBotsRequest.md)|  | 
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

[**ListBotsResponse**](ListBotsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listBuiltInIntents

> ListBuiltInIntentsResponse listBuiltInIntents(localeId, listBuiltInIntentsRequest, opts)



&lt;p&gt;Gets a list of built-in intents provided by Amazon Lex that you can use in your bot. &lt;/p&gt; &lt;p&gt;To use a built-in intent as a the base for your own intent, include the built-in intent signature in the &lt;code&gt;parentIntentSignature&lt;/code&gt; parameter when you call the &lt;code&gt;CreateIntent&lt;/code&gt; operation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateIntent.html\&quot;&gt;CreateIntent&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let localeId = "localeId_example"; // String | The identifier of the language and locale of the intents to list. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
let listBuiltInIntentsRequest = new AmazonLexModelBuildingV2.ListBuiltInIntentsRequest(); // ListBuiltInIntentsRequest | 
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
apiInstance.listBuiltInIntents(localeId, listBuiltInIntentsRequest, opts, (error, data, response) => {
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
 **localeId** | **String**| The identifier of the language and locale of the intents to list. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
 **listBuiltInIntentsRequest** | [**ListBuiltInIntentsRequest**](ListBuiltInIntentsRequest.md)|  | 
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

[**ListBuiltInIntentsResponse**](ListBuiltInIntentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listBuiltInSlotTypes

> ListBuiltInSlotTypesResponse listBuiltInSlotTypes(localeId, listBuiltInSlotTypesRequest, opts)



Gets a list of built-in slot types that meet the specified criteria.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let localeId = "localeId_example"; // String | The identifier of the language and locale of the slot types to list. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
let listBuiltInSlotTypesRequest = new AmazonLexModelBuildingV2.ListBuiltInSlotTypesRequest(); // ListBuiltInSlotTypesRequest | 
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
apiInstance.listBuiltInSlotTypes(localeId, listBuiltInSlotTypesRequest, opts, (error, data, response) => {
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
 **localeId** | **String**| The identifier of the language and locale of the slot types to list. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
 **listBuiltInSlotTypesRequest** | [**ListBuiltInSlotTypesRequest**](ListBuiltInSlotTypesRequest.md)|  | 
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

[**ListBuiltInSlotTypesResponse**](ListBuiltInSlotTypesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listCustomVocabularyItems

> ListCustomVocabularyItemsResponse listCustomVocabularyItems(botId, botVersion, localeId, listCustomVocabularyItemsRequest, opts)



Paginated list of custom vocabulary items for a given bot locale&#39;s custom vocabulary.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier of the version of the bot associated with this custom vocabulary.
let botVersion = "botVersion_example"; // String | The bot version of the bot to the list custom vocabulary request.
let localeId = "localeId_example"; // String | The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see Supported languages (https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).
let listCustomVocabularyItemsRequest = new AmazonLexModelBuildingV2.ListCustomVocabularyItemsRequest(); // ListCustomVocabularyItemsRequest | 
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
apiInstance.listCustomVocabularyItems(botId, botVersion, localeId, listCustomVocabularyItemsRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier of the version of the bot associated with this custom vocabulary. | 
 **botVersion** | **String**| The bot version of the bot to the list custom vocabulary request. | 
 **localeId** | **String**| The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see Supported languages (https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html). | 
 **listCustomVocabularyItemsRequest** | [**ListCustomVocabularyItemsRequest**](ListCustomVocabularyItemsRequest.md)|  | 
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

[**ListCustomVocabularyItemsResponse**](ListCustomVocabularyItemsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listExports

> ListExportsResponse listExports(listExportsRequest, opts)



Lists the exports for a bot, bot locale, or custom vocabulary. Exports are kept in the list for 7 days.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let listExportsRequest = new AmazonLexModelBuildingV2.ListExportsRequest(); // ListExportsRequest | 
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
apiInstance.listExports(listExportsRequest, opts, (error, data, response) => {
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
 **listExportsRequest** | [**ListExportsRequest**](ListExportsRequest.md)|  | 
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

[**ListExportsResponse**](ListExportsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listImports

> ListImportsResponse listImports(listImportsRequest, opts)



Lists the imports for a bot, bot locale, or custom vocabulary. Imports are kept in the list for 7 days.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let listImportsRequest = new AmazonLexModelBuildingV2.ListImportsRequest(); // ListImportsRequest | 
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
apiInstance.listImports(listImportsRequest, opts, (error, data, response) => {
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
 **listImportsRequest** | [**ListImportsRequest**](ListImportsRequest.md)|  | 
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

[**ListImportsResponse**](ListImportsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listIntentMetrics

> ListIntentMetricsResponse listIntentMetrics(botId, listIntentMetricsRequest, opts)



&lt;p&gt;Retrieves summary metrics for the intents in your bot. The following fields are required:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;metrics&lt;/code&gt; – A list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsIntentMetric.html\&quot;&gt;AnalyticsIntentMetric&lt;/a&gt; objects. In each object, use the &lt;code&gt;name&lt;/code&gt; field to specify the metric to calculate, the &lt;code&gt;statistic&lt;/code&gt; field to specify whether to calculate the &lt;code&gt;Sum&lt;/code&gt;, &lt;code&gt;Average&lt;/code&gt;, or &lt;code&gt;Max&lt;/code&gt; number, and the &lt;code&gt;order&lt;/code&gt; field to specify whether to sort the results in &lt;code&gt;Ascending&lt;/code&gt; or &lt;code&gt;Descending&lt;/code&gt; order.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;startDateTime&lt;/code&gt; and &lt;code&gt;endDateTime&lt;/code&gt; – Define a time range for which you want to retrieve results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Of the optional fields, you can organize the results in the following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;filters&lt;/code&gt; field to filter the results, the &lt;code&gt;groupBy&lt;/code&gt; field to specify categories by which to group the results, and the &lt;code&gt;binBy&lt;/code&gt; field to specify time intervals by which to group the results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;maxResults&lt;/code&gt; field to limit the number of results to return in a single response and the &lt;code&gt;nextToken&lt;/code&gt; field to return the next batch of results if the response does not return the full set of results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Note that an &lt;code&gt;order&lt;/code&gt; field exists in both &lt;code&gt;binBy&lt;/code&gt; and &lt;code&gt;metrics&lt;/code&gt;. You can specify only one &lt;code&gt;order&lt;/code&gt; in a given request.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier for the bot for which you want to retrieve intent metrics.
let listIntentMetricsRequest = new AmazonLexModelBuildingV2.ListIntentMetricsRequest(); // ListIntentMetricsRequest | 
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
apiInstance.listIntentMetrics(botId, listIntentMetricsRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier for the bot for which you want to retrieve intent metrics. | 
 **listIntentMetricsRequest** | [**ListIntentMetricsRequest**](ListIntentMetricsRequest.md)|  | 
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

[**ListIntentMetricsResponse**](ListIntentMetricsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listIntentPaths

> ListIntentPathsResponse listIntentPaths(botId, listIntentPathsRequest, opts)



&lt;p&gt;Retrieves summary statistics for a path of intents that users take over sessions with your bot. The following fields are required:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;startDateTime&lt;/code&gt; and &lt;code&gt;endDateTime&lt;/code&gt; – Define a time range for which you want to retrieve results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;intentPath&lt;/code&gt; – Define an order of intents for which you want to retrieve metrics. Separate intents in the path with a forward slash. For example, populate the &lt;code&gt;intentPath&lt;/code&gt; field with &lt;code&gt;/BookCar/BookHotel&lt;/code&gt; to see details about how many times users invoked the &lt;code&gt;BookCar&lt;/code&gt; and &lt;code&gt;BookHotel&lt;/code&gt; intents in that order.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Use the optional &lt;code&gt;filters&lt;/code&gt; field to filter the results.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier for the bot for which you want to retrieve intent path metrics.
let listIntentPathsRequest = new AmazonLexModelBuildingV2.ListIntentPathsRequest(); // ListIntentPathsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listIntentPaths(botId, listIntentPathsRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier for the bot for which you want to retrieve intent path metrics. | 
 **listIntentPathsRequest** | [**ListIntentPathsRequest**](ListIntentPathsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListIntentPathsResponse**](ListIntentPathsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listIntentStageMetrics

> ListIntentStageMetricsResponse listIntentStageMetrics(botId, listIntentStageMetricsRequest, opts)



&lt;p&gt;Retrieves summary metrics for the stages within intents in your bot. The following fields are required:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;metrics&lt;/code&gt; – A list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsIntentStageMetric.html\&quot;&gt;AnalyticsIntentStageMetric&lt;/a&gt; objects. In each object, use the &lt;code&gt;name&lt;/code&gt; field to specify the metric to calculate, the &lt;code&gt;statistic&lt;/code&gt; field to specify whether to calculate the &lt;code&gt;Sum&lt;/code&gt;, &lt;code&gt;Average&lt;/code&gt;, or &lt;code&gt;Max&lt;/code&gt; number, and the &lt;code&gt;order&lt;/code&gt; field to specify whether to sort the results in &lt;code&gt;Ascending&lt;/code&gt; or &lt;code&gt;Descending&lt;/code&gt; order.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;startDateTime&lt;/code&gt; and &lt;code&gt;endDateTime&lt;/code&gt; – Define a time range for which you want to retrieve results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Of the optional fields, you can organize the results in the following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;filters&lt;/code&gt; field to filter the results, the &lt;code&gt;groupBy&lt;/code&gt; field to specify categories by which to group the results, and the &lt;code&gt;binBy&lt;/code&gt; field to specify time intervals by which to group the results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;maxResults&lt;/code&gt; field to limit the number of results to return in a single response and the &lt;code&gt;nextToken&lt;/code&gt; field to return the next batch of results if the response does not return the full set of results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Note that an &lt;code&gt;order&lt;/code&gt; field exists in both &lt;code&gt;binBy&lt;/code&gt; and &lt;code&gt;metrics&lt;/code&gt;. You can only specify one &lt;code&gt;order&lt;/code&gt; in a given request.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier for the bot for which you want to retrieve intent stage metrics.
let listIntentStageMetricsRequest = new AmazonLexModelBuildingV2.ListIntentStageMetricsRequest(); // ListIntentStageMetricsRequest | 
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
apiInstance.listIntentStageMetrics(botId, listIntentStageMetricsRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier for the bot for which you want to retrieve intent stage metrics. | 
 **listIntentStageMetricsRequest** | [**ListIntentStageMetricsRequest**](ListIntentStageMetricsRequest.md)|  | 
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

[**ListIntentStageMetricsResponse**](ListIntentStageMetricsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listIntents

> ListIntentsResponse listIntents(botId, botVersion, localeId, listIntentsRequest, opts)



Get a list of intents that meet the specified criteria.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The unique identifier of the bot that contains the intent.
let botVersion = "botVersion_example"; // String | The version of the bot that contains the intent.
let localeId = "localeId_example"; // String | The identifier of the language and locale of the intents to list. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
let listIntentsRequest = new AmazonLexModelBuildingV2.ListIntentsRequest(); // ListIntentsRequest | 
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
apiInstance.listIntents(botId, botVersion, localeId, listIntentsRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The unique identifier of the bot that contains the intent. | 
 **botVersion** | **String**| The version of the bot that contains the intent. | 
 **localeId** | **String**| The identifier of the language and locale of the intents to list. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
 **listIntentsRequest** | [**ListIntentsRequest**](ListIntentsRequest.md)|  | 
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

[**ListIntentsResponse**](ListIntentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listRecommendedIntents

> ListRecommendedIntentsResponse listRecommendedIntents(botId, botVersion, localeId, botRecommendationId, listRecommendedIntentsRequest, opts)



Gets a list of recommended intents provided by the bot recommendation that you can use in your bot. Intents in the response are ordered by relevance.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The unique identifier of the bot associated with the recommended intents.
let botVersion = "botVersion_example"; // String | The version of the bot that contains the recommended intents.
let localeId = "localeId_example"; // String | The identifier of the language and locale of the recommended intents.
let botRecommendationId = "botRecommendationId_example"; // String | The identifier of the bot recommendation that contains the recommended intents.
let listRecommendedIntentsRequest = new AmazonLexModelBuildingV2.ListRecommendedIntentsRequest(); // ListRecommendedIntentsRequest | 
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
apiInstance.listRecommendedIntents(botId, botVersion, localeId, botRecommendationId, listRecommendedIntentsRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The unique identifier of the bot associated with the recommended intents. | 
 **botVersion** | **String**| The version of the bot that contains the recommended intents. | 
 **localeId** | **String**| The identifier of the language and locale of the recommended intents. | 
 **botRecommendationId** | **String**| The identifier of the bot recommendation that contains the recommended intents. | 
 **listRecommendedIntentsRequest** | [**ListRecommendedIntentsRequest**](ListRecommendedIntentsRequest.md)|  | 
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

[**ListRecommendedIntentsResponse**](ListRecommendedIntentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listSessionAnalyticsData

> ListSessionAnalyticsDataResponse listSessionAnalyticsData(botId, listSessionAnalyticsDataRequest, opts)



&lt;p&gt;Retrieves a list of metadata for individual user sessions with your bot. The &lt;code&gt;startDateTime&lt;/code&gt; and &lt;code&gt;endDateTime&lt;/code&gt; fields are required. These fields define a time range for which you want to retrieve results. Of the optional fields, you can organize the results in the following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;filters&lt;/code&gt; field to filter the results and the &lt;code&gt;sortBy&lt;/code&gt; field to specify the values by which to sort the results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;maxResults&lt;/code&gt; field to limit the number of results to return in a single response and the &lt;code&gt;nextToken&lt;/code&gt; field to return the next batch of results if the response does not return the full set of results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier for the bot for which you want to retrieve session analytics.
let listSessionAnalyticsDataRequest = new AmazonLexModelBuildingV2.ListSessionAnalyticsDataRequest(); // ListSessionAnalyticsDataRequest | 
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
apiInstance.listSessionAnalyticsData(botId, listSessionAnalyticsDataRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier for the bot for which you want to retrieve session analytics. | 
 **listSessionAnalyticsDataRequest** | [**ListSessionAnalyticsDataRequest**](ListSessionAnalyticsDataRequest.md)|  | 
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

[**ListSessionAnalyticsDataResponse**](ListSessionAnalyticsDataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listSessionMetrics

> ListSessionMetricsResponse listSessionMetrics(botId, listSessionMetricsRequest, opts)



&lt;p&gt;Retrieves summary metrics for the user sessions with your bot. The following fields are required:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;metrics&lt;/code&gt; – A list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsSessionMetric.html\&quot;&gt;AnalyticsSessionMetric&lt;/a&gt; objects. In each object, use the &lt;code&gt;name&lt;/code&gt; field to specify the metric to calculate, the &lt;code&gt;statistic&lt;/code&gt; field to specify whether to calculate the &lt;code&gt;Sum&lt;/code&gt;, &lt;code&gt;Average&lt;/code&gt;, or &lt;code&gt;Max&lt;/code&gt; number, and the &lt;code&gt;order&lt;/code&gt; field to specify whether to sort the results in &lt;code&gt;Ascending&lt;/code&gt; or &lt;code&gt;Descending&lt;/code&gt; order.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;startDateTime&lt;/code&gt; and &lt;code&gt;endDateTime&lt;/code&gt; – Define a time range for which you want to retrieve results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Of the optional fields, you can organize the results in the following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;filters&lt;/code&gt; field to filter the results, the &lt;code&gt;groupBy&lt;/code&gt; field to specify categories by which to group the results, and the &lt;code&gt;binBy&lt;/code&gt; field to specify time intervals by which to group the results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;maxResults&lt;/code&gt; field to limit the number of results to return in a single response and the &lt;code&gt;nextToken&lt;/code&gt; field to return the next batch of results if the response does not return the full set of results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Note that an &lt;code&gt;order&lt;/code&gt; field exists in both &lt;code&gt;binBy&lt;/code&gt; and &lt;code&gt;metrics&lt;/code&gt;. Currently, you can specify it in either field, but not in both.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier for the bot for which you want to retrieve session metrics.
let listSessionMetricsRequest = new AmazonLexModelBuildingV2.ListSessionMetricsRequest(); // ListSessionMetricsRequest | 
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
apiInstance.listSessionMetrics(botId, listSessionMetricsRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier for the bot for which you want to retrieve session metrics. | 
 **listSessionMetricsRequest** | [**ListSessionMetricsRequest**](ListSessionMetricsRequest.md)|  | 
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

[**ListSessionMetricsResponse**](ListSessionMetricsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listSlotTypes

> ListSlotTypesResponse listSlotTypes(botId, botVersion, localeId, listSlotTypesRequest, opts)



Gets a list of slot types that match the specified criteria.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The unique identifier of the bot that contains the slot types.
let botVersion = "botVersion_example"; // String | The version of the bot that contains the slot type.
let localeId = "localeId_example"; // String | The identifier of the language and locale of the slot types to list. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
let listSlotTypesRequest = new AmazonLexModelBuildingV2.ListSlotTypesRequest(); // ListSlotTypesRequest | 
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
apiInstance.listSlotTypes(botId, botVersion, localeId, listSlotTypesRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The unique identifier of the bot that contains the slot types. | 
 **botVersion** | **String**| The version of the bot that contains the slot type. | 
 **localeId** | **String**| The identifier of the language and locale of the slot types to list. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
 **listSlotTypesRequest** | [**ListSlotTypesRequest**](ListSlotTypesRequest.md)|  | 
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

[**ListSlotTypesResponse**](ListSlotTypesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listSlots

> ListSlotsResponse listSlots(botId, botVersion, localeId, intentId, listSlotsRequest, opts)



Gets a list of slots that match the specified criteria.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier of the bot that contains the slot.
let botVersion = "botVersion_example"; // String | The version of the bot that contains the slot.
let localeId = "localeId_example"; // String | The identifier of the language and locale of the slots to list. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
let intentId = "intentId_example"; // String | The unique identifier of the intent that contains the slot.
let listSlotsRequest = new AmazonLexModelBuildingV2.ListSlotsRequest(); // ListSlotsRequest | 
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
apiInstance.listSlots(botId, botVersion, localeId, intentId, listSlotsRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier of the bot that contains the slot. | 
 **botVersion** | **String**| The version of the bot that contains the slot. | 
 **localeId** | **String**| The identifier of the language and locale of the slots to list. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
 **intentId** | **String**| The unique identifier of the intent that contains the slot. | 
 **listSlotsRequest** | [**ListSlotsRequest**](ListSlotsRequest.md)|  | 
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

[**ListSlotsResponse**](ListSlotsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceARN, opts)



Gets a list of tags associated with a resource. Only bots, bot aliases, and bot channels can have tags associated with them.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let resourceARN = "resourceARN_example"; // String | The Amazon Resource Name (ARN) of the resource to get a list of tags for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(resourceARN, opts, (error, data, response) => {
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
 **resourceARN** | **String**| The Amazon Resource Name (ARN) of the resource to get a list of tags for. | 
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


## listTestExecutionResultItems

> ListTestExecutionResultItemsResponse listTestExecutionResultItems(testExecutionId, listTestExecutionResultItemsRequest, opts)



Gets a list of test execution result items.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let testExecutionId = "testExecutionId_example"; // String | The unique identifier of the test execution to list the result items.
let listTestExecutionResultItemsRequest = new AmazonLexModelBuildingV2.ListTestExecutionResultItemsRequest(); // ListTestExecutionResultItemsRequest | 
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
apiInstance.listTestExecutionResultItems(testExecutionId, listTestExecutionResultItemsRequest, opts, (error, data, response) => {
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
 **testExecutionId** | **String**| The unique identifier of the test execution to list the result items. | 
 **listTestExecutionResultItemsRequest** | [**ListTestExecutionResultItemsRequest**](ListTestExecutionResultItemsRequest.md)|  | 
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

[**ListTestExecutionResultItemsResponse**](ListTestExecutionResultItemsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTestExecutions

> ListTestExecutionsResponse listTestExecutions(listTestExecutionsRequest, opts)



The list of test set executions.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let listTestExecutionsRequest = new AmazonLexModelBuildingV2.ListTestExecutionsRequest(); // ListTestExecutionsRequest | 
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
apiInstance.listTestExecutions(listTestExecutionsRequest, opts, (error, data, response) => {
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
 **listTestExecutionsRequest** | [**ListTestExecutionsRequest**](ListTestExecutionsRequest.md)|  | 
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

[**ListTestExecutionsResponse**](ListTestExecutionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTestSetRecords

> ListTestSetRecordsResponse listTestSetRecords(testSetId, listTestSetRecordsRequest, opts)



The list of test set records.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let testSetId = "testSetId_example"; // String | The identifier of the test set to list its test set records.
let listTestSetRecordsRequest = new AmazonLexModelBuildingV2.ListTestSetRecordsRequest(); // ListTestSetRecordsRequest | 
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
apiInstance.listTestSetRecords(testSetId, listTestSetRecordsRequest, opts, (error, data, response) => {
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
 **testSetId** | **String**| The identifier of the test set to list its test set records. | 
 **listTestSetRecordsRequest** | [**ListTestSetRecordsRequest**](ListTestSetRecordsRequest.md)|  | 
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

[**ListTestSetRecordsResponse**](ListTestSetRecordsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTestSets

> ListTestSetsResponse listTestSets(listTestSetsRequest, opts)



The list of the test sets

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let listTestSetsRequest = new AmazonLexModelBuildingV2.ListTestSetsRequest(); // ListTestSetsRequest | 
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
apiInstance.listTestSets(listTestSetsRequest, opts, (error, data, response) => {
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
 **listTestSetsRequest** | [**ListTestSetsRequest**](ListTestSetsRequest.md)|  | 
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

[**ListTestSetsResponse**](ListTestSetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listUtteranceAnalyticsData

> ListUtteranceAnalyticsDataResponse listUtteranceAnalyticsData(botId, listUtteranceAnalyticsDataRequest, opts)



&lt;note&gt; &lt;p&gt;To use this API operation, your IAM role must have permissions to perform the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListAggregatedUtterances.html\&quot;&gt;ListAggregatedUtterances&lt;/a&gt; operation, which provides access to utterance-related analytics. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/monitoring-utterances.html\&quot;&gt;Viewing utterance statistics&lt;/a&gt; for the IAM policy to apply to the IAM role.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Retrieves a list of metadata for individual user utterances to your bot. The following fields are required:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;startDateTime&lt;/code&gt; and &lt;code&gt;endDateTime&lt;/code&gt; – Define a time range for which you want to retrieve results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Of the optional fields, you can organize the results in the following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;filters&lt;/code&gt; field to filter the results and the &lt;code&gt;sortBy&lt;/code&gt; field to specify the values by which to sort the results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;maxResults&lt;/code&gt; field to limit the number of results to return in a single response and the &lt;code&gt;nextToken&lt;/code&gt; field to return the next batch of results if the response does not return the full set of results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier for the bot for which you want to retrieve utterance analytics.
let listUtteranceAnalyticsDataRequest = new AmazonLexModelBuildingV2.ListUtteranceAnalyticsDataRequest(); // ListUtteranceAnalyticsDataRequest | 
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
apiInstance.listUtteranceAnalyticsData(botId, listUtteranceAnalyticsDataRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier for the bot for which you want to retrieve utterance analytics. | 
 **listUtteranceAnalyticsDataRequest** | [**ListUtteranceAnalyticsDataRequest**](ListUtteranceAnalyticsDataRequest.md)|  | 
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

[**ListUtteranceAnalyticsDataResponse**](ListUtteranceAnalyticsDataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listUtteranceMetrics

> ListUtteranceMetricsResponse listUtteranceMetrics(botId, listUtteranceMetricsRequest, opts)



&lt;note&gt; &lt;p&gt;To use this API operation, your IAM role must have permissions to perform the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListAggregatedUtterances.html\&quot;&gt;ListAggregatedUtterances&lt;/a&gt; operation, which provides access to utterance-related analytics. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/monitoring-utterances.html\&quot;&gt;Viewing utterance statistics&lt;/a&gt; for the IAM policy to apply to the IAM role.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Retrieves summary metrics for the utterances in your bot. The following fields are required:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;metrics&lt;/code&gt; – A list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsUtteranceMetric.html\&quot;&gt;AnalyticsUtteranceMetric&lt;/a&gt; objects. In each object, use the &lt;code&gt;name&lt;/code&gt; field to specify the metric to calculate, the &lt;code&gt;statistic&lt;/code&gt; field to specify whether to calculate the &lt;code&gt;Sum&lt;/code&gt;, &lt;code&gt;Average&lt;/code&gt;, or &lt;code&gt;Max&lt;/code&gt; number, and the &lt;code&gt;order&lt;/code&gt; field to specify whether to sort the results in &lt;code&gt;Ascending&lt;/code&gt; or &lt;code&gt;Descending&lt;/code&gt; order.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;startDateTime&lt;/code&gt; and &lt;code&gt;endDateTime&lt;/code&gt; – Define a time range for which you want to retrieve results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Of the optional fields, you can organize the results in the following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;filters&lt;/code&gt; field to filter the results, the &lt;code&gt;groupBy&lt;/code&gt; field to specify categories by which to group the results, and the &lt;code&gt;binBy&lt;/code&gt; field to specify time intervals by which to group the results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;maxResults&lt;/code&gt; field to limit the number of results to return in a single response and the &lt;code&gt;nextToken&lt;/code&gt; field to return the next batch of results if the response does not return the full set of results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Note that an &lt;code&gt;order&lt;/code&gt; field exists in both &lt;code&gt;binBy&lt;/code&gt; and &lt;code&gt;metrics&lt;/code&gt;. Currently, you can specify it in either field, but not in both.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The identifier for the bot for which you want to retrieve utterance metrics.
let listUtteranceMetricsRequest = new AmazonLexModelBuildingV2.ListUtteranceMetricsRequest(); // ListUtteranceMetricsRequest | 
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
apiInstance.listUtteranceMetrics(botId, listUtteranceMetricsRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The identifier for the bot for which you want to retrieve utterance metrics. | 
 **listUtteranceMetricsRequest** | [**ListUtteranceMetricsRequest**](ListUtteranceMetricsRequest.md)|  | 
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

[**ListUtteranceMetricsResponse**](ListUtteranceMetricsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchAssociatedTranscripts

> SearchAssociatedTranscriptsResponse searchAssociatedTranscripts(botId, botVersion, localeId, botRecommendationId, searchAssociatedTranscriptsRequest, opts)



Search for associated transcripts that meet the specified criteria.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The unique identifier of the bot associated with the transcripts that you are searching.
let botVersion = "botVersion_example"; // String | The version of the bot containing the transcripts that you are searching.
let localeId = "localeId_example"; // String | The identifier of the language and locale of the transcripts to search. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a> 
let botRecommendationId = "botRecommendationId_example"; // String | The unique identifier of the bot recommendation associated with the transcripts to search.
let searchAssociatedTranscriptsRequest = new AmazonLexModelBuildingV2.SearchAssociatedTranscriptsRequest(); // SearchAssociatedTranscriptsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.searchAssociatedTranscripts(botId, botVersion, localeId, botRecommendationId, searchAssociatedTranscriptsRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The unique identifier of the bot associated with the transcripts that you are searching. | 
 **botVersion** | **String**| The version of the bot containing the transcripts that you are searching. | 
 **localeId** | **String**| The identifier of the language and locale of the transcripts to search. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;  | 
 **botRecommendationId** | **String**| The unique identifier of the bot recommendation associated with the transcripts to search. | 
 **searchAssociatedTranscriptsRequest** | [**SearchAssociatedTranscriptsRequest**](SearchAssociatedTranscriptsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SearchAssociatedTranscriptsResponse**](SearchAssociatedTranscriptsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startBotRecommendation

> StartBotRecommendationResponse startBotRecommendation(botId, botVersion, localeId, startBotRecommendationRequest, opts)



Use this to provide your transcript data, and to start the bot recommendation process.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The unique identifier of the bot containing the bot recommendation.
let botVersion = "botVersion_example"; // String | The version of the bot containing the bot recommendation.
let localeId = "localeId_example"; // String | The identifier of the language and locale of the bot recommendation to start. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a> 
let startBotRecommendationRequest = new AmazonLexModelBuildingV2.StartBotRecommendationRequest(); // StartBotRecommendationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startBotRecommendation(botId, botVersion, localeId, startBotRecommendationRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The unique identifier of the bot containing the bot recommendation. | 
 **botVersion** | **String**| The version of the bot containing the bot recommendation. | 
 **localeId** | **String**| The identifier of the language and locale of the bot recommendation to start. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;  | 
 **startBotRecommendationRequest** | [**StartBotRecommendationRequest**](StartBotRecommendationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartBotRecommendationResponse**](StartBotRecommendationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startImport

> StartImportResponse startImport(startImportRequest, opts)



Starts importing a bot, bot locale, or custom vocabulary from a zip archive that you uploaded to an S3 bucket.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let startImportRequest = new AmazonLexModelBuildingV2.StartImportRequest(); // StartImportRequest | 
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


## startTestExecution

> StartTestExecutionResponse startTestExecution(testSetId, startTestExecutionRequest, opts)



The action to start test set execution.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let testSetId = "testSetId_example"; // String | The test set Id for the test set execution.
let startTestExecutionRequest = new AmazonLexModelBuildingV2.StartTestExecutionRequest(); // StartTestExecutionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startTestExecution(testSetId, startTestExecutionRequest, opts, (error, data, response) => {
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
 **testSetId** | **String**| The test set Id for the test set execution. | 
 **startTestExecutionRequest** | [**StartTestExecutionRequest**](StartTestExecutionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartTestExecutionResponse**](StartTestExecutionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startTestSetGeneration

> StartTestSetGenerationResponse startTestSetGeneration(startTestSetGenerationRequest, opts)



The action to start the generation of test set.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let startTestSetGenerationRequest = new AmazonLexModelBuildingV2.StartTestSetGenerationRequest(); // StartTestSetGenerationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startTestSetGeneration(startTestSetGenerationRequest, opts, (error, data, response) => {
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
 **startTestSetGenerationRequest** | [**StartTestSetGenerationRequest**](StartTestSetGenerationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartTestSetGenerationResponse**](StartTestSetGenerationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopBotRecommendation

> StopBotRecommendationResponse stopBotRecommendation(botId, botVersion, localeId, botRecommendationId, opts)



Stop an already running Bot Recommendation request.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The unique identifier of the bot containing the bot recommendation to be stopped.
let botVersion = "botVersion_example"; // String | The version of the bot containing the bot recommendation.
let localeId = "localeId_example"; // String | The identifier of the language and locale of the bot recommendation to stop. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a> 
let botRecommendationId = "botRecommendationId_example"; // String | The unique identifier of the bot recommendation to be stopped.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopBotRecommendation(botId, botVersion, localeId, botRecommendationId, opts, (error, data, response) => {
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
 **botId** | **String**| The unique identifier of the bot containing the bot recommendation to be stopped. | 
 **botVersion** | **String**| The version of the bot containing the bot recommendation. | 
 **localeId** | **String**| The identifier of the language and locale of the bot recommendation to stop. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;  | 
 **botRecommendationId** | **String**| The unique identifier of the bot recommendation to be stopped. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StopBotRecommendationResponse**](StopBotRecommendationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagResource

> Object tagResource(resourceARN, tagResourceRequest, opts)



Adds the specified tags to the specified resource. If a tag key already exists, the existing value is replaced with the new value.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let resourceARN = "resourceARN_example"; // String | The Amazon Resource Name (ARN) of the bot, bot alias, or bot channel to tag.
let tagResourceRequest = new AmazonLexModelBuildingV2.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(resourceARN, tagResourceRequest, opts, (error, data, response) => {
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
 **resourceARN** | **String**| The Amazon Resource Name (ARN) of the bot, bot alias, or bot channel to tag. | 
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

> Object untagResource(resourceARN, tagKeys, opts)



Removes tags from a bot, bot alias, or bot channel.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let resourceARN = "resourceARN_example"; // String | The Amazon Resource Name (ARN) of the resource to remove the tags from.
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
apiInstance.untagResource(resourceARN, tagKeys, opts, (error, data, response) => {
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
 **resourceARN** | **String**| The Amazon Resource Name (ARN) of the resource to remove the tags from. | 
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


## updateBot

> UpdateBotResponse updateBot(botId, updateBotRequest, opts)



Updates the configuration of an existing bot. 

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The unique identifier of the bot to update. This identifier is returned by the <a href=\"https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html\">CreateBot</a> operation.
let updateBotRequest = new AmazonLexModelBuildingV2.UpdateBotRequest(); // UpdateBotRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateBot(botId, updateBotRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The unique identifier of the bot to update. This identifier is returned by the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html\&quot;&gt;CreateBot&lt;/a&gt; operation. | 
 **updateBotRequest** | [**UpdateBotRequest**](UpdateBotRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateBotResponse**](UpdateBotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateBotAlias

> UpdateBotAliasResponse updateBotAlias(botAliasId, botId, updateBotAliasRequest, opts)



Updates the configuration of an existing bot alias.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botAliasId = "botAliasId_example"; // String | The unique identifier of the bot alias.
let botId = "botId_example"; // String | The identifier of the bot with the updated alias.
let updateBotAliasRequest = new AmazonLexModelBuildingV2.UpdateBotAliasRequest(); // UpdateBotAliasRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateBotAlias(botAliasId, botId, updateBotAliasRequest, opts, (error, data, response) => {
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
 **botAliasId** | **String**| The unique identifier of the bot alias. | 
 **botId** | **String**| The identifier of the bot with the updated alias. | 
 **updateBotAliasRequest** | [**UpdateBotAliasRequest**](UpdateBotAliasRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateBotAliasResponse**](UpdateBotAliasResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateBotLocale

> UpdateBotLocaleResponse updateBotLocale(botId, botVersion, localeId, updateBotLocaleRequest, opts)



Updates the settings that a bot has for a specific locale.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The unique identifier of the bot that contains the locale.
let botVersion = "botVersion_example"; // String | The version of the bot that contains the locale to be updated. The version can only be the <code>DRAFT</code> version.
let localeId = "localeId_example"; // String | The identifier of the language and locale to update. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
let updateBotLocaleRequest = new AmazonLexModelBuildingV2.UpdateBotLocaleRequest(); // UpdateBotLocaleRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateBotLocale(botId, botVersion, localeId, updateBotLocaleRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The unique identifier of the bot that contains the locale. | 
 **botVersion** | **String**| The version of the bot that contains the locale to be updated. The version can only be the &lt;code&gt;DRAFT&lt;/code&gt; version. | 
 **localeId** | **String**| The identifier of the language and locale to update. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
 **updateBotLocaleRequest** | [**UpdateBotLocaleRequest**](UpdateBotLocaleRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateBotLocaleResponse**](UpdateBotLocaleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateBotRecommendation

> UpdateBotRecommendationResponse updateBotRecommendation(botId, botVersion, localeId, botRecommendationId, updateBotRecommendationRequest, opts)



Updates an existing bot recommendation request.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let botId = "botId_example"; // String | The unique identifier of the bot containing the bot recommendation to be updated.
let botVersion = "botVersion_example"; // String | The version of the bot containing the bot recommendation to be updated.
let localeId = "localeId_example"; // String | The identifier of the language and locale of the bot recommendation to update. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a> 
let botRecommendationId = "botRecommendationId_example"; // String | The unique identifier of the bot recommendation to be updated.
let updateBotRecommendationRequest = new AmazonLexModelBuildingV2.UpdateBotRecommendationRequest(); // UpdateBotRecommendationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateBotRecommendation(botId, botVersion, localeId, botRecommendationId, updateBotRecommendationRequest, opts, (error, data, response) => {
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
 **botId** | **String**| The unique identifier of the bot containing the bot recommendation to be updated. | 
 **botVersion** | **String**| The version of the bot containing the bot recommendation to be updated. | 
 **localeId** | **String**| The identifier of the language and locale of the bot recommendation to update. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;  | 
 **botRecommendationId** | **String**| The unique identifier of the bot recommendation to be updated. | 
 **updateBotRecommendationRequest** | [**UpdateBotRecommendationRequest**](UpdateBotRecommendationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateBotRecommendationResponse**](UpdateBotRecommendationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateExport

> UpdateExportResponse updateExport(exportId, updateExportRequest, opts)



&lt;p&gt;Updates the password used to protect an export zip archive.&lt;/p&gt; &lt;p&gt;The password is not required. If you don&#39;t supply a password, Amazon Lex generates a zip file that is not protected by a password. This is the archive that is available at the pre-signed S3 URL provided by the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeExport.html\&quot;&gt;DescribeExport&lt;/a&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let exportId = "exportId_example"; // String | The unique identifier Amazon Lex assigned to the export.
let updateExportRequest = new AmazonLexModelBuildingV2.UpdateExportRequest(); // UpdateExportRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateExport(exportId, updateExportRequest, opts, (error, data, response) => {
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
 **exportId** | **String**| The unique identifier Amazon Lex assigned to the export. | 
 **updateExportRequest** | [**UpdateExportRequest**](UpdateExportRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateExportResponse**](UpdateExportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateIntent

> UpdateIntentResponse updateIntent(intentId, botId, botVersion, localeId, updateIntentRequest, opts)



Updates the settings for an intent.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let intentId = "intentId_example"; // String | The unique identifier of the intent to update.
let botId = "botId_example"; // String | The identifier of the bot that contains the intent.
let botVersion = "botVersion_example"; // String | The version of the bot that contains the intent. Must be <code>DRAFT</code>.
let localeId = "localeId_example"; // String | The identifier of the language and locale where this intent is used. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
let updateIntentRequest = new AmazonLexModelBuildingV2.UpdateIntentRequest(); // UpdateIntentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateIntent(intentId, botId, botVersion, localeId, updateIntentRequest, opts, (error, data, response) => {
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
 **intentId** | **String**| The unique identifier of the intent to update. | 
 **botId** | **String**| The identifier of the bot that contains the intent. | 
 **botVersion** | **String**| The version of the bot that contains the intent. Must be &lt;code&gt;DRAFT&lt;/code&gt;. | 
 **localeId** | **String**| The identifier of the language and locale where this intent is used. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
 **updateIntentRequest** | [**UpdateIntentRequest**](UpdateIntentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateIntentResponse**](UpdateIntentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateResourcePolicy

> UpdateResourcePolicyResponse updateResourcePolicy(resourceArn, updateResourcePolicyRequest, opts)



Replaces the existing resource policy for a bot or bot alias with a new one. If the policy doesn&#39;t exist, Amazon Lex returns an exception.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.
let updateResourcePolicyRequest = new AmazonLexModelBuildingV2.UpdateResourcePolicyRequest(); // UpdateResourcePolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'expectedRevisionId': "expectedRevisionId_example" // String | <p>The identifier of the revision of the policy to update. If this revision ID doesn't match the current revision ID, Amazon Lex throws an exception.</p> <p>If you don't specify a revision, Amazon Lex overwrites the contents of the policy with the new values.</p>
};
apiInstance.updateResourcePolicy(resourceArn, updateResourcePolicyRequest, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to. | 
 **updateResourcePolicyRequest** | [**UpdateResourcePolicyRequest**](UpdateResourcePolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **expectedRevisionId** | **String**| &lt;p&gt;The identifier of the revision of the policy to update. If this revision ID doesn&#39;t match the current revision ID, Amazon Lex throws an exception.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a revision, Amazon Lex overwrites the contents of the policy with the new values.&lt;/p&gt; | [optional] 

### Return type

[**UpdateResourcePolicyResponse**](UpdateResourcePolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSlot

> UpdateSlotResponse updateSlot(slotId, botId, botVersion, localeId, intentId, updateSlotRequest, opts)



Updates the settings for a slot.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let slotId = "slotId_example"; // String | The unique identifier for the slot to update.
let botId = "botId_example"; // String | The unique identifier of the bot that contains the slot.
let botVersion = "botVersion_example"; // String | The version of the bot that contains the slot. Must always be <code>DRAFT</code>.
let localeId = "localeId_example"; // String | The identifier of the language and locale that contains the slot. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
let intentId = "intentId_example"; // String | The identifier of the intent that contains the slot.
let updateSlotRequest = new AmazonLexModelBuildingV2.UpdateSlotRequest(); // UpdateSlotRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSlot(slotId, botId, botVersion, localeId, intentId, updateSlotRequest, opts, (error, data, response) => {
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
 **slotId** | **String**| The unique identifier for the slot to update. | 
 **botId** | **String**| The unique identifier of the bot that contains the slot. | 
 **botVersion** | **String**| The version of the bot that contains the slot. Must always be &lt;code&gt;DRAFT&lt;/code&gt;. | 
 **localeId** | **String**| The identifier of the language and locale that contains the slot. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
 **intentId** | **String**| The identifier of the intent that contains the slot. | 
 **updateSlotRequest** | [**UpdateSlotRequest**](UpdateSlotRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateSlotResponse**](UpdateSlotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSlotType

> UpdateSlotTypeResponse updateSlotType(slotTypeId, botId, botVersion, localeId, updateSlotTypeRequest, opts)



Updates the configuration of an existing slot type.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let slotTypeId = "slotTypeId_example"; // String | The unique identifier of the slot type to update.
let botId = "botId_example"; // String | The identifier of the bot that contains the slot type.
let botVersion = "botVersion_example"; // String | The version of the bot that contains the slot type. Must be <code>DRAFT</code>.
let localeId = "localeId_example"; // String | The identifier of the language and locale that contains the slot type. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
let updateSlotTypeRequest = new AmazonLexModelBuildingV2.UpdateSlotTypeRequest(); // UpdateSlotTypeRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSlotType(slotTypeId, botId, botVersion, localeId, updateSlotTypeRequest, opts, (error, data, response) => {
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
 **slotTypeId** | **String**| The unique identifier of the slot type to update. | 
 **botId** | **String**| The identifier of the bot that contains the slot type. | 
 **botVersion** | **String**| The version of the bot that contains the slot type. Must be &lt;code&gt;DRAFT&lt;/code&gt;. | 
 **localeId** | **String**| The identifier of the language and locale that contains the slot type. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
 **updateSlotTypeRequest** | [**UpdateSlotTypeRequest**](UpdateSlotTypeRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateSlotTypeResponse**](UpdateSlotTypeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTestSet

> UpdateTestSetResponse updateTestSet(testSetId, updateTestSetRequest, opts)



The action to update the test set.

### Example

```javascript
import AmazonLexModelBuildingV2 from 'amazon_lex_model_building_v2';
let defaultClient = AmazonLexModelBuildingV2.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonLexModelBuildingV2.DefaultApi();
let testSetId = "testSetId_example"; // String | The test set Id for which update test operation to be performed.
let updateTestSetRequest = new AmazonLexModelBuildingV2.UpdateTestSetRequest(); // UpdateTestSetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateTestSet(testSetId, updateTestSetRequest, opts, (error, data, response) => {
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
 **testSetId** | **String**| The test set Id for which update test operation to be performed. | 
 **updateTestSetRequest** | [**UpdateTestSetRequest**](UpdateTestSetRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateTestSetResponse**](UpdateTestSetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

